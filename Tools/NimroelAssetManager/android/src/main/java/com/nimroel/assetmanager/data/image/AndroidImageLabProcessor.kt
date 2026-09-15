package com.nimroel.assetmanager.data.image

import android.annotation.SuppressLint
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix
import android.os.Build
import androidx.exifinterface.media.ExifInterface
import com.nimroel.assetmanager.domain.processing.ImageDimensions
import com.nimroel.assetmanager.domain.processing.ImageLabArtifactRef
import com.nimroel.assetmanager.domain.processing.ImageLabException
import com.nimroel.assetmanager.domain.processing.ImageLabExifStatus
import com.nimroel.assetmanager.domain.processing.ImageLabMetrics
import com.nimroel.assetmanager.domain.processing.ImageLabProcessor
import com.nimroel.assetmanager.domain.processing.ImageLabRequest
import com.nimroel.assetmanager.domain.processing.ImageLabResize
import com.nimroel.assetmanager.domain.processing.ImageLabResult
import java.io.File
import java.io.FileInputStream
import java.io.FileNotFoundException
import java.io.FileOutputStream
import java.io.IOException
import java.nio.file.AtomicMoveNotSupportedException
import java.nio.file.FileVisitResult
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.SimpleFileVisitor
import java.nio.file.StandardCopyOption
import java.nio.file.attribute.BasicFileAttributes
import java.util.UUID
import java.util.concurrent.ConcurrentHashMap
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.currentCoroutineContext
import kotlinx.coroutines.ensureActive
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

/** Optional synchronization point used only by deterministic processor tests. */
internal fun interface ImageLabBeforePromotionHook {
    suspend fun beforePromotion()
}

/** Android platform-codec implementation for disposable, non-canonical experiments. */
class AndroidImageLabProcessor internal constructor(
    private val managedRoot: File,
    private val cacheRoot: File,
    private val afterTemporaryWrittenHook: suspend (File) -> Unit = {},
    private val beforePromotionHook: ImageLabBeforePromotionHook = ImageLabBeforePromotionHook {},
) : ImageLabProcessor, ImageLabPreviewLoader {
    constructor(context: Context) : this(
        managedRoot = File(context.applicationContext.filesDir, MANAGED_ROOT_NAME),
        cacheRoot = File(context.applicationContext.cacheDir, LAB_ROOT_NAME),
    )

    private val artifacts = ConcurrentHashMap<String, Artifact>()
    private val workMutexes = ConcurrentHashMap<String, Mutex>()

    override suspend fun generate(request: ImageLabRequest): ImageLabResult {
        currentCoroutineContext().ensureActive()
        val workId = request.source.workId
        return mutexFor(workId).withLock { generateLocked(request) }
    }

    private suspend fun generateLocked(request: ImageLabRequest): ImageLabResult {
        currentCoroutineContext().ensureActive()
        val source = resolveStagedSource(request)
        validateSupportedSource(source, request.source.content.mimeType)
        val sourceBytes = request.source.content.byteSize
        if (sourceBytes == null || sourceBytes <= 0L || source.length() != sourceBytes) {
            throw ImageLabException("El staged source no tiene un tamaño válido o cambió después de verificarse.")
        }

        val sourceDimensions = readSourceDimensions(source, request)
        val exif = readExifOrientation(source)
        val orientedSourceDimensions = orientedDimensions(
            sourceDimensions.widthPx,
            sourceDimensions.heightPx,
            exif.orientation,
        )
        val profile = request.profile
        val resultDimensions = ImageLabResize.fit(
            orientedSourceDimensions.widthPx,
            orientedSourceDimensions.heightPx,
            profile.targetLongEdge,
        )
        val workDirectory = resolveWorkDirectory(request.source.workId)
        if (!workDirectory.isDirectory && !workDirectory.mkdirs()) {
            throw ImageLabException("No se pudo preparar el cache temporal del laboratorio.")
        }
        val target = File(workDirectory, "long${profile.targetLongEdge}-q${profile.quality}.webp")
        val temporary = File(workDirectory, ".${target.name}.${UUID.randomUUID()}.part")

        var decoded: Bitmap? = null
        var oriented: Bitmap? = null
        var scaled: Bitmap? = null
        try {
            val sampleSize = sampleSizeFor(
                sourceDimensions.widthPx,
                sourceDimensions.heightPx,
                profile.targetLongEdge,
            )
            val decodedBitmap = BitmapFactory.decodeFile(
                source.absolutePath,
                BitmapFactory.Options().apply {
                    inSampleSize = sampleSize
                    inPreferredConfig = Bitmap.Config.ARGB_8888
                },
            ) ?: throw ImageLabException("Android no pudo decodificar el staged source.")
            decoded = decodedBitmap
            currentCoroutineContext().ensureActive()

            val orientedBitmap = applyExifOrientation(decodedBitmap, exif.orientation)
            oriented = orientedBitmap
            if (orientedBitmap !== decodedBitmap) {
                decodedBitmap.recycle()
                decoded = null
            }
            val sourceHasAlphaCapability = orientedBitmap.hasAlpha()
            val transparentPixelsObserved = sourceHasAlphaCapability && containsTransparentPixel(orientedBitmap)
            currentCoroutineContext().ensureActive()

            val scaledBitmap = if (
                orientedBitmap.width == resultDimensions.widthPx && orientedBitmap.height == resultDimensions.heightPx
            ) {
                orientedBitmap
            } else {
                Bitmap.createScaledBitmap(
                    orientedBitmap,
                    resultDimensions.widthPx,
                    resultDimensions.heightPx,
                    true,
                )
            }
            scaled = scaledBitmap
            if (scaledBitmap !== orientedBitmap) {
                orientedBitmap.recycle()
                oriented = null
            }

            writeWebp(scaledBitmap, profile.quality, temporary)
            scaledBitmap.recycle()
            scaled = null
            afterTemporaryWrittenHook(temporary)
            val resultBytes = validateTemporary(
                temporary = temporary,
                expectedDimensions = resultDimensions,
                transparentPixelsExpected = transparentPixelsObserved,
            )

            // The previous target remains untouched through all processing and validation.
            currentCoroutineContext().ensureActive()
            beforePromotionHook.beforePromotion()
            currentCoroutineContext().ensureActive()
            promoteWithRollback(temporary, target)

            // No cancellable operation belongs between successful promotion and publication.
            val token = UUID.randomUUID().toString()
            artifacts.entries.removeAll { it.value.file == target }
            artifacts[token] = Artifact(request.source.workId, target)
            return ImageLabResult(
                workId = request.source.workId,
                mimeType = ImageLabResult.MIME_WEBP,
                widthPx = resultDimensions.widthPx,
                heightPx = resultDimensions.heightPx,
                byteSize = resultBytes,
                requestedTargetLongEdge = profile.targetLongEdge,
                quality = profile.quality,
                reduction = ImageLabMetrics.reduction(sourceBytes, resultBytes),
                sourceHasAlphaCapability = sourceHasAlphaCapability,
                transparentPixelsObserved = transparentPixelsObserved,
                orientationApplied = exif.orientation.requiresTransform(),
                exifStatus = exif.status,
                artifactRef = ImageLabArtifactRef(token),
            )
        } catch (error: CancellationException) {
            throw error
        } catch (error: ImageLabException) {
            throw error
        } catch (error: OutOfMemoryError) {
            throw ImageLabException("Memoria insuficiente al procesar la imagen. Prueba un lado largo menor.", error)
        } catch (error: Exception) {
            throw ImageLabException("No se pudo generar la prueba WebP temporal.", error)
        } finally {
            // This invocation owns only its UUID-scoped temporary; never delete target here.
            temporary.delete()
            recycleDistinct(scaled, oriented, decoded)
        }
    }

    override suspend fun clear(workId: String) {
        requireSafeWorkId(workId)
        mutexFor(workId).withLock {
            val directory = resolveWorkDirectory(workId)
            artifacts.entries.removeAll { it.value.workId == workId }
            if (directory.exists()) deleteDirectoryWithoutFollowingLinks(directory)
            if (directory.exists()) {
                throw ImageLabException("No se pudieron eliminar todas las pruebas temporales.")
            }
        }
    }

    override suspend fun load(
        artifactRef: ImageLabArtifactRef,
        maxLongEdge: Int,
    ): ImageLabPreviewLoadResult {
        if (maxLongEdge <= 0) return ImageLabPreviewLoadResult.Error("El límite de preview no es válido.")
        return try {
            val initial = artifacts[artifactRef.value] ?: return ImageLabPreviewLoadResult.Unavailable
            mutexFor(initial.workId).withLock {
                val artifact = artifacts[artifactRef.value]
                    ?: return@withLock ImageLabPreviewLoadResult.Unavailable
                if (!artifact.file.isFile || !isInside(cacheRoot, artifact.file)) {
                    artifacts.remove(artifactRef.value)
                    return@withLock ImageLabPreviewLoadResult.Unavailable
                }
                val result = decodePreview(artifact.file, maxLongEdge)
                try {
                    currentCoroutineContext().ensureActive()
                    result
                } catch (error: CancellationException) {
                    (result as? ImageLabPreviewLoadResult.Ready)?.bitmap?.recycle()
                    throw error
                }
            }
        } catch (error: CancellationException) {
            throw error
        } catch (_: FileNotFoundException) {
            ImageLabPreviewLoadResult.Unavailable
        } catch (error: IOException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo leer la preview temporal.")
        } catch (error: SecurityException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo acceder a la preview temporal.")
        } catch (_: OutOfMemoryError) {
            ImageLabPreviewLoadResult.Error("Memoria insuficiente para mostrar la preview.")
        } catch (error: RuntimeException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo decodificar la preview temporal.")
        }
    }

    private fun decodePreview(file: File, maxLongEdge: Int): ImageLabPreviewLoadResult {
        var decoded: Bitmap? = null
        return try {
            val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
            FileInputStream(file).use { BitmapFactory.decodeStream(it, null, bounds) }
            if (bounds.outWidth <= 0 || bounds.outHeight <= 0) {
                return ImageLabPreviewLoadResult.Error("La prueba temporal no contiene una imagen válida.")
            }
            var sample = 1
            while (maxOf(bounds.outWidth, bounds.outHeight) / (sample * 2) >= maxLongEdge) sample *= 2
            decoded = FileInputStream(file).use { input ->
                BitmapFactory.decodeStream(
                    input,
                    null,
                    BitmapFactory.Options().apply {
                        inSampleSize = sample
                        inPreferredConfig = Bitmap.Config.ARGB_8888
                    },
                )
            } ?: return ImageLabPreviewLoadResult.Error("Android no pudo decodificar la preview temporal.")
            val bitmap = requireNotNull(decoded)
            val fitted = ImageLabResize.fit(bitmap.width, bitmap.height, maxLongEdge)
            if (bitmap.width == fitted.widthPx && bitmap.height == fitted.heightPx) {
                decoded = null
                ImageLabPreviewLoadResult.Ready(bitmap)
            } else {
                val downscaled = Bitmap.createScaledBitmap(bitmap, fitted.widthPx, fitted.heightPx, true)
                bitmap.recycle()
                decoded = null
                ImageLabPreviewLoadResult.Ready(downscaled)
            }
        } catch (_: FileNotFoundException) {
            ImageLabPreviewLoadResult.Unavailable
        } catch (error: IOException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo leer la preview temporal.")
        } catch (error: SecurityException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo acceder a la preview temporal.")
        } catch (_: OutOfMemoryError) {
            ImageLabPreviewLoadResult.Error("Memoria insuficiente para mostrar la preview.")
        } catch (error: RuntimeException) {
            ImageLabPreviewLoadResult.Error(error.message ?: "No se pudo decodificar la preview temporal.")
        } finally {
            decoded?.takeUnless(Bitmap::isRecycled)?.recycle()
        }
    }

    private fun readSourceDimensions(source: File, request: ImageLabRequest): ImageDimensions {
        val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
        BitmapFactory.decodeFile(source.absolutePath, bounds)
        if (bounds.outWidth <= 0 || bounds.outHeight <= 0) {
            throw ImageLabException("El staged source no contiene un raster decodificable.")
        }
        if (
            bounds.outWidth != request.source.content.widthPx ||
            bounds.outHeight != request.source.content.heightPx
        ) {
            throw ImageLabException("Las dimensiones del staged source cambiaron después de verificarse.")
        }
        return ImageDimensions(bounds.outWidth, bounds.outHeight)
    }

    private suspend fun validateTemporary(
        temporary: File,
        expectedDimensions: ImageDimensions,
        transparentPixelsExpected: Boolean,
    ): Long {
        if (!temporary.isFile || temporary.length() <= 0L) {
            throw ImageLabException("El encoder no produjo un WebP temporal válido.")
        }
        val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
        FileInputStream(temporary).use { BitmapFactory.decodeStream(it, null, bounds) }
        if (
            bounds.outMimeType?.normalizeImageMimeAlias() != ImageLabResult.MIME_WEBP ||
            bounds.outWidth != expectedDimensions.widthPx ||
            bounds.outHeight != expectedDimensions.heightPx
        ) {
            throw ImageLabException("El WebP temporal generado no superó la verificación.")
        }
        if (transparentPixelsExpected) {
            val verification = FileInputStream(temporary).use { BitmapFactory.decodeStream(it) }
                ?: throw ImageLabException("No se pudo verificar el alpha del WebP temporal.")
            try {
                if (!verification.hasAlpha() || !containsTransparentPixel(verification)) {
                    throw ImageLabException("El encoder no conservó la transparencia observada; la prueba se descartó.")
                }
            } finally {
                verification.recycle()
            }
        }
        return temporary.length()
    }

    private fun resolveStagedSource(request: ImageLabRequest): File {
        val source = File(managedRoot, request.source.relativePath)
        if (!source.isFile || !isInside(managedRoot, source)) {
            throw ImageLabException("El staged source privado ya no está disponible.")
        }
        return source
    }

    private fun resolveWorkDirectory(workId: String): File {
        requireSafeWorkId(workId)
        val directory = File(cacheRoot, workId)
        check(isInside(cacheRoot, directory)) { "Image Lab cache escaped its managed root." }
        if (Files.isSymbolicLink(directory.toPath())) {
            throw ImageLabException("El directorio temporal del laboratorio no puede ser un enlace simbólico.")
        }
        return directory
    }

    private fun deleteDirectoryWithoutFollowingLinks(directory: File) {
        try {
            Files.walkFileTree(
                directory.toPath(),
                object : SimpleFileVisitor<Path>() {
                    override fun visitFile(file: Path, attrs: BasicFileAttributes): FileVisitResult {
                        Files.deleteIfExists(file)
                        return FileVisitResult.CONTINUE
                    }

                    override fun postVisitDirectory(dir: Path, error: IOException?): FileVisitResult {
                        if (error != null) throw error
                        Files.deleteIfExists(dir)
                        return FileVisitResult.CONTINUE
                    }
                },
            )
        } catch (error: IOException) {
            throw ImageLabException("No se pudieron eliminar todas las pruebas temporales.", error)
        }
    }

    private fun validateSupportedSource(source: File, mimeType: String) {
        if (mimeType !in SUPPORTED_MIME_TYPES) {
            throw ImageLabException("El laboratorio v1 sólo admite staged source JPEG, PNG o WebP estático.")
        }
        if (mimeType == "image/webp" && isAnimatedWebp(source)) {
            throw ImageLabException("El laboratorio v1 no procesa WebP animado.")
        }
    }

    @Suppress("DEPRECATION")
    @SuppressLint("NewApi") // Production passes Build.VERSION.SDK_INT; the parameter keeps API 26/30 selection testable.
    internal fun webpFormatFor(apiLevel: Int): Bitmap.CompressFormat =
        if (apiLevel >= Build.VERSION_CODES.R) {
            Bitmap.CompressFormat.WEBP_LOSSY
        } else {
            Bitmap.CompressFormat.WEBP
        }

    private fun writeWebp(bitmap: Bitmap, quality: Int, temporary: File) {
        FileOutputStream(temporary).use { output ->
            if (!bitmap.compress(webpFormatFor(Build.VERSION.SDK_INT), quality, output)) {
                throw ImageLabException("El encoder WebP de Android rechazó la imagen.")
            }
            output.flush()
            output.fd.sync()
        }
    }

    private fun promoteWithRollback(temporary: File, target: File) {
        try {
            Files.move(
                temporary.toPath(),
                target.toPath(),
                StandardCopyOption.ATOMIC_MOVE,
                StandardCopyOption.REPLACE_EXISTING,
            )
            return
        } catch (_: AtomicMoveNotSupportedException) {
            // A rollback copy protects an existing candidate on filesystems without atomic replace.
        } catch (error: IOException) {
            throw ImageLabException("No se pudo publicar el WebP en cache temporal.", error)
        }

        val backup = File(target.parentFile, ".${target.name}.${UUID.randomUUID()}.rollback")
        var backupCreated = false
        try {
            if (target.isFile) {
                Files.copy(target.toPath(), backup.toPath(), StandardCopyOption.REPLACE_EXISTING)
                FileOutputStream(backup, true).use { it.fd.sync() }
                backupCreated = true
            }
            Files.move(temporary.toPath(), target.toPath(), StandardCopyOption.REPLACE_EXISTING)
            backup.delete()
        } catch (error: IOException) {
            if (backupCreated) restoreBackup(backup, target)
            throw ImageLabException("No se pudo publicar el WebP en cache temporal.", error)
        }
    }

    private fun restoreBackup(backup: File, target: File) {
        try {
            Files.move(backup.toPath(), target.toPath(), StandardCopyOption.REPLACE_EXISTING)
        } catch (moveError: IOException) {
            try {
                Files.copy(backup.toPath(), target.toPath(), StandardCopyOption.REPLACE_EXISTING)
                backup.delete()
            } catch (copyError: IOException) {
                moveError.addSuppressed(copyError)
                throw ImageLabException(
                    "Falló la promoción y no se pudo restaurar el candidato anterior; se conservó el rollback.",
                    moveError,
                )
            }
        }
    }

    private fun readExifOrientation(source: File): ExifReadResult {
        return try {
            val exif = ExifInterface(source)
            if (!exif.hasAttribute(ExifInterface.TAG_ORIENTATION)) {
                ExifReadResult(ExifInterface.ORIENTATION_NORMAL, ImageLabExifStatus.ABSENT)
            } else {
                val orientation = exif.getAttributeInt(
                    ExifInterface.TAG_ORIENTATION,
                    ExifInterface.ORIENTATION_UNDEFINED,
                )
                if (orientation == ExifInterface.ORIENTATION_UNDEFINED) {
                    ExifReadResult(ExifInterface.ORIENTATION_NORMAL, ImageLabExifStatus.ABSENT)
                } else if (orientation in VALID_EXIF_ORIENTATIONS) {
                    ExifReadResult(
                        orientation,
                        if (orientation.requiresTransform()) {
                            ImageLabExifStatus.TRANSFORMED
                        } else {
                            ImageLabExifStatus.NORMAL
                        },
                    )
                } else {
                    ExifReadResult(ExifInterface.ORIENTATION_NORMAL, ImageLabExifStatus.UNREADABLE)
                }
            }
        } catch (_: IOException) {
            ExifReadResult(ExifInterface.ORIENTATION_NORMAL, ImageLabExifStatus.UNREADABLE)
        } catch (_: RuntimeException) {
            ExifReadResult(ExifInterface.ORIENTATION_NORMAL, ImageLabExifStatus.UNREADABLE)
        }
    }

    internal fun applyExifOrientation(source: Bitmap, orientation: Int): Bitmap {
        val matrix = Matrix()
        when (orientation) {
            ExifInterface.ORIENTATION_FLIP_HORIZONTAL -> matrix.setScale(-1f, 1f)
            ExifInterface.ORIENTATION_ROTATE_180 -> matrix.setRotate(180f)
            ExifInterface.ORIENTATION_FLIP_VERTICAL -> matrix.setScale(1f, -1f)
            ExifInterface.ORIENTATION_TRANSPOSE -> {
                matrix.setRotate(90f)
                matrix.postScale(-1f, 1f)
            }
            ExifInterface.ORIENTATION_ROTATE_90 -> matrix.setRotate(90f)
            ExifInterface.ORIENTATION_TRANSVERSE -> {
                matrix.setRotate(-90f)
                matrix.postScale(-1f, 1f)
            }
            ExifInterface.ORIENTATION_ROTATE_270 -> matrix.setRotate(-90f)
            else -> return source
        }
        return Bitmap.createBitmap(source, 0, 0, source.width, source.height, matrix, false)
    }

    private fun orientedDimensions(width: Int, height: Int, orientation: Int): ImageDimensions =
        if (orientation.swapsEdges()) ImageDimensions(height, width) else ImageDimensions(width, height)

    private fun sampleSizeFor(width: Int, height: Int, targetLongEdge: Int): Int {
        val sourceLongEdge = maxOf(width, height)
        var sample = 1
        while (sample <= Int.MAX_VALUE / 2 && sourceLongEdge / (sample * 2) >= targetLongEdge) sample *= 2
        return sample
    }

    private suspend fun containsTransparentPixel(bitmap: Bitmap): Boolean {
        val row = IntArray(bitmap.width)
        for (y in 0 until bitmap.height) {
            if (y % 64 == 0) currentCoroutineContext().ensureActive()
            bitmap.getPixels(row, 0, bitmap.width, 0, y, bitmap.width, 1)
            if (row.any { pixel -> pixel ushr 24 != 0xff }) return true
        }
        return false
    }

    private fun isAnimatedWebp(file: File): Boolean {
        val header = ByteArray(21)
        val read = FileInputStream(file).use { it.read(header) }
        if (read < header.size) return false
        val riff = header.copyOfRange(0, 4).decodeToString()
        val webp = header.copyOfRange(8, 12).decodeToString()
        val chunk = header.copyOfRange(12, 16).decodeToString()
        return riff == "RIFF" && webp == "WEBP" && chunk == "VP8X" &&
            (header[20].toInt() and WEBP_ANIMATION_FLAG) != 0
    }

    private fun Int.requiresTransform(): Boolean = this in TRANSFORMED_EXIF_ORIENTATIONS

    private fun Int.swapsEdges(): Boolean = this in SWAPPED_EXIF_ORIENTATIONS

    private fun recycleDistinct(vararg bitmaps: Bitmap?) {
        val seen = HashSet<Bitmap>()
        bitmaps.filterNotNull().forEach { bitmap ->
            if (seen.add(bitmap) && !bitmap.isRecycled) bitmap.recycle()
        }
    }

    private fun mutexFor(workId: String): Mutex = workMutexes.computeIfAbsent(workId) { Mutex() }

    private fun requireSafeWorkId(workId: String) {
        require(SAFE_WORK_ID.matches(workId)) { "workId is not safe." }
    }

    private fun isInside(root: File, child: File): Boolean {
        val rootPath = root.canonicalFile.toPath()
        val childPath = child.canonicalFile.toPath()
        return childPath.startsWith(rootPath) && childPath != rootPath
    }

    private data class Artifact(val workId: String, val file: File)
    private data class ExifReadResult(val orientation: Int, val status: ImageLabExifStatus)

    private companion object {
        const val MANAGED_ROOT_NAME = "nimroel-assets"
        const val LAB_ROOT_NAME = "nimroel-image-lab"
        const val WEBP_ANIMATION_FLAG = 0x02
        val SAFE_WORK_ID = Regex("^[A-Za-z0-9_-]{1,128}$")
        val SUPPORTED_MIME_TYPES = setOf("image/jpeg", "image/png", "image/webp")
        val VALID_EXIF_ORIENTATIONS = ExifInterface.ORIENTATION_NORMAL..ExifInterface.ORIENTATION_ROTATE_270
        val TRANSFORMED_EXIF_ORIENTATIONS = setOf(
            ExifInterface.ORIENTATION_FLIP_HORIZONTAL,
            ExifInterface.ORIENTATION_ROTATE_180,
            ExifInterface.ORIENTATION_FLIP_VERTICAL,
            ExifInterface.ORIENTATION_TRANSPOSE,
            ExifInterface.ORIENTATION_ROTATE_90,
            ExifInterface.ORIENTATION_TRANSVERSE,
            ExifInterface.ORIENTATION_ROTATE_270,
        )
        val SWAPPED_EXIF_ORIENTATIONS = setOf(
            ExifInterface.ORIENTATION_TRANSPOSE,
            ExifInterface.ORIENTATION_ROTATE_90,
            ExifInterface.ORIENTATION_TRANSVERSE,
            ExifInterface.ORIENTATION_ROTATE_270,
        )
    }
}

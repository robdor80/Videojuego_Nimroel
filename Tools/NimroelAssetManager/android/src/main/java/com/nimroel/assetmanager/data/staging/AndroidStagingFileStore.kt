package com.nimroel.assetmanager.data.staging

import android.content.ContentResolver
import android.content.Context
import android.net.Uri
import com.nimroel.assetmanager.data.image.ANDROID_IMAGE_MIME
import com.nimroel.assetmanager.data.image.DecodedImageBounds
import com.nimroel.assetmanager.data.image.decodeImageBounds
import com.nimroel.assetmanager.data.image.normalizeImageMimeAlias
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.StagedImage
import com.nimroel.assetmanager.domain.processing.StagingErrorCode
import com.nimroel.assetmanager.domain.processing.StagingException
import com.nimroel.assetmanager.domain.processing.StagingFileStore
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.io.IOException
import java.io.InputStream
import java.security.MessageDigest
import java.nio.file.Files
import java.nio.file.AtomicMoveNotSupportedException
import java.nio.file.StandardCopyOption
import kotlinx.coroutines.currentCoroutineContext
import kotlinx.coroutines.ensureActive

class AndroidStagingFileStore internal constructor(
    private val sourceAccess: AndroidStagingSourceAccess,
    private val managedRoot: File,
    private val outputFactory: (File) -> FileOutputStream = ::FileOutputStream,
    private val renamer: (File, File) -> Boolean = ::atomicRename,
    private val boundsReader: (File) -> DecodedImageBounds = ::decodeBounds,
) : StagingFileStore {
    constructor(context: Context) : this(
        sourceAccess = ContentResolverStagingSourceAccess(context.applicationContext.contentResolver),
        managedRoot = File(context.applicationContext.filesDir, MANAGED_ROOT_NAME),
    )

    override suspend fun stageVerified(
        workId: String,
        sourceRef: ImageSourceRef,
        expectedContent: Content,
    ): StagedImage {
        require(SAFE_WORK_ID.matches(workId)) { "workId is not safe for a managed staging path." }
        val relativePath = "staging/$workId/source"
        val target = File(managedRoot, relativePath)
        val part = File(target.parentFile, "${target.name}.part")
        var promoted = false
        try {
            prepareDestination(target, part)
            val measured = copySource(sourceRef, part)
            verifyBytes(measured, expectedContent)
            val bounds = inspectPart(part)
            verifyImage(bounds, expectedContent)
            val renamed = try {
                renamer(part, target)
            } catch (error: IOException) {
                throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo publicar la copia staged verificada.", error)
            }
            if (!renamed) {
                throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo publicar la copia staged verificada.")
            }
            promoted = true
            if (!target.isFile || target.length() != measured.byteSize) {
                throw StagingException(StagingErrorCode.STAGING_VERIFY_FAILED, "La copia staged publicada no supera la verificación final.")
            }
            return StagedImage(
                relativePath = relativePath,
                content = expectedContent.copy(
                    mimeType = checkNotNull(bounds.decoderMimeType),
                    widthPx = bounds.widthPx,
                    heightPx = bounds.heightPx,
                    byteSize = measured.byteSize,
                    sha256 = measured.sha256,
                ),
            )
        } catch (error: Throwable) {
            part.delete()
            if (promoted) target.delete()
            throw error
        }
    }

    private fun prepareDestination(target: File, part: File) {
        val directory = checkNotNull(target.parentFile)
        if ((!directory.isDirectory && !directory.mkdirs()) || target.exists()) {
            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo preparar el directorio privado de staging.")
        }
        if (part.exists() && !part.delete()) {
            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo limpiar un temporal de staging anterior.")
        }
    }

    private suspend fun copySource(sourceRef: ImageSourceRef, part: File): MeasuredBytes {
        val input = try {
            sourceAccess.openStream(sourceRef)
        } catch (error: SecurityException) {
            throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "La fuente externa ya no está disponible.", error)
        } catch (error: IOException) {
            throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "No se pudo abrir la fuente externa.", error)
        } ?: throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "No se pudo abrir la fuente externa.")
        val output = try {
            outputFactory(part)
        } catch (error: IOException) {
            input.close()
            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo crear el temporal privado de staging.", error)
        }
        val digest = MessageDigest.getInstance("SHA-256")
        var byteSize = 0L
        try {
            input.use { source ->
                output.use { destination ->
                    val buffer = ByteArray(DEFAULT_BUFFER_SIZE)
                    while (true) {
                        currentCoroutineContext().ensureActive()
                        val read = try {
                            source.read(buffer)
                        } catch (error: IOException) {
                            throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "La fuente externa dejó de estar disponible durante la copia.", error)
                        } catch (error: SecurityException) {
                            throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "Android retiró el acceso a la fuente durante la copia.", error)
                        }
                        if (read < 0) break
                        if (read == 0) continue
                        try {
                            destination.write(buffer, 0, read)
                        } catch (error: IOException) {
                            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "Falló la escritura del temporal privado de staging.", error)
                        }
                        digest.update(buffer, 0, read)
                        byteSize = try {
                            Math.addExact(byteSize, read.toLong())
                        } catch (error: ArithmeticException) {
                            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "La fuente excede el tamaño representable.", error)
                        }
                    }
                    try {
                        destination.flush()
                        destination.fd.sync()
                    } catch (error: IOException) {
                        throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo sincronizar el temporal privado de staging.", error)
                    }
                }
            }
        } catch (error: StagingException) {
            throw error
        } catch (error: IOException) {
            throw StagingException(StagingErrorCode.STAGING_WRITE_FAILED, "No se pudo cerrar correctamente el temporal privado de staging.", error)
        }
        return MeasuredBytes(
            byteSize = byteSize,
            sha256 = digest.digest().toHex(),
        )
    }

    private fun verifyBytes(actual: MeasuredBytes, expected: Content) {
        if (actual.byteSize != expected.byteSize || actual.sha256 != expected.sha256) {
            throw StagingException(StagingErrorCode.SOURCE_CHANGED, "La fuente cambió después de preparar la imagen.")
        }
    }

    private fun inspectPart(part: File): DecodedImageBounds = try {
        boundsReader(part)
    } catch (error: StagingException) {
        throw error
    } catch (error: Exception) {
        throw StagingException(StagingErrorCode.STAGING_VERIFY_FAILED, "No se pudo inspeccionar directamente la copia staged.", error)
    }

    private fun verifyImage(actual: DecodedImageBounds, expected: Content) {
        val mimeType = actual.decoderMimeType.orEmpty()
        if (actual.widthPx <= 0 || actual.heightPx <= 0 || !ANDROID_IMAGE_MIME.matches(mimeType)) {
            throw StagingException(StagingErrorCode.INVALID_IMAGE, "La copia staged no contiene una imagen válida.")
        }
        if (
            actual.widthPx != expected.widthPx ||
            actual.heightPx != expected.heightPx ||
            mimeType != expected.mimeType.normalizeImageMimeAlias()
        ) {
            throw StagingException(StagingErrorCode.SOURCE_CHANGED, "La imagen staged no coincide con la fuente preparada.")
        }
    }

    private data class MeasuredBytes(val byteSize: Long, val sha256: String)

    private companion object {
        const val MANAGED_ROOT_NAME = "nimroel-assets"
        val SAFE_WORK_ID = Regex("^[A-Za-z0-9_-]{1,128}$")
    }
}

internal fun interface AndroidStagingSourceAccess {
    fun openStream(sourceRef: ImageSourceRef): InputStream?
}

private class ContentResolverStagingSourceAccess(
    private val contentResolver: ContentResolver,
) : AndroidStagingSourceAccess {
    override fun openStream(sourceRef: ImageSourceRef): InputStream? {
        val uri = Uri.parse(sourceRef.value)
        if (uri.scheme != ContentResolver.SCHEME_CONTENT) {
            throw SecurityException("Only content URIs can cross the external-source boundary.")
        }
        return contentResolver.openInputStream(uri)
    }
}

private fun decodeBounds(file: File): DecodedImageBounds = FileInputStream(file).use(::decodeImageBounds)

private fun atomicRename(source: File, target: File): Boolean {
    try {
        Files.move(source.toPath(), target.toPath(), StandardCopyOption.ATOMIC_MOVE)
    } catch (_: AtomicMoveNotSupportedException) {
        Files.move(source.toPath(), target.toPath())
    }
    return true
}

private fun ByteArray.toHex(): String = joinToString("") { byte -> "%02x".format(byte.toInt() and 0xff) }

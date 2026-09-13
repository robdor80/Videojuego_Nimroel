package com.nimroel.assetmanager.data.image

import android.content.ContentResolver
import android.graphics.BitmapFactory
import android.net.Uri
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.ContentValidator
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.PreparedImage
import java.io.IOException
import java.io.InputStream
import java.security.GeneralSecurityException
import java.security.MessageDigest
import kotlinx.coroutines.currentCoroutineContext
import kotlinx.coroutines.ensureActive

class AndroidImageContentPreparer internal constructor(
    private val sourceAccess: AndroidImageSourceAccess,
    private val messageDigestFactory: () -> MessageDigest = { MessageDigest.getInstance("SHA-256") },
) : ImageContentPreparer {
    constructor(contentResolver: ContentResolver) : this(ContentResolverImageSourceAccess(contentResolver))

    override suspend fun prepare(sourceRef: ImageSourceRef): PreparedImage {
        try {
            val resolverMimeType = sourceAccess.mimeType(sourceRef)
            validateResolverMimeType(resolverMimeType)
            val measured = hashAndMeasure(sourceRef)
            if (measured.byteSize == 0L) throw ImagePreparationException("La imagen seleccionada está vacía.")

            val bounds = sourceAccess.decodeBounds(sourceRef)
            if (bounds.widthPx <= 0 || bounds.heightPx <= 0) {
                throw ImagePreparationException("Android no pudo interpretar dimensiones válidas para la imagen seleccionada.")
            }
            val mimeType = resolveMimeType(resolverMimeType, bounds.decoderMimeType)
            val content = Content(
                mimeType = mimeType,
                widthPx = bounds.widthPx,
                heightPx = bounds.heightPx,
                byteSize = measured.byteSize,
                sha256 = measured.sha256,
                colorSpace = null,
            )
            val errors = ContentValidator.validate(content)
            if (errors.isNotEmpty()) throw ImagePreparationException("El contenido preparado no es válido: ${errors.joinToString("; ")}")
            return PreparedImage(sourceRef, content)
        } catch (error: ImagePreparationException) {
            throw error
        } catch (error: SecurityException) {
            throw ImagePreparationException("Android ya no permite acceder a la imagen seleccionada.", error)
        } catch (error: IOException) {
            throw ImagePreparationException("No se pudo leer la imagen seleccionada.", error)
        } catch (error: GeneralSecurityException) {
            throw ImagePreparationException("No se pudo calcular la huella SHA-256 de la imagen.", error)
        }
    }

    private suspend fun hashAndMeasure(sourceRef: ImageSourceRef): MeasuredBytes {
        val digest = messageDigestFactory()
        var byteSize = 0L
        val buffer = ByteArray(DEFAULT_BUFFER_SIZE)
        val stream = sourceAccess.openStream(sourceRef)
            ?: throw ImagePreparationException("No se pudo abrir la imagen seleccionada.")
        stream.use { input ->
            while (true) {
                currentCoroutineContext().ensureActive()
                val read = input.read(buffer)
                if (read < 0) break
                if (read == 0) continue
                digest.update(buffer, 0, read)
                byteSize = Math.addExact(byteSize, read.toLong())
            }
        }
        return MeasuredBytes(
            byteSize = byteSize,
            sha256 = digest.digest().joinToString("") { byte -> "%02x".format(byte.toInt() and 0xff) },
        )
    }

    private fun resolveMimeType(resolverValue: String?, decoderValue: String?): String {
        val resolverMime = resolverValue?.trim()?.lowercase()?.normalizeMimeAlias()
        val decoderMime = decoderValue?.trim()?.lowercase()?.normalizeMimeAlias()
        if (resolverMime != null && !IMAGE_MIME.matches(resolverMime)) {
            throw ImagePreparationException("El archivo seleccionado no tiene un tipo MIME de imagen válido.")
        }
        if (decoderMime != null && !IMAGE_MIME.matches(decoderMime)) {
            throw ImagePreparationException("El decoder devolvió un tipo MIME de imagen no válido.")
        }
        return decoderMime ?: resolverMime
        ?: throw ImagePreparationException("No se pudo determinar de forma fiable el tipo MIME de la imagen.")
    }

    private fun validateResolverMimeType(value: String?) {
        val normalized = value?.trim()?.lowercase()?.normalizeMimeAlias() ?: return
        if (!IMAGE_MIME.matches(normalized)) {
            throw ImagePreparationException("El archivo seleccionado no tiene un tipo MIME de imagen válido.")
        }
    }

    private fun String.normalizeMimeAlias(): String = if (this == "image/jpg") "image/jpeg" else this

    private data class MeasuredBytes(val byteSize: Long, val sha256: String)

    private companion object {
        val IMAGE_MIME = Regex("^image/[a-z0-9.+-]+$")
    }
}

internal data class DecodedImageBounds(
    val widthPx: Int,
    val heightPx: Int,
    val decoderMimeType: String?,
)

internal interface AndroidImageSourceAccess {
    fun mimeType(sourceRef: ImageSourceRef): String?
    fun openStream(sourceRef: ImageSourceRef): InputStream?
    fun decodeBounds(sourceRef: ImageSourceRef): DecodedImageBounds
}

private class ContentResolverImageSourceAccess(
    private val contentResolver: ContentResolver,
) : AndroidImageSourceAccess {
    override fun mimeType(sourceRef: ImageSourceRef): String? = contentResolver.getType(sourceRef.toUri())

    override fun openStream(sourceRef: ImageSourceRef): InputStream? =
        contentResolver.openInputStream(sourceRef.toUri())

    override fun decodeBounds(sourceRef: ImageSourceRef): DecodedImageBounds {
        val options = BitmapFactory.Options().apply { inJustDecodeBounds = true }
        val stream = openStream(sourceRef)
            ?: throw ImagePreparationException("No se pudo volver a abrir la imagen para leer sus dimensiones.")
        stream.use { BitmapFactory.decodeStream(it, null, options) }
        return DecodedImageBounds(options.outWidth, options.outHeight, options.outMimeType)
    }

    private fun ImageSourceRef.toUri(): Uri = Uri.parse(value).also { uri ->
        if (uri.scheme != ContentResolver.SCHEME_CONTENT) {
            throw ImagePreparationException("La referencia seleccionada no es un URI content:// válido.")
        }
    }
}

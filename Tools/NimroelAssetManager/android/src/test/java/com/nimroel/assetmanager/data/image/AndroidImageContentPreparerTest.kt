package com.nimroel.assetmanager.data.image

import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import java.io.ByteArrayInputStream
import java.io.IOException
import java.security.NoSuchAlgorithmException
import java.security.MessageDigest
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AndroidImageContentPreparerTest {
    @Test
    fun `prepares canonical Content from exact streamed bytes`() = runTest {
        val bytes = "exact selected bytes".encodeToByteArray()
        val access = FakeSourceAccess(bytes, "image/png", DecodedImageBounds(24, 36, "image/png"))
        val preparer = AndroidImageContentPreparer(access)

        val prepared = preparer.prepare(ImageSourceRef("content://test/image"))

        assertEquals("image/png", prepared.content.mimeType)
        assertEquals(24, prepared.content.widthPx)
        assertEquals(36, prepared.content.heightPx)
        assertEquals(bytes.size.toLong(), prepared.content.byteSize)
        assertEquals(sha256(bytes), prepared.content.sha256)
        assertEquals(64, prepared.content.sha256.length)
        assertTrue(prepared.content.sha256.all { it in '0'..'9' || it in 'a'..'f' })
        assertEquals(2, access.openCount)
    }

    @Test
    fun `byte size is measured from stream instead of external metadata`() = runTest {
        val bytes = ByteArray(18_437) { index -> (index % 251).toByte() }
        val access = FakeSourceAccess(bytes, "image/jpeg", DecodedImageBounds(400, 300, "image/jpeg"))

        val prepared = AndroidImageContentPreparer(access).prepare(ImageSourceRef("content://test/large"))

        assertEquals(18_437L, prepared.content.byteSize)
        assertEquals(sha256(bytes), prepared.content.sha256)
    }

    @Test
    fun `rejects an empty image`() = runTest {
        val preparer = AndroidImageContentPreparer(
            FakeSourceAccess(byteArrayOf(), "image/png", DecodedImageBounds(-1, -1, null)),
        )

        val error = runCatching { preparer.prepare(ImageSourceRef("content://test/empty")) }.exceptionOrNull()

        assertTrue(error is ImagePreparationException)
        assertTrue(error?.message.orEmpty().contains("vacía"))
    }

    @Test
    fun `rejects non image MIME`() = runTest {
        val preparer = AndroidImageContentPreparer(
            FakeSourceAccess(byteArrayOf(1), "text/plain", DecodedImageBounds(1, 1, null)),
        )

        val error = runCatching { preparer.prepare(ImageSourceRef("content://test/text")) }.exceptionOrNull()

        assertTrue(error is ImagePreparationException)
        assertTrue(error?.message.orEmpty().contains("MIME"))
    }

    @Test
    fun `rejects invalid decoded dimensions`() = runTest {
        val preparer = AndroidImageContentPreparer(
            FakeSourceAccess(byteArrayOf(1, 2), "image/png", DecodedImageBounds(0, -1, "image/png")),
        )

        val error = runCatching { preparer.prepare(ImageSourceRef("content://test/invalid")) }.exceptionOrNull()

        assertTrue(error is ImagePreparationException)
        assertTrue(error?.message.orEmpty().contains("dimensiones válidas"))
    }

    @Test
    fun `rejects a null input stream clearly`() = runTest {
        val preparer = AndroidImageContentPreparer(NullStreamAccess)

        val error = runCatching { preparer.prepare(ImageSourceRef("content://test/missing")) }.exceptionOrNull()

        assertTrue(error is ImagePreparationException)
        assertTrue(error?.message.orEmpty().contains("abrir"))
    }

    @Test
    fun `reports security and IO failures distinctly`() = runTest {
        val securityError = runCatching {
            AndroidImageContentPreparer(ThrowingSourceAccess(SecurityException("denied")))
                .prepare(ImageSourceRef("content://test/denied"))
        }.exceptionOrNull()
        val ioError = runCatching {
            AndroidImageContentPreparer(ThrowingSourceAccess(IOException("broken")))
                .prepare(ImageSourceRef("content://test/broken"))
        }.exceptionOrNull()

        assertTrue(securityError is ImagePreparationException)
        assertTrue(securityError?.message.orEmpty().contains("ya no permite"))
        assertTrue(ioError is ImagePreparationException)
        assertTrue(ioError?.message.orEmpty().contains("No se pudo leer"))
    }

    @Test
    fun `reports SHA-256 initialization failures distinctly`() = runTest {
        val preparer = AndroidImageContentPreparer(
            FakeSourceAccess(byteArrayOf(1), "image/png", DecodedImageBounds(1, 1, "image/png")),
            messageDigestFactory = { throw NoSuchAlgorithmException("missing") },
        )

        val error = runCatching { preparer.prepare(ImageSourceRef("content://test/hash")) }.exceptionOrNull()

        assertTrue(error is ImagePreparationException)
        assertTrue(error?.message.orEmpty().contains("SHA-256"))
    }

    private class FakeSourceAccess(
        private val bytes: ByteArray,
        private val sourceMimeType: String?,
        private val bounds: DecodedImageBounds,
    ) : AndroidImageSourceAccess {
        var openCount = 0

        override fun mimeType(sourceRef: ImageSourceRef): String? = sourceMimeType

        override fun openStream(sourceRef: ImageSourceRef) = ByteArrayInputStream(bytes).also { openCount += 1 }

        override fun decodeBounds(sourceRef: ImageSourceRef): DecodedImageBounds {
            openStream(sourceRef).use { it.read() }
            return bounds
        }
    }

    private object NullStreamAccess : AndroidImageSourceAccess {
        override fun mimeType(sourceRef: ImageSourceRef): String? = "image/png"
        override fun openStream(sourceRef: ImageSourceRef) = null
        override fun decodeBounds(sourceRef: ImageSourceRef) = DecodedImageBounds(1, 1, "image/png")
    }

    private class ThrowingSourceAccess(private val error: Exception) : AndroidImageSourceAccess {
        override fun mimeType(sourceRef: ImageSourceRef): String? = throw error
        override fun openStream(sourceRef: ImageSourceRef): ByteArrayInputStream = throw error
        override fun decodeBounds(sourceRef: ImageSourceRef): DecodedImageBounds = throw error
    }

    private fun sha256(bytes: ByteArray) = MessageDigest.getInstance("SHA-256")
        .digest(bytes)
        .joinToString("") { "%02x".format(it.toInt() and 0xff) }

}

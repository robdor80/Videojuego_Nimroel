package com.nimroel.assetmanager.data.staging

import android.content.ContentProvider
import android.content.ContentValues
import android.content.Context
import android.database.Cursor
import android.net.Uri
import android.os.ParcelFileDescriptor
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.StagingErrorCode
import com.nimroel.assetmanager.domain.processing.StagingException
import java.io.ByteArrayInputStream
import java.io.File
import java.io.IOException
import java.security.MessageDigest
import java.util.Base64
import java.util.UUID
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test
import org.junit.rules.TemporaryFolder
import org.junit.runner.RunWith
import org.robolectric.Robolectric
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [35])
@GraphicsMode(GraphicsMode.Mode.NATIVE)
class AndroidStagingFileStoreTest {
    @get:Rule val temporaryFolder = TemporaryFolder()

    private val pngBytes = Base64.getDecoder().decode(KNOWN_PNG_BASE64)
    private val sourceRef = ImageSourceRef("content://images/current")
    private val expected = Content("image/png", 1, 1, pngBytes.size.toLong(), pngBytes.sha256())

    @Test
    fun `valid source is streamed exactly to normalized relative staging and promoted without part`() = runTest {
        val root = temporaryFolder.newFolder("nimroel-assets")
        val store = store(root, pngBytes)

        val staged = store.stageVerified("work-valid", sourceRef, expected)

        assertEquals("staging/work-valid/source", staged.relativePath)
        assertFalse(staged.relativePath.startsWith('/'))
        assertFalse(staged.relativePath.contains('\\'))
        assertEquals(expected, staged.content)
        assertArrayEquals(pngBytes, root.resolve(staged.relativePath).readBytes())
        assertFalse(root.resolve("staging/work-valid/source.part").exists())
    }

    @Test
    fun `source changed after preparation fails by hash and never promotes part`() = runTest {
        val root = temporaryFolder.newFolder("hash-root")
        val changed = pngBytes.clone().also { it[it.lastIndex] = (it.last().toInt() xor 1).toByte() }

        val error = failure(store(root, changed), "work-hash", expected)

        assertEquals(StagingErrorCode.SOURCE_CHANGED, error.code)
        assertNoPublishedFiles(root, "work-hash")
    }

    @Test
    fun `byte size mismatch fails and never publishes ready staging`() = runTest {
        val root = temporaryFolder.newFolder("size-root")

        val error = failure(store(root, pngBytes), "work-size", expected.copy(byteSize = expected.byteSize!! + 1))

        assertEquals(StagingErrorCode.SOURCE_CHANGED, error.code)
        assertNoPublishedFiles(root, "work-size")
    }

    @Test
    fun `dimension mismatch detected from staged file fails`() = runTest {
        val root = temporaryFolder.newFolder("dimension-root")

        val error = failure(store(root, pngBytes), "work-dimension", expected.copy(widthPx = 2))

        assertEquals(StagingErrorCode.SOURCE_CHANGED, error.code)
        assertNoPublishedFiles(root, "work-dimension")
    }

    @Test
    fun `MIME mismatch detected from staged file fails`() = runTest {
        val root = temporaryFolder.newFolder("mime-root")

        val error = failure(store(root, pngBytes), "work-mime", expected.copy(mimeType = "image/jpeg"))

        assertEquals(StagingErrorCode.SOURCE_CHANGED, error.code)
        assertNoPublishedFiles(root, "work-mime")
    }

    @Test
    fun `unavailable external stream becomes stable source unavailable error`() = runTest {
        val root = temporaryFolder.newFolder("unavailable-root")
        val store = AndroidStagingFileStore(AndroidStagingSourceAccess { null }, root)

        val error = failure(store, "work-unavailable", expected)

        assertEquals(StagingErrorCode.SOURCE_UNAVAILABLE, error.code)
        assertNoPublishedFiles(root, "work-unavailable")
    }

    @Test
    fun `write and rename failures never leave part treated as valid`() = runTest {
        val writeRoot = temporaryFolder.newFolder("write-root")
        val writeFailure = AndroidStagingFileStore(
            sourceAccess = AndroidStagingSourceAccess { ByteArrayInputStream(pngBytes) },
            managedRoot = writeRoot,
            outputFactory = { throw IOException("disk full") },
        )
        val renameRoot = temporaryFolder.newFolder("rename-root")
        val renameFailure = AndroidStagingFileStore(
            sourceAccess = AndroidStagingSourceAccess { ByteArrayInputStream(pngBytes) },
            managedRoot = renameRoot,
            renamer = { _, _ -> false },
        )

        assertEquals(StagingErrorCode.STAGING_WRITE_FAILED, failure(writeFailure, "work-write", expected).code)
        assertNoPublishedFiles(writeRoot, "work-write")
        assertEquals(StagingErrorCode.STAGING_WRITE_FAILED, failure(renameFailure, "work-rename", expected).code)
        assertNoPublishedFiles(renameRoot, "work-rename")
    }

    @Test
    fun `invalid staged bytes fail direct image inspection even when hash and size match`() = runTest {
        val root = temporaryFolder.newFolder("invalid-root")
        val invalid = "not-an-image".encodeToByteArray()
        val described = Content("image/png", 1, 1, invalid.size.toLong(), invalid.sha256())

        val error = failure(store(root, invalid), "work-invalid", described)

        assertEquals(StagingErrorCode.INVALID_IMAGE, error.code)
        assertNoPublishedFiles(root, "work-invalid")
    }

    @Test
    fun `real content URI is copied into app private managed staging`() = runTest {
        val context = ApplicationProvider.getApplicationContext<Context>()
        RealImageProvider.imageFile = temporaryFolder.newFile("provider.png").apply { writeBytes(pngBytes) }
        Robolectric.buildContentProvider(RealImageProvider::class.java).create(AUTHORITY).get()
        val workId = UUID.randomUUID().toString()

        val staged = AndroidStagingFileStore(context).stageVerified(
            workId,
            ImageSourceRef("content://$AUTHORITY/image"),
            expected,
        )

        val managed = context.filesDir.resolve("nimroel-assets/${staged.relativePath}")
        assertTrue(managed.isFile)
        assertArrayEquals(pngBytes, managed.readBytes())
        managed.parentFile?.deleteRecursively()
    }

    @Test
    fun `discard removes only its managed work directory and tolerates an absent source`() = runTest {
        val root = temporaryFolder.newFolder("discard-root")
        val store = store(root, pngBytes)
        store.stageVerified("work-a", sourceRef, expected)
        store.stageVerified("work-b", sourceRef, expected)
        val stagingRootMarker = root.resolve("staging/keep.txt").apply { writeText("keep") }

        store.discard("work-a")
        store.discard("work-a")

        assertFalse(root.resolve("staging/work-a").exists())
        assertTrue(root.resolve("staging/work-b/source").isFile)
        assertTrue(stagingRootMarker.isFile)
    }

    @Test
    fun `discard rejects unsafe work paths before touching storage`() = runTest {
        val root = temporaryFolder.newFolder("unsafe-discard-root")
        val sentinel = root.resolve("sentinel.txt").apply { writeText("keep") }
        val store = store(root, pngBytes)

        try {
            store.discard("../sentinel")
            error("Expected unsafe work ID rejection")
        } catch (_: IllegalArgumentException) {
            assertTrue(sentinel.isFile)
        }
    }

    private fun store(root: File, bytes: ByteArray) = AndroidStagingFileStore(
        sourceAccess = AndroidStagingSourceAccess { ByteArrayInputStream(bytes) },
        managedRoot = root,
    )

    private suspend fun failure(
        store: AndroidStagingFileStore,
        workId: String,
        content: Content,
    ): StagingException {
        try {
            store.stageVerified(workId, sourceRef, content)
        } catch (error: StagingException) {
            return error
        }
        error("Expected staging to fail")
    }

    private fun assertNoPublishedFiles(root: File, workId: String) {
        assertFalse(root.resolve("staging/$workId/source").exists())
        assertFalse(root.resolve("staging/$workId/source.part").exists())
    }

    class RealImageProvider : ContentProvider() {
        override fun onCreate() = true
        override fun getType(uri: Uri) = "image/png"
        override fun openFile(uri: Uri, mode: String): ParcelFileDescriptor =
            ParcelFileDescriptor.open(imageFile, ParcelFileDescriptor.MODE_READ_ONLY)

        override fun query(uri: Uri, projection: Array<out String>?, selection: String?, selectionArgs: Array<out String>?, sortOrder: String?): Cursor? = null
        override fun insert(uri: Uri, values: ContentValues?): Uri? = null
        override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int = 0
        override fun update(uri: Uri, values: ContentValues?, selection: String?, selectionArgs: Array<out String>?): Int = 0

        companion object {
            lateinit var imageFile: File
        }
    }

    private fun ByteArray.sha256(): String =
        MessageDigest.getInstance("SHA-256").digest(this).joinToString("") { "%02x".format(it.toInt() and 0xff) }

    private companion object {
        const val AUTHORITY = "com.nimroel.assetmanager.test.staging"
        const val KNOWN_PNG_BASE64 =
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
    }
}

package com.nimroel.assetmanager.data.image

import android.content.ContentProvider
import android.content.ContentValues
import android.content.Context
import android.database.Cursor
import android.net.Uri
import android.os.ParcelFileDescriptor
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import java.io.File
import java.util.Base64
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.Robolectric
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [35])
@GraphicsMode(GraphicsMode.Mode.NATIVE)
class AndroidImageContentPreparerRobolectricTest {
    @Test
    fun `real ContentResolver preparer reads known PNG dimensions bytes and hash`() = runTest {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val bytes = Base64.getDecoder().decode(KNOWN_PNG_BASE64)
        KnownImageProvider.imageFile = context.cacheDir.resolve("known-image.png").apply { writeBytes(bytes) }
        Robolectric.buildContentProvider(KnownImageProvider::class.java).create(AUTHORITY).get()

        val prepared = AndroidImageContentPreparer(context.contentResolver).prepare(
            ImageSourceRef("content://$AUTHORITY/known-image"),
        )

        assertEquals("image/png", prepared.content.mimeType)
        assertEquals(1, prepared.content.widthPx)
        assertEquals(1, prepared.content.heightPx)
        assertEquals(68L, prepared.content.byteSize)
        assertEquals("431ced6916a2a21a156e38701afe55bbd7f88969fbbfc56d7fe099d47f265460", prepared.content.sha256)
        assertNull(prepared.content.colorSpace)
    }

    class KnownImageProvider : ContentProvider() {
        override fun onCreate() = true

        override fun getType(uri: Uri) = "image/png"

        override fun openFile(uri: Uri, mode: String): ParcelFileDescriptor =
            ParcelFileDescriptor.open(imageFile, ParcelFileDescriptor.MODE_READ_ONLY)

        override fun query(
            uri: Uri,
            projection: Array<out String>?,
            selection: String?,
            selectionArgs: Array<out String>?,
            sortOrder: String?,
        ): Cursor? = null

        override fun insert(uri: Uri, values: ContentValues?): Uri? = null

        override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int = 0

        override fun update(uri: Uri, values: ContentValues?, selection: String?, selectionArgs: Array<out String>?): Int = 0

        companion object {
            lateinit var imageFile: File
        }
    }

    private companion object {
        const val AUTHORITY = "com.nimroel.assetmanager.test.images"
        const val KNOWN_PNG_BASE64 =
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
    }
}

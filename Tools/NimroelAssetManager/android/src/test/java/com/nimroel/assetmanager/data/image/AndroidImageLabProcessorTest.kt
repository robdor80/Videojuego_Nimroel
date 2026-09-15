package com.nimroel.assetmanager.data.image

import android.content.Context
import android.graphics.Bitmap
import android.graphics.Color
import android.os.Build
import androidx.exifinterface.media.ExifInterface
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.processing.ImageLabException
import com.nimroel.assetmanager.domain.processing.ImageLabExifStatus
import com.nimroel.assetmanager.domain.processing.ImageLabProfile
import com.nimroel.assetmanager.domain.processing.ImageLabRequest
import com.nimroel.assetmanager.domain.processing.ImageLabResult
import com.nimroel.assetmanager.domain.processing.StagedImage
import com.nimroel.assetmanager.domain.processing.StagedImageLabSource
import java.io.File
import java.io.FileOutputStream
import java.security.MessageDigest
import java.util.UUID
import kotlinx.coroutines.CompletableDeferred
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.async
import kotlinx.coroutines.cancelAndJoin
import kotlinx.coroutines.test.runCurrent
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Assert.fail
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [35])
@GraphicsMode(GraphicsMode.Mode.NATIVE)
@OptIn(ExperimentalCoroutinesApi::class)
class AndroidImageLabProcessorTest {
    private val context = ApplicationProvider.getApplicationContext<Context>()

    @Test
    fun `real platform encoder reads immutable staging and writes disposable verified WebP`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.rgb(40, 90, 160))
        val sourceFile = sourceFile(workId)
        val originalBytes = sourceFile.readBytes()
        val processor = processor()

        val result = processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85)))

        assertEquals(ImageLabResult.MIME_WEBP, result.mimeType)
        assertEquals(400, result.widthPx)
        assertEquals(200, result.heightPx)
        assertEquals(85, result.quality)
        assertTrue(result.byteSize > 0)
        assertArrayEquals(originalBytes, sourceFile.readBytes())
        assertTrue(candidate(workId).isFile)
        assertTrue(sourceFile.isFile)
        assertTrue(workDirectory(workId).listFiles().orEmpty().none { it.name.endsWith(".part") })
    }

    @Test
    fun `transparent sampled raster is detected and retained by generated WebP`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(
            workId,
            40,
            20,
            Bitmap.CompressFormat.PNG,
            Color.rgb(40, 90, 160),
            hasTransparency = true,
        )

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 90)))

        assertTrue(result.sourceHasAlphaCapability)
        assertTrue(result.transparentPixelsObserved)
    }

    @Test
    fun `JPEG EXIF rotation is physically applied and swaps output dimensions`() = runTest {
        val source = stagedWithExif(uniqueWorkId(), Bitmap.CompressFormat.JPEG, ExifInterface.ORIENTATION_ROTATE_90)

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 80)))

        assertEquals(200, result.widthPx)
        assertEquals(400, result.heightPx)
        assertTrue(result.orientationApplied)
        assertEquals(ImageLabExifStatus.TRANSFORMED, result.exifStatus)
    }

    @Test
    @Config(sdk = [26])
    fun `PNG EXIF is read through AndroidX in Robolectric environment`() = runTest {
        val source = stagedWithExif(uniqueWorkId(), Bitmap.CompressFormat.PNG, ExifInterface.ORIENTATION_ROTATE_90)

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 80)))

        assertEquals(200, result.widthPx)
        assertEquals(400, result.heightPx)
        assertEquals(ImageLabExifStatus.TRANSFORMED, result.exifStatus)
    }

    @Suppress("DEPRECATION")
    @Test
    @Config(sdk = [26])
    fun `WebP EXIF is read through AndroidX in Robolectric environment`() = runTest {
        val source = stagedWithExif(
            uniqueWorkId(),
            Bitmap.CompressFormat.WEBP,
            ExifInterface.ORIENTATION_ROTATE_90,
        )

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 80)))

        assertEquals(200, result.widthPx)
        assertEquals(400, result.heightPx)
        assertEquals(ImageLabExifStatus.TRANSFORMED, result.exifStatus)
    }

    @Test
    fun `missing EXIF is explicitly normal and non fatal`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 80)))

        assertFalse(result.orientationApplied)
        assertEquals(ImageLabExifStatus.ABSENT, result.exifStatus)
    }

    @Test
    fun `invalid EXIF orientation is controlled and reported as unreadable`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.JPEG, Color.BLUE)
        ExifInterface(sourceFile(workId)).apply {
            setAttribute(ExifInterface.TAG_ORIENTATION, "9")
            saveAttributes()
        }
        val updated = refreshedSource(workId, source, "image/jpeg")

        val result = processor().generate(ImageLabRequest(updated, ImageLabProfile(1024, 80)))

        assertFalse(result.orientationApplied)
        assertEquals(ImageLabExifStatus.UNREADABLE, result.exifStatus)
    }

    @Test
    fun `corrupt raster is rejected before metadata can be mistaken for normal`() = runTest {
        val workId = uniqueWorkId()
        val file = sourceFile(workId)
        file.parentFile?.mkdirs()
        file.writeBytes(byteArrayOf(1, 2, 3, 4))
        val source = StagedImageLabSource.from(
            workId,
            StagedImage(
                "staging/$workId/source",
                Content("image/jpeg", 10, 10, file.length(), file.readBytes().sha256()),
            ),
        )

        expectImageLabFailure { processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 80))) }
    }

    @Test
    fun `oriented visual axes drive final resize`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedWithExif(
            workId,
            Bitmap.CompressFormat.JPEG,
            ExifInterface.ORIENTATION_ROTATE_90,
            width = 1200,
            height = 1600,
        )

        val result = processor().generate(ImageLabRequest(source, ImageLabProfile(1024, 85)))

        assertEquals(1024, result.widthPx)
        assertEquals(768, result.heightPx)
    }

    @Test
    fun `orientation 1 keeps asymmetric pixels`() = assertOrientation(
        ExifInterface.ORIENTATION_NORMAL,
        listOf(listOf(A, B, C), listOf(D, E, F)),
    )

    @Test
    fun `orientation 2 flips asymmetric pixels horizontally`() = assertOrientation(
        ExifInterface.ORIENTATION_FLIP_HORIZONTAL,
        listOf(listOf(C, B, A), listOf(F, E, D)),
    )

    @Test
    fun `orientation 3 rotates asymmetric pixels 180`() = assertOrientation(
        ExifInterface.ORIENTATION_ROTATE_180,
        listOf(listOf(F, E, D), listOf(C, B, A)),
    )

    @Test
    fun `orientation 4 flips asymmetric pixels vertically`() = assertOrientation(
        ExifInterface.ORIENTATION_FLIP_VERTICAL,
        listOf(listOf(D, E, F), listOf(A, B, C)),
    )

    @Test
    fun `orientation 5 transposes asymmetric pixels`() = assertOrientation(
        ExifInterface.ORIENTATION_TRANSPOSE,
        listOf(listOf(A, D), listOf(B, E), listOf(C, F)),
    )

    @Test
    fun `orientation 6 rotates asymmetric pixels 90 clockwise`() = assertOrientation(
        ExifInterface.ORIENTATION_ROTATE_90,
        listOf(listOf(D, A), listOf(E, B), listOf(F, C)),
    )

    @Test
    fun `orientation 7 transverses asymmetric pixels`() = assertOrientation(
        ExifInterface.ORIENTATION_TRANSVERSE,
        listOf(listOf(F, C), listOf(E, B), listOf(D, A)),
    )

    @Test
    fun `orientation 8 rotates asymmetric pixels 270 clockwise`() = assertOrientation(
        ExifInterface.ORIENTATION_ROTATE_270,
        listOf(listOf(C, F), listOf(B, E), listOf(A, D)),
    )

    @Config(sdk = [26])
    @Test
    fun `API 26 selects legacy lossy WebP format`() {
        @Suppress("DEPRECATION")
        val expected = Bitmap.CompressFormat.WEBP
        assertEquals(26, Build.VERSION.SDK_INT)
        assertEquals(expected, processor().webpFormatFor(Build.VERSION.SDK_INT))
    }

    @Config(sdk = [30])
    @Test
    fun `API 30 selects explicit WebP lossy format`() {
        assertEquals(30, Build.VERSION.SDK_INT)
        assertEquals(Bitmap.CompressFormat.WEBP_LOSSY, processor().webpFormatFor(Build.VERSION.SDK_INT))
    }

    @Test
    fun `failed verification of same profile preserves previous candidate and artifact`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)
        var writes = 0
        val processor = processor(afterTemporaryWritten = { temporary ->
            writes += 1
            if (writes == 2) temporary.writeBytes(byteArrayOf(1, 2, 3))
        })
        val first = processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85)))
        val original = candidate(workId).readBytes()

        expectImageLabFailure { processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85))) }

        assertArrayEquals(original, candidate(workId).readBytes())
        val preview = processor.load(first.artifactRef, 100)
        assertTrue(preview is ImageLabPreviewLoadResult.Ready)
        (preview as ImageLabPreviewLoadResult.Ready).bitmap.recycle()
    }

    @Test
    fun `OOM during same profile regeneration preserves previous candidate`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)
        var writes = 0
        val processor = processor(afterTemporaryWritten = {
            writes += 1
            if (writes == 2) throw OutOfMemoryError("forced")
        })
        processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85)))
        val original = candidate(workId).readBytes()

        expectImageLabFailure { processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85))) }

        assertArrayEquals(original, candidate(workId).readBytes())
    }

    @Test
    fun `successful replacement remains old until second temporary is verified and promoted`() = runTest {
        val workId = uniqueWorkId()
        val firstSource = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)
        val entered = CompletableDeferred<Unit>()
        val release = CompletableDeferred<Unit>()
        var promotions = 0
        val processor = processor(beforePromotion = {
            promotions += 1
            if (promotions == 2) {
                entered.complete(Unit)
                release.await()
            }
        })
        processor.generate(ImageLabRequest(firstSource, ImageLabProfile(1024, 85)))
        val oldBytes = candidate(workId).readBytes()
        val secondSource = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.RED)

        val second = async { processor.generate(ImageLabRequest(secondSource, ImageLabProfile(1024, 85))) }
        entered.await()
        assertArrayEquals(oldBytes, candidate(workId).readBytes())
        release.complete(Unit)
        second.await()

        assertNotEquals(oldBytes.toList(), candidate(workId).readBytes().toList())
    }

    @Test
    fun `cancellation before promotion preserves previous candidate`() = runTest {
        val workId = uniqueWorkId()
        val firstSource = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)
        val entered = CompletableDeferred<Unit>()
        val release = CompletableDeferred<Unit>()
        var promotions = 0
        val processor = processor(beforePromotion = {
            promotions += 1
            if (promotions == 2) {
                entered.complete(Unit)
                release.await()
            }
        })
        processor.generate(ImageLabRequest(firstSource, ImageLabProfile(1024, 85)))
        val oldBytes = candidate(workId).readBytes()
        val secondSource = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.RED)

        val second = async { processor.generate(ImageLabRequest(secondSource, ImageLabProfile(1024, 85))) }
        entered.await()
        second.cancelAndJoin()
        release.complete(Unit)

        assertArrayEquals(oldBytes, candidate(workId).readBytes())
        assertTrue(workDirectory(workId).listFiles().orEmpty().none { it.name.endsWith(".part") })
    }

    @Test
    fun `real clear is scoped to one work and keeps staging and roots`() = runTest {
        val workA = uniqueWorkId()
        val workB = uniqueWorkId()
        val sourceA = stagedBitmap(workA, 80, 40, Bitmap.CompressFormat.PNG, Color.BLUE)
        val sourceB = stagedBitmap(workB, 80, 40, Bitmap.CompressFormat.PNG, Color.RED)
        val processor = processor()
        val cacheSentinel = cacheRoot().resolve("root-sentinel").apply { writeText("safe") }
        val filesSentinel = managedRoot().resolve("root-sentinel").apply { parentFile?.mkdirs(); writeText("safe") }
        val resultA = processor.generate(ImageLabRequest(sourceA, ImageLabProfile(1024, 85)))
        val resultB = processor.generate(ImageLabRequest(sourceB, ImageLabProfile(1024, 85)))
        workDirectory(workA).resolve("owned-orphan.part").writeText("temporary")

        processor.clear(workA)

        assertFalse(workDirectory(workA).exists())
        assertTrue(workDirectory(workB).isDirectory)
        assertTrue(sourceFile(workA).isFile)
        assertTrue(sourceFile(workB).isFile)
        assertTrue(managedRoot().isDirectory)
        assertTrue(cacheRoot().isDirectory)
        assertTrue(cacheSentinel.isFile)
        assertTrue(filesSentinel.isFile)
        assertTrue(processor.load(resultA.artifactRef, 100) is ImageLabPreviewLoadResult.Unavailable)
        val previewB = processor.load(resultB.artifactRef, 100)
        assertTrue(previewB is ImageLabPreviewLoadResult.Ready)
        (previewB as ImageLabPreviewLoadResult.Ready).bitmap.recycle()

        processor.clear(workA)
    }

    @Test
    fun `clear waits for generation critical section of same work`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 80, 40, Bitmap.CompressFormat.PNG, Color.BLUE)
        val entered = CompletableDeferred<Unit>()
        val release = CompletableDeferred<Unit>()
        val processor = processor(beforePromotion = {
            entered.complete(Unit)
            release.await()
        })

        val generation = async { processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85))) }
        entered.await()
        val clear = async { processor.clear(workId) }
        runCurrent()
        assertFalse(clear.isCompleted)
        release.complete(Unit)
        generation.await()
        clear.await()

        assertFalse(workDirectory(workId).exists())
    }

    @Test
    fun `blocked generation for one work does not block a different work`() = runTest {
        val workA = uniqueWorkId()
        val workB = uniqueWorkId()
        val sourceA = stagedBitmap(workA, 80, 40, Bitmap.CompressFormat.PNG, Color.BLUE)
        val sourceB = stagedBitmap(workB, 80, 40, Bitmap.CompressFormat.PNG, Color.RED)
        val entered = CompletableDeferred<Unit>()
        val release = CompletableDeferred<Unit>()
        val processor = processor(beforePromotion = {
            if (!entered.isCompleted) {
                entered.complete(Unit)
                release.await()
            }
        })

        val generationA = async { processor.generate(ImageLabRequest(sourceA, ImageLabProfile(1024, 85))) }
        entered.await()
        val generationB = async { processor.generate(ImageLabRequest(sourceB, ImageLabProfile(1024, 85))) }
        runCurrent()
        assertTrue(generationB.isCompleted)
        release.complete(Unit)
        generationA.await()
        generationB.await()
    }

    @Test
    fun `path traversal work id is rejected without touching cache root`() = runTest {
        val sentinel = cacheRoot().resolve("sentinel-${UUID.randomUUID()}").apply { writeText("safe") }

        try {
            processor().clear("../escape")
            fail("Expected unsafe workId rejection")
        } catch (_: IllegalArgumentException) {
            assertTrue(sentinel.isFile)
        }
    }

    @Test
    fun `preview enforces real max long edge and missing file is unavailable`() = runTest {
        val workId = uniqueWorkId()
        val source = stagedBitmap(workId, 400, 200, Bitmap.CompressFormat.PNG, Color.BLUE)
        val processor = processor()
        val result = processor.generate(ImageLabRequest(source, ImageLabProfile(1024, 85)))

        val loaded = processor.load(result.artifactRef, 100)
        assertTrue(loaded is ImageLabPreviewLoadResult.Ready)
        val bitmap = (loaded as ImageLabPreviewLoadResult.Ready).bitmap
        assertEquals(100, bitmap.width)
        assertEquals(50, bitmap.height)
        bitmap.recycle()

        candidate(workId).writeBytes(byteArrayOf(1, 2, 3))
        assertTrue(processor.load(result.artifactRef, 100) is ImageLabPreviewLoadResult.Error)
        assertTrue(candidate(workId).delete())
        assertTrue(processor.load(result.artifactRef, 100) is ImageLabPreviewLoadResult.Unavailable)
    }

    private fun assertOrientation(orientation: Int, expected: List<List<Int>>) {
        val source = Bitmap.createBitmap(3, 2, Bitmap.Config.ARGB_8888)
        listOf(A, B, C, D, E, F).forEachIndexed { index, color ->
            source.setPixel(index % 3, index / 3, color)
        }
        val transformed = processor().applyExifOrientation(source, orientation)
        try {
            assertEquals(expected.first().size, transformed.width)
            assertEquals(expected.size, transformed.height)
            expected.forEachIndexed { y, row ->
                row.forEachIndexed { x, color -> assertEquals("pixel ($x,$y)", color, transformed.getPixel(x, y)) }
            }
        } finally {
            if (transformed !== source) transformed.recycle()
            source.recycle()
        }
    }

    private fun stagedWithExif(
        workId: String,
        format: Bitmap.CompressFormat,
        orientation: Int,
        width: Int = 400,
        height: Int = 200,
    ): StagedImageLabSource {
        val source = stagedBitmap(workId, width, height, format, Color.rgb(40, 90, 160))
        ExifInterface(sourceFile(workId)).apply {
            setAttribute(ExifInterface.TAG_ORIENTATION, orientation.toString())
            saveAttributes()
        }
        return refreshedSource(workId, source, mimeFor(format))
    }

    private fun refreshedSource(
        workId: String,
        source: StagedImageLabSource,
        mimeType: String,
    ): StagedImageLabSource {
        val file = sourceFile(workId)
        return StagedImageLabSource.from(
            workId,
            StagedImage(
                "staging/$workId/source",
                source.content.copy(mimeType = mimeType, byteSize = file.length(), sha256 = file.readBytes().sha256()),
            ),
        )
    }

    private fun stagedBitmap(
        workId: String,
        width: Int,
        height: Int,
        format: Bitmap.CompressFormat,
        color: Int,
        hasTransparency: Boolean = false,
    ): StagedImageLabSource {
        val file = sourceFile(workId)
        file.parentFile?.mkdirs()
        check(file.parentFile?.isDirectory == true)
        val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        for (y in 0 until height) {
            for (x in 0 until width) {
                bitmap.setPixel(x, y, if (hasTransparency && x < width / 2) Color.TRANSPARENT else color)
            }
        }
        FileOutputStream(file).use { check(bitmap.compress(format, 95, it)) }
        bitmap.recycle()
        val content = Content(mimeFor(format), width, height, file.length(), file.readBytes().sha256())
        return StagedImageLabSource.from(workId, StagedImage("staging/$workId/source", content))
    }

    @Suppress("DEPRECATION")
    private fun mimeFor(format: Bitmap.CompressFormat): String = when (format) {
        Bitmap.CompressFormat.JPEG -> "image/jpeg"
        Bitmap.CompressFormat.PNG -> "image/png"
        Bitmap.CompressFormat.WEBP,
        Bitmap.CompressFormat.WEBP_LOSSY,
        Bitmap.CompressFormat.WEBP_LOSSLESS,
        -> "image/webp"
        else -> error("Unsupported test format: $format")
    }

    private suspend fun expectImageLabFailure(block: suspend () -> Unit) {
        try {
            block()
            fail("Expected ImageLabException")
        } catch (_: ImageLabException) {
            // Expected.
        }
    }

    private fun processor(
        afterTemporaryWritten: suspend (File) -> Unit = {},
        beforePromotion: suspend () -> Unit = {},
    ) = AndroidImageLabProcessor(
        managedRoot = managedRoot(),
        cacheRoot = cacheRoot(),
        afterTemporaryWrittenHook = afterTemporaryWritten,
        beforePromotionHook = ImageLabBeforePromotionHook { beforePromotion() },
    )

    private fun uniqueWorkId(): String = "work-${UUID.randomUUID()}"
    private fun managedRoot(): File = context.filesDir.resolve("nimroel-assets")
    private fun cacheRoot(): File = context.cacheDir.resolve("nimroel-image-lab").apply { mkdirs() }
    private fun sourceFile(workId: String): File = managedRoot().resolve("staging/$workId/source")
    private fun workDirectory(workId: String): File = cacheRoot().resolve(workId)
    private fun candidate(workId: String): File = workDirectory(workId).resolve("long1024-q85.webp")

    private fun ByteArray.sha256(): String =
        MessageDigest.getInstance("SHA-256").digest(this).joinToString("") { "%02x".format(it.toInt() and 0xff) }

    private companion object {
        val A = Color.rgb(255, 0, 0)
        val B = Color.rgb(0, 255, 0)
        val C = Color.rgb(0, 0, 255)
        val D = Color.rgb(255, 255, 0)
        val E = Color.rgb(255, 0, 255)
        val F = Color.rgb(0, 255, 255)
    }
}

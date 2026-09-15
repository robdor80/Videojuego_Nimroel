package com.nimroel.assetmanager.domain.processing

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ImageLabTest {
    @Test
    fun `landscape aspect ratio is preserved`() {
        assertEquals(ImageDimensions(1536, 1024), ImageLabResize.fit(3000, 2000, 1536))
    }

    @Test
    fun `portrait aspect ratio is preserved`() {
        assertEquals(ImageDimensions(1152, 1536), ImageLabResize.fit(3456, 4608, 1536))
    }

    @Test
    fun `smaller source is never upscaled`() {
        assertEquals(ImageDimensions(640, 480), ImageLabResize.fit(640, 480, 2048))
    }

    @Test
    fun `square image preserves square aspect ratio`() {
        assertEquals(ImageDimensions(1536, 1536), ImageLabResize.fit(3000, 3000, 1536))
    }

    @Test
    fun `one by one image remains positive and is not upscaled`() {
        assertEquals(ImageDimensions(1, 1), ImageLabResize.fit(1, 1, 2048))
    }

    @Test
    fun `source exactly at target is unchanged`() {
        assertEquals(ImageDimensions(1536, 900), ImageLabResize.fit(1536, 900, 1536))
    }

    @Test
    fun `very large dimensions do not overflow or produce zero`() {
        val result = ImageLabResize.fit(Int.MAX_VALUE, 1, 2048)

        assertEquals(ImageDimensions(2048, 1), result)
        assertTrue(result.widthPx > 0 && result.heightPx > 0)
    }

    @Test
    fun `rounding is deterministic with positive half ties upward`() {
        assertEquals(ImageDimensions(500, 167), ImageLabResize.fit(1000, 333, 500))
    }

    @Test
    fun `quality 80 is accepted`() {
        assertEquals(80, ImageLabProfile(1024, 80).quality)
    }

    @Test
    fun `quality 85 is accepted`() {
        assertEquals(85, ImageLabProfile(1280, 85).quality)
    }

    @Test
    fun `quality 90 is accepted`() {
        assertEquals(90, ImageLabProfile(2048, 90).quality)
    }

    @Test(expected = IllegalArgumentException::class)
    fun `quality outside experimental presets is rejected`() {
        ImageLabProfile(1536, 75)
    }

    @Test(expected = IllegalArgumentException::class)
    fun `invalid target long edge is rejected`() {
        ImageLabProfile(0, 85)
    }

    @Test
    fun `reduction uses real byte sizes`() {
        val reduction = requireNotNull(ImageLabMetrics.reduction(1000, 125))

        assertEquals(875L, reduction.absoluteBytes)
        assertEquals(87.5, reduction.percent, 0.0001)
    }

    @Test
    fun `invalid source byte sizes are handled without invented metrics`() {
        assertNull(ImageLabMetrics.reduction(null, 100))
        assertNull(ImageLabMetrics.reduction(0, 100))
        assertNull(ImageLabMetrics.reduction(-1, 100))
    }

    @Test
    fun `larger result reports signed negative reduction for neutral variation UI`() {
        val reduction = requireNotNull(ImageLabMetrics.reduction(100, 125))

        assertEquals(-25L, reduction.absoluteBytes)
        assertEquals(-25.0, reduction.percent, 0.0001)
    }

    @Test
    fun `result MIME is always WebP`() {
        val result = ImageLabResult(
            workId = "work-1",
            mimeType = ImageLabResult.MIME_WEBP,
            widthPx = 10,
            heightPx = 20,
            byteSize = 30,
            requestedTargetLongEdge = 1024,
            quality = 80,
            reduction = ImageLabMetrics.reduction(100, 30),
            sourceHasAlphaCapability = false,
            transparentPixelsObserved = false,
            orientationApplied = false,
            artifactRef = ImageLabArtifactRef("opaque-token"),
        )

        assertEquals("image/webp", result.mimeType)
        assertTrue(result.artifactRef.toString().contains("ImageLabArtifactRef"))
    }
}

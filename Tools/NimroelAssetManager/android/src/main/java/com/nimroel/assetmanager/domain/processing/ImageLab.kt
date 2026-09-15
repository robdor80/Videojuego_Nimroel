package com.nimroel.assetmanager.domain.processing

import com.nimroel.assetmanager.domain.model.Content
import kotlin.math.roundToInt

/** Experimental parameters only. They are deliberately not an Asset or canonical profile. */
data class ImageLabProfile(
    val targetLongEdge: Int,
    val quality: Int,
) {
    init {
        require(targetLongEdge in TARGET_LONG_EDGES) {
            "Experimental targetLongEdge must be one of $TARGET_LONG_EDGES."
        }
        require(quality in QUALITIES) { "Experimental quality must be one of $QUALITIES." }
    }

    companion object {
        val TARGET_LONG_EDGES = listOf(2048, 1536, 1280, 1024)
        val QUALITIES = listOf(90, 85, 80)
    }
}

data class ImageDimensions(val widthPx: Int, val heightPx: Int) {
    init {
        require(widthPx > 0 && heightPx > 0) { "Image dimensions must be positive." }
    }
}

object ImageLabResize {
    /**
     * Fits inside the requested long edge, never upscales, and rounds each scaled edge
     * to the nearest integer with positive .5 ties rounded upward.
     */
    fun fit(widthPx: Int, heightPx: Int, targetLongEdge: Int): ImageDimensions {
        require(widthPx > 0 && heightPx > 0) { "Source dimensions must be positive." }
        require(targetLongEdge > 0) { "targetLongEdge must be positive." }
        val sourceLongEdge = maxOf(widthPx, heightPx)
        if (sourceLongEdge <= targetLongEdge) return ImageDimensions(widthPx, heightPx)
        val scale = targetLongEdge.toDouble() / sourceLongEdge.toDouble()
        return ImageDimensions(
            widthPx = maxOf(1, (widthPx * scale).roundToInt()),
            heightPx = maxOf(1, (heightPx * scale).roundToInt()),
        )
    }
}

data class ImageLabReduction(
    val absoluteBytes: Long,
    val percent: Double,
)

enum class ImageLabExifStatus {
    ABSENT,
    NORMAL,
    TRANSFORMED,
    UNREADABLE,
}

object ImageLabMetrics {
    fun reduction(sourceBytes: Long?, resultBytes: Long): ImageLabReduction? {
        if (sourceBytes == null || sourceBytes <= 0L || resultBytes < 0L) return null
        return ImageLabReduction(
            absoluteBytes = sourceBytes - resultBytes,
            percent = (1.0 - resultBytes.toDouble() / sourceBytes.toDouble()) * 100.0,
        )
    }
}

/** A private managed staging reference. UI models never receive its relative path. */
class StagedImageLabSource internal constructor(
    val workId: String,
    internal val relativePath: String,
    val content: Content,
) {
    init {
        require(SAFE_WORK_ID.matches(workId)) { "workId is not safe." }
        require(relativePath == "staging/$workId/source") { "Unexpected managed staging reference." }
    }

    companion object {
        private val SAFE_WORK_ID = Regex("^[A-Za-z0-9_-]{1,128}$")

        fun from(workId: String, stagedImage: StagedImage): StagedImageLabSource =
            StagedImageLabSource(workId, stagedImage.relativePath, stagedImage.content)
    }
}

@JvmInline
value class ImageLabArtifactRef internal constructor(internal val value: String)

data class ImageLabRequest(
    val source: StagedImageLabSource,
    val profile: ImageLabProfile,
)

data class ImageLabResult(
    val workId: String,
    val mimeType: String,
    val widthPx: Int,
    val heightPx: Int,
    val byteSize: Long,
    val requestedTargetLongEdge: Int,
    val quality: Int,
    val reduction: ImageLabReduction?,
    /** Decoder capability on the sampled source raster, not proof of transparent pixels. */
    val sourceHasAlphaCapability: Boolean,
    /** True only when at least one transparent pixel was observed in the sampled source raster. */
    val transparentPixelsObserved: Boolean,
    val orientationApplied: Boolean,
    val exifStatus: ImageLabExifStatus = ImageLabExifStatus.ABSENT,
    val artifactRef: ImageLabArtifactRef,
) {
    init {
        require(mimeType == MIME_WEBP) { "Image Lab results must be WebP." }
        require(widthPx > 0 && heightPx > 0 && byteSize > 0L) { "Invalid generated result." }
    }

    companion object {
        const val MIME_WEBP = "image/webp"
    }
}

interface ImageLabProcessor {
    suspend fun generate(request: ImageLabRequest): ImageLabResult
    suspend fun clear(workId: String)
}

class ImageLabException(message: String, cause: Throwable? = null) : Exception(message, cause)

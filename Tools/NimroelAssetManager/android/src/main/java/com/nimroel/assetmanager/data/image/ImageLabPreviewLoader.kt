package com.nimroel.assetmanager.data.image

import android.graphics.Bitmap
import com.nimroel.assetmanager.domain.processing.ImageLabArtifactRef

fun interface ImageLabPreviewLoader {
    suspend fun load(artifactRef: ImageLabArtifactRef, maxLongEdge: Int): ImageLabPreviewLoadResult
}

sealed interface ImageLabPreviewLoadResult {
    data class Ready(val bitmap: Bitmap) : ImageLabPreviewLoadResult
    data object Unavailable : ImageLabPreviewLoadResult
    data class Error(val message: String) : ImageLabPreviewLoadResult
}

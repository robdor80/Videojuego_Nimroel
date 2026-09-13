package com.nimroel.assetmanager.domain.processing

import com.nimroel.assetmanager.domain.model.Content

@JvmInline
value class ImageSourceRef(val value: String) {
    init {
        require(value.isNotBlank()) { "Image source reference cannot be blank." }
    }
}

data class PreparedImage(
    val sourceRef: ImageSourceRef,
    val content: Content,
)

fun interface ImageContentPreparer {
    suspend fun prepare(sourceRef: ImageSourceRef): PreparedImage
}

class ImagePreparationException(message: String, cause: Throwable? = null) : IllegalArgumentException(message, cause)

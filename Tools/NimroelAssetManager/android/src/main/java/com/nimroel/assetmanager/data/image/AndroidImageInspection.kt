package com.nimroel.assetmanager.data.image

import android.graphics.BitmapFactory
import java.io.InputStream

internal val ANDROID_IMAGE_MIME = Regex("^image/[a-z0-9.+-]+$")

internal data class DecodedImageBounds(
    val widthPx: Int,
    val heightPx: Int,
    val decoderMimeType: String?,
)

internal fun decodeImageBounds(input: InputStream): DecodedImageBounds {
    val options = BitmapFactory.Options().apply { inJustDecodeBounds = true }
    BitmapFactory.decodeStream(input, null, options)
    return DecodedImageBounds(
        widthPx = options.outWidth,
        heightPx = options.outHeight,
        decoderMimeType = options.outMimeType?.trim()?.lowercase()?.normalizeImageMimeAlias(),
    )
}

internal fun String.normalizeImageMimeAlias(): String = if (this == "image/jpg") "image/jpeg" else this

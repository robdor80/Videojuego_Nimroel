package com.nimroel.assetmanager.domain.model

/**
 * Stable logical identity of an asset. Its final textual convention remains an open contract decision.
 */
@JvmInline
value class AssetId(val value: String) {
    init {
        require(value.isNotBlank()) { "An asset ID cannot be blank." }
    }
}

package com.nimroel.assetmanager.domain.model

/** Minimal, provider-independent representation until schema v1 is agreed. */
data class AssetRecord(
    val schemaVersion: Int,
    val id: AssetId,
    val localState: LocalAssetState,
    val contentHash: String? = null,
)

enum class LocalAssetState {
    DRAFT,
    READY_FOR_SYNC,
    SYNCED,
    SYNC_FAILED,
}

package com.nimroel.assetmanager.domain.storage

import com.nimroel.assetmanager.domain.model.AssetId

/**
 * Boundary for a future authenticated remote storage implementation.
 * Client-side ImageKit private credentials must never be used here.
 */
interface RemoteAssetStore {
    suspend fun sync(assetId: AssetId): RemoteSyncResult
}

sealed interface RemoteSyncResult {
    data object Deferred : RemoteSyncResult
    data class Failed(val reason: String) : RemoteSyncResult
}

package com.nimroel.assetmanager.domain.storage

import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import java.time.Instant

/** Domain-facing boundary for the installation-local asset library. */
interface LocalAssetStore : IngestWorkItemStore {
    suspend fun saveAsset(asset: Asset)
    suspend fun asset(assetId: AssetId): Asset?
    suspend fun containsAsset(assetId: AssetId): Boolean
    suspend fun assets(): List<Asset>
    suspend fun assetsByType(type: AssetType): List<Asset>
    suspend fun assetsByLifecycleStatus(status: LifecycleStatus): List<Asset>
    suspend fun assetsByRealmId(realmId: String): List<Asset>
    suspend fun assetsByCultureId(cultureId: String): List<Asset>
    suspend fun assetsBySubjectEntityId(subjectEntityId: String): List<Asset>
    suspend fun rebuildProjections(): ProjectionRebuildReport

    suspend fun saveLocalState(state: AssetLocalState)
    suspend fun localState(assetId: AssetId): AssetLocalState?

    suspend fun saveRepresentation(representation: LocalRepresentation)
    suspend fun representations(assetId: AssetId): List<LocalRepresentation>

    /** Atomically installs all Room state produced by one completed ingest operation. */
    suspend fun commitIngestedAsset(
        workId: String,
        asset: Asset,
        localState: AssetLocalState,
        representations: List<LocalRepresentation>,
        committedAt: Instant,
    )
}

/** Narrow operational boundary used by local staging before an Asset exists. */
interface IngestWorkItemStore {
    suspend fun createIngestWorkItem(workItem: IngestWorkItem)
    suspend fun transitionIngestWorkItem(transition: IngestWorkTransition): IngestWorkItem?
    suspend fun ingestWorkItem(workId: String): IngestWorkItem?
    suspend fun ingestWorkItemByReservedAssetId(assetId: AssetId): IngestWorkItem?
}

data class ProjectionRebuildReport(
    val rebuiltCount: Int,
    val unreadableAssetIds: List<String>,
)

enum class AssetAvailability(val wireValue: String) {
    AVAILABLE("available"),
    DEGRADED("degraded"),
    UNAVAILABLE("unavailable");

    companion object {
        fun fromWireValue(value: String): AssetAvailability =
            entries.firstOrNull { it.wireValue == value }
                ?: throw IllegalArgumentException("Unknown asset availability: $value")
    }
}

data class AssetLocalState(
    val assetId: AssetId,
    val availability: AssetAvailability,
    val lastReconciledAt: Instant? = null,
    val diagnosticCode: String? = null,
    val diagnosticDetail: String? = null,
)

enum class RepresentationRole(val wireValue: String) {
    SOURCE_ORIGINAL("source_original"),
    CANONICAL("canonical"),
    THUMBNAIL("thumbnail");

    companion object {
        fun fromWireValue(value: String): RepresentationRole =
            entries.firstOrNull { it.wireValue == value }
                ?: throw IllegalArgumentException("Unknown representation role: $value")
    }
}

enum class RepresentationAvailability(val wireValue: String) {
    PRESENT("present"),
    MISSING("missing"),
    CORRUPT("corrupt");

    companion object {
        fun fromWireValue(value: String): RepresentationAvailability =
            entries.firstOrNull { it.wireValue == value }
                ?: throw IllegalArgumentException("Unknown representation availability: $value")
    }
}

data class LocalRepresentation(
    val representationId: String,
    val assetId: AssetId,
    val role: RepresentationRole,
    val relativePath: String,
    val mimeType: String,
    val sha256: String,
    val widthPx: Int? = null,
    val heightPx: Int? = null,
    val byteSize: Long,
    val availability: RepresentationAvailability,
)

enum class IngestWorkState(val wireValue: String) {
    QUEUED("queued"),
    PROCESSING("processing"),
    READY_TO_COMMIT("ready_to_commit"),
    FAILED("failed"),
    COMMITTED("committed");

    companion object {
        fun fromWireValue(value: String): IngestWorkState =
            entries.firstOrNull { it.wireValue == value }
                ?: throw IllegalArgumentException("Unknown ingest work state: $value")
    }
}

data class IngestWorkItem(
    val workId: String,
    val reservedAssetId: AssetId,
    val sourceUri: String,
    val state: IngestWorkState,
    val stagingRelativePath: String? = null,
    val createdAt: Instant,
    val updatedAt: Instant,
    val errorCode: String? = null,
    val errorDetail: String? = null,
)

data class IngestWorkTransition(
    val workId: String,
    val expectedState: IngestWorkState,
    val targetState: IngestWorkState,
    val updatedAt: Instant,
    val stagingRelativePath: String? = null,
    val errorCode: String? = null,
    val errorDetail: String? = null,
)

object IngestWorkTransitionPolicy {
    private val allowed = setOf(
        IngestWorkState.QUEUED to IngestWorkState.PROCESSING,
        IngestWorkState.PROCESSING to IngestWorkState.READY_TO_COMMIT,
        IngestWorkState.PROCESSING to IngestWorkState.FAILED,
    )

    fun apply(current: IngestWorkItem, transition: IngestWorkTransition): IngestWorkItem {
        require(transition.workId == current.workId) { "Transition workId must match the current work item." }
        require(current.state == transition.expectedState) { "Ingest work item is not in the expected state." }
        require(transition.expectedState to transition.targetState in allowed) {
            "Transition ${transition.expectedState.wireValue} -> ${transition.targetState.wireValue} is not allowed."
        }
        require(!transition.updatedAt.isBefore(current.updatedAt)) { "Transition timestamp cannot move backwards." }
        when (transition.targetState) {
            IngestWorkState.PROCESSING -> require(
                transition.stagingRelativePath == null && transition.errorCode == null && transition.errorDetail == null,
            ) { "Processing cannot publish staging or an error." }

            IngestWorkState.READY_TO_COMMIT -> {
                require(!transition.stagingRelativePath.isNullOrBlank()) { "Ready work requires a staging path." }
                require(transition.errorCode == null && transition.errorDetail == null) { "Ready work cannot retain an error." }
            }

            IngestWorkState.FAILED -> {
                require(!transition.errorCode.isNullOrBlank()) { "Failed work requires an error code." }
                require(!transition.errorDetail.isNullOrBlank()) { "Failed work requires error detail." }
                require(transition.errorDetail.length <= 240) { "Failed work error detail is too long." }
                require(transition.stagingRelativePath == null) { "Failed work cannot publish a staging path." }
            }

            else -> error("Unsupported transition target.")
        }
        return current.copy(
            state = transition.targetState,
            stagingRelativePath = transition.stagingRelativePath,
            updatedAt = transition.updatedAt,
            errorCode = transition.errorCode,
            errorDetail = transition.errorDetail,
        )
    }
}

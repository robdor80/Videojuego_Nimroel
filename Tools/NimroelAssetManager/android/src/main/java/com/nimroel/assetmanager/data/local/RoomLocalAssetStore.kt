package com.nimroel.assetmanager.data.local

import androidx.room.withTransaction
import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.storage.AssetLocalState
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.IngestWorkTransition
import com.nimroel.assetmanager.domain.storage.IngestWorkTransitionPolicy
import com.nimroel.assetmanager.domain.storage.LocalAssetStore
import com.nimroel.assetmanager.domain.storage.LocalRepresentation
import com.nimroel.assetmanager.domain.storage.ProjectionRebuildReport
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant

internal class RoomLocalAssetStore(
    private val database: NimroelAssetDatabase,
) : LocalAssetStore {
    private val documents get() = database.assetDocuments()
    private val localStates get() = database.assetLocalStates()
    private val representationDao get() = database.localRepresentations()
    private val ingestWorkItems get() = database.ingestWorkItems()

    override suspend fun saveAsset(asset: Asset) {
        val document = AssetDocumentProjector.project(asset)
        database.withTransaction {
            representationDao.findByAssetId(asset.assetId.value)
                .map(LocalRepresentationEntity::toDomain)
                .forEach { validateCanonicalRepresentation(it, asset) }
            documents.upsert(document)
        }
    }

    override suspend fun asset(assetId: AssetId): Asset? =
        documents.find(assetId.value)?.let(AssetDocumentProjector::restore)

    override suspend fun containsAsset(assetId: AssetId): Boolean = documents.exists(assetId.value)

    override suspend fun assets(): List<Asset> = documents.listAll().map(AssetDocumentProjector::restore)

    override suspend fun assetsByType(type: AssetType): List<Asset> =
        documents.findByAssetType(CanonicalWireValues.assetType(type)).map(AssetDocumentProjector::restore)

    override suspend fun assetsByLifecycleStatus(status: LifecycleStatus): List<Asset> =
        documents.findByLifecycleStatus(CanonicalWireValues.lifecycleStatus(status)).map(AssetDocumentProjector::restore)

    override suspend fun assetsByRealmId(realmId: String): List<Asset> =
        documents.findByRealmId(realmId).map(AssetDocumentProjector::restore)

    override suspend fun assetsByCultureId(cultureId: String): List<Asset> =
        documents.findByCultureId(cultureId).map(AssetDocumentProjector::restore)

    override suspend fun assetsBySubjectEntityId(subjectEntityId: String): List<Asset> =
        documents.findBySubjectEntityId(subjectEntityId).map(AssetDocumentProjector::restore)

    override suspend fun rebuildProjections(): ProjectionRebuildReport = database.withTransaction {
        var rebuiltCount = 0
        val unreadableAssetIds = mutableListOf<String>()
        documents.listAll().forEach { current ->
            try {
                val rebuilt = AssetDocumentProjector.project(AssetDocumentProjector.restore(current))
                    .copy(canonicalJson = current.canonicalJson)
                documents.upsert(rebuilt)
                rebuiltCount += 1
            } catch (_: InvalidStoredAssetException) {
                unreadableAssetIds += current.assetId
            }
        }
        ProjectionRebuildReport(rebuiltCount, unreadableAssetIds)
    }

    override suspend fun saveLocalState(state: AssetLocalState) {
        localStates.upsert(state.toEntity())
    }

    override suspend fun localState(assetId: AssetId): AssetLocalState? =
        localStates.find(assetId.value)?.toDomain()

    override suspend fun saveRepresentation(representation: LocalRepresentation) {
        val entity = representation.toEntity()
        database.withTransaction {
            documents.find(representation.assetId.value)?.let { document ->
                validateCanonicalRepresentation(representation, AssetDocumentProjector.restore(document))
            }
            representationDao.upsert(entity)
        }
    }

    override suspend fun representations(assetId: AssetId): List<LocalRepresentation> =
        representationDao.findByAssetId(assetId.value).map(LocalRepresentationEntity::toDomain)

    override suspend fun createIngestWorkItem(workItem: IngestWorkItem) {
        require(workItem.state == IngestWorkState.QUEUED) { "A new ingest work item must start queued." }
        require(workItem.stagingRelativePath == null) { "A queued work item cannot publish staging." }
        require(workItem.errorCode == null && workItem.errorDetail == null) { "A queued work item cannot contain an error." }
        ingestWorkItems.insert(workItem.toEntity())
    }

    override suspend fun transitionIngestWorkItem(transition: IngestWorkTransition): IngestWorkItem? =
        database.withTransaction {
            val current = ingestWorkItems.find(transition.workId)?.toDomain() ?: return@withTransaction null
            val updated = IngestWorkTransitionPolicy.apply(current, transition)
            // Keep conditional DAO writes behind the same persistence validation as inserts.
            val updatedEntity = updated.toEntity()
            val changed = ingestWorkItems.transition(
                workId = updatedEntity.workId,
                expectedState = transition.expectedState,
                targetState = updatedEntity.state,
                stagingRelativePath = updatedEntity.stagingRelativePath,
                updatedAt = updatedEntity.updatedAt,
                errorCode = updatedEntity.errorCode,
                errorDetail = updatedEntity.errorDetail,
            )
            if (changed == 1) updated else null
        }

    override suspend fun ingestWorkItem(workId: String): IngestWorkItem? =
        ingestWorkItems.find(workId)?.toDomain()

    override suspend fun ingestWorkItemByReservedAssetId(assetId: AssetId): IngestWorkItem? =
        ingestWorkItems.findByReservedAssetId(assetId.value)?.toDomain()

    override suspend fun commitIngestedAsset(
        workId: String,
        asset: Asset,
        localState: AssetLocalState,
        representations: List<LocalRepresentation>,
        committedAt: Instant,
    ) {
        val document = AssetDocumentProjector.project(asset)
        require(localState.assetId == asset.assetId) { "Local state must belong to the committed Asset." }
        require(representations.all { it.assetId == asset.assetId }) { "Every representation must belong to the committed Asset." }
        representations.forEach { validateCanonicalRepresentation(it, asset) }
        val stateEntity = localState.toEntity()
        val representationEntities = representations.map(LocalRepresentation::toEntity)

        database.withTransaction {
            val workItem = checkNotNull(ingestWorkItems.find(workId)) { "Ingest work item $workId does not exist." }
            require(workItem.reservedAssetId == asset.assetId.value) { "The work item reserved a different assetId." }
            require(workItem.state == IngestWorkState.READY_TO_COMMIT) { "The work item must be ready_to_commit." }

            documents.upsert(document)
            localStates.upsert(stateEntity)
            representationDao.upsertAll(representationEntities)
            check(
                ingestWorkItems.transition(
                    workId = workId,
                    expectedState = IngestWorkState.READY_TO_COMMIT,
                    targetState = IngestWorkState.COMMITTED,
                    stagingRelativePath = workItem.stagingRelativePath,
                    updatedAt = committedAt,
                    errorCode = null,
                    errorDetail = null,
                ) == 1,
            )
        }
    }
}

private fun AssetLocalState.toEntity() = AssetLocalStateEntity(
    assetId = assetId.value,
    availability = availability,
    lastReconciledAt = lastReconciledAt,
    diagnosticCode = diagnosticCode,
    diagnosticDetail = diagnosticDetail,
)

private fun AssetLocalStateEntity.toDomain() = AssetLocalState(
    assetId = AssetId.parse(assetId),
    availability = availability,
    lastReconciledAt = lastReconciledAt,
    diagnosticCode = diagnosticCode,
    diagnosticDetail = diagnosticDetail,
)

private fun LocalRepresentation.toEntity(): LocalRepresentationEntity {
    require(representationId.isNotBlank()) { "representationId cannot be blank." }
    require(isManagedRelativePath(relativePath)) { "relativePath must be normalized and relative to the managed root." }
    require(Regex("^image/[a-z0-9.+-]+$").matches(mimeType)) { "mimeType must be a valid image MIME type." }
    require(Regex("^[0-9a-f]{64}$").matches(sha256)) { "sha256 must be 64 lowercase hexadecimal characters." }
    require(widthPx?.let { it > 0 } != false && heightPx?.let { it > 0 } != false) { "Dimensions must be positive when present." }
    require(byteSize > 0) { "byteSize must be positive." }
    return LocalRepresentationEntity(representationId, assetId.value, role, relativePath, mimeType, sha256, widthPx, heightPx, byteSize, availability)
}

private fun LocalRepresentationEntity.toDomain() = LocalRepresentation(
    representationId,
    AssetId.parse(assetId),
    role,
    relativePath,
    mimeType,
    sha256,
    widthPx,
    heightPx,
    byteSize,
    availability,
)

private fun IngestWorkItem.toEntity(): IngestWorkItemEntity {
    require(workId.isNotBlank()) { "workId cannot be blank." }
    require(sourceUri.isNotBlank()) { "sourceUri cannot be blank." }
    require(!updatedAt.isBefore(createdAt)) { "updatedAt cannot precede createdAt." }
    require(stagingRelativePath == null || isManagedRelativePath(stagingRelativePath)) { "stagingRelativePath must be normalized and relative to the managed root." }
    return IngestWorkItemEntity(workId, reservedAssetId.value, sourceUri, state, stagingRelativePath, createdAt, updatedAt, errorCode, errorDetail)
}

private fun IngestWorkItemEntity.toDomain() = IngestWorkItem(
    workId,
    AssetId.parse(reservedAssetId),
    sourceUri,
    state,
    stagingRelativePath,
    createdAt,
    updatedAt,
    errorCode,
    errorDetail,
)

private fun isManagedRelativePath(value: String): Boolean {
    if (value.isBlank() || value.startsWith('/') || '\\' in value || ':' in value) return false
    return value.split('/').all { segment -> segment.isNotEmpty() && segment != "." && segment != ".." }
}

private fun validateCanonicalRepresentation(representation: LocalRepresentation, asset: Asset) {
    if (representation.role != RepresentationRole.CANONICAL || representation.availability != RepresentationAvailability.PRESENT) return
    require(representation.sha256 == asset.content.sha256) { "A present canonical representation must match content.sha256." }
    require(representation.mimeType == asset.content.mimeType) { "A present canonical representation must match content.mimeType." }
    require(representation.widthPx == asset.content.widthPx && representation.heightPx == asset.content.heightPx) {
        "A present canonical representation must match content dimensions."
    }
    require(asset.content.byteSize == null || representation.byteSize == asset.content.byteSize) {
        "A present canonical representation must match content.byteSize when declared."
    }
}

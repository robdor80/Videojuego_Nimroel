package com.nimroel.assetmanager.data.local

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey
import com.nimroel.assetmanager.domain.storage.AssetAvailability
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant

internal const val CURRENT_PROJECTION_VERSION = 1

@Entity(
    tableName = "asset_documents",
    indices = [
        Index(value = ["asset_type"], name = "index_asset_documents_asset_type"),
        Index(value = ["lifecycle_status"], name = "index_asset_documents_lifecycle_status"),
        Index(value = ["subject_entity_id"], name = "index_asset_documents_subject_entity_id"),
        Index(value = ["realm_id"], name = "index_asset_documents_realm_id"),
        Index(value = ["culture_id"], name = "index_asset_documents_culture_id"),
    ],
)
internal data class AssetDocumentEntity(
    @PrimaryKey @ColumnInfo(name = "asset_id") val assetId: String,
    @ColumnInfo(name = "schema_version") val schemaVersion: Int,
    @ColumnInfo(name = "canonical_json") val canonicalJson: String,
    @ColumnInfo(name = "asset_type") val assetType: String,
    @ColumnInfo(name = "lifecycle_status") val lifecycleStatus: String,
    @ColumnInfo(name = "realm_id") val realmId: String?,
    @ColumnInfo(name = "culture_id") val cultureId: String?,
    @ColumnInfo(name = "subject_entity_id") val subjectEntityId: String?,
    @ColumnInfo(name = "projection_version") val projectionVersion: Int,
)

@Entity(
    tableName = "asset_local_state",
    foreignKeys = [
        ForeignKey(
            entity = AssetDocumentEntity::class,
            parentColumns = ["asset_id"],
            childColumns = ["asset_id"],
            onDelete = ForeignKey.NO_ACTION,
            onUpdate = ForeignKey.NO_ACTION,
        ),
    ],
)
internal data class AssetLocalStateEntity(
    @PrimaryKey @ColumnInfo(name = "asset_id") val assetId: String,
    val availability: AssetAvailability,
    @ColumnInfo(name = "last_reconciled_at") val lastReconciledAt: Instant?,
    @ColumnInfo(name = "diagnostic_code") val diagnosticCode: String?,
    @ColumnInfo(name = "diagnostic_detail") val diagnosticDetail: String?,
)

@Entity(
    tableName = "local_representations",
    foreignKeys = [
        ForeignKey(
            entity = AssetDocumentEntity::class,
            parentColumns = ["asset_id"],
            childColumns = ["asset_id"],
            onDelete = ForeignKey.NO_ACTION,
            onUpdate = ForeignKey.NO_ACTION,
        ),
    ],
    indices = [Index(value = ["asset_id"], name = "index_local_representations_asset_id")],
)
internal data class LocalRepresentationEntity(
    @PrimaryKey @ColumnInfo(name = "representation_id") val representationId: String,
    @ColumnInfo(name = "asset_id") val assetId: String,
    val role: RepresentationRole,
    @ColumnInfo(name = "relative_path") val relativePath: String,
    @ColumnInfo(name = "mime_type") val mimeType: String,
    val sha256: String,
    @ColumnInfo(name = "width_px") val widthPx: Int?,
    @ColumnInfo(name = "height_px") val heightPx: Int?,
    @ColumnInfo(name = "byte_size") val byteSize: Long,
    val availability: RepresentationAvailability,
)

@Entity(
    tableName = "ingest_work_items",
    indices = [
        Index(
            value = ["reserved_asset_id"],
            unique = true,
            name = "index_ingest_work_items_reserved_asset_id",
        ),
    ],
)
internal data class IngestWorkItemEntity(
    @PrimaryKey @ColumnInfo(name = "work_id") val workId: String,
    @ColumnInfo(name = "reserved_asset_id") val reservedAssetId: String,
    @ColumnInfo(name = "source_uri") val sourceUri: String,
    val state: IngestWorkState,
    @ColumnInfo(name = "staging_relative_path") val stagingRelativePath: String?,
    @ColumnInfo(name = "created_at") val createdAt: Instant,
    @ColumnInfo(name = "updated_at") val updatedAt: Instant,
    @ColumnInfo(name = "error_code") val errorCode: String?,
    @ColumnInfo(name = "error_detail") val errorDetail: String?,
)

internal data class AssetDocumentOverview(
    @ColumnInfo(name = "asset_id") val assetId: String,
    @ColumnInfo(name = "schema_version") val schemaVersion: Int,
    @ColumnInfo(name = "asset_type") val assetType: String,
    @ColumnInfo(name = "lifecycle_status") val lifecycleStatus: String,
    @ColumnInfo(name = "realm_id") val realmId: String?,
    @ColumnInfo(name = "culture_id") val cultureId: String?,
    @ColumnInfo(name = "subject_entity_id") val subjectEntityId: String?,
    @ColumnInfo(name = "projection_version") val projectionVersion: Int,
)

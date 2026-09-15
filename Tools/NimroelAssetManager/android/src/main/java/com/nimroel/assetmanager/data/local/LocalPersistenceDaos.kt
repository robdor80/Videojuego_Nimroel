package com.nimroel.assetmanager.data.local

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Upsert
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import java.time.Instant

@Dao
internal interface AssetDocumentDao {
    @Upsert suspend fun upsert(document: AssetDocumentEntity)

    @Query("SELECT * FROM asset_documents WHERE asset_id = :assetId")
    suspend fun find(assetId: String): AssetDocumentEntity?

    @Query("SELECT EXISTS(SELECT 1 FROM asset_documents WHERE asset_id = :assetId)")
    suspend fun exists(assetId: String): Boolean

    @Query("SELECT asset_id, schema_version, asset_type, lifecycle_status, realm_id, culture_id, subject_entity_id, projection_version FROM asset_documents ORDER BY asset_id")
    suspend fun listOverviews(): List<AssetDocumentOverview>

    @Query("SELECT * FROM asset_documents ORDER BY asset_id")
    suspend fun listAll(): List<AssetDocumentEntity>

    @Query("SELECT * FROM asset_documents WHERE asset_type = :assetType ORDER BY asset_id")
    suspend fun findByAssetType(assetType: String): List<AssetDocumentEntity>

    @Query("SELECT * FROM asset_documents WHERE lifecycle_status = :lifecycleStatus ORDER BY asset_id")
    suspend fun findByLifecycleStatus(lifecycleStatus: String): List<AssetDocumentEntity>

    @Query("SELECT * FROM asset_documents WHERE subject_entity_id = :subjectEntityId ORDER BY asset_id")
    suspend fun findBySubjectEntityId(subjectEntityId: String): List<AssetDocumentEntity>

    @Query("SELECT * FROM asset_documents WHERE realm_id = :realmId ORDER BY asset_id")
    suspend fun findByRealmId(realmId: String): List<AssetDocumentEntity>

    @Query("SELECT * FROM asset_documents WHERE culture_id = :cultureId ORDER BY asset_id")
    suspend fun findByCultureId(cultureId: String): List<AssetDocumentEntity>
}

@Dao
internal interface AssetLocalStateDao {
    @Upsert suspend fun upsert(state: AssetLocalStateEntity)

    @Query("SELECT * FROM asset_local_state WHERE asset_id = :assetId")
    suspend fun find(assetId: String): AssetLocalStateEntity?
}

@Dao
internal interface LocalRepresentationDao {
    @Upsert suspend fun upsert(representation: LocalRepresentationEntity)

    @Upsert suspend fun upsertAll(representations: List<LocalRepresentationEntity>)

    @Query("SELECT * FROM local_representations WHERE asset_id = :assetId ORDER BY representation_id")
    suspend fun findByAssetId(assetId: String): List<LocalRepresentationEntity>
}

@Dao
internal interface IngestWorkItemDao {
    @Insert(onConflict = OnConflictStrategy.ABORT)
    suspend fun insert(workItem: IngestWorkItemEntity)

    @Query(
        """
        UPDATE ingest_work_items
        SET state = :targetState,
            staging_relative_path = :stagingRelativePath,
            updated_at = :updatedAt,
            error_code = :errorCode,
            error_detail = :errorDetail
        WHERE work_id = :workId AND state = :expectedState
        """,
    )
    suspend fun transition(
        workId: String,
        expectedState: IngestWorkState,
        targetState: IngestWorkState,
        stagingRelativePath: String?,
        updatedAt: Instant,
        errorCode: String?,
        errorDetail: String?,
    ): Int

    @Query("DELETE FROM ingest_work_items WHERE work_id = :workId AND state = :readyState")
    suspend fun deleteReady(workId: String, readyState: IngestWorkState): Int

    @Query("SELECT * FROM ingest_work_items WHERE work_id = :workId")
    suspend fun find(workId: String): IngestWorkItemEntity?

    @Query("SELECT * FROM ingest_work_items WHERE reserved_asset_id = :assetId")
    suspend fun findByReservedAssetId(assetId: String): IngestWorkItemEntity?
}

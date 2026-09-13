package com.nimroel.assetmanager.data.local

import android.content.Context
import android.database.sqlite.SQLiteConstraintException
import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.model.Classification
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.Subject
import com.nimroel.assetmanager.domain.storage.AssetLocalState
import com.nimroel.assetmanager.domain.storage.AssetAvailability
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.LocalRepresentation
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant
import kotlinx.coroutines.runBlocking
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertThrows
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [35])
class RoomLocalAssetStoreTest {
    private lateinit var database: NimroelAssetDatabase
    private lateinit var store: RoomLocalAssetStore

    @Before
    fun setUp() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        database = Room.inMemoryDatabaseBuilder(context, NimroelAssetDatabase::class.java)
            .allowMainThreadQueries()
            .build()
        store = RoomLocalAssetStore(database)
    }

    @After
    fun tearDown() = database.close()

    @Test
    fun `valid Asset persists and restores without losing typed details extensions or optionals`() = runBlocking {
        val asset = TestAssets.withExtensionsAndOptionalFields()

        store.saveAsset(asset)

        assertTrue(store.containsAsset(asset.assetId))
        assertEquals(asset, store.asset(asset.assetId))
        assertEquals(listOf(asset), store.assets())
    }

    @Test
    fun `saving allowed metadata changes updates canonical JSON and every projection coherently`() = runBlocking {
        val original = TestAssets.fixture()
        store.saveAsset(original)
        val updated = original.copy(
            lifecycle = original.lifecycle.copy(status = LifecycleStatus.DEPRECATED, note = "Superseded editorial metadata"),
            classification = Classification(realmId = "norgard", cultureId = "norgard"),
            subject = Subject(entityId = "npc.norgard.farmer"),
        )

        store.saveAsset(updated)

        assertEquals(updated, store.asset(original.assetId))
        val row = checkNotNull(database.assetDocuments().find(original.assetId.value))
        assertEquals("deprecated", row.lifecycleStatus)
        assertEquals("norgard", row.realmId)
        assertEquals("norgard", row.cultureId)
        assertEquals("npc.norgard.farmer", row.subjectEntityId)
        assertEquals(listOf(updated), store.assetsByLifecycleStatus(LifecycleStatus.DEPRECATED))
        assertEquals(listOf(updated), store.assetsByType(updated.type))
        assertEquals(listOf(updated), store.assetsByRealmId("norgard"))
        assertEquals(listOf(updated), store.assetsByCultureId("norgard"))
        assertEquals(listOf(updated), store.assetsBySubjectEntityId("npc.norgard.farmer"))
    }

    @Test
    fun `projections can be rebuilt from canonical JSON without changing it`() = runBlocking {
        val asset = TestAssets.withExtensionsAndOptionalFields()
        store.saveAsset(asset)
        val originalJson = checkNotNull(database.assetDocuments().find(asset.assetId.value)).canonicalJson
        database.openHelper.writableDatabase.execSQL(
            "UPDATE asset_documents SET asset_type = 'landscape', lifecycle_status = 'retired', projection_version = 0 WHERE asset_id = ?",
            arrayOf(asset.assetId.value),
        )

        val report = store.rebuildProjections()

        assertEquals(1, report.rebuiltCount)
        assertTrue(report.unreadableAssetIds.isEmpty())
        val rebuilt = checkNotNull(database.assetDocuments().find(asset.assetId.value))
        assertEquals("npc_portrait", rebuilt.assetType)
        assertEquals("approved", rebuilt.lifecycleStatus)
        assertEquals(CURRENT_PROJECTION_VERSION, rebuilt.projectionVersion)
        assertEquals(originalJson, rebuilt.canonicalJson)
    }

    @Test
    fun `unsupported future schema JSON is preserved and isolated during projection rebuild`() = runBlocking {
        val asset = TestAssets.fixture()
        val current = AssetDocumentProjector.project(asset)
        val futureJson = current.canonicalJson.replaceFirst("\"schemaVersion\":1", "\"schemaVersion\":2")
        database.assetDocuments().upsert(current.copy(schemaVersion = 2, canonicalJson = futureJson, projectionVersion = 0))

        val report = store.rebuildProjections()

        assertEquals(0, report.rebuiltCount)
        assertEquals(listOf(asset.assetId.value), report.unreadableAssetIds)
        assertEquals(futureJson, database.assetDocuments().find(asset.assetId.value)?.canonicalJson)
        assertThrows(InvalidStoredAssetException::class.java) {
            runBlocking { store.asset(asset.assetId) }
        }
        Unit
    }

    @Test
    fun `invalid Asset never reaches Room`() = runBlocking {
        val original = TestAssets.fixture()
        val invalid = original.copy(content = original.content.copy(sha256 = "INVALID"))

        assertThrows(InvalidAssetForPersistenceException::class.java) { runBlocking { store.saveAsset(invalid) } }
        assertFalse(store.containsAsset(original.assetId))
    }

    @Test
    fun `operational local state is stored separately and never enters canonical JSON`() = runBlocking {
        val asset = TestAssets.fixture()
        store.saveAsset(asset)
        val state = AssetLocalState(
            asset.assetId,
            AssetAvailability.DEGRADED,
            Instant.parse("2026-09-13T10:00:00Z"),
            "thumbnail_missing",
            "Regenerable derivative is absent",
        )

        store.saveLocalState(state)

        assertEquals(state, store.localState(asset.assetId))
        val json = checkNotNull(database.assetDocuments().find(asset.assetId.value)).canonicalJson
        assertFalse("canonical JSON must not contain local availability", json.contains("degraded"))
        assertFalse("canonical JSON must not contain diagnostics", json.contains("thumbnail_missing"))
    }

    @Test
    fun `ingest may reserve an Asset ID before the document exists and reservation is unique`() = runBlocking {
        val assetId = TestAssets.fixture().assetId
        val work = workItem("work-1", assetId.value)

        store.createIngestWorkItem(work)

        assertFalse(store.containsAsset(assetId))
        assertEquals(work, store.ingestWorkItem("work-1"))
        assertEquals(work, store.ingestWorkItemByReservedAssetId(assetId))
        val processing = work.copy(state = IngestWorkState.PROCESSING, updatedAt = work.updatedAt.plusSeconds(1))
        assertTrue(store.updateIngestWorkItem(processing))
        assertEquals(processing, store.ingestWorkItem("work-1"))
        assertThrows(SQLiteConstraintException::class.java) {
            runBlocking { store.createIngestWorkItem(work.copy(workId = "work-2")) }
        }
        Unit
    }

    @Test
    fun `foreign keys reject orphans and NO ACTION prevents destructive parent deletion`() = runBlocking {
        val asset = TestAssets.fixture()
        val state = AssetLocalState(asset.assetId, AssetAvailability.AVAILABLE)

        assertThrows(SQLiteConstraintException::class.java) { runBlocking { store.saveLocalState(state) } }
        assertThrows(SQLiteConstraintException::class.java) {
            runBlocking { store.saveRepresentation(representation(asset)) }
        }

        store.saveAsset(asset)
        store.saveLocalState(state)
        store.saveRepresentation(representation(asset))
        assertThrows(SQLiteConstraintException::class.java) {
            database.openHelper.writableDatabase.execSQL(
                "DELETE FROM asset_documents WHERE asset_id = ?",
                arrayOf(asset.assetId.value),
            )
        }
        assertTrue(store.containsAsset(asset.assetId))
    }

    @Test
    fun `present canonical representation must match canonical Asset content`() = runBlocking {
        val asset = TestAssets.fixture()
        store.saveAsset(asset)

        assertThrows(IllegalArgumentException::class.java) {
            runBlocking {
                store.saveRepresentation(representation(asset).copy(sha256 = "f".repeat(64)))
            }
        }
        assertTrue(store.representations(asset.assetId).isEmpty())
    }

    @Test
    fun `bundle commit writes document local state representations and committed work atomically`() = runBlocking {
        val asset = TestAssets.fixture()
        val ready = workItem("work-commit", asset.assetId.value).copy(state = IngestWorkState.READY_TO_COMMIT)
        val state = AssetLocalState(asset.assetId, AssetAvailability.AVAILABLE)
        val representation = representation(asset)
        store.createIngestWorkItem(ready)

        store.commitIngestedAsset(
            ready.workId,
            asset,
            state,
            listOf(representation),
            Instant.parse("2026-09-13T11:00:00Z"),
        )

        assertEquals(asset, store.asset(asset.assetId))
        assertEquals(state, store.localState(asset.assetId))
        assertEquals(listOf(representation), store.representations(asset.assetId))
        assertEquals(IngestWorkState.COMMITTED, store.ingestWorkItem(ready.workId)?.state)
    }

    @Test
    fun `failed bundle preconditions leave no partial Asset state`() = runBlocking {
        val asset = TestAssets.fixture()
        val queued = workItem("work-not-ready", asset.assetId.value)
        store.createIngestWorkItem(queued)

        assertThrows(IllegalArgumentException::class.java) {
            runBlocking {
                store.commitIngestedAsset(
                    queued.workId,
                    asset,
                    AssetLocalState(asset.assetId, AssetAvailability.AVAILABLE),
                    listOf(representation(asset)),
                    Instant.parse("2026-09-13T11:00:00Z"),
                )
            }
        }

        assertNull(store.asset(asset.assetId))
        assertNull(store.localState(asset.assetId))
        assertTrue(store.representations(asset.assetId).isEmpty())
        assertEquals(IngestWorkState.QUEUED, store.ingestWorkItem(queued.workId)?.state)
    }

    @Test
    fun `Room stores stable enum wire values and epoch millisecond timestamps`() = runBlocking {
        val asset = TestAssets.fixture()
        val timestamp = Instant.parse("2026-09-13T10:00:00Z")
        store.saveAsset(asset)
        store.saveLocalState(AssetLocalState(asset.assetId, AssetAvailability.UNAVAILABLE, timestamp))
        store.saveRepresentation(representation(asset))
        store.createIngestWorkItem(workItem("work-wire", asset.assetId.value))

        database.openHelper.readableDatabase.query(
            "SELECT availability, last_reconciled_at FROM asset_local_state",
        ).use { cursor ->
            assertTrue(cursor.moveToFirst())
            assertEquals("unavailable", cursor.getString(0))
            assertEquals(timestamp.toEpochMilli(), cursor.getLong(1))
        }
        database.openHelper.readableDatabase.query(
            "SELECT role, availability FROM local_representations",
        ).use { cursor ->
            assertTrue(cursor.moveToFirst())
            assertEquals("canonical", cursor.getString(0))
            assertEquals("present", cursor.getString(1))
        }
        database.openHelper.readableDatabase.query("SELECT state FROM ingest_work_items").use { cursor ->
            assertTrue(cursor.moveToFirst())
            assertEquals("queued", cursor.getString(0))
        }
    }

    private fun workItem(workId: String, assetId: String): IngestWorkItem {
        val timestamp = Instant.parse("2026-09-13T09:00:00Z")
        return IngestWorkItem(
            workId = workId,
            reservedAssetId = AssetId.parse(assetId),
            sourceUri = "content://media/external/images/42",
            state = IngestWorkState.QUEUED,
            stagingRelativePath = "staging/$workId.bin",
            createdAt = timestamp,
            updatedAt = timestamp,
        )
    }

    private fun representation(asset: com.nimroel.assetmanager.domain.model.Asset) = LocalRepresentation(
        representationId = "representation-1",
        assetId = asset.assetId,
        role = RepresentationRole.CANONICAL,
        relativePath = "managed/assets/example.webp",
        mimeType = asset.content.mimeType,
        sha256 = asset.content.sha256,
        widthPx = asset.content.widthPx,
        heightPx = asset.content.heightPx,
        byteSize = asset.content.byteSize ?: 128,
        availability = RepresentationAvailability.PRESENT,
    )
}

package com.nimroel.assetmanager.data.local

import android.content.Context
import android.database.sqlite.SQLiteConstraintException
import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.model.Classification
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.Subject
import com.nimroel.assetmanager.domain.identity.AssetIdGenerator
import com.nimroel.assetmanager.domain.identity.WorkIdGenerator
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.LocalIngestCoordinator
import com.nimroel.assetmanager.domain.processing.LocalIngestResult
import com.nimroel.assetmanager.domain.processing.PreparedImage
import com.nimroel.assetmanager.domain.processing.StagedImage
import com.nimroel.assetmanager.domain.processing.StagingFileStore
import com.nimroel.assetmanager.domain.storage.AssetLocalState
import com.nimroel.assetmanager.domain.storage.AssetAvailability
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.IngestWorkTransition
import com.nimroel.assetmanager.domain.storage.LocalRepresentation
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant
import java.time.Clock
import java.time.ZoneOffset
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
        store.saveRepresentation(representation(original))
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
        assertEquals(listOf(representation(original)), store.representations(original.assetId))
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
        val processing = checkNotNull(
            store.transitionIngestWorkItem(
                IngestWorkTransition(
                    workId = work.workId,
                    expectedState = IngestWorkState.QUEUED,
                    targetState = IngestWorkState.PROCESSING,
                    updatedAt = work.updatedAt.plusSeconds(1),
                ),
            ),
        )
        assertEquals(processing, store.ingestWorkItem("work-1"))
        assertThrows(SQLiteConstraintException::class.java) {
            runBlocking { store.createIngestWorkItem(work.copy(workId = "work-2")) }
        }
        Unit
    }

    @Test
    fun `Room conditionally enforces queued processing ready transitions`() = runBlocking {
        val queued = workItem("work-transitions", TestAssets.fixture().assetId.value)
        store.createIngestWorkItem(queued)

        assertThrows(IllegalArgumentException::class.java) {
            runBlocking {
                store.transitionIngestWorkItem(
                    IngestWorkTransition(
                        queued.workId,
                        IngestWorkState.QUEUED,
                        IngestWorkState.READY_TO_COMMIT,
                        queued.updatedAt.plusSeconds(1),
                        "staging/${queued.workId}/source",
                    ),
                )
            }
        }
        assertEquals(IngestWorkState.QUEUED, store.ingestWorkItem(queued.workId)?.state)
    }

    @Test
    fun `ready transition persists a normalized managed staging path`() = runBlocking {
        val processing = processingWork("work-safe-path")

        val ready = store.transitionIngestWorkItem(
            IngestWorkTransition(
                workId = processing.workId,
                expectedState = IngestWorkState.PROCESSING,
                targetState = IngestWorkState.READY_TO_COMMIT,
                updatedAt = processing.updatedAt.plusSeconds(1),
                stagingRelativePath = "staging/work-1/source",
            ),
        )

        assertEquals(IngestWorkState.READY_TO_COMMIT, ready?.state)
        assertEquals("staging/work-1/source", ready?.stagingRelativePath)
        assertEquals(ready, store.ingestWorkItem(processing.workId))
    }

    @Test
    fun `ready transition rejects unsafe staging paths before Room write`() = runBlocking {
        val processing = processingWork("work-unsafe-path")
        listOf(
            "/data/user/0/source",
            "../source",
            "staging/../source",
            "staging\\work-1\\source",
            "staging:work-1/source",
        ).forEach { unsafePath ->

            assertThrows(IllegalArgumentException::class.java) {
                runBlocking {
                    store.transitionIngestWorkItem(
                        IngestWorkTransition(
                            workId = processing.workId,
                            expectedState = IngestWorkState.PROCESSING,
                            targetState = IngestWorkState.READY_TO_COMMIT,
                            updatedAt = processing.updatedAt.plusSeconds(1),
                            stagingRelativePath = unsafePath,
                        ),
                    )
                }
            }

            val persisted = checkNotNull(store.ingestWorkItem(processing.workId))
            assertEquals(IngestWorkState.PROCESSING, persisted.state)
            assertNull(persisted.stagingRelativePath)
        }
    }

    @Test
    fun `discard removes only a ready operational work item and creates no Asset state`() = runBlocking {
        val ready = processingWork("work-discard")
        val completed = checkNotNull(
            store.transitionIngestWorkItem(
                IngestWorkTransition(
                    ready.workId,
                    IngestWorkState.PROCESSING,
                    IngestWorkState.READY_TO_COMMIT,
                    ready.updatedAt.plusSeconds(1),
                    stagingRelativePath = "staging/${ready.workId}/source",
                ),
            ),
        )
        val queued = workItem("work-kept", "ast_01991d80-1000-7000-8000-000000000099")
        store.createIngestWorkItem(queued)

        assertEquals(completed, store.discardReadyIngestWorkItem(completed.workId))

        assertNull(store.ingestWorkItem(completed.workId))
        assertEquals(queued, store.ingestWorkItem(queued.workId))
        assertFalse(store.containsAsset(completed.reservedAssetId))
        assertNull(store.localState(completed.reservedAssetId))
        assertTrue(store.representations(completed.reservedAssetId).isEmpty())
        assertEquals(1, NimroelAssetDatabase.VERSION)
    }

    @Test
    fun `real Room integration persists coordinator result as ready without creating Asset state`() = runBlocking {
        val reservedId = TestAssets.fixture().assetId
        val content = Content("image/png", 32, 64, 256, "c".repeat(64))
        val prepared = PreparedImage(ImageSourceRef("content://images/room-integration"), content)
        val coordinator = LocalIngestCoordinator(
            assetIdGenerator = AssetIdGenerator { reservedId },
            workIdGenerator = WorkIdGenerator { "room-work" },
            stagingFileStore = StagingFileStore { workId, _, expected ->
                StagedImage("staging/$workId/source", expected)
            },
            workItemStore = store,
            clock = Clock.fixed(Instant.parse("2026-09-14T12:00:00Z"), ZoneOffset.UTC),
        )

        val result = coordinator.begin(prepared) as LocalIngestResult.Ready

        val persisted = checkNotNull(store.ingestWorkItem("room-work"))
        assertEquals(result.workItem, persisted)
        assertEquals(IngestWorkState.READY_TO_COMMIT, persisted.state)
        assertEquals("staging/room-work/source", persisted.stagingRelativePath)
        assertFalse(store.containsAsset(reservedId))
        assertNull(store.localState(reservedId))
        assertTrue(store.representations(reservedId).isEmpty())
        assertEquals(1, NimroelAssetDatabase.VERSION)
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
    fun `saving Asset with changed content rejects update and preserves existing document representation and projections`() = runBlocking {
        val original = TestAssets.fixture()
        val originalRepresentation = representation(original)
        store.saveAsset(original)
        store.saveRepresentation(originalRepresentation)
        val originalDocument = checkNotNull(database.assetDocuments().find(original.assetId.value))
        val changedContent = original.copy(content = original.content.copy(sha256 = "f".repeat(64)))

        assertThrows(IllegalArgumentException::class.java) {
            runBlocking { store.saveAsset(changedContent) }
        }

        assertEquals(original, store.asset(original.assetId))
        assertEquals(originalRepresentation, store.representations(original.assetId).single())
        assertEquals(originalDocument, database.assetDocuments().find(original.assetId.value))
    }

    @Test
    fun `bundle commit writes document local state representations and committed work atomically`() = runBlocking {
        val asset = TestAssets.fixture()
        val queued = workItem("work-commit", asset.assetId.value)
        val state = AssetLocalState(asset.assetId, AssetAvailability.AVAILABLE)
        val representation = representation(asset)
        store.createIngestWorkItem(queued)
        store.transitionIngestWorkItem(
            IngestWorkTransition(
                queued.workId,
                IngestWorkState.QUEUED,
                IngestWorkState.PROCESSING,
                queued.updatedAt.plusSeconds(1),
            ),
        )
        val ready = checkNotNull(
            store.transitionIngestWorkItem(
                IngestWorkTransition(
                    queued.workId,
                    IngestWorkState.PROCESSING,
                    IngestWorkState.READY_TO_COMMIT,
                    queued.updatedAt.plusSeconds(2),
                    stagingRelativePath = "staging/${queued.workId}/source",
                ),
            ),
        )

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
            stagingRelativePath = null,
            createdAt = timestamp,
            updatedAt = timestamp,
        )
    }

    private suspend fun processingWork(workId: String): IngestWorkItem {
        val queued = workItem(workId, TestAssets.fixture().assetId.value)
        store.createIngestWorkItem(queued)
        return checkNotNull(
            store.transitionIngestWorkItem(
                IngestWorkTransition(
                    workId = queued.workId,
                    expectedState = IngestWorkState.QUEUED,
                    targetState = IngestWorkState.PROCESSING,
                    updatedAt = queued.updatedAt.plusSeconds(1),
                ),
            ),
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

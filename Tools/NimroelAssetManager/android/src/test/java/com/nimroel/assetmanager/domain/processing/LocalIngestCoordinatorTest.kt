package com.nimroel.assetmanager.domain.processing

import com.nimroel.assetmanager.domain.identity.AssetIdGenerator
import com.nimroel.assetmanager.domain.identity.WorkIdGenerator
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkItemStore
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.IngestWorkTransition
import com.nimroel.assetmanager.domain.storage.IngestWorkTransitionPolicy
import java.time.Clock
import java.time.Instant
import java.time.ZoneOffset
import kotlinx.coroutines.CompletableDeferred
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.async
import kotlinx.coroutines.test.runCurrent
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class LocalIngestCoordinatorTest {
    private val fixedClock = Clock.fixed(Instant.parse("2026-09-14T10:00:00Z"), ZoneOffset.UTC)
    private val prepared = PreparedImage(
        ImageSourceRef("content://images/prepared"),
        Content("image/png", 10, 20, 128, "a".repeat(64)),
    )

    @Test
    fun `begin reserves AssetId creates queued then processing and finishes ready`() = runTest {
        val store = FakeWorkItemStore()
        val coordinator = coordinator(store = store)

        val result = coordinator.begin(prepared) as LocalIngestResult.Ready

        assertEquals(listOf(IngestWorkState.QUEUED, IngestWorkState.PROCESSING, IngestWorkState.READY_TO_COMMIT), store.publishedStates)
        assertEquals(assetId(1), result.workItem.reservedAssetId)
        assertEquals("work-1", result.workItem.workId)
        assertEquals("staging/work-1/source", result.workItem.stagingRelativePath)
        assertEquals(result.workItem, store.ingestWorkItem("work-1"))
        assertNull(result.workItem.errorCode)
    }

    @Test
    fun `known staging failure publishes failed with stable bounded diagnostics`() = runTest {
        val store = FakeWorkItemStore()
        val staging = StagingFileStore { _, _, _ ->
            throw StagingException(
                StagingErrorCode.SOURCE_CHANGED,
                "La fuente cambió.\ncontent://private/provider/value ${"x".repeat(300)}",
            )
        }

        val result = coordinator(store, staging).begin(prepared) as LocalIngestResult.Failed

        assertEquals(IngestWorkState.FAILED, result.workItem.state)
        assertEquals("source_changed", result.workItem.errorCode)
        assertTrue(result.workItem.errorDetail.orEmpty().length <= 240)
        assertFalse(result.workItem.errorDetail.orEmpty().contains('\n'))
        assertFalse(result.workItem.errorDetail.orEmpty().contains("content://"))
        assertNull(result.workItem.stagingRelativePath)
        assertEquals(prepared.sourceRef.value, result.workItem.sourceUri)
    }

    @Test
    fun `ready is not published before staging verification completes`() = runTest {
        val store = FakeWorkItemStore()
        val gate = CompletableDeferred<StagedImage>()
        val staging = StagingFileStore { _, _, _ -> gate.await() }
        val running = async { coordinator(store, staging).begin(prepared) }

        runCurrent()

        assertEquals(IngestWorkState.PROCESSING, store.ingestWorkItem("work-1")?.state)
        assertFalse(running.isCompleted)

        gate.complete(StagedImage("staging/work-1/source", prepared.content))
        runCurrent()

        assertTrue(running.await() is LocalIngestResult.Ready)
        assertEquals(IngestWorkState.READY_TO_COMMIT, store.ingestWorkItem("work-1")?.state)
    }

    @Test
    fun `retry creates a new work item and a new reserved AssetId while keeping failed evidence`() = runTest {
        val store = FakeWorkItemStore()
        var attempt = 0
        val staging = StagingFileStore { workId, _, expected ->
            attempt += 1
            if (attempt == 1) throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "Fuente no disponible.")
            StagedImage("staging/$workId/source", expected)
        }
        val coordinator = coordinator(
            store = store,
            staging = staging,
            assetIds = listOf(assetId(1), assetId(2)),
            workIds = listOf("work-1", "work-2"),
        )

        val first = coordinator.begin(prepared) as LocalIngestResult.Failed
        val second = coordinator.begin(prepared) as LocalIngestResult.Ready

        assertEquals(IngestWorkState.FAILED, store.ingestWorkItem(first.workItem.workId)?.state)
        assertEquals(IngestWorkState.READY_TO_COMMIT, store.ingestWorkItem(second.workItem.workId)?.state)
        assertNotEquals(first.workItem.reservedAssetId, second.workItem.reservedAssetId)
        assertNotEquals(first.workItem.workId, second.workItem.workId)
    }

    @Test
    fun `transition policy rejects arbitrary regressions from ready and failed`() {
        val ready = workItem(IngestWorkState.READY_TO_COMMIT).copy(stagingRelativePath = "staging/work-1/source")
        val failed = workItem(IngestWorkState.FAILED).copy(errorCode = "source_changed", errorDetail = "changed")

        assertFailsTransition(ready, IngestWorkState.READY_TO_COMMIT, IngestWorkState.PROCESSING)
        assertFailsTransition(failed, IngestWorkState.FAILED, IngestWorkState.PROCESSING)
    }

    @Test
    fun `discard removes only ready operational work and invokes scoped staging cleanup`() = runTest {
        val store = FakeWorkItemStore()
        val discardedWorkIds = mutableListOf<String>()
        val staging = object : StagingFileStore {
            override suspend fun stageVerified(workId: String, sourceRef: ImageSourceRef, expectedContent: Content) =
                StagedImage("staging/$workId/source", expectedContent)

            override suspend fun discard(workId: String) {
                discardedWorkIds += workId
            }
        }
        val coordinator = coordinator(
            store = store,
            staging = staging,
            assetIds = listOf(assetId(1), assetId(2)),
            workIds = listOf("work-1", "work-2"),
        )
        val first = coordinator.begin(prepared) as LocalIngestResult.Ready

        val discarded = coordinator.discardReady(first.workItem.workId)
        val second = coordinator.begin(prepared) as LocalIngestResult.Ready

        assertEquals(first.workItem, discarded)
        assertNull(store.ingestWorkItem("work-1"))
        assertEquals(listOf("work-1"), discardedWorkIds)
        assertNotEquals(first.workItem.reservedAssetId, second.workItem.reservedAssetId)
        assertEquals(IngestWorkState.READY_TO_COMMIT, store.ingestWorkItem("work-2")?.state)
    }

    private fun coordinator(
        store: FakeWorkItemStore,
        staging: StagingFileStore = StagingFileStore { workId, _, expected ->
            StagedImage("staging/$workId/source", expected)
        },
        assetIds: List<AssetId> = listOf(assetId(1)),
        workIds: List<String> = listOf("work-1"),
    ): LocalIngestCoordinator {
        val assetIterator = assetIds.iterator()
        val workIterator = workIds.iterator()
        return LocalIngestCoordinator(
            assetIdGenerator = AssetIdGenerator { assetIterator.next() },
            workIdGenerator = WorkIdGenerator { workIterator.next() },
            stagingFileStore = staging,
            workItemStore = store,
            clock = fixedClock,
        )
    }

    private fun assetId(suffix: Int): AssetId =
        AssetId.parse("ast_01991d80-1000-7000-8000-${suffix.toString().padStart(12, '0')}")

    private fun workItem(state: IngestWorkState) = IngestWorkItem(
        workId = "work-1",
        reservedAssetId = assetId(1),
        sourceUri = prepared.sourceRef.value,
        state = state,
        createdAt = Instant.parse("2026-09-14T10:00:00Z"),
        updatedAt = Instant.parse("2026-09-14T10:00:00Z"),
    )

    private fun assertFailsTransition(current: IngestWorkItem, from: IngestWorkState, to: IngestWorkState) {
        var failed = false
        try {
            IngestWorkTransitionPolicy.apply(
                current,
                IngestWorkTransition(current.workId, from, to, current.updatedAt),
            )
        } catch (_: IllegalArgumentException) {
            failed = true
        }
        assertTrue(failed)
    }

    private class FakeWorkItemStore : IngestWorkItemStore {
        private val items = linkedMapOf<String, IngestWorkItem>()
        val publishedStates = mutableListOf<IngestWorkState>()

        override suspend fun createIngestWorkItem(workItem: IngestWorkItem) {
            check(workItem.workId !in items)
            check(workItem.state == IngestWorkState.QUEUED)
            items[workItem.workId] = workItem
            publishedStates += workItem.state
        }

        override suspend fun transitionIngestWorkItem(transition: IngestWorkTransition): IngestWorkItem? {
            val current = items[transition.workId] ?: return null
            val updated = IngestWorkTransitionPolicy.apply(current, transition)
            items[transition.workId] = updated
            publishedStates += updated.state
            return updated
        }

        override suspend fun discardReadyIngestWorkItem(workId: String): IngestWorkItem? {
            val current = items[workId] ?: return null
            if (current.state != IngestWorkState.READY_TO_COMMIT) return null
            items.remove(workId)
            return current
        }

        override suspend fun ingestWorkItem(workId: String): IngestWorkItem? = items[workId]

        override suspend fun ingestWorkItemByReservedAssetId(assetId: AssetId): IngestWorkItem? =
            items.values.firstOrNull { it.reservedAssetId == assetId }
    }
}

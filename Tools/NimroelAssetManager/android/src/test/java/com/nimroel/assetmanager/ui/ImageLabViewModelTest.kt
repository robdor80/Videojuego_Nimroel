package com.nimroel.assetmanager.ui

import com.nimroel.assetmanager.data.contracts.ProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftEnvironment
import com.nimroel.assetmanager.data.image.ImageLabPreviewLoadResult
import com.nimroel.assetmanager.data.image.ImageLabPreviewLoader
import com.nimroel.assetmanager.domain.contracts.PresetRegistry
import com.nimroel.assetmanager.domain.contracts.PresetSelections
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.ProductionPreset
import com.nimroel.assetmanager.domain.contracts.Vocabulary
import com.nimroel.assetmanager.domain.contracts.VocabularyReference
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularyValue
import com.nimroel.assetmanager.domain.identity.AssetIdGenerator
import com.nimroel.assetmanager.domain.identity.WorkIdGenerator
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.OriginKind
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.ImageLabArtifactRef
import com.nimroel.assetmanager.domain.processing.ImageLabException
import com.nimroel.assetmanager.domain.processing.ImageLabMetrics
import com.nimroel.assetmanager.domain.processing.ImageLabProcessor
import com.nimroel.assetmanager.domain.processing.ImageLabRequest
import com.nimroel.assetmanager.domain.processing.ImageLabResult
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.LocalIngestCoordinator
import com.nimroel.assetmanager.domain.processing.PreparedImage
import com.nimroel.assetmanager.domain.processing.StagedImage
import com.nimroel.assetmanager.domain.processing.StagedImageLabSource
import com.nimroel.assetmanager.domain.processing.StagingFileStore
import com.nimroel.assetmanager.domain.production.ProductionDraftService
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkItemStore
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.IngestWorkTransition
import com.nimroel.assetmanager.domain.storage.IngestWorkTransitionPolicy
import java.time.Clock
import java.time.Instant
import java.time.ZoneOffset
import kotlinx.coroutines.CompletableDeferred
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.NonCancellable
import kotlinx.coroutines.withContext
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runCurrent
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class ImageLabViewModelTest {
    @Test
    fun `ready staging enables experimental lab and generated result belongs to current work`() = runTest {
        val processor = FakeImageLabProcessor()
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            assertTrue(viewModel.ready().imageLabState is ImageLabUiState.Idle)

            viewModel.selectImageLabTarget(1280)
            viewModel.selectImageLabQuality(90)
            viewModel.generateImageLabCandidate()
            runCurrent()

            val result = (viewModel.ready().imageLabState as ImageLabUiState.Results).session.results.single()
            assertEquals("work-1", result.workId)
            assertEquals(1280, result.requestedTargetLongEdge)
            assertEquals(90, result.quality)
            assertEquals("image/webp", result.mimeType)
            assertEquals(90.0, result.reductionPercent!!, 0.001)
        }
    }

    @Test
    fun `double generation launch is protected`() = runTest {
        val gate = CompletableDeferred<Unit>()
        val processor = FakeImageLabProcessor(gate = gate)
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)

            viewModel.generateImageLabCandidate()
            viewModel.generateImageLabCandidate()
            runCurrent()

            assertEquals(1, processor.generateCalls)
            assertTrue(viewModel.ready().imageLabState is ImageLabUiState.Processing)
            gate.complete(Unit)
            runCurrent()
        }
    }

    @Test
    fun `processing error preserves staging provenance and disabled Asset creation`() = runTest {
        val processor = FakeImageLabProcessor(failure = ImageLabException("codec failure"))
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.selectProvenanceKind(OriginKind.IMPORTED)
            val stagingBefore = viewModel.ready().localIngestState
            val provenanceBefore = viewModel.ready().provenanceState

            viewModel.generateImageLabCandidate()
            runCurrent()

            val state = viewModel.ready()
            assertTrue(state.imageLabState is ImageLabUiState.Error)
            assertEquals(stagingBefore, state.localIngestState)
            assertEquals(provenanceBefore, state.provenanceState)
            assertFalse(state.isAssetCreationEnabled)
        }
    }

    @Test
    fun `clean action removes temporary results without exposing file paths`() = runTest {
        val processor = FakeImageLabProcessor()
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.generateImageLabCandidate()
            runCurrent()
            val visible = viewModel.ready().imageLabState.toString()
            assertFalse(visible.contains("/data/"))
            assertFalse(visible.contains("nimroel-image-lab"))

            viewModel.clearImageLabResults()
            runCurrent()

            val state = viewModel.ready().imageLabState as ImageLabUiState.Idle
            assertTrue(state.session.results.isEmpty())
            assertEquals(listOf("work-1"), processor.clearedWorkIds)
        }
    }

    @Test
    fun `result for another work is rejected`() = runTest {
        val processor = FakeImageLabProcessor(resultWorkId = "work-other")
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)

            viewModel.generateImageLabCandidate()
            runCurrent()

            val state = viewModel.ready().imageLabState as ImageLabUiState.Error
            assertTrue(state.session.results.isEmpty())
            assertTrue(state.message.contains("staged work actual"))
        }
    }

    @Test
    fun `changing current staged work clears and cannot mix previous results`() = runTest {
        val processor = FakeImageLabProcessor()
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.generateImageLabCandidate()
            runCurrent()
            assertEquals(1, (viewModel.ready().imageLabState as ImageLabUiState.Results).session.results.size)

            val nextContent = content.copy(sha256 = "b".repeat(64))
            viewModel.activateImageLab(
                StagedImageLabSource.from("work-2", StagedImage("staging/work-2/source", nextContent)),
            )
            runCurrent()

            val state = viewModel.ready().imageLabState as ImageLabUiState.Idle
            assertTrue(state.session.results.isEmpty())
            assertEquals(nextContent, state.session.sourceContent)
            assertTrue("work-1" in processor.clearedWorkIds)
        }
    }

    @Test
    fun `late non cancellable result from work A never appears in work B`() = runTest {
        val gate = CompletableDeferred<Unit>()
        val processor = FakeImageLabProcessor(gate = gate, ignoreCancellationAtGate = true)
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.generateImageLabCandidate()
            runCurrent()

            val nextContent = content.copy(sha256 = "b".repeat(64))
            viewModel.activateImageLab(
                StagedImageLabSource.from("work-2", StagedImage("staging/work-2/source", nextContent)),
            )
            gate.complete(Unit)
            runCurrent()

            val state = viewModel.ready().imageLabState as ImageLabUiState.Idle
            assertTrue(state.session.results.isEmpty())
            assertEquals(nextContent, state.session.sourceContent)
        }
    }

    @Test
    fun `late generation cannot republish after clear`() = runTest {
        val gate = CompletableDeferred<Unit>()
        val processor = FakeImageLabProcessor(gate = gate, ignoreCancellationAtGate = true)
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.generateImageLabCandidate()
            runCurrent()

            viewModel.clearImageLabResults()
            runCurrent()
            gate.complete(Unit)
            runCurrent()

            val state = viewModel.ready().imageLabState as ImageLabUiState.Idle
            assertTrue(state.session.results.isEmpty())
        }
    }

    @Test
    fun `discard during a non cancellable generation clears lab provenance and prevents late publication`() = runTest {
        val gate = CompletableDeferred<Unit>()
        val processor = FakeImageLabProcessor(gate = gate, ignoreCancellationAtGate = true)
        withLabViewModel(processor) { viewModel ->
            readyStaging(viewModel)
            viewModel.selectProvenanceKind(OriginKind.IMPORTED)
            viewModel.generateImageLabCandidate()
            runCurrent()

            viewModel.discardLocalIngest()
            runCurrent()
            gate.complete(Unit)
            runCurrent()

            val state = viewModel.ready()
            assertEquals(ImageUiState.NoImage, state.imageState)
            assertEquals(LocalIngestUiState.NotStarted, state.localIngestState)
            assertEquals(ProvenanceUiState.Unavailable, state.provenanceState)
            assertEquals(ImageLabUiState.Unavailable, state.imageLabState)
            assertEquals(listOf("work-1"), processor.clearedWorkIds)
            assertFalse(state.isAssetCreationEnabled)
        }
    }

    private suspend fun kotlinx.coroutines.test.TestScope.readyStaging(viewModel: AssetManagerViewModel) {
        viewModel.selectImage(ImageSourceRef("content://images/source"))
        runCurrent()
        viewModel.prepareLocalIngest()
        runCurrent()
    }

    private suspend fun kotlinx.coroutines.test.TestScope.withLabViewModel(
        processor: FakeImageLabProcessor,
        block: suspend kotlinx.coroutines.test.TestScope.(AssetManagerViewModel) -> Unit,
    ) {
        val dispatcher = StandardTestDispatcher(testScheduler)
        Dispatchers.setMain(dispatcher)
        try {
            val store = FakeWorkItemStore()
            val coordinator = LocalIngestCoordinator(
                assetIdGenerator = AssetIdGenerator { AssetId.parse("ast_01991d80-1000-7000-8000-000000000001") },
                workIdGenerator = WorkIdGenerator { "work-1" },
                stagingFileStore = StagingFileStore { workId, _, expected ->
                    StagedImage("staging/$workId/source", expected)
                },
                workItemStore = store,
                clock = fixedClock,
            )
            block(
                AssetManagerViewModel(
                    bootstrap = bootstrap(),
                    imageContentPreparer = ImageContentPreparer { PreparedImage(it, content) },
                    imageDispatcher = dispatcher,
                    localIngestCoordinator = coordinator,
                    imageLabProcessor = processor,
                    imageLabPreviewLoader = ImageLabPreviewLoader { _, _ ->
                        ImageLabPreviewLoadResult.Unavailable
                    },
                    clock = fixedClock,
                ),
            )
        } finally {
            Dispatchers.resetMain()
        }
    }

    private class FakeImageLabProcessor(
        private val resultWorkId: String? = null,
        private val gate: CompletableDeferred<Unit>? = null,
        private val ignoreCancellationAtGate: Boolean = false,
        private val failure: Exception? = null,
    ) : ImageLabProcessor {
        var generateCalls = 0
        val clearedWorkIds = mutableListOf<String>()

        override suspend fun generate(request: ImageLabRequest): ImageLabResult {
            generateCalls += 1
            gate?.let {
                if (ignoreCancellationAtGate) withContext(NonCancellable) { it.await() } else it.await()
            }
            failure?.let { throw it }
            val resultBytes = 100L
            return ImageLabResult(
                workId = resultWorkId ?: request.source.workId,
                mimeType = ImageLabResult.MIME_WEBP,
                widthPx = 50,
                heightPx = 100,
                byteSize = resultBytes,
                requestedTargetLongEdge = request.profile.targetLongEdge,
                quality = request.profile.quality,
                reduction = ImageLabMetrics.reduction(request.source.content.byteSize, resultBytes),
                sourceHasAlphaCapability = true,
                transparentPixelsObserved = false,
                orientationApplied = false,
                artifactRef = ImageLabArtifactRef("token-$generateCalls"),
            )
        }

        override suspend fun clear(workId: String) {
            clearedWorkIds += workId
        }
    }

    private class FakeWorkItemStore : IngestWorkItemStore {
        private val values = linkedMapOf<String, IngestWorkItem>()

        override suspend fun createIngestWorkItem(workItem: IngestWorkItem) {
            values[workItem.workId] = workItem
        }

        override suspend fun transitionIngestWorkItem(transition: IngestWorkTransition): IngestWorkItem? {
            val current = values[transition.workId] ?: return null
            return IngestWorkTransitionPolicy.apply(current, transition).also { values[it.workId] = it }
        }

        override suspend fun discardReadyIngestWorkItem(workId: String): IngestWorkItem? {
            val current = values[workId] ?: return null
            if (current.state != IngestWorkState.READY_TO_COMMIT) return null
            values.remove(workId)
            return current
        }

        override suspend fun ingestWorkItem(workId: String): IngestWorkItem? = values[workId]
        override suspend fun ingestWorkItemByReservedAssetId(assetId: AssetId): IngestWorkItem? =
            values.values.firstOrNull { it.reservedAssetId == assetId }
    }

    private fun bootstrap(): ProductionDraftBootstrap {
        val preset = ProductionPreset(
            presetId = "lab-test-preset",
            version = "1.0",
            label = "Lab test",
            assetType = AssetType.NPC_PORTRAIT,
            vocabularySetId = "lab-test-set",
            vocabularySetVersion = "1.0",
            selections = PresetSelections(),
        )
        val service = ProductionDraftService(
            PresetRegistry.create(listOf(preset)),
            VocabularySetRegistry.create(
                listOf(
                    VocabularySet(
                        "lab-test-set",
                        "1.0",
                        mapOf(ProductionFieldPaths.SUBJECT_AGE_BAND_ID to VocabularyReference("ages", "1.0")),
                    ),
                ),
            ),
            VocabularyRegistry.create(listOf(Vocabulary("ages", "1.0", listOf(VocabularyValue("adult", "Adult"))))),
        )
        return ProductionDraftBootstrap {
            ProductionDraftEnvironment(service, service.startDraft(preset.presetId, preset.version), preset.label)
        }
    }

    private fun AssetManagerViewModel.ready() = uiState as AssetManagerUiState.Ready

    companion object {
        private val fixedClock = Clock.fixed(Instant.parse("2026-09-14T10:00:00Z"), ZoneOffset.UTC)
        private val content = Content("image/png", 100, 200, 1000, "a".repeat(64))
    }
}

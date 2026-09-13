package com.nimroel.assetmanager.ui

import com.nimroel.assetmanager.data.contracts.ProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftEnvironment
import com.nimroel.assetmanager.domain.contracts.PresetRegistry
import com.nimroel.assetmanager.domain.contracts.PresetSelections
import com.nimroel.assetmanager.domain.contracts.PresetValue
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.ProductionPreset
import com.nimroel.assetmanager.domain.contracts.SubjectSelections
import com.nimroel.assetmanager.domain.contracts.Vocabulary
import com.nimroel.assetmanager.domain.contracts.VocabularyReference
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularyValue
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.identity.AssetIdGenerator
import com.nimroel.assetmanager.domain.identity.WorkIdGenerator
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.LocalIngestCoordinator
import com.nimroel.assetmanager.domain.processing.PreparedImage
import com.nimroel.assetmanager.domain.processing.StagedImage
import com.nimroel.assetmanager.domain.processing.StagingErrorCode
import com.nimroel.assetmanager.domain.processing.StagingException
import com.nimroel.assetmanager.domain.processing.StagingFileStore
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
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
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runCurrent
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import kotlinx.coroutines.withContext
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class ImageSelectionViewModelTest {
    @Test
    fun `cancelled selection does not alter NoImage state`() = runTest {
        withViewModel(ImageContentPreparer { prepared(it, "a") }) { viewModel ->
            val before = viewModel.ready()

            viewModel.selectImage(null)

            assertSame(before, viewModel.uiState)
            assertEquals(ImageUiState.NoImage, viewModel.ready().imageState)
        }
    }

    @Test
    fun `image moves through Processing and Prepared with canonical Content`() = runTest {
        val source = ImageSourceRef("content://images/one")
        val expected = prepared(source, "1", width = 2048, height = 1024, size = 8_192)
        val deferred = CompletableDeferred<PreparedImage>()
        withViewModel(ImageContentPreparer { deferred.await() }) { viewModel ->
            viewModel.selectImage(source)

            assertTrue(viewModel.ready().imageState is ImageUiState.Processing)
            runCurrent()
            deferred.complete(expected)
            runCurrent()

            val state = viewModel.ready().imageState as ImageUiState.Prepared
            assertEquals(expected.content, state.image.content)
            assertEquals("image/png", state.image.content.mimeType)
            assertEquals(2048, state.image.content.widthPx)
            assertEquals(1024, state.image.content.heightPx)
            assertEquals(8_192L, state.image.content.byteSize)
        }
    }

    @Test
    fun `removing a prepared image returns to NoImage`() = runTest {
        withViewModel(ImageContentPreparer { prepared(it, "2") }) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/one"))
            runCurrent()
            assertTrue(viewModel.ready().imageState is ImageUiState.Prepared)

            viewModel.removeImage()

            assertEquals(ImageUiState.NoImage, viewModel.ready().imageState)
        }
    }

    @Test
    fun `changing image replaces Content after successful analysis`() = runTest {
        val preparer = ImageContentPreparer { source ->
            if (source.value.endsWith("one")) prepared(source, "3", width = 10) else prepared(source, "4", width = 20)
        }
        withViewModel(preparer) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/one"))
            runCurrent()
            viewModel.selectImage(ImageSourceRef("content://images/two"))
            runCurrent()

            val state = viewModel.ready().imageState as ImageUiState.Prepared
            assertEquals(20, state.image.content.widthPx)
            assertEquals("4".repeat(64), state.image.content.sha256)
        }
    }

    @Test
    fun `failed replacement preserves last prepared image and reports error`() = runTest {
        val originalSource = ImageSourceRef("content://images/original")
        val original = prepared(originalSource, "5")
        val preparer = ImageContentPreparer { source ->
            if (source == originalSource) original else throw ImagePreparationException("La nueva imagen no es válida.")
        }
        withViewModel(preparer) { viewModel ->
            viewModel.selectImage(originalSource)
            runCurrent()
            viewModel.selectImage(ImageSourceRef("content://images/broken"))
            runCurrent()

            val state = viewModel.ready().imageState as ImageUiState.ImageError
            assertEquals(original.content, state.previousPrepared?.content)
            assertTrue(state.message.contains("no es válida"))
        }
    }

    @Test
    fun `draft selections survive image success change and error`() = runTest {
        var shouldFail = false
        val preparer = ImageContentPreparer { source ->
            if (shouldFail) throw ImagePreparationException("fallo esperado") else prepared(source, "6")
        }
        withViewModel(preparer) { viewModel ->
            viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")
            viewModel.selectImage(ImageSourceRef("content://images/valid"))
            runCurrent()
            shouldFail = true
            viewModel.selectImage(ImageSourceRef("content://images/invalid"))
            runCurrent()

            val field = viewModel.ready().fields.single { it.fieldPath == ProductionFieldPaths.SUBJECT_AGE_BAND_ID }
            assertEquals("elder", field.selectedValueId)
            assertEquals(DraftSelectionSource.OPERATOR, field.source)
            assertNotNull((viewModel.ready().imageState as ImageUiState.ImageError).previousPrepared)
        }
    }

    @Test
    fun `cancelled picker preserves an existing Prepared image`() = runTest {
        withViewModel(ImageContentPreparer { prepared(it, "7") }) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/valid"))
            runCurrent()
            val before = viewModel.ready().imageState

            viewModel.selectImage(null)

            assertEquals(before, viewModel.ready().imageState)
        }
    }

    @Test
    fun `latest selection wins when first result arrives late`() = runTest {
        val preparer = ControlledPreparer()
        val sourceA = ImageSourceRef("content://images/a")
        val sourceB = ImageSourceRef("content://images/b")
        preparer.expect(sourceA)
        preparer.expect(sourceB)
        withViewModel(preparer) { viewModel ->
            viewModel.selectImage(sourceA)
            runCurrent()
            viewModel.selectImage(sourceB)
            runCurrent()

            preparer.complete(sourceB, prepared(sourceB, "b"))
            runCurrent()
            assertEquals("b".repeat(64), viewModel.preparedContent().sha256)

            preparer.complete(sourceA, prepared(sourceA, "a"))
            runCurrent()
            assertEquals("b".repeat(64), viewModel.preparedContent().sha256)
        }
    }

    @Test
    fun `local ingest moves through processing and ready without exposing its path`() = runTest {
        val gate = CompletableDeferred<StagedImage>()
        val store = FakeWorkItemStore()
        val coordinator = coordinator(store, StagingFileStore { _, _, _ -> gate.await() })
        withStagingViewModel(coordinator) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/staging"))
            runCurrent()

            viewModel.prepareLocalIngest()
            assertEquals(LocalIngestUiState.Processing, viewModel.ready().localIngestState)
            runCurrent()
            assertEquals(IngestWorkState.PROCESSING, store.items.single().state)

            gate.complete(StagedImage("staging/work-1/source", viewModel.preparedContent()))
            runCurrent()

            val ready = viewModel.ready().localIngestState as LocalIngestUiState.Ready
            assertEquals(assetId(1).value, ready.reservedAssetId)
            assertEquals("ready_to_commit", ready.status)
            assertFalse(ready.toString().contains("staging/"))
            assertFalse(ready.toString().contains("/data/"))
        }
    }

    @Test
    fun `double staging tap creates only one concurrent work item`() = runTest {
        val gate = CompletableDeferred<StagedImage>()
        val store = FakeWorkItemStore()
        val coordinator = coordinator(store, StagingFileStore { _, _, expected -> gate.await(); StagedImage("unused", expected) })
        withStagingViewModel(coordinator) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/staging"))
            runCurrent()

            viewModel.prepareLocalIngest()
            viewModel.prepareLocalIngest()
            runCurrent()

            assertEquals(1, store.items.size)
            gate.complete(StagedImage("staging/work-1/source", viewModel.preparedContent()))
            runCurrent()
        }
    }

    @Test
    fun `staging failure preserves draft and PreparedImage and allows retry with new identities`() = runTest {
        val store = FakeWorkItemStore()
        var attempt = 0
        val coordinator = coordinator(
            store,
            StagingFileStore { workId, _, expected ->
                attempt += 1
                if (attempt == 1) throw StagingException(StagingErrorCode.SOURCE_UNAVAILABLE, "Fuente no disponible.")
                StagedImage("staging/$workId/source", expected)
            },
            assetIds = listOf(assetId(1), assetId(2)),
            workIds = listOf("work-1", "work-2"),
        )
        withStagingViewModel(coordinator) { viewModel ->
            viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")
            viewModel.selectImage(ImageSourceRef("content://images/staging"))
            runCurrent()
            val preparedBefore = viewModel.preparedContent()

            viewModel.prepareLocalIngest()
            runCurrent()

            val failure = viewModel.ready().localIngestState as LocalIngestUiState.Failed
            assertEquals("source_unavailable", failure.errorCode)
            assertEquals("elder", viewModel.ready().fields.single().selectedValueId)
            assertEquals(preparedBefore, viewModel.preparedContent())

            viewModel.prepareLocalIngest()
            runCurrent()

            assertTrue(viewModel.ready().localIngestState is LocalIngestUiState.Ready)
            assertEquals(listOf(IngestWorkState.FAILED, IngestWorkState.READY_TO_COMMIT), store.items.map { it.state })
            assertNotNull(store.items.first().errorCode)
            assertTrue(store.items[0].reservedAssetId != store.items[1].reservedAssetId)
        }
    }

    @Test
    fun `ready staging locks image replacement and removal`() = runTest {
        val store = FakeWorkItemStore()
        withStagingViewModel(coordinator(store)) { viewModel ->
            viewModel.selectImage(ImageSourceRef("content://images/staging"))
            runCurrent()
            viewModel.prepareLocalIngest()
            runCurrent()
            val before = viewModel.ready()

            viewModel.removeImage()
            viewModel.selectImage(ImageSourceRef("content://images/replacement"))
            runCurrent()

            assertEquals(before.imageState, viewModel.ready().imageState)
            assertEquals(before.localIngestState, viewModel.ready().localIngestState)
        }
    }

    private suspend fun kotlinx.coroutines.test.TestScope.withViewModel(
        preparer: ImageContentPreparer,
        block: suspend kotlinx.coroutines.test.TestScope.(AssetManagerViewModel) -> Unit,
    ) {
        val dispatcher = StandardTestDispatcher(testScheduler)
        Dispatchers.setMain(dispatcher)
        try {
            block(AssetManagerViewModel(bootstrap(), preparer, dispatcher))
        } finally {
            Dispatchers.resetMain()
        }
    }

    private suspend fun kotlinx.coroutines.test.TestScope.withStagingViewModel(
        coordinator: LocalIngestCoordinator,
        block: suspend kotlinx.coroutines.test.TestScope.(AssetManagerViewModel) -> Unit,
    ) {
        val dispatcher = StandardTestDispatcher(testScheduler)
        Dispatchers.setMain(dispatcher)
        try {
            block(
                AssetManagerViewModel(
                    bootstrap = bootstrap(),
                    imageContentPreparer = ImageContentPreparer { prepared(it, "d") },
                    imageDispatcher = dispatcher,
                    localIngestCoordinator = coordinator,
                ),
            )
        } finally {
            Dispatchers.resetMain()
        }
    }

    private fun coordinator(
        store: FakeWorkItemStore,
        staging: StagingFileStore = StagingFileStore { workId, _, expected ->
            StagedImage("staging/$workId/source", expected)
        },
        assetIds: List<AssetId> = listOf(assetId(1)),
        workIds: List<String> = listOf("work-1"),
    ): LocalIngestCoordinator {
        val ids = assetIds.iterator()
        val works = workIds.iterator()
        return LocalIngestCoordinator(
            AssetIdGenerator { ids.next() },
            WorkIdGenerator { works.next() },
            staging,
            store,
            Clock.fixed(Instant.parse("2026-09-14T10:00:00Z"), ZoneOffset.UTC),
        )
    }

    private fun assetId(suffix: Int): AssetId =
        AssetId.parse("ast_01991d80-1000-7000-8000-${suffix.toString().padStart(12, '0')}")

    private class FakeWorkItemStore : IngestWorkItemStore {
        private val values = linkedMapOf<String, IngestWorkItem>()
        val items: List<IngestWorkItem> get() = values.values.toList()

        override suspend fun createIngestWorkItem(workItem: IngestWorkItem) {
            check(values.put(workItem.workId, workItem) == null)
        }

        override suspend fun transitionIngestWorkItem(transition: IngestWorkTransition): IngestWorkItem? {
            val current = values[transition.workId] ?: return null
            return IngestWorkTransitionPolicy.apply(current, transition).also { values[it.workId] = it }
        }

        override suspend fun ingestWorkItem(workId: String): IngestWorkItem? = values[workId]
        override suspend fun ingestWorkItemByReservedAssetId(assetId: AssetId): IngestWorkItem? =
            values.values.firstOrNull { it.reservedAssetId == assetId }
    }

    private class ControlledPreparer : ImageContentPreparer {
        private val results = mutableMapOf<ImageSourceRef, CompletableDeferred<PreparedImage>>()

        fun expect(sourceRef: ImageSourceRef) {
            results[sourceRef] = CompletableDeferred()
        }

        fun complete(sourceRef: ImageSourceRef, image: PreparedImage) {
            checkNotNull(results[sourceRef]).complete(image)
        }

        override suspend fun prepare(sourceRef: ImageSourceRef): PreparedImage =
            withContext(NonCancellable) { checkNotNull(results[sourceRef]).await() }
    }

    private fun prepared(
        sourceRef: ImageSourceRef,
        hashCharacter: String,
        width: Int = 100,
        height: Int = 200,
        size: Long = 512,
    ) = PreparedImage(
        sourceRef,
        Content("image/png", width, height, size, hashCharacter.repeat(64)),
    )

    private fun bootstrap(): ProductionDraftBootstrap {
        val preset = ProductionPreset(
            "image-test-preset",
            "1.0",
            "Image test preset",
            assetType = AssetType.NPC_PORTRAIT,
            vocabularySetId = "image-test-set",
            vocabularySetVersion = "1.0",
            selections = PresetSelections(
                subject = SubjectSelections(ageBandId = PresetValue(PresetValueMode.SUGGESTED, "adult")),
            ),
        )
        val set = VocabularySet(
            "image-test-set",
            "1.0",
            mapOf(ProductionFieldPaths.SUBJECT_AGE_BAND_ID to VocabularyReference("test-ages", "1.0")),
        )
        val service = ProductionDraftService(
            PresetRegistry.create(listOf(preset)),
            VocabularySetRegistry.create(listOf(set)),
            VocabularyRegistry.create(
                listOf(Vocabulary("test-ages", "1.0", listOf(VocabularyValue("adult", "Adult"), VocabularyValue("elder", "Elder")))),
            ),
        )
        return ProductionDraftBootstrap {
            ProductionDraftEnvironment(service, service.startDraft(preset.presetId, preset.version), preset.label)
        }
    }

    private fun AssetManagerViewModel.ready() = uiState as AssetManagerUiState.Ready

    private fun AssetManagerViewModel.preparedContent(): Content =
        (ready().imageState as ImageUiState.Prepared).image.content
}

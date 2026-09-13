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
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.PreparedImage
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.domain.production.ProductionDraftService
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

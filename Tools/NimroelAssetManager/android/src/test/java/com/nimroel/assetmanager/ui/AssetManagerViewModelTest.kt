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
import com.nimroel.assetmanager.domain.contracts.VisualSelections
import com.nimroel.assetmanager.domain.contracts.Vocabulary
import com.nimroel.assetmanager.domain.contracts.VocabularyReference
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularyValue
import com.nimroel.assetmanager.domain.contracts.VocabularyValueStatus
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.domain.production.ProductionDraftService
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class AssetManagerViewModelTest {
    @Test
    fun `produces ready state with exact draft metadata and no unbound empty fields`() {
        val state = AssetManagerViewModel(bootstrap()).ready()

        assertEquals("Nueva producción", state.screenTitle)
        assertEquals("Retrato de PNJ", state.screenSubtitle)
        assertEquals("Test editorial preset", state.presetLabel)
        assertEquals("test-preset", state.presetId)
        assertEquals("2.4", state.presetVersion)
        assertEquals(AssetType.NPC_PORTRAIT, state.assetType)
        assertEquals("test-set", state.vocabularySetId)
        assertEquals("7.1", state.vocabularySetVersion)
        assertEquals(
            listOf(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, ProductionFieldPaths.VISUAL_EXPRESSION_ID),
            state.fields.map { it.fieldPath },
        )
        assertFalse(state.fields.any { it.fieldPath == ProductionFieldPaths.SUBJECT_SPECIES_ID })
    }

    @Test
    fun `field options expose editorial labels and preserve deprecated values`() {
        val age = AssetManagerViewModel(bootstrap()).ready().field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID)

        assertEquals(listOf("Adult", "Elder"), age.values.map { it.label })
        assertFalse(age.values.first().label == age.values.first().valueId)
        assertTrue(age.values.last().isDeprecated)
        assertEquals("Former age band", age.values.last().description)
    }

    @Test
    fun `suggested value can change and becomes operator selection while summary updates`() {
        val viewModel = AssetManagerViewModel(bootstrap())

        viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")

        val state = viewModel.ready()
        val age = state.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID)
        assertEquals("elder", age.selectedValueId)
        assertEquals("Elder", age.selectedValueLabel)
        assertEquals(DraftSelectionSource.OPERATOR, age.source)
        assertEquals(PresetValueMode.SUGGESTED, age.presetMode)
        assertTrue(age.selectedValueDeprecated)
        assertEquals("Elder", state.summary.selections.single { it.fieldLabel == "Rango de edad" }.valueLabel)
    }

    @Test
    fun `suggested value can be cleared and selected again`() {
        val viewModel = AssetManagerViewModel(bootstrap())

        viewModel.clearSelection(ProductionFieldPaths.SUBJECT_AGE_BAND_ID)

        val cleared = viewModel.ready()
        assertNull(cleared.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID).selectedValueId)
        assertEquals(1, cleared.summary.activeSelectionCount)

        viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "adult")

        val selectedAgain = viewModel.ready().field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID)
        assertEquals("Adult", selectedAgain.selectedValueLabel)
        assertEquals(DraftSelectionSource.OPERATOR, selectedAgain.source)
        assertEquals(PresetValueMode.SUGGESTED, selectedAgain.presetMode)
    }

    @Test
    fun `fixed field is locked and rejected actions preserve the valid draft`() {
        val viewModel = AssetManagerViewModel(bootstrap(ageMode = PresetValueMode.FIXED))
        val initial = viewModel.ready()
        assertTrue(initial.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID).isLocked)
        assertFalse(initial.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID).isEditable)

        viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")

        val afterChange = viewModel.ready()
        assertEquals("Adult", afterChange.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID).selectedValueLabel)
        assertNotNull(afterChange.actionError)

        viewModel.clearSelection(ProductionFieldPaths.SUBJECT_AGE_BAND_ID)

        val afterClear = viewModel.ready()
        assertEquals("Adult", afterClear.field(ProductionFieldPaths.SUBJECT_AGE_BAND_ID).selectedValueLabel)
        assertNotNull(afterClear.actionError)
    }

    @Test
    fun `domain errors do not destroy the last valid draft`() {
        val viewModel = AssetManagerViewModel(bootstrap())
        val before = viewModel.ready()

        viewModel.selectValue(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "unknown")

        val after = viewModel.ready()
        assertEquals(before.fields, after.fields)
        assertEquals(before.summary, after.summary)
        assertTrue(after.actionError.orEmpty().contains("Unknown value"))
    }

    @Test
    fun `bootstrap failure produces a clear error state`() {
        val viewModel = AssetManagerViewModel(ProductionDraftBootstrap { error("missing contracts") })

        assertTrue(viewModel.uiState is AssetManagerUiState.Error)
        assertTrue((viewModel.uiState as AssetManagerUiState.Error).message.contains("missing contracts"))
    }

    private fun bootstrap(ageMode: PresetValueMode = PresetValueMode.SUGGESTED): ProductionDraftBootstrap {
        val preset = ProductionPreset(
            presetId = "test-preset",
            version = "2.4",
            label = "Test editorial preset",
            assetType = AssetType.NPC_PORTRAIT,
            vocabularySetId = "test-set",
            vocabularySetVersion = "7.1",
            selections = PresetSelections(
                subject = SubjectSelections(ageBandId = PresetValue(ageMode, "adult")),
                visual = VisualSelections(expressionId = PresetValue(PresetValueMode.SUGGESTED, "neutral")),
            ),
        )
        val set = VocabularySet(
            vocabularySetId = "test-set",
            version = "7.1",
            bindings = mapOf(
                ProductionFieldPaths.SUBJECT_AGE_BAND_ID to VocabularyReference("custom-ages", "3.0"),
                ProductionFieldPaths.VISUAL_EXPRESSION_ID to VocabularyReference("custom-expressions", "8.0"),
            ),
        )
        val service = ProductionDraftService(
            presets = PresetRegistry.create(listOf(preset)),
            vocabularySets = VocabularySetRegistry.create(listOf(set)),
            vocabularies = VocabularyRegistry.create(
                listOf(
                    Vocabulary(
                        "custom-ages",
                        "3.0",
                        listOf(
                            VocabularyValue("adult", "Adult", "Current age band"),
                            VocabularyValue("elder", "Elder", "Former age band", VocabularyValueStatus.DEPRECATED),
                        ),
                    ),
                    Vocabulary("custom-expressions", "8.0", listOf(VocabularyValue("neutral", "Neutral"))),
                ),
            ),
        )
        return ProductionDraftBootstrap {
            ProductionDraftEnvironment(service, service.startDraft(preset.presetId, preset.version), preset.label)
        }
    }

    private fun AssetManagerViewModel.ready(): AssetManagerUiState.Ready {
        assertTrue(uiState is AssetManagerUiState.Ready)
        return uiState as AssetManagerUiState.Ready
    }

    private fun AssetManagerUiState.Ready.field(path: String) = fields.single { it.fieldPath == path }
}

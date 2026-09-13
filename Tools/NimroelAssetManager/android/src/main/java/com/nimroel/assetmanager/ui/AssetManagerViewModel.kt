package com.nimroel.assetmanager.ui

import android.content.res.AssetManager
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.nimroel.assetmanager.data.contracts.AndroidProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftEnvironment
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.VocabularyValueStatus
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.domain.production.ProductionDraftException

sealed interface AssetManagerUiState {
    data object Loading : AssetManagerUiState

    data class Error(val message: String) : AssetManagerUiState

    data class Ready(
        val screenTitle: String,
        val screenSubtitle: String,
        val presetLabel: String,
        val presetId: String,
        val presetVersion: String,
        val assetType: AssetType,
        val assetTypeLabel: String,
        val vocabularySetId: String,
        val vocabularySetVersion: String,
        val fields: List<ProductionFieldUiState>,
        val summary: ProductionDraftSummaryUiState,
        val actionError: String? = null,
    ) : AssetManagerUiState
}

data class ProductionFieldUiState(
    val fieldPath: String,
    val label: String,
    val selectedValueId: String?,
    val selectedValueLabel: String?,
    val selectedValueDeprecated: Boolean,
    val values: List<VocabularyValueUiState>,
    val presetMode: PresetValueMode?,
    val source: DraftSelectionSource?,
    val isLocked: Boolean,
    val isEditable: Boolean,
    val canClear: Boolean,
)

data class VocabularyValueUiState(
    val valueId: String,
    val label: String,
    val description: String?,
    val isDeprecated: Boolean,
)

data class ProductionDraftSummaryUiState(
    val activeSelectionCount: Int,
    val selections: List<ProductionSummarySelectionUiState>,
)

data class ProductionSummarySelectionUiState(
    val fieldLabel: String,
    val valueLabel: String,
    val isDeprecated: Boolean,
)

class AssetManagerViewModel(
    private val bootstrap: ProductionDraftBootstrap,
) : ViewModel() {
    var uiState: AssetManagerUiState by mutableStateOf(AssetManagerUiState.Loading)
        private set

    private var environment: ProductionDraftEnvironment? = null
    private var initialPresetModes: Map<String, PresetValueMode> = emptyMap()

    init {
        loadPilot()
    }

    fun selectValue(fieldPath: String, valueId: String) {
        val current = environment ?: return
        try {
            val updatedDraft = current.service.setSelection(current.draft, fieldPath, valueId)
            environment = current.copy(draft = updatedDraft)
            uiState = environment!!.toReadyState(initialPresetModes)
        } catch (error: ProductionDraftException) {
            uiState = current.toReadyState(initialPresetModes, error.message ?: "No se pudo actualizar la selección.")
        }
    }

    fun clearSelection(fieldPath: String) {
        val current = environment ?: return
        try {
            val updatedDraft = current.service.clearSelection(current.draft, fieldPath)
            environment = current.copy(draft = updatedDraft)
            uiState = environment!!.toReadyState(initialPresetModes)
        } catch (error: ProductionDraftException) {
            uiState = current.toReadyState(initialPresetModes, error.message ?: "No se pudo eliminar la selección.")
        }
    }

    private fun loadPilot() {
        uiState = AssetManagerUiState.Loading
        try {
            val loaded = bootstrap.load()
            environment = loaded
            initialPresetModes = loaded.draft.selections.mapNotNull { (path, selection) ->
                selection.presetMode?.let { path to it }
            }.toMap()
            uiState = loaded.toReadyState(initialPresetModes)
        } catch (error: Exception) {
            uiState = AssetManagerUiState.Error(
                "No se pudieron cargar los contratos de producción. ${error.message ?: "Error inesperado."}",
            )
        }
    }

    companion object {
        fun factory(assets: AssetManager): ViewModelProvider.Factory = object : ViewModelProvider.Factory {
            @Suppress("UNCHECKED_CAST")
            override fun <T : ViewModel> create(modelClass: Class<T>): T {
                require(modelClass.isAssignableFrom(AssetManagerViewModel::class.java))
                return AssetManagerViewModel(AndroidProductionDraftBootstrap(assets)) as T
            }
        }
    }
}

private data class ProductionFieldPresentation(val path: String, val label: String)

private val productionFieldPresentations = listOf(
    ProductionFieldPresentation(ProductionFieldPaths.CLASSIFICATION_REALM_ID, "Reino"),
    ProductionFieldPresentation(ProductionFieldPaths.CLASSIFICATION_CULTURE_ID, "Cultura"),
    ProductionFieldPresentation(ProductionFieldPaths.SUBJECT_SPECIES_ID, "Especie"),
    ProductionFieldPresentation(ProductionFieldPaths.SUBJECT_GENDER_ID, "Género"),
    ProductionFieldPresentation(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "Rango de edad"),
    ProductionFieldPresentation(ProductionFieldPaths.DETAILS_PROFESSION_ID, "Profesión"),
    ProductionFieldPresentation(ProductionFieldPaths.DETAILS_SOCIAL_CLASS_ID, "Clase social"),
    ProductionFieldPresentation(ProductionFieldPaths.VISUAL_EXPRESSION_ID, "Expresión"),
)

private fun ProductionDraftEnvironment.toReadyState(
    initialPresetModes: Map<String, PresetValueMode>,
    actionError: String? = null,
): AssetManagerUiState.Ready {
    val boundPaths = service.boundVocabularyFieldPaths(draft)
    val fields = productionFieldPresentations.mapNotNull { presentation ->
        if (presentation.path !in boundPaths) return@mapNotNull null
        val values = service.availableValues(draft, presentation.path).map { value ->
            VocabularyValueUiState(
                valueId = value.id,
                label = value.label,
                description = value.description,
                isDeprecated = value.status == VocabularyValueStatus.DEPRECATED,
            )
        }
        val selection = draft.selections[presentation.path]
        val selectedValue = values.firstOrNull { it.valueId == selection?.value }
        val presetMode = selection?.presetMode ?: initialPresetModes[presentation.path]
        ProductionFieldUiState(
            fieldPath = presentation.path,
            label = presentation.label,
            selectedValueId = selection?.value,
            selectedValueLabel = selectedValue?.label,
            selectedValueDeprecated = selectedValue?.isDeprecated == true,
            values = values,
            presetMode = presetMode,
            source = selection?.source,
            isLocked = presetMode == PresetValueMode.FIXED,
            isEditable = presetMode != PresetValueMode.FIXED,
            canClear = selection != null && presetMode != PresetValueMode.FIXED,
        )
    }
    val summarySelections = fields.mapNotNull { field ->
        field.selectedValueLabel?.let { label ->
            ProductionSummarySelectionUiState(field.label, label, field.selectedValueDeprecated)
        }
    }
    return AssetManagerUiState.Ready(
        screenTitle = "Nueva producción",
        screenSubtitle = draft.assetType.displayLabel(),
        presetLabel = presetLabel,
        presetId = draft.presetId,
        presetVersion = draft.presetVersion,
        assetType = draft.assetType,
        assetTypeLabel = draft.assetType.displayLabel(),
        vocabularySetId = draft.vocabularySetId,
        vocabularySetVersion = draft.vocabularySetVersion,
        fields = fields,
        summary = ProductionDraftSummaryUiState(summarySelections.size, summarySelections),
        actionError = actionError,
    )
}

private fun AssetType.displayLabel(): String = when (this) {
    AssetType.NPC_PORTRAIT -> "Retrato de PNJ"
    AssetType.LANDSCAPE -> "Paisaje"
    AssetType.SETTLEMENT -> "Asentamiento"
    AssetType.BUILDING -> "Edificio"
    AssetType.INTERIOR -> "Interior"
    AssetType.OBJECT -> "Objeto"
    AssetType.ENVIRONMENT_SCENE -> "Escena de entorno"
}

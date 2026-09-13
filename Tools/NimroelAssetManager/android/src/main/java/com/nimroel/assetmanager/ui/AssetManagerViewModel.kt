package com.nimroel.assetmanager.ui

import android.content.Context
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import com.nimroel.assetmanager.data.contracts.AndroidProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftBootstrap
import com.nimroel.assetmanager.data.contracts.ProductionDraftEnvironment
import com.nimroel.assetmanager.data.image.AndroidImageContentPreparer
import com.nimroel.assetmanager.data.local.LocalAssetStoreFactory
import com.nimroel.assetmanager.data.staging.AndroidStagingFileStore
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.VocabularyValueStatus
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.identity.RandomUuidWorkIdGenerator
import com.nimroel.assetmanager.domain.identity.UuidV7AssetIdGenerator
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.domain.production.ProductionDraftException
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.LocalIngestCoordinator
import com.nimroel.assetmanager.domain.processing.LocalIngestResult
import com.nimroel.assetmanager.domain.processing.PreparedImage
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

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
        val imageState: ImageUiState = ImageUiState.NoImage,
        val localIngestState: LocalIngestUiState = LocalIngestUiState.NotStarted,
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

sealed interface ImageUiState {
    data object NoImage : ImageUiState
    data class Processing(val previousPrepared: PreparedImageUiState?) : ImageUiState
    data class Prepared(val image: PreparedImageUiState) : ImageUiState
    data class ImageError(val message: String, val previousPrepared: PreparedImageUiState?) : ImageUiState
}

data class PreparedImageUiState(
    val content: Content,
)

sealed interface LocalIngestUiState {
    data object NotStarted : LocalIngestUiState
    data object Processing : LocalIngestUiState
    data class Ready(
        val reservedAssetId: String,
        val status: String,
        val content: Content,
    ) : LocalIngestUiState

    data class Failed(
        val errorCode: String,
        val message: String,
    ) : LocalIngestUiState
}

class AssetManagerViewModel(
    private val bootstrap: ProductionDraftBootstrap,
    private val imageContentPreparer: ImageContentPreparer = UnavailableImageContentPreparer,
    private val imageDispatcher: CoroutineDispatcher = Dispatchers.IO,
    private val localIngestCoordinator: LocalIngestCoordinator? = null,
) : ViewModel() {
    var uiState: AssetManagerUiState by mutableStateOf(AssetManagerUiState.Loading)
        private set

    private var environment: ProductionDraftEnvironment? = null
    private var initialPresetModes: Map<String, PresetValueMode> = emptyMap()
    private var imagePreparationJob: Job? = null
    private var imageRequestGeneration = 0L
    private var preparedImage: PreparedImage? = null
    private var imageState: ImageUiState = ImageUiState.NoImage
    private var localIngestState: LocalIngestUiState = LocalIngestUiState.NotStarted
    private var draftActionError: String? = null

    init {
        loadPilot()
    }

    fun selectValue(fieldPath: String, valueId: String) {
        val current = environment ?: return
        try {
            val updatedDraft = current.service.setSelection(current.draft, fieldPath, valueId)
            environment = current.copy(draft = updatedDraft)
            draftActionError = null
            refreshReadyState()
        } catch (error: ProductionDraftException) {
            draftActionError = error.message ?: "No se pudo actualizar la selección."
            refreshReadyState()
        }
    }

    fun clearSelection(fieldPath: String) {
        val current = environment ?: return
        try {
            val updatedDraft = current.service.clearSelection(current.draft, fieldPath)
            environment = current.copy(draft = updatedDraft)
            draftActionError = null
            refreshReadyState()
        } catch (error: ProductionDraftException) {
            draftActionError = error.message ?: "No se pudo eliminar la selección."
            refreshReadyState()
        }
    }

    fun selectImage(sourceRef: ImageSourceRef?) {
        if (sourceRef == null || environment == null || localIngestState.locksImage()) return
        val previousPrepared = preparedImage?.toUiState()
        val requestGeneration = ++imageRequestGeneration
        imagePreparationJob?.cancel()
        imageState = ImageUiState.Processing(previousPrepared)
        refreshReadyState()
        imagePreparationJob = viewModelScope.launch {
            try {
                val result = withContext(imageDispatcher) { imageContentPreparer.prepare(sourceRef) }
                if (requestGeneration != imageRequestGeneration) return@launch
                preparedImage = result
                imageState = ImageUiState.Prepared(result.toUiState())
                localIngestState = LocalIngestUiState.NotStarted
                refreshReadyState()
            } catch (error: CancellationException) {
                throw error
            } catch (error: ImagePreparationException) {
                if (requestGeneration != imageRequestGeneration) return@launch
                imageState = ImageUiState.ImageError(
                    message = error.message ?: "No se pudo preparar la imagen seleccionada.",
                    previousPrepared = previousPrepared,
                )
                refreshReadyState()
            }
        }
    }

    fun removeImage() {
        if (localIngestState.locksImage()) return
        imagePreparationJob?.cancel()
        imagePreparationJob = null
        imageRequestGeneration += 1
        preparedImage = null
        imageState = ImageUiState.NoImage
        localIngestState = LocalIngestUiState.NotStarted
        refreshReadyState()
    }

    fun prepareLocalIngest() {
        val image = preparedImage ?: return
        val coordinator = localIngestCoordinator ?: return
        if (localIngestState is LocalIngestUiState.Processing || localIngestState is LocalIngestUiState.Ready) return
        localIngestState = LocalIngestUiState.Processing
        refreshReadyState()
        viewModelScope.launch {
            try {
                when (val result = withContext(imageDispatcher) { coordinator.begin(image) }) {
                    is LocalIngestResult.Ready -> {
                        localIngestState = LocalIngestUiState.Ready(
                            reservedAssetId = result.workItem.reservedAssetId.value,
                            status = result.workItem.state.wireValue,
                            content = result.stagedImage.content,
                        )
                    }

                    is LocalIngestResult.Failed -> {
                        localIngestState = LocalIngestUiState.Failed(
                            errorCode = result.workItem.errorCode ?: "unexpected_io",
                            message = result.workItem.errorDetail ?: "No se pudo preparar la ingestión local.",
                        )
                    }
                }
                refreshReadyState()
            } catch (error: CancellationException) {
                throw error
            } catch (_: Exception) {
                localIngestState = LocalIngestUiState.Failed(
                    errorCode = "unexpected_io",
                    message = "No se pudo completar la ingestión local.",
                )
                refreshReadyState()
            }
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
            refreshReadyState()
        } catch (error: Exception) {
            uiState = AssetManagerUiState.Error(
                "No se pudieron cargar los contratos de producción. ${error.message ?: "Error inesperado."}",
            )
        }
    }

    private fun refreshReadyState() {
        environment?.let { loaded ->
            uiState = loaded.toReadyState(initialPresetModes, imageState, localIngestState, draftActionError)
        }
    }

    companion object {
        fun factory(context: Context): ViewModelProvider.Factory = object : ViewModelProvider.Factory {
            @Suppress("UNCHECKED_CAST")
            override fun <T : ViewModel> create(modelClass: Class<T>): T {
                require(modelClass.isAssignableFrom(AssetManagerViewModel::class.java))
                val applicationContext = context.applicationContext
                val localStore = LocalAssetStoreFactory.create(applicationContext)
                return AssetManagerViewModel(
                    bootstrap = AndroidProductionDraftBootstrap(applicationContext.assets),
                    imageContentPreparer = AndroidImageContentPreparer(applicationContext.contentResolver),
                    localIngestCoordinator = LocalIngestCoordinator(
                        assetIdGenerator = UuidV7AssetIdGenerator(),
                        workIdGenerator = RandomUuidWorkIdGenerator(),
                        stagingFileStore = AndroidStagingFileStore(applicationContext),
                        workItemStore = localStore,
                    ),
                ) as T
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
    imageState: ImageUiState = ImageUiState.NoImage,
    localIngestState: LocalIngestUiState = LocalIngestUiState.NotStarted,
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
        imageState = imageState,
        localIngestState = localIngestState,
        actionError = actionError,
    )
}

private fun PreparedImage.toUiState() = PreparedImageUiState(content)

private fun LocalIngestUiState.locksImage(): Boolean =
    this is LocalIngestUiState.Processing || this is LocalIngestUiState.Ready

private object UnavailableImageContentPreparer : ImageContentPreparer {
    override suspend fun prepare(sourceRef: ImageSourceRef): PreparedImage {
        throw ImagePreparationException("No hay un preparador de imagen configurado.")
    }
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

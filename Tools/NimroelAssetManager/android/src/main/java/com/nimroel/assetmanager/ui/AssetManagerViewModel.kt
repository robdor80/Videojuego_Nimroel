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
import com.nimroel.assetmanager.data.image.AndroidImageLabProcessor
import com.nimroel.assetmanager.data.image.ImageLabPreviewLoader
import com.nimroel.assetmanager.data.local.LocalAssetStoreFactory
import com.nimroel.assetmanager.data.staging.AndroidStagingFileStore
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.VocabularyValueStatus
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.OriginKind
import com.nimroel.assetmanager.domain.model.Provenance
import com.nimroel.assetmanager.domain.identity.RandomUuidWorkIdGenerator
import com.nimroel.assetmanager.domain.identity.UuidV7AssetIdGenerator
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.domain.production.ProvenanceDraft
import com.nimroel.assetmanager.domain.production.ProvenanceDraftService
import com.nimroel.assetmanager.domain.production.ProvenanceMaterialization
import com.nimroel.assetmanager.domain.production.ProductionDraftException
import com.nimroel.assetmanager.domain.processing.ImageContentPreparer
import com.nimroel.assetmanager.domain.processing.DiscardedStagingCleanupException
import com.nimroel.assetmanager.domain.processing.ImageLabArtifactRef
import com.nimroel.assetmanager.domain.processing.ImageLabException
import com.nimroel.assetmanager.domain.processing.ImageLabExifStatus
import com.nimroel.assetmanager.domain.processing.ImageLabProcessor
import com.nimroel.assetmanager.domain.processing.ImageLabProfile
import com.nimroel.assetmanager.domain.processing.ImageLabRequest
import com.nimroel.assetmanager.domain.processing.ImageLabResult
import com.nimroel.assetmanager.domain.processing.ImagePreparationException
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.domain.processing.LocalIngestCoordinator
import com.nimroel.assetmanager.domain.processing.LocalIngestResult
import com.nimroel.assetmanager.domain.processing.PreparedImage
import com.nimroel.assetmanager.domain.processing.StagedImageLabSource
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.time.Clock
import java.time.Instant

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
        val imageLabState: ImageLabUiState = ImageLabUiState.Unavailable,
        val provenanceState: ProvenanceUiState = ProvenanceUiState.Unavailable,
        val isAssetCreationEnabled: Boolean = false,
        val assetCreationExplanation: String = "Aún faltan una procedencia válida, el procesamiento del binario canónico y la finalización antes de crear el Asset.",
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

data class ImageLabSessionUiState(
    val sourceContent: Content,
    val selectedTargetLongEdge: Int = 1536,
    val selectedQuality: Int = 85,
    val results: List<ImageLabResultUiState> = emptyList(),
)

data class ImageLabResultUiState(
    val workId: String,
    val mimeType: String,
    val widthPx: Int,
    val heightPx: Int,
    val byteSize: Long,
    val requestedTargetLongEdge: Int,
    val quality: Int,
    val reductionBytes: Long?,
    val reductionPercent: Double?,
    val sourceHasAlphaCapability: Boolean,
    val transparentPixelsObserved: Boolean,
    val orientationApplied: Boolean,
    val exifStatus: ImageLabExifStatus,
    val artifactRef: ImageLabArtifactRef,
)

sealed interface ImageLabUiState {
    data object Unavailable : ImageLabUiState
    data class Idle(val session: ImageLabSessionUiState) : ImageLabUiState
    data class Processing(val session: ImageLabSessionUiState, val operation: String) : ImageLabUiState
    data class Results(val session: ImageLabSessionUiState) : ImageLabUiState
    data class Error(val session: ImageLabSessionUiState, val message: String) : ImageLabUiState
}

sealed interface LocalIngestUiState {
    data object NotStarted : LocalIngestUiState
    data object Processing : LocalIngestUiState
    data object Discarding : LocalIngestUiState
    data class Ready(
        internal val workId: String,
        val reservedAssetId: String,
        val status: String,
        val content: Content,
    ) : LocalIngestUiState

    data class Failed(
        val errorCode: String,
        val message: String,
    ) : LocalIngestUiState
}

data class ProvenanceFormUiState(
    val originKind: OriginKind,
    val provider: String = "",
    val model: String = "",
    val generatedAt: String = "",
    val importedAt: String = "",
    val sourceAssetIds: String = "",
    val unknownConfirmed: Boolean = false,
)

sealed interface ProvenanceUiState {
    data object Unavailable : ProvenanceUiState
    data object NotSpecified : ProvenanceUiState
    data class Invalid(val form: ProvenanceFormUiState, val errors: List<String>) : ProvenanceUiState
    data class Valid(val form: ProvenanceFormUiState, val provenance: Provenance) : ProvenanceUiState
}

class AssetManagerViewModel(
    private val bootstrap: ProductionDraftBootstrap,
    private val imageContentPreparer: ImageContentPreparer = UnavailableImageContentPreparer,
    private val imageDispatcher: CoroutineDispatcher = Dispatchers.IO,
    private val localIngestCoordinator: LocalIngestCoordinator? = null,
    private val imageLabProcessor: ImageLabProcessor? = null,
    val imageLabPreviewLoader: ImageLabPreviewLoader? = null,
    private val provenanceDraftService: ProvenanceDraftService = ProvenanceDraftService(),
    private val clock: Clock = Clock.systemUTC(),
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
    private var imageLabState: ImageLabUiState = ImageLabUiState.Unavailable
    private var currentImageLabSource: StagedImageLabSource? = null
    private var imageLabJob: Job? = null
    private var imageLabGeneration = 0L
    private var provenanceDraft: ProvenanceDraft = ProvenanceDraft.NotSpecified
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
                resetImageLab()
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
        resetImageLab()
        refreshReadyState()
    }

    fun prepareLocalIngest() {
        val image = preparedImage ?: return
        val coordinator = localIngestCoordinator ?: return
        if (
            localIngestState is LocalIngestUiState.Processing ||
            localIngestState is LocalIngestUiState.Discarding ||
            localIngestState is LocalIngestUiState.Ready
        ) return
        localIngestState = LocalIngestUiState.Processing
        refreshReadyState()
        viewModelScope.launch {
            try {
                when (val result = withContext(imageDispatcher) { coordinator.begin(image) }) {
                    is LocalIngestResult.Ready -> {
                        localIngestState = LocalIngestUiState.Ready(
                            workId = result.workItem.workId,
                            reservedAssetId = result.workItem.reservedAssetId.value,
                            status = result.workItem.state.wireValue,
                            content = result.stagedImage.content,
                        )
                        activateImageLab(StagedImageLabSource.from(result.workItem.workId, result.stagedImage))
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

    fun selectImageLabTarget(targetLongEdge: Int) {
        if (targetLongEdge !in ImageLabProfile.TARGET_LONG_EDGES || imageLabState is ImageLabUiState.Processing) return
        updateImageLabSession { it.copy(selectedTargetLongEdge = targetLongEdge) }
    }

    fun selectImageLabQuality(quality: Int) {
        if (quality !in ImageLabProfile.QUALITIES || imageLabState is ImageLabUiState.Processing) return
        updateImageLabSession { it.copy(selectedQuality = quality) }
    }

    fun generateImageLabCandidate() {
        val processor = imageLabProcessor ?: return
        val source = currentImageLabSource ?: return
        val session = imageLabState.sessionOrNull() ?: return
        if (imageLabState is ImageLabUiState.Processing) return
        val generation = ++imageLabGeneration
        imageLabState = ImageLabUiState.Processing(session, "Generando WebP…")
        refreshReadyState()
        imageLabJob = viewModelScope.launch {
            try {
                val result = withContext(imageDispatcher) {
                    processor.generate(
                        ImageLabRequest(
                            source = source,
                            profile = ImageLabProfile(session.selectedTargetLongEdge, session.selectedQuality),
                        ),
                    )
                }
                if (generation != imageLabGeneration || currentImageLabSource?.workId != source.workId) return@launch
                if (result.workId != source.workId) throw ImageLabException("El resultado no pertenece al staged work actual.")
                val uiResult = result.toUiState()
                val results = session.results
                    .filterNot {
                        it.requestedTargetLongEdge == uiResult.requestedTargetLongEdge &&
                            it.quality == uiResult.quality
                    } + uiResult
                imageLabState = ImageLabUiState.Results(session.copy(results = results))
                refreshReadyState()
            } catch (error: CancellationException) {
                throw error
            } catch (error: DiscardedStagingCleanupException) {
                if (generation != imageLabGeneration) return@launch
                imageLabJob = null
                currentImageLabSource = null
                preparedImage = null
                imageState = ImageUiState.NoImage
                localIngestState = LocalIngestUiState.NotStarted
                imageLabState = ImageLabUiState.Unavailable
                provenanceDraft = ProvenanceDraft.NotSpecified
                draftActionError = "La ingestión se descartó, pero no se pudo limpiar por completo su almacenamiento temporal."
                refreshReadyState()
            } catch (error: Exception) {
                if (generation != imageLabGeneration || currentImageLabSource?.workId != source.workId) return@launch
                imageLabState = ImageLabUiState.Error(
                    session,
                    error.message ?: "No se pudo generar la prueba WebP.",
                )
                refreshReadyState()
            }
        }
    }

    fun discardLocalIngest() {
        val coordinator = localIngestCoordinator ?: return
        val ready = localIngestState as? LocalIngestUiState.Ready ?: return
        if (currentImageLabSource?.workId?.let { it != ready.workId } == true) return
        val session = imageLabState.sessionOrNull()
        val generation = ++imageLabGeneration
        imageLabJob?.cancel()
        localIngestState = LocalIngestUiState.Discarding
        imageLabState = session?.let { ImageLabUiState.Processing(it, "Descartando ingestión…") }
            ?: ImageLabUiState.Unavailable
        refreshReadyState()
        viewModelScope.launch {
            try {
                withContext(imageDispatcher) {
                    imageLabProcessor?.clear(ready.workId)
                    coordinator.discardReady(ready.workId)
                }
                if (generation != imageLabGeneration) return@launch
                imageLabJob = null
                currentImageLabSource = null
                preparedImage = null
                imageState = ImageUiState.NoImage
                localIngestState = LocalIngestUiState.NotStarted
                imageLabState = ImageLabUiState.Unavailable
                provenanceDraft = ProvenanceDraft.NotSpecified
                draftActionError = null
                refreshReadyState()
            } catch (error: CancellationException) {
                throw error
            } catch (error: Exception) {
                if (generation != imageLabGeneration) return@launch
                localIngestState = ready
                imageLabState = ImageLabUiState.Idle(
                    ImageLabSessionUiState(
                        sourceContent = ready.content,
                        selectedTargetLongEdge = session?.selectedTargetLongEdge ?: 1536,
                        selectedQuality = session?.selectedQuality ?: 85,
                    ),
                )
                draftActionError = error.message ?: "No se pudo descartar la ingestión local."
                refreshReadyState()
            }
        }
    }

    fun clearImageLabResults() {
        val processor = imageLabProcessor ?: return
        val source = currentImageLabSource ?: return
        val session = imageLabState.sessionOrNull() ?: return
        imageLabJob?.cancel()
        val generation = ++imageLabGeneration
        imageLabState = ImageLabUiState.Processing(session, "Limpiando pruebas…")
        refreshReadyState()
        imageLabJob = viewModelScope.launch {
            try {
                withContext(imageDispatcher) { processor.clear(source.workId) }
                if (generation != imageLabGeneration || currentImageLabSource?.workId != source.workId) return@launch
                imageLabState = ImageLabUiState.Idle(session.copy(results = emptyList()))
                refreshReadyState()
            } catch (error: CancellationException) {
                throw error
            } catch (error: Exception) {
                if (generation != imageLabGeneration || currentImageLabSource?.workId != source.workId) return@launch
                imageLabState = ImageLabUiState.Error(
                    session,
                    error.message ?: "No se pudieron limpiar las pruebas temporales.",
                )
                refreshReadyState()
            }
        }
    }

    fun selectProvenanceKind(originKind: OriginKind) = updateProvenance {
        provenanceDraftService.select(originKind)
    }

    fun setGeneratedProvider(value: String) = updateProvenance {
        provenanceDraftService.setGeneratedProvider(it, value)
    }

    fun setGeneratedModel(value: String) = updateProvenance {
        provenanceDraftService.setGeneratedModel(it, value)
    }

    fun setGeneratedAt(value: String) = updateProvenance {
        provenanceDraftService.setGeneratedAt(it, value)
    }

    fun useCurrentGeneratedAt() = updateProvenance {
        provenanceDraftService.useGeneratedAt(it, Instant.now(clock))
    }

    fun setImportedAt(value: String) = updateProvenance {
        provenanceDraftService.setImportedAt(it, value)
    }

    fun useCurrentImportedAt() = updateProvenance {
        provenanceDraftService.useImportedAt(it, Instant.now(clock))
    }

    fun setSourceAssetIds(value: String) = updateProvenance {
        provenanceDraftService.setSourceAssetIds(it, value)
    }

    fun setUnknownConfirmed(confirmed: Boolean) = updateProvenance {
        provenanceDraftService.setUnknownConfirmed(it, confirmed)
    }

    private inline fun updateProvenance(transform: (ProvenanceDraft) -> ProvenanceDraft) {
        if (localIngestState !is LocalIngestUiState.Ready) return
        provenanceDraft = transform(provenanceDraft)
        refreshReadyState()
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
            uiState = loaded.toReadyState(
                initialPresetModes,
                imageState,
                localIngestState,
                imageLabState,
                provenanceDraft.toUiState(localIngestState, provenanceDraftService),
                draftActionError,
            )
        }
    }

    companion object {
        fun factory(context: Context): ViewModelProvider.Factory = object : ViewModelProvider.Factory {
            @Suppress("UNCHECKED_CAST")
            override fun <T : ViewModel> create(modelClass: Class<T>): T {
                require(modelClass.isAssignableFrom(AssetManagerViewModel::class.java))
                val applicationContext = context.applicationContext
                val localStore = LocalAssetStoreFactory.create(applicationContext)
                val imageLab = AndroidImageLabProcessor(applicationContext)
                return AssetManagerViewModel(
                    bootstrap = AndroidProductionDraftBootstrap(applicationContext.assets),
                    imageContentPreparer = AndroidImageContentPreparer(applicationContext.contentResolver),
                    localIngestCoordinator = LocalIngestCoordinator(
                        assetIdGenerator = UuidV7AssetIdGenerator(),
                        workIdGenerator = RandomUuidWorkIdGenerator(),
                        stagingFileStore = AndroidStagingFileStore(applicationContext),
                        workItemStore = localStore,
                    ),
                    imageLabProcessor = imageLab,
                    imageLabPreviewLoader = imageLab,
                ) as T
            }
        }
    }

    internal fun activateImageLab(source: StagedImageLabSource) {
        val previous = currentImageLabSource
        if (previous != null && previous.workId != source.workId) {
            imageLabJob?.cancel()
            imageLabProcessor?.let { processor ->
                viewModelScope.launch { withContext(imageDispatcher) { processor.clear(previous.workId) } }
            }
        }
        imageLabGeneration += 1
        currentImageLabSource = source
        imageLabState = if (imageLabProcessor != null && imageLabPreviewLoader != null) {
            ImageLabUiState.Idle(ImageLabSessionUiState(source.content))
        } else {
            ImageLabUiState.Unavailable
        }
        refreshReadyState()
    }

    private fun resetImageLab() {
        val previous = currentImageLabSource
        imageLabJob?.cancel()
        imageLabJob = null
        imageLabGeneration += 1
        currentImageLabSource = null
        imageLabState = ImageLabUiState.Unavailable
        if (previous != null) {
            imageLabProcessor?.let { processor ->
                viewModelScope.launch { withContext(imageDispatcher) { processor.clear(previous.workId) } }
            }
        }
    }

    private fun updateImageLabSession(transform: (ImageLabSessionUiState) -> ImageLabSessionUiState) {
        val updated = imageLabState.sessionOrNull()?.let(transform) ?: return
        imageLabState = if (updated.results.isEmpty()) ImageLabUiState.Idle(updated) else ImageLabUiState.Results(updated)
        refreshReadyState()
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
    imageLabState: ImageLabUiState = ImageLabUiState.Unavailable,
    provenanceState: ProvenanceUiState = ProvenanceUiState.Unavailable,
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
        imageLabState = imageLabState,
        provenanceState = provenanceState,
        isAssetCreationEnabled = false,
        assetCreationExplanation = if (provenanceState is ProvenanceUiState.Valid) {
            "Aún faltan el procesamiento del binario canónico y la finalización antes de crear el Asset."
        } else {
            "Aún faltan una procedencia válida, el procesamiento del binario canónico y la finalización antes de crear el Asset."
        },
        actionError = actionError,
    )
}

private fun PreparedImage.toUiState() = PreparedImageUiState(content)

private fun ImageLabUiState.sessionOrNull(): ImageLabSessionUiState? = when (this) {
    ImageLabUiState.Unavailable -> null
    is ImageLabUiState.Idle -> session
    is ImageLabUiState.Processing -> session
    is ImageLabUiState.Results -> session
    is ImageLabUiState.Error -> session
}

private fun ImageLabResult.toUiState() = ImageLabResultUiState(
    workId = workId,
    mimeType = mimeType,
    widthPx = widthPx,
    heightPx = heightPx,
    byteSize = byteSize,
    requestedTargetLongEdge = requestedTargetLongEdge,
    quality = quality,
    reductionBytes = reduction?.absoluteBytes,
    reductionPercent = reduction?.percent,
    sourceHasAlphaCapability = sourceHasAlphaCapability,
    transparentPixelsObserved = transparentPixelsObserved,
    orientationApplied = orientationApplied,
    exifStatus = exifStatus,
    artifactRef = artifactRef,
)

private fun LocalIngestUiState.locksImage(): Boolean =
    this is LocalIngestUiState.Processing ||
        this is LocalIngestUiState.Discarding ||
        this is LocalIngestUiState.Ready

private fun ProvenanceDraft.toUiState(
    localIngestState: LocalIngestUiState,
    service: ProvenanceDraftService,
): ProvenanceUiState {
    val ready = localIngestState as? LocalIngestUiState.Ready ?: return ProvenanceUiState.Unavailable
    if (this == ProvenanceDraft.NotSpecified) return ProvenanceUiState.NotSpecified
    val form = toFormUiState()
    return when (val result = service.materialize(this, AssetId.parse(ready.reservedAssetId))) {
        is ProvenanceMaterialization.Invalid -> ProvenanceUiState.Invalid(form, result.errors.map { it.message })
        is ProvenanceMaterialization.Valid -> ProvenanceUiState.Valid(form, result.provenance)
    }
}

private fun ProvenanceDraft.toFormUiState(): ProvenanceFormUiState = when (this) {
    ProvenanceDraft.NotSpecified -> error("NotSpecified has no provenance form.")
    is ProvenanceDraft.Generated -> ProvenanceFormUiState(
        originKind = OriginKind.GENERATED,
        provider = provider,
        model = model,
        generatedAt = generatedAt.text,
    )
    is ProvenanceDraft.Imported -> ProvenanceFormUiState(
        originKind = OriginKind.IMPORTED,
        importedAt = importedAt.text,
    )
    is ProvenanceDraft.Edited -> ProvenanceFormUiState(OriginKind.EDITED, sourceAssetIds = sourceAssetIdsText)
    is ProvenanceDraft.Derived -> ProvenanceFormUiState(OriginKind.DERIVED, sourceAssetIds = sourceAssetIdsText)
    is ProvenanceDraft.Unknown -> ProvenanceFormUiState(OriginKind.UNKNOWN, unknownConfirmed = confirmed)
}

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

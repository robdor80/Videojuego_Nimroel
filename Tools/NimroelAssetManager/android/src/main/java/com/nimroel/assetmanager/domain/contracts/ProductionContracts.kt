package com.nimroel.assetmanager.domain.contracts

import com.nimroel.assetmanager.domain.model.AssetType
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

object ContractJson {
    val codec = Json { encodeDefaults = false; explicitNulls = false; ignoreUnknownKeys = false }
}

@Serializable data class Vocabulary(val vocabularyId: String, val version: String, val values: List<VocabularyValue>)
@Serializable data class VocabularyValue(val id: String, val label: String, val description: String? = null, val status: VocabularyValueStatus = VocabularyValueStatus.ACTIVE, val presentationOrder: Int? = null)
@Serializable enum class VocabularyValueStatus { @kotlinx.serialization.SerialName("active") ACTIVE, @kotlinx.serialization.SerialName("deprecated") DEPRECATED }
@Serializable data class VocabularyReference(val vocabularyId: String, val version: String)
@Serializable data class VocabularySet(val vocabularySetId: String, val version: String, val bindings: Map<String, VocabularyReference>)

class VocabularyRegistry private constructor(private val entries: Map<ContractKey, Vocabulary>) {
    fun vocabulary(id: String, version: String): Vocabulary? = entries[ContractKey(id, version)]
    fun value(id: String, version: String, valueId: String): VocabularyValue? = vocabulary(id, version)?.values?.firstOrNull { it.id == valueId }

    companion object {
        fun create(vocabularies: Iterable<Vocabulary>): VocabularyRegistry {
            val list = vocabularies.toList()
            require(list.map { ContractKey(it.vocabularyId, it.version) }.distinct().size == list.size) { "Vocabulary ID/version pairs must be unique." }
            list.forEach { vocabulary ->
                require(vocabulary.values.isNotEmpty()) { "Vocabulary ${vocabulary.vocabularyId} cannot be empty." }
                require(vocabulary.values.map(VocabularyValue::id).distinct().size == vocabulary.values.size) { "Vocabulary ${vocabulary.vocabularyId} contains duplicate value IDs." }
            }
            return VocabularyRegistry(list.associateBy { ContractKey(it.vocabularyId, it.version) })
        }
    }
}

class VocabularySetRegistry private constructor(private val entries: Map<ContractKey, VocabularySet>) {
    fun vocabularySet(id: String, version: String): VocabularySet? = entries[ContractKey(id, version)]
    fun binding(setId: String, setVersion: String, fieldPath: String): VocabularyReference? = vocabularySet(setId, setVersion)?.bindings?.get(fieldPath)

    companion object {
        fun create(sets: Iterable<VocabularySet>): VocabularySetRegistry {
            val list = sets.toList()
            require(list.map { ContractKey(it.vocabularySetId, it.version) }.distinct().size == list.size) { "Vocabulary Set ID/version pairs must be unique." }
            list.forEach { require(it.bindings.isNotEmpty()) { "Vocabulary Set ${it.vocabularySetId} cannot have empty bindings." } }
            return VocabularySetRegistry(list.associateBy { ContractKey(it.vocabularySetId, it.version) })
        }
    }
}

private data class ContractKey(val id: String, val version: String)

@Serializable
data class ProductionPreset(
    val presetId: String,
    val version: String,
    val label: String,
    val description: String? = null,
    val assetType: AssetType,
    val vocabularySetId: String,
    val vocabularySetVersion: String,
    val selections: PresetSelections,
)

@Serializable data class PresetSelections(val classification: ClassificationSelections? = null, val subject: SubjectSelections? = null, val details: NpcPortraitDetailSelections? = null, val visual: VisualSelections? = null, val provenance: ProvenanceSelections? = null)
@Serializable data class ClassificationSelections(val realmId: PresetValue? = null, val cultureId: PresetValue? = null)
@Serializable data class SubjectSelections(val speciesId: PresetValue? = null, val genderId: PresetValue? = null, val ageBandId: PresetValue? = null)
@Serializable data class NpcPortraitDetailSelections(val professionId: PresetValue? = null, val socialClassId: PresetValue? = null)
@Serializable data class VisualSelections(val visualProfileId: PresetValue? = null, val visualProfileVersion: PresetVersionValue? = null, val expressionId: PresetValue? = null)
@Serializable data class ProvenanceSelections(val promptTemplateId: PresetValue? = null, val promptTemplateVersion: PresetVersionValue? = null)
@Serializable data class PresetValue(val mode: PresetValueMode, val value: String)
@Serializable data class PresetVersionValue(val mode: PresetValueMode, val value: String)
@Serializable enum class PresetValueMode { @kotlinx.serialization.SerialName("fixed") FIXED, @kotlinx.serialization.SerialName("suggested") SUGGESTED }

object ProductionFieldPaths {
    const val CLASSIFICATION_REALM_ID = "classification.realmId"
    const val CLASSIFICATION_CULTURE_ID = "classification.cultureId"
    const val SUBJECT_SPECIES_ID = "subject.speciesId"
    const val SUBJECT_GENDER_ID = "subject.genderId"
    const val SUBJECT_AGE_BAND_ID = "subject.ageBandId"
    const val DETAILS_PROFESSION_ID = "details.professionId"
    const val DETAILS_SOCIAL_CLASS_ID = "details.socialClassId"
    const val VISUAL_PROFILE_ID = "visual.visualProfileId"
    const val VISUAL_PROFILE_VERSION = "visual.visualProfileVersion"
    const val VISUAL_EXPRESSION_ID = "visual.expressionId"
    const val PROVENANCE_PROMPT_TEMPLATE_ID = "provenance.promptTemplateId"
    const val PROVENANCE_PROMPT_TEMPLATE_VERSION = "provenance.promptTemplateVersion"

    val vocabularySelections = setOf(
        CLASSIFICATION_REALM_ID,
        CLASSIFICATION_CULTURE_ID,
        SUBJECT_SPECIES_ID,
        SUBJECT_GENDER_ID,
        SUBJECT_AGE_BAND_ID,
        DETAILS_PROFESSION_ID,
        DETAILS_SOCIAL_CLASS_ID,
        VISUAL_EXPRESSION_ID,
    )

    val externalReferences = setOf(
        VISUAL_PROFILE_ID,
        VISUAL_PROFILE_VERSION,
        PROVENANCE_PROMPT_TEMPLATE_ID,
        PROVENANCE_PROMPT_TEMPLATE_VERSION,
    )

    val supportedSelections = vocabularySelections + externalReferences
}

internal data class PresetSelectionEntry(val mode: PresetValueMode, val value: String)

internal fun PresetSelections.flatten(): Map<String, PresetSelectionEntry> = buildMap {
    classification?.realmId?.let { put(ProductionFieldPaths.CLASSIFICATION_REALM_ID, PresetSelectionEntry(it.mode, it.value)) }
    classification?.cultureId?.let { put(ProductionFieldPaths.CLASSIFICATION_CULTURE_ID, PresetSelectionEntry(it.mode, it.value)) }
    subject?.speciesId?.let { put(ProductionFieldPaths.SUBJECT_SPECIES_ID, PresetSelectionEntry(it.mode, it.value)) }
    subject?.genderId?.let { put(ProductionFieldPaths.SUBJECT_GENDER_ID, PresetSelectionEntry(it.mode, it.value)) }
    subject?.ageBandId?.let { put(ProductionFieldPaths.SUBJECT_AGE_BAND_ID, PresetSelectionEntry(it.mode, it.value)) }
    details?.professionId?.let { put(ProductionFieldPaths.DETAILS_PROFESSION_ID, PresetSelectionEntry(it.mode, it.value)) }
    details?.socialClassId?.let { put(ProductionFieldPaths.DETAILS_SOCIAL_CLASS_ID, PresetSelectionEntry(it.mode, it.value)) }
    visual?.visualProfileId?.let { put(ProductionFieldPaths.VISUAL_PROFILE_ID, PresetSelectionEntry(it.mode, it.value)) }
    visual?.visualProfileVersion?.let { put(ProductionFieldPaths.VISUAL_PROFILE_VERSION, PresetSelectionEntry(it.mode, it.value)) }
    visual?.expressionId?.let { put(ProductionFieldPaths.VISUAL_EXPRESSION_ID, PresetSelectionEntry(it.mode, it.value)) }
    provenance?.promptTemplateId?.let { put(ProductionFieldPaths.PROVENANCE_PROMPT_TEMPLATE_ID, PresetSelectionEntry(it.mode, it.value)) }
    provenance?.promptTemplateVersion?.let { put(ProductionFieldPaths.PROVENANCE_PROMPT_TEMPLATE_VERSION, PresetSelectionEntry(it.mode, it.value)) }
}

class PresetRegistry private constructor(private val entries: Map<ContractKey, ProductionPreset>) {
    fun preset(id: String, version: String): ProductionPreset? = entries[ContractKey(id, version)]
    companion object {
        fun create(presets: Iterable<ProductionPreset>): PresetRegistry {
            val list = presets.toList()
            require(list.map { ContractKey(it.presetId, it.version) }.distinct().size == list.size) { "Preset ID/version pairs must be unique." }
            return PresetRegistry(list.associateBy { ContractKey(it.presetId, it.version) })
        }
    }
}

object ProductionContractValidator {
    fun validateSet(set: VocabularySet, vocabularies: VocabularyRegistry): List<String> = buildList {
        set.bindings.forEach { (path, reference) ->
            if (vocabularies.vocabulary(reference.vocabularyId, reference.version) == null) add("Binding $path references missing vocabulary ${reference.vocabularyId} ${reference.version}")
        }
    }

    fun validatePreset(preset: ProductionPreset, sets: VocabularySetRegistry, vocabularies: VocabularyRegistry): List<String> = buildList {
        if (preset.assetType != AssetType.NPC_PORTRAIT) add("Preset v1 currently supports npc_portrait only.")
        validateNonEmptyBlocks(preset.selections, this)
        validatePairedFields(preset.selections, this)
        val set = sets.vocabularySet(preset.vocabularySetId, preset.vocabularySetVersion)
        if (set == null) {
            add("Missing Vocabulary Set ${preset.vocabularySetId} ${preset.vocabularySetVersion}")
            return@buildList
        }
        addAll(validateSet(set, vocabularies))
        preset.selections.flatten().filterKeys { it in ProductionFieldPaths.vocabularySelections }.forEach { (path, selected) ->
            val binding = set.bindings[path]
            if (binding == null) add("Selected field $path has no binding in the Vocabulary Set")
            else if (vocabularies.value(binding.vocabularyId, binding.version, selected.value) == null) add("Unknown value ${selected.value} for $path in ${binding.vocabularyId} ${binding.version}")
        }
    }

    private fun validateNonEmptyBlocks(value: PresetSelections, errors: MutableList<String>) {
        if (value.classification == ClassificationSelections()) errors += "classification selections cannot be empty"
        if (value.subject == SubjectSelections()) errors += "subject selections cannot be empty"
        if (value.details == NpcPortraitDetailSelections()) errors += "details selections cannot be empty"
        if (value.visual == VisualSelections()) errors += "visual selections cannot be empty"
        if (value.provenance == ProvenanceSelections()) errors += "provenance selections cannot be empty"
    }

    private fun validatePairedFields(value: PresetSelections, errors: MutableList<String>) {
        value.visual?.let { if ((it.visualProfileId == null) != (it.visualProfileVersion == null)) errors += "visual profile ID and version must be supplied together" }
        value.provenance?.let { if ((it.promptTemplateId == null) != (it.promptTemplateVersion == null)) errors += "prompt template ID and version must be supplied together" }
    }
}

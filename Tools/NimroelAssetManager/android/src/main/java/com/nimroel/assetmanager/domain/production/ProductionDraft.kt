package com.nimroel.assetmanager.domain.production

import com.nimroel.assetmanager.domain.contracts.PresetRegistry
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.ProductionContractValidator
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularyValue
import com.nimroel.assetmanager.domain.contracts.flatten
import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.AssetValidator
import com.nimroel.assetmanager.domain.model.Classification
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.Lifecycle
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.NpcPortraitDetails
import com.nimroel.assetmanager.domain.model.Provenance
import com.nimroel.assetmanager.domain.model.Subject
import com.nimroel.assetmanager.domain.model.Visual

enum class DraftSelectionSource { PRESET, OPERATOR }

data class DraftSelection(
    val value: String,
    val source: DraftSelectionSource,
    val presetMode: PresetValueMode? = null,
) {
    val isLocked: Boolean get() = presetMode == PresetValueMode.FIXED
    val isSuggested: Boolean get() = presetMode == PresetValueMode.SUGGESTED
}

class ProductionDraft internal constructor(
    val presetId: String,
    val presetVersion: String,
    val assetType: AssetType,
    val vocabularySetId: String,
    val vocabularySetVersion: String,
    selections: Map<String, DraftSelection>,
) {
    val selections: Map<String, DraftSelection> = selections.toMap()
}

class ProductionDraftException(message: String) : IllegalArgumentException(message)

class ProductionDraftService(
    private val presets: PresetRegistry,
    private val vocabularySets: VocabularySetRegistry,
    private val vocabularies: VocabularyRegistry,
) {
    fun startDraft(presetId: String, presetVersion: String): ProductionDraft {
        val preset = presets.preset(presetId, presetVersion)
            ?: throw ProductionDraftException("Missing Production Preset $presetId $presetVersion")
        val errors = ProductionContractValidator.validatePreset(preset, vocabularySets, vocabularies)
        if (errors.isNotEmpty()) throw ProductionDraftException("Invalid Production Preset $presetId $presetVersion: ${errors.joinToString("; ")}")
        vocabularySet(preset.vocabularySetId, preset.vocabularySetVersion)

        val draft = ProductionDraft(
            presetId = preset.presetId,
            presetVersion = preset.version,
            assetType = preset.assetType,
            vocabularySetId = preset.vocabularySetId,
            vocabularySetVersion = preset.vocabularySetVersion,
            selections = preset.selections.flatten().mapValues { (_, selected) ->
                DraftSelection(selected.value, DraftSelectionSource.PRESET, selected.mode)
            },
        )
        draft.selections.forEach { (fieldPath, selection) -> validateSelectionValue(draft, fieldPath, selection.value) }
        return draft
    }

    fun setSelection(draft: ProductionDraft, fieldPath: String, valueId: String): ProductionDraft {
        validateSelectionValue(draft, fieldPath, valueId)
        val current = draft.selections[fieldPath]
        if (current?.isLocked == true && current.value != valueId) {
            throw ProductionDraftException("Selection $fieldPath is fixed by preset ${draft.presetId} ${draft.presetVersion}")
        }
        if (current?.value == valueId) return draft
        return draft.withSelections(
            draft.selections + (fieldPath to DraftSelection(valueId, DraftSelectionSource.OPERATOR, current?.presetMode)),
        )
    }

    fun clearSelection(draft: ProductionDraft, fieldPath: String): ProductionDraft {
        validateFieldPath(draft, fieldPath)
        val current = draft.selections[fieldPath] ?: return draft
        if (current.isLocked) {
            throw ProductionDraftException("Selection $fieldPath is fixed by preset ${draft.presetId} ${draft.presetVersion}")
        }
        return draft.withSelections(draft.selections - fieldPath)
    }

    fun availableValues(draft: ProductionDraft, fieldPath: String): List<VocabularyValue> {
        validateFieldPath(draft, fieldPath)
        val reference = binding(draft, fieldPath)
        return vocabularies.vocabulary(reference.vocabularyId, reference.version)?.values
            ?: throw ProductionDraftException("Missing Vocabulary ${reference.vocabularyId} ${reference.version} for $fieldPath")
    }

    /** Vocabulary-backed v1 fields that the draft's exact Vocabulary Set actually exposes. */
    fun boundVocabularyFieldPaths(draft: ProductionDraft): Set<String> =
        vocabularySet(draft.vocabularySetId, draft.vocabularySetVersion)
            .bindings
            .keys
            .filterTo(linkedSetOf()) { it in ProductionFieldPaths.vocabularySelections }

    fun buildAsset(draft: ProductionDraft, assetId: AssetId, content: Content, provenance: Provenance): Asset {
        if (draft.assetType != AssetType.NPC_PORTRAIT) {
            throw ProductionDraftException("Production Draft v1 can only materialize npc_portrait")
        }
        val value: (String) -> String? = { draft.selections[it]?.value }
        val professionId = value(ProductionFieldPaths.DETAILS_PROFESSION_ID)
        val socialClassId = value(ProductionFieldPaths.DETAILS_SOCIAL_CLASS_ID)
        val subject = Subject(
            speciesId = value(ProductionFieldPaths.SUBJECT_SPECIES_ID),
            genderId = value(ProductionFieldPaths.SUBJECT_GENDER_ID),
            ageBandId = value(ProductionFieldPaths.SUBJECT_AGE_BAND_ID),
        ).takeUnless { it == Subject() }
        val visual = Visual(
            visualProfileId = value(ProductionFieldPaths.VISUAL_PROFILE_ID),
            visualProfileVersion = value(ProductionFieldPaths.VISUAL_PROFILE_VERSION),
            expressionId = value(ProductionFieldPaths.VISUAL_EXPRESSION_ID),
        ).takeUnless { it == Visual() }
        val promptTemplateId = value(ProductionFieldPaths.PROVENANCE_PROMPT_TEMPLATE_ID)
        val promptTemplateVersion = value(ProductionFieldPaths.PROVENANCE_PROMPT_TEMPLATE_VERSION)
        if ((promptTemplateId == null) != (promptTemplateVersion == null)) {
            throw ProductionDraftException("Production Draft prompt template ID and version must be supplied together")
        }
        val materializedProvenance = if (promptTemplateId != null) {
            provenance.copy(promptTemplateId = promptTemplateId, promptTemplateVersion = promptTemplateVersion)
        } else {
            provenance
        }
        val asset = Asset(
            schemaVersion = 1,
            assetId = assetId,
            type = draft.assetType,
            lifecycle = Lifecycle(LifecycleStatus.DRAFT),
            classification = Classification(
                vocabularyId = draft.vocabularySetId,
                vocabularyVersion = draft.vocabularySetVersion,
                realmId = value(ProductionFieldPaths.CLASSIFICATION_REALM_ID),
                cultureId = value(ProductionFieldPaths.CLASSIFICATION_CULTURE_ID),
            ),
            subject = subject,
            details = if (professionId != null || socialClassId != null) NpcPortraitDetails(professionId, socialClassId) else null,
            visual = visual,
            content = content,
            provenance = materializedProvenance,
        )
        val errors = AssetValidator.validate(asset)
        if (errors.isNotEmpty()) throw ProductionDraftException("Production Draft cannot build a valid Asset: ${errors.joinToString("; ")}")
        return asset
    }

    private fun validateSelectionValue(draft: ProductionDraft, fieldPath: String, value: String) {
        validateFieldPath(draft, fieldPath)
        if (fieldPath in ProductionFieldPaths.externalReferences) {
            val valid = if (fieldPath.endsWith("Version")) VERSION.matches(value) else REFERENCE_ID.matches(value)
            if (!valid) throw ProductionDraftException("Invalid value $value for $fieldPath")
            return
        }
        val reference = binding(draft, fieldPath)
        if (vocabularies.value(reference.vocabularyId, reference.version, value) == null) {
            throw ProductionDraftException("Unknown value $value for $fieldPath in ${reference.vocabularyId} ${reference.version}")
        }
    }

    private fun validateFieldPath(draft: ProductionDraft, fieldPath: String) {
        if (fieldPath !in ProductionFieldPaths.supportedSelections) {
            throw ProductionDraftException("Field $fieldPath is not supported by Production Draft v1")
        }
        if (fieldPath !in ProductionFieldPaths.externalReferences) binding(draft, fieldPath)
    }

    private fun binding(draft: ProductionDraft, fieldPath: String) =
        vocabularySet(draft.vocabularySetId, draft.vocabularySetVersion).bindings[fieldPath]
            ?: throw ProductionDraftException("Field $fieldPath has no binding in Vocabulary Set ${draft.vocabularySetId} ${draft.vocabularySetVersion}")

    private fun vocabularySet(id: String, version: String): VocabularySet =
        vocabularySets.vocabularySet(id, version)
            ?: throw ProductionDraftException("Missing Vocabulary Set $id $version")

    private fun ProductionDraft.withSelections(updated: Map<String, DraftSelection>) = ProductionDraft(
        presetId,
        presetVersion,
        assetType,
        vocabularySetId,
        vocabularySetVersion,
        updated,
    )

    private companion object {
        val REFERENCE_ID = Regex("^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
        val VERSION = Regex("^[0-9]+\\.[0-9]+(?:\\.[0-9]+)?(?:[-+][0-9A-Za-z.-]+)?$")
    }
}

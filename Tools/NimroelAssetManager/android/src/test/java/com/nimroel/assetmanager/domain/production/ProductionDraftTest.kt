package com.nimroel.assetmanager.domain.production

import com.nimroel.assetmanager.domain.contracts.ClassificationSelections
import com.nimroel.assetmanager.domain.contracts.ContractJson
import com.nimroel.assetmanager.domain.contracts.NpcPortraitDetailSelections
import com.nimroel.assetmanager.domain.contracts.PresetRegistry
import com.nimroel.assetmanager.domain.contracts.PresetSelections
import com.nimroel.assetmanager.domain.contracts.PresetValue
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.contracts.PresetVersionValue
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.domain.contracts.ProductionPreset
import com.nimroel.assetmanager.domain.contracts.ProvenanceSelections
import com.nimroel.assetmanager.domain.contracts.SubjectSelections
import com.nimroel.assetmanager.domain.contracts.VisualSelections
import com.nimroel.assetmanager.domain.contracts.Vocabulary
import com.nimroel.assetmanager.domain.contracts.VocabularyReference
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularyValue
import com.nimroel.assetmanager.domain.contracts.VocabularyValueStatus
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetValidator
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.Generator
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.NpcPortraitDetails
import com.nimroel.assetmanager.domain.model.OriginKind
import com.nimroel.assetmanager.domain.model.Provenance
import kotlinx.serialization.decodeFromString
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertThrows
import org.junit.Assert.assertTrue
import org.junit.Test

class ProductionDraftTest {
    @Test
    fun `startDraft loads real pilot and resolves its exact set and vocabularies`() {
        val service = pilotService()

        val draft = service.startDraft("npc-portrait-pilot", "1.0")

        assertEquals("npc-portrait-pilot", draft.presetId)
        assertEquals("1.0", draft.presetVersion)
        assertEquals("nimroel-npc-pilot", draft.vocabularySetId)
        assertEquals("1.0", draft.vocabularySetVersion)
        assertEquals("adult", draft.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]?.value)
        assertEquals(PresetValueMode.SUGGESTED, draft.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]?.presetMode)
        assertEquals("Adult", service.availableValues(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID).single().label)
        assertEquals("Neutral", service.availableValues(draft, ProductionFieldPaths.VISUAL_EXPRESSION_ID).single().label)
    }

    @Test
    fun `startDraft reports missing preset set and vocabulary clearly`() {
        val validPreset = pilotPreset()
        val missingPreset = service(emptyList(), listOf(pilotSet()), pilotVocabularies())
        assertTrue(assertThrows(ProductionDraftException::class.java) { missingPreset.startDraft("missing", "1.0") }.message!!.contains("Missing Production Preset"))

        val missingSet = service(listOf(validPreset), emptyList(), pilotVocabularies())
        assertTrue(assertThrows(ProductionDraftException::class.java) { missingSet.startDraft(validPreset.presetId, validPreset.version) }.message!!.contains("Missing Vocabulary Set"))

        val missingVocabulary = service(listOf(validPreset), listOf(pilotSet()), emptyList())
        assertTrue(assertThrows(ProductionDraftException::class.java) { missingVocabulary.startDraft(validPreset.presetId, validPreset.version) }.message!!.contains("missing vocabulary"))
    }

    @Test
    fun `suggested selection is preloaded editable and removable`() {
        val service = completeService()
        val initial = service.startDraft("test-preset", "1.0")

        val changed = service.setSelection(initial, ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")
        assertEquals("adult", initial.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]?.value)
        assertEquals("elder", changed.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]?.value)
        assertEquals(DraftSelectionSource.OPERATOR, changed.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]?.source)
        assertTrue(changed.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]!!.isSuggested)

        val cleared = service.clearSelection(changed, ProductionFieldPaths.SUBJECT_AGE_BAND_ID)
        assertFalse(cleared.selections.containsKey(ProductionFieldPaths.SUBJECT_AGE_BAND_ID))
    }

    @Test
    fun `fixed selection cannot be changed or removed`() {
        val fixedPreset = completePreset().copy(
            selections = completePreset().selections.copy(
                subject = completePreset().selections.subject?.copy(
                    ageBandId = PresetValue(PresetValueMode.FIXED, "adult"),
                ),
            ),
        )
        val service = completeService(fixedPreset)
        val draft = service.startDraft(fixedPreset.presetId, fixedPreset.version)

        assertTrue(draft.selections[ProductionFieldPaths.SUBJECT_AGE_BAND_ID]!!.isLocked)
        assertThrows(ProductionDraftException::class.java) {
            service.setSelection(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "elder")
        }
        assertThrows(ProductionDraftException::class.java) {
            service.clearSelection(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID)
        }
    }

    @Test
    fun `editing rejects unknown values and fields without a binding`() {
        val service = pilotService()
        val draft = service.startDraft("npc-portrait-pilot", "1.0")

        assertThrows(ProductionDraftException::class.java) {
            service.setSelection(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID, "invented")
        }
        assertThrows(ProductionDraftException::class.java) {
            service.setSelection(draft, ProductionFieldPaths.SUBJECT_SPECIES_ID, "human")
        }
        assertThrows(ProductionDraftException::class.java) {
            service.clearSelection(draft, ProductionFieldPaths.SUBJECT_SPECIES_ID)
        }
    }

    @Test
    fun `supported routes reject an unsupported Vocabulary Set binding`() {
        val weatherPath = "visual.weatherId"
        val set = completeSet().copy(
            bindings = completeSet().bindings + (weatherPath to VocabularyReference("weather-catalog", "5.0")),
        )
        val service = service(
            listOf(completePreset()),
            listOf(set),
            completeVocabularies() + Vocabulary("weather-catalog", "5.0", listOf(VocabularyValue("sunny", "Sunny"))),
        )
        val draft = service.startDraft("test-preset", "1.0")

        assertEquals("Adult", service.availableValues(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID).first().label)
        assertThrows(ProductionDraftException::class.java) { service.setSelection(draft, weatherPath, "sunny") }
        assertThrows(ProductionDraftException::class.java) { service.clearSelection(draft, weatherPath) }
        assertThrows(ProductionDraftException::class.java) { service.availableValues(draft, weatherPath) }
    }

    @Test
    fun `availableValues preserves the linked vocabulary values metadata and order`() {
        val service = completeService()
        val draft = service.startDraft("test-preset", "1.0")

        val values = service.availableValues(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID)

        assertEquals(listOf("adult", "elder"), values.map(VocabularyValue::id))
        assertEquals("Adult", values[0].label)
        assertEquals("Initial adult band", values[0].description)
        assertEquals(VocabularyValueStatus.DEPRECATED, values[1].status)
        assertEquals(20, values[1].presentationOrder)
    }

    @Test
    fun `Vocabulary Set can point to alternative vocabulary IDs without code changes`() {
        val alternativeVocabulary = Vocabulary("alternative-age-source", "9.4", listOf(VocabularyValue("adult", "Alternative adult")))
        val alternativeSet = VocabularySet(
            "alternative-set",
            "2.0",
            mapOf(ProductionFieldPaths.SUBJECT_AGE_BAND_ID to VocabularyReference("alternative-age-source", "9.4")),
        )
        val alternativePreset = completePreset().copy(
            presetId = "alternative-preset",
            vocabularySetId = alternativeSet.vocabularySetId,
            vocabularySetVersion = alternativeSet.version,
            selections = PresetSelections(subject = SubjectSelections(ageBandId = suggested("adult"))),
        )
        val service = service(listOf(alternativePreset), listOf(alternativeSet), listOf(alternativeVocabulary))

        val draft = service.startDraft(alternativePreset.presetId, alternativePreset.version)

        assertEquals("Alternative adult", service.availableValues(draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID).single().label)
    }

    @Test
    fun `buildAsset materializes all NPC selections and preserves canonical inputs and provenance`() {
        val service = completeService()
        val draft = service.startDraft("test-preset", "1.0")
        val assetId = assetId()
        val content = content()
        val sourceAssetId = AssetId.parse("ast_019c1a23-4567-7abc-8def-1123456789ab")
        val provenance = Provenance(
            originKind = OriginKind.DERIVED,
            generator = Generator("openai", "image-model", "2026-09-13T12:00:00Z"),
            sourceAssetIds = listOf(sourceAssetId),
            promptRecordId = "prompt-record-7",
            importedAt = "2026-09-13T12:01:00Z",
        )

        val asset = service.buildAsset(draft, assetId, content, provenance)

        assertEquals(1, asset.schemaVersion)
        assertEquals(assetId, asset.assetId)
        assertEquals(LifecycleStatus.DRAFT, asset.lifecycle.status)
        assertEquals("test-set", asset.classification?.vocabularyId)
        assertEquals("3.2", asset.classification?.vocabularyVersion)
        assertEquals("valemar", asset.classification?.realmId)
        assertEquals("human", asset.subject?.speciesId)
        assertEquals("female", asset.subject?.genderId)
        assertEquals("adult", asset.subject?.ageBandId)
        assertEquals(NpcPortraitDetails("farmer", "commoner"), asset.details)
        assertEquals("neutral", asset.visual?.expressionId)
        assertEquals("valemar-portrait", asset.visual?.visualProfileId)
        assertEquals("2.1", asset.visual?.visualProfileVersion)
        assertSame(content, asset.content)
        assertEquals("npc-portrait-template", asset.provenance.promptTemplateId)
        assertEquals("4.0", asset.provenance.promptTemplateVersion)
        assertEquals(provenance.generator, asset.provenance.generator)
        assertEquals(provenance.sourceAssetIds, asset.provenance.sourceAssetIds)
        assertEquals(provenance.promptRecordId, asset.provenance.promptRecordId)
        assertEquals(provenance.importedAt, asset.provenance.importedAt)
        assertTrue(AssetValidator.validate(asset).isEmpty())
    }

    @Test
    fun `NpcPortraitDetails is omitted when profession and social class are absent`() {
        val service = pilotService()
        val draft = service.startDraft("npc-portrait-pilot", "1.0")

        val asset = service.buildAsset(draft, assetId(), content(), Provenance(OriginKind.IMPORTED, importedAt = "2026-09-13T12:00:00Z"))

        assertNull(asset.details)
        assertTrue(AssetValidator.validate(asset).isEmpty())
    }

    @Test
    fun `buildAsset rejects a draft that leaves a canonical reference pair incomplete`() {
        val service = completeService()
        val draft = service.clearSelection(
            service.startDraft("test-preset", "1.0"),
            ProductionFieldPaths.PROVENANCE_PROMPT_TEMPLATE_VERSION,
        )

        val error = assertThrows(ProductionDraftException::class.java) {
            service.buildAsset(draft, assetId(), content(), Provenance(OriginKind.IMPORTED))
        }

        assertTrue(error.message!!.contains("prompt template ID and version"))
    }

    private fun pilotService() = service(listOf(pilotPreset()), listOf(pilotSet()), pilotVocabularies())

    private fun completeService(preset: ProductionPreset = completePreset()) =
        service(listOf(preset), listOf(completeSet()), completeVocabularies())

    private fun service(
        presets: List<ProductionPreset>,
        sets: List<VocabularySet>,
        vocabularies: List<Vocabulary>,
    ) = ProductionDraftService(
        PresetRegistry.create(presets),
        VocabularySetRegistry.create(sets),
        VocabularyRegistry.create(vocabularies),
    )

    private fun completePreset() = ProductionPreset(
        presetId = "test-preset",
        version = "1.0",
        label = "Test preset",
        assetType = com.nimroel.assetmanager.domain.model.AssetType.NPC_PORTRAIT,
        vocabularySetId = "test-set",
        vocabularySetVersion = "3.2",
        selections = PresetSelections(
            classification = ClassificationSelections(realmId = suggested("valemar"), cultureId = suggested("valemar-culture")),
            subject = SubjectSelections(speciesId = suggested("human"), genderId = suggested("female"), ageBandId = suggested("adult")),
            details = NpcPortraitDetailSelections(professionId = suggested("farmer"), socialClassId = suggested("commoner")),
            visual = VisualSelections(
                visualProfileId = suggested("valemar-portrait"),
                visualProfileVersion = suggestedVersion("2.1"),
                expressionId = suggested("neutral"),
            ),
            provenance = ProvenanceSelections(
                promptTemplateId = suggested("npc-portrait-template"),
                promptTemplateVersion = suggestedVersion("4.0"),
            ),
        ),
    )

    private fun completeSet() = VocabularySet(
        "test-set",
        "3.2",
        mapOf(
            ProductionFieldPaths.CLASSIFICATION_REALM_ID to VocabularyReference("realms-custom", "5.0"),
            ProductionFieldPaths.CLASSIFICATION_CULTURE_ID to VocabularyReference("cultures-custom", "5.0"),
            ProductionFieldPaths.SUBJECT_SPECIES_ID to VocabularyReference("species-custom", "5.0"),
            ProductionFieldPaths.SUBJECT_GENDER_ID to VocabularyReference("genders-custom", "5.0"),
            ProductionFieldPaths.SUBJECT_AGE_BAND_ID to VocabularyReference("ages-custom", "5.0"),
            ProductionFieldPaths.DETAILS_PROFESSION_ID to VocabularyReference("professions-custom", "5.0"),
            ProductionFieldPaths.DETAILS_SOCIAL_CLASS_ID to VocabularyReference("classes-custom", "5.0"),
            ProductionFieldPaths.VISUAL_EXPRESSION_ID to VocabularyReference("expressions-custom", "5.0"),
        ),
    )

    private fun completeVocabularies() = listOf(
        vocabulary("realms-custom", "valemar"),
        vocabulary("cultures-custom", "valemar-culture"),
        vocabulary("species-custom", "human"),
        vocabulary("genders-custom", "female"),
        Vocabulary(
            "ages-custom",
            "5.0",
            listOf(
                VocabularyValue("adult", "Adult", "Initial adult band", VocabularyValueStatus.ACTIVE, 10),
                VocabularyValue("elder", "Elder", "Deprecated test band", VocabularyValueStatus.DEPRECATED, 20),
            ),
        ),
        vocabulary("professions-custom", "farmer"),
        vocabulary("classes-custom", "commoner"),
        vocabulary("expressions-custom", "neutral"),
    )

    private fun vocabulary(id: String, value: String) = Vocabulary(id, "5.0", listOf(VocabularyValue(value, value)))
    private fun suggested(value: String) = PresetValue(PresetValueMode.SUGGESTED, value)
    private fun suggestedVersion(value: String) = PresetVersionValue(PresetValueMode.SUGGESTED, value)
    private fun assetId() = AssetId.parse("ast_019c1a23-4567-7abc-8def-0123456789ab")
    private fun content() = Content("image/webp", 1024, 1024, 4096, "a".repeat(64), "srgb")
    private fun pilotPreset(): ProductionPreset = ContractJson.codec.decodeFromString(resource("presets/examples/npc-portrait-pilot.example.json"))
    private fun pilotSet(): VocabularySet = ContractJson.codec.decodeFromString(resource("vocabulary-sets/data/nimroel-npc-pilot-1.0.json"))
    private fun pilotVocabularies() = listOf(
        vocabularyResource("vocabularies/data/nimroel-age-bands-1.0.json"),
        vocabularyResource("vocabularies/data/nimroel-expressions-1.0.json"),
    )
    private fun vocabularyResource(path: String): Vocabulary = ContractJson.codec.decodeFromString(resource(path))
    private fun resource(path: String): String = checkNotNull(javaClass.classLoader?.getResource(path)) { "Missing contract resource $path" }.readText()
}

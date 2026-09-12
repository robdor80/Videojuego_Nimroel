package com.nimroel.assetmanager.domain.contracts

import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ProductionContractsTest {
    @Test fun `loads a versioned vocabulary and looks up its value`() {
        val registry = registry()
        assertEquals("Adult", registry.value("nimroel-age-bands", "1.0", "adult")?.label)
        assertEquals(null, registry.value("nimroel-age-bands", "2.0", "adult"))
    }

    @Test(expected = IllegalArgumentException::class)
    fun `rejects duplicate vocabulary value IDs`() {
        VocabularyRegistry.create(listOf(vocabulary("test-fixtures/invalid/duplicate-value-id.json")))
    }

    @Test fun `loads a Vocabulary Set and resolves a field binding`() {
        val sets = setRegistry()
        assertEquals(VocabularyReference("nimroel-age-bands", "1.0"), sets.binding("nimroel-npc-pilot", "1.0", "subject.ageBandId"))
    }

    @Test fun `rejects binding to missing vocabulary or version`() {
        val valid = vocabularySet()
        val missingVocabulary = valid.copy(bindings = mapOf("subject.ageBandId" to VocabularyReference("missing", "1.0")))
        val missingVersion = valid.copy(bindings = mapOf("subject.ageBandId" to VocabularyReference("nimroel-age-bands", "2.0")))
        assertTrue(ProductionContractValidator.validateSet(missingVocabulary, registry()).isNotEmpty())
        assertTrue(ProductionContractValidator.validateSet(missingVersion, registry()).isNotEmpty())
    }

    @Test fun `loads and resolves the preset through its Vocabulary Set`() {
        val value = preset()
        assertTrue(ProductionContractValidator.validatePreset(value, setRegistry(), registry()).isEmpty())
        assertNotNull(PresetRegistry.create(listOf(value)).preset("npc-portrait-pilot", "1.0"))
    }

    @Test fun `rejects selected field without binding`() {
        val source = preset()
        val invalid = source.copy(selections = source.selections.copy(subject = source.selections.subject?.copy(speciesId = PresetValue(PresetValueMode.FIXED, "human"))))
        assertTrue(ProductionContractValidator.validatePreset(invalid, setRegistry(), registry()).any { it.contains("has no binding") })
    }

    @Test fun `rejects unknown selected value`() {
        val source = preset()
        val invalid = source.copy(selections = source.selections.copy(subject = SubjectSelections(ageBandId = PresetValue(PresetValueMode.FIXED, "invented"))))
        assertTrue(ProductionContractValidator.validatePreset(invalid, setRegistry(), registry()).any { it.contains("Unknown value") })
    }

    @Test fun `rejects empty blocks and incomplete external reference pairs in domain`() {
        val source = preset()
        val invalid = source.copy(selections = source.selections.copy(
            classification = ClassificationSelections(),
            visual = VisualSelections(visualProfileId = PresetValue(PresetValueMode.FIXED, "profile")),
            provenance = ProvenanceSelections(promptTemplateVersion = PresetVersionValue(PresetValueMode.FIXED, "1.0")),
        ))
        val errors = ProductionContractValidator.validatePreset(invalid, setRegistry(), registry())
        assertTrue(errors.any { it.contains("classification selections cannot be empty") })
        assertTrue(errors.any { it.contains("visual profile ID and version") })
        assertTrue(errors.any { it.contains("prompt template ID and version") })
    }

    @Test fun `contract JSON round trips`() {
        val vocabulary = vocabulary("data/nimroel-age-bands-1.0.json")
        assertEquals(vocabulary, ContractJson.codec.decodeFromString<Vocabulary>(ContractJson.codec.encodeToString(vocabulary)))
        val set = vocabularySet()
        assertEquals(set, ContractJson.codec.decodeFromString<VocabularySet>(ContractJson.codec.encodeToString(set)))
        val preset = preset()
        assertEquals(preset, ContractJson.codec.decodeFromString<ProductionPreset>(ContractJson.codec.encodeToString(preset)))
    }

    @Test fun `validator follows bindings rather than hardcoded vocabulary IDs`() {
        val customVocabulary = Vocabulary("custom-ages", "7.2", listOf(VocabularyValue("adult", "Adult")))
        val customSet = VocabularySet("custom-set", "3.0", mapOf("subject.ageBandId" to VocabularyReference("custom-ages", "7.2")))
        val customPreset = preset().copy(vocabularySetId = "custom-set", vocabularySetVersion = "3.0", selections = PresetSelections(subject = SubjectSelections(ageBandId = PresetValue(PresetValueMode.FIXED, "adult"))))
        assertTrue(ProductionContractValidator.validatePreset(customPreset, VocabularySetRegistry.create(listOf(customSet)), VocabularyRegistry.create(listOf(customVocabulary))).isEmpty())
    }

    private fun registry() = VocabularyRegistry.create(listOf(vocabulary("data/nimroel-age-bands-1.0.json"), vocabulary("data/nimroel-expressions-1.0.json")))
    private fun setRegistry() = VocabularySetRegistry.create(listOf(vocabularySet()))
    private fun vocabularySet(): VocabularySet = ContractJson.codec.decodeFromString(resource("vocabulary-sets/data/nimroel-npc-pilot-1.0.json"))
    private fun preset(): ProductionPreset = ContractJson.codec.decodeFromString(resource("presets/examples/npc-portrait-pilot.example.json"))
    private fun vocabulary(path: String): Vocabulary = ContractJson.codec.decodeFromString(resource("vocabularies/$path"))
    private fun resource(path: String): String = checkNotNull(javaClass.classLoader?.getResource(path)) { "Missing contract resource $path" }.readText()
}

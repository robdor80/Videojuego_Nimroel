package com.nimroel.assetmanager.domain.model

import kotlinx.serialization.SerializationException
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonPrimitive
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.put
import java.nio.file.Files
import java.nio.file.Path
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class AssetSchemaV1Test {
    private val json = AssetJson.codec
    private val validFixtures = listOf(
        "examples/npc-portrait-valemar-farmer.json",
        "examples/npc-portrait-norgard-soldier.json",
        "examples/npc-portrait-canonical-character.json",
        "examples/landscape-valemar-forest.json",
        "examples/interior-humble-tavern.json",
    )

    @Test fun `canonical fixtures deserialize to expected typed details`() {
        val assets = validFixtures.map(::assetResource)
        assertTrue(assets.all { AssetValidator.validate(it).isEmpty() })
        assertTrue(assets[0].details is NpcPortraitDetails)
        assertTrue(assets[1].details is NpcPortraitDetails)
        assertEquals(null, assets[2].details)
        assertTrue(assets[3].details is LandscapeDetails)
        assertTrue(assets[4].details is InteriorDetails)
    }

    @Test fun `canonical fixtures retain semantics after JSON round trip`() {
        validFixtures.map(::assetResource).forEach { original ->
            val restored = json.decodeFromString<Asset>(json.encodeToString(original))
            assertEquals(original, restored)
        }
    }

    @Test fun `details JSON has no Kotlin metadata or discriminator`() {
        listOf(assetResource(validFixtures[0]), assetResource(validFixtures[3])).forEach { asset ->
            val details = json.parseToJsonElement(json.encodeToString(asset)).jsonObject.getValue("details").jsonObject
            assertFalse("details must not contain assetType", "assetType" in details)
            assertFalse("details must not contain a Kotlin discriminator", details.keys.any { it in setOf("type", "_type", "@type", "class") })
        }
    }

    @Test fun `serialized canonical fixtures are available for schema tooling`() {
        val outputDirectory = Path.of(System.getProperty("user.dir"), "build", "generated", "kotlin-asset-schema-v1")
        Files.createDirectories(outputDirectory)
        validFixtures.forEach { fixture ->
            Files.write(outputDirectory.resolve(fixture.substringAfterLast('/')), json.encodeToString(assetResource(fixture)).toByteArray())
        }
    }

    @Test fun `all invalid canonical fixtures fail decoding or domain validation`() {
        listOf(
            "test-fixtures/invalid/unknown-type.json",
            "test-fixtures/invalid/missing-required-content.json",
            "test-fixtures/invalid/invalid-asset-id.json",
            "test-fixtures/invalid/incorrect-schema-version.json",
            "test-fixtures/invalid/incompatible-details.json",
        ).forEach { path ->
            val text = resource(path)
            val rejected = runCatching { json.decodeFromString<Asset>(text) }
                .fold(onSuccess = { AssetValidator.validate(it).isNotEmpty() }, onFailure = { true })
            assertTrue("$path should be rejected", rejected)
        }
    }

    @Test fun `incompatible type and details is rejected by validation`() {
        val asset = assetResource(validFixtures.first()).copy(type = AssetType.LANDSCAPE)
        assertTrue(AssetValidator.validate(asset).any { it.contains("details must match type") })
    }

    @Test fun `self-referential source asset is rejected`() {
        val original = assetResource(validFixtures.first())
        val asset = original.copy(provenance = original.provenance.copy(originKind = OriginKind.DERIVED, sourceAssetIds = listOf(original.assetId)))
        assertTrue(AssetValidator.validate(asset).any { it.contains("sourceAssetIds cannot contain") })
    }

    @Test fun `self-referential supersession is rejected`() {
        val original = assetResource(validFixtures.first())
        val asset = original.copy(lifecycle = original.lifecycle.copy(supersededByAssetId = original.assetId))
        assertTrue(AssetValidator.validate(asset).any { it.contains("supersededByAssetId") })
    }

    @Test fun `paired identifiers and versions must be present together`() {
        val original = assetResource(validFixtures.first())
        val asset = original.copy(visual = Visual(visualProfileId = "profile"))
        assertTrue(AssetValidator.validate(asset).any { it.contains("visual profile ID and version") })
    }

    private fun assetResource(path: String): Asset = json.decodeFromString(resource(path))
    private fun resource(path: String): String = checkNotNull(javaClass.classLoader?.getResource(path)) { "Missing canonical fixture $path" }.readText()
}

package com.nimroel.assetmanager.data.local

import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetJson
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.NpcPortraitDetails
import kotlinx.serialization.decodeFromString
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AssetDocumentProjectorTest {
    @Test
    fun `canonical JSON and all projections come from the validated decoded Asset`() {
        val asset = TestAssets.withExtensionsAndOptionalFields().copy(
            subject = TestAssets.fixture().subject?.copy(entityId = "npc.valemar.farmer"),
        )

        val document = AssetDocumentProjector.project(asset)
        val decoded = AssetJson.codec.decodeFromString<Asset>(document.canonicalJson)

        assertEquals(asset, decoded)
        assertTrue(decoded.details is NpcPortraitDetails)
        assertEquals("preserved", decoded.extensions?.namespaces?.get("nimroel.test")?.get("optionalText")?.toString()?.trim('"'))
        assertEquals(asset.assetId.value, document.assetId)
        assertEquals(1, document.schemaVersion)
        assertEquals("npc_portrait", document.assetType)
        assertEquals("approved", document.lifecycleStatus)
        assertEquals("valemar", document.realmId)
        assertEquals("valemar", document.cultureId)
        assertEquals("npc.valemar.farmer", document.subjectEntityId)
        assertEquals(CURRENT_PROJECTION_VERSION, document.projectionVersion)
    }

    @Test(expected = InvalidAssetForPersistenceException::class)
    fun `invalid Asset is rejected before a document can be produced`() {
        AssetDocumentProjector.project(TestAssets.fixture().copy(content = TestAssets.fixture().content.copy(widthPx = 0)))
    }

    @Test
    fun `canonical enum projections use contract wire values`() {
        assertEquals("environment_scene", CanonicalWireValues.assetType(AssetType.ENVIRONMENT_SCENE))
        assertEquals("deprecated", CanonicalWireValues.lifecycleStatus(LifecycleStatus.DEPRECATED))
    }
}

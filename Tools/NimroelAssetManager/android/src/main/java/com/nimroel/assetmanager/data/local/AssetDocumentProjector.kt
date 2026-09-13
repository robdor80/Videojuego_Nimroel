package com.nimroel.assetmanager.data.local

import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetJson
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.AssetValidator
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString

internal object AssetDocumentProjector {
    fun project(asset: Asset): AssetDocumentEntity {
        validateForPersistence(asset)

        val firstPassJson = AssetJson.codec.encodeToString(asset)
        val canonicalAsset = decodeAndValidate(firstPassJson, asset.assetId.value)
        val canonicalJson = AssetJson.codec.encodeToString(canonicalAsset)

        return AssetDocumentEntity(
            assetId = canonicalAsset.assetId.value,
            schemaVersion = canonicalAsset.schemaVersion,
            canonicalJson = canonicalJson,
            assetType = CanonicalWireValues.assetType(canonicalAsset.type),
            lifecycleStatus = CanonicalWireValues.lifecycleStatus(canonicalAsset.lifecycle.status),
            realmId = canonicalAsset.classification?.realmId,
            cultureId = canonicalAsset.classification?.cultureId,
            subjectEntityId = canonicalAsset.subject?.entityId,
            projectionVersion = CURRENT_PROJECTION_VERSION,
        )
    }

    fun restore(document: AssetDocumentEntity): Asset =
        decodeAndValidate(document.canonicalJson, document.assetId).also { asset ->
            if (asset.assetId.value != document.assetId) {
                throw InvalidStoredAssetException(document.assetId, listOf("canonical assetId does not match the row primary key"))
            }
        }

    private fun validateForPersistence(asset: Asset) {
        val violations = AssetValidator.validate(asset)
        if (violations.isNotEmpty()) throw InvalidAssetForPersistenceException(asset.assetId.value, violations)
    }

    private fun decodeAndValidate(json: String, expectedAssetId: String): Asset {
        val asset = try {
            AssetJson.codec.decodeFromString<Asset>(json)
        } catch (error: Exception) {
            throw InvalidStoredAssetException(expectedAssetId, listOf("canonical_json cannot be decoded"), error)
        }
        val violations = AssetValidator.validate(asset)
        if (violations.isNotEmpty()) throw InvalidStoredAssetException(expectedAssetId, violations)
        return asset
    }
}

internal object CanonicalWireValues {
    fun assetType(value: AssetType): String = when (value) {
        AssetType.NPC_PORTRAIT -> "npc_portrait"
        AssetType.LANDSCAPE -> "landscape"
        AssetType.SETTLEMENT -> "settlement"
        AssetType.BUILDING -> "building"
        AssetType.INTERIOR -> "interior"
        AssetType.OBJECT -> "object"
        AssetType.ENVIRONMENT_SCENE -> "environment_scene"
    }

    fun lifecycleStatus(value: LifecycleStatus): String = when (value) {
        LifecycleStatus.DRAFT -> "draft"
        LifecycleStatus.APPROVED -> "approved"
        LifecycleStatus.DEPRECATED -> "deprecated"
        LifecycleStatus.RETIRED -> "retired"
    }
}

internal class InvalidAssetForPersistenceException(
    assetId: String,
    val violations: List<String>,
) : IllegalArgumentException("Asset $assetId is invalid: ${violations.joinToString()}")

internal class InvalidStoredAssetException(
    assetId: String,
    val violations: List<String>,
    cause: Throwable? = null,
) : IllegalStateException("Stored Asset $assetId is invalid: ${violations.joinToString()}", cause)

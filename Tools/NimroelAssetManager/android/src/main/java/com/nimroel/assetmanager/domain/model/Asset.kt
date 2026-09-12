package com.nimroel.assetmanager.domain.model

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.builtins.MapSerializer
import kotlinx.serialization.builtins.serializer
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonPrimitive
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.decodeFromJsonElement
import kotlinx.serialization.json.encodeToJsonElement
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.put

@Serializable(with = AssetSerializer::class)
data class Asset(
    val schemaVersion: Int,
    val assetId: AssetId,
    val type: AssetType,
    val lifecycle: Lifecycle,
    val classification: Classification? = null,
    val subject: Subject? = null,
    val details: AssetDetails? = null,
    val visual: Visual? = null,
    val content: Content,
    val provenance: Provenance,
    val storage: Storage? = null,
    val extensions: Extensions? = null,
)

@Serializable
enum class AssetType {
    @kotlinx.serialization.SerialName("npc_portrait") NPC_PORTRAIT,
    @kotlinx.serialization.SerialName("landscape") LANDSCAPE,
    @kotlinx.serialization.SerialName("settlement") SETTLEMENT,
    @kotlinx.serialization.SerialName("building") BUILDING,
    @kotlinx.serialization.SerialName("interior") INTERIOR,
    @kotlinx.serialization.SerialName("object") OBJECT,
    @kotlinx.serialization.SerialName("environment_scene") ENVIRONMENT_SCENE,
}

@Serializable data class Lifecycle(val status: LifecycleStatus, val supersededByAssetId: AssetId? = null, val note: String? = null)
@Serializable enum class LifecycleStatus { @kotlinx.serialization.SerialName("draft") DRAFT, @kotlinx.serialization.SerialName("approved") APPROVED, @kotlinx.serialization.SerialName("deprecated") DEPRECATED, @kotlinx.serialization.SerialName("retired") RETIRED }
@Serializable data class Classification(val vocabularyId: String? = null, val vocabularyVersion: String? = null, val realmId: String? = null, val cultureId: String? = null, val regionId: String? = null, val settlementId: String? = null, val tags: List<String>? = null)
@Serializable data class Subject(val entityId: String? = null, val speciesId: String? = null, val genderId: String? = null, val ageBandId: String? = null)
@Serializable data class Visual(val visualProfileId: String? = null, val visualProfileVersion: String? = null, val compositionId: String? = null, val timeOfDayId: String? = null, val weatherId: String? = null, val lightingId: String? = null, val expressionId: String? = null)
@Serializable data class Content(val mimeType: String, val widthPx: Int, val heightPx: Int, val byteSize: Long? = null, val sha256: String, val colorSpace: String? = null)
@Serializable data class Provenance(val originKind: OriginKind, val generator: Generator? = null, val sourceAssetIds: List<AssetId>? = null, val promptTemplateId: String? = null, val promptTemplateVersion: String? = null, val promptRecordId: String? = null, val importedAt: String? = null)
@Serializable enum class OriginKind { @kotlinx.serialization.SerialName("generated") GENERATED, @kotlinx.serialization.SerialName("imported") IMPORTED, @kotlinx.serialization.SerialName("edited") EDITED, @kotlinx.serialization.SerialName("derived") DERIVED, @kotlinx.serialization.SerialName("unknown") UNKNOWN }
@Serializable data class Generator(val provider: String, val model: String? = null, val generatedAt: String)
@Serializable data class Storage(val replicas: List<Replica>)
@Serializable data class Replica(val replicaId: String, val locationType: LocationType, val purpose: ReplicaPurpose? = null, val provider: String, val objectId: String? = null, val logicalPath: String? = null, val deliveryUrl: String? = null)
@Serializable enum class LocationType { @kotlinx.serialization.SerialName("local") LOCAL, @kotlinx.serialization.SerialName("remote") REMOTE }
@Serializable enum class ReplicaPurpose { @kotlinx.serialization.SerialName("primary") PRIMARY, @kotlinx.serialization.SerialName("backup") BACKUP, @kotlinx.serialization.SerialName("cache") CACHE }

/** Arbitrary JSON is contained only under a namespace; canonical fields stay typed. */
@Serializable data class Extensions(val namespaces: Map<String, JsonObject>)

sealed interface AssetDetails { val assetType: AssetType }
@Serializable data class NpcPortraitDetails(val professionId: String? = null, val socialClassId: String? = null) : AssetDetails { override val assetType get() = AssetType.NPC_PORTRAIT }
@Serializable data class LandscapeDetails(val environmentId: String, val landformIds: List<String>? = null, val waterFeatureIds: List<String>? = null, val seasonId: String? = null) : AssetDetails { override val assetType get() = AssetType.LANDSCAPE }
@Serializable data class SettlementDetails(val settlementScaleId: String, val environmentId: String? = null) : AssetDetails { override val assetType get() = AssetType.SETTLEMENT }
@Serializable data class BuildingDetails(val buildingFunctionId: String, val materialIds: List<String>? = null) : AssetDetails { override val assetType get() = AssetType.BUILDING }
@Serializable data class InteriorDetails(val interiorFunctionId: String, val containingBuildingEntityId: String? = null) : AssetDetails { override val assetType get() = AssetType.INTERIOR }
@Serializable data class ObjectDetails(val objectKindId: String, val materialIds: List<String>? = null) : AssetDetails { override val assetType get() = AssetType.OBJECT }
@Serializable data class EnvironmentSceneDetails(val sceneFunctionId: String, val environmentId: String? = null, val featuredEntityIds: List<String>? = null) : AssetDetails { override val assetType get() = AssetType.ENVIRONMENT_SCENE }

object AssetJson {
    val codec = Json { encodeDefaults = false; explicitNulls = false; ignoreUnknownKeys = false }
}

object AssetSerializer : KSerializer<Asset> {
    override val descriptor: SerialDescriptor = JsonObject.serializer().descriptor

    override fun deserialize(decoder: Decoder): Asset {
        val jsonDecoder = decoder as? kotlinx.serialization.json.JsonDecoder ?: throw SerializationException("Asset requires JSON")
        val objectValue = jsonDecoder.decodeJsonElement().jsonObject
        val type = jsonDecoder.json.decodeFromJsonElement<AssetType>(objectValue.getValue("type"))
        val details = objectValue["details"]?.jsonObject?.let { decodeDetails(jsonDecoder.json, type, it) }
        val wire = jsonDecoder.json.decodeFromJsonElement<AssetWire>(objectValue)
        return wire.toAsset(details)
    }

    override fun serialize(encoder: Encoder, value: Asset) {
        val jsonEncoder = encoder as? kotlinx.serialization.json.JsonEncoder ?: throw SerializationException("Asset requires JSON")
        if (value.details != null && value.details.assetType != value.type) throw SerializationException("details does not match type")
        val base = jsonEncoder.json.encodeToJsonElement(value.toWire()).jsonObject
        val result = buildJsonObject {
            base.forEach { (key, element) -> if (key != "details" && key != "extensions") put(key, element) }
            value.details?.let { put("details", encodeDetails(jsonEncoder.json, it)) }
            value.extensions?.let { put("extensions", jsonEncoder.json.encodeToJsonElement(MapSerializer(String.serializer(), JsonObject.serializer()), it.namespaces)) }
        }
        jsonEncoder.encodeJsonElement(result)
    }

    private fun decodeDetails(json: Json, type: AssetType, value: JsonObject): AssetDetails = when (type) {
        AssetType.NPC_PORTRAIT -> json.decodeFromJsonElement<NpcPortraitDetails>(value)
        AssetType.LANDSCAPE -> json.decodeFromJsonElement<LandscapeDetails>(value)
        AssetType.SETTLEMENT -> json.decodeFromJsonElement<SettlementDetails>(value)
        AssetType.BUILDING -> json.decodeFromJsonElement<BuildingDetails>(value)
        AssetType.INTERIOR -> json.decodeFromJsonElement<InteriorDetails>(value)
        AssetType.OBJECT -> json.decodeFromJsonElement<ObjectDetails>(value)
        AssetType.ENVIRONMENT_SCENE -> json.decodeFromJsonElement<EnvironmentSceneDetails>(value)
    }
    private fun encodeDetails(json: Json, value: AssetDetails) = when (value) {
        is NpcPortraitDetails -> json.encodeToJsonElement(value)
        is LandscapeDetails -> json.encodeToJsonElement(value)
        is SettlementDetails -> json.encodeToJsonElement(value)
        is BuildingDetails -> json.encodeToJsonElement(value)
        is InteriorDetails -> json.encodeToJsonElement(value)
        is ObjectDetails -> json.encodeToJsonElement(value)
        is EnvironmentSceneDetails -> json.encodeToJsonElement(value)
    }
}

@Serializable
private data class AssetWire(val schemaVersion: Int, val assetId: AssetId, val type: AssetType, val lifecycle: Lifecycle, val classification: Classification? = null, val subject: Subject? = null, val details: JsonObject? = null, val visual: Visual? = null, val content: Content, val provenance: Provenance, val storage: Storage? = null, val extensions: Map<String, JsonObject>? = null)
private fun AssetWire.toAsset(details: AssetDetails?) = Asset(schemaVersion, assetId, type, lifecycle, classification, subject, details, visual, content, provenance, storage, extensions?.let(::Extensions))
private fun Asset.toWire() = AssetWire(
    schemaVersion = schemaVersion,
    assetId = assetId,
    type = type,
    lifecycle = lifecycle,
    classification = classification,
    subject = subject,
    visual = visual,
    content = content,
    provenance = provenance,
    storage = storage,
    extensions = extensions?.namespaces,
)

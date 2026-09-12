package com.nimroel.assetmanager.domain.model

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** Opaque, immutable `ast_` + canonical lowercase UUIDv7 identity. */
@Serializable(with = AssetIdSerializer::class)
@JvmInline
value class AssetId private constructor(val value: String) {
    companion object {
        private val pattern = Regex("^ast_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")

        fun parse(value: String): AssetId {
            require(pattern.matches(value)) { "Asset ID must be ast_ followed by a canonical lowercase UUIDv7." }
            return AssetId(value)
        }
    }
}

object AssetIdSerializer : KSerializer<AssetId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor("AssetId", PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AssetId = AssetId.parse(decoder.decodeString())
    override fun serialize(encoder: Encoder, value: AssetId) = encoder.encodeString(value.value)
}

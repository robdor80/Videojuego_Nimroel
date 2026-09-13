package com.nimroel.assetmanager.data.local

import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetJson
import com.nimroel.assetmanager.domain.model.Extensions
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.JsonPrimitive
import kotlinx.serialization.json.buildJsonObject

internal object TestAssets {
    fun fixture(): Asset = AssetJson.codec.decodeFromString(resource("examples/npc-portrait-valemar-farmer.json"))

    fun withExtensionsAndOptionalFields(): Asset = fixture().copy(
        extensions = Extensions(
            mapOf(
                "nimroel.test" to buildJsonObject {
                    put("optionalText", JsonPrimitive("preserved"))
                    put("optionalNumber", JsonPrimitive(7))
                },
            ),
        ),
    )

    private fun resource(path: String): String =
        checkNotNull(javaClass.classLoader?.getResource(path)) { "Missing canonical fixture $path" }.readText()
}

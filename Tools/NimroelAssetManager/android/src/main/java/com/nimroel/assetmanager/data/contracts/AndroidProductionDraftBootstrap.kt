package com.nimroel.assetmanager.data.contracts

import android.content.res.AssetManager
import com.nimroel.assetmanager.domain.contracts.ContractJson
import com.nimroel.assetmanager.domain.contracts.PresetRegistry
import com.nimroel.assetmanager.domain.contracts.ProductionPreset
import com.nimroel.assetmanager.domain.contracts.Vocabulary
import com.nimroel.assetmanager.domain.contracts.VocabularyRegistry
import com.nimroel.assetmanager.domain.contracts.VocabularySet
import com.nimroel.assetmanager.domain.contracts.VocabularySetRegistry
import com.nimroel.assetmanager.domain.production.ProductionDraft
import com.nimroel.assetmanager.domain.production.ProductionDraftService
import kotlinx.serialization.decodeFromString

data class ProductionDraftEnvironment(
    val service: ProductionDraftService,
    val draft: ProductionDraft,
    val presetLabel: String,
)

fun interface ProductionDraftBootstrap {
    fun load(): ProductionDraftEnvironment
}

/** Temporary single-preset entry point; editorial IDs remain outside ViewModels and Composables. */
object PilotProductionConfiguration {
    const val PRESET_ID = "npc-portrait-pilot"
    const val PRESET_VERSION = "1.0"
}

class AndroidProductionDraftBootstrap(
    private val assets: AssetManager,
) : ProductionDraftBootstrap {
    override fun load(): ProductionDraftEnvironment {
        val presets = readDirectory<ProductionPreset>(PRESETS_DIRECTORY)
        val sets = readDirectory<VocabularySet>(VOCABULARY_SETS_DIRECTORY)
        val vocabularies = readDirectory<Vocabulary>(VOCABULARIES_DIRECTORY)

        val presetRegistry = PresetRegistry.create(presets)
        val service = ProductionDraftService(
            presets = presetRegistry,
            vocabularySets = VocabularySetRegistry.create(sets),
            vocabularies = VocabularyRegistry.create(vocabularies),
        )
        val preset = presetRegistry.preset(
            PilotProductionConfiguration.PRESET_ID,
            PilotProductionConfiguration.PRESET_VERSION,
        ) ?: throw ProductionBootstrapException(
            "No se encuentra el preset piloto ${PilotProductionConfiguration.PRESET_ID} ${PilotProductionConfiguration.PRESET_VERSION}.",
        )
        return ProductionDraftEnvironment(
            service = service,
            draft = service.startDraft(preset.presetId, preset.version),
            presetLabel = preset.label,
        )
    }

    private inline fun <reified T> readDirectory(path: String): List<T> {
        val names = assets.list(path)
            ?.filter { it.endsWith(".json") }
            ?.sorted()
            .orEmpty()
        if (names.isEmpty()) throw ProductionBootstrapException("No hay contratos JSON empaquetados en $path.")
        return names.map { name ->
            val assetPath = "$path/$name"
            try {
                assets.open(assetPath).bufferedReader().use { reader ->
                    ContractJson.codec.decodeFromString<T>(reader.readText())
                }
            } catch (error: Exception) {
                throw ProductionBootstrapException("No se pudo cargar el contrato $assetPath: ${error.message}", error)
            }
        }
    }

    private companion object {
        const val PRESETS_DIRECTORY = "presets/examples"
        const val VOCABULARY_SETS_DIRECTORY = "vocabulary-sets/data"
        const val VOCABULARIES_DIRECTORY = "vocabularies/data"
    }
}

class ProductionBootstrapException(message: String, cause: Throwable? = null) : IllegalStateException(message, cause)

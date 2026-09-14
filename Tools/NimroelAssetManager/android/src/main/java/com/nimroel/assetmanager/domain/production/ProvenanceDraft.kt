package com.nimroel.assetmanager.domain.production

import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.Generator
import com.nimroel.assetmanager.domain.model.OriginKind
import com.nimroel.assetmanager.domain.model.Provenance
import java.time.Instant
import java.time.format.DateTimeParseException

/** Explicit editing state. It is never persisted and is not a second canonical Provenance model. */
sealed interface ProvenanceDraft {
    data object NotSpecified : ProvenanceDraft

    data class Generated(
        val provider: String = "",
        val model: String = "",
        val generatedAt: DraftInstant = DraftInstant.Empty,
    ) : ProvenanceDraft

    data class Imported(
        val importedAt: DraftInstant = DraftInstant.Empty,
    ) : ProvenanceDraft

    data class Edited(val sourceAssetIdsText: String = "") : ProvenanceDraft
    data class Derived(val sourceAssetIdsText: String = "") : ProvenanceDraft
    data class Unknown(val confirmed: Boolean = false) : ProvenanceDraft
}

/** A temporal field is either absent, a parsed Instant, or explicitly invalid editing input. */
sealed interface DraftInstant {
    val text: String

    data object Empty : DraftInstant {
        override val text: String = ""
    }

    data class Valid(val value: Instant) : DraftInstant {
        override val text: String = value.toString()
    }

    data class Invalid(override val text: String) : DraftInstant

    companion object {
        fun parse(text: String): DraftInstant {
            if (text.isBlank()) return Empty
            return try {
                Valid(Instant.parse(text))
            } catch (_: DateTimeParseException) {
                Invalid(text)
            }
        }
    }
}

enum class ProvenanceDraftErrorCode {
    NOT_SPECIFIED,
    INVALID_PROVIDER,
    GENERATED_AT_REQUIRED,
    INVALID_GENERATED_AT,
    INVALID_MODEL,
    INVALID_IMPORTED_AT,
    SOURCE_ASSET_IDS_REQUIRED,
    INVALID_SOURCE_ASSET_ID,
    DUPLICATE_SOURCE_ASSET_ID,
    SOURCE_ASSET_ID_IS_TARGET,
    UNKNOWN_NOT_CONFIRMED,
}

data class ProvenanceDraftError(
    val code: ProvenanceDraftErrorCode,
    val message: String,
)

sealed interface ProvenanceMaterialization {
    data class Valid(val provenance: Provenance) : ProvenanceMaterialization
    data class Invalid(val errors: List<ProvenanceDraftError>) : ProvenanceMaterialization
}

/** The sole authority that turns editable provenance input into canonical Asset Schema v1 Provenance. */
class ProvenanceDraftService {
    fun select(originKind: OriginKind): ProvenanceDraft = when (originKind) {
        OriginKind.GENERATED -> ProvenanceDraft.Generated()
        OriginKind.IMPORTED -> ProvenanceDraft.Imported()
        OriginKind.EDITED -> ProvenanceDraft.Edited()
        OriginKind.DERIVED -> ProvenanceDraft.Derived()
        OriginKind.UNKNOWN -> ProvenanceDraft.Unknown()
    }

    fun setGeneratedProvider(draft: ProvenanceDraft, value: String): ProvenanceDraft =
        requireGenerated(draft).copy(provider = value)

    fun setGeneratedModel(draft: ProvenanceDraft, value: String): ProvenanceDraft =
        requireGenerated(draft).copy(model = value)

    fun setGeneratedAt(draft: ProvenanceDraft, value: String): ProvenanceDraft =
        requireGenerated(draft).copy(generatedAt = DraftInstant.parse(value))

    fun useGeneratedAt(draft: ProvenanceDraft, value: Instant): ProvenanceDraft =
        requireGenerated(draft).copy(generatedAt = DraftInstant.Valid(value))

    fun setImportedAt(draft: ProvenanceDraft, value: String): ProvenanceDraft =
        requireImported(draft).copy(importedAt = DraftInstant.parse(value))

    fun useImportedAt(draft: ProvenanceDraft, value: Instant): ProvenanceDraft =
        requireImported(draft).copy(importedAt = DraftInstant.Valid(value))

    fun setSourceAssetIds(draft: ProvenanceDraft, value: String): ProvenanceDraft = when (draft) {
        is ProvenanceDraft.Edited -> draft.copy(sourceAssetIdsText = value)
        is ProvenanceDraft.Derived -> draft.copy(sourceAssetIdsText = value)
        else -> error("Source Asset IDs can only be edited for edited or derived provenance.")
    }

    fun setUnknownConfirmed(draft: ProvenanceDraft, confirmed: Boolean): ProvenanceDraft =
        (draft as? ProvenanceDraft.Unknown)?.copy(confirmed = confirmed)
            ?: error("Unknown confirmation can only be edited for unknown provenance.")

    fun materialize(
        draft: ProvenanceDraft,
        targetAssetId: AssetId,
    ): ProvenanceMaterialization {
        val errors = validate(draft, targetAssetId)
        if (errors.isNotEmpty()) return ProvenanceMaterialization.Invalid(errors)
        val provenance = when (draft) {
            ProvenanceDraft.NotSpecified -> error("Validated NotSpecified provenance cannot be materialized.")
            is ProvenanceDraft.Generated -> Provenance(
                originKind = OriginKind.GENERATED,
                generator = Generator(
                    provider = draft.provider,
                    model = draft.model.takeUnless(String::isBlank),
                    generatedAt = (draft.generatedAt as DraftInstant.Valid).value.toString(),
                ),
            )
            is ProvenanceDraft.Imported -> Provenance(
                originKind = OriginKind.IMPORTED,
                importedAt = (draft.importedAt as? DraftInstant.Valid)?.value?.toString(),
            )
            is ProvenanceDraft.Edited -> Provenance(
                originKind = OriginKind.EDITED,
                sourceAssetIds = parseSourceAssetIds(draft.sourceAssetIdsText),
            )
            is ProvenanceDraft.Derived -> Provenance(
                originKind = OriginKind.DERIVED,
                sourceAssetIds = parseSourceAssetIds(draft.sourceAssetIdsText),
            )
            is ProvenanceDraft.Unknown -> Provenance(originKind = OriginKind.UNKNOWN)
        }
        return ProvenanceMaterialization.Valid(provenance)
    }

    fun validate(draft: ProvenanceDraft, targetAssetId: AssetId): List<ProvenanceDraftError> = buildList {
        when (draft) {
            ProvenanceDraft.NotSpecified -> add(
                ProvenanceDraftError(ProvenanceDraftErrorCode.NOT_SPECIFIED, "Selecciona la procedencia real de la imagen."),
            )
            is ProvenanceDraft.Generated -> {
                if (!REFERENCE_ID.matches(draft.provider) || draft.provider.length > 128) {
                    add(ProvenanceDraftError(ProvenanceDraftErrorCode.INVALID_PROVIDER, "El proveedor es obligatorio y debe ser un ID válido."))
                }
                when (draft.generatedAt) {
                    DraftInstant.Empty -> add(ProvenanceDraftError(ProvenanceDraftErrorCode.GENERATED_AT_REQUIRED, "La fecha y hora de generación es obligatoria."))
                    is DraftInstant.Invalid -> add(ProvenanceDraftError(ProvenanceDraftErrorCode.INVALID_GENERATED_AT, "La fecha y hora de generación debe usar formato ISO-8601."))
                    is DraftInstant.Valid -> Unit
                }
                if (draft.model.isNotBlank() && draft.model.length > 200) {
                    add(ProvenanceDraftError(ProvenanceDraftErrorCode.INVALID_MODEL, "El modelo no puede superar 200 caracteres."))
                }
            }
            is ProvenanceDraft.Imported -> if (draft.importedAt is DraftInstant.Invalid) {
                add(ProvenanceDraftError(ProvenanceDraftErrorCode.INVALID_IMPORTED_AT, "La fecha y hora de importación debe usar formato ISO-8601."))
            }
            is ProvenanceDraft.Edited -> validateSources(draft.sourceAssetIdsText, targetAssetId, this)
            is ProvenanceDraft.Derived -> validateSources(draft.sourceAssetIdsText, targetAssetId, this)
            is ProvenanceDraft.Unknown -> if (!draft.confirmed) {
                add(ProvenanceDraftError(ProvenanceDraftErrorCode.UNKNOWN_NOT_CONFIRMED, "Confirma explícitamente que la procedencia real es desconocida."))
            }
        }
    }

    private fun validateSources(value: String, targetAssetId: AssetId, errors: MutableList<ProvenanceDraftError>) {
        val tokens = sourceTokens(value)
        if (tokens.isEmpty()) {
            errors += ProvenanceDraftError(ProvenanceDraftErrorCode.SOURCE_ASSET_IDS_REQUIRED, "Indica al menos un Asset de origen.")
            return
        }
        val parsed = tokens.mapNotNull { token ->
            try {
                AssetId.parse(token)
            } catch (_: IllegalArgumentException) {
                errors += ProvenanceDraftError(ProvenanceDraftErrorCode.INVALID_SOURCE_ASSET_ID, "Uno de los AssetId de origen no es válido.")
                null
            }
        }
        if (tokens.distinct().size != tokens.size) {
            errors += ProvenanceDraftError(ProvenanceDraftErrorCode.DUPLICATE_SOURCE_ASSET_ID, "Los Assets de origen no pueden repetirse.")
        }
        if (targetAssetId in parsed) {
            errors += ProvenanceDraftError(ProvenanceDraftErrorCode.SOURCE_ASSET_ID_IS_TARGET, "El Asset reservado no puede ser su propio origen.")
        }
    }

    private fun parseSourceAssetIds(value: String): List<AssetId> = sourceTokens(value).map(AssetId::parse)

    private fun sourceTokens(value: String): List<String> =
        value.split(SOURCE_SEPARATOR).map(String::trim).filter(String::isNotEmpty)

    private fun requireGenerated(draft: ProvenanceDraft): ProvenanceDraft.Generated =
        draft as? ProvenanceDraft.Generated ?: error("Generated fields require generated provenance.")

    private fun requireImported(draft: ProvenanceDraft): ProvenanceDraft.Imported =
        draft as? ProvenanceDraft.Imported ?: error("Imported fields require imported provenance.")

    private companion object {
        val REFERENCE_ID = Regex("^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
        val SOURCE_SEPARATOR = Regex("[,\\r\\n]+")
    }
}

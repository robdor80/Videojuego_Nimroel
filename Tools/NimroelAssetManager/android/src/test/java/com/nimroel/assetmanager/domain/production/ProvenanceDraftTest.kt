package com.nimroel.assetmanager.domain.production

import com.nimroel.assetmanager.domain.model.Asset
import com.nimroel.assetmanager.domain.model.AssetId
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.model.AssetValidator
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.Lifecycle
import com.nimroel.assetmanager.domain.model.LifecycleStatus
import com.nimroel.assetmanager.domain.model.OriginKind
import java.time.Instant
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class ProvenanceDraftTest {
    private val service = ProvenanceDraftService()

    @Test
    fun `initial state is not specified and cannot materialize`() {
        val result = service.materialize(ProvenanceDraft.NotSpecified, targetAssetId())

        assertInvalid(result, ProvenanceDraftErrorCode.NOT_SPECIFIED)
    }

    @Test
    fun `generated requires provider and generatedAt while model stays optional`() {
        val selected = service.select(OriginKind.GENERATED)

        assertInvalid(service.materialize(selected, targetAssetId()), ProvenanceDraftErrorCode.INVALID_PROVIDER)
        assertInvalid(service.materialize(selected, targetAssetId()), ProvenanceDraftErrorCode.GENERATED_AT_REQUIRED)

        val withoutProvider = service.useGeneratedAt(selected, Instant.parse("2026-09-14T10:00:00Z"))
        assertInvalid(service.materialize(withoutProvider, targetAssetId()), ProvenanceDraftErrorCode.INVALID_PROVIDER)

        val withoutDate = service.setGeneratedProvider(selected, "custom-provider")
        assertInvalid(service.materialize(withoutDate, targetAssetId()), ProvenanceDraftErrorCode.GENERATED_AT_REQUIRED)

        val valid = service.materialize(
            service.useGeneratedAt(withoutDate, Instant.parse("2026-09-14T10:00:00Z")),
            targetAssetId(),
        ).valid()
        assertEquals(OriginKind.GENERATED, valid.originKind)
        assertEquals("custom-provider", valid.generator?.provider)
        assertEquals("2026-09-14T10:00:00Z", valid.generator?.generatedAt)
        assertNull(valid.generator?.model)
    }

    @Test
    fun `generated accepts an explicit optional model and rejects an invalid date`() {
        var draft = service.select(OriginKind.GENERATED)
        draft = service.setGeneratedProvider(draft, "local.tool")
        draft = service.setGeneratedModel(draft, "Any Image Model")
        draft = service.setGeneratedAt(draft, "not-a-date")

        assertInvalid(service.materialize(draft, targetAssetId()), ProvenanceDraftErrorCode.INVALID_GENERATED_AT)

        draft = service.setGeneratedAt(draft, "2026-09-14T11:12:13Z")
        assertEquals("Any Image Model", service.materialize(draft, targetAssetId()).valid().generator?.model)
    }

    @Test
    fun `generated rejects a provider composed only of whitespace`() {
        var draft = service.select(OriginKind.GENERATED)
        draft = service.setGeneratedProvider(draft, "   ")
        draft = service.useGeneratedAt(draft, Instant.parse("2026-09-14T10:00:00Z"))

        assertInvalid(service.materialize(draft, targetAssetId()), ProvenanceDraftErrorCode.INVALID_PROVIDER)
    }

    @Test
    fun `imported exists only after explicit selection and importedAt is optional`() {
        assertInvalid(service.materialize(ProvenanceDraft.NotSpecified, targetAssetId()), ProvenanceDraftErrorCode.NOT_SPECIFIED)

        val imported = service.materialize(service.select(OriginKind.IMPORTED), targetAssetId()).valid()

        assertEquals(OriginKind.IMPORTED, imported.originKind)
        assertNull(imported.importedAt)
        assertNull(imported.generator)
        assertNull(imported.sourceAssetIds)
    }

    @Test
    fun `importedAt is stored only after safe Instant parsing`() {
        val selected = service.select(OriginKind.IMPORTED)
        assertInvalid(service.materialize(service.setImportedAt(selected, "yesterday"), targetAssetId()), ProvenanceDraftErrorCode.INVALID_IMPORTED_AT)

        val imported = service.materialize(service.setImportedAt(selected, "2026-09-14T10:00:00Z"), targetAssetId()).valid()
        assertEquals("2026-09-14T10:00:00Z", imported.importedAt)
    }

    @Test
    fun `edited and derived require parsed source AssetIds`() {
        val source = sourceAssetId().value
        val editedEmpty = service.select(OriginKind.EDITED)
        val derivedEmpty = service.select(OriginKind.DERIVED)

        assertInvalid(service.materialize(editedEmpty, targetAssetId()), ProvenanceDraftErrorCode.SOURCE_ASSET_IDS_REQUIRED)
        assertInvalid(service.materialize(derivedEmpty, targetAssetId()), ProvenanceDraftErrorCode.SOURCE_ASSET_IDS_REQUIRED)

        val edited = service.materialize(service.setSourceAssetIds(editedEmpty, source), targetAssetId()).valid()
        val derived = service.materialize(service.setSourceAssetIds(derivedEmpty, source), targetAssetId()).valid()
        assertEquals(OriginKind.EDITED, edited.originKind)
        assertEquals(listOf(sourceAssetId()), edited.sourceAssetIds)
        assertEquals(OriginKind.DERIVED, derived.originKind)
        assertEquals(listOf(sourceAssetId()), derived.sourceAssetIds)
    }

    @Test
    fun `edited rejects invalid and duplicate AssetIds`() {
        val selected = service.select(OriginKind.EDITED)
        assertInvalid(service.materialize(service.setSourceAssetIds(selected, "ast_invalid"), targetAssetId()), ProvenanceDraftErrorCode.INVALID_SOURCE_ASSET_ID)

        val repeated = "${sourceAssetId().value}\n${sourceAssetId().value}"
        assertInvalid(service.materialize(service.setSourceAssetIds(selected, repeated), targetAssetId()), ProvenanceDraftErrorCode.DUPLICATE_SOURCE_ASSET_ID)
    }

    @Test
    fun `edited rejects a self referential AssetId`() {
        val target = targetAssetId()
        val draft = service.setSourceAssetIds(service.select(OriginKind.EDITED), target.value)

        assertInvalid(
            service.materialize(draft, target),
            ProvenanceDraftErrorCode.SOURCE_ASSET_ID_IS_TARGET,
        )
    }

    @Test
    fun `derived rejects a self referential AssetId`() {
        val target = targetAssetId()
        val draft = service.setSourceAssetIds(service.select(OriginKind.DERIVED), target.value)

        assertInvalid(service.materialize(draft, target), ProvenanceDraftErrorCode.SOURCE_ASSET_ID_IS_TARGET)
    }

    @Test
    fun `derived rejects an invalid AssetId`() {
        val draft = service.setSourceAssetIds(service.select(OriginKind.DERIVED), "ast_invalid")

        assertInvalid(service.materialize(draft, targetAssetId()), ProvenanceDraftErrorCode.INVALID_SOURCE_ASSET_ID)
    }

    @Test
    fun `derived rejects duplicate AssetIds`() {
        val repeated = "${sourceAssetId().value}\n${sourceAssetId().value}"
        val draft = service.setSourceAssetIds(service.select(OriginKind.DERIVED), repeated)

        assertInvalid(service.materialize(draft, targetAssetId()), ProvenanceDraftErrorCode.DUPLICATE_SOURCE_ASSET_ID)
    }

    @Test
    fun `unknown needs explicit confirmation`() {
        val selected = service.select(OriginKind.UNKNOWN)
        assertInvalid(service.materialize(selected, targetAssetId()), ProvenanceDraftErrorCode.UNKNOWN_NOT_CONFIRMED)

        val confirmed = service.materialize(service.setUnknownConfirmed(selected, true), targetAssetId()).valid()
        assertEquals(OriginKind.UNKNOWN, confirmed.originKind)

        val unconfirmed = service.setUnknownConfirmed(service.setUnknownConfirmed(selected, true), false)
        assertInvalid(service.materialize(unconfirmed, targetAssetId()), ProvenanceDraftErrorCode.UNKNOWN_NOT_CONFIRMED)
    }

    @Test
    fun `changing generated to imported cannot leak generator fields`() {
        var generated = service.select(OriginKind.GENERATED)
        generated = service.setGeneratedProvider(generated, "provider-x")
        generated = service.setGeneratedModel(generated, "model-x")
        generated = service.useGeneratedAt(generated, Instant.parse("2026-09-14T10:00:00Z"))

        val imported = service.materialize(service.select(OriginKind.IMPORTED), targetAssetId()).valid()

        assertEquals(OriginKind.IMPORTED, imported.originKind)
        assertNull(imported.generator)
    }

    @Test
    fun `changing edited to generated cannot leak source AssetIds`() {
        var edited = service.select(OriginKind.EDITED)
        edited = service.setSourceAssetIds(edited, sourceAssetId().value)
        assertTrue(service.materialize(edited, targetAssetId()) is ProvenanceMaterialization.Valid)

        var generated = service.select(OriginKind.GENERATED)
        generated = service.setGeneratedProvider(generated, "provider-x")
        generated = service.useGeneratedAt(generated, Instant.parse("2026-09-14T10:00:00Z"))
        val provenance = service.materialize(generated, targetAssetId()).valid()

        assertNull(provenance.sourceAssetIds)
    }

    @Test
    fun `materialization produces canonical Provenance accepted by AssetValidator`() {
        var draft = service.select(OriginKind.GENERATED)
        draft = service.setGeneratedProvider(draft, "provider-independent")
        draft = service.useGeneratedAt(draft, Instant.parse("2026-09-14T10:00:00Z"))
        val asset = Asset(
            schemaVersion = 1,
            assetId = targetAssetId(),
            type = AssetType.NPC_PORTRAIT,
            lifecycle = Lifecycle(LifecycleStatus.DRAFT),
            content = Content("image/png", 1, 1, 1, "a".repeat(64)),
            provenance = service.materialize(draft, targetAssetId()).valid(),
        )

        assertTrue(AssetValidator.validate(asset).isEmpty())
    }

    private fun assertInvalid(result: ProvenanceMaterialization, code: ProvenanceDraftErrorCode) {
        assertTrue(result is ProvenanceMaterialization.Invalid)
        assertTrue((result as ProvenanceMaterialization.Invalid).errors.any { it.code == code })
    }

    private fun ProvenanceMaterialization.valid() = (this as ProvenanceMaterialization.Valid).provenance

    private fun sourceAssetId() = AssetId.parse("ast_01991d80-1000-7000-8000-000000000001")
    private fun targetAssetId() = AssetId.parse("ast_01991d80-1000-7000-8000-000000000002")
}

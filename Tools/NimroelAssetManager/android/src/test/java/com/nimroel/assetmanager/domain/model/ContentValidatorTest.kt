package com.nimroel.assetmanager.domain.model

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class ContentValidatorTest {
    @Test
    fun `accepts valid prepared image content`() {
        assertTrue(ContentValidator.validate(validContent()).isEmpty())
    }

    @Test
    fun `rejects invalid MIME dimensions byte size and hash`() {
        val errors = ContentValidator.validate(
            validContent().copy(
                mimeType = "application/octet-stream",
                widthPx = 0,
                heightPx = -1,
                byteSize = 0,
                sha256 = "ABC",
            ),
        )

        assertEquals(3, errors.size)
        assertTrue(errors.any { it.contains("mimeType") })
        assertTrue(errors.any { it.contains("positive") })
        assertTrue(errors.any { it.contains("lowercase hexadecimal") })
    }

    @Test
    fun `AssetValidator delegates unchanged Content rules`() {
        val asset = validAsset().copy(content = validContent().copy(sha256 = "A".repeat(64)))

        assertEquals(ContentValidator.validate(asset.content), AssetValidator.validate(asset))
    }

    private fun validContent() = Content(
        mimeType = "image/png",
        widthPx = 2,
        heightPx = 3,
        byteSize = 71,
        sha256 = "a".repeat(64),
    )

    private fun validAsset() = Asset(
        schemaVersion = 1,
        assetId = AssetId.parse("ast_019c1a23-4567-7abc-8def-0123456789ab"),
        type = AssetType.NPC_PORTRAIT,
        lifecycle = Lifecycle(LifecycleStatus.DRAFT),
        content = validContent(),
        provenance = Provenance(OriginKind.IMPORTED),
    )
}

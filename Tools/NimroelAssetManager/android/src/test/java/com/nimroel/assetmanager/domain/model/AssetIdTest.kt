package com.nimroel.assetmanager.domain.model

import org.junit.Assert.assertEquals
import org.junit.Test

class AssetIdTest {
    @Test
    fun `keeps a stable logical ID value`() {
        val assetId = AssetId.parse("ast_019c1a23-4567-7abc-8def-0123456789ab")

        assertEquals("ast_019c1a23-4567-7abc-8def-0123456789ab", assetId.value)
    }

    @Test(expected = IllegalArgumentException::class)
    fun `rejects blank IDs`() {
        AssetId.parse("   ")
    }
}

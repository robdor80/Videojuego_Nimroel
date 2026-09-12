package com.nimroel.assetmanager.domain.model

import org.junit.Assert.assertEquals
import org.junit.Test

class AssetIdTest {
    @Test
    fun `keeps a stable logical ID value`() {
        val assetId = AssetId("pending-convention-001")

        assertEquals("pending-convention-001", assetId.value)
    }

    @Test(expected = IllegalArgumentException::class)
    fun `rejects blank IDs`() {
        AssetId("   ")
    }
}

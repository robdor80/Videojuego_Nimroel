package com.nimroel.assetmanager.data.local

import com.nimroel.assetmanager.domain.storage.AssetAvailability
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant
import org.junit.Assert.assertEquals
import org.junit.Assert.assertThrows
import org.junit.Test

class LocalPersistenceConvertersTest {
    private val converters = LocalPersistenceConverters()

    @Test
    fun `operational enums use stable wire values and round trip`() {
        assertEquals("available", converters.assetAvailabilityToWire(AssetAvailability.AVAILABLE))
        assertEquals(AssetAvailability.DEGRADED, converters.assetAvailabilityFromWire("degraded"))
        assertEquals("source_original", converters.representationRoleToWire(RepresentationRole.SOURCE_ORIGINAL))
        assertEquals(RepresentationAvailability.CORRUPT, converters.representationAvailabilityFromWire("corrupt"))
        assertEquals("ready_to_commit", converters.ingestWorkStateToWire(IngestWorkState.READY_TO_COMMIT))
    }

    @Test
    fun `unknown enum wire values fail clearly`() {
        assertThrows(IllegalArgumentException::class.java) { converters.ingestWorkStateFromWire("uploaded") }
    }

    @Test
    fun `timestamps use UTC epoch milliseconds`() {
        val instant = Instant.parse("2026-09-13T12:34:56.789Z")
        val stored = converters.instantToEpochMillis(instant)
        assertEquals(1_789_302_896_789L, stored)
        assertEquals(instant, converters.instantFromEpochMillis(stored))
    }
}

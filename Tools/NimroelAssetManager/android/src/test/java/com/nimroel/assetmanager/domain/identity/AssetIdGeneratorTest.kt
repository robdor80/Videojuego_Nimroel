package com.nimroel.assetmanager.domain.identity

import com.nimroel.assetmanager.domain.model.AssetId
import java.time.Clock
import java.time.Instant
import java.time.ZoneOffset
import java.util.UUID
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class AssetIdGeneratorTest {
    private val clock = Clock.fixed(Instant.parse("2026-09-14T12:34:56.789Z"), ZoneOffset.UTC)

    @Test
    fun `generated identity satisfies AssetId parse and uses lowercase canonical form`() {
        val generated = UuidV7AssetIdGenerator(clock, FixedRandom(0xAB)).generate()

        assertEquals(generated, AssetId.parse(generated.value))
        assertEquals(generated.value.lowercase(), generated.value)
        assertTrue(generated.value.startsWith("ast_"))
    }

    @Test
    fun `generated UUID has version 7 and RFC variant`() {
        val generated = UuidV7AssetIdGenerator(clock, FixedRandom(0x42)).generate()
        val uuid = UUID.fromString(generated.value.removePrefix("ast_"))

        assertEquals(7, uuid.version())
        assertEquals(2, uuid.variant())
    }

    @Test
    fun `sequential generations never reuse the same identity`() {
        val generator = UuidV7AssetIdGenerator(clock, IncrementingRandom())

        assertNotEquals(generator.generate(), generator.generate())
    }

    @Test
    fun `controlled Clock and random bytes make generation deterministic`() {
        val first = UuidV7AssetIdGenerator(clock, FixedRandom(0x11)).generate()
        val second = UuidV7AssetIdGenerator(clock, FixedRandom(0x11)).generate()

        assertEquals(first, second)
        val timestampHex = clock.instant().toEpochMilli().toString(16).padStart(12, '0')
        assertEquals(timestampHex, first.value.removePrefix("ast_").replace("-", "").take(12))
    }

    private class FixedRandom(private val value: Int) : RandomBytesSource {
        override fun nextBytes(destination: ByteArray) = destination.fill(value.toByte())
    }

    private class IncrementingRandom : RandomBytesSource {
        private var next = 0
        override fun nextBytes(destination: ByteArray) {
            destination.fill(next++.toByte())
        }
    }
}

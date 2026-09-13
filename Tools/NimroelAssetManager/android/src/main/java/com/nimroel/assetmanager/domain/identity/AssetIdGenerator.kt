package com.nimroel.assetmanager.domain.identity

import com.nimroel.assetmanager.domain.model.AssetId
import java.security.SecureRandom
import java.time.Clock
import java.time.Instant
import java.util.UUID

fun interface AssetIdGenerator {
    fun generate(): AssetId
}

fun interface RandomBytesSource {
    fun nextBytes(destination: ByteArray)
}

class SecureRandomBytesSource(
    private val secureRandom: SecureRandom = SecureRandom(),
) : RandomBytesSource {
    override fun nextBytes(destination: ByteArray) = secureRandom.nextBytes(destination)
}

/** Small RFC 9562 UUIDv7 generator: 48-bit Unix milliseconds plus 74 cryptographic random bits. */
class UuidV7AssetIdGenerator(
    private val clock: Clock = Clock.systemUTC(),
    private val random: RandomBytesSource = SecureRandomBytesSource(),
) : AssetIdGenerator {
    override fun generate(): AssetId {
        val timestamp = Instant.now(clock).toEpochMilli()
        require(timestamp in 0..MAX_UUID_V7_TIMESTAMP) { "UUIDv7 timestamp is outside its 48-bit range." }
        val randomBytes = ByteArray(10).also(random::nextBytes)
        val bytes = ByteArray(16)
        for (index in 0 until 6) {
            bytes[index] = (timestamp ushr (40 - index * 8)).toByte()
        }
        bytes[6] = (0x70 or (randomBytes[0].toInt() and 0x0f)).toByte()
        bytes[7] = randomBytes[1]
        bytes[8] = (0x80 or (randomBytes[2].toInt() and 0x3f)).toByte()
        randomBytes.copyInto(bytes, destinationOffset = 9, startIndex = 3)
        return AssetId.parse("ast_${bytes.toCanonicalUuidString()}")
    }

    private companion object {
        const val MAX_UUID_V7_TIMESTAMP = 0xffffffffffffL
    }
}

fun interface WorkIdGenerator {
    fun generate(): String
}

class RandomUuidWorkIdGenerator : WorkIdGenerator {
    override fun generate(): String = UUID.randomUUID().toString()
}

private fun ByteArray.toCanonicalUuidString(): String = buildString(36) {
    this@toCanonicalUuidString.forEachIndexed { index, byte ->
        if (index == 4 || index == 6 || index == 8 || index == 10) append('-')
        append(HEX[(byte.toInt() ushr 4) and 0x0f])
        append(HEX[byte.toInt() and 0x0f])
    }
}

private const val HEX = "0123456789abcdef"

package com.nimroel.assetmanager.data.local

import androidx.room.TypeConverter
import com.nimroel.assetmanager.domain.storage.AssetAvailability
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.RepresentationAvailability
import com.nimroel.assetmanager.domain.storage.RepresentationRole
import java.time.Instant

internal class LocalPersistenceConverters {
    @TypeConverter fun assetAvailabilityToWire(value: AssetAvailability): String = value.wireValue
    @TypeConverter fun assetAvailabilityFromWire(value: String): AssetAvailability = AssetAvailability.fromWireValue(value)

    @TypeConverter fun representationRoleToWire(value: RepresentationRole): String = value.wireValue
    @TypeConverter fun representationRoleFromWire(value: String): RepresentationRole = RepresentationRole.fromWireValue(value)

    @TypeConverter fun representationAvailabilityToWire(value: RepresentationAvailability): String = value.wireValue
    @TypeConverter fun representationAvailabilityFromWire(value: String): RepresentationAvailability = RepresentationAvailability.fromWireValue(value)

    @TypeConverter fun ingestWorkStateToWire(value: IngestWorkState): String = value.wireValue
    @TypeConverter fun ingestWorkStateFromWire(value: String): IngestWorkState = IngestWorkState.fromWireValue(value)

    /** All operational timestamps are stored as UTC Unix epoch milliseconds. */
    @TypeConverter fun instantToEpochMillis(value: Instant?): Long? = value?.toEpochMilli()
    @TypeConverter fun instantFromEpochMillis(value: Long?): Instant? = value?.let(Instant::ofEpochMilli)
}

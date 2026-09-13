package com.nimroel.assetmanager.data.local

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.TypeConverters
import com.nimroel.assetmanager.domain.storage.LocalAssetStore

internal const val ROOM_DATABASE_VERSION = 1

@Database(
    entities = [
        AssetDocumentEntity::class,
        AssetLocalStateEntity::class,
        LocalRepresentationEntity::class,
        IngestWorkItemEntity::class,
    ],
    version = ROOM_DATABASE_VERSION,
    exportSchema = true,
)
@TypeConverters(LocalPersistenceConverters::class)
internal abstract class NimroelAssetDatabase : RoomDatabase() {
    abstract fun assetDocuments(): AssetDocumentDao
    abstract fun assetLocalStates(): AssetLocalStateDao
    abstract fun localRepresentations(): LocalRepresentationDao
    abstract fun ingestWorkItems(): IngestWorkItemDao

    companion object {
        const val VERSION = ROOM_DATABASE_VERSION
        const val DATABASE_NAME = "nimroel-assets.db"
    }
}

/** Composition-root entry point. Callers receive the domain store, never Room entities. */
object LocalAssetStoreFactory {
    fun create(context: Context): LocalAssetStore {
        val database = Room.databaseBuilder(
            context.applicationContext,
            NimroelAssetDatabase::class.java,
            NimroelAssetDatabase.DATABASE_NAME,
        ).build()
        return RoomLocalAssetStore(database)
    }
}

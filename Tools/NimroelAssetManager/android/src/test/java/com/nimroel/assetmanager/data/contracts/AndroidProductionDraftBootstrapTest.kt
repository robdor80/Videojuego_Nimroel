package com.nimroel.assetmanager.data.contracts

import android.content.Context
import androidx.test.core.app.ApplicationProvider
import com.nimroel.assetmanager.domain.contracts.ProductionFieldPaths
import com.nimroel.assetmanager.ui.AssetManagerUiState
import com.nimroel.assetmanager.ui.AssetManagerViewModel
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.annotation.Config
import org.robolectric.RobolectricTestRunner

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [35])
class AndroidProductionDraftBootstrapTest {
    @Test
    fun `loads the real pilot contracts from packaged Android assets`() {
        val context = ApplicationProvider.getApplicationContext<Context>()

        val environment = AndroidProductionDraftBootstrap(context.assets).load()

        assertEquals("npc-portrait-pilot", environment.draft.presetId)
        assertEquals("1.0", environment.draft.presetVersion)
        assertEquals("NPC portrait pilot", environment.presetLabel)
        assertEquals("nimroel-npc-pilot", environment.draft.vocabularySetId)
        assertEquals("1.0", environment.draft.vocabularySetVersion)
        assertEquals(
            "Adult",
            environment.service.availableValues(environment.draft, ProductionFieldPaths.SUBJECT_AGE_BAND_ID).single().label,
        )
        assertTrue(ProductionFieldPaths.SUBJECT_SPECIES_ID !in environment.service.boundVocabularyFieldPaths(environment.draft))

        val state = AssetManagerViewModel(ProductionDraftBootstrap { environment }).uiState as AssetManagerUiState.Ready
        assertEquals(listOf("Adult", "Neutral"), state.fields.map { it.selectedValueLabel })
    }
}

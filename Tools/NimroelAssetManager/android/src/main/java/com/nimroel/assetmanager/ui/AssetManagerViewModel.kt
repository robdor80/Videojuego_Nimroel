package com.nimroel.assetmanager.ui

import androidx.lifecycle.ViewModel
import com.nimroel.assetmanager.domain.model.LocalAssetState

data class AssetManagerUiState(
    val title: String = "Nimroel Asset Manager",
    val localState: LocalAssetState = LocalAssetState.DRAFT,
)

class AssetManagerViewModel : ViewModel() {
    val uiState = AssetManagerUiState()
}

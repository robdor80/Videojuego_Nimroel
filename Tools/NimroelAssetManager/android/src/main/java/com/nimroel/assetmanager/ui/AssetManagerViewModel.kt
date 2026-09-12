package com.nimroel.assetmanager.ui

import androidx.lifecycle.ViewModel

data class AssetManagerUiState(
    val title: String = "Nimroel Asset Manager",
)

class AssetManagerViewModel : ViewModel() {
    val uiState = AssetManagerUiState()
}

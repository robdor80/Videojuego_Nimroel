package com.nimroel.assetmanager

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.enableEdgeToEdge
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.lifecycle.viewmodel.compose.viewModel
import com.nimroel.assetmanager.domain.processing.ImageSourceRef
import com.nimroel.assetmanager.ui.AssetManagerApp
import com.nimroel.assetmanager.ui.AssetManagerViewModel
import com.nimroel.assetmanager.ui.theme.NimroelAssetManagerTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            NimroelAssetManagerTheme {
                val viewModel: AssetManagerViewModel = viewModel(
                    factory = AssetManagerViewModel.factory(applicationContext),
                )
                val imagePicker = rememberLauncherForActivityResult(ActivityResultContracts.GetContent()) { uri ->
                    viewModel.selectImage(uri?.let { ImageSourceRef(it.toString()) })
                }
                AssetManagerApp(
                    uiState = viewModel.uiState,
                    onSelectValue = viewModel::selectValue,
                    onClearSelection = viewModel::clearSelection,
                    onSelectImage = { imagePicker.launch("image/*") },
                    onRemoveImage = viewModel::removeImage,
                    onPrepareLocalIngest = viewModel::prepareLocalIngest,
                    onSelectProvenanceKind = viewModel::selectProvenanceKind,
                    onGeneratedProviderChange = viewModel::setGeneratedProvider,
                    onGeneratedModelChange = viewModel::setGeneratedModel,
                    onGeneratedAtChange = viewModel::setGeneratedAt,
                    onUseCurrentGeneratedAt = viewModel::useCurrentGeneratedAt,
                    onImportedAtChange = viewModel::setImportedAt,
                    onUseCurrentImportedAt = viewModel::useCurrentImportedAt,
                    onSourceAssetIdsChange = viewModel::setSourceAssetIds,
                    onUnknownConfirmedChange = viewModel::setUnknownConfirmed,
                )
            }
        }
    }
}

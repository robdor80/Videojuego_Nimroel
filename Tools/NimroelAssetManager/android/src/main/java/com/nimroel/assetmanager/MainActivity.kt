package com.nimroel.assetmanager

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.lifecycle.viewmodel.compose.viewModel
import com.nimroel.assetmanager.ui.AssetManagerApp
import com.nimroel.assetmanager.ui.AssetManagerViewModel
import com.nimroel.assetmanager.ui.theme.NimroelAssetManagerTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            NimroelAssetManagerTheme {
                val viewModel: AssetManagerViewModel = viewModel()
                AssetManagerApp(uiState = viewModel.uiState)
            }
        }
    }
}

package com.nimroel.assetmanager.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable

private val NimroelColors = darkColorScheme()

@Composable
fun NimroelAssetManagerTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = NimroelColors, content = content)
}

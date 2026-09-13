package com.nimroel.assetmanager.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ElevatedCard
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.ExposedDropdownMenuDefaults
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedCard
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.nimroel.assetmanager.domain.contracts.PresetValueMode
import com.nimroel.assetmanager.domain.model.AssetType
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.ui.theme.NimroelAssetManagerTheme

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AssetManagerApp(
    uiState: AssetManagerUiState,
    onSelectValue: (fieldPath: String, valueId: String) -> Unit = { _, _ -> },
    onClearSelection: (fieldPath: String) -> Unit = {},
) {
    Scaffold(
        topBar = {
            TopAppBar(title = { Text("Nimroel Asset Manager", fontWeight = FontWeight.SemiBold) })
        },
    ) { contentPadding ->
        when (uiState) {
            AssetManagerUiState.Loading -> LoadingContent(contentPadding)
            is AssetManagerUiState.Error -> ErrorContent(uiState.message, contentPadding)
            is AssetManagerUiState.Ready -> ReadyContent(
                state = uiState,
                contentPadding = contentPadding,
                onSelectValue = onSelectValue,
                onClearSelection = onClearSelection,
            )
        }
    }
}

@Composable
private fun LoadingContent(contentPadding: PaddingValues) {
    Box(
        modifier = Modifier.fillMaxSize().padding(contentPadding),
        contentAlignment = Alignment.Center,
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            CircularProgressIndicator()
            Text(
                text = "Cargando contratos de producción…",
                modifier = Modifier.padding(top = 16.dp),
                style = MaterialTheme.typography.bodyLarge,
            )
        }
    }
}

@Composable
private fun ErrorContent(message: String, contentPadding: PaddingValues) {
    Box(
        modifier = Modifier.fillMaxSize().padding(contentPadding).padding(24.dp),
        contentAlignment = Alignment.Center,
    ) {
        ElevatedCard(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(24.dp)) {
                Text("No se puede abrir la producción", style = MaterialTheme.typography.titleLarge)
                Text(
                    text = message,
                    modifier = Modifier.padding(top = 12.dp),
                    color = MaterialTheme.colorScheme.error,
                    style = MaterialTheme.typography.bodyMedium,
                )
            }
        }
    }
}

@Composable
private fun ReadyContent(
    state: AssetManagerUiState.Ready,
    contentPadding: PaddingValues,
    onSelectValue: (String, String) -> Unit,
    onClearSelection: (String) -> Unit,
) {
    BoxWithConstraints(modifier = Modifier.fillMaxSize().padding(contentPadding)) {
        if (maxWidth >= 840.dp) {
            Row(
                modifier = Modifier.fillMaxSize().padding(horizontal = 32.dp, vertical = 24.dp),
                horizontalArrangement = Arrangement.spacedBy(24.dp),
            ) {
                ProductionEditor(
                    state = state,
                    onSelectValue = onSelectValue,
                    onClearSelection = onClearSelection,
                    modifier = Modifier.weight(1.35f).fillMaxHeight().verticalScroll(rememberScrollState()),
                )
                DraftSummary(
                    state = state,
                    modifier = Modifier.weight(1f).fillMaxHeight().verticalScroll(rememberScrollState()),
                )
            }
        } else {
            Column(
                modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(20.dp),
            ) {
                ProductionEditor(state, onSelectValue, onClearSelection)
                DraftSummary(state)
            }
        }
    }
}

@Composable
private fun ProductionEditor(
    state: AssetManagerUiState.Ready,
    onSelectValue: (String, String) -> Unit,
    onClearSelection: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    Column(modifier = modifier, verticalArrangement = Arrangement.spacedBy(16.dp)) {
        Column {
            Text(state.screenTitle, style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.SemiBold)
            Text(
                text = state.screenSubtitle,
                modifier = Modifier.padding(top = 4.dp),
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                style = MaterialTheme.typography.titleMedium,
            )
        }
        PresetCard(state)
        Text("Selecciones", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
        state.fields.forEach { field ->
            ProductionFieldSelector(
                field = field,
                onSelectValue = { onSelectValue(field.fieldPath, it) },
                onClear = { onClearSelection(field.fieldPath) },
            )
        }
        state.actionError?.let { error ->
            Card(colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.errorContainer)) {
                Text(
                    text = error,
                    modifier = Modifier.fillMaxWidth().padding(16.dp),
                    color = MaterialTheme.colorScheme.onErrorContainer,
                    style = MaterialTheme.typography.bodyMedium,
                )
            }
        }
    }
}

@Composable
private fun PresetCard(state: AssetManagerUiState.Ready) {
    ElevatedCard(modifier = Modifier.fillMaxWidth()) {
        Column(modifier = Modifier.padding(18.dp)) {
            Text("Preset", style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
            Text(
                text = state.presetLabel,
                modifier = Modifier.padding(top = 4.dp),
                style = MaterialTheme.typography.titleMedium,
                fontWeight = FontWeight.Medium,
            )
            Text(
                text = "Las selecciones iniciales proceden del preset editorial versionado.",
                modifier = Modifier.padding(top = 8.dp),
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                style = MaterialTheme.typography.bodySmall,
            )
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ProductionFieldSelector(
    field: ProductionFieldUiState,
    onSelectValue: (String) -> Unit,
    onClear: () -> Unit,
) {
    OutlinedCard(modifier = Modifier.fillMaxWidth()) {
        Column(modifier = Modifier.padding(16.dp)) {
            Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Text(field.label, modifier = Modifier.weight(1f), style = MaterialTheme.typography.titleMedium)
                FieldStatus(field)
            }
            Spacer(Modifier.height(12.dp))
            if (field.isLocked) {
                OutlinedTextField(
                    value = field.selectedValueLabel.orEmpty(),
                    onValueChange = {},
                    modifier = Modifier.fillMaxWidth(),
                    enabled = false,
                    label = { Text("Valor") },
                    supportingText = { Text("Fijo por preset") },
                )
            } else {
                var expanded by remember(field.fieldPath) { mutableStateOf(false) }
                ExposedDropdownMenuBox(expanded = expanded, onExpandedChange = { expanded = !expanded }) {
                    OutlinedTextField(
                        value = field.selectedValueLabel ?: "Sin selección",
                        onValueChange = {},
                        modifier = Modifier.menuAnchor().fillMaxWidth(),
                        readOnly = true,
                        label = { Text("Valor") },
                        trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded) },
                        supportingText = {
                            Text(
                                when (field.source) {
                                    DraftSelectionSource.OPERATOR -> "Seleccionado por el operador"
                                    DraftSelectionSource.PRESET -> "Sugerido por preset"
                                    null -> "Selecciona un valor"
                                },
                            )
                        },
                    )
                    ExposedDropdownMenu(
                        expanded = expanded,
                        onDismissRequest = { expanded = false },
                    ) {
                        field.values.forEach { value ->
                            DropdownMenuItem(
                                text = {
                                    Column {
                                        Text(value.label)
                                        if (value.isDeprecated) {
                                            Text(
                                                "Obsoleto",
                                                color = MaterialTheme.colorScheme.error,
                                                style = MaterialTheme.typography.labelSmall,
                                            )
                                        }
                                    }
                                },
                                onClick = {
                                    expanded = false
                                    onSelectValue(value.valueId)
                                },
                            )
                        }
                    }
                }
                if (field.canClear) {
                    TextButton(onClick = onClear, modifier = Modifier.align(Alignment.End)) {
                        Text("Eliminar selección")
                    }
                }
            }
            if (field.selectedValueDeprecated) {
                Text(
                    "El valor seleccionado está obsoleto; se conserva para revisión editorial.",
                    color = MaterialTheme.colorScheme.error,
                    style = MaterialTheme.typography.bodySmall,
                )
            }
        }
    }
}

@Composable
private fun FieldStatus(field: ProductionFieldUiState) {
    val (label, emphasized) = when {
        field.isLocked -> "Fijo" to false
        field.source == DraftSelectionSource.OPERATOR -> "Operador" to true
        field.presetMode == PresetValueMode.SUGGESTED -> "Sugerido" to false
        else -> "Editable" to false
    }
    Surface(
        color = if (emphasized) MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surfaceVariant,
        shape = MaterialTheme.shapes.small,
    ) {
        Text(label, modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp), style = MaterialTheme.typography.labelMedium)
    }
}

@Composable
private fun DraftSummary(state: AssetManagerUiState.Ready, modifier: Modifier = Modifier) {
    Column(modifier = modifier, verticalArrangement = Arrangement.spacedBy(16.dp)) {
        ElevatedCard(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(20.dp)) {
                Text("Resumen del borrador", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                Spacer(Modifier.height(16.dp))
                MetadataRow("Tipo de Asset", state.assetTypeLabel)
                MetadataRow("Preset", state.presetLabel)
                MetadataRow("Vocabulary Set", "${state.vocabularySetId} · ${state.vocabularySetVersion}")
                MetadataRow("Selecciones activas", state.summary.activeSelectionCount.toString())
                HorizontalDivider(modifier = Modifier.padding(vertical = 16.dp))
                if (state.summary.selections.isEmpty()) {
                    Text("Aún no hay valores seleccionados.", color = MaterialTheme.colorScheme.onSurfaceVariant)
                } else {
                    state.summary.selections.forEach { selection ->
                        Row(
                            modifier = Modifier.fillMaxWidth().padding(vertical = 6.dp),
                            horizontalArrangement = Arrangement.SpaceBetween,
                        ) {
                            Text(selection.fieldLabel, color = MaterialTheme.colorScheme.onSurfaceVariant)
                            Column(horizontalAlignment = Alignment.End) {
                                Text(selection.valueLabel, fontWeight = FontWeight.Medium)
                                if (selection.isDeprecated) {
                                    Text("Obsoleto", color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.labelSmall)
                                }
                            }
                        }
                    }
                }
            }
        }
        OutlinedCard(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(20.dp)) {
                Text("Metadata técnica", style = MaterialTheme.typography.titleMedium)
                Spacer(Modifier.height(12.dp))
                MetadataRow("Preset", "${state.presetId} · ${state.presetVersion}")
                MetadataRow("Vocabulary Set", "${state.vocabularySetId} · ${state.vocabularySetVersion}")
            }
        }
        Button(onClick = {}, enabled = false, modifier = Modifier.fillMaxWidth()) {
            Text("Continuar con imagen")
        }
        Text(
            "La importación de imagen se añadirá en el siguiente paso del flujo.",
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            style = MaterialTheme.typography.bodySmall,
        )
    }
}

@Composable
private fun MetadataRow(label: String, value: String) {
    Row(modifier = Modifier.fillMaxWidth().padding(vertical = 5.dp)) {
        Text(label, modifier = Modifier.weight(1f), color = MaterialTheme.colorScheme.onSurfaceVariant)
        Spacer(Modifier.width(16.dp))
        Text(value, fontWeight = FontWeight.Medium)
    }
}

private val previewState = AssetManagerUiState.Ready(
    screenTitle = "Nueva producción",
    screenSubtitle = "Retrato de PNJ",
    presetLabel = "NPC portrait pilot",
    presetId = "preview-preset",
    presetVersion = "1.0",
    assetType = AssetType.NPC_PORTRAIT,
    assetTypeLabel = "Retrato de PNJ",
    vocabularySetId = "preview-set",
    vocabularySetVersion = "1.0",
    fields = listOf(
        ProductionFieldUiState(
            fieldPath = "subject.ageBandId",
            label = "Rango de edad",
            selectedValueId = "adult",
            selectedValueLabel = "Adulto",
            selectedValueDeprecated = false,
            values = listOf(VocabularyValueUiState("adult", "Adulto", null, false)),
            presetMode = PresetValueMode.FIXED,
            source = DraftSelectionSource.PRESET,
            isLocked = true,
            isEditable = false,
            canClear = false,
        ),
        ProductionFieldUiState(
            fieldPath = "visual.expressionId",
            label = "Expresión",
            selectedValueId = "neutral",
            selectedValueLabel = "Neutral",
            selectedValueDeprecated = false,
            values = listOf(VocabularyValueUiState("neutral", "Neutral", null, false)),
            presetMode = PresetValueMode.SUGGESTED,
            source = DraftSelectionSource.OPERATOR,
            isLocked = false,
            isEditable = true,
            canClear = true,
        ),
    ),
    summary = ProductionDraftSummaryUiState(
        activeSelectionCount = 2,
        selections = listOf(
            ProductionSummarySelectionUiState("Rango de edad", "Adulto", false),
            ProductionSummarySelectionUiState("Expresión", "Neutral", false),
        ),
    ),
)

@Preview(name = "Nueva producción · móvil", widthDp = 412, heightDp = 915, showBackground = true)
@Composable
private fun NewProductionMobilePreview() {
    NimroelAssetManagerTheme { AssetManagerApp(previewState) }
}

@Preview(name = "Nueva producción · tablet", widthDp = 1280, heightDp = 800, showBackground = true)
@Composable
private fun NewProductionTabletPreview() {
    NimroelAssetManagerTheme { AssetManagerApp(previewState) }
}

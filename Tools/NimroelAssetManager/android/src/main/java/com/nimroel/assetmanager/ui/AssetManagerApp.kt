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
import androidx.compose.foundation.text.selection.SelectionContainer
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Checkbox
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
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.model.OriginKind
import com.nimroel.assetmanager.domain.production.DraftSelectionSource
import com.nimroel.assetmanager.ui.theme.NimroelAssetManagerTheme

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AssetManagerApp(
    uiState: AssetManagerUiState,
    onSelectValue: (fieldPath: String, valueId: String) -> Unit = { _, _ -> },
    onClearSelection: (fieldPath: String) -> Unit = {},
    onSelectImage: () -> Unit = {},
    onRemoveImage: () -> Unit = {},
    onPrepareLocalIngest: () -> Unit = {},
    onSelectProvenanceKind: (OriginKind) -> Unit = {},
    onGeneratedProviderChange: (String) -> Unit = {},
    onGeneratedModelChange: (String) -> Unit = {},
    onGeneratedAtChange: (String) -> Unit = {},
    onUseCurrentGeneratedAt: () -> Unit = {},
    onImportedAtChange: (String) -> Unit = {},
    onUseCurrentImportedAt: () -> Unit = {},
    onSourceAssetIdsChange: (String) -> Unit = {},
    onUnknownConfirmedChange: (Boolean) -> Unit = {},
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
                onSelectImage = onSelectImage,
                onRemoveImage = onRemoveImage,
                onPrepareLocalIngest = onPrepareLocalIngest,
                onSelectProvenanceKind = onSelectProvenanceKind,
                onGeneratedProviderChange = onGeneratedProviderChange,
                onGeneratedModelChange = onGeneratedModelChange,
                onGeneratedAtChange = onGeneratedAtChange,
                onUseCurrentGeneratedAt = onUseCurrentGeneratedAt,
                onImportedAtChange = onImportedAtChange,
                onUseCurrentImportedAt = onUseCurrentImportedAt,
                onSourceAssetIdsChange = onSourceAssetIdsChange,
                onUnknownConfirmedChange = onUnknownConfirmedChange,
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
    onSelectImage: () -> Unit,
    onRemoveImage: () -> Unit,
    onPrepareLocalIngest: () -> Unit,
    onSelectProvenanceKind: (OriginKind) -> Unit,
    onGeneratedProviderChange: (String) -> Unit,
    onGeneratedModelChange: (String) -> Unit,
    onGeneratedAtChange: (String) -> Unit,
    onUseCurrentGeneratedAt: () -> Unit,
    onImportedAtChange: (String) -> Unit,
    onUseCurrentImportedAt: () -> Unit,
    onSourceAssetIdsChange: (String) -> Unit,
    onUnknownConfirmedChange: (Boolean) -> Unit,
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
                    onSelectImage = onSelectImage,
                    onRemoveImage = onRemoveImage,
                    onPrepareLocalIngest = onPrepareLocalIngest,
                    onSelectProvenanceKind = onSelectProvenanceKind,
                    onGeneratedProviderChange = onGeneratedProviderChange,
                    onGeneratedModelChange = onGeneratedModelChange,
                    onGeneratedAtChange = onGeneratedAtChange,
                    onUseCurrentGeneratedAt = onUseCurrentGeneratedAt,
                    onImportedAtChange = onImportedAtChange,
                    onUseCurrentImportedAt = onUseCurrentImportedAt,
                    onSourceAssetIdsChange = onSourceAssetIdsChange,
                    onUnknownConfirmedChange = onUnknownConfirmedChange,
                    modifier = Modifier.weight(1f).fillMaxHeight().verticalScroll(rememberScrollState()),
                )
            }
        } else {
            Column(
                modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(20.dp),
            ) {
                ProductionEditor(state, onSelectValue, onClearSelection)
                DraftSummary(
                    state,
                    onSelectImage,
                    onRemoveImage,
                    onPrepareLocalIngest,
                    onSelectProvenanceKind,
                    onGeneratedProviderChange,
                    onGeneratedModelChange,
                    onGeneratedAtChange,
                    onUseCurrentGeneratedAt,
                    onImportedAtChange,
                    onUseCurrentImportedAt,
                    onSourceAssetIdsChange,
                    onUnknownConfirmedChange,
                )
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
private fun DraftSummary(
    state: AssetManagerUiState.Ready,
    onSelectImage: () -> Unit,
    onRemoveImage: () -> Unit,
    onPrepareLocalIngest: () -> Unit,
    onSelectProvenanceKind: (OriginKind) -> Unit,
    onGeneratedProviderChange: (String) -> Unit,
    onGeneratedModelChange: (String) -> Unit,
    onGeneratedAtChange: (String) -> Unit,
    onUseCurrentGeneratedAt: () -> Unit,
    onImportedAtChange: (String) -> Unit,
    onUseCurrentImportedAt: () -> Unit,
    onSourceAssetIdsChange: (String) -> Unit,
    onUnknownConfirmedChange: (Boolean) -> Unit,
    modifier: Modifier = Modifier,
) {
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
        ImagePreparationCard(
            state = state.imageState,
            onSelectImage = onSelectImage,
            onRemoveImage = onRemoveImage,
            imageLocked = state.localIngestState is LocalIngestUiState.Processing ||
                state.localIngestState is LocalIngestUiState.Ready,
        )
        LocalIngestCard(state.imageState, state.localIngestState, onPrepareLocalIngest)
        if (state.provenanceState !is ProvenanceUiState.Unavailable) {
            ProvenanceCard(
                state = state.provenanceState,
                onSelectKind = onSelectProvenanceKind,
                onProviderChange = onGeneratedProviderChange,
                onModelChange = onGeneratedModelChange,
                onGeneratedAtChange = onGeneratedAtChange,
                onUseCurrentGeneratedAt = onUseCurrentGeneratedAt,
                onImportedAtChange = onImportedAtChange,
                onUseCurrentImportedAt = onUseCurrentImportedAt,
                onSourceAssetIdsChange = onSourceAssetIdsChange,
                onUnknownConfirmedChange = onUnknownConfirmedChange,
            )
        }
        Button(onClick = {}, enabled = state.isAssetCreationEnabled, modifier = Modifier.fillMaxWidth()) {
            Text("Crear borrador de Asset")
        }
        Text(
            state.assetCreationExplanation,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            style = MaterialTheme.typography.bodySmall,
        )
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ProvenanceCard(
    state: ProvenanceUiState,
    onSelectKind: (OriginKind) -> Unit,
    onProviderChange: (String) -> Unit,
    onModelChange: (String) -> Unit,
    onGeneratedAtChange: (String) -> Unit,
    onUseCurrentGeneratedAt: () -> Unit,
    onImportedAtChange: (String) -> Unit,
    onUseCurrentImportedAt: () -> Unit,
    onSourceAssetIdsChange: (String) -> Unit,
    onUnknownConfirmedChange: (Boolean) -> Unit,
) {
    val form = when (state) {
        is ProvenanceUiState.Invalid -> state.form
        is ProvenanceUiState.Valid -> state.form
        ProvenanceUiState.NotSpecified, ProvenanceUiState.Unavailable -> null
    }
    ElevatedCard(modifier = Modifier.fillMaxWidth()) {
        Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                Text("Procedencia", modifier = Modifier.weight(1f), style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                Surface(color = MaterialTheme.colorScheme.surfaceVariant, shape = MaterialTheme.shapes.small) {
                    Text(
                        when (state) {
                            ProvenanceUiState.NotSpecified -> "Sin especificar"
                            is ProvenanceUiState.Invalid -> "Revisar"
                            is ProvenanceUiState.Valid -> "Válida"
                            ProvenanceUiState.Unavailable -> "No disponible"
                        },
                        modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp),
                        style = MaterialTheme.typography.labelMedium,
                    )
                }
            }
            Text(
                "Declara el origen real. La forma de seleccionar la imagen no determina su procedencia.",
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                style = MaterialTheme.typography.bodySmall,
            )
            var expanded by remember { mutableStateOf(false) }
            ExposedDropdownMenuBox(expanded = expanded, onExpandedChange = { expanded = !expanded }) {
                OutlinedTextField(
                    value = form?.originKind?.displayLabel() ?: "Sin especificar",
                    onValueChange = {},
                    modifier = Modifier.menuAnchor().fillMaxWidth(),
                    readOnly = true,
                    label = { Text("Tipo de procedencia") },
                    trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded) },
                )
                ExposedDropdownMenu(expanded = expanded, onDismissRequest = { expanded = false }) {
                    OriginKind.entries.forEach { kind ->
                        DropdownMenuItem(
                            text = { Text(kind.displayLabel()) },
                            onClick = {
                                expanded = false
                                onSelectKind(kind)
                            },
                        )
                    }
                }
            }

            when (form?.originKind) {
                OriginKind.GENERATED -> {
                    OutlinedTextField(
                        value = form.provider,
                        onValueChange = onProviderChange,
                        modifier = Modifier.fillMaxWidth(),
                        label = { Text("Proveedor *") },
                        supportingText = { Text("ID contractual, por ejemplo el proveedor realmente utilizado") },
                        singleLine = true,
                    )
                    OutlinedTextField(
                        value = form.model,
                        onValueChange = onModelChange,
                        modifier = Modifier.fillMaxWidth(),
                        label = { Text("Modelo") },
                        singleLine = true,
                    )
                    InstantField(
                        value = form.generatedAt,
                        label = "Fecha/hora de generación *",
                        onValueChange = onGeneratedAtChange,
                        onUseCurrent = onUseCurrentGeneratedAt,
                    )
                }
                OriginKind.IMPORTED -> InstantField(
                    value = form.importedAt,
                    label = "Fecha/hora de importación",
                    onValueChange = onImportedAtChange,
                    onUseCurrent = onUseCurrentImportedAt,
                )
                OriginKind.EDITED, OriginKind.DERIVED -> OutlinedTextField(
                    value = form.sourceAssetIds,
                    onValueChange = onSourceAssetIdsChange,
                    modifier = Modifier.fillMaxWidth(),
                    label = { Text("Assets de origen *") },
                    supportingText = { Text("Un AssetId ast_… por línea") },
                    minLines = 2,
                )
                OriginKind.UNKNOWN -> Row(verticalAlignment = Alignment.CenterVertically) {
                    Checkbox(checked = form.unknownConfirmed, onCheckedChange = onUnknownConfirmedChange)
                    Text("Confirmo que la procedencia real es desconocida", modifier = Modifier.weight(1f))
                }
                null -> Unit
            }

            if (state is ProvenanceUiState.Invalid) {
                state.errors.forEach { error ->
                    Text(error, color = MaterialTheme.colorScheme.error, style = MaterialTheme.typography.bodySmall)
                }
            }
        }
    }
}

@Composable
private fun InstantField(
    value: String,
    label: String,
    onValueChange: (String) -> Unit,
    onUseCurrent: () -> Unit,
) {
    OutlinedTextField(
        value = value,
        onValueChange = onValueChange,
        modifier = Modifier.fillMaxWidth(),
        label = { Text(label) },
        supportingText = { Text("ISO-8601, por ejemplo 2026-09-14T10:00:00Z") },
        singleLine = true,
    )
    TextButton(onClick = onUseCurrent, modifier = Modifier.fillMaxWidth()) {
        Text("Usar fecha y hora actual")
    }
}

private fun OriginKind.displayLabel(): String = when (this) {
    OriginKind.GENERATED -> "Generada"
    OriginKind.IMPORTED -> "Importada"
    OriginKind.EDITED -> "Editada"
    OriginKind.DERIVED -> "Derivada"
    OriginKind.UNKNOWN -> "Desconocida"
}

@Composable
private fun ImagePreparationCard(
    state: ImageUiState,
    onSelectImage: () -> Unit,
    onRemoveImage: () -> Unit,
    imageLocked: Boolean,
) {
    ElevatedCard(modifier = Modifier.fillMaxWidth()) {
        Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            when (state) {
                ImageUiState.NoImage -> {
                    Text("Imagen", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                    Text(
                        "Selecciona la imagen fuente para preparar su metadata de contenido.",
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                    Button(onClick = onSelectImage, modifier = Modifier.fillMaxWidth()) {
                        Text("Seleccionar imagen")
                    }
                }

                is ImageUiState.Processing -> {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        CircularProgressIndicator(modifier = Modifier.width(28.dp).height(28.dp))
                        Text(
                            "Analizando imagen…",
                            modifier = Modifier.padding(start = 14.dp),
                            style = MaterialTheme.typography.titleMedium,
                        )
                    }
                    state.previousPrepared?.let { previous ->
                        Text(
                            "La imagen preparada anterior se conserva hasta completar el nuevo análisis.",
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            style = MaterialTheme.typography.bodySmall,
                        )
                        PreparedImageMetadata(previous)
                    }
                    ImageActions(onSelectImage, onRemoveImage, enabled = !imageLocked)
                }

                is ImageUiState.Prepared -> {
                    Text("Imagen preparada", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                    PreparedImageMetadata(state.image)
                    ImageActions(onSelectImage, onRemoveImage, enabled = !imageLocked)
                }

                is ImageUiState.ImageError -> {
                    Text("No se pudo preparar la imagen", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                    Card(colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.errorContainer)) {
                        Text(
                            state.message,
                            modifier = Modifier.fillMaxWidth().padding(14.dp),
                            color = MaterialTheme.colorScheme.onErrorContainer,
                        )
                    }
                    state.previousPrepared?.let { previous ->
                        Text(
                            "La última imagen preparada sigue disponible.",
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            style = MaterialTheme.typography.bodySmall,
                        )
                        PreparedImageMetadata(previous)
                    }
                    ImageActions(
                        onSelectImage,
                        onRemoveImage,
                        canRemove = state.previousPrepared != null,
                        enabled = !imageLocked,
                    )
                }
            }
        }
    }
}

@Composable
private fun LocalIngestCard(
    imageState: ImageUiState,
    state: LocalIngestUiState,
    onPrepareLocalIngest: () -> Unit,
) {
    val hasPreparedImage = imageState is ImageUiState.Prepared ||
        (imageState is ImageUiState.ImageError && imageState.previousPrepared != null)
    when (state) {
        LocalIngestUiState.NotStarted -> if (hasPreparedImage) {
            Button(onClick = onPrepareLocalIngest, modifier = Modifier.fillMaxWidth()) {
                Text("Preparar ingestión local")
            }
        }

        LocalIngestUiState.Processing -> ElevatedCard(modifier = Modifier.fillMaxWidth()) {
            Row(
                modifier = Modifier.fillMaxWidth().padding(20.dp),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                CircularProgressIndicator(modifier = Modifier.width(28.dp).height(28.dp))
                Text(
                    "Copiando y verificando imagen…",
                    modifier = Modifier.padding(start = 14.dp),
                    style = MaterialTheme.typography.titleMedium,
                )
            }
        }

        is LocalIngestUiState.Ready -> ElevatedCard(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Ingestión local preparada", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.SemiBold)
                MetadataRow("AssetId reservado", state.reservedAssetId)
                MetadataRow("Estado", state.status)
                MetadataRow("Tipo MIME", state.content.mimeType)
                MetadataRow("Dimensiones", "${state.content.widthPx} × ${state.content.heightPx} px")
                MetadataRow("Tamaño", state.content.byteSize?.let(::formatByteSize) ?: "No disponible")
                MetadataRow("SHA-256", "${state.content.sha256.take(16)}…${state.content.sha256.takeLast(8)}")
                Text(
                    "Copia local privada verificada. Ya no depende del acceso posterior al URI externo.",
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    style = MaterialTheme.typography.bodySmall,
                )
            }
        }

        is LocalIngestUiState.Failed -> OutlinedCard(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(20.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Text("La ingestión local no se completó", style = MaterialTheme.typography.titleMedium)
                Text(state.message, color = MaterialTheme.colorScheme.error)
                Text("Código: ${state.errorCode}", style = MaterialTheme.typography.bodySmall)
                Button(onClick = onPrepareLocalIngest, enabled = hasPreparedImage, modifier = Modifier.fillMaxWidth()) {
                    Text("Reintentar ingestión local")
                }
            }
        }
    }
}

@Composable
private fun PreparedImageMetadata(image: PreparedImageUiState) {
    val content = image.content
    var showFullHash by remember(content.sha256) { mutableStateOf(false) }
    MetadataRow("Estado", "Preparada")
    MetadataRow("Tipo MIME", content.mimeType)
    MetadataRow("Dimensiones", "${content.widthPx} × ${content.heightPx} px")
    MetadataRow("Tamaño", content.byteSize?.let(::formatByteSize) ?: "No disponible")
    MetadataRow("SHA-256", if (showFullHash) "Completo" else "${content.sha256.take(16)}…${content.sha256.takeLast(8)}")
    if (showFullHash) {
        SelectionContainer {
            Text(
                content.sha256,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                style = MaterialTheme.typography.bodySmall,
            )
        }
    }
    TextButton(onClick = { showFullHash = !showFullHash }, modifier = Modifier.fillMaxWidth()) {
        Text(if (showFullHash) "Ocultar SHA-256 completo" else "Ver SHA-256 completo")
    }
}

@Composable
private fun ImageActions(
    onSelectImage: () -> Unit,
    onRemoveImage: () -> Unit,
    canRemove: Boolean = true,
    enabled: Boolean = true,
) {
    Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
        Button(onClick = onSelectImage, enabled = enabled, modifier = Modifier.weight(1f)) {
            Text("Cambiar imagen")
        }
        TextButton(onClick = onRemoveImage, enabled = canRemove && enabled) {
            Text("Eliminar imagen")
        }
    }
}

private fun formatByteSize(bytes: Long): String = when {
    bytes >= 1024L * 1024L -> "%.1f MB".format(bytes / (1024.0 * 1024.0))
    bytes >= 1024L -> "%.1f KB".format(bytes / 1024.0)
    else -> "$bytes B"
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
    imageState = ImageUiState.Prepared(
        PreparedImageUiState(
            Content(
                mimeType = "image/png",
                widthPx = 2048,
                heightPx = 2048,
                byteSize = 4_194_304,
                sha256 = "a".repeat(64),
            ),
        ),
    ),
    localIngestState = LocalIngestUiState.Ready(
        reservedAssetId = "ast_01991d80-1000-7000-8000-000000000001",
        status = "ready_to_commit",
        content = Content(
            mimeType = "image/png",
            widthPx = 2048,
            heightPx = 2048,
            byteSize = 4_194_304,
            sha256 = "a".repeat(64),
        ),
    ),
    provenanceState = ProvenanceUiState.NotSpecified,
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

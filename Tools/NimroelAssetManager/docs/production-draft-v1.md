# Production Draft v1

## Propósito

`ProductionDraft` es el estado de dominio editable situado entre los contratos de producción y un `Asset` canónico. No es un Asset persistido, no genera `assetId` y no depende de Android, Room, filesystem ni proveedores remotos.

El flujo v1 es:

```text
Production Preset
  → Vocabulary Set exacto
  → Vocabularies/versiones enlazados
  → ProductionDraft editable
  → Asset Schema v1 validado
```

`ProductionDraftService.startDraft(presetId, presetVersion)` resuelve el preset exacto, lo valida con `ProductionContractValidator`, resuelve su Vocabulary Set y comprueba todas las referencias a vocabularios y valores antes de crear el borrador. Los fallos de resolución o validación producen errores de dominio explícitos.

## Selecciones y modos

El borrador conserva el ID y versión del preset, el `AssetType`, el ID y versión del Vocabulary Set y un mapa de selecciones indexado por rutas canónicas compartidas en `ProductionFieldPaths`.

Cada selección indica su valor, si procede del preset o del operador y el modo original del preset cuando existe:

- `fixed`: permanece bloqueada; no se puede cambiar ni eliminar en el flujo normal.
- `suggested`: se precarga, pero puede cambiarse o eliminarse.

Las selecciones introducidas por el operador que no estaban en el preset no tienen modo de preset.

## Edición y valores disponibles

`setSelection` y `clearSelection` operan sobre rutas canónicas conocidas. Para campos gobernados por vocabulario, la ruta debe tener un binding en el Vocabulary Set y el valor debe existir en el Vocabulary y versión enlazados. No existe ninguna tabla de IDs editoriales hardcodeada.

`availableValues` devuelve directamente, en el orden contractual, los valores del Vocabulary enlazado. Conserva `id`, `label`, `description`, `status` y `presentationOrder`, incluidos los valores `deprecated`.

Las parejas externas de Visual Profile y Prompt Template usan los campos canónicos existentes y validan la forma de ID o versión. No se resuelven registros de esos contratos porque todavía no existen registros canónicos para hacerlo.

## Materialización del Asset

`buildAsset` recibe el borrador, un `AssetId`, `Content` y `Provenance` del caller. Produce un Asset Schema v1 con:

- `schemaVersion = 1` y lifecycle `draft`;
- el `assetId`, `Content` y datos legítimos de `Provenance` recibidos;
- el `AssetType` del preset;
- la referencia exacta al Vocabulary Set en `classification.vocabularyId/vocabularyVersion`;
- selecciones materializadas en `classification`, `subject`, `details`, `visual` y, para Prompt Template, `provenance`;
- `NpcPortraitDetails` únicamente cuando existe `professionId` o `socialClassId`.

La pareja de Prompt Template del preset, cuando existe completa, sustituye esa pareja en `Provenance` sin borrar generator, `sourceAssetIds`, `promptRecordId`, `importedAt` ni otros datos admitidos. Si el borrador no aporta la pareja, se conserva la del caller. Las referencias incompletas se rechazan.

Antes de devolver el resultado, el builder ejecuta `AssetValidator`; cualquier infracción impide construir el Asset y se comunica en el error.

## Límites v1

La materialización implementada se limita a `npc_portrait` y `NpcPortraitDetails`. La estructura de rutas permite ampliar tipos en hitos posteriores sin introducir un motor JSONPath genérico.

Quedan fuera UI Compose, persistencia del borrador, generación de AssetId, perfiles visuales y prompt templates nuevos, filesystem, procesamiento de imágenes, WorkManager, ImageKit, backend, sincronización, Asset Resolver y el flujo de abandono de preset.

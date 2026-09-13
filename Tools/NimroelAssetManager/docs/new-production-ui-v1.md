# Nueva producción UI v1

## Objetivo

La primera pantalla funcional Android abre un `ProductionDraft` con el preset piloto real y permite revisar y editar sus selecciones gobernadas por vocabularios. La pantalla no crea, serializa ni persiste un `Asset`: el borrador continúa siendo el estado previo a la incorporación de imagen, `Content`, `AssetId` y `Provenance` final.

## Arquitectura

El flujo mantiene cinco responsabilidades separadas:

1. `ProductionDraftService` y `ProductionDraft` conservan las reglas de dominio, validación, bloqueo y resolución de valores.
2. `AndroidProductionDraftBootstrap` carga los contratos compartidos empaquetados por Android y construye los registros y el servicio.
3. `AssetManagerUiState` y sus modelos asociados representan datos inmutables orientados a presentación.
4. `AssetManagerViewModel` recibe eventos de selección o limpieza, invoca el servicio y reconstruye el estado visible.
5. `AssetManagerApp` renderiza estados loading, ready y error, sin leer JSON ni registros de contratos.

`ProductionDraftService.boundVocabularyFieldPaths` expone explícitamente la intersección entre rutas de vocabulario soportadas por Production Draft v1 y bindings del Vocabulary Set del borrador. Así la presentación no usa excepciones para descubrir campos ni crea selectores vacíos para rutas no enlazadas.

## Carga runtime de contratos

El source set `main` de Android incorpora directamente `../contracts` como directorio de assets. No existe copia de los JSON ni una segunda fuente de verdad.

El bootstrap enumera y deserializa los JSON de:

- `presets/examples`;
- `vocabulary-sets/data`;
- `vocabularies/data`.

Después crea `PresetRegistry`, `VocabularySetRegistry`, `VocabularyRegistry` y `ProductionDraftService`. `PilotProductionConfiguration` es la única frontera que contiene el ID y versión temporales del preset que abre la aplicación. La UI y el ViewModel no conocen esos valores.

## ViewModel y estado de UI

`AssetManagerViewModel` conserva internamente el entorno de dominio y nunca expone el `ProductionDraft` a Compose. Publica uno de estos estados:

- `Loading` durante la carga;
- `Error`, con un mensaje de bootstrap visible;
- `Ready`, con título, subtítulo, label y metadata del preset, `AssetType`, metadata del Vocabulary Set, campos visibles, resumen y error opcional de una acción.

Cada campo contiene ruta y etiqueta de presentación, valor actual y label editorial, opciones con su metadata de deprecación, modo original del preset, fuente actual, y capacidades de edición y limpieza. Los IDs de valores sólo se conservan para enviar las acciones al dominio; no son el texto principal de la interfaz.

Las etiquetas españolas de las rutas canónicas v1 son configuración de presentación. Los IDs de vocabularios, IDs de valores y listas editoriales proceden exclusivamente de contratos y del servicio.

## Fixed, suggested y operator

- Una selección `fixed` aparece deshabilitada, marcada como fija y no ofrece limpieza. El servicio sigue siendo la autoridad y rechaza también cualquier intento programático de cambio.
- Una selección `suggested` comienza con el valor del preset y puede modificarse o eliminarse.
- Después de un cambio, la fuente mostrada es `OPERATOR` y el resumen se actualiza inmediatamente.
- Después de limpiar un suggested, el selector queda vacío y admite una selección posterior. El ViewModel conserva su modo original para explicar correctamente el origen del campo.

Los errores de dominio mantienen el último borrador válido y aparecen en un bloque discreto. Las excepciones inesperadas de acciones no se absorben; los fallos de bootstrap sí se convierten en el estado de error de pantalla con su detalle.

## Comportamiento responsive

Con 840 dp o más de ancho, la pantalla usa dos zonas independientes: editor a la izquierda y resumen/metadata a la derecha. En anchos menores apila ambas zonas en un único scroll vertical. Se incluyen previews para 412 × 915 dp y 1280 × 800 dp.

## Valores deprecated

Los valores deprecated no se filtran. Permanecen en las opciones, se marcan como `Obsoleto` y, si están seleccionados, mantienen esa advertencia tanto en el campo como en el resumen.

## Límites del hito

La acción `Continuar con imagen` es visible pero está deshabilitada. No se implementan selección o permisos de imagen, filesystem administrado, transformación WebP, thumbnails, hashing, `Content`, generación de `AssetId`, `buildAsset` desde UI, Room, WorkManager, proveedores remotos, sincronización, navegación ni catálogo general de presets.

El siguiente hito es la selección/importación local de imagen y la preparación de `Content`, sin adelantar todavía persistencia o sincronización.

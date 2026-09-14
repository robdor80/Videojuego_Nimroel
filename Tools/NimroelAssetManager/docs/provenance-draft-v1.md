# Provenance Draft v1

## Propósito y frontera

`ProvenanceDraft` captura la procedencia real declarada por el operador después de que la ingestión local alcance `ready_to_commit`. Es estado de edición puro y no persistido; sólo `ProvenanceDraftService` puede materializarlo como el `Provenance` canónico ya definido por Asset Schema v1.

```text
ProductionDraft + PreparedImage + staging ready_to_commit + AssetId reservado
  → ProvenanceDraft explícito
  → Provenance válida
  → [hito futuro] procesamiento canónico y finalización del Asset
```

Este hito no crea un `Asset`, no llama `ProductionDraftService.buildAsset` desde la UI y no llama `commitIngestedAsset`.

## El selector Android no determina la procedencia

Una URI `content://` sólo describe el mecanismo temporal mediante el que Android entrega acceso a una imagen. No dice quién creó la obra ni cómo se obtuvo originalmente. Una imagen generada mediante IA y guardada en la tablet sigue teniendo procedencia `generated` aunque el operador la seleccione desde la galería.

Por ello no se infiere `originKind` desde URI, MIME, galería, nombre, filesystem ni mecanismo de selección. El estado inicial tras staging es `Sin especificar`, y `imported` sólo existe cuando el operador lo selecciona explícitamente.

## Modelo y validación

La jerarquía sellada admite exactamente las variantes wire de Asset Schema v1:

- `Generated`: exige `generator.provider` con formato de reference ID y `generator.generatedAt`; `generator.model` es opcional y admite hasta 200 caracteres.
- `Imported`: no añade campos obligatorios; `importedAt` es opcional.
- `Edited`: exige uno o más `sourceAssetIds`.
- `Derived`: exige uno o más `sourceAssetIds` y permanece distinta de `Edited`.
- `Unknown`: exige la confirmación explícita “Confirmo que la procedencia real es desconocida”. No sirve de fallback para datos incompletos.

Las fechas introducidas se convierten a `java.time.Instant`. Una entrada vacía, válida o inválida tiene representación explícita en el borrador; sólo un `Instant` válido llega a `Provenance`. La acción “Usar fecha y hora actual” es voluntaria y el formulario nunca presupone cuándo se generó o importó la imagen.

Los Asset IDs de `Edited` y `Derived` se separan por línea o coma y se validan mediante `AssetId.parse`. Se exige al menos uno, se rechazan duplicados y, cuando se conoce el AssetId reservado, se impide la autorreferencia. No se consulta aún un catálogo ni se inventan Assets.

Seleccionar otra variante crea un estado nuevo. De este modo `Generated → Imported` no puede conservar `generator`, y `Edited/Derived → Generated` no puede conservar `sourceAssetIds`.

## Relación con Production Draft y Provenance canónica

El formulario no duplica `promptTemplateId` ni `promptTemplateVersion`: pertenecen a las selecciones del `ProductionDraft`. La materialización produce sólo los campos declarados por la variante. En el futuro, `ProductionDraftService.buildAsset` añadirá su pareja de prompt template de forma atómica y conservará generator, `sourceAssetIds`, `promptRecordId`, `importedAt` y cualquier otro campo canónico recibido, tal como cubren sus tests actuales.

`ProvenanceDraft` no sustituye ni modifica el modelo canónico `Provenance`, sus enums, wire values, serialización o contratos JSON. Es exclusivamente el estado previo que evita tratar una `Provenance` inválida como válida.

## Estado de UI y staging

La UI distingue:

- `Unavailable`: no existe staging `ready_to_commit` y la edición no se muestra ni acepta acciones.
- `NotSpecified`: staging listo, pero el operador aún no eligió procedencia.
- `Invalid`: existe una variante seleccionada con campos pendientes o incorrectos.
- `Valid`: el servicio ha materializado una `Provenance` canónica.

La sección aparece inmediatamente después de “Ingestión local preparada”. Editar o fallar la validación de procedencia no modifica el `ProductionDraft`, `PreparedImage`, staged source, work item, estado `ready_to_commit` ni AssetId reservado. La presentación no expone URI externas ni paths administrados.

El botón “Crear borrador de Asset” permanece deshabilitado. Cuando la procedencia ya es válida, la explicación deja de citarla como pendiente, pero recuerda que aún faltan el procesamiento del binario canónico y la finalización del Asset.

## Fuera de alcance y siguiente hito

No se implementan WebP, canonicalización, resize, recompress, thumbnails, `AssetDocument`, `AssetLocalState`, `LocalRepresentation`, publicación remota, ImageKit, R2, Firebase, sincronización ni Asset Resolver. Tampoco se persiste `ProvenanceDraft` en Room: la DB permanece en versión 1 y su schema físico no cambia.

El siguiente hito es definir **Canonical Image Profile / Canonical Image Processing** mediante pruebas reales de calidad y tamaño. Sólo después podrá finalizarse el Asset y ejecutarse el commit transaccional ya existente.

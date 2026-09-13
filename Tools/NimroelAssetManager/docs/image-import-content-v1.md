# Selección local de imagen y preparación de Content v1

## Objetivo

Este hito incorpora una imagen local al flujo interactivo de “Nueva producción” y calcula un `Content` de Asset Schema v1 que describe exactamente los bytes seleccionados. La imagen todavía no se copia a almacenamiento administrado, no se transforma, no se persiste y no produce un Asset final.

## Selección Android y referencia temporal

`MainActivity` utiliza `ActivityResultContracts.GetContent` con `image/*`. El selector concede acceso puntual mediante un `content:// Uri`; no se solicita `READ_EXTERNAL_STORAGE` ni ningún permiso general de almacenamiento, no se consulta `MediaStore.DATA`, no se convierte el URI en una ruta física y no se presupone la existencia de un `File`.

El URI se serializa en `ImageSourceRef`, una referencia técnica opaca y temporal de la sesión. No es identidad de Asset y no forma parte de Asset Schema. Este hito no persiste permisos URI ni recupera la referencia después de la muerte del proceso. La política de ingestión/staging futura deberá resolver esa transición antes de depender de la fuente temporal.

Cancelar el selector no se considera error y conserva intacto el estado actual.

## Arquitectura

El flujo es:

```text
Activity Result / Compose
  → AssetManagerViewModel
  → ImageContentPreparer
  → AndroidImageContentPreparer
  → ContentResolver
```

`ImageContentPreparer` es una frontera suspendible y testeable que recibe `ImageSourceRef` y devuelve `PreparedImage`. `PreparedImage` mantiene separadas la referencia temporal y el `Content` canónico. El ViewModel no conoce streams, hashing, `BitmapFactory` ni detalles del proveedor de documentos.

La implementación Android encapsula el acceso a `ContentResolver`; su trabajo se ejecuta desde el ViewModel en `Dispatchers.IO` mediante `viewModelScope`.

## SHA-256 y byteSize

La fuente se abre con `use {}` y se recorre con un buffer mediante `MessageDigest` SHA-256. Los bytes no se acumulan en un `ByteArray`. Cada bloque leído actualiza simultáneamente el digest y un contador `Long`; por tanto `byteSize` procede de los bytes realmente leídos y no de metadata externa.

El hash resultante usa exactamente 64 caracteres hexadecimales en minúsculas y corresponde a esos mismos bytes.

## Dimensiones, MIME y colorSpace

Las dimensiones se obtienen en una segunda apertura del URI con `BitmapFactory.Options.inJustDecodeBounds`. No se decodifica el bitmap completo. `widthPx` y `heightPx` describen las dimensiones codificadas del binario; este hito no aplica orientación EXIF ni transforma píxeles.

El MIME declarado por `ContentResolver` debe ser `image/*` si existe. El MIME detectado por el decoder completa o prevalece sobre la declaración del proveedor porque describe el formato codificado. Se normaliza el alias `image/jpg` a `image/jpeg`. Si no existe una determinación fiable, el tipo no es de imagen o las dimensiones son inválidas, la preparación se rechaza.

`colorSpace` queda en `null`: no se inventa un valor ni se decodifica una imagen completa sólo para obtenerlo.

## Content y validación

El resultado contiene:

- `mimeType`;
- `widthPx` y `heightPx` positivos;
- `byteSize` positivo medido durante hashing;
- `sha256` de los bytes exactos;
- `colorSpace = null`.

`ContentValidator` concentra las reglas de dominio que antes eran privadas en `AssetValidator`. `AssetValidator` delega en él, por lo que la preparación puede validar `Content` antes de que existan `AssetId` y `Provenance` sin duplicar ni relajar Asset Schema v1.

Regla crítica: este `Content` describe la fuente seleccionada en este punto del flujo. Si posteriormente PNG/JPEG u otra fuente se transforma a un WebP canónico, el `Content` del Asset final deberá recalcular MIME, dimensiones, byteSize y SHA-256 sobre el binario transformado. Nunca se reutilizará la metadata de la fuente después de una transformación.

## Estado, reemplazo y concurrencia

El estado de imagen dentro de `Ready` es uno de:

- `NoImage`;
- `Processing`, que puede conservar una imagen preparada previa;
- `Prepared`, con el `Content` validado;
- `ImageError`, con mensaje y la imagen preparada previa cuando existe.

Seleccionar una imagen inicia progreso indeterminado sin ocultar ni reconstruir el `ProductionDraft`. Eliminar cancela el trabajo actual y vuelve a `NoImage`.

Cada selección incrementa un token de generación y cancela el `Job` anterior. Aunque una operación A no responda inmediatamente a cancelación, su resultado se descarta si ya existe una selección B. La última selección gana.

Durante un reemplazo, la imagen preparada anterior permanece separada del trabajo en curso. Si la nueva fuente falla, se conserva la anterior y se muestra el error; sólo un análisis correcto la sustituye.

## UI

La sección de imagen ofrece `Seleccionar imagen`, progreso `Analizando imagen…`, metadata de una imagen preparada, SHA-256 truncado con expansión seleccionable, `Cambiar imagen` y `Eliminar imagen`. El URI no se muestra.

La acción futura `Crear borrador de Asset` permanece deshabilitada e indica que faltan AssetId, Provenance y persistencia.

## Fuera de alcance

Quedan fuera copia definitiva, filesystem administrado, staging, política de retención, persistencia de permisos URI, WebP, recompress, resize, thumbnails, normalización EXIF, AssetId, Provenance final, `buildAsset` desde UI, Room para la imagen, WorkManager, ImageKit, backend, sincronización y Asset Resolver.

El siguiente hito razonable es definir staging/ingestión local y generación controlada de AssetId/Provenance, sin fijar aún la política definitiva de retención.

# Local staging y reserva de AssetId v1

## Objetivo y frontera

Este hito cruza de forma inmediata la frontera entre una fuente Android temporal y bytes controlados por Nimroel Asset Manager:

```text
content:// temporal
  → copia streaming y verificación
  → staging privado gestionado
  → ready_to_commit
```

Cuando el trabajo alcanza `ready_to_commit`, la copia estable ya no necesita volver a abrir el URI externo. El URI se conserva en `ingest_work_items.source_uri` únicamente como dato operacional.

## Identidades

`AssetIdGenerator` es una frontera de dominio. `UuidV7AssetIdGenerator` produce `ast_` seguido de un UUIDv7 canónico lowercase: codifica los 48 bits del instante Unix en milisegundos, fija versión 7 y variant RFC, y completa los 74 bits libres con `SecureRandom`. `Clock` y `RandomBytesSource` son inyectables para pruebas deterministas. El ID se reserva una sola vez antes de crear el trabajo y se persiste de inmediato en `reserved_asset_id`.

`work_id` es una identidad operacional opaca e independiente, generada como UUID aleatorio estándar. No se deriva del `AssetId` y no entra en Asset Schema.

## Orquestación y Room

`LocalIngestCoordinator` recibe `PreparedImage`, generadores, `StagingFileStore`, `IngestWorkItemStore` y `Clock`. El ViewModel sólo inicia el caso de uso y proyecta su resultado; no coordina filesystem ni estados Room.

La DB permanece en versión 1 y no cambia su schema físico. Se reutiliza `ingest_work_items` con este protocolo:

1. reservar `AssetId` y crear una fila `queued` sin staging ni error;
2. transición condicionada `queued → processing`;
3. copiar, sincronizar y verificar staging;
4. transición condicionada `processing → ready_to_commit` con el path relativo;
5. ante un fallo conocido, `processing → failed` con código estable y detalle acotado.

`IngestWorkTransitionPolicy` sólo admite `queued → processing`, `processing → ready_to_commit` y `processing → failed`. El DAO aplica el cambio con `WHERE work_id = ? AND state = ?`, de modo que una carrera no puede sobrescribir un estado distinto. `ready_to_commit`, `failed` y `committed` no regresan a `processing` por esta API. El paso posterior `ready_to_commit → committed` continúa reservado a la transacción existente `commitIngestedAsset`, fuera del flujo ejecutado por este hito.

Si Room acepta la creación `queued` pero no puede confirmar la transición inmediata a `processing`, el coordinador aborta y conserva explícitamente la fila `queued`; no inventa `queued → failed` ni inicia filesystem. Un ejecutor/reconciliador futuro podrá decidir cómo reanudar esa evidencia. Las excepciones inesperadas ocurridas ya en `processing` se registran como `unexpected_io` y se vuelven a propagar, en lugar de ocultarse.

## Directorio gestionado y paths

`AndroidStagingFileStore` usa exclusivamente almacenamiento privado de la app:

```text
filesDir/
  nimroel-assets/
    staging/
      <workId>/
        source.part
        source
```

Room sólo recibe `staging/<workId>/source`, relativo a `nimroel-assets`. El `workId` se valida como un único segmento seguro y las validaciones existentes de `RoomLocalAssetStore` rechazan rutas absolutas, barras invertidas, unidades, segmentos vacíos, `.` y `..`. El nombre original de la fuente no se usa.

## Escritura y verificación

La fuente se abre mediante `ContentResolver` y se copia con un buffer a `source.part`; nunca se usa `readBytes()` ni se carga un bitmap completo. Cada bloque actualiza simultáneamente SHA-256 y `byteSize`. Después se hace `flush`, `FileDescriptor.sync()` y cierre.

Antes de publicar el archivo estable se comparan hash y tamaño con `PreparedImage.content`. Las dimensiones y el MIME se obtienen directamente de `source.part` con `BitmapFactory.Options.inJustDecodeBounds` sobre un stream del archivo privado, sin consultar otra vez al `ContentResolver`. MIME, dimensiones, tamaño y hash deben coincidir exactamente. Un cambio en cualquiera produce `source_changed`; bytes que ya no describen una imagen válida producen `invalid_image`.

Sólo tras superar la verificación se mueve `source.part` a `source` dentro del mismo filesystem. Se solicita movimiento atómico y se comprueba que el destino publicado existe y conserva el tamaño verificado. Un fallo de rename nunca publica `ready_to_commit` y limpia el temporal cuando es seguro.

Los códigos operacionales v1 son `source_unavailable`, `staging_write_failed`, `staging_verify_failed`, `source_changed`, `invalid_image` y `unexpected_io`. Los detalles se limitan a 240 caracteres, eliminan saltos de línea y redactan URIs `content://`; no contienen stack traces.

## Consistencia ante cierre y recuperación

Room y filesystem no comparten transacción. El orden anterior mantiene estas propiedades:

- `processing` con `source.part` no significa contenido válido;
- `processing` con `source` completo tampoco se convierte automáticamente en listo;
- `ready_to_commit` sólo se publica después de verificar y mover el archivo, y contiene un path relativo estable;
- un cierre abrupto puede dejar evidencia parcial o un `source` huérfano bajo un trabajo `processing`, que un reconciliador futuro podrá inspeccionar sin fingir éxito.

No se implementa todavía reconciliación de arranque ni WorkManager. La cancelación normal limpia el `.part`; la muerte abrupta se resuelve conservadoramente mediante el estado `processing` no listo.

## UI, concurrencia y retry

Una imagen preparada habilita `Preparar ingestión local`. Mientras se copia, la UI muestra progreso indeterminado, deshabilita el inicio duplicado y bloquea cambio/eliminación de imagen. Al terminar muestra el `AssetId` reservado, `ready_to_commit`, MIME, dimensiones, tamaño, hash resumido y confirmación local, sin URI ni paths internos.

Después de `ready_to_commit` se bloquean `Cambiar imagen` y `Eliminar imagen`; el descarte completo queda fuera de v1 para no dejar filas listas huérfanas. El Production Draft y el `PreparedImage` permanecen intactos ante fallos.

Un retry después de `failed` crea deliberadamente un nuevo work item y un nuevo `AssetId`; el trabajo fallido se conserva como evidencia. No se añade la transición `failed → processing` ni se reutiliza una identidad reservada tras un fallo.

## Staging no es canonical

`source` es una copia exacta de la fuente seleccionada y una entrada estable para procesamiento posterior. No es necesariamente el binario canónico: una etapa futura puede convertir PNG/JPEG a WebP y deberá recalcular `Content` sobre ese resultado.

Este hito no crea `Asset`, `Provenance`, `LocalRepresentation`, `asset_documents`, `asset_local_state` ni `Asset.storage`, y no llama `commitIngestedAsset`. Seleccionar un archivo local tampoco decide si el origen real fue generated, imported, edited o derived; la procedencia se capturará explícitamente en un flujo posterior.

## Fuera de alcance

- canonicalización, WebP, resize, recompress, thumbnails y EXIF;
- creación/finalización del Asset y Provenance;
- descarte de una ingestión lista y limpieza periódica de staging;
- reconciliador de arranque y WorkManager;
- ImageKit, backend, Firebase, sincronización y Asset Resolver.

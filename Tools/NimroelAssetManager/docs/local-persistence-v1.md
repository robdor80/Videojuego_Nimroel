# Persistencia local v1

## 1. Alcance

Este documento define la arquitectura local que deberá implementar Android con Room en el siguiente hito. No implementa base de datos, importación, conversión, sincronización ni UI.

La misma separación conceptual puede reproducirse en Windows, aunque las entidades Room y sus migraciones serán exclusivamente Android.

## 2. Alternativas evaluadas

### A. Asset completamente normalizado en Room

Cada propiedad de Asset Schema se repartiría entre columnas y tablas relacionadas.

Ventajas:

- consultas SQL directas sobre cualquier campo;
- integridad relacional detallada para estructuras estables.

Problemas:

- replica Asset Schema dentro de Room y obliga a mantener dos contratos equivalentes;
- `details` condicionado por tipo y `extensions` producirían muchas tablas o columnas dispersas;
- cada evolución del schema canónico exigiría migraciones físicas complejas;
- reconstruir el JSON exacto para exportación sería más frágil;
- normaliza campos sin una necesidad de consulta demostrada.

### B. `canonicalJson` con proyecciones reconstruibles

Room conserva la ficha completa y válida como JSON, junto con un conjunto pequeño de columnas derivadas para búsqueda. El estado local y los archivos físicos viven en tablas separadas.

Ventajas:

- Asset Schema sigue siendo la única forma canónica;
- preserva sin pérdida `details`, `extensions` y campos opcionales;
- las proyecciones pueden regenerarse al cambiar las consultas o el lector;
- una migración de Asset Schema no obliga automáticamente a normalizar toda su estructura;
- permite transacciones consistentes entre documento, proyecciones y estado local dentro de Room.

Costes:

- toda escritura debe deserializar y validar el JSON antes de persistirlo;
- no se consultan eficientemente campos que no tengan proyección;
- debe impedirse que una proyección desactualizada se trate como fuente de verdad.

### C. JSON externo y Room sólo como índice

Cada ficha canónica sería un archivo JSON; Room guardaría únicamente índices y referencias.

Ventajas:

- documentos visibles y portables fuera de la base;
- el índice se podría reconstruir desde el directorio.

Problemas:

- no existe una transacción atómica común entre filesystem y Room;
- aumenta el riesgo de JSON sin índice o índice sin JSON;
- complica escrituras concurrentes, backup y recuperación;
- añade archivos pequeños sin una necesidad operativa actual.

## 3. Decisión

Se adopta la alternativa B: `canonicalJson` en Room más proyecciones reconstruibles.

La fuente de verdad local de los **datos canónicos** es `asset_documents.canonical_json`. Sólo se guarda después de deserializarlo, validarlo como Asset Schema soportado y serializarlo con el codec canónico Kotlin.

Las columnas proyectadas, el estado operacional y el inventario de archivos locales no forman parte de la ficha intercambiable. Nunca se exportan como si fueran campos de Asset Schema.

## 4. Modelo conceptual de tablas

Los nombres son contractuales para el diseño v1, pero podrán ajustarse al implementar Room si el cambio queda documentado.

### `asset_documents`

Una fila por asset lógico.

| Campo | Propósito |
|---|---|
| `asset_id` (PK) | Identidad lógica; debe coincidir con `canonicalJson.assetId`. |
| `schema_version` | Proyección de `canonicalJson.schemaVersion`. |
| `canonical_json` | Ficha canónica completa y validada. |
| `asset_type` | Proyección indexable de `type`. |
| `lifecycle_status` | Proyección indexable de `lifecycle.status`. |
| `realm_id` | Proyección nullable de `classification.realmId`. |
| `culture_id` | Proyección nullable de `classification.cultureId`. |
| `subject_entity_id` | Proyección nullable de `subject.entityId`. |
| `projection_version` | Versión del algoritmo local que generó las proyecciones. |

Los campos proyectados iniciales corresponden a filtros previsibles de biblioteca. No se añadirán columnas para cada propiedad del schema. Si la búsqueda por tags se demuestra necesaria, se añadirá una tabla derivada `asset_tag_projections(asset_id, tag)` con índice por `tag`; no será fuente de verdad.

Índices iniciales razonables:

- `asset_type`;
- `lifecycle_status`;
- `subject_entity_id`;
- `realm_id`;
- `culture_id`;
- opcionalmente el compuesto `asset_type + lifecycle_status` cuando exista la consulta real.

### `asset_local_state`

Una fila por asset conocido localmente. Separa disponibilidad técnica de `lifecycle.status`.

| Campo | Propósito |
|---|---|
| `asset_id` (PK/FK) | Relación con `asset_documents`. |
| `availability` | `available`, `degraded` o `unavailable`. |
| `last_reconciled_at` | Instante de la última comprobación local, nullable. |
| `diagnostic_code` | Código local estable, nullable. |
| `diagnostic_detail` | Detalle local para diagnóstico, nullable y acotado. |

`availability` significa:

- `available`: existe y pasa verificación la representación local requerida;
- `degraded`: el asset es legible, pero falta o falla una representación derivada o secundaria esperada;
- `unavailable`: no existe o no verifica ningún binario local utilizable.

No incluye estados de red, upload, retry remoto ni conflictos.

### `local_representations`

Inventario de archivos físicos administrados por la instalación.

| Campo | Propósito |
|---|---|
| `representation_id` (PK) | Identidad técnica local, nunca identidad del asset. |
| `asset_id` (FK) | Asset lógico al que pertenece. |
| `role` | `source_original`, `canonical` o `thumbnail`. |
| `relative_path` | Localizador relativo a una raíz gestionada por la app. |
| `mime_type` | MIME observado del archivo. |
| `sha256` | Hash del binario local. |
| `width_px`, `height_px` | Dimensiones observadas cuando aplican. |
| `byte_size` | Tamaño observado. |
| `availability` | `present`, `missing` o `corrupt`. |

El formato no determina el rol. Un WebP futuro será `canonical` si es el binario descrito por `Asset.content`, o una representación derivada si una política futura lo define. `thumbnail` siempre es regenerable. El original importado puede conservarse o eliminarse según una política aún pendiente.

La presencia real se decide desde `local_representations` más verificación del filesystem, no desde `Asset.storage`. El bloque canónico `storage` sigue describiendo réplicas intercambiables conocidas; no sustituye el inventario operacional de esta instalación.

### `ingest_work_items`

Registra trabajo local antes de que exista una ficha Asset completa.

| Campo | Propósito |
|---|---|
| `work_id` (PK) | Identidad operacional local. |
| `reserved_asset_id` (unique) | `assetId` generado para el resultado futuro; aún no implica que exista un Asset. |
| `source_uri` | URI de entrada local, nunca identidad ni campo canónico. |
| `state` | Estado del procesamiento local. |
| `staging_relative_path` | Archivo temporal dentro de almacenamiento gestionado, nullable. |
| `created_at`, `updated_at` | Timestamps operacionales. |
| `error_code`, `error_detail` | Diagnóstico local nullable. |

Estados v1:

- `queued`: entrada registrada y pendiente de trabajo;
- `processing`: una operación local está construyendo/verificando resultados;
- `ready_to_commit`: resultados temporales completos y verificados, pendientes de transacción final;
- `failed`: el trabajo se detuvo y conserva diagnóstico;
- `committed`: documento y representaciones ya se registraron; la fila puede depurarse según política.

`imported` no se usa como estado porque describe un origen o evento, no si el asset está procesado y disponible. `ready` se reserva conceptualmente para disponibilidad; el trabajo usa `ready_to_commit` para evitar ambigüedad.

## 5. Modelo conceptual de archivos

La app tendrá una raíz privada o gestionada. La base sólo conservará paths relativos normalizados y generados por la aplicación. Los nombres concretos de carpetas no se fijan todavía porque dependen de la política de retención y APIs de almacenamiento elegidas.

Se distinguen estas clases:

- entrada externa: URI recibida, posiblemente temporal;
- staging: copia temporal bajo control de la app mientras se procesa;
- original administrado: copia opcional de la fuente importada;
- binario canónico: archivo descrito por `Asset.content`;
- miniatura: derivado prescindible y regenerable.

Ni el nombre, extensión, URI ni path participan en la identidad lógica. `assetId` es la única identidad del asset.

## 6. Protocolo de escritura y recuperación

Room y filesystem no comparten una transacción. La implementación deberá usar un protocolo ordenado:

1. Crear o actualizar `ingest_work_items` en una transacción Room.
2. Escribir en staging dentro del mismo filesystem que el destino final.
3. Calcular y verificar SHA-256, MIME, dimensiones y tamaño.
4. Cerrar y sincronizar el archivo cuando la plataforma lo permita.
5. Moverlo al destino gestionado mediante rename atómico cuando sea posible.
6. En una transacción Room, insertar `asset_documents`, sus proyecciones, `local_representations` y `asset_local_state`, y marcar el trabajo `committed`.

La fila que declara un archivo `present` sólo se crea después de verificar que el movimiento final terminó. Un cierre entre los pasos 5 y 6 puede dejar un archivo huérfano, pero no una fila que afirme falsamente su existencia. Una reconciliación futura podrá adoptar o eliminar huérfanos tras verificar identidad/hash y aplicar un periodo de seguridad.

Al iniciar la app, los trabajos `processing` o `ready_to_commit` no se dan por completados: se revisan staging, destino y hashes para reanudar o marcar fallo. No se implementa todavía el motor de recuperación.

## 7. Proyecciones

Las proyecciones se calculan exclusivamente desde el modelo Kotlin deserializado de `canonical_json`. Nunca se editan de forma independiente.

Invariantes:

- toda escritura de JSON actualiza sus proyecciones en la misma transacción Room;
- `asset_id` y `schema_version` deben coincidir con el documento;
- `projection_version` identifica el algoritmo, no Asset Schema;
- si una proyección discrepa, gana `canonical_json` y se reconstruye la fila;
- una reconstrucción valida cada documento y aísla los que no pueda leer, sin descartarlos.

## 8. Versiones y migraciones

La versión de Room y `Asset.schemaVersion` son independientes.

- La base inicial será Room DB version 1 cuando se implemente.
- Una migración física de Room preservará siempre `canonical_json` antes de recalcular proyecciones.
- Añadir o cambiar una proyección incrementa la versión de base y/o `projection_version` según requiera cambio físico; la proyección se regenera desde JSON.
- Si aparece Asset Schema v2, la base puede conservar documentos v1 y v2 simultáneamente mientras existan lectores compatibles.
- Migrar un documento v1 a v2 será una operación de dominio explícita, validada e idempotente; no se fingirá mediante una migración de columnas Room.
- Un documento de schema desconocido se conserva intacto y queda no editable/no indexable hasta disponer de lector; no se elimina.

No se definen migraciones futuras ficticias en este hito.

## 9. Invariantes críticas

1. `assetId` es la identidad; ninguna fila, URI, ruta, URL o ID de proveedor puede sustituirlo.
2. `canonical_json` es la única fuente local de datos canónicos.
3. Sólo se persiste como documento canónico JSON soportado, deserializable y válido.
4. Las proyecciones son derivadas, coherentes transaccionalmente y reconstruibles.
5. Lifecycle editorial y estado operacional nunca comparten campo ni enum.
6. Un archivo físico siempre se identifica como representación de un asset, no como el asset mismo.
7. Los paths persistidos son relativos, normalizados y no pueden escapar de la raíz gestionada.
8. Una representación `canonical` disponible debe coincidir con `content.sha256`, MIME, dimensiones y tamaño cuando éste exista.
9. Las miniaturas y demás derivados nunca son la única copia necesaria para recuperar el binario canónico.
10. Las operaciones sobre filesystem se verifican antes de declararse completas en Room.
11. Ningún estado de ImageKit, upload, red o resolver entra en Asset Schema ni en este contrato local v1.

## 10. Riesgos y mitigaciones

- Divergencia JSON/proyección: transacción única y reconstrucción por `projection_version`.
- Divergencia DB/filesystem: protocolo de staging, rename verificado y reconciliación futura.
- Corrupción silenciosa: SHA-256 y metadatos observados.
- Crecimiento por originales/derivados: política de retención pendiente y roles explícitos.
- Schema futuro no soportado: conservar JSON intacto y bloquear edición destructiva.
- Consultas no previstas: añadir sólo proyecciones justificadas y reconstruirlas desde JSON.

## 11. Fuera de alcance

- entidades, DAO, Database y migrations Room reales;
- importación desde galería y permisos URI;
- conversión WebP o thumbnails reales;
- WorkManager y ejecución de colas;
- upload, ImageKit, backend y sincronización;
- Asset Catalog y Asset Resolver;
- UI, lotes y sesiones de producción;
- política definitiva de retención y borrado.

## 12. Decisiones pendientes

1. Política de retención del original importado.
2. Ubicación Android concreta de la raíz gestionada y política de backup del sistema.
3. Cuándo se materializa `Asset.storage` para una representación local y cómo se mantiene coordinado con el inventario local.
4. Consultas reales que justifican índices adicionales o proyección de tags.
5. Política de limpieza de staging, trabajos `committed` y archivos huérfanos.
6. Tratamiento UX de documentos con schema futuro no soportado.

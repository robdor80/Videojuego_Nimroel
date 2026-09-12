# Nimroel Asset Schema v1

**Estado:** aprobado como contrato canónico v1  
**Contrato validable:** `../contracts/asset-schema-v1.schema.json`  
**JSON Schema:** Draft 2020-12

## 1. Propósito

Asset Schema v1 define la ficha canónica e intercambiable de un asset visual de Nimroel. Debe poder ser leído por Android, la futura aplicación Windows, el catálogo y el futuro Asset Resolver sin depender de una plataforma, proveedor o base de datos concretos.

Una ficha describe la identidad lógica, semántica, procedencia, contenido y ubicaciones conocidas del asset. Puede existir y ser válida completamente offline. El estado operacional de una instalación se almacena fuera de este contrato.

## 2. Principios

- `assetId` es identidad opaca, permanente e independiente de toda clasificación.
- Un cambio visual material crea un asset nuevo; una edición de metadata no.
- `type` expresa la clase de representación visual, no el sujeto, reino o estilo.
- El núcleo es pequeño; `details` se valida según `type`.
- Los datos experimentales sólo entran en extensiones con namespace.
- `content` describe el binario canónico; `storage` describe sus réplicas.
- El schema no contiene `sync`, credenciales, estado de UI ni rutas temporales.
- No se serializan objetos o arrays vacíos. Los bloques opcionales se omiten.
- IDs y versiones de perfiles, templates y vocabularios son campos separados.

## 3. Revisión de arquitectura

No se ha detectado ningún **CRITICAL DESIGN CONCERN** en las decisiones aprobadas.

Sí se detectó una contradicción corregible: el contrato preliminar `asset-contract-foundations.json` exigía `localState` dentro de la ficha compartida. Eso contradecía la separación ya aprobada entre asset canónico y sincronización local. El schema v1 sustituye ese contrato preliminar; el estado local seguirá siendo responsabilidad de la persistencia Android/Windows en el próximo hito.

También se resolvieron estas ambigüedades:

- El perfil visual tiene una única fuente dentro de la ficha: `visual.visualProfileId` y `visual.visualProfileVersion`. Procedencia lo referencia conceptualmente, pero no duplica ambos campos.
- `details` es opcional cuando un tipo no necesita aún ningún dato específico —por ejemplo, un retrato canónico sin profesión conocida—, pero si existe no puede estar vacío ni contener campos de otro tipo.
- `storage` sólo admite localizadores técnicos portables: IDs de objeto, rutas lógicas relativas a una raíz de biblioteca o URL opcional. Nunca rutas temporales/absolutas dependientes del dispositivo.
- El hash identifica el binario canónico actual, no el concepto visual. Una conversión técnica reproducible puede actualizarlo sin cambiar `assetId`; una imagen visualmente distinta no puede.

## 4. AssetId

Formato definitivo:

```text
ast_ + UUIDv7 canónico en minúsculas
```

Ejemplo:

```text
ast_019c1a23-4567-7abc-8def-0123456789ab
```

Expresión de validación:

```regex
^ast_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$
```

Se genera una vez al crear el asset, incluso sin conexión. Es inmutable durante reclasificación, migración, publicación, cambio de proveedor o conversión técnica. El prefijo identifica el dominio de la clave y no codifica semántica.

## 5. Anatomía de la ficha

```json
{
  "schemaVersion": 1,
  "assetId": "ast_019c1a23-4567-7abc-8def-0123456789ab",
  "type": "npc_portrait",
  "lifecycle": { "status": "approved" },
  "classification": {},
  "subject": {},
  "details": {},
  "visual": {},
  "content": {},
  "provenance": {},
  "storage": {},
  "extensions": {}
}
```

El fragmento anterior muestra la anatomía, no una ficha válida: los objetos opcionales vacíos se omiten y los bloques requeridos deben satisfacer su contrato.

## 6. Tabla de campos

| Campo | Obligatorio | Fuente | Naturaleza | Regla principal |
|---|---:|---|---|---|
| `schemaVersion` | Sí | Contrato | Inmutable por representación | En v1 debe ser exactamente `1`. |
| `assetId` | Sí | Generador de identidad | Inmutable | `ast_` + UUIDv7 canónico. |
| `type` | Sí | Clasificación editorial | Inmutable tras publicación | Uno de los siete tipos v1. |
| `lifecycle` | Sí | Edición | Mutable | Estado editorial, nunca de red. |
| `classification` | No | Edición/vocabularios | Mutable | Contexto del mundo y tags. |
| `subject` | No | Edición/lore | Mutable | Referencia al sujeto, no copia de lore. |
| `details` | No | Edición/vocabularios | Mutable | Forma condicionada por `type`. |
| `visual` | No | Perfil visual/edición | Mutable con auditoría | Perfil y rasgos visuales estructurados. |
| `content` | Sí | Procesador de imagen | Calculado | Propiedades del binario canónico. |
| `provenance` | Sí | Importador/generador | Histórica | Origen y referencias de generación. |
| `storage` | No | Adaptadores de almacenamiento | Mutable | Réplicas conocidas; no identidad. |
| `extensions` | No | Herramientas autorizadas | Experimental | Objetos bajo namespace. |

En JSON, `additionalProperties: false` se aplica al nivel raíz y a todos los bloques canónicos. Así un error tipográfico no se convierte silenciosamente en metadata. `extensions` es la excepción deliberada y controlada.

## 7. Mutabilidad e inmutabilidad

### Inmutable

- `assetId`.
- La relación histórica expresada en `provenance.sourceAssetIds`.
- La versión declarada de una representación ya guardada; una migración produce representación nueva con el mismo `assetId`.
- La imagen lógica representada: si cambia materialmente, se crea otro asset.

### Mutable con control de revisión/auditoría

- `lifecycle`, `classification`, `subject`, `details`, `visual` y tags.
- Localizadores de `storage` y URLs de entrega.
- `content` únicamente si cambia la codificación técnica sin cambiar la representación visual.
- Datos de procedencia que se completan posteriormente, sin borrar historia válida.

El número de revisión y el historial de cambios no se fijan aún dentro del schema. Corresponden al catálogo o mecanismo de versionado que se diseñará por separado.

## 8. Details por type

Los identificadores siguientes apuntan a vocabularios versionados externos. El schema valida su forma, no enumera todo Nimroel.

| `type` | Campos admitidos en `details` | Requerido si existe el bloque |
|---|---|---|
| `npc_portrait` | `professionId`, `socialClassId` | Al menos uno. Género, edad y especie pertenecen a `subject`; expresión a `visual`. |
| `landscape` | `environmentId`, `landformIds`, `waterFeatureIds` | `environmentId`. Hora, clima e iluminación pertenecen a `visual`. |
| `settlement` | `settlementScaleId`, `environmentId` | `settlementScaleId`. Una entidad canónica concreta va en `subject.entityId`. |
| `building` | `buildingFunctionId`, `materialIds` | `buildingFunctionId`. Reino/región/asentamiento van en `classification`. |
| `interior` | `interiorFunctionId`, `containingBuildingEntityId` | `interiorFunctionId`. El segundo campo enlaza un edificio canónico contenedor. |
| `object` | `objectKindId`, `materialIds` | `objectKindId`. Una pieza canónica concreta se referencia en `subject.entityId`. |
| `environment_scene` | `sceneFunctionId`, `environmentId`, `featuredEntityIds` | `sceneFunctionId`. Las entidades destacadas no sustituyen al sujeto principal. |

`unique_character` y `unique_location` no existen como tipos. Canonicidad es una propiedad del sujeto, no de la técnica de representación.

## 9. Entidades canónicas

`subject.entityId` referencia una entidad estable gestionada por una fuente de lore futura. La ficha visual no copia nombre, historia, relaciones ni atributos canónicos de dicha entidad.

Varios assets pueden compartir el mismo `subject.entityId`:

```text
personaje canónico X
├── asset A: npc_portrait
├── asset B: environment_scene
└── asset C: otro npc_portrait materialmente distinto
```

Cada representación conserva su propio `assetId`. En v1, `subject` también puede contener `speciesId`, `genderId` y `ageBandId` para sujetos no canónicos o facetas de búsqueda. Ninguno forma parte de la identidad.

## 10. Classification

`classification` alberga contexto compartido: `realmId`, `cultureId`, `regionId`, `settlementId` y `tags`. Los tags son auxiliares; un dato que necesite consultas fiables debe tener un campo estructurado.

`vocabularyId` y `vocabularyVersion` pueden identificar el conjunto versionado que interpreta los IDs. Si aparece uno, el otro es obligatorio. La fuente y contenido del primer vocabulario son una decisión abierta.

No se usan `null`, `unspecified`, `region-unspecified` ni pseudo-valores equivalentes para campos opcionales. Un dato ausente se omite.

## 11. Visual

`visual` contiene el perfil realmente aplicado y rasgos visuales consultables:

- `visualProfileId` + `visualProfileVersion`, siempre como pareja;
- `compositionId`, `timeOfDayId`, `weatherId`, `lightingId`, `expressionId`.

El perfil se referencia, no se copia. Su ID no incorpora versión. Estos rasgos no deben duplicarse como tags.

## 12. Procedencia

`provenance.originKind` es obligatorio y admite:

- `generated`: requiere `generator.provider` y `generator.generatedAt`; el modelo es opcional si no se conoce.
- `imported`: puede registrar `importedAt`.
- `edited` o `derived`: requiere uno o más `sourceAssetIds`.
- `unknown`: se reserva para una fuente que realmente no puede determinarse, no para un formulario incompleto.

Puede referenciar `promptTemplateId` + `promptTemplateVersion` y un `promptRecordId`. El prompt completo, conversaciones privadas, secretos y credenciales quedan fuera. El perfil visual aplicado vive únicamente en `visual` para evitar dos valores contradictorios; junto con `provenance` forma la trazabilidad de generación.

Las relaciones históricas no se eliminan durante una migración. El schema no puede comprobar que un asset no se incluya a sí mismo en `sourceAssetIds`; esa regla corresponde a validación de dominio.

## 13. Content

`content` describe el binario canónico actual y requiere:

- `mimeType` de imagen;
- `widthPx` y `heightPx` positivos;
- `sha256` hexadecimal en minúsculas de 64 caracteres.

`byteSize` y `colorSpace` son opcionales. Todos son calculados por el procesador, no editados manualmente. `sha256` permite verificar integridad y detectar duplicados exactos, pero dos archivos técnicamente distintos pueden representar el mismo asset lógico tras una conversión autorizada.

Miniaturas, caches y resultados de validación son derivados y no pertenecen a este bloque v1.

## 14. Storage

`storage.replicas` representa cero o más ubicaciones conocidas; si no hay ninguna, se omite todo `storage`. Cada réplica declara:

- `replicaId`: clave local a la ficha para actualizar esa entrada;
- `locationType`: `local` o `remote`;
- `purpose`: `primary`, `backup` o `cache`, opcional;
- `provider`: adaptador genérico, por ejemplo `filesystem`; no se fija ImageKit;
- al menos uno de `objectId`, `logicalPath` o `deliveryUrl`.

`logicalPath` se interpreta respecto a una raíz gestionada por la biblioteca, nunca como ruta absoluta de un dispositivo. `deliveryUrl` es opcional, reemplazable y potencialmente efímera. Ni el asset, ni el catálogo, ni un savegame dependen de ella.

Las colas, errores, reintentos y conflictos de una réplica no se guardan aquí: son estado operacional local.

## 15. Extensions

`extensions` admite objetos bajo claves con namespace, por ejemplo:

```json
{
  "extensions": {
    "dev.nimroel.production": {
      "reviewNote": "dato experimental"
    }
  }
}
```

Una extensión no puede redefinir un campo canónico, ser necesaria para resolver el asset ni contener secretos. Si se vuelve necesaria para producción, debe promocionarse en una versión futura del contrato mediante migración explícita.

## 16. Qué queda fuera del schema

- estado local `pending_upload`, `uploading`, `synced`, `failed`, `retry`, `conflict`;
- URI Android, rutas absolutas, nombres originales de importación y estado de UI;
- credenciales, tokens, claves privadas, URLs firmadas y logs internos;
- prompts completos y conversaciones privadas;
- fichas completas de lore, perfiles visuales o vocabularios;
- índice del catálogo, revisión operacional e historial de migraciones;
- thumbnails, caches y variantes técnicas regenerables.

## 17. Política de sustitución visual

Se crea un **nuevo `assetId`** cuando cambia materialmente lo que verá el jugador: otra cara, otra ilustración, una regeneración con resultado distinto, otra composición o una sustitución visual sustancial.

Se conserva el `assetId` cuando sólo cambian metadata, clasificación, tags, procedencia completada, estado editorial, versión de schema, almacenamiento, thumbnail o una conversión/recompresión técnica que mantenga exactamente la misma representación visual.

Esta regla protege savegames: una referencia antigua nunca debe mostrar de forma silenciosa una cara o escena nueva. El asset anterior puede pasar a `deprecated` y señalar `lifecycle.supersededByAssetId`.

## 18. Versionado y migraciones

- `schemaVersion` vale exactamente `1` en este contrato.
- Un cambio aditivo que los lectores v1 puedan ignorar puede documentarse sin romper v1 sólo si no modifica validación/semántica existente; dado el uso de `additionalProperties: false`, normalmente requerirá publicar una revisión formal del schema y coordinar lectores.
- Cambios de estructura, significado, obligatoriedad o tipos admitidos originan v2.
- Una migración v1→v2 conserva `assetId`, procedencia histórica y significado visual.
- Las migraciones deben ser idempotentes, probadas con fixtures y no sobrescribir la única copia si fallan.
- Los clientes pueden migrar al abrir o mantener lectores paralelos durante una transición; assets antiguos no dejan de existir por aparecer v2.

La versión de schema es independiente de `visualProfileVersion`, `promptTemplateVersion` y `vocabularyVersion`.

## 19. Compatibilidad con Asset Resolver

El futuro Resolver podrá consultar o indexar:

- `assetId` para resolución directa desde savegames;
- `type`, `lifecycle.status`, clasificación, `subject.entityId` y `details`;
- perfil y rasgos visuales;
- MIME, dimensiones y hash para compatibilidad/integridad;
- réplicas publicadas a través del catálogo.

El Resolver no infiere identidad desde paths, nombres o URLs. Debe obtener una ubicación disponible para un `assetId`, y excluir por política borradores, retirados o réplicas no publicables. La selección de variantes por plataforma/resolución será un contrato posterior.

## 20. Ejemplos completos

Los fixtures JSON forman parte del contrato v1 y se validan contra el schema:

| Caso | Fixture |
|---|---|
| Campesina adulta de Valemar | `../contracts/examples/npc-portrait-valemar-farmer.json` |
| Soldado de Norgard | `../contracts/examples/npc-portrait-norgard-soldier.json` |
| Bosque de Valemar | `../contracts/examples/landscape-valemar-forest.json` |
| Interior de taberna humilde | `../contracts/examples/interior-humble-tavern.json` |
| Retrato de personaje canónico sin lore inventado | `../contracts/examples/npc-portrait-canonical-character.json` |

Los cinco son fichas completas y validables, no fragmentos. El personaje canónico mantiene `type: npc_portrait` y usa `subject.entityId`. Los hashes son valores sintácticamente válidos reservados para fixtures, no hashes de imágenes reales.

## 21. Reglas no expresables completamente en JSON Schema

La validación de dominio deberá comprobar además:

- unicidad global de `assetId` en el catálogo;
- que `sourceAssetIds` no incluya el propio asset ni produzca ciclos indebidos;
- existencia de IDs y versiones en lore, vocabularios, perfiles y templates;
- correspondencia entre `content.sha256` y el binario;
- que rutas lógicas no escapen de la raíz de biblioteca;
- que `supersededByAssetId` no se autorreferencie;
- cumplimiento de la política de cambio visual material.

## 22. Decisiones todavía abiertas

1. Definir el primer registro versionado de vocabularios y sus valores reales.
2. Definir la fuente canónica y formato de `subject.entityId` para entidades de lore.
3. Diseñar revisión/auditoría del catálogo y concurrencia entre Android y Windows.
4. Precisar el ciclo editorial permitido y las transiciones entre estados.
5. Diseñar variantes técnicas reproducibles si WebP, original y thumbnails necesitan coexistir como contenidos diferenciados.
6. Decidir qué localizadores de `storage` se exportan al catálogo público y cuáles permanecen locales.

Estas decisiones no cambian las decisiones de arquitectura ya aprobadas, pero deben cerrarse antes de implementar persistencia y sincronización completas.

## 23. Validación reproducible

El contrato se valida con AJV 8 mediante `ajv-cli` y el plugin de formatos:

```powershell
npx --yes --package ajv-cli@5.0.0 --package ajv-formats@3.0.1 ajv validate --spec=draft2020 --all-errors -c ajv-formats -s contracts/asset-schema-v1.schema.json -d "contracts/examples/*.json"
npx --yes --package ajv-cli@5.0.0 --package ajv-formats@3.0.1 ajv test --spec=draft2020 -c ajv-formats -s contracts/asset-schema-v1.schema.json -d "contracts/test-fixtures/invalid/*.json" --invalid
```

El primer comando exige que todos los ejemplos de producción sean válidos. El segundo exige que fallen los casos de ID incorrecto, tipo desconocido, `details` incompatible, versión de schema incorrecta y contenido obligatorio ausente.

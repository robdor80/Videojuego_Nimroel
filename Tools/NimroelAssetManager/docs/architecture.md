# Arquitectura del Asset Manager

## Decisiones adoptadas

- Android nativo con Kotlin, Compose y Material 3; mínimo SDK 26 y compilación/objetivo SDK 36.
- Separación de contratos compartibles (`contracts/`) y la implementación Android (`android/`).
- Asset Schema v1 es el contrato canónico multiplataforma en `contracts/asset-schema-v1.schema.json` y dispone de representación, serialización y validación Kotlin independiente de Android.
- Vocabulary v1 define valores editoriales versionados; Vocabulary Set v1 enlaza rutas canónicas con vocabularios/versiones; Preset v1 precarga valores mediante un único set.
- Los JSON compartidos bajo `contracts/` son fuente de verdad para estos contratos. Kotlin, Android y la futura herramienta Windows son consumidores.
- `RemoteAssetStore` es una frontera de dominio, no una implementación de ImageKit. No contiene ni admite credenciales privadas cliente.
- La persistencia local Room v1 está implementada con `canonical_json` como fuente de verdad, proyecciones reconstruibles, tablas operacionales separadas e inventario independiente de representaciones físicas.
- Room DB version 1 exporta su schema de forma reproducible. La API tipada actual sólo admite Asset Schema v1; la columna `canonical_json` permite conservar documentos futuros, pero su lectura/edición queda bloqueada hasta disponer de un codec y validador compatibles.

## Capas Android

- `domain/`: modelos y contratos de negocio independientes de UI/proveedor; incluye Production Draft v1 como flujo puro Preset → Vocabulary Set → Vocabulary → borrador → Asset validado.
- `data/`: Room DB v1, DAOs, conversores, proyección del documento canónico y `RoomLocalAssetStore`; el procesamiento se añadirá cuando se definan sus necesidades concretas.
- `ui/`: Compose y ViewModels; no debe alojar reglas de schema ni persistencia.
- `sync/` y `processing/`: se crearán junto con operaciones reales y pruebas; WorkManager será el candidato para colas fiables de sincronización.

## Estado de hitos

- Completado: Asset Schema v1 y sus fixtures.
- Completado: adaptación Kotlin, serialización y validación de dominio.
- Completado: Vocabulary v1, Vocabulary Set v1 y Preset v1, con registros piloto limitados a valores confirmados.
- Completado: persistencia local Room v1 descrita en `local-persistence-v1.md`, incluido el schema exportado y las pruebas de integración en memoria.
- Completado: Production Draft v1 para `npc_portrait`, con resolución versionada, semántica fixed/suggested, edición validada y materialización de Asset Schema v1.
- Completado: interfaz Android “Nueva producción” v1, conectada al Production Draft y a los contratos compartidos empaquetados en runtime, con edición responsive y resumen reactivo.

## Decisiones aún abiertas

1. Completar las taxonomías editoriales necesarias para producción.
2. Definir perfiles visuales y prompt templates versionados de producción.
3. Definir la fuente canónica de IDs de entidades de lore.
4. Cerrar la política de retención del original y ubicación de archivos administrados.
5. Definir backend/autenticación y almacenamiento remoto sin credenciales privadas en clientes.
6. Precisar ciclo editorial y resolución de conflictos cuando se diseñe sincronización.

## Próximo hito

Implementar la selección/importación local de imagen y preparar el `Content` necesario para el siguiente paso del flujo, sin adelantar las decisiones abiertas de persistencia, retención, procesamiento remoto, sincronización ni Asset Resolver.

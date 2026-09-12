# Arquitectura del Asset Manager

## Decisiones adoptadas

- Android nativo con Kotlin, Compose y Material 3; mínimo SDK 26 y compilación/objetivo SDK 36.
- Separación de contratos compartibles (`contracts/`) y la implementación Android (`android/`).
- Asset Schema v1 es el contrato canónico multiplataforma en `contracts/asset-schema-v1.schema.json` y dispone de representación, serialización y validación Kotlin independiente de Android.
- Vocabulary v1 define valores editoriales versionados; Vocabulary Set v1 enlaza rutas canónicas con vocabularios/versiones; Preset v1 precarga valores mediante un único set.
- Los JSON compartidos bajo `contracts/` son fuente de verdad para estos contratos. Kotlin, Android y la futura herramienta Windows son consumidores.
- `RemoteAssetStore` es una frontera de dominio, no una implementación de ImageKit. No contiene ni admite credenciales privadas cliente.
- La persistencia local v1 adopta `canonicalJson` en Room con proyecciones reconstruibles, tablas operacionales separadas e inventario independiente de representaciones físicas. Room se implementará en el siguiente hito.

## Capas Android

- `domain/`: modelos y contratos de negocio independientes de UI/proveedor.
- `data/`: repositorios, Room y procesamiento cuando se definan sus necesidades concretas.
- `ui/`: Compose y ViewModels; no debe alojar reglas de schema ni persistencia.
- `sync/` y `processing/`: se crearán junto con operaciones reales y pruebas; WorkManager será el candidato para colas fiables de sincronización.

## Estado de hitos

- Completado: Asset Schema v1 y sus fixtures.
- Completado: adaptación Kotlin, serialización y validación de dominio.
- Completado: Vocabulary v1, Vocabulary Set v1 y Preset v1, con registros piloto limitados a valores confirmados.
- Diseñado, pendiente de implementación: persistencia local v1 descrita en `local-persistence-v1.md`.

## Decisiones aún abiertas

1. Completar las taxonomías editoriales necesarias para producción.
2. Definir perfiles visuales y prompt templates versionados de producción.
3. Definir la fuente canónica de IDs de entidades de lore.
4. Cerrar la política de retención del original y ubicación de archivos administrados.
5. Definir backend/autenticación y almacenamiento remoto sin credenciales privadas en clientes.
6. Precisar ciclo editorial y resolución de conflictos cuando se diseñe sincronización.

## Próximo hito

Implementar Room DB version 1 a partir de `local-persistence-v1.md`: documento canónico, proyecciones, estado local, representaciones físicas y trabajos de ingestión. La implementación debe permanecer desacoplada de ImageKit, sincronización, importación UI y Asset Resolver.

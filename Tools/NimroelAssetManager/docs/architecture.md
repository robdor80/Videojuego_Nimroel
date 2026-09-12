# Arquitectura inicial y decisiones abiertas

## Decisiones adoptadas

- Android nativo con Kotlin, Compose y Material 3; mínimo SDK 26 y compilación/objetivo SDK 36.
- Separación de contratos compartibles (`contracts/`) y la implementación Android (`android/`).
- El dominio Android continúa siendo un cimiento mínimo. Asset Schema v1 es el contrato canónico multiplataforma en `contracts/asset-schema-v1.schema.json`; su adaptación completa a Kotlin pertenece al siguiente hito.
- `RemoteAssetStore` es una frontera de dominio, no una implementación de ImageKit. No contiene ni admite credenciales privadas cliente.
- Room se pospone: primero debe diseñarse correctamente el modelo de persistencia local y separarse el contrato canónico del estado operacional de cada instalación.

## Capas Android

- `domain/`: modelos y contratos de negocio independientes de UI/proveedor.
- `data/`: repositorios, Room y procesamiento cuando se definan sus necesidades concretas.
- `ui/`: Compose y ViewModels; no debe alojar reglas de schema ni persistencia.
- `sync/` y `processing/`: se crearán junto con operaciones reales y pruebas; WorkManager será el candidato para colas fiables de sincronización.

## Decisiones pendientes antes de la siguiente fase

1. Adaptar Asset Schema v1 al dominio Kotlin mediante modelos, validadores y mapeos, sin convertirlo todavía en entidades Room.
2. Definir los registros versionados de vocabularios, perfiles visuales y presets.
3. Definir la fuente canónica de IDs de entidades de lore.
4. Modelo de almacenamiento local (original, WebP, miniaturas, hashes) y política de retención.
5. Backend de autenticación segura y rutas de almacenamiento ImageKit.
6. Reglas de validación de dominio, ciclo editorial y resolución de conflictos de sincronización.

## Próximo hito

Adaptar Asset Schema v1 al dominio Kotlin mediante modelos, validadores y mapeos, todavía sin convertirlo en entidades Room. Después se puede diseñar persistencia e importación local sin acoplarse al proveedor remoto.

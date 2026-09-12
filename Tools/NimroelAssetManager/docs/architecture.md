# Arquitectura inicial y decisiones abiertas

## Decisiones adoptadas

- Android nativo con Kotlin, Compose y Material 3; mínimo SDK 26 y compilación/objetivo SDK 36.
- Separación de contratos compartibles (`contracts/`) y la implementación Android (`android/`).
- El dominio contiene únicamente invariantes seguros: `AssetId`, `schemaVersion`, hash opcional y estado local.
- `RemoteAssetStore` es una frontera de dominio, no una implementación de ImageKit. No contiene ni admite credenciales privadas cliente.
- Room se pospone: una tabla creada ahora congelaría campos y relaciones de un schema que aún está deliberadamente abierto.

## Capas Android

- `domain/`: modelos y contratos de negocio independientes de UI/proveedor.
- `data/`: repositorios, Room y procesamiento cuando se definan sus necesidades concretas.
- `ui/`: Compose y ViewModels; no debe alojar reglas de schema ni persistencia.
- `sync/` y `processing/`: se crearán junto con operaciones reales y pruebas; WorkManager será el candidato para colas fiables de sincronización.

## Decisiones pendientes antes de la siguiente fase

1. Schema v1: campos obligatorios/opcionales, extensiones y estrategia de migración.
2. Convención de `assetId`, incluyendo asignación de secuencias y unicidad local/remota.
3. Taxonomía, perfiles visuales, presets y sus fuentes versionadas.
4. Modelo de almacenamiento local (original, WebP, miniaturas, hashes) y política de retención.
5. Backend de autenticación segura y rutas de almacenamiento ImageKit.
6. Reglas de validación, ciclo de vida y resolución de conflictos de sincronización.

## Próximo hito

Diseñar y versionar el schema v1 junto con una taxonomía mínima y ejemplos reales. Después se puede añadir Room mediante migraciones explícitas e implementar importación local sin acoplarse todavía al proveedor remoto.

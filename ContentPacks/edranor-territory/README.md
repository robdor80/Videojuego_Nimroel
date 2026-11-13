# EDRANOR E11 — Catálogo estructural 0.1.0

**Estado:** referencias compatibles con CoreRPG Content Contract JSON 0.1.0. No es un territorio jugable ni activa reglas de juego.

## Contenido
- `pack/manifest.json`: catálogo `nimroel.edranor.territory`, cinco referencias tipadas y enlaces locales comprobables.
- `pack/resources/territory/edranor.json`: enlace desde la Casa a Dorth, Lumina, Karsath y Rodas **sin atribuir dominio de Rodas**.
- `pack/resources/places/*.json`: Dorth ciudad, Lumina y Karsath asentamientos canónicos, Rodas **aldea bajo Corona Aethros**.
- `authoring/projection-v0.1.json`: procedencia E00–E10, autoridad por localidad, deuda y salvaguardas; **no se envía como ResourceDefinition**.
- `fixtures/e11-scenarios-v0.1.json`: doce especificaciones de laboratorio TEST_ONLY, no hechos de mundo.

## Frontera técnica
El Content Contract 0.1.0 solo admite `id`, `kind`, `references` y el `$schema` permitido. Jurisdicción, población desconocida, validaciones y propuestas E10 se guardan en el sidecar; nunca se añaden campos inventados a CoreRPG. El catálogo puede ser leído por CoreRPG, pero **no se asegura integración de Godot, mapas, NPC, rutas, economía, misiones ni sincronización de World State**.

## Fuentes y pruebas
Los 11 `sourceLocks` exigen hashes de blob Git exactos E00–E10. La validación verifica también E00/E05/E06/E07/E08/E09/E10, 37 mutaciones adversariales, esquema oficial de CoreRPG y prueba nativa C++ de catálogo y persistencia TEST_ONLY en CI Windows/Linux.

Ejecutar `python Tools/EdranorE11/validate.py --core-root .edranor-core` tras obtener CoreRPG en el commit fijo `4f282863737bcd8f5add401202a9e1064c133672`. El workflow compila `Tools/EdranorE11`; solo se declaran pruebas ejecutadas cuando conste resultado real.

Rodas no es un feudo Edranor; Hallheim no pertenece a este catálogo. Nunca instanciar la genealogía E10 antes de ratificar EDD-05 y validar NAME/KIN.

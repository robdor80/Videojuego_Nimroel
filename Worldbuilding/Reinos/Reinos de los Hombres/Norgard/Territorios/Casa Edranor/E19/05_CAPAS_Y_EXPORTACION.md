# E19 — Catálogo de capas y exportación segura a Godot 2D

La fábrica de mundos reutilizará CoreRPG/Norgard Defaults, no implementará nuevo clima, drenaje, economía ni sistema de propiedad. Las capas se diseñan como datos referenciables, no como motor paralelo.

| ID | Capa | Estado real E19 |
|---|---|---|
| L00 | Mapa fuente + licencias/hashes | GENERAL verificado, recorte autoral pendiente |
| L01 | Perímetro, jurisdicciones y excepciones | BLOCKED EDD-01/02 |
| L02 | Hitos geológicos/topónimos/anclas | Anclas nominales, sin puntos |
| L03 | DEM y tile heightfield | BLOCKED EDD-02/03 |
| L04 | Divisorias y cuencas | BLOCKED EDD-03 |
| L05 | Hidrografía/receptores | Solo referencias regionales |
| L06 | Clima y suelos | Clasificación E03/E13, sin polígonos |
| L07 | Vegetación/forestal | Bosque Alto/Azurios, sin geometría ni permisos nuevos |
| L08 | Parcelas, aprovechamientos, restricciones | Sin parcelas |
| L09 | Vías/puentes/accesos | Grafo físico vacío, EDD-07 |
| L10 | Núcleos, edificios e interiores 2D | Cinco anclas nominales; E20–E24 |
| L11 | Persistencia y World State | Sin integración/instancias, E28 |

## Formato de datos futuro
`FeatureCollection` de geometrias revisadas con `sourceId`, `authority`, `confidence`, `crsId`, `version`, `jurisdictionOwner`, `featureId`, `validFrom` si aplica y `license`. Para trazas, añadir `crossingRights`, `slopeProfile`, `passability`. Para aguas: `drainTo` y procedencia. Para tiles: `tileOrigin`, `pixelResolution`, `nodata`, `heightDatum`, checksums.

No se emite GeoJSON con geometría vacía **disfrazada** de territorio válido. El JSON E19 es un contrato de bloqueo explícito; los campos geométricos permanecen `null` o colecciones vacías, `runtimeEnabled=false`.

## Gobiernos de importación
- Los recursos L00/L02 pueden servir a una UI de consulta no métrica, siempre con leyenda de incertidumbre.
- Prohibido activar triggers de propiedad, colisión, spawn, tala, captaciones, movimiento o impuestos por datos E19 preliminares.
- Godot 4.7.2 Standard (2D), Windows x64 y Android ARM64 son consumidores futuros de E28; este corte no modifica `Game`, `ContentPacks`, `CoreRPG` ni `main` directamente.
- Cada capa exportada tendrá versión, origen, firma/hash, validación por lotes y prueba de importación idempotente.
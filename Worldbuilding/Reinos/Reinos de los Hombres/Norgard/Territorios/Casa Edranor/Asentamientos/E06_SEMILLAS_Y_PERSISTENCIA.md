# E06 — Laboratorio determinista y contrato de integración futura
El laboratorio está en `Tools/EdranorE06/lab.py`; no modifica escenas Godot, CoreRPG, partidas ni Content Packs.

## Identidad y aleatoriedad aislada
`stableId = "edr_e06_test_" + first16hex(sha256(json_utf8_compact(["edranor-e06/v0.1", worldSeed, studyZoneId, slotId])))`.

Para modelo: `sha256(json_utf8_compact([worldSeed, stableId, "model", "0.1"]))`, primeros 8 bytes big-endian sin signo módulo suma de pesos elegibles ordenados lexicográficamente por ID. La serialización usa JSON arrays con `ensure_ascii=False` y `separators=(",",":")`. No utiliza RNG global, no depende del orden de catálogo ni del nombre de localidad. `slotId` empieza por `sandbox_`: **NO** es geolocalización. Las ponderaciones pueden cambiar resultados en nuevas versiones: versionar y migrar; nunca regenerar partidas silenciosamente.

## Proyección sin materialización
Todo resultado positivo contiene `provenance=TEST_ONLY`, `canonical=false`, `materialized=false`, `visibleName=null`, `coordinates=null`, `population=null`, `worldStateId=null`; hogares, NPC, edificios, servicios, inventarios y rutas son listas vacías. `potentialBuildings` y `potentialServices` son *catálogos condicionales*, no objetos.

El resultado negativo tiene motivos explícitos (protección canónica, falta de agua, zona cerrada, derechos, jurisdicción, etc.) y ningún ID materializable.

## Puertas E11
Para activar en el futuro: mapa del perímetro aprobado y revisión; prueba geográfica del sitio y huella de Dorth/Lumina/Karsath/Rodas; titularidad y derechos; agua/suelo/riesgos; red física y derechos de paso; distribución/demanda de hogares E08; límites de carga y reglas de cuota; contrato estable de IDs; sincronización CoreRPG ↔ Godot y persistencia Windows x64/Android ARM64. El World State debe actualizar necesidades sin resembrar aldeas cada vez que cambia el clima o la ruta.

**Prohibido activar E06 trasladando booleanos `*_Verified` de fixtures al mundo real.** Son pruebas sintéticas sin procedencia de observación real.

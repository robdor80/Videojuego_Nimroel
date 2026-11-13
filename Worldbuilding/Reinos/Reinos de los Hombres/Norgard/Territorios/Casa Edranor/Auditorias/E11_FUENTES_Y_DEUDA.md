# E11 — Evidencia, trazabilidad y deuda territorial

## Trazabilidad inmovilizada
Los `sourceLocks` cubren E00 a E10 con SHA reales de sus JSON documentales (consultar `ContentPacks/edranor-territory/authoring/projection-v0.1.json`). Si cualquier fuente cambia, se exige revisar la proyección y regenerar el lock de forma razonada; jamás reajustarlo a ciegas.

## Canon protegido (E00/E07/E08/E09/E10)
- Dorth es ciudad y sede de Edranor; Lumina asentamiento compacto de blancos; Karsath asentamiento pequeño y vino escaso, ribera no adjudicada.
- Rodas es **aldea Corona Aethros**. Su justicia, fiscalidad, seguridad y mando berserker no se transfieren a Edranor. Casa Druídica custodiada ≠ templo ni culto ambiental.
- Hallheim fuera del perímetro; la representación espacial de Edranor no extiende la jurisdicción de Casa.
- Una Corona y una ley, moneda común, sin aduana interior, ejército soberano ni ceca de Casa.
- E07/E08/E09 no ofrecen coordenadas, habitantes, rutas físicas, edificios, funcionarios ni inventarios instanciados.
- E10 propone 11 identidades de diseño, ocho conflictos y ocho escenas. Permanecen **no ejecutables**, sin bautismo NPC/NAME-KIN, tratados fechados o consecuencias de World State.

## Deuda explícita
`EDD-01` borde norte, `EDD-02` escala y georreferencia, `EDD-03` hidrografía, `EDD-04` censos, `EDD-05` persona titular y árbol familiar jurídico, `EDD-07` enlaces físicos y `EDD-08` actos fechados. Resolver cada cuestión con fuente superior o autorización editorial, no con heurísticas del motor.

## Evidencia y alcance de pruebas
- Validación estática: integridad de hashes, esquema de proyección, contrato Core oficial y rechazo de mutaciones; regresión E00–E10.
- C++ real: carga de paquete/DefinitionId, binding sintético, captura/serialización/restauración, determinismo y rechazo sin catálogo.
- **No certifica** Godot GDExtension, navegación 2D, combate, logística, permisos administrativos, NPC/diálogo, ejecución de misiones ni persistencia de escenas reales.
- No modificar `Norgard Defaults`, `grandes_casas.md`, CoreRPG ni Godot: E11 es un paquete agregado, no una migración de motor.

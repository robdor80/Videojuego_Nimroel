# Acta técnica E11 — Casa Edranor
**Fecha:** 13/11/2026 · **Estado:** entrega E11 técnicamente conforme en PR #63; su fusión queda sujeta al HEAD final y a las puertas de gobierno.

## Entrega verificada
1. Pack `nimroel.edranor.territory`: cinco DefinitionIds y enlaces tipados, conforme a CoreRPG Content Contract JSON 0.1.0.
2. Proyección autoral: once SHA de blob de E00–E10, cuatro anclas protegidas, autoridad de Rodas en Corona Aethros y Hallheim fuera.
3. Doce escenarios `TEST_ONLY`, ninguno convertido en suceso canónico.
4. Validador Python que rechaza **37 mutaciones adversariales** y comprueba fuentes, contratos oficiales y regresiones E00–E10.
5. C++ CoreRPG real: cinco recursos de catálogo, dos bindings **sintéticos** (Dorth y Rodas), serialización/restauración, bytes iguales con semilla idéntica y rechazo de restauración si falta catálogo.

## Evidencia CI
- **Ejecución de referencia:** [GitHub Actions #43335463248](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43335463248).
- **HEAD probado de la ejecución:** `52891d2b0b6eb74789f3c8659ad5ab7fbe208d10`.
- **Ubuntu 24.04:** regresiones E00–E10, validación E11, schema oficial CoreRPG, CMake C++ y CTest: **SUCCESS**.
- **Windows 2022:** misma matriz: **SUCCESS**.
- Las 22 comprobaciones históricas separadas de E00–E10 (más la base) están verdes en ese HEAD.
- Si este acta u otro documento desplazan HEAD, la nueva ejecución también deberá aprobarse antes de fusionar.

## Restricciones
Ninguna prueba certifica Godot 4.7.2, GDExtension, contenido poblado, navegación, justicia y fiscalidad ejecutables, permisos, escenas, NPC, misiones o simulación de Mundo. E10 es `PROPUESTA_E10`, pendiente de ratificar EDD-05 y demás deuda. El C++ creó dos entidades de laboratorio, **no** ciudadanos del videojuego.

## Puertas restantes
Verificar checks del HEAD definitivo (Ubuntu y Windows), confirmar diff circunscrito a E11 (18 rutas; sin canon histórico ni CoreRPG/Game), comprobar `main` no desplazada, pasar PR #63 a ready y fusionar únicamente si todas las puertas se mantienen verdes. E12 será fase independiente.

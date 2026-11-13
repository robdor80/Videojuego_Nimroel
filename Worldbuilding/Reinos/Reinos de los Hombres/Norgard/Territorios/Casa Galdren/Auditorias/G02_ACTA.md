# G02 — Acta de entrega condicionada a CI y revisión
**13/11/2026 · fase G02 · modalidad autónoma sin Codex.**

## Alcance y contabilidad verificable
- **5 ríos canónicos referenciados:** Caleran, Vornarsk, Keldarsk (contexto Galdren) y Sareno, Theleno (contexto de Valrik).
- **1 sistema Caleran, 2 brazos con nombre ya existente**, 2 bifurcaciones ulteriores sin nombres nuevos. Número de desembocaduras finales no establecido.
- **5 expedientes de cuenca no delimitados**, **6 interfaces de aguas pendientes**, **5 expedientes de riesgo**, **10 rutas de fuente versionada**.
- **0** ríos, afluentes, arroyos, lagos, puertos, puentes, canales o estaciones con nombre creados; **0** polígonos/caudales/cotas locales añadidos.
- Documento contractual `galdren_g02_hydrology_v0.1.json` con `runtimeEnabled=false`. No se modifica CoreRPG, Godot, Norgard superior ni Casas vecinas.

## Puertas de fusión
1. Regresión G00 → G01 → G02 y pruebas adversariales G02 verdes en Ubuntu 24.04 y Windows 2022 **para el HEAD exacto**.
2. Diff exclusivamente bajo `Casa Galdren/`, `Tools/GaldrenG02/` y workflow G02; sin cambios de canon superior.
3. Contrato no-runtime, 5 cursos fijados, separación Valrik, dudas Azurios y Zanthir sin «solución» añadida, fuentes comprobadas.
4. `main` verificada sin deriva incompatible; PR fusionable.

**No declarar SUCCESS, cierre fusionado o funcionalidad jugable antes de evidencia real.** Esta acta es una checklist de aceptación, no un registro ficticio de pruebas.

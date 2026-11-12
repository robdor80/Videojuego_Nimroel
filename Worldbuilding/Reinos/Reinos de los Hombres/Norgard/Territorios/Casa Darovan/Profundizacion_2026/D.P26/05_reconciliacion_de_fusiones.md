# D.P26/05 — Reconciliación final de D.P23, D.P24 y D.P25

**Fecha:** 12/11/2026. **Alcance:** verificación tras fusión autorizada por el autor de las tres PR predecesoras. Este documento **actualiza** la incidencia administrativa A-01 del acta D.P26/04, sin falsificar el estado histórico inicial de la auditoría.

## Autorización y secuencia real

El autor autorizó expresamente la fusión de las cuatro PR de cierre en orden `#46 → #47 → #48 → #49`. Se ha ejecutado y confirmado la secuencia de integración de las tres fuentes:

| Fase | PR fusionada | Commit de integración en main | Blob JSON idéntico al de su fuente |
|---|---|---|---|
| D.P23 — Treihord | [#46](https://github.com/robdor80/Videojuego_Nimroel/pull/46) | `dcb2bb8939ee6f62ca89ca926ea1f4afbf75dab0` | `0f6f2ecad7cbbd9adeb4290e15df6ed25b2b5d6b` |
| D.P24 — rural | [#47](https://github.com/robdor80/Videojuego_Nimroel/pull/47) | `21712c17d1369f4979a518247ec040f44c529ab9` | `5a2c41e07c654ef15f751dd07d3670c0468a3bfc` |
| D.P25 — personas y conflictos | [#48](https://github.com/robdor80/Videojuego_Nimroel/pull/48) | `50e2412dc2160b3bb5bf5abef0d04382160807d2` | `8fb6ef595138581781a202dcd95d95f56a0dd504` |

**Base integrada certificada para el cierre de D.P26:** `main` tras la PR #48, commit `50e2412dc2160b3bb5bf5abef0d04382160807d2`.

## Método y hallazgos

1. Confirmación de PR cerrada y `merged=true` de #46, #47 y #48, con SHA de merge concreto.
2. Comparación de cada JSON integrado en `main` con el correspondiente JSON de su fuente D.P23/D.P24/D.P25 fijada por SHA. **Tres blobs idénticos**: no existen reescrituras, pérdidas de biografías, renumeraciones ni sustituciones ocultas por el proceso de fusión.
3. D.P25 sigue seleccionando 27 de los mismos 52 perfiles fuente sin desactivar a los restantes 25. Sus treinta relaciones y diez conflictos siguen siendo editoriales y condicionales.
4. D.P23, D.P24 y D.P25 se agregaron como **nuevos archivos independientes**, sin modificar contenidos previos de CoreRPG/Godot, contratos originales o el manuscrito canónico `Treihord.md`.
5. El validador D.P26 verifica **en el checkout integrado real** las tres huellas Git declaradas, además de repetir la verificación del catálogo completo con las fuentes ancladas. No le basta con aprobar los SHAs de ramas que aún no se hubieran incorporado.

## Estados de cierre por momento

- **Antes de las fusiones**, el manifiesto D.P26 recoge el estado histórico correcto: #46/#47/#48 eran Draft, sin integrar en la línea base `512434957f248f2513761615a9685ddd6c49c65f`. Es un registro de auditoría, no una afirmación sobre la situación actual.
- **Ahora**, al redactar este documento, las tres fuentes están **fusionadas**. La advertencia de dependencia upstream de D.P25 queda **resuelta a efectos de contenido**.
- **PR #49 (D.P26):** todavía se encuentra en proceso de revisión y cierre mientras se certifica su HEAD definitivo. Su acto de fusión y la verificación postmerge se consignarán en la PR y en GitHub Actions tras completarse, no se inventan aquí anticipadamente.

## Dictamen

**DEPENDENCIAS EDITORIALES RESUELTAS** y fuentes reconciliadas. Los límites de alcance siguen intactos: sin geografía métrica, sin nuevo WorldState, sin NPC instanciados, sin hogares o recursos inventados ni misiones activas. La integración final de D.P26 y el CI postmerge todavía son condiciones para declarar el ciclo **administrativamente cerrado**.

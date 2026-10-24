# DAROVAN D04 — Validación CI real y cierre estático (21-10-2026)

**Estado:** D04 documentalmente completa y validada estáticamente en GitHub Actions. **NO nuevo canon; NO runtime.** PR de integración: [#20](https://github.com/robdor80/Videojuego_Nimroel/pull/20). Esta acta se redacta antes de conocer el resultado final de su merge; la PR de GitHub prevalece para comprobar ese estado.

## Origen y reparación
- PR #20 partió de main `df43be5`; desde entonces main avanzó 49 commits en ramas del proyecto. La comparación previa al cierre mostró los 19 archivos originales Darovan sin otros archivos y PR considerada fusionable. La comprobación debe repetirse antes del merge definitivo.
- Se detectó una desincronización no canónica: `DECISIONES_Y_BLOQUEOS.md` incluía `DAR-P10` y `DAR-P11`, pero el campo `approvals.pendingAuthor` y el test esperaban solo P01/P04/P07/P08/P09. Se añadieron P10 y P11 sin resolverlos ni elevar hipótesis a canon.
- Nuevo workflow: `.github/workflows/darovan-static-regression.yml`. Dispara en cambios Darovan, pull requests y pushes a main relacionados; `workflow_dispatch` disponible. No añade dependencias Python externas ni toca el juego.

## Evidencia ejecutada, NO simulada
[GitHub Actions: run 39583142837](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39583142837) en rama D04, HEAD `2d6e21ff3da2d869a4ebb1b8dc0740f9c103eebf`.

| Plataforma de CI | ID job | Conclusión | D01 | D02 | D03 | D04 |
|---|---|---|---|---|---|---|
| Ubuntu 24.04 | 119165399107 | `success` | STATIC OK | STATIC OK | STATIC OK | STATIC OK |
| Windows Server 2022 | 119165399471 | `success` | STATIC OK | STATIC OK | STATIC OK | STATIC OK |

Salidas D04 comprobadas en los registros de ambos jobs:

```text
D04 STATIC OK: 12 zones, 8 chains, 19 sources, 16 negative tests; NOT RUNTIME
```

El Python de ambos jobs cargó archivos **reales del checkout íntegro**, comparó D01/D02/D03, verificó contratos Core y fiscal Norgard y rechazó las 16 mutaciones negativas de D04. D01–D03 han vuelto a pasar íntegramente; la comprobación remota JavaScript histórica 22/22 queda conservada, no se suplanta.

## Alcance de la aceptación
- Aceptado: **cierre documental y validación Python estática multiplataforma de D04**, incluido control de regresiones territoriales anteriores.
- Sin ejecutar: **prueba específica D04 en MSI físico**, cartografía GIS, motor Godot/CoreRPG en runtime, inventario/producción real, contabilidad, navegación, persistencia. El MSI no es requisito técnico imprescindible para esta validación puramente documental; puede repetirse allí a voluntad.
- Ninguna aprobación de datos de autor: `newCanonApproved=false` y `DAR-P01/P04/P07/P08/P09/P10/P11` pendientes. La falta de cifras, ubicaciones y decisiones de canon se mantiene registrada y no bloquea cierre estático.

## Puerta de entrada D05
Solo después de comprobar `PR #20 merged=true` en GitHub y releer `00_Control_del_proyecto/TRASPASO_D05.md`. Esta acta **no inicia D05** ni acredita integración de los datos con el videojuego. Si hay nuevos cambios después del run acreditado, revisar el CI asociado al HEAD final de la PR.

# G04 — Acta de entrega, agricultura y economía alimentaria

**Fecha:** 13/11/2026. Estado: **DOCUMENTARY_PLANNING_ONLY**. El autor dio luz verde para **continuar** la siguiente fase después de G03; esto autoriza el trabajo y la fusión tras controles, **no** convierte en hechos canónicos las propuestas de producción o comercio.

## Entrega verificable
- Un atlas productivo con las 12 unidades G01 y sus limitaciones G03.
- Catálogo de cultivos Norgard, animales y alimentos, separado de la producción local confirmada.
- Especialización caballar del Bosque Quebrado respaldada en el canon de bosques; sin inventar razas ni censo.
- Seis modelos de cadenas, seis flujos de interés y diez condicionantes/riesgos.
- Calendario civil de Norgard (365 días/12 meses/cuatro estaciones) reconocido explícitamente y distinto del calendario agrícola local.
- Contrato JSON sin runtime, validador de mutaciones negativas y workflow CI con regresión G00–G04.
- Revisión de jerarquía G03→G04 en Auditorias/G04_FUENTES_Y_DEUDA.md.

## Puertas de cierre
- [x] G00–G04 PASS en Ubuntu 24.04 y Windows 2022 para el HEAD definitivo.
- [x] Comparación contra main sin deriva, archivos dentro de ámbitos permitidos.
- [x] Auditoría de cultivos (no patata canónica), ganado (no copiar distribución Treskal), caballos, suelos, autoridad fiscal, identidad de Casas y cronología civil.
- [x] Confirmar que no se inventaron producción, precios, aldeas, carreteras, puertos, infraestructura ni peligro ocurrido.
- [x] Fusionar únicamente con las puertas anteriores superadas.

**No incluye:** compilación CoreRPG C++20, GDExtension, Godot 4.7.2 2D, mapas, simulación económica, NPC vivos, compras o misiones implementadas.

**G05:** preparada en documento de traspaso, no iniciada.

## Certificación de entrega previa al cierre
- HEAD auditado antes de esta adenda: `1e259a4c41a96da6908d65bf6c176d2f423ea353`. Base main `0cec00d7b05a28972a9e6969279446aa0a6d119a`; diff 14 archivos (13 nuevos y README de Galdren actualizado), **sin modificar otros territorios, canon superior, CoreRPG ni Godot**.
- [CI G04 PR run #43355037462](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43355037462): **SUCCESS** Ubuntu 24.04 + Windows 2022 sobre el mismo HEAD. En cada sistema G00, G01, G02, G03 y G04 PASS.
- Regresiones documentales: G00 28, G01 49, G02 58, G03 86 y **G04 113 mutaciones negativas rechazadas**. No son pruebas de simulación económica ni ejecución del juego.
- Otros workflows PR [G00 #43355037568](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43355037568), [G01 #43355037672](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43355037672), [G02 #43355037493](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43355037493) y [G03 #43355037466](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43355037466): todos **SUCCESS** sobre el HEAD anterior.
- Tras esta adenda administrativa debe verificarse de nuevo CI en el HEAD final **antes de fusionar**. G05 permanece no iniciada.

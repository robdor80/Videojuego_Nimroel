# D11 — Acta técnica de auditoría y preparación para revisión

**Fecha:** 23/10/2026. **Estado:** fase técnica D11 construida, PR Draft #37 abierta; no fusionada, pendiente de autorización del autor. No se declara Casa Darovan jugable.

## Línea base certificada

- Videojuego_Nimroel main: a5d25d8e6a1d70015a63b0327837fd0da0004cbd; D10 PR #36 fusionada.
- Postmerge D10: Actions #40026616322 SUCCESS Ubuntu 24.04 y Windows Server 2022.
- CoreRPG main inspeccionado: 4f282863737bcd8f5add401202a9e1064c133672, versión con precedente 4.13 de Treskal.
- Rama D11 propia: feat/darovan-d11-integracion-contratos-pruebas. Sin cambios en main, Godot, GDExtension o repositorio CoreRPG.

## Evidencias de ejecución real de D11 (commit 4852c2af96ab151ac8b3cf17948e497032de5293)

[GitHub Actions #40029048181](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40029048181) — SUCCESS en Windows Server 2022 y Ubuntu 24.04.

- Regresión D01–D10: PASS en las dos matrices, sin saltarse fases.
- CoreRPG JSON Schema 0.1.0 originales, obtenidos por checkout del commit 4f28286: PASS en ambos sistemas.
- D11 fuente/sidecar: 11 SHA de blobs D00–D10, cinco definiciones estables, cuatro ciudades, cinco ríos/cuatro sistemas, tres enlaces físicos y cuatro suministros **no transitables automáticamente**, ocho escenarios TEST_ONLY: PASS.
- 23 mutaciones negativas adversariales: RECHAZADAS en ambos sistemas.
- Compilación real con CoreRPGContentJson, parser nativo C++: PASS Windows/Linux.
- CTest darovan_d11_core_catalog_smoke: 1/1 PASS en ambas plataformas. Carga cinco definiciones, binding TEST_ONLY y round-trip Persistence con catálogo.

**Verificación posterior al último cambio:** pendiente en la presente acta; el commit de refuerzo C++ de determinismo se revalidará en GitHub Actions sobre la PR. El link del run definitivo y su SHA se registrarán en la descripción de la PR sin tocar main.

## Alcance certificado y límites

Implementada una **proyección estructural mínima** verificable, no una simulación completa del reino. La existencia de un objeto JSON y de ResourceDefinition NO crea una ciudad, un hogar, un recurso comercial, una ruta o un personaje en WorldState. El C++ de laboratorio no representa un guardado del juego.

Se conserva la precedencia Nimroel Core → Norgard Defaults → Darovan → Localidad → World State a nivel documental. CoreRPG 0.1.0 no resuelve esa herencia ni interpreta el sidecar. Los escenarios T01–T08 siguen SPECIFICATION_NOT_EXECUTED por brechas de inventarios, producción, economía, permisos, rutas, hogares, tiempo, personalidad y Host. La prueba C++ comprueba un solo binding sintético y continuidad estructural, no materializa demografía D08. La prueba nueva de doble mundo y semilla igual cubre identidad de bytes de snapshot para **ese** estado sintético, no determinismo completo de simulación territorial.

No hay ejecución física en MSI Raider ni Samsung Tab S9+, ni pruebas Android/Godot/D11; CI Windows/Linux no equivale a hardware local. Arven conserva cultura UNKNOWN, Treihord sus ocho barrios, Karsath fuera, sin minas/caminos/puentes impuestos, sin personajes, fiestas, instituciones o hechos nuevos. D12 no se inicia.

## Dependencias e informe de cierre

Consultar matriz D11-A y peticiones CORE-REQ-D11-01..06 / NIM-HOST-D11-01 en Contratos_y_runtime/D11_ESTRATEGIA_INTEGRACION_Y_DEPENDENCIAS.md. No se abre ni modifica CoreRPG de oficio. Ninguna dependencia bloquea el **cierre de la preparación estructural D11**, aunque bloquea gameplay real de esos ámbitos.

**Decisión pendiente del autor:** revisión de PR Draft #37 y autorización explícita para fusionar. La presente acta no constituye tal autorización.

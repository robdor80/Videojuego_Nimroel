# D08 — Resolución autoral DAR-D08-01: Veldora (22/10/2026)

**Estado:** DECISIÓN AUTORAL APROBADA, intervalo canónico de población. Se registra **solo en la rama D08**; PR #34 Draft sin fusionar.

## Declaración del autor
«Apruebo la opción B para DAR-D08-01, población de Veldora. Registra la decisión en la rama D08 sin fusionar la PR y continuemos con la siguiente decisión de canon.»

**Opción B previamente ofrecida:** «29.000–35.000 habitantes — Gran ciudad comparable a Treihord». No se aprobó una cifra exacta ni un censo calculado.

## Hecho aprobado y límites
- **Veldora: intervalo demográfico de referencia de 29.000 a 35.000 habitantes, inclusivo.** Fuente: elección expresa del autor, no cálculo de CoreRPG, D04 o D07.
- Es un **rango canónico aprobado**; el valor de población exacto **permanece UNKNOWN** (`populationApprox: null`). No utilizar media aritmética ni muestreo de ese rango como nueva cifra oficial.
- **Treihord:** ~32.000, su cifra y diseño base cerrado no se alteran. No se deduce orden exacto de población entre Treihord y Veldora, dado que los rangos se solapan.
- **Taramin, Syvaris y población total de Darovan:** desconocidas hasta resoluciones separadas del autor.
- No fija densidad, hogares, pirámide de edad, ocupaciones, establecimientos, trabajadores, escuelas, muelles, rutas, patrimonio o capacidades. Veldora conserva la opción D07-B, **varios sectores comerciales orgánicos** como concepto sin urbanismo definitivo.
- No crea una reserva de población en CoreRPG: `PopulationRecord::declare_population` requiere grupo y total concretos; no hay instancia ni total seleccionado.

## Referencia operativa
`Datos operativos/darovan_d08_population_services_v0.1.json`, `cities[id=veldora].populationRange`: `minInclusive=29000`, `maxInclusive=35000`, `status=APPROVED_AUTHOR_RANGE`, `decisionId=DAR-D08-01`, `option=B`. `populationStatus=AUTHORED_RANGE`. El campo `populationApprox` sigue `null`.

## Control de cambios
Este anexo registra una aprobación sustantiva posterior al informe inicial D08 (21/10). Validador y esquema D08 actualizados para impedir transformar intervalo en cifra puntual o extenderlo a otras ciudades. Las pruebas estáticas no constituyen ejecución de mecánicas del juego. Ninguna PR será fusionada sin nueva orden expresa.

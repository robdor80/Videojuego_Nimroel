# Registro de fases — Casa Darovan
**Fecha de comprobación:** 21-10-2026. **Estados comprobados en GitHub el 21-10-2026:** D00–D04 integradas en main; D01–D03 Python MSI superados; D01–D04 Python GitHub Actions Windows/Linux superados. D05 documental en rama independiente, pendiente de auditoría/PR y decisión de merge.

| Fase | Entrega | Estado | Conversación |
|---|---|---|---|
| D00 | Canon, auditoría, estructura, metodología y protocolo | **FUSIONADA en main, PR #14** (merge commit 73aa5c4691a3dc07ca588c07a7ce267a69fdd085) | Darovan 1 |
| D01 | Geografía y orografía | **FUSIONADA EN MAIN, PR #15**, merge 9f3f723b0e7b2b78567c6397bba7099bfe658b0a | Darovan 2 |
| D02 | Hidrografía y cuencas | **FUSIONADA EN MAIN, PR #16**, merge 34c9652eba2bd0fed33ab6a3931f24400a39b812; no-runtime | Darovan 3 |
| D03 | Clima y ecosistemas | **FUSIONADA MAIN, PR #17 squash 191bcd5; PYTHON MSI D01–D03 SUPERADO**; 12 zonas de estudio cualitativas; no-runtime/no canon nuevo | Darovan 4 |
| D04 | Recursos y producción | **FUSIONADA EN MAIN**, PR #20, commit d4a07ba25f8560d5005a52aafc763699917f2388; CI D01–D04 Windows/Linux OK; no runtime | Darovan 5 |
| D05 | Movilidad y comunicaciones | **EN RAMA** feat/darovan-d05-rutas-comunicaciones; entrega estática en preparación para PR, sin canon nuevo ni runtime; merge requiere autor | Darovan 6 |
| D06 | Asentamientos procedurales | NO INICIADA | Darovan 7 |
| D07 | Ciudades canónicas | NO INICIADA | Darovan 8 |
| D08 | Población y servicios | NO INICIADA | Darovan 9 |
| D09 | Administración y defensa | NO INICIADA | Darovan 10 |
| D10 | Cultura y sociedad | NO INICIADA | Darovan 11 |
| D11 | Contratos y motor | NO INICIADA | Darovan 12 |
| D12 | Auditoría integral | NO INICIADA | Darovan 13 |

**Evidencia:** MSI físico (15-10-2026): D01/D02/D03 `STATIC OK` en checkout local (acta D03). CI Windows 2022 + Ubuntu 24.04 (21-10-2026): D01/D02/D03/D04 `STATIC OK` en checkout íntegro; run `39583142837` ([acta](../Auditorias/D04_VALIDACION_CI_Y_CIERRE_2026-10-21.md)). No prueba Godot/GIS/runtime ni MSI físico D04. El merge de PR #20 requiere autorización del autor y verificación GitHub.

**Protocolo:** una fase/conversación/rama, PR propia, sin merge automático. D02 documental no implica canon nuevo, mapa métrico, cuencas trazadas ni juego ejecutado. D02 ya está fusionada. Consultar acta D04 y TRASPASO_D05.md para D05, siempre condicionada al merge autorizado de D04.

## Inicio D05 comprobado 21-10-2026
GitHub confirmó PR #20 fusionada y `main` en `d4a07ba25f8560d5005a52aafc763699917f2388` antes de crear rama D05. D05 documenta red modal, datos, validación y traspaso D06; no comienza D06 ni se afirma prueba de D05 antes de CI. La frase histórica «PR #20 pendiente» más arriba en evidencias se refiere a un momento anterior al merge.

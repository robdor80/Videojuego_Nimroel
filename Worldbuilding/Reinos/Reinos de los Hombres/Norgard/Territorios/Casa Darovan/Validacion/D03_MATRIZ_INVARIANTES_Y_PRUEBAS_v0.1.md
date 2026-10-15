# DAROVAN D03 — Matriz de invariantes, pruebas y límites v0.1

**15-10-2026 · PLANIFICACIÓN NO CANÓNICA / NO RUNTIME.** Los controles estáticos del perfil pueden ejecutarse en JavaScript sobre datos de GitHub; el script reproducible Python necesita un checkout íntegro. No sustituye pruebas Godot, GIS, climatología ni decisión del autor.

## Matriz de invariantes
| ID | Afirmación que debe conservarse | Evidencia / control |
|---|---|---|
| D03-01 | Cadena de autoridad Core → Defaults → Darovan → Localidad → World State | JSON authorityChain |
| D03-02 | Propuestas no se convierten en canon | approvals.newCanonApproved = false |
| D03-03 | Proveniencia AUTHORED, DERIVED, GENERATED, DYNAMIC, UNKNOWN | JSON sourceHierarchy |
| D03-04 | Perfil marcado NO RUNTIME | status, runtimeIntegration |
| D03-05 | 12 unidades cualitativas D01 con IDs únicos | d01 physicalUnits vs zones |
| D03-06 | Sin fronteras climáticas ni polígonos | zones.classification |
| D03-07 | Sin coordenadas, mediciones, clima numérico o suelos medidos | contains* y campos nulos |
| D03-08 | Sin especies, episodios meteorológicos ni ríos creados | contains* |
| D03-09 | Costa occidental oceánica suave | regionalAnchors.westernCoast y Norgard/clima |
| D03-10 | Norte polar–frío–continental gradual, sin demarcación política | regionalAnchors.northernTransition |
| D03-11 | Taramin norte/centro semiárido NO desierto | regionalAnchors.taraminNorthCentral |
| D03-12 | Taramin gana humedad al sur y bosque subtropical húmedo final | regionalAnchors.taraminSouth |
| D03-13 | Syvaris cálida y parcialmente seca, calas protegidas verdes | regionalAnchors.syvaris |
| D03-14 | Bosque de Pilares: un sistema pese a claros | regionalAnchors.pilaresOneForest |
| D03-15 | Bosque de Taramin: un solo conjunto longitudinal | regionalAnchors.taraminOneForest |
| D03-16 | Bosquetes Syvaris discontinuos | regionalAnchors.syvarisForestsDiscontinuous |
| D03-17 | Agujas sin poblados permanentes interiores | permanentSettlementsInsideAgujasAllowed |
| D03-18 | Las 4 ciudades Darovan son manuales | manualCities |
| D03-19 | Karsath excluida, Syvaris isla Darovan | excludedCity/syvarisOwner |
| D03-20 | Arven administrativo UNKNOWN | arvenOwner + zona contexto |
| D03-21 | Belara junto a Treihord sin atravesarla; boca Golfo Norgard | hydroProtection |
| D03-22 | Lhera deriva de Belara y desemboca Golfo Veldora | hydroProtection |
| D03-23 | Veldora independiente de Belara y Lhera | hydroProtection |
| D03-24 | Thalen es un río de dos brazos terminales con Taramin entre ellos | hydroProtection |
| D03-25 | No se afirma permanencia de ríos con nombre | namedRiverPermanence UNKNOWN |
| D03-26 | Sin afluentes/manantiales/humedales/cuencas instanciados | Arrays vacíos y geometría nula |
| D03-27 | Referencias originales localizables y usadas por cada zona | sourceRefs/sourceRefIds; filesystem |
| D03-28 | D01/D02/Core presentes y compatibles | validate_d03.py carga JSON anteriores |
| D03-29 | Estado dinámico futuro no reescribe identidad de cauces | contrato Core + docs D03 |
| D03-30 | Riesgos candidatos requieren comprobación, sin áreas declaradas | docs D03 03, prospectiveRisks |

## Pruebas y trazabilidad
- **JavaScript remoto ejecutado durante construcción (15-10-2026):** comprobaciones estructurales sobre objeto serializado y **10 mutaciones negativas** (Arven adjudicada; Belara atraviesa ciudad; origen Lhera alterado; brazos Thalen; grados inventados; especies nuevas; bosque Taramin fragmentado; poblado Agujas; referencia falsa; permanencia inventada). Afirmar únicamente lo comprobado; no suponer que se ejecutó Python.
- **Revisión posterior GitHub:** descargar JSON efectivo desde rama, parsearlo, comprobar IDs, garantías, referencias y relación D02. Registrar resultados en acta.
- **Reproducción en checkout completo:** ejecutar **python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d01.py"**, luego D02 y D03. D03 incluye 10 fixtures negativos. Hasta su ejecución real, estado: **PENDIENTE — MSI (checkout completo)**.
- **PENDIENTE — GODOT:** sistemas de clima, agua, persistencia, carga y rendimiento con motor; sin simulaciones ni artefactos de ejecución.
- **PENDIENTE — MSI/GIS:** altimetría, mapa, medición de pendientes y exposición, cartografía climática; no bloqueantes para documento cualitativo.
- **Bloqueo para cuantificación/runtime:** DEM, meteorología por temporada, suelos/acuíferos y contratos integrados en fase D11. **No son bloqueo de entrega D03**.

## Pruebas negativas mínimas del validador Python
arven_claim; belara_cross; lhera_source; veldora_join; thalen_arm; numeric_climate; new_species; missing_reference; agujas_village; perennial_assertion.

**Alcance esperado del diff:** solo archivos debajo de Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/. D03 nunca edita originales de Norgard, ciudades, Core ni otras Casas.

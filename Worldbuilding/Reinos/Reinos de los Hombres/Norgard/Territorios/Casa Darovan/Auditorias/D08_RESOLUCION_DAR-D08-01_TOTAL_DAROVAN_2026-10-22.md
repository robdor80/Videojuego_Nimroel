# D08 — Resolución autoral DAR-D08-01: población total de Casa Darovan (22/10/2026)

**Estado:** DECISIÓN DEL AUTOR APROBADA, **solo rango**. Incorporada a rama D08, PR #34 abierta en Draft **sin fusionar**.

## Declaración expresa del autor
«Apruebo la opción B para el intervalo de población total de Casa Darovan en DAR-D08-01. Regístrala como rango autoral en la rama D08, mantén desconocidos los censos exactos y los asentamientos no definidos, valida las pruebas y no fusiones la PR #34. Continuemos con la siguiente decisión de canon.»

**Opción B ofrecida:** **300.000–450.000 habitantes**, «Gran territorio agrícola y comercial».

## Alcance canónico exacto
- **Casa Darovan, territorio completo:** entre **300.000 y 450.000 habitantes**, ambos extremos inclusivos, como intervalo demográfico de referencia aprobado (`AUTHORED_RANGE`). Incluye ciudades, pueblos, aldeas, enclaves y población extramuros/rural o insular residente en el territorio de la Casa, sin establecer cuántos hay ni ubicarlos.
- **Censo exacto del territorio:** `UNKNOWN` (`populationApprox=null`). El punto medio, un valor aleatorio, o la suma de máximos/mínimos no son un censo.
- No confundir el total territorial de la Casa con el **reino de Norgard**, con Karsath u otras casas, ni con el total de **isla Syvaris**. La ciudad de Syvaris (7.000–10.000 habitantes), el resto de su isla (UNKNOWN) y la población insular total (UNKNOWN) son subconjuntos internos de la Casa Darovan, **no cifras para sumar por encima del total territorial**.
- **Treihord:** ~32.000; **Veldora:** 29.000–35.000; **Taramin:** 14.000–20.000; **ciudad de Syvaris:** 7.000–10.000. Los intervalos de ciudades son referencias no censos puntuales. No se deducen de ellos automáticamente densidades, coeficientes urbano/rurales, habitantes por localidad o población rural exacta.
- D06: **nueve modelos técnicos y seis escenarios sintéticos TEST_ONLY**, no nueve pueblos reales ni un censo rural. Se conservan sin instanciaciones los asentamientos no aprobados.
- No se fijan cantidades ni cuotas de viviendas, familias, profesiones, instituciones, servicios, suministros, guardias, barcos, caminos, NPC, reservas latentes u otras entidades de CoreRPG.
- La opción B significa una **escala territorial de población aprobada**, no un porcentaje rural/urbano ni validación de capacidad agrícola. Los recursos y cadenas D04 y la movilidad D05 quedan intactos.

## Trazabilidad operativa
- `Datos operativos/darovan_d08_population_services_v0.1.json` → `territoryPopulation`: `scope=casa_darovan_entire_territory_including_islands`, `populationApprox=null`, `populationStatus=AUTHORED_RANGE`, `populationRange.minInclusive=300000`, `maxInclusive=450000`, `option=B`, `decisionId=DAR-D08-01`, `provenance=AUTHORED`, `sourceRefId=decisionD0801DarovanTotal`.
- Se deja `ruralPopulationApprox=null`, `canonicalSettlementCensus=null`, `physicalSettlementCount=null`, `cityTotalsAreExact=false`, `runtimeInstantiated=false`.
- `sourceRefs.decisionD0801DarovanTotal` enlaza este documento. `planningUnknowns` mantiene censo exacto, cuantías rurales/insulares, tamaños de hogares y asentamientos no materializados.
- El validador estático impide modificar el rango, crear cifras puntuales o trasladarlo a un territorio ajeno.

**PR #34 continúa Draft y SIN FUSIONAR. D09–D11 no iniciadas; sin integración CoreRPG/Godot.**

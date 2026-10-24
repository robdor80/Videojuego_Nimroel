# D08 — Resolución autoral DAR-D08-01: Syvaris (22/10/2026)

**Estado:** DECISIÓN AUTORAL APROBADA, intervalo canónico de la **ciudad** de Syvaris. Se registra exclusivamente en rama D08, PR #34 Draft, **SIN FUSIONAR**.

## Declaración del autor
«Apruebo la opción B para la población de Syvaris en DAR-D08-01. Registra el intervalo aprobado en la rama D08, valida las pruebas, conserva la PR #34 sin fusionar y continuemos con la siguiente decisión de canon.»

**Opción B ofrecida al autor:** **7.000–10.000 habitantes**, «Ciudad portuaria insular consolidada».

## Hecho aprobado y exclusiones
- **Ciudad de Syvaris**: población de referencia **7.000 a 10.000 habitantes inclusive**; opción B y decisión `DAR-D08-01`. No es censo exacto; `populationApprox: null` y `populationStatus: AUTHORED_RANGE`.
- **La isla de Syvaris no equivale automáticamente a la ciudad**. La población del resto de la isla sigue `UNKNOWN`, y por tanto también el total insular. No extrapolar tamaño del territorio, ocupaciones ni número de otros asentamientos.
- Syvaris conserva su menor escala demográfica respecto a Taramin (14.000–20.000; opción B anterior), sin alterar Veldora (29.000–35.000) ni Treihord (aproximadamente 32.000).
- Se conserva la decisión D07-A conceptual: actividad principal en bahía protegida, pesca y comercio, con presencia naval **de Norgard**, sin flota propia de Darovan. No se aprueban muelles, astilleros nuevos, barrios, instituciones, dotaciones o emplazamientos específicos.
- La población total de Casa Darovan sigue `UNKNOWN`: el agregado de las cuatro ciudades no representa el territorio. Hogares, NPC individuales, servicios, trabajadores y detalles geográficos no se cuantifican.
- Este índice de planificación NO crea `PopulationRecord` o identidades CoreRPG ni ejecuta Godot.

## Fuente de datos
En `Datos operativos/darovan_d08_population_services_v0.1.json` aparece la ficha de Syvaris: `populationRange.minInclusive=7000`, `maxInclusive=10000`, `status=APPROVED_AUTHOR_RANGE`, `decisionId=DAR-D08-01`, `option=B`, `sourceRefId=decisionD0801Syvaris`, `provenance=AUTHORED`, `populationApprox=null`. La fuente se enlaza desde `sourceRefs.decisionD0801Syvaris` y `sourceRefIds`.

Validador y esquema D08 blindan el intervalo y distinguen ciudad/isla; la PR #34 queda Draft sin merge.

# D08 — Resolución autoral DAR-D08-02: tamaño medio de los hogares urbanos (22/10/2026)

**Estado:** decisión del autor APROBADA; ámbito estrictamente urbano y **solo rango estadístico de referencia**. Incorporado a la rama D08 y a PR #34 en Draft, **SIN FUSIONAR**.

## Declaración del autor
«Apruebo la opción B para DAR-D08-02, rango de tamaño medio de los hogares urbanos de Casa Darovan. Registra la decisión en la rama D08, sin fijar cantidades exactas de hogares, viviendas o habitantes ni fusionar PR #34. Valida las pruebas y continúa con la siguiente decisión de canon.»

**Opción B ofrecida:** **3–5 personas por hogar urbano, de media**. Se trata del **intervalo aprobado en que puede situarse el promedio de habitantes por hogar urbano**, no de la obligación de alojar exactamente 3, 4 o 5 personas en cada hogar.

## Alcance canónico y límites
- `householdModel.urbanMeanPersonsPerHouseholdRange` = **[3,5]**, extremos inclusivos, personas por hogar como media urbana de referencia (opción B, `AUTHORED_RANGE`). No fija media puntual (por ejemplo 4) ni tamaño obligatorio de cada unidad doméstica.
- Se permiten hogares de una sola persona, parejas, familiares convivientes o no convivientes, personas sin parentesco, aprendices y alojados, respetando `RES/KIN/CARE/CHORE/EMP/APR` y Norgard Defaults. La composición **no** deriva automáticamente del tamaño.
- El **promedio rural** sigue `UNKNOWN`; el promedio global de toda Casa Darovan sigue `UNKNOWN`; tampoco se fijan porcentajes urbanos/rurales, distribución de tamaños, proporciones demográficas ni pirámide de edad.
- **NO** calcular ni dar por canónico el número de hogares, viviendas, edificios, personas físicas, plazas domésticas, establecimientos, población individual ni habitantes de localidad alguna. El hecho de conocer rangos de población urbana/total no permite transformar automáticamente este intervalo en censos de hogares.
- Los asentamientos no definidos por D06 siguen siendo **modelos técnicos**, sin localidades ni viviendas creadas.
- **SIN RUNTIME:** no crea relaciones de CoreRPG, población materializada, NPC ni nuevas operaciones Godot.

## Trazabilidad
- `Datos operativos/darovan_d08_population_services_v0.1.json` → `householdModel.urbanMeanPersonsPerHouseholdRange`: `minInclusive=3`, `maxInclusive=5`, `status=APPROVED_AUTHOR_RANGE`, `option=B`, `decisionId=DAR-D08-02`, `sourceRefId=decisionD0802UrbanHousehold`, `provenance=AUTHORED`, `notAnIndividualHouseholdLimit=true`.
- `householdModel.ruralMeanPersonsPerHouseholdRange=null`; `householdModel.meanPersonsPerHousehold=null`; `householdModel.householdCount=null`. La media exacta urbana y la distribución urbana de tamaños también son desconocidas.
- `sourceRefs.decisionD0802UrbanHousehold` enlaza la presente acta. El esquema y las pruebas estáticas impiden extrapolaciones o falsos censos.

Continúa pendiente DAR-D08-02 para **hogares rurales** y estructura demográfica por edades. PR #34 Draft sin fusionar; D09–D11 sin iniciar.

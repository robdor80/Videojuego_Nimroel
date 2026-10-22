# D08 — Resolución conjunta del autor: cierre demográfico y de hogares (22/10/2026)

**APROBADO POR EL AUTOR, LOTE ÚNICO.** Solo rama D08; PR #34 abierta en Draft **SIN FUSIONAR**. No se aprueba integración CoreRPG/Godot, NPC ni localidades nuevas.

## Texto autoral y alcance
El autor confirma: «Apruebo conjuntamente las decisiones pendientes de D08: **1B** (Distribución equilibrada); **2C** (Sin diferencias cuantitativas por ahora); **3C** (**35–45 % urbana**); **4A** (Ninguna nueva en D08). Mantén también aprobada la **B de hogares rurales 4–6**. Registra todo en un solo lote en la rama D08, valida en Windows y Linux, mantén la PR #34 Draft sin fusionar y prepara el cierre documental».

Decisiones aprobadas expresamente:

1. **DAR-D08-02 / hogares rurales B:** intervalo del **promedio rural 4–6 personas por hogar**. No es mínimo/máximo obligatorio por hogar individual, no afirma que cada familia tenga ese tamaño y **no fija media exacta**, viviendas ni hogares. Se conserva el rango urbano previamente aprobado **3–5 personas de media**.
2. **DAR-D08-02 / 1B / estructura territorial de edades:** **30 % de menores de 18 años (0–17)**; **60 % de 18–59 años**; **10 % de 60 años en adelante**. Referencia porcentual global de Casa Darovan; los tres porcentajes suman exactamente 100. Ningún conteo puntual, proporción por localidad, mortalidad o estructura laboral se deduce.
3. **DAR-D08-02 / 2C / edades urbanas frente a rurales:** **no se aprueban porcentajes desglosados distintos**. La ausencia de división cuantitativa aprobada **no supone que campo y ciudad tengan distribuciones idénticas**. Sus porcentajes específicos y la variación real permanecen UNKNOWN.
4. **DAR-D08-02 / 3C / población urbana-rural:** **35–45 % urbana y 55–65 % rural** del total de habitantes de Casa Darovan, como rangos **complementarios vinculados** (una proporción urbana U implica proporción rural 100−U). No se fija proporción exacta, censo exacto urbano o rural, ni clasificación automática de cada asentamiento.
5. **DAR-D08-03 / 4A:** **ninguna categoría social, institución singular ni especialidad profesional nueva en D08**. Aplicar el canon existente de Norgard y Darovan. Esta decisión **no bloquea** que una fase futura plantee propuestas para aprobación expresa.

## Comprobación de cobertura territorial: NO inventar localidades
Las cuatro ciudades canónicas son Treihord (~32.000), Veldora (29.000–35.000), Taramin (14.000–20.000) y **la ciudad** de Syvaris (7.000–10.000). Esas cuatro referencias suman ~82.000–97.000 habitantes; no son el censo urbano completo.

El 35 % del límite territorial inferior aprobado, 300.000, equivale a 105.000 habitantes; por ello **las cuatro ciudades conocidas, incluso por su referencia máxima, no cubren por sí solas el mínimo urbano compatible con el nuevo intervalo**. Esto es una **brecha de cobertura documental**, NO aprobación de ciudades, villas, asentamientos, viviendas, rutas o habitantes restantes. Su identidad, cantidad, situación, categoría urbano/rural, población y distribución quedan `UNKNOWN`, pendientes de un futuro inventario autorizado. No deducir un número de nuevas localidades ni volcar habitantes a D06 `TEST_ONLY`.

El término **urbano** del 35–45 % es clasificación agregada de planificación del territorio, no sinónimo exclusivo de las cuatro ciudades canónicas. No inventar criterios locales detallados de clasificación.

## Elementos no resueltos en D08
Población exacta de Casa Darovan y ciudades; total y resto no urbano de la isla de Syvaris; censos de las demás localidades; número de hogares, viviendas, NPC y nuevos asentamientos; promedio exacto urbano/rural/territorial; distribución de tamaños domésticos; cuantía exacta de residentes urbanos y rurales; estructura por edad en cada ámbito; tasas y hechos demográficos no aprobados; capacidades de servicios, personal e infraestructuras y todos los elementos runtime.

El `householdModel` sigue siendo conceptual (`RES/KIN/CARE/CHORE/EMP/APR`), sin suponer familia = hogar, profesión = puesto, o porcentaje = entidad materializada. `ageShares` se entiende como referencia agregada, no reparto exacto computado de NPC.

## Trazabilidad
`sourceRefs.decisionD0802FinalBatch` enlaza esta acta en `Datos operativos/darovan_d08_population_services_v0.1.json`; se añaden campos `householdModel.ruralMeanPersonsPerHouseholdRange`, `householdModel.ageShares`, `householdModel.urbanRuralAgeBreakdown`, `householdModel.ruralUrbanShares`, y `socialInstitutionPolicyD08`, con validación de esquema, invariantes y negativos. `runtimeIntegration` conserva todo desactivado. Ninguna fusión ni inicio D09/D10/D11 autorizado.

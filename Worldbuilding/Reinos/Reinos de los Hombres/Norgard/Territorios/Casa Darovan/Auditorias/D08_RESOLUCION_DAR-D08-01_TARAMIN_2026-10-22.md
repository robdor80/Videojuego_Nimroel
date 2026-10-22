# D08 — Resolución autoral DAR-D08-01: Taramin (22/10/2026)

**Estado:** DECISIÓN AUTORAL APROBADA, intervalo poblacional canónico. Registro solo en rama D08 / PR #34 Draft; **SIN FUSIONAR**.

## Declaración del autor
«Apruebo la opción B para la población de Taramin en DAR-D08-01. Registra el rango aprobado en la rama D08, valida las pruebas, no fusiones la PR y continuemos con la siguiente decisión de canon.»

**Opción B ofrecida:** **14.000–20.000 habitantes**, ciudad pesquera mediana. Es una propuesta convertida en canon por aprobación expresa, no una estimación extraída del mapa ni un censo.

## Alcance exacto del canon aprobado
- **Taramin:** rango de referencia **14.000–20.000 habitantes, inclusivo** (opción B; fuente autor). Su censo exacto sigue `UNKNOWN` y en el JSON operativo `populationApprox: null`.
- El intervalo es **menor que Veldora** (29.000–35.000 habitantes; DAR-D08-01/Veldora B) y la cifra aproximada de Treihord (~32.000), preservando el hecho D07 de escala media.
- Mantener la **zona pesquera principal D07-A como concepto**. No se fijan número ni situación de muelles, cauces navegables de los brazos del Thalen, barrios, instituciones, casas, personas, existencias, profesionales, cuotas laborales ni tiempos.
- **Syvaris** y el **total poblacional de Darovan**: `UNKNOWN` pendientes de elecciones separadas. La cifra precisa de Veldora, Taramin y la composición de hogares no se deduce de los rangos.
- Esta aprobación no crea población simulada, NPC, almacenes o `PopulationRecord` en CoreRPG, y no convierte la planificación D08 en runtime.

## Trazabilidad
- Ficha operacional: `Datos operativos/darovan_d08_population_services_v0.1.json` → `cities[id=taramin].populationRange`.
- `minInclusive=14000`, `maxInclusive=20000`, `unit=habitantes`, `status=APPROVED_AUTHOR_RANGE`, `decisionId=DAR-D08-01`, `option=B`, `sourceRefId=decisionD0801Taramin`.
- `populationStatus=AUTHORED_RANGE`, `populationApprox=null`, `sourceRefIds` añade exclusivamente la referencia al acta.

El esquema y el validador D08 impiden sustituir el rango por una cifra puntual y rechazan modificaciones de extremos, autoría o localidad. La PR #34 sigue Draft; cualquier fusión requiere permiso expreso.

# D08 — Matriz de invariantes y pruebas v0.1

| Grupo | Condición estática y negativa |
|---|---|
| Integridad de fuente | Todos los `sourceRefs` existen; los índices D04/D06/D07 siguen siendo autoridad |
| Jerarquía | Nimroel Core → Norgard Defaults → Darovan → Localidad → World State |
| Canon urbano | Solo cuatro ciudades manuales, fuera Karsath; Treihord aproximadamente 32.000 |
| D07 conceptos | Veldora B, Taramin A, Syvaris A solo concepto, sin nuevo plano/edificio |
| Demografía | Poblaciones restantes, población territorial y número de hogares `null/UNKNOWN` |
| Población CoreRPG | Nada de simulación runtime por JSON, sin registro numérico `RelationKind` aprobado |
| Edad y convivencia | 18+ civil, aprendiz desde 12 y empleo limitado desde 15; no co-residencia matrimonial automática |
| Recursos e inventarios | Sin stock ex nihilo, ni proveedor gratuito, ni demanda que cree edificio |
| Trabajo | Profesión ≠ empleo; ausencia/vacante ≠ sustituto instantáneo |
| D05/D06 | Referencias existentes válidas; no se generan ciudades ni caminos a partir de suministros |
| Servicios | Diez necesidades, no diez edificios; capacidades y proveedores cuantificados UNKNOWN |
| TEST_ONLY | Casos de laboratorio aislados, IDs prefijados y sin NPC persistentes creados |

Ejecutar `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d08.py"` sobre checkout íntegro. CI GitHub Actions en Ubuntu y Windows ejecutará D01–D08 sin necesidad de MSI. Estas pruebas **son estáticas**, no certifican integración CoreRPG/Godot, ni desplazamientos, guardados o economía simulada.

## Extensión DAR-D08-01 — 22/10/2026
El validador debe aceptar únicamente el rango autoral **[29000,35000]** para **Veldora**, con `AUTHORED_RANGE` y referencia exacta a la decisión. Rechazar alteración de extremos, pérdida de autoría, desaparición de rango, creación de cifra puntual y contaminación de Taramin/Syvaris o Treihord. Las cifras restantes y la población total continúan nulas. Nueve mutaciones negativas adicionales: de 35 a **44**. No altera las regresiones D01–D07.

## Extensión Taramin DAR-D08-01 — 22/10/2026
Taramin: intervalo autoral inclusivo **[14000,20000]** (opción B) ligado a acta propia y estado `AUTHORED_RANGE`, sin cifra exacta, hogares, infraestructura ni nueva instancia runtime. Preservar el intervalo de Veldora [29000,35000] y Treihord ≈32.000, y mantener Syvaris UNKNOWN. Rechazar alteraciones de extremos, fuente, provincia, clase, autoría, censo inventado o trasplante del rango a Syvaris. Se añaden **9 negativos** (44 → **53** negativos D08), además del control de orden de escala poblacional. Ningún cambio de los validadores D01–D07.

## Extensión Syvaris DAR-D08-01 — 22/10/2026
Comprobar `populationRange=[7000,10000]` únicamente para **ciudad Syvaris**, estado `AUTHORED_RANGE`, procedencia del acta y `populationApprox=null`. No atribuir a la isla completa ni inventar su resto poblacional; `planningUnknowns` conserva población insular restante y total insular. Respetar jerarquía de tamaño Syvaris (10.000 máximo) < Taramin (14.000 mínimo), Veldora y Treihord invariantes. Añadidas **9 mutaciones negativas** (53 → **62**): límites, rango anulado, contaminación Treihord, falsa autoría, censo exacto, estado, enlace de fuente y fuente inexistente. Regresiones D01–D07 conservadas.

## Extensión DAR-D08-01 — Total territorial (22/10/2026)
`territoryPopulation`: rango autoral inclusivo `[300000,450000]` para **toda Casa Darovan**, opción B, procedencia propia. No se confunde con Norgard, con isla Syvaris aislada ni con la suma de habitantes de cuatro ciudades. No se canoniza un punto, el remanente rural, la cantidad de pueblos/aldeas o un censo de asentamientos. Se añaden **14 negativos** (62 → **76**): extremos, procedencia, desaparición de rango, censo exacto, jurisdicción incorrecta, cantidad rural inventada, censo/contador de asentamientos, falsa exactitud de ciudades, trazabilidad perdida, fuente eliminada, integración runtime y contaminación de la ficha Syvaris. Se impide que el límite inferior territorial quede por debajo de los máximos de las referencias urbanas. D01–D07 conservadas y sin nuevo CoreRPG/Godot.

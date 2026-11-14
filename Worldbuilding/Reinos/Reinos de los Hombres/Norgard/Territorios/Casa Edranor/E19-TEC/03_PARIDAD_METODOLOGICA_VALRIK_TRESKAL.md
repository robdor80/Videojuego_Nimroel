# E19-TEC.03 — Paridad metodológica vinculante Valrik/Treskal

**Fecha:** 14/11/2026. **Estado:** criterio técnico y de calidad, no certificación B3/B4.

## Qué se ha contrastado realmente

Se han revisado los documentos originales de Casa Valrik / Geografia_local:
- `README.md`
- `microrelieve_y_unidades_de_drenaje_v0.1.md`
- `cuencas_manantiales_red_hidrografica_menor_v0.1.md`
- `reglas_espaciales_generacion_motor_v0.1.md`

El método Valrik **no ubica con coordenadas todas las lomas, arroyos o nacimientos antes de aprobar su geografía**. Primero define anclas mayores, ocho contextos regionales, familias geomorfológicas, tipos de microcuenca y criterios físicos de plausibilidad; después encadena generación y materialización. Las reglas espaciales publican explícitamente `CANON → MACRORELIEVE → MICRORRELIEVE → DRENAJE → CUENCAS → HIDROGRAFIA MENOR → MICROCLIMA → SUELO/VEGETACION → USO HUMANO → WORLDSTATE`. La semilla y la identidad estable solo proceden al materializar. Los tipos de terreno no son coordenadas métricas.

En Edranor la misma jerarquía fue desarrollada y auditada en E19-R0–R6, con diferencias territoriales legítimas. El objetivo **no** es copiar los ríos Sareno/Theleno, costas o cotas de Valrik. Es mantener la profundidad causal y las puertas de calidad.

## Matriz de transferencia verificada

| Estándar Valrik | Homólogo Edranor | Regla obligatoria TEC |
| --- | --- | --- |
| Anclas mayores, contexto previo al terreno | R0 correcciones de autor, R1 perfiles Valkram/Azurios/Lurien/Antela | Las anclas no se eligen por un generador |
| Contextos de microrelieve y transiciones | R1 ocho MF, seis unidades de diseño; MF-08 sin evaluación | Cada sector debe adscribirse a MF aprobado; MF-08/U7 no se rellena |
| Divisorias, unidades y familias de cuenca | R2 HC, HS/SP/WH condicionales | No crear cauce sin causa, receptor y continuidad |
| Manantiales y regímenes de agua | R2 surgencias, drenaje y balances estacionales | Permanente/estacional/efímero no es una tirada aleatoria |
| Microclima derivado de pendiente, humedad y exposición | R3 SO/MU/CV/RN/ES | Condiciones y recursos derivados; evidencia legal independiente |
| Caminos condicionados por suelo, pendiente y agua | R4 Gd/Gq/Gp y 12 CT | Gd/Gq son preguntas; solo Gp acreditado se convierte en camino |
| Asentamientos condicionados por habitabilidad y capacidad | R5 estudios OS, cobertura Sp, modelos aldeas/pueblos/villas | OS no es poblado; Sp vacío no inventa servicios |
| Generación persistente con autoridad y trazabilidad | E19-TEC → E28 | ID estable, seed/version, geometría estática y estado mutable separados |
| Narrativa subordinada al estado físico | E19-R1 y contratos posteriores | IA no inventa hechos geográficos cuando necesita una escena |

## Obligación de calidad

1. **Paridad causal:** ningún suelo, cauce, viñedo, bosque, carretera o aldea se justifica únicamente por estética, misión o azar.
2. **Paridad geográfica:** cada relieve local está vinculado al sistema regional, gradiente, receptor, transiciones y territorio adyacente. Sin falsos puertos, ríos, pasos ni costa al norte.
3. **Paridad jurídico-ecológica:** Rodas ALDEA de Corona; Hallheim fuera; Bosque Real regio; aprovechamiento Bosque Alto condicionado. Divisorias Valkram/Azurios conservan las laderas de cada Casa.
4. **Paridad procedural:** generador determinista, reproducible e idempotente; una entidad generada pasa a identidad estable al materializarse, y después no se re-tira por visitar otra vez.
5. **Paridad de comprobación:** casos adversariales de mal drenaje, ríos sin receptor, autopistas entre núcleos sin terreno/permiso, ocupaciones sin agua/acceso, MF-08, bosques y Corona.
6. **Paridad de autoridad:** `AUTHORED`, `DERIVED`, `GENERATED` y `UNKNOWN` no son intercambiables. Un elemento generado puede ser válido en una partida sin convertirse automáticamente en canon regional.

## Separar tres productos sin rebajar la calidad

**A. Geografía causal B2:** E19-R0–R6, ya documentada y auditada; **no necesita mapa métrico** ni reabrirse por falta de coordenadas. Su aprobación no afirma la existencia de sectores jugables.

**B. Puente técnico TEC-A:** validar y exportar únicamente geometría espacial autorizada; rechazar input no probado, conservar referencias y no fingir datos B3. La CI valida código y contratos, no cartografía real. Permite crear futuros sectores sin modificar el canon ni copiar Valrik.

**C. Sector B3 y runtime B4:** un sector alcanza B3 únicamente cuando existen datos espaciales legítimos y coherencia física, hidrológica, legal y material. B4 requiere **pruebas de carga en Godot y persistencia real CoreRPG**. No exigir B3/B4 para decir que el método de worldbuilding tiene la profundidad de Valrik; tampoco declarar B3/B4 por unos tests sintéticos.

## Qué puede hacer el responsable técnico sin pedir trabajo al autor

El asistente puede completar documentación, código, matrices, validador, procedimientos de semilla/identidad, ejemplos sintéticos, pruebas, auditoría y traspaso. Puede diseñar **opciones** de colocación por causalidad cuando existan referencias suficientes, diferenciándolas de hechos aprobados. No reclamará al autor que dibuje perímetros o mida escalas para justificar la geografía B2. Sólo una decisión nueva de canon que no pueda derivarse de fuentes existentes requerirá decisión autoral; mientras tanto quedará como `UNKNOWN`, no como bloqueo para trabajos independientes.

## Revisión comparativa de los entregables actuales

- E19-R1.05 `05_PERFILES_Y_TRANSICIONES_CAUSALES.md`: perfiles cualitativos y secuencia para generación, mismos principios que Valrik.
- E19-R2.06 `06_CONTRATO_CAUSAL_GENERACION_Y_PERSISTENCIA.md`: receptor, gradiente y balance previos a instancias.
- E19-R3.07 `07_CONTRATO_GENERACION_2D.md`: suelo, clima y vegetación condicionados.
- E19-R4.08 `08_CONTRATO_DE_CARTOGRAFIA_2D.md`: Gd/Gq no acreditan Gp.
- E19-R5.09 `09_CONTRATO_B3_B4.md`: OS no constituye automáticamente población o construcción.
- E19-R6.04 `04_PUERTAS_B3_B4_Y_PLAN_DE_ENTREGA.md`: madurez y pruebas deben certificarse por sector.

**Dictamen:** paridad de procedimiento con Valrik exigida y documentada, infraestructura TEC-A comprobable. **No confundir con paridad material o cierre de toda E19-TEC:** faltan primer sector autorizado B3 y demostración runtime B4. El método no se rebaja para ocultar esas deudas.

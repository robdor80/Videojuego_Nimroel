# Darovan D.P13 — inventario comparado, autoridad y método

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Referencia de profundidad real: Valrik/Treskal

Se han leído los diez capítulos del bloque `Casa Valrik/Clima_local/00…09`, sus tres trabajos `Geografia_local/microrelieve_y_unidades_de_drenaje_v0.1.md`, `cuencas_manantiales_red_hidrografica_menor_v0.1.md`, `reglas_espaciales_generacion_motor_v0.1.md` y el perfil JSON `territorio_treskal_geografia_hidrologia_profile_v0.1.json`. Allí el clima local es **borrador de diseño aprobado dentro del borrador**, no canon definitivo ni código ejecutado. Contempla ocho contextos territoriales, alta variabilidad estacional, cinco familias de drenaje, persistencia conceptual y reglas contra cauces sin cuenca.

## Diagnóstico de Darovan previo a D.P13

- D01: doce unidades cualitativas, cuatro ciudades ancladas, sin relieve fino ni altimetría.
- D02: cinco ríos canónicos y cuatro sistemas, grafo abstracto de 15 nodos/11 aristas; sin microcuencas, afluentes instanciados ni geometrías.
- D03: gradientes climáticos y masas vegetales protegidas, pero temperatura, viento, suelo, caudales y fechas no cuantificados; la validación impide atribuciones inventadas.
- D04–D12: actividades, asentamientos, ciudades, población, contratos y guardrails; no aportan permiso para inventar cruces, granjas, minas, puertos o simulación en vivo.

## Matriz de equivalencia metodológica

| Eje Valrik/Treskal | Producto D.P13 Darovan | Nivel de cierre admisible |
|---|---|---|
| Ocho subzonas climáticas | Doce unidades D01, cada una con perfil multivariable | Cobertura conceptual comparable, sin fronteras |
| Cotas Montes Invernos en borrador | Cotas de Valkram y Elyra UNKNOWN; relieve relativo y filtros espaciales | Reserva justificada: no copiar cotas de otro sistema |
| Microrelieve y cuencas | Catálogo contextual + divisorias y receptores condicionados | Diseño completo, geometría pendiente |
| Lluvia, temperatura, nieve y deshielo | Cuatro estaciones con gradientes dependientes del episodio | Tendencias, no valores meteorológicos cerrados |
| Vientos, humedad y nieblas | Reglas de exposición / flujo efectivo / condensación | Sin dirección dominante inventada |
| Suelos, drenaje, vegetación | Matriz de doce perfiles y reglas acopladas | Fertilidad y litología locales UNKNOWN |
| Persistencia y generación | Contrato de identidad e inferencia no-runtime + validador | Preparación, no ejecución CoreRPG/Godot |
| Evidencia | Validación estructural, causal, negativa y regresión D01–D12 | Requiere CI real y auditoría cualitativa final |

## Escalera de autoridad

`AUTHORED` procede solo de documentos superiores/decisiones; `DERIVED_CONDITIONAL` son reglas físicas compatibles; `PROPOSAL_PENDING_AUTHOR` son nuevas identidades espaciales hipotéticas; `GENERATED_TEST_ONLY` son escenarios sintéticos; `UNKNOWN` no se sustituye. La priorización conceptual es Core → Norgard → Darovan → localidad → World State, **no** un resolvedor implementado.

## Exclusiones innegociables

Sin nuevos hidrónimos, cauces cartografiados, caudales, vientos anuales, rutas, puentes, nombres de accidentes, poblaciones, industrias ni recursos; D.P14–D.P17 intactas. No trasladar temperaturas ni régimen de Sareno/Theleno, Bosque Negro o Montes Invernos a Valkram/Taramin/Syvaris.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/montanas.md), [ríos](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/rios_y_lagos.md), [bosques](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/bosques.md), [clima](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Clima/clima_general.md), [regiones](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/regiones_naturales.md); D01/D02/D03 y [auditoría D12](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

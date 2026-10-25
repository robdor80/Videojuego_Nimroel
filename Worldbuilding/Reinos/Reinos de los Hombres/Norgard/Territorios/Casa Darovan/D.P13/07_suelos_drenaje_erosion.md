# Darovan D.P13 — suelos, permeabilidad, barro, erosión y aptitud

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Principio edafológico

Una cubierta forestal no garantiza fertilidad; un río no garantiza campo cultivable; y un suelo pedregoso no implica el mismo drenaje en todos sus sectores. Las categorías `shallow_possible`, `deposition_possible`, `poor_drainage_possible` son hipótesis **condicionadas al terreno real**. Salinidad, pH, profundidad, granulometría y nivel freático carecen de autorización métrica.

## Matriz de las doce unidades — contexto edáfico y drenaje

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | rocoso/somero posible en pendientes, depósitos más profundos al pie; litología local UNKNOWN |
| `d01_elyra_paso_peninsular` | suelos variables por afloramiento y depósitos; mineral regional no define textura del suelo |
| `d01_norte_transicion` | drenaje temporalmente restringido por hielo posible, suelos reales UNKNOWN |
| `d01_aguja_litoral` | hojarasca y raíces alteran respuesta, permeabilidad medible UNKNOWN |
| `d01_belara_treihord` | aluvión y saturación en bajos candidatos; no declarar fertilidad automática |
| `d01_veldora_litoral` | suelos costeros de propiedades UNKNOWN; salinidad localizada solo tras evidencia |
| `d01_linde_caminos` | rodadas compactadas: barro en drenaje lento, charcos condicionados |
| `d01_pilares_sur` | raíces y compactación tras uso pueden modificar infiltración como mecanismo |
| `d01_taramin_norte_centro` | seco y pedregoso AUTHORED; permeabilidad y fertilidad particulares UNKNOWN |
| `d01_taramin_bosque_sur` | suelo bajo dosel no equivale a fertilidad ni acuífero garantizados |
| `d01_syvaris` | superficies secas y pedregosas, profundidad/salinidad no determinada |
| `d01_arven_contexto` | propiedades de suelo, agua dulce y fertilidad UNKNOWN |

## Reglas de proceso

1. La permeabilidad se infiere a partir de material, estructura y compactación cuando estén definidos; sin ellos permanece UNKNOWN.
2. El barro requiere humedad suficiente y superficie susceptible, y puede agravarse por rodadas/tránsito futuro; no es lluvia por sí sola.
3. El agua que no infiltra ni se almacena necesita receptor, evaporación o flujo superficial coherente.
4. Pendiente y cubierta controlan vulnerabilidad a erosión; episodios intensos aumentan riesgo, no certifican deslizamientos ocurridos.
5. Una depresión con aportes y drenaje lento puede sostener encharcamiento, sin crear humedal canónico automáticamente.
6. La exposición al viento y al sol seca superficies, modulada por aire húmedo y suelo protegido.
7. La fertilidad agrícola exige propiedades del suelo, clima, pendiente, agua y continuidad temporal; sin evaluar datos no se crea parcela apta.
8. Cambios antropogénicos futuros (tala, caminos, pisoteo) podrán alterar compactación y cubierta con procedencia y persistencia.

## Casos de contraste

Taramin norte-centro: sequedad y pedregosidad **AUTHORED**, pero no se fija permeabilidad. Pilares: la tala es actividad documentada sin asumir que todas las laderas estén erosionadas. Syvaris: vegetación verde de cala no demuestra nivel freático apto para abastecimiento. Belara: una vega hipotética no autoriza agricultura efectiva ni edificaciones en llanura inundable.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/montanas.md), [ríos](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/rios_y_lagos.md), [bosques](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/bosques.md), [clima](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Clima/clima_general.md), [regiones](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/regiones_naturales.md); D01/D02/D03 y [auditoría D12](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

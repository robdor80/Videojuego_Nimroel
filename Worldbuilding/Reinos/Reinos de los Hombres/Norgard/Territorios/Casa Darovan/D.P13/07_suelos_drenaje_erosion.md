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

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## DAR-DP13-HILLS-01 — Colinas del norte y centro de Taramin (25/10/2026)

**AUTOR APROBÓ OPCIÓN B:** las colinas **del norte y centro de la península de Taramin, fuera de Elyra**, tienen **elevaciones características aproximadas de 300–600 m s. n. m.** Es rango de las **colinas del sector**, NO una altitud uniforme de toda la zona, un máximo de la península o una cifra válida para las Montañas Elyra.

No modifica la altura del núcleo de Taramin (**0–40 m**), ni la referencia alta de Elyra (hasta **~2.600 m**); sigue el canon de colinas ocres y transición semiárida, Thalen de dos brazos terminales y Bosque de Taramin meridional. No define cotas individuales, barrancos específicos, ríos, rutas, localidades, precipitaciones ni terreno ejecutable.

**Trazabilidad:** `D.P13/20_colinas_norte_centro_taramin_autorizadas.md` y `Datos operativos/darovan_dp13_taramin_north_central_hills_authorial_v0.1.json`. Sin modificar D01–D12 ni iniciar D.P14–D.P18.


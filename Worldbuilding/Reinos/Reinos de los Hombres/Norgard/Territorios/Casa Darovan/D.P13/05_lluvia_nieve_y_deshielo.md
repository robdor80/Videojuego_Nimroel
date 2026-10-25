# Darovan D.P13 — precipitación, nieve, hielo y deshielo

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Presupuesto de agua

Precipitación efectiva no es lluvia total: parte queda interceptada, parte evapora, parte infiltra, parte alimenta reservas y parte es escorrentía. Nieve acumulada representa reserva temporal, no un cauce nuevo. No se adjudican milímetros ni calendarios meteorológicos a Darovan.

## Matriz de las doce unidades — precipitación y humedad efectiva

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | ascenso orográfico únicamente con flujo húmedo de barlovento comprobado |
| `d01_elyra_paso_peninsular` | barlovento y sombra pluviométrica dependen del flujo real, no de un viento importado de Valrik |
| `d01_norte_transicion` | fase de precipitación dependiente de temperatura del episodio |
| `d01_aguja_litoral` | intercepción forestal no crea lluvia adicional; exposición litoral variable |
| `d01_belara_treihord` | lluvia regional y aporte aguas arriba son procesos diferentes |
| `d01_veldora_litoral` | entrada de humedad marina posible según flujo, orientación y relieve |
| `d01_linde_caminos` | lluvia del mismo episodio, diferente retención superficial posible |
| `d01_pilares_sur` | intercepción y aporte de ladera, sin cuantificar efecto sobre lluvia |
| `d01_taramin_norte_centro` | balance seco cualitativo, aguaceros intensos posibles sin régimen impuesto |
| `d01_taramin_bosque_sur` | humedad efectiva aumenta hacia el sur; reparto mensual UNKNOWN |
| `d01_syvaris` | sectores resguardados pueden retener humedad; no imponer monzón |
| `d01_arven_contexto` | precipitación por zona UNKNOWN, bosque no garantiza mayor lluvia |

## Matriz de las doce unidades — nieve y heladas

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | nieve y helada más plausibles en altura; sin cota ni espesor fijados |
| `d01_elyra_paso_peninsular` | residuos nivales altos hipotéticos, sin glaciares afirmados |
| `d01_norte_transicion` | helada/nieve estacional cualitativa; no permafrost ni nieve perpetua sin fuente |
| `d01_aguja_litoral` | posibilidad de heladas ligada al sector septentrional, sin permanencia decretada |
| `d01_belara_treihord` | deshielo de cabeceras puede influir con desfase solo si conexión autorizada |
| `d01_veldora_litoral` | nieve litoral no ordinaria inferida sin datos; condicionada a episodio frío |
| `d01_linde_caminos` | persistencia de hielo bajo sombra solo si se ha formado |
| `d01_pilares_sur` | nieve en altura posible, persistencia condicionada a sombra |
| `d01_taramin_norte_centro` | nieve ordinaria sin respaldo; frío excepcional condicionado |
| `d01_taramin_bosque_sur` | nieve general del bosque meridional no autorizada |
| `d01_syvaris` | nieve ordinaria no sustentada, episodio extraordinario requiere causa |
| `d01_arven_contexto` | nieve local UNKNOWN; no copiar norte frío ni Syvaris cálida |

## Matriz de las doce unidades — procesos estacionales

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | deshielo local puede sumar escorrentía a lluvia |
| `d01_elyra_paso_peninsular` | agua superficial depende de ladera y recarga verificables |
| `d01_norte_transicion` | deshielo puede activar escorrentía superficial antes que infiltración |
| `d01_aguja_litoral` | retención forestal condicionada puede prolongar humedad tras lluvia |
| `d01_belara_treihord` | crecida aguas arriba no implica lluvia local |
| `d01_veldora_litoral` | oleaje/lluvia no alteran automáticamente cursos canónicos |
| `d01_linde_caminos` | secado de caminos responde a lluvia y viento previo |
| `d01_pilares_sur` | cubierta cambiante afecta secado, escorrentía y regeneración |
| `d01_taramin_norte_centro` | lluvia episódica puede activar cauces temporales en concavidades |
| `d01_taramin_bosque_sur` | sequía local y regeneración responden a clima y cubierta |
| `d01_syvaris` | respuesta rápida al secado en suelo expuesto, recuperación forestal condicionada |
| `d01_arven_contexto` | sombra reduce pérdida de humedad según contexto |

## Secuencias causales válidas

1. Lluvia moderada persistente: suelos con drenaje lento ganan humedad; barro solo si material, tránsito y saturación lo permiten.
2. Lluvia intensa sobre ladera con escasa infiltración: escorrentía rápida y erosión posible, sin curso mayor inventado.
3. Nevada: acumulación local depende de temperatura, viento, cubierta y exposición; no crea automáticamente hielo de río.
4. Deshielo: fusión cuando balance térmico lo permita, libera agua con retardo y puede coincidir con lluvia.
5. Episodio seco y ventilado: secado gradual de suelos expuestos; bajo dosel puede conservarse humedad más tiempo.
6. Suelos helados: pueden limitar infiltración y favorecer escorrentía superficial durante fusión; sin permafrost general decretado.
7. Misma lluvia local no implica idéntica crecida entre cuencas de tamaños y coberturas diferentes.

## Casos protegidos

Los barrancos estacionales como **tipo** de Taramin no certifican el secado estival del río Thalen. Tampoco se declara congelación anual de Belara, Lhera, Veldora o Fhalion; los únicos ríos con congelación explícita en Norgard son otros ríos septentrionales ajenos a esta lista. Las regiones altas admiten nieve condicional. **Excepción autoral posterior:** la Viuda, en el sector norte de Valkram, conserva neveros localizados que sobreviven al verano (DAR-DP13-SNOW-01). No hay cota nival aprobada, distribución métrica de esos neveros ni decisión positiva sobre glaciares; el resto de la cordillera continúa sin un régimen de nieve permanente establecido.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## Decisión autoral DAR-DP13-SNOW-01 — Neveros permanentes en la Viuda (25/10/2026)

**APROBADA — opción B.** En **la Viuda**, cumbre septentrional de los Montes Valkram (~4.200 m), **existen acumulaciones de nieve (neveros) que sobreviven al verano en sectores altos y protegidos**. Se confirma la persistencia localizada de nieve de un año a otro; **no** se afirma que todo el pico permanezca nevado ni que exista un límite altitudinal de nieve uniforme para el conjunto de Valkram.

**No se han aprobado glaciares** con esta decisión. Su existencia real sigue **UNKNOWN**, no debe darse por demostrada ni descartada definitivamente sin otra decisión autoral. No se fijan tamaños, volúmenes, espesores, cotas de aparición, localización métrica de neveros, fechas de deshielo ni caudales. La aportación hídrica por fusión es una **posibilidad causal derivada**, no un nuevo nacimiento de río ni una cuantificación.

**Fuente autoral:** elección expresa de opción B a la pregunta 3 de D.P13, 25 de octubre de 2026.

**Registro estructurado:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `worldHighestSummit.snowPersistence` y `snowPersistenceDetail`. Referencias anteriores a «nieve permanente UNKNOWN» en registros históricos quedan parcialmente superadas **solo para la Viuda**; el régimen del resto de Valkram/Elyra permanece por definir.


## Efectos estacionales posibles de pasos de Valkram (aprobación de 25/10/2026)

Los pasos naturales principales tienen rango orientativo de 1.400–2.200 m por decisión `DAR-DP13-PASS-01`. Nieve/hielo y dificultades por viento son consecuencias potenciales dependientes de tiempo y situación local; no se fijan cierres, fechas ni frecuencias de uso. **No confundir un collado hipotético con un camino existente o una vía de paso materializada.**

## DAR-DP13-CITY-ALT-03 — Taramin, opción A (25/10/2026)

**APROBADO POR EL AUTOR:** el **núcleo urbano principal de Taramin** tiene una banda altitudinal de referencia aproximada de **0–40 m s. n. m.**. No define una altitud exacta de barrios, muelles, nivel de agua, pendientes o plano georreferenciado. Mantiene un único **Thalen** con **dos brazos terminales** entre los que se sitúa la ciudad; las conexiones físicas, navegabilidad y emplazamiento exacto de estructuras permanecen UNKNOWN. No se crea isla, puente, vía, canal, puerto adicional ni escenario de inundación.

Documento: `D.P13/16_altitud_taramin_autorizada.md`. Registro: `Datos operativos/darovan_dp13_taramin_elevation_authorial_v0.1.json`. La cifra es una decisión autoral y no una topografía métrica ejecutada; no inicia D.P16/D.P18.


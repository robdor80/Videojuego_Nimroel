# Darovan D.P13 — regiones, transiciones y doce unidades

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Lectura física del territorio

El occidente de Norgard no es un paisaje uniforme: combina cordilleras, franja septentrional fría, costa occidental, valle y río Belara, península Taramin, dos islas de identidades distintas y masas forestales de distinta continuidad. El límite de una unidad de estudio no determina automáticamente linde política, forma de cuenca ni frontera de bioma. El mapa ilustrado solo ancla relaciones autoradas.

## Matriz de las doce unidades — ancla autorizada

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | Cordillera norte-sur; nacimiento septentrional del Belara |
| `d01_elyra_paso_peninsular` | Cordillera occidental meridional con continuidad hacia la península |
| `d01_norte_transicion` | Franja polar/fría gradualmente decreciente hacia el sur, supraterritorial |
| `d01_aguja_litoral` | Bosque antiguo de coníferas, borde de Lhera y litoral abrupto |
| `d01_belara_treihord` | Belara pasa junto a Treihord, no la atraviesa; puerto industrial de barcazas someras |
| `d01_veldora_litoral` | Veldora puerto marítimo; Lhera y río Veldora son independientes y desembocan en el golfo |
| `d01_linde_caminos` | Pequeño bosque de coníferas junto al camino principal, poca caza |
| `d01_pilares_sur` | Masa forestal única al pie meridional de Valkram, claros y aprovechamiento maderero |
| `d01_taramin_norte_centro` | Península con colinas ocres, piedra, matorral, pastos duros, barrancos estacionales como tipo |
| `d01_taramin_bosque_sur` | Bosque longitudinal único de coníferas a mixto y subtropical húmedo al sur |
| `d01_syvaris` | Isla cálida, norte/centro relativamente seco y sur más verde; bosquetes discontinuos; ciudad junto a bahía |
| `d01_arven_contexto` | Administración Darovan aprobada 21/10; bosque continuo de coníferas ocupa aprox. 90 % |

## Perfiles de discontinuidad

1. Valkram: una cresta cambia vertiente y exposición, pero no toda cresta está declarada frontera Darovan; la divisoria de aguas debe seguir el relieve materializado.
2. Elyra y Taramin: diferencia entre cadena montañosa y transición semiárida peninsular; la continuidad topográfica no establece rutas.
3. Costa de Veldora: transición mar-tierra gradual con bocas separadas de Lhera y Veldora.
4. Linde y Pilares: transición de cubierta y uso humano sin convertir los claros en nuevos bosques.
5. Taramin: sequedad de norte/centro hacia bosque más húmedo al sur, sin división del bosque longitudinal.
6. Syvaris: diferencia entre sectores expuestos secos y bahías resguardadas más verdes, con sur relativamente más verde.
7. Arven: bosque continuo ~90 %, distinto de la vegetación dispersa de Syvaris; pertenece a Darovan por decisión posterior a D00.
8. Zona norte: borde climático transicional supraterritorial, sin una línea de tundra inventada.

## Regla de consulta espacial

Una localización se describe por `studyUnitId`, atributos de relieve medidos o `UNKNOWN`, cobertura efectivamente cartografiada o `UNKNOWN`, exposición al mar y conexiones hidrográficas acreditadas. No se permite asignación por cercanía administrativa solamente.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## DAR-DP13-CITY-ALT-04 — Syvaris: banda altitudinal aprobada (25/10/2026)

**APROBACIÓN AUTORAL, opción A:** el **núcleo urbano principal de Syvaris** se sitúa aproximadamente entre **0 y 40 metros sobre el nivel del mar**, junto a la bahía principal de la isla. **No** implica que toda Syvaris o sus colinas/calas/acantilados estén por debajo de 40 m; tampoco fija coordenadas, barrios, pendientes, muelles, mareas, inundabilidad, abastecimiento de agua o instalaciones navales.

Continúa siendo una isla de Norgard administrada por Darovan, con **puerto seguro y presencia naval del Reino (no armada privada Darovan)**. Se respetan sus sectores secos y verdes y sus bosques discontinuos, sin inventar infraestructuras, fenómenos, vías, calas adicionales o cartografía métrica.

**Documentos:** `D.P13/17_altitud_syvaris_autorizada.md` y `Datos operativos/darovan_dp13_syvaris_elevation_authorial_v0.1.json`. D.P16/D.P18 pendientes, sin runtime.


## DAR-DP13-ISLAND-ALT-01 — Máxima altitud de la isla de Syvaris (25/10/2026)

**APROBADO POR EL AUTOR — opción A:** el **punto natural más elevado de toda la isla de Syvaris** estará aproximadamente **entre 200 y 400 m s. n. m.** La franja corresponde a su **máximo insular**; no fija una altura uniforme de las colinas ni certifica un pico a 300 m. La ciudad de Syvaris conserva por separado los **0–40 m** de su núcleo urbano junto a la bahía.

La cumbre máxima exacta, su nombre, emplazamiento, cartografía, pendientes, cotas de acantilados y condiciones climáticas medidas siguen UNKNOWN. El norte/centro seco, el sur más verde y los bosques discontinuos no se alteran. No se generan montañas, rutas, ríos, infraestructuras ni runtime.

Documentación: `D.P13/18_altitud_maxima_isla_syvaris_autorizada.md`; registro: `Datos operativos/darovan_dp13_syvaris_island_relief_authorial_v0.1.json`. No supone iniciar D.P16/D.P18.


## DAR-DP13-ISLAND-ALT-02 — Cota máxima insular de Arven (25/10/2026)

**APROBACIÓN EXPRESA DEL AUTOR — opción B:** la **máxima elevación natural de la isla de Arven** se situará aproximadamente **entre 250 y 500 m s. n. m.** Es un intervalo para el **máximo de la isla**, no una altitud para todas sus lomas, acantilados, aldeas o costa. No se elige una altura puntual ni se bautiza una montaña.

Se mantiene el **Bosque del Manto Verde** (aproximadamente **90 %** de Arven, continuo y principalmente de coníferas), las aldeas concentradas principalmente en la costa interior orientada al Golfo de Veldora, la caza y la gestión maderera limitada. Se conserva la jurisdicción de **Casa Darovan**. Sin alturas de aldeas, geometría, manantiales, nuevos caminos o gameplay runtime. Ver `D.P13/19_altitud_maxima_isla_arven_autorizada.md` y `Datos operativos/darovan_dp13_arven_island_relief_authorial_v0.1.json`.


## DAR-DP13-HILLS-01 — Colinas del norte y centro de Taramin (25/10/2026)

**AUTOR APROBÓ OPCIÓN B:** las colinas **del norte y centro de la península de Taramin, fuera de Elyra**, tienen **elevaciones características aproximadas de 300–600 m s. n. m.** Es rango de las **colinas del sector**, NO una altitud uniforme de toda la zona, un máximo de la península o una cifra válida para las Montañas Elyra.

No modifica la altura del núcleo de Taramin (**0–40 m**), ni la referencia alta de Elyra (hasta **~2.600 m**); sigue el canon de colinas ocres y transición semiárida, Thalen de dos brazos terminales y Bosque de Taramin meridional. No define cotas individuales, barrancos específicos, ríos, rutas, localidades, precipitaciones ni terreno ejecutable.

**Trazabilidad:** `D.P13/20_colinas_norte_centro_taramin_autorizadas.md` y `Datos operativos/darovan_dp13_taramin_north_central_hills_authorial_v0.1.json`. Sin modificar D01–D12 ni iniciar D.P14–D.P18.


## DAR-DP13-FOOTHILLS-01 — Piedemonte occidental de Valkram (25/10/2026)

**APROBACIÓN DEL AUTOR, opción B:** las **elevaciones características de las estribaciones occidentales de los Montes Valkram** se sitúan aproximadamente entre **400 y 900 m s. n. m.** No es un rango uniforme para cada ladera, valle, aldea, ni la cota máxima de la cordillera. Mantiene las cumbres (3.600–4.200 m), **la Viuda (~4.200 m)**, los pasos naturales principales (1.400–2.200 m) y la altura urbana general de **Treihord (150–350 m)** como referencias distintas.

No modifica el curso del **Belara**, que pasa junto a Treihord sin atravesarlo. La unidad `d01_valkram_oeste` sigue siendo un ámbito cualitativo y no una frontera política. No se atribuyen pendientes medidas, bosque altitudinal concreto, nuevos ríos, caminos, pasos, núcleos ni terreno generado.

Documentación: `D.P13/21_piedemonte_occidental_valkram_autorizado.md`. Contrato: `Datos operativos/darovan_dp13_valkram_west_foothills_authorial_v0.1.json`. D.P18 queda pendiente.


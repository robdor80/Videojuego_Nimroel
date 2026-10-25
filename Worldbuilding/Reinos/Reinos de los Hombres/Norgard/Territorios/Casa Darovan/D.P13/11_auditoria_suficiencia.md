# D.P13 — Comparativa final de profundidad frente a Valrik/Treskal

**Fecha:** 25-10-2026. **Estado:** dictamen documental de diseño; validación GitHub Actions a registrar separadamente. Valrik posee bloque climático de diez capítulos, tres documentos adicionales de geografía local y perfil JSON; su estatus es borrador de diseño aprobado como tal, no canon final ni ejecución de física.

| Criterio | Valrik/Treskal verificado | Darovan tras D.P13 | Juicio y reserva |
|---|---|---|---|
| Relieve/microrelieve | Catálogos por ocho zonas; Montes Invernos con cotas de borrador | 12 unidades; formas, continuidad y filtros | Comparable conceptualmente; cotas Valkram/Elyra UNKNOWN |
| Subzonas geográficas | 8 contextos | 12 claves D01 con matrices por 14 dimensiones | Equivalente o más granular en cobertura |
| Cuencas/red menor | Cinco familias y perfil de red candidata | Cuatro sistemas mayores, doce perfiles, reglas de nacimiento y receptor | Comparable cualitativamente; sin geometría ni nuevos afluentes |
| Temperatura/estaciones | Cuatro estaciones por contexto | Cuatro estaciones por contrastes Darovan y doce gradientes térmicos | Comparable conceptualmente, sin números |
| Lluvias/nieve/deshielo | Contrastes por zonas y fases | Matrices por 12 unidades, procesos y falsas inferencias rechazadas | Comparable como reglas; no hay calendario local aprobado |
| Vientos/humedad/nieblas | Rosa estacional de borrador Valrik | Flujo efectivo y barlovento por episodio; niebla por saturación | Reserva: direcciones dominantes Darovan UNKNOWN, no copiables |
| Suelos/drenaje | Contrastes aluviales, forestales y montanos | Contrastes Taramin, Linde, Pilares, isla, montaña y corredores | Comparable en causalidad; clases reales de suelo UNKNOWN |
| Ecosistemas/vegetación | Bosque Negro, Gemelos, montaña y costa | Agujas, Linde, Pilares, Taramin, Syvaris, Arven | Comparable en identidad diferenciada; sin inventar especies |
| Microclimas | Valles, costa, dosel, exposición | 12 perfiles cruzados y mecanismos de sombra/exposición | Comparable como hipótesis condicionadas |
| Reglas de generación | Pipeline espacial y restricciones | Pipeline por capas + 10 reglas operativas y topológicas | Equivalencia conceptual, no algoritmo implementado |
| Persistencia/causalidad | Continuidad conceptual de WorldState | Esquema de estado y deltas, versionado, semillas y 8 negativos | Comparable en diseño, no en ejecución |
| Datos y pruebas | JSON de hidrología de borrador | 3 JSON nuevos, validador con negativos y CI prevista | Conclusión condicionada a verificaciones reales |

## Diferencias justificadas

La ausencia de cotas métricas específicas, mapas de cuencas, aforos, vientos por rumbo, bocas exactas del Fhalion y red de cauces materializada **no se cierra inventando**. Son decisiones autorales o dependen de cartografía posterior. Tampoco Valrik materializa en runtime sus reglas de geografía local. La ciudad Treskal sí dispone de plano métrico, pero **comparar esa materialización urbana con D.P13** sería extrapolar una fase posterior D.P16 y violar el alcance.

## Puertas de cierre

[A] Fuentes/autoridad y doce unidades; [B] coherencia de 5 ríos/4 sistemas; [C] cobertura temática; [D] regresiones y negativos CI Windows/Linux; [E] diferencia justificada frente a Valrik; [F] incertidumbres y contrato no-runtime. Si una de A-D falla, D.P13 es **INCOMPLETA**; si todas pasan y E/F son transparentes, dictamen **COMPLETA CON RESERVAS DE CARTOGRAFÍA MATERIAL Y RUNTIME**, nunca «entorno físico ejecutado».

## Decisiones de autor

No bloquea la finalización documental ninguna decisión nueva. Quedan futuros: relieves georreferenciados y cotas, localización exacta de cauces menores y manantiales, bifurcación Belara/Lhera, desembocadura Fhalion, rosa de vientos local y datos de suelo medidos. `UNKNOWN` permanece hasta aportación de fuente o materialización legítima.

## Evidencia posterior — GitHub Actions, 25-10-2026

El commit de documentación y auditoría `3b77cd9f70f36d1ec49344b941d71a34a6f87184` superó ambas baterías de GitHub Actions:

- [D.P13 específica — ejecución #40186172798](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40186172798): **SUCCESS** tanto en `windows-2022` como en `ubuntu-24.04`. Doce zonas; cuatro sistemas; diez reglas causales; 24 pruebas adversariales rechazadas.
- [Regresión D01–D12 — ejecución #40186172806](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40186172806): **SUCCESS** tanto en `windows-2022` como en `ubuntu-24.04`, incluida la compilación C++ de catálogo CoreRPG y CTest sintético heredados de D11.

**Dictamen documental actualizado: D.P13 COMPLETA CON RESERVAS.** Cobertura ambiental comparable al borrador geográfico de Valrik/Treskal a nivel conceptual y de contratos; no equivale a cotas, posiciones ni simulación de terreno en CoreRPG/Godot. Las reservas de materialización se trasladan sin inventarlas. Este anexo registra una ejecución concreta, no sustituye la obligación de comprobar las Actions correspondientes a cualquier HEAD nuevo.

## Adenda de altitud aprobada (25-10-2026)

La reserva previa «sin alturas de Valkram» es **histórica y parcialmente resuelta**: escala B de grandes cumbres Valkram (3.600–4.200 m) y máximo absoluto de Norgard de **aprox. 4.200 m** en la cumbre del norte de Valkram entre N/O del rótulo. Otras altitudes, divisorias y geometrías siguen UNKNOWN. Ver `12_altitud_valkram_autorizada.md` y el JSON AUTHORED de altitud. No confundir el dato aprobado con malla métrica ni con climatología medida.

## Resoluciones canónicas adicionales — 25/10/2026

**la Viuda** queda aprobada como topónimo oficial de la cima de ~4.200 m del norte de Valkram, récord absoluto de Norgard. **Elyra, opción A**, queda aprobada para cumbres de hasta ~2.600 m. Son anclas expresamente aprobadas por el autor y almacenadas en los contratos de elevación; el resto de las cotas y geometrías sigue UNKNOWN. Validez documental, sin runtime ni mapa de alturas. 

## Decisión de nieve aprobada con posterioridad a la auditoría

`DAR-DP13-SNOW-01` confirma **neveros localizados que sobreviven al verano en la Viuda**, únicamente en zonas altas y resguardadas. Las incógnitas nival-métricas restantes y la existencia de glaciares no se resuelven. Se incorpora al JSON autoral y la batería negativa sin suponer un sistema físico en runtime.

## DAR-DP13-PASS-01 — Altitudes orientativas de los principales pasos de Valkram (25/10/2026)

**Decisión expresa del autor: OPCIÓN B (APROBADA).** Los principales **pasos naturales** practicables de los Montes Valkram tendrán un **rango de referencia aproximado de 1.400 a 2.200 metros sobre el nivel del mar**.

Este intervalo describe la **categoría general de los pasos principales**, no la cota de todos los collados, ni una obligación de distribuirlos uniformemente en esas alturas. Pueden existir relieves menores o collados más altos si el canon y la futura topografía lo permiten; la decisión **no autoriza** afirmar nombres, cantidad, emplazamientos, rutas, pasos abiertos durante todo el año, infraestructuras, puentes ni caminos nuevos.

**Comportamiento plausible (DERIVED_CONDITIONAL, no hecho local decretado):** a esas alturas, algunos pasos pueden sufrir nieve, hielo, viento o dificultades de circulación durante episodios fríos. No se aprueban cierres regulares, fechas, duraciones ni cotas de nieve de pasos individuales. **La Viuda (≈4.200 m) y sus neveros de verano permanecen intactos**.

**Dato operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `principalNaturalPasses`. Esta nueva autorización sustituye el UNKNOWN anterior referido al **rango general de pasos principales**, pero no resuelve la altitud individual de ningún paso ni la cartografía métrica. Fuentes: aprobación expresa del autor en conversación D.P13, 25/10/2026, y canon de `Geografía/montanas.md`.


## DAR-DP13-CITY-ALT-01 — Altitud de Treihord (25/10/2026)

**APROBADA — opción A:** banda de referencia de **150–350 m s. n. m.** para el emplazamiento urbano general de Treihord. No se fija una altitud exacta de la ciudad ni de sus ocho barrios, muelles o plazas. Tampoco cota del Belara, pendientes, accesos, nuevos puentes o navegabilidad. La ciudad sigue **junto al Belara, sin que el río la atraviese**, y su puerto continúa siendo exclusivamente industrial para barcazas de poco calado. Este rango es dato de **autor**, no altimetría métrica de un mapa.

Documento: `D.P13/14_altitud_treihord_autorizada.md`; contrato: `Datos operativos/darovan_dp13_treihord_elevation_authorial_v0.1.json`. Uso para D.P16/D.P18 únicamente como referencia, sin iniciar esas fases.


## DAR-DP13-CITY-ALT-02 — Altitud urbana orientativa de Veldora (25/10/2026)

**OPCIÓN A APROBADA POR EL AUTOR:** el emplazamiento general de **Veldora** tiene un rango altitudinal aproximado de **0–60 m s. n. m.**, que admite una franja litoral baja y zonas interiores más elevadas sin fijar cotas individuales. La ciudad permanece como **principal puerto comercial marítimo de Darovan en el Golfo de Veldora**.

No se asignan alturas a muelles, calles, barrios, mar, mareas, lechos o desembocaduras fluviales. Los ríos **Lhera** y **Veldora** conservan su independencia; la identidad del cauce mostrado tras la ciudad en el perfil visual sigue **UNKNOWN (DAR-P07)**. El dato de autor no es un levantamiento topográfico ni genera infraestructura, poblaciones, rutas o WorldState.

Documento: `D.P13/15_altitud_veldora_autorizada.md`. JSON: `Datos operativos/darovan_dp13_veldora_elevation_authorial_v0.1.json`. Decisión destinada a D.P16/D.P18 sin iniciarlas.


## Corrección de Veldora en el cierre de suficiencia

La opción vigente aprobada es **A, 0–60 m** para el núcleo urbano principal de Veldora, y no la opción B/0–150 m que aparecía en el registro provisional. Sin cambios a los ríos Lhera/Veldora, puerto o microaltitudes UNKNOWN.

## DAR-DP13-CITY-ALT-03 — Taramin, opción A (25/10/2026)

**APROBADO POR EL AUTOR:** el **núcleo urbano principal de Taramin** tiene una banda altitudinal de referencia aproximada de **0–40 m s. n. m.**. No define una altitud exacta de barrios, muelles, nivel de agua, pendientes o plano georreferenciado. Mantiene un único **Thalen** con **dos brazos terminales** entre los que se sitúa la ciudad; las conexiones físicas, navegabilidad y emplazamiento exacto de estructuras permanecen UNKNOWN. No se crea isla, puente, vía, canal, puerto adicional ni escenario de inundación.

Documento: `D.P13/16_altitud_taramin_autorizada.md`. Registro: `Datos operativos/darovan_dp13_taramin_elevation_authorial_v0.1.json`. La cifra es una decisión autoral y no una topografía métrica ejecutada; no inicia D.P16/D.P18.


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


## Cierre delegado de preguntas Q13–Q28 — 25/10/2026

El autor concede autonomía expresa al asistente para escoger las opciones recomendadas de todas las preguntas pendientes. Se registran **16 opciones B (Q13–Q28)**, de las cuales cuatro son nuevas referencias altitudinales: **valles interiores de Valkram 700–1.300 m**, **pasos principales de Elyra 900–1.500 m**, **valles interiores de Elyra 400–900 m**, **lomas del ámbito forestal meridional de Taramin fuera de Elyra 150–500 m**. Las restantes protegen condiciones climáticas, agua menor, suelo, vegetación y riesgos sin inventar mediciones.

Las decisiones son del **asistente por delegación** y no respuestas individuales dadas por el autor; en ningún caso suponen geometría métrica, vientos medidos, glaciares, cauces ubicados o simulación CoreRPG/Godot. Documentación: `D.P13/22_cierre_delegado_preguntas_y_opciones.md`; datos: `Datos operativos/darovan_dp13_delegated_decisions_authorized_v0.1.json`. D.P14 y fases posteriores siguen sin iniciar; PR #39 Draft, main sin fusionar.


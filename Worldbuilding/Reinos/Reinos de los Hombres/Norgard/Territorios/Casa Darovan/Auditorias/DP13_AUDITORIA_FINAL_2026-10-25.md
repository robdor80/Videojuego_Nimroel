# D.P13 — Auditoría integral de profundidad, autoridad y entrega

**Fecha:** 25 de octubre de 2026. **Rama:** `feat/darovan-dp13-territorio-fisico`. **PR:** #39 Draft, sin autorización de fusión. **Base:** D12 #38 fusionada en `main` mediante `aa3c162d4a3f58a41331fdc6bb9479b39d708afc`.

## Inventario de cambios

- Doce capítulos `D.P13/00_…11_` y README de acceso.
- `Datos operativos/darovan_dp13_physical_profiles_v0.1.json`: 12 zonas/14 dimensiones explicativas y referencias.
- `Datos operativos/darovan_dp13_hydro_overlay_v0.1.json`: 4 sistemas, 5 ríos canónicos, 12 roles potenciales de cuenca y restricciones.
- `Datos operativos/darovan_dp13_environment_causal_v0.1.json`: 10 reglas causales, 8 escenarios conceptuales negativos y campos de persistencia futura.
- `Tools/DarovanDP13/validate.py`: invariantes y **24 mutaciones adversariales**.
- Workflow `.github/workflows/darovan-dp13-regression.yml`; traspaso `TRASPASO_DP14.md`.

## Alcance verificado manualmente

Se leyeron los índices y capítulos 00–09 del clima de Casa Valrik y su geografía local para microrelieve, cuencas y reglas espaciales, incluido el JSON de hidrología de Treskal. Se contrastaron los datos D01/D02/D03, inventario D12, geografía de Norgard, Treihord y bosques. Son diseños de autoridad distinta: Valrik es borrador de diseño aprobado dentro del borrador, **no** fuente climática canónica aplicable a Darovan.

## Matriz de suficiencia

| Eje | Resultado | Reserva explícita |
|---|---|---|
| 12 unidades, transiciones | Cubierta por perfiles y matriz | No son polígonos administrativos |
| Relieve y microrelieve | Criterios para montaña, costa, valle, isla y península | Sin alturas ni mapa altimétrico |
| Cuencas y cauces | Recepción y generación condicionada, 4 sistemas invariantes | Nacimiento y desembocadura Fhalion exactos UNKNOWN |
| Termicidad / estaciones | 4 estaciones por contexto, 12 perfiles de respuesta | Sin grados ni calendario real |
| Lluvias / nieve / hielo | Reglas por cuenca, exposición, aporte y nieve previa | Sin mm, caudales ni glaciares |
| Viento / niebla | Flujo por episodio, exposición, condensación | Rosa de vientos Darovan UNKNOWN |
| Suelo / erosión / barro | Permeabilidad condicionada y casos regionales diferenciados | Sin datos edafológicos medidos |
| Vegetación / bosques | Seis identidades forestales y gradientes protegidos | Sin especies o nuevas extracciones |
| Generación espacial | Anclas→relieve→divisoria→cuenca→cauce→estados | Algoritmo CoreRPG no implementado |
| Persistencia | Variables, autoridad, versión, identidad futura | No existe WorldState territorial ejecutado |
| Validaciones | 24 negativas y regresiones en Actions | Confirmar verde definitivo del HEAD de la PR |

## Dictamen de suficiencia cualitativa

**Comparable con Valrik/Treskal al nivel de worldbuilding ambiental y contratos conceptuales**, con doce unidades diferenciadas y matriz temática exhaustiva; NO comparable todavía con el plano métrico de la **ciudad** de Treskal, que corresponde a la etapa urbana D.P16. La ausencia de cifras, perfiles medidos y accidentes nominados responde a límites de canon y no debe ocultarse como desarrollo completo de terreno jugable.

**Dictamen provisional: COMPLETA CON RESERVAS DE MATERIALIZACIÓN/CARTOGRAFÍA**, condicionado al éxito de D.P13 y regresiones D01–D12 Windows/Linux sobre el HEAD definitivo. Si falla alguna, mantener D.P13 INCOMPLETA hasta corregirla.

## Decisiones de autor / UNKNOWN

No hay bloqueo autoral para el diseño cualitativo. En materialización quedarán por decidir: altitudes exactas y malla, divisorias, nacimientos, Fhalion, escala cartográfica, geometría de Belara/Lhera, cauces/manantiales menores, vientos estacionales y suelos; no se ha promocionado ninguna hipótesis a canon.

## Acciones excluidas

No se fusiona la PR, ni se borran ramas. No se modifica CoreRPG, NIM/Godot, D00–D12, geometría de ciudades, asentamientos D.P14, economía D.P15, desarrollo urbano D.P16, sociedad D.P17 ni cartografía final D.P18.

## Evidencia posterior — GitHub Actions, 25-10-2026

El commit de documentación y auditoría `3b77cd9f70f36d1ec49344b941d71a34a6f87184` superó ambas baterías de GitHub Actions:

- [D.P13 específica — ejecución #40186172798](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40186172798): **SUCCESS** tanto en `windows-2022` como en `ubuntu-24.04`. Doce zonas; cuatro sistemas; diez reglas causales; 24 pruebas adversariales rechazadas.
- [Regresión D01–D12 — ejecución #40186172806](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40186172806): **SUCCESS** tanto en `windows-2022` como en `ubuntu-24.04`, incluida la compilación C++ de catálogo CoreRPG y CTest sintético heredados de D11.

**Dictamen documental actualizado: D.P13 COMPLETA CON RESERVAS.** Cobertura ambiental comparable al borrador geográfico de Valrik/Treskal a nivel conceptual y de contratos; no equivale a cotas, posiciones ni simulación de terreno en CoreRPG/Godot. Las reservas de materialización se trasladan sin inventarlas. Este anexo registra una ejecución concreta, no sustituye la obligación de comprobar las Actions correspondientes a cualquier HEAD nuevo.

## Adenda autoral posterior a la auditoría (25-10-2026)

Aprobada en D.P13 opción B de altura de grandes cumbres Valkram (3.600–4.200 m), junto con una **cumbre excepcional de aproximadamente 4.200 m**, récord absoluto de Norgard, localizada visualmente al norte de Valkram entre las letras N y O del rótulo NORGARD. Conservar alturas restantes UNKNOWN y el estado documental/no runtime. La comparación general con Azurios queda pendiente de armonización editorial superior, sin invalidar esta decisión expresa. Ver `D.P13/12_altitud_valkram_autorizada.md`.

## Ampliación de decisiones de altitud — 25/10/2026

El topónimo **la Viuda** reemplaza la reserva del nombre para la cumbre máxima (~4.200 m) del norte de Valkram. La altura orientativa de las cumbres más altas de Elyra queda aprobada en **~2.600 m (A)**. Ninguna supone topografía métrica ni reabre D01–D12. Ver `D.P13/12_altitud_valkram_autorizada.md` y `D.P13/13_altitud_elyra_autorizada.md`.

## Anexo autoral de nieve en la Viuda (25/10/2026)

Decisión **DAR-DP13-SNOW-01**, **opción A**: neveros persistentes durante el verano en sectores altos y resguardados de **la Viuda** (~4.200 m, norte de Valkram). Se corrige únicamente la incógnita de persistencia nival local para esta cumbre, sin geometría, nieve perpetua en toda la cordillera, cotas de nieve ni afirmación de glaciares. Se actualizan los contratos y las pruebas de canon. La auditoría de suficiencia territorial general mantiene sus reservas de materialización.

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


## Rectificación de la banda altitudinal de Veldora — 25/10/2026

La decisión autoral **DAR-DP13-CITY-ALT-02** es **opción A, de 0–60 m** para el núcleo urbano principal. La versión que anotaba **opción B (0–150 m)** fue una discrepancia de registro y queda expresamente invalidada, sin modificar el canon hidrológico ni las fases previas. El dato autoral es aproximado, no cartografía métrica.

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


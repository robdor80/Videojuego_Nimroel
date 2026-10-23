# Registro de fases — Casa Darovan
**Fecha de comprobación:** 21-10-2026. **Estados comprobados en GitHub el 21-10-2026:** D00–D04 integradas en main; D01–D03 Python MSI superados; D01–D05 Python GitHub Actions Windows/Linux superados. D05 documental cerrada y validada en CI Windows/Linux; PR #30 preparada para revisión, no fusionada; decisión de merge reservada al autor.

| Fase | Entrega | Estado | Conversación |
|---|---|---|---|
| D00 | Canon, auditoría, estructura, metodología y protocolo | **FUSIONADA en main, PR #14** (merge commit 73aa5c4691a3dc07ca588c07a7ce267a69fdd085) | Darovan 1 |
| D01 | Geografía y orografía | **FUSIONADA EN MAIN, PR #15**, merge 9f3f723b0e7b2b78567c6397bba7099bfe658b0a | Darovan 2 |
| D02 | Hidrografía y cuencas | **FUSIONADA EN MAIN, PR #16**, merge 34c9652eba2bd0fed33ab6a3931f24400a39b812; no-runtime | Darovan 3 |
| D03 | Clima y ecosistemas | **FUSIONADA MAIN, PR #17 squash 191bcd5; PYTHON MSI D01–D03 SUPERADO**; 12 zonas de estudio cualitativas; no-runtime/no canon nuevo | Darovan 4 |
| D04 | Recursos y producción | **FUSIONADA EN MAIN**, PR #20, commit d4a07ba25f8560d5005a52aafc763699917f2388; CI D01–D04 Windows/Linux OK; no runtime | Darovan 5 |
| D05 | Movilidad y comunicaciones | **DOCUMENTALMENTE CERRADA Y CI ESTÁTICA WINDOWS/LINUX OK**; PR #30 en revisión, SIN FUSIONAR; no canon nuevo ni runtime, merge exige autor | Darovan 6 |
| D06 | Asentamientos ordinarios y diseño procedural | DOCUMENTACIÓN / CI D01–D06 WINDOWS+LINUX SUPERADA en primer run #39627654566; PR Draft #31 sin fusionar; no runtime | Darovan 7 |
| D07 | Ciudades canónicas | **EN REVISIÓN — rama exclusiva, PR Draft pendiente de auditoría CI/autor; NO FUSIONADA** | Darovan 8 |
| D08 | Población y servicios | NO INICIADA | Darovan 9 |
| D09 | Administración y defensa | NO INICIADA | Darovan 10 |
| D10 | Cultura y sociedad | NO INICIADA | Darovan 11 |
| D11 | Contratos y motor | NO INICIADA | Darovan 12 |
| D12 | Auditoría integral | NO INICIADA | Darovan 13 |

**Evidencia:** MSI físico (15-10-2026): D01/D02/D03 `STATIC OK` en checkout local (acta D03). CI Windows 2022 + Ubuntu 24.04 (21-10-2026): D01/D02/D03/D04/D05 `STATIC OK` en checkout íntegro de la rama D05 (run `39587112092`, [acta](../Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md)). No prueba Godot/GIS/runtime ni MSI físico D04/D05. PR #20 **ya fue fusionada**; D05 PR #30 está abierta sin merge.

**Protocolo:** una fase/conversación/rama, PR propia, sin merge automático. La validación documental NO acredita canon nuevo, mapa métrico ni juego ejecutado. D00–D04 están integradas; D05 requiere aprobación de PR #30. D06 aún no se ha iniciado.

## Inicio D05 comprobado 21-10-2026
GitHub confirmó PR #20 fusionada y `main` en `d4a07ba25f8560d5005a52aafc763699917f2388` antes de crear rama D05. D05 documenta red modal, datos, validación y traspaso D06 sin comenzar D06. [CI de la PR #30 D01–D05](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092) superada en Ubuntu y Windows, con 30 negativas D05 rechazadas. [Acta D05](../Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md). El commit final de auditoría se verificará nuevamente en Actions.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.

## Seguimiento D06 — 21-10-2026
- **D05 PR #30 fusionada en main** (commit `0818886f8cc9f91c21b5db00f91feb1b942d230d`) antes de crear D06.
- D06 prepara reglas y simulaciones `TEST_ONLY` con nueve modelos, doce unidades D01, esqueleto obligatorio, pesos relativos no demográficos, validador Python y 42 negativos. Sin nuevos topónimos ni asentamientos canónicos.
- D06 rama `feat/darovan-d06-asentamientos-ordinarios` y PR Draft propia; comprobar CI Windows/Linux y acta antes de afirmar cierre. No fusionar sin permiso. D07 NO INICIADA.
- **Nota histórica:** el antiguo estado D05 «sin fusionar» más arriba refleja el estado de redacción anterior al merge del 21-10-2026, no el estado actual de GitHub.

## Inicio D07 confirmado — 21-10-2026
- D06 PR #31 **fusionada** en main mediante e2636f33791b11ec6ad2e478df95ab190de0f09e. GitHub Actions post-merge #39628590145 completada en verde Windows/Linux; las afirmaciones antiguas «D06 sin fusionar» de arriba son históricas.
- Nueva rama exclusiva feat/darovan-d07-ciudades-canonicas, desde ese commit. Canon Treihord cerrado conservado; tres perfiles de ciudad con propuestas urbanas aún no aprobadas.
- D07 añade auditorías, matriz de hechos y fuente, JSON de planificación con UNKNOWN, 9 capas conceptuales PROPOSAL_PENDING_AUTHOR, validador y CI D01–D07. No runtime ni demografía D08.
- **No merge automático ni D08.** Los enfoques pendientes de aprobación son DAR-D07-01/02/03. CI de HEAD D07 se registrará al finalizar; no presumir éxito de un run previo.

## Actualización D07 — Resolución autoral 02 (21-10-2026)
Veldora DAR-D07-01 B y Taramin DAR-D07-02 A aprobadas **solo a nivel conceptual**. Taramin organiza su actividad pesquera alrededor de una zona principal sin fijar ubicación, accesos, navegación ni infraestructura. Queda pendiente DAR-D07-03 Syvaris. Se mantiene la PR #32 como Draft, sin fusionar ni iniciar D08.

## D07 — Cierre de las tres decisiones urbanas conceptuales (21/10/2026)
El autor aprobó DAR-D07-01 Veldora **B** (varios sectores comerciales orgánicos); DAR-D07-02 Taramin **A** (una zona pesquera principal); y DAR-D07-03 Syvaris **A** (actividad urbana principal concentrada alrededor de la bahía protegida). Son decisiones de orientación funcional, **sin aprobación de trazados, barrios, puertos o edificios concretos**. Las incertidumbres geográficas y demográficas continúan sin inventar. PR #32 preparada para revisión, sigue Draft y no fusionada; D08 no comenzada.

## Actualización D08 — 21/10/2026 (no sustituye el historial)
**Estado real GitHub verificado al inicio de D08:** D00–D07 FUSIONADAS en `main`; D07 PR #32 fusionada, merge `23670e68532447d918c04839369a9962448f2e44`; post-merge Actions #39669078239 comunicada como verde (verificación del estado corriente en el inicio D08). D08 tiene rama exclusiva `feat/darovan-d08-hogares-poblacion-servicios`; entregables exclusivamente documentales/JSON de planificación y 35 negativos; PR Draft prevista para auditoría humana. **D08 NO FUSIONADA, D09–D11 NO INICIADAS.** Ningún resultado estático acredita CoreRPG/Godot runtime.

## Aprobación parcial DAR-D08-01 — 22/10/2026
El autor aprueba Veldora **opción B, intervalo 29.000–35.000 habitantes** como rango demográfico canónico, sin censo exacto. Registro incorporado solo a rama D08/PR Draft #34. Taramin, Syvaris y total Darovan siguen `UNKNOWN`. D07 no se altera; D09–D11 no se inician.

## Aprobación parcial DAR-D08-01 — Taramin — 22/10/2026
El autor aprueba **opción B, rango 14.000–20.000 habitantes** para Taramin como canon de referencia, sin censo exacto. Veldora B (29.000–35.000) y Treihord ~32.000 conservadas. Syvaris y población total Darovan permanecen `UNKNOWN`. Se anexa la decisión y se amplían validaciones en rama D08, PR #34 Draft sin fusión. Ninguna fase D09–D11 iniciada.

## DAR-D08-01 — Resolución Syvaris (22/10/2026)
El autor aprueba **opción B 7.000–10.000 habitantes**, rango de la **ciudad** de Syvaris; el resto de su isla, el total insular y el total demográfico de Darovan permanecen `UNKNOWN`. Se incorporan acta autoral, JSON, esquema y nuevas pruebas negativas a D08. Veldora B, Taramin B y Treihord sin alterar. **PR #34 permanece Draft y no fusionada**, D09–D11 no iniciadas.

## DAR-D08-01 — Total de población territorial aprobado (22/10/2026)
El autor elige opción B: **rango canónico de 300.000–450.000 habitantes para toda Casa Darovan**, sin fijar censo puntual, porcentajes rurales/urbanos, nuevas localidades ni habitantes por asentamiento. Se completan los rangos autorales de DAR-D08-01 (tres ciudades + total territorial) y se mantienen incógnitas documentadas; D08 solo planificación y pruebas estáticas. PR #34 sigue Draft SIN FUSIONAR, D09–D11 no iniciadas.

## DAR-D08-02 — Aprobación de hogares urbanos (22/10/2026)
Autor aprueba **opción B, intervalo 3–5 personas por hogar urbano de media**. Fuente archivada con referencia autoral, índice JSON, esquema y regresiones negativas en rama D08. No se autoriza censo de hogares ni viviendas, media urbana exacta, media rural o cambios a los cuatro rangos urbanos y total Casa Darovan aprobados. PR #34 sigue abierta en Draft SIN FUSIONAR.

## Resolución conjunta de cierre documental D08 — 22/10/2026
En un solo lote, autor aprueba **rural B 4–6** media por hogar, **edad 1B 30/60/10**, **diferencias edades urbano/rurales 2C sin desglose**, **reparto territorial 3C urbano 35–45 % / rural 55–65 %** y **social 4A sin categorías ni instituciones nuevas en D08**. Persisten cifras exactas y asentamientos no registrados como `UNKNOWN`; cuatro ciudades no bastan para cubrir el porcentaje urbano y no se crean otras. Acta `../Auditorias/D08_RESOLUCION_LOTE_FINAL_2026-10-22.md`; entrega documental lista para revisión tras CI del nuevo HEAD, sin runtime ni fusionar PR #34. D09–D11 no iniciadas.

## Constancia administrativa de cierre D08 — 22/10/2026
**D08 CERRADA DOCUMENTALMENTE Y FUSIONADA EN `main`.** [PR #34](https://github.com/robdor80/Videojuego_Nimroel/pull/34) fusionada el **22/10/2026, 11:00:26 UTC**, mediante commit de merge `b2a9bdedee29fa156f04eef2dd9fcb479e78be91`. [GitHub Actions posterior a la fusión #39767329941](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39767329941): **SUCCESS** en Ubuntu 24.04 y Windows 2022, con regresiones D01–D08 y **125 mutaciones negativas D08**. Rama original `feat/darovan-d08-hogares-poblacion-servicios` **eliminada**, comprobado en GitHub.

Esta nota **actualiza el estado administrativo**, no modifica las decisiones autorales, el canon, las cifras ni el funcionamiento del juego. Las referencias precedentes a PR Draft/sin fusionar y CI pendiente son **históricas**, anteriores a este cierre. Continúan `UNKNOWN` los censos exactos, número de hogares, poblaciones de asentamientos no definidos, cobertura urbana no inventariada, NPC, oficios concretos, edificios/capacidades y funcionalidades de ejecución; estas reservas no impiden el **cierre documental D08**. **D09–D11 no iniciadas ni autorizadas por esta anotación.**


## Inicio y paquete final D09 — 22/10/2026
D08 PR #34 fusionada en main `b2a9bdedee29fa156f04eef2dd9fcb479e78be91`, registro administrativo `1b64b3894d12c5b95c1894f1a6564c064e5efddb`; [GitHub Actions #39767826469](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39767826469) verificada SUCCESS Windows/Linux sobre el HEAD de inicio D09. El autor aprueba en lote 17 decisiones conceptuales G01–G06/F01–F04/D01–D04/S01–S03; G05C, G06A y F04C mantienen UNKNOWN.
**D09 desarrollada documentalmente en rama exclusiva `feat/darovan-d09-gobierno-fiscalidad-defensa`, PR Draft pendiente de revisión/fusión; validación D01–D09 final se comprueba en la propia PR.** No se acredita ejecución CoreRPG/Godot ni se inicia D10. Estados de D09 como «no iniciada» en tablas anteriores son históricos y quedan sustituidos por esta adenda. Sin fusionar a `main` sin autorización.

## Inicio D10 — autorización autoral 23/10/2026
Verificada directamente PR #35 D09 fusionada y main `26a2ed5d43b6bd794bad8954b28994742d52ac97`; [Actions post-fusión #39775254865](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39775254865) SUCCESS Windows 2022 + Ubuntu 24.04. La afirmación histórica `D10 NO INICIADA` en las secciones precedentes se sustituye por la presente adenda. **D10 AUTORIZADA**: 17 decisiones culturales de lote, D10-01–08 B, D10-09 C y D10-10–17 B, según respuesta textual «Apruebo todas tus recomendaciones». Rama propia `feat/darovan-d10-cultura-sociedad`, no modifica D00–D09, preparación documental/JSON/schema/tests de planificación únicamente. **D10 NO FUSIONADA** y D11/D12 NO INICIADAS. No anticipar CI ni ejecución CoreRPG/Godot.

## Cierre documental D10 en PR Draft — 23/10/2026
Aprobadas las 17 opciones D10 por el autor (01–08 B, 09 C, 10–17 B). Documentación cultural, matriz de fuentes, JSON/schema, 16 TEST_ONLY y validador con **98 mutaciones negativas rechazadas**. La PR **#36** permanece **Draft, SIN FUSIONAR**. [GitHub Actions run #39951196364](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39951196364) dio **SUCCESS Windows 2022 y Ubuntu 24.04** para la revisión `878a1a932e56b2815478d0151233d2793156cea0`, tras corregir una aserción del validador contra el objeto ampliado de D08 sin cambiar el canon. El cierre administrativo final añade acta y esta nota; **revalidar su nuevo HEAD** antes de decidir fusión. Integridad: 34 referencias de fuentes existentes; sin cambios D00–D09 ni ejecución CoreRPG/Godot/GDExtension. D11 y D12 **NO INICIADAS**.

## Inicio D11 — 23/10/2026
Autorizada D11 tras fusión de PR #36; main a5d25d8e6a1d70015a63b0327837fd0da0004cbd y postmerge Actions #40026616322 SUCCESS Windows/Linux. Rama exclusiva feat/darovan-d11-integracion-contratos-pruebas. Auditoría CoreRPG 4.13 fijada a 4f282863737bcd8f5add401202a9e1064c133672. Entregado primer pack estructural de 5 IDs, sidecar con locks 11 fases, T01–T08 TEST_ONLY y validadores/C++ CI. **CI D11, PR y cierre PENDIENTES de verificación**. No cambia D00–D10 ni Core/Godot; D12 NO INICIADA.

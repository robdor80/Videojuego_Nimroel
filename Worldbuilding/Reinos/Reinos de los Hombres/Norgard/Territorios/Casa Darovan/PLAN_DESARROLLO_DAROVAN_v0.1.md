# Darovan — plan de desarrollo integral v0.1
**Estado:** PLAN DE TRABAJO (NO CANON). **Inicio:** 15-10-2026. **Responsable de aprobar canon:** autor.

## Convenciones y criterios de aceptación generales
- Jerarquía: `Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`.
- Cada entrega diferencia `canon_fuente`, `inferencia_mapa`, `propuesta_tecnica`, `pendiente_autor`.
- Treihord conserva su documento canónico actual; lo demás añade referencias y capas operativas, no lo reemplaza.
- Veldora, Taramin, Syvaris y Treihord son lugares canónicos individuales; **nunca** se generan como asentamientos ordinarios.
- Los documentos aprobados de Valrik son referencias metodológicas, no perfiles transferibles.
- No se afirma funcionamiento runtime por disponer de contratos JSON; requiere integración real con CoreRPG/Godot y pruebas.
- En cada fase: inventario de fuentes, especificación separando niveles, datos operativos si procede, comprobación de referencias y JSON, informe de deuda y PR propio o incrementos auditables. **No merge automático.**

## D00 — Auditoría y arranque [FUSIONADA EN MAIN; PR #14]
- Inventario del canon, fuentes, perfiles, reglas y alcance. Diferencias de línea roja y frontera.
- Comparación con árboles Valrik/Treskal y Core/Defaults.
- Registrar resolución canónica Belara (Eshneva descartado para Darovan por decisión del autor), y detectar dudas pendientes (Arven, casas menores/figuras nobles).
- Entregables: auditoría, inventario del mapa, este plan y manifiesto inicial no-runtime.
- **Cierre 15-10-2026:** estructura territorial y de ciudades preparada; anclas de Treihord y cuatro ciudades auditadas; fuentes trazadas; protocolo de una fase por conversación y una PR por fase; pendientes preservados. Ver `Auditorias/D00_CIERRE_Y_VALIDACION_2026-10-15.md`.
- **Salida:** fuentes trazadas, ninguna alteración de canon, pendientes registrados. La PR debe ser autorizada para fusionar; D01 no comienza en esta conversación.

## D01 — Límites, subregiones y geografía física [FUSIONADA EN MAIN; PR #15]
- Delimitar cualitativamente montaña, costa, bahías, islas, península, gradientes y relaciones políticas sin cartografía falsa.
- Separar capas físicas/administrativas y puntos de control; capa georreferenciada solo cuando exista plano/escala.
- Aplicar contrato Core `nimroel_physical_geography_drainage_contract_v0.1.json`.
- **Salida D01 (15-10-2026):** marco físico y 12 unidades cualitativas con fuentes, perfil JSON no-runtime, interfaz cartográfica, matriz de 18 controles, acta y traspaso D02. **Cierre documental, NO canon nuevo ni implementación runtime.** PR #15 fusionada en main (9f3f723b0e7b2b78567c6397bba7099bfe658b0a).

## D02 — Hidrología y drenaje [FUSIONADA EN MAIN; PR #16]
- Grafos Belara/Lhera/Veldora/Thalen, cuencas, afluentes plausibles, manantiales y arroyos con límites estrictos.
- Zonas de inundación, estacionalidad, vados, navegabilidad y recursos hídricos sin caudales inventados.
- **Salida D02 (15-10-2026):** 4 ríos, 3 sistemas topológicos, 13 nodos, 10 aristas; cuencas cualitativas, perfil JSON no-runtime, reglas, validador y acta. Sin afluentes, caudales, medidas ni geometría inventados; PR propia para revisión y sin merge.

## D03 — Climas y ecosistemas [FUSIONADA EN MAIN, PR #17]
- Clima del litoral Veldora, Valkram, transición fría norte, península Taramin y Syvaris; microclimas y suelos.
- Evitar falsa homogeneidad: costa atlántica, altura, sotavento, valle, corredor seco y protegido.
- **Salida D03 (15-10-2026):** 3 documentos climáticos/ecológicos, 12 unidades D01 trazadas, JSON de planificación NO RUNTIME, 30 invariantes, script de regresión, acta y traspaso D04; sin grados, lluvias, cumbres, especies o ríos nuevos.
- **Estado vigente:** validadores Python D01/D02/D03 superados por el autor en MSI checkout completo 15-10-2026; PR #17 fusionada squash 191bcd5. Godot/GIS siguen pendientes; NO RUNTIME.

## D04 — Recursos y economía territorial [DOCUMENTALMENTE CERRADA; PYTHON CI WINDOWS/LINUX OK; PR #20]
- Oro/plata/minas, fundición y ensayo, carbón importado de Azurios, madera de Pilares, agricultura, pesca/puertos y transportes.
- Revisar fiscalidad E8, moneda E2, transacciones Core, sin aduanas internas entre Grandes Casas.
- **Salida D04:** 4 documentos, 12 unidades, 8 cadenas, 19 fuentes y validador Python con 16 negativos; 22 controles JS remotos superados. **21-10-2026: Python D01–D04 STATIC OK tanto en Windows 2022 como Ubuntu 24.04 con checkout íntegro de GitHub Actions (run #39583142837).** No se ha ejecutado físicamente D04 en el MSI; esa repetición es opcional, no condición de cierre estático. Godot/GIS/CoreRPG runtime no ejecutados por D04. PR #20 fusionada el 21-10-2026, commit `d4a07ba25f8560d5005a52aafc763699917f2388`; no canon nuevo.

## D05 — Red de transporte, rutas y comunicaciones [DOCUMENTALMENTE CERRADA; CI WINDOWS/LINUX OK; PR #30 SIN MERGE]
- Corredores existentes (Veldora–Treihord), transporte mineral/Belara, accesos a Taramin, cabotaje y Syvaris.
- Caminos, puentes, vados, barcazas, mercantes, barcos pesqueros, mensajería y tiempos derivados por terreno cuando exista escala.
- **Salida:** grafo modal básico, nodos y restricciones, sin kilómetros/itinerarios ficticios.

## D06 — Asentamientos ordinarios y generación procedural [EN REVISIÓN; RAMA EXCLUSIVA]
- Aldeas → pueblos → villas; enclaves mineros, pesqueros, forestales, agrícolas, isleños y servicios de ruta.
- Esqueleto obligatorio → posibilidades → condiciones → pesos regionales → modelos → instancias y seed.
- Diferenciar distribución espacial, servicios y límites logísticos de rangos Valrik.
- **Salida:** modelos Darovan verificables y datos no canónicos de prueba.

## D07 — Las ciudades canónicas [FUSIONADA EN MAIN, PR #32]
- **Treihord:** extracción de referencias, necesidades operativas, validación con canon vigente **sin rediseñar**; cartografía técnica solo cuando proceda.
- **Veldora:** auditoría previa de su perfil aprobado y diseño manual puerto comercial/aduanas/almacenes y ciudad.
- **Taramin:** auditoría previa y diseño manual puerto pesquero, desembocadura bifurcada Thalen, abastecimiento.
- **Syvaris:** auditoría previa, bahía principal, calas, puerto y biomas internos diferenciados.
- Cada ciudad: fases de diseño individual con autorización del autor en decisiones de identidad, personajes o acontecimientos.
- **Salida:** matrices de anclas canónicas, sin reemplazar ciudades por generador.

## D08 — Hogares, población, servicios y profesiones [PENDIENTE]
- Integrar Core de población/relaciones/empleo/residencia, ley Norgard y perfil de demanda laboral.
- Cadenas de abastecimiento, cuidados, salud, educación, posadas, transporte y servicios locales.
- Cálculos cuantitativos solo después de aprobar rangos Darovan; sin trasplantar Valrik.
- **Salida:** cobertura de servicios, presupuesto lógico hogares–trabajo–inventarios.

## D09 — Gobierno, fiscalidad, defensa y seguridad [PENDIENTE]
- Delegaciones Casa/Corona, Justicia del Rey, guardias urbanas, guardia de Casa, custodia de minas, puertos y caravanas.
- Reutilizar Norgard E4, E5, E6, E8 y E9. No crear armada autónoma Darovan.
- Componentes políticos sensibles (señor, herederos, casas menores, historias) requieren autor.
- **Salida:** atribución de competencias y contratos de incidencia, seguridad/custodia.

## D10 — Cultura y sociedad local [PENDIENTE]
- Contraste de élites comerciales, trabajadores de minas, comunidades pesqueras, rutas e insularidad.
- Heredar Norgard (nombres, familia, ritos, cultura material, toponimia) sin inventar tradiciones universales.
- **Salida:** perfiles diferenciados de subregiones y variantes locales autorizadas.

## D10-A — Veldora: desarrollo urbano y canónico integral [PROGRAMADA; NO INICIADA]
- **Finalidad:** llevar Veldora a una profundidad descriptiva y funcional comparable a Treihord y Treskal, sin copiar identidad, barrios, instituciones ni composición social de esas ciudades. Fase exclusiva con conversación, rama, auditoría, decisiones de autor y PR propias.
- **Canon inicial:** gran puerto mercante de Norgard; aduana de comercio exterior y presencia administrativa/fiscal de la Corona; almacenes, talleres y gremios; crecimiento orgánico de varios sectores comerciales (decisión autoral **DAR-D07-01 B**); zonas acomodadas alejadas de los muelles. El río Veldora es independiente de Belara/Lhera; no adjudicar puentes, puertos fluviales ni travesías sin evidencia.
- **Diseño a desarrollar:** historia y evolución de la ciudad, organización de barrios y plazas, tejido residencial, mercados/zonas de oficios, muelles ya acreditados como función, arquitectura característica, instituciones acreditadas, actividad económica, hogares, servicios, gobierno, seguridad, cultura y espacios narrativos. Diferenciar propuestas de decisiones cerradas.
- **Dependencias:** D08 población y servicios; D09 competencias; D10 cultura; cartografía D01–D07. Cifras nuevas de población, topónimos, personajes importantes, barrios concretos e instituciones nuevas requieren aprobación expresa del autor.
- **Salida:** monografía canónica aprobable, matriz de fuentes/decisiones/UNKNOWN, fichas urbanas y datos operativos **no-runtime**, validador y auditoría; sin geometría métrica, instalaciones, NPC o world state materializados por defecto.

## D10-B — Taramin: desarrollo urbano y canónico integral [PROGRAMADA; NO INICIADA]
- **Finalidad:** diseñar Taramin con el mismo nivel de detalle editorial y operativo que Treihord y Treskal, adaptado a su propia economía pesquera y territorio, mediante fase/conversación/rama/PR independiente.
- **Canon inicial:** ciudad media pesquera marítima y fluvial entre los **dos brazos terminales del mismo río Thalen**; entorno peninsular de transición semiárida; identidad funcional no monumental y pesca/productos marinos. Decisión autoral **DAR-D07-02 A**: **una zona pesquera principal**, sin ubicación ni navegabilidad de brazos aprobadas. Bosque de Taramin sin tala industrial.
- **Diseño a desarrollar:** historia, sectores urbanos, barrios y espacios comunes, frentes de pesca y comercio acreditables, vivienda, trabajo, oficios, abastecimiento, agua y salubridad, servicios, gobierno/seguridad, arquitectura, cultura local, relaciones socioeconómicas y posibilidades narrativas.
- **Dependencias:** D08–D10 y evidencia hidrográfica/topográfica. No inventar puentes, rutas, embarcaderos, muelles, flotas, navegación, población ni capacidad; cuando falten datos, registrar `UNKNOWN` o alternativa `pendiente_autor`.
- **Salida:** monografía canónica aprobable y datos operativos trazados, estudio de dependencias y riesgos, validación estática/auditoría, sin crear elementos físicos ni NPC en runtime.

## D10-C — Syvaris: desarrollo urbano y canónico integral [PROGRAMADA; NO INICIADA]
- **Finalidad:** desarrollar Syvaris con profundidad comparable a Treihord y Treskal, preservando su identidad de ciudad insular del reino de Norgard bajo administración Darovan. Fase/conversación/rama/PR propia.
- **Canon inicial:** ciudad principal de la isla, más pequeña que Taramin; puerto seguro y **presencia naval de Norgard**, nunca armada privativa de Casa Darovan. Decisión autoral **DAR-D07-03 A**: concentración de funciones urbanas principales en la **bahía protegida**. Calas menores sin nuevos puertos ni rutas acreditadas. Contraste de sur más verde y centro/norte más secos; bosques discontinuos, edificios bajos de piedra y madera, encalado parcial.
- **Diseño a desarrollar:** historia insular, barrios y tejido edificado, centro ligado a bahía, vivienda, pesca/comercio, servicios y abastecimiento, gobierno y seguridad, funciones navales ya acreditadas, adaptación a microclimas, cultura, relaciones comunitarias, personajes relevantes sujetos a autorización y espacios narrativos.
- **Dependencias:** D08–D10, Norgard marítimo/naval, clima D03, recursos D04 y logística D05. Sin atribuir instalaciones militares, flotas, fondeaderos, viajes, puertos secundarios, cifras demográficas o itinerarios no aprobados.
- **Salida:** monografía canónica aprobable y fichas/datos operativos trazados, decisiones y `UNKNOWN` auditables, regresión de compatibilidad; sin materialización en CoreRPG/Godot.

### Condiciones comunes de cierre D10-A, D10-B y D10-C
- Cada ciudad debe alcanzar **profundidad de diseño comparable**, no diseños iguales, a las fuentes canónicas de **Treihord y Treskal**: origen e historia, estructura urbana, espacios reconocibles, economía, hogares y población cuando estén autorizados, servicios, instituciones, sociedad, cultura, personajes e historias solo con aprobación del autor, y utilidad narrativa para Nimroel RPG.
- **Treihord continúa cerrada y no se rediseña.** Treskal sirve como referencia de grado de detalle/metodología, nunca fuente para copiar instituciones, topónimos, demografía ni canon de Valrik.
- Las tres fases son **desarrollo canónico manual**, no generación procedural D06. Ninguna deducción cartográfica, cuantía demográfica o propuesta técnica pasa a canon silenciosamente. El autor toma decisiones sustantivas **una por una**.
- Cada fase tiene entregables versionados, auditoría, validaciones y una PR propia; **no fusionar sin autorización expresa**. La finalización de D10-C y los cierres autorales mínimos habilitan D11; los `UNKNOWN` residuales se rastrean explícitamente y no se ocultan ni impiden pruebas de partes independientes.
- D11 y D12 **conservan su numeración original**: estas tres subfases se insertan entre D10 y D11 y todavía no han comenzado.

## D11 — Integración técnica y pruebas [PENDIENTE]
- Datos con IDs persistentes y trazabilidad fuente; precedencia y versionado.
- Validar JSON/schema real, integridad de referencias, derivación de overrides y determinismo.
- Escenarios: ruta mina–Crisol, bloqueo de carbón, barcaza Belara, comercio exterior Veldora, pesca Taramin, travesía Syvaris, migración de hogares; todos **fixtures de prueba, no sucesos canónicos**.
- Pruebas de continuidad con Norgard/Core/Valrik, ausencia de duplicación y persistencia del world state.
- Integrar las tres ciudades completas de **D10-A Veldora, D10-B Taramin y D10-C Syvaris**, junto al canon cerrado de Treihord, solo cuando existan sus aprobaciones; no simular una ciudad completa a partir de su ficha conceptual D07.
- **Salida:** reporte de regresión estática; runtime SOLO cuando el motor esté integrado y ejecutado.

## D12 — Auditoría integral y cierre territorial [PENDIENTE]
- Comparar canon, perfil geográfico, pueblos, cuatro ciudades (Treihord y las monografías **D10-A / D10-B / D10-C**), rutas, economía, clima y contratos.
- Resolver por el autor los bloqueos de canon; consolidar referencias sin copias.
- Emitir ficha de versión, matriz aprobaciones y deuda real.
- **Salida:** propuesta de cierre a revisión humana; canon solo tras decisión de autor.

## Dependencias y política de desbloqueo
- **Autor:** solo decisiones sustantivas de historia/geografía/política/ciudades/NPC importantes. Es lícito continuar documentos independientes.
- **Terreno o mapa métrico:** cotas, distancias, tiempos y cuencas exactas siguen provisionales.
- **Core RPG:** la integración ejecutable no se presupone completada; contratos estáticos sí se pueden preparar ya.
- **Arven:** no asignar administración Darovan sin confirmación.
- **Belara (RESUELTO 15-10-2026):** por decisión explícita del autor prevalece el canon de GitHub; Belara pasa junto a Treihord, no por su casco urbano. «Eshneva» en el manuscrito es una discrepancia editorial pendiente de revisión del texto, **no** una dependencia de canon o de desarrollo.
- **PR:** revisión por autor, **nunca fusionar `main` sin permiso expreso**.

## Continuidad de conversaciones
Darovan 1: D00 **integrada en main** mediante PR #14. Darovan 2: D01 **fusionada por PR #15**. Darovan 3: D02 **fusionada en main por PR #16**. Darovan 4: D03 **FUSIONADA PR #17, Python MSI D01–D03 OK**, habiendo leído `00_Control_del_proyecto/TRASPASO_D03.md`. Darovan 5: D04 **fusionada PR #20, Python CI Windows/Linux OK (21-10-2026)**. Darovan 6: D05 **desarrollada y validada estáticamente en PR #30; sin fusionar**, solo tras comprobar el merge D04. Una fase por conversación. No presumir merge ni pruebas runtime. Actualizar `Estado` de cada fase con commit por incremento.

## Nota de ejecución D05 (21-10-2026)
D04 PR #20 fusionada en `main` (`d4a07ba25f8560d5005a52aafc763699917f2388`); D05 rama propia desde ese SHA. Grafo cualitativo con 17 nodos, 3 vínculos físicos apoyados por fuentes y 4 relaciones de suministro **no equivalentes a caminos**. Mensajería MSG trazada, cinco riesgos condicionales, sin cartografía, rutas nuevas, mediciones, correos postales ni runtime. D06 no iniciado. CI real D01–D05 Windows/Linux superada en [run #39587112092](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092) (30 negativos D05), cierre documental de D05 acreditado sin activar canon ni runtime; [acta](Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md). PR #30 precisa aprobación del autor para fusionar.


## Adenda operativa D06 — 21-10-2026
D05 PR #30 fue fusionada en `main`, commit `0818886f8cc9f91c21b5db00f91feb1b942d230d`. D06 cuenta con documentos de modelo, datos no runtime, seis casos sintéticos y 42 mutaciones negativas. Los pesos 0–4 son prioridades de diseño, nunca densidades demográficas; solo se valida laboratorio. No se inicia D07 ni se fusiona D06 automáticamente. Las menciones históricas a Arven UNKNOWN y cuatro ríos quedan sustituidas por la corrección del autor: Arven Darovan y cinco ríos/cuatro redes, con Fhalion. Primera CI D01–D06 superada en Windows y Linux, run #39627654566; revalidar commit final de PR.

## Seguimiento D07 — 21-10-2026
Tras verificar la fusión de D06 PR #31 (main e2636f33791b11ec6ad2e478df95ab190de0f09e), D07 trabaja en rama exclusiva feat/darovan-d07-ciudades-canonicas. Entrega técnica prevista: auditoría de cuatro ciudades, Treihord solo compatibilidad con D01–D06, perfiles manuales Veldora/Taramin/Syvaris, matriz de fuente, JSON no-runtime, validación Python y PR Draft. Las decisiones de organización urbana DAR-D07-01/02/03 permanecen pendientes del autor. No se han desarrollado D08, NPC, habitantes nuevos, calles, puertos o rutas; no hay integración CoreRPG/Godot acreditada.

## Actualización del calendario aprobada por el autor — 21-10-2026
**Decisión:** reservar **D10-A (Veldora)**, **D10-B (Taramin)** y **D10-C (Syvaris)** inmediatamente **después de D10** y **antes de D11**. Cada ciudad contará con una fase integral manual, independiente y comparable en profundidad con Treihord y Treskal. No cambia la numeración de D11 (integración) y D12 (auditoría final). **No se han iniciado estas subfases.**
**Estado de partida real para la revisión de este plan:** D00–D07 fusionadas; D07 PR #32 integrada en `main` por commit `23670e68532447d918c04839369a9962448f2e44`, regresión post-merge D01–D07 en Windows/Linux [Actions #39669078239](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39669078239) satisfactoria. Decisiones D07 confirmadas: Veldora B, Taramin A y Syvaris A, **solo a nivel conceptual**. D08 sigue pendiente de iniciar. Los estados históricos anteriores del plan se conservan como cronología y no prevalecen sobre esta nota.

# Decisiones y bloqueos — D00
## Canon resuelto expresamente por el autor
- **DAR-A01:** Las cuatro ciudades canónicas de Darovan son **Treihord (capital), Veldora, Taramin y Syvaris**. No crear otras ciudades principales ni convertirlas en asentamientos procedurales.
- **DAR-A02:** **Karsath pertenece a otra Casa**, queda excluida de Darovan; no inferir dueño Darovan por aparecer cerca del borde del recorte.
- **DAR-A03:** **Belara** es el río canónico junto a Treihord (no atraviesa el casco urbano). El antiguo **Eshneva** queda exclusivamente como errata/discrepancia editorial del borrador narrativo.
- **DAR-A04:** **Una fase por conversación**, comenzando D01 en conversación nueva después de D00.
- **DAR-A05:** No fusionar ramas en `main` sin permiso.

## Pendientes para fases posteriores (NO bloquean D00)
| ID | Asunto | Tratamiento |
|---|---|---|
| DAR-P01 | Jurisdicción exacta de la **isla de Arven** | Es isla occidental de Norgard, ante Golfo de Veldora; **no se ha acreditado su administración formal**. No asignar Darovan por cercanía. |
| DAR-P02 | Señor/a actual de Darovan, herederos y casas menores | Decisión sustantiva del autor, D09/D10 |
| DAR-P03 | Origen del dominio y de la rivalidad Darovan/Galdren | Decisión del autor, D10 |
| DAR-P04 | Fronteras, cotas, distancias, nombres menores y escala cartográfica | No fijar sin fuentes/mapa métrico, D01/D02/D05 |
| DAR-P05 | Referencias en Treihord a una futura revisión militar frente a E5 Norgard ya activo | Revisar compatibilidad, no reescribir Treihord, D09 |
| DAR-P06 | Nombre Eshneva en manuscrito de trabajo | **Incidencia editorial no bloqueante**, no revivir el topónimo en gameplay |

No resolver ambigüedades creando canon propio.

## Seguimiento D01 — 15-10-2026 (sin nuevos decretos de canon)
- **DAR-P07:** el perfil visual de Veldora menciona un río detrás de la ciudad, sin identificar en esa ficha qué cauce ocupa exactamente esa relación. **No convertir una pista visual en identificación fluvial definitiva**. Revisar durante D02/D07 con mapa y fuente urbana aprobada.
- **DAR-P04 sigue abierto:** sin polígonos de frontera, alturas, collados, distancias, puentes ni escala geográfica pese al inventario cualitativo D01.
- **DAR-P01 sigue abierto:** Arven tiene geografía norgardiana pero no propietario Darovan confirmado.
- D01 deja **12 claves técnicas de unidades de estudio**, NO nuevos nombres/límites de regiones naturales ni canon publicado. La PR #15 requiere decisión expresa del autor para su merge; D02 no iniciada.

## Seguimiento D02 — 15-10-2026 (sin promulgar canon)
- **DAR-P01** continúa: Arven no adjudicada a Darovan.
- **DAR-P04** continúa: desconocidos fronteras, cotas, escala, altimetría y delimitación de cuencas.
- **DAR-P07** continúa: no atribuir nombre al curso que aparece detrás de Veldora en el perfil visual.
- **DAR-P08 (nuevo registro de UNKNOWN, NO hecho canónico):** posición de bifurcación Belara/Lhera respecto del tramo cercano a Treihord; nacimientos Veldora y Thalen; recorridos y divisorias exactos; orden/disposición cartográfica de los brazos terminales Thalen; caudales y permanencia. Documentar, no resolver por proximidad ni ficción.
- **D03 no iniciada:** puede preparar clima cualitativo cuando D02 esté fusionada, sin atribuir valores numéricos no acreditados.

## Seguimiento D03 — 15-10-2026 (NO canon nuevo)
- **DAR-P09 (nuevo, no bloqueante para documentación):** faltan valores y calendario de temperaturas, precipitaciones, viento, nieve y deshielo, límites climáticos, suelos y permeabilidad, niveles freáticos, recarga, erosión y riesgos verificados. NO atribuir climatología cuantitativa ni regímenes fluviales por analogía.
- **DAR-P01/P04/P07/P08 permanecen abiertos:** Arven sin dueño administrativo, altimetría y límites desconocidos, cauce visual detrás de Veldora por resolver, bifurcación Belara/Lhera y cabeceras/caudales por localizar. Ninguno se inventa en D03.
- **Protección ecológica:** Agujas sin asentamientos permanentes interiores; Pilares y Taramin son bosques únicos en sus respectivas transiciones; Syvaris bosquetes discontinuos, región cálida parcialmente seca y sectores resguardados verdes.
- **D03 en rama exclusiva:** documentos de Clima_local y JSON NO RUNTIME; pruebas estáticas JavaScript efectuadas, validador Python aportado sin ejecución en checkout completo; D04 NO iniciada.

## Seguimiento D04 — 15-10-2026 (no nuevo canon)
- **DAR-P10 (nuevo, aprobación de autor):** localización/identidad de explotaciones minerales concretas, eventual minería Darovan en Elyra, parcelas madereras, cultivos, ganado, nuevos propietarios y acuerdos económicos aún no acreditados. Una riqueza regional no prueba una mina individual.
- **DAR-P11 (nuevo, dependencias técnicas D05/D07/D08/D11):** itinerario y nodos del carbón Azurios→Treihord, existencias/capacidades, accesos Belara, métodos y quotas de pesca, almacenamiento y disponibilidad de agua; no inventar magnitudes ni tiempos.
- **DAR-P01/P04/P07/P08/P09:** Arven UNKNOWN, límites/cotas desconocidos, río visual Veldora no identificado, drenaje detallado y clima/suelos no medidos.
- **Evidencia:** PR #17 fusionada en `191bcd5`; D01–D03 Python MSI superados. D04 rama desde `df43be5`, PR #20 a revisión; 22 controles JS remotos OK y 16 negativos rechazados. Python D04 sobre checkout completo PENDIENTE MSI. No se ha modificado canon.

## D05 — Inventario de incertidumbres (21-10-2026, NO resolución de canon)
- **DAR-P01/P04/P07/P08/P09/P10/P11 continúan abiertos** sin alterar su contenido anterior. Arven sin atribución, sin escala, cruces, pasos ni puentes; río visual Veldora sin identificar; posiciones/caudales de D02 no medidos; riesgos D03 sin calendario; explotaciones no localizadas; itinerario carbón Azurios→Treihord UNKNOWN.
- Ninguna conexión marina Syvaris↔Veldora/Taramin, terrestre a Taramin, correo interurbano o transbordo nuevo resulta autorizada por un mapa o necesidad logística. Si el autor define alguna, actualizar fuente canónica primero y revalidar D05.
- En D05 la red física acreditada se limita a camino Veldora–Treihord, función logística con barcaza somera Belara y galería restringida La Vena. Los enlaces carbón Azurios y madera Pilares son suministros acreditados, no itinerarios.
- No se crea un nuevo identificador DAR-P sin decisión sustantiva; el cierre documental D05 conserva estas incógnitas.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.

**Estado de cuestiones pendientes tras la decisión de hoy:** DAR-P01 y DAR-P07 cerradas; DAR-P08 parcialmente resuelta; DAR-P04, DAR-P09, DAR-P10 y DAR-P11 siguen abiertas. La decisión del autor tiene prioridad sobre la tabla histórica que mostraba P01 y P07 abiertas.

## D06 — Protección de decisiones (21-10-2026)
- Se respetan los cierres **DAR-P01 (Arven Casa Darovan)** y **DAR-P07 (río Veldora identificado)** y la resolución parcial **DAR-P08 (Fhalion y cinco ríos, cuatro redes)** conforme al anexo aprobado por el autor.
- **No** se reabren los pendientes DAR-P04, P08 restante, P09, P10 y P11; permanecen UNKNOWN cartografía, suelo/agua, emplazamientos mineros, vías, navegabilidad, volúmenes y capacidad.
- **D06 no legisla canon:** los modelos, pesos 0–4, clases, edificios posibles, nombres de slots de prueba y semillas son únicamente propuestas técnicas. No hay emplazamientos específicos acreditados. El canon ya menciona aldeas en Arven/Pilares/Taramin, sin que D06 les asigne instancias.
- Treihord, Veldora, Taramin y Syvaris siguen fuera del generador. No hay población permanente en Bosque de las Agujas. Ninguna ruta D04/D05 de suministro se materializa como camino.
- Las decisiones sobre nuevos nombres, enclaves oficiales, fronteras, personas importantes e instituciones corresponden al autor y quedan fuera de D06.

## D07 — Tres decisiones conceptuales aprobadas (21-10-2026)
**No constituyen canon.** Los campos JSON etiquetados PROPOSAL_PENDING_AUTHOR no son decretos, barrios reales, emplazamientos ni prueba cartográfica. Treihord queda estrictamente excluida de rediseño.

| ID | Pregunta al autor | Alternativas para valorar | Recomendación técnica, NO aprobada |
|---|---|---|---|
| **DAR-D07-01 — RESUELTA: B** | ¿Cómo expresar la estructura urbana comercial de Veldora? | **B aprobada por el autor: varios sectores comerciales y artesanales orgánicos**, con puerto comercial como referencia | Aprobación de concepto general, no de trazado, nombres, límites ni nuevos edificios |
| **DAR-D07-02 — RESUELTA: A** | ¿Qué organización pesquera de Taramin es compatible con el interfluvio? | **A aprobada por el autor: una zona pesquera principal** | Solo criterio de concentración funcional; posición, navegación, acceso y muelles no aprobados |
| **DAR-D07-03 — RESUELTA: A** | ¿Qué grado de concentración urbana desea el autor en Syvaris? | **A aprobada por el autor: actividad urbana principal en torno a bahía resguardada** | Sin trazado, localizaciones de edificios o nuevos puertos en calas |

En los tres casos la aprobación de un criterio conceptual NO autoriza por sí sola edificios singulares, puentes, muelles nuevos, mapas, personajes, calles, nombres de barrios, instituciones o actividades no respaldadas. La materialización requiere alcance y fuentes definidos por el autor. Pendientes DAR-P02/P04/P05/P08 (parcial)/P09/P10/P11 sin modificación. DAR-P01 y P07 siguen resueltos y no se reabren. D08 y D11 son fases futuras.

### Resolución expresa DAR-D07-01 — Veldora
**Autor, 21/10/2026:** «Decisión 1 de D07: elijo la opción A para Veldora».
**APROBADO (solo concepto):** varios sectores comerciales, artesanales y residenciales, surgidos de crecimiento orgánico, sin reducir la ciudad a un único núcleo de comercio. Continúa vigente el canon preexistente de puerto principal, aduana exterior, almacenes, gremios, viviendas mixtas y zonas acomodadas alejadas de muelles.
**NO aprobado:** nomenclatura/número exacto de barrios, división urbana, calles, trazado, rutas, puentes, muelles nuevos, establecimientos singulares, personajes, habitantes, hogares ni servicios D08. En el índice operativo figura como `APPROVED_CONCEPT_ONLY`, sin `authorApprovedNewLayout`.
**Aún pendientes:** DAR-D07-02 (Taramin) y DAR-D07-03 (Syvaris). No actualizar `main` ni fusionar PR Draft sin autorización.

## Resolución del autor D07-01 — 21/10/2026
El autor elige B para Veldora: varios sectores comerciales orgánicos. Aprobación exclusivamente conceptual, sin calles, barrios, nuevos edificios, rutas ni cartografía definitiva. DAR-D07-02 Taramin y DAR-D07-03 Syvaris siguen pendientes.

## Resolución expresa DAR-D07-02 — Taramin (21/10/2026)
El autor declara: «Decisión 2 de D07: elijo la opción A para Taramin». Queda **APROBADA SOLO COMO CONCEPTO** una zona pesquera principal para concentrar la mayor parte de la faena y descarga. Sin determinación de su ubicación, número de muelles, navegación de los brazos del Thalen, puentes, caminos, edificios o población. No se crean instancias CoreRPG/Godot y no se transforma ninguna capa PROPOSAL en canon. Permanecen pendientes DAR-D07-03 Syvaris y las aprobaciones espaciales futuras. D08 no comenzada; PR #32 mantiene estado Draft.

## Resolución expresa DAR-D07-03 — Syvaris (21/10/2026)
El autor confirma: «Decisión 3 de D07: elijo la opción A para Syvaris». **APROBADO SOLO COMO CONCEPTO:** concentrar la actividad urbana principal, comercial, pesquera y naval de Syvaris alrededor de su bahía protegida. Se mantiene la presencia naval de Norgard (no armada de Darovan), las calas menores sin funciones portuarias nuevas, y la variedad climática de la isla. No se han aprobado barrios, callejero, nuevos puertos, infraestructura, rutas, medidas ni población. `DAR-D07-01 B / DAR-D07-02 A / DAR-D07-03 A` quedan cerradas a nivel conceptual; siguen abiertas las decisiones cartográficas y de detalle en su fase competente. D08 NO iniciada. PR #32 DRAFT, SIN FUSIONAR.

## Pendientes específicos D08 — 21/10/2026
- **DAR-D08-01 (PENDIENTE AUTOR):** rango poblacional o número aproximado de habitantes de Veldora, Taramin y Syvaris, por separado; también total territorial. No se proponen cifras canónicas ni se interpolan por tamaños.
- **DAR-D08-02 (PENDIENTE AUTOR):** rangos/patrones cuantitativos de tamaño de hogar y estructura demográfica urbana/rural. Hasta decisión: `UNKNOWN`.
- **DAR-D08-03 (CONDICIONAL):** nueva categoría social, institución singular o especialidad profesional que exceda Norgard; no hay ninguna aprobada ni creada en D08.
- Las opciones D07 Veldora B / Taramin A / Syvaris A están **APROBADO SOLO CONCEPTO**, sin convertirse en traza urbana; Treihord ≈32.000 y su canon intactos.
- No se traslada a Darovan el mínimo herrero de Treskal ni la posada casi generalizada de Valrik. Salud sin hospital universal, cuidado sin asistente automático.
- CoreRPG integra relaciones genéricas/población agregada (4.8), pero **no** implementa como API los contratos semánticos de hogar, EMP, salarios o stocks de Nimroel Core. D08 es exclusivamente estática.
Estas reservas no impiden validar datos documentales. Decisiones sustantivas de canon corresponden al autor, de una en una.

## DAR-D08-01 — Veldora, intervalo poblacional aprobado (22/10/2026)
**RESUELTA PARCIALMENTE por el autor:** Opción **B**, **29.000–35.000 habitantes**, intervalo de referencia **canónico aprobado** para Veldora. Aprobado expresamente, **no** extrapolado. Véase `../Auditorias/D08_RESOLUCION_DAR-D08-01_VELDORA_2026-10-22.md`.

Se conserva `UNKNOWN` el número exacto de Veldora; no convertir el punto medio ni una semilla en canon, ni derivar viviendas, empleo, aforos o stock. Sin cambios en Treihord ≈32.000 o la decisión urbana D07 Veldora B. **DAR-D08-01 sigue abierto exclusivamente para las siguientes localidades** Taramin/Syvaris y el total territorial, tratadas una a una. Todas las demás decisiones pendientes se mantienen.

PR #34 sigue **Draft y SIN FUSIONAR**. D08 no es integración runtime.

## DAR-D08-01 — Taramin, intervalo poblacional aprobado (22/10/2026)
**RESUELTA PARCIALMENTE por el autor:** Opción **B**, **14.000–20.000 habitantes**, intervalo demográfico de referencia canónico para Taramin. Aprobación expresa; acta `../Auditorias/D08_RESOLUCION_DAR-D08-01_TARAMIN_2026-10-22.md`.

No se fija censo exacto ni plazas de empleo, hogares, población latente, infraestructura o capacidades. Se preserva el carácter de ciudad pesquera mediana, la opción D07-A de zona pesquera principal **solo conceptual**, y su escala inferior a Treihord/Veldora. Quedan abiertas **Syvaris, el total territorial, las cifras puntuales** y DAR-D08-02/03. El registro de Veldora B 29.000–35.000 sigue vigente. PR #34 permanece Draft, sin fusionar; D09 no iniciada.

## DAR-D08-01 — Syvaris, intervalo de población urbana aprobado (22/10/2026)
**AUTOR APRUEBA OPCIÓN B:** **7.000–10.000 habitantes para la ciudad de Syvaris**, rango inclusivo. No corresponde al total de la isla; no hay valor exacto y la población rural/otros núcleos insulares y el total insular permanecen `UNKNOWN`. Acta `../Auditorias/D08_RESOLUCION_DAR-D08-01_SYVARIS_2026-10-22.md`.

Se conserva el canon D07-A de bahía protegida, pesca y presencia naval de Norgard (no armada Darovan); la ciudad es menor que Taramin. Treihord (~32.000), Veldora (29.000–35.000) y Taramin (14.000–20.000) intactas. **DAR-D08-01 queda resuelta para los tres intervalos urbanos pendientes**, pero aún falta decidir el total demográfico de Casa Darovan y se mantienen desconocidos los valores exactos y hogares. No crear casas, NPC, instalaciones o censos automáticos. PR #34 Draft, sin fusionar; D09–D11 sin iniciar.

## DAR-D08-01 — Total territorial Casa Darovan, opción B (22/10/2026)
**APROBADO POR EL AUTOR:** **300.000–450.000 habitantes** para el **territorio completo** de Casa Darovan. Fuente `../Auditorias/D08_RESOLUCION_DAR-D08-01_TOTAL_DAROVAN_2026-10-22.md`.

La aprobación resuelve la parte de **intervalos territoriales y urbanos DAR-D08-01**: Treihord ≈32.000, Veldora 29.000–35.000, Taramin 14.000–20.000, Syvaris ciudad 7.000–10.000, Darovan total 300.000–450.000. **Censos exactos, resto y total insular Syvaris, distribución urbano/rural, número y habitantes de asentamientos ordinarios permanecen UNKNOWN.** Las cuatro ciudades son subconjuntos del territorio, no población adicional al total. Ninguna cifra crea pueblos, hogares, NPC, infraestructuras o actividad CoreRPG. `DAR-D08-02` continúa pendiente de decisiones domésticas una por una. PR #34 Draft, sin fusionar. D09–D11 no iniciadas.

## DAR-D08-02 — Hogares urbanos, intervalo de promedio aprobado (22/10/2026)
**AUTOR APRUEBA OPCIÓN B:** **3–5 personas por hogar urbano, de media** en Casa Darovan. Documento fuente `../Auditorias/D08_RESOLUCION_DAR-D08-02_HOGARES_URBANOS_2026-10-22.md`. Aprobado **como rango de la media urbana**, sin imponer esos tamaños a todos los hogares ni fijar media exacta de cuatro personas.

**Siguen pendientes:** rango medio de hogares rurales, promedio territorial global, cantidades exactas de hogares/viviendas/habitantes, distribución por tamaños, demografía por edades y proporciones urbano/rurales. D08 no crea edificios ni hogares CoreRPG y mantiene Norgard Defaults. PR #34 Draft sin fusionar; D09–D11 sin iniciar.

## Lote final de decisiones autorales D08 — 22/10/2026
El autor aprueba conjuntamente: **hogares rurales B 4–6 personas por hogar como media**, **1B edades 30 % (0–17), 60 % (18–59), 10 % (60+)**, **2C sin porcentajes diferenciados urbano/rurales por edad (NO equivalencia forzada)**, **3C 35–45 % de población urbana y 55–65 % rural como porcentajes complementarios del territorio**, y **4A sin nuevas categorías sociales, instituciones singulares ni especialidades profesionales en D08**, sin bloquear propuestas futuras.

Acta vinculante: `../Auditorias/D08_RESOLUCION_LOTE_FINAL_2026-10-22.md`. La población urbana de las cuatro ciudades conocidas **no cubre por sí sola el rango urbano territorial**: queda `UNKNOWN` la cobertura de otras localidades, sin crearlas o atribuirles censos. Siguen sin aprobarse censos puntuales, cantidades de hogares/viviendas, nuevos asentamientos o NPC, desglose de edades por ciudad/campo, normas sobre familias adicionales o ejecución CoreRPG/Godot.

**DAR-D08-01** resuelto a nivel de rangos territoriales/urbanos; **DAR-D08-02** resuelto para promedios urbanos/rurales y proporciones agregadas; **DAR-D08-03** resuelto con 4A «ninguna nueva en D08». Pendientes operativos solo para futura materialización y autoría de localidades/cifras exactas, no bloquean el cierre documental. PR #34 queda Draft y sin fusionar.


## D09 — Aprobación de lote único y límites (22/10/2026)
**Autor aprueba todas las recomendaciones (17 decisiones) y autoriza implementación documental en rama propia.**
- **Gobierno:** G01B centralización Treihord + delegaciones funcionales; G02B administración local que consulta gremios/comerciantes/representantes existentes sin órganos nuevos; G03B rural/Arven subordinado sin divisiones inventadas; G04B Justicia del Rey ordinaria en las cuatro ciudades e itinerante en localidades menores, sin nuevas sedes; G05C confirmante preciso de pena capital Darovan **UNKNOWN**, obligación legal existente vigente; G06A Casas menores concretas/existencia **UNKNOWN**.
- **Fiscalidad:** F01B registros locales y conciliación central con Corona; F02C aduana exterior Veldora control real con apoyo Darovan; F03B registros de ensaye/producción Darovan sujetos a contraste real; F04C plazo y cuota de remesa **UNKNOWN**. No impuestos, tarifas, aduanas internas ni ceca nuevas.
- **Defensa:** D01A Guardia de Casa Bóveda/Crisol/Vena/escoltas; D02C guardias urbanas locales coordinadas; D03C fuerza profesional equilibrada según amenazas y recursos; D04A seguridad terrestre Darovan y mando Armada exclusivamente real en Syvaris.
- **Seguridad:** S01B patrullas adaptables sin itinerarios inventados; S02C escolta privada/territorial/institucional según título/risgo y recursos; S03B autorización y custodia conjuntas Crisol–Bóveda en La Vena.
**Nuevos datos sin autorización:** Lord/Lady/herederos, Casas menores, juez/confirmante capital, porcentajes/calendario, guardias y guarniciones numéricas, edificios, rutas o instituciones individuales. No extrapolar Valrik. Registro canónico D00–D08 intacto. JSON `darovan_d09_governance_security_v0.1.json` referencia estos conceptos y sigue `planning_reference_not_runtime`.

## D10 — Aprobación cultural conjunta (23/10/2026)
**Fuente: autor en Darovan 11, «Apruebo todas tus recomendaciones».** D10-01B identidad diversa; 02B desigualdad no casteada y movilidad posible; 03B cultura de oficio sin psicología obligatoria; 04B rivalidad Galdren contextual; 05B Treihord plural dentro de sus ocho barrios; 06B Veldora mercantil diversa; 07B Taramin pesquera sin exclusividad; 08B Syvaris insular sin aislamiento forzado; **09C Arven cultura UNKNOWN**; 10B rural condicionado por asentamientos realmente acreditados; 11B cocina solo Norgard existente; 12B atuendo y objetos por recursos/contexto; 13B feria de metales preexistente pero nombre/fecha UNKNOWN; 14B funeral Norgard sin rito nuevo; 15B redes de relaciones personales causales; 16B nombres Norgard y registro/contexto sin dialecto inventado; 17B PERS individual inalterada. No se autoriza fiesta, Casa menor, institución, privilegio legal, religión, edificio, NPC, asentamiento, evento ni World State. Se mantiene el origen histórico Galdren, nombre/fechas feria, población Arven, personajes y tradiciones nuevas en UNKNOWN.

**Estado:** D10 en rama exclusiva, PR Draft y CI por verificar; no fusionar sin aprobación. D11/D12 NO iniciadas.

## D11 — Decisiones técnicas no canónicas (23/10/2026)
- DAR-D11-T01: usar CoreRPG Content Contract 0.1.0 solo para sobres de identidad de Darovan y cuatro ciudades; sidecar Nimroel separado para propiedades y trazabilidad, sin extensión pública de Core.
- DAR-D11-T02: once bloqueos de procedencia D00–D10 por SHA de blob; futuros cambios obligan a revisión y nueva versión, sin reescribir fases históricas.
- DAR-D11-T03: ocho escenarios TEST_ONLY son especificaciones; ninguno es canon ni prueba de ejecución de reglas de dominio.
- DAR-D11-T04: bloqueos de canon se conservan: Arven cultura UNKNOWN, geometrías, minas y recursos exactos pendientes; la Casa no crea armada ni fiscalidad interior nueva.
- DAR-D11-T05: no se modifica CoreRPG, GDExtension o Host; dependencias CoreRPG se documentan en petición técnica separada. Revisión del autor obligatoria antes de fusionar PR D11; D12 no iniciada.

## Resolución autoral de altitud — 25 de octubre de 2026

**DAR-DP13-ALT-01 (APROBADA):** Montes Valkram, **opción A**: cordillera muy alta. Rango orientativo de **3.600–4.200 m para las grandes cumbres**, no para la totalidad del macizo ni cada montaña individual. Es una escala de diseño expresamente aprobada por el autor; las cotas de valles, cumbres secundarias, pasos, cabeceras y localidades permanecen sin definir.

**DAR-DP13-ALT-02 (APROBADA):** una cumbre excepcional situada en el **sector norte de Valkram**, representada en el mapa del autor **entre la N y la O del rótulo «NORGARD»**, es **la mayor elevación de todo Norgard** y alcanza **aproximadamente 4.200 metros sobre el nivel del mar**. Su nombre propio, coordenadas, laderas exactas, jurisdicción precisa, extensión nival y existencia de glaciares permanecen **UNKNOWN**. «Cumbre septentrional de Valkram» es una descripción, NO un topónimo nuevo.

**Compatibilidad transversal pendiente:** `Geografía/montanas.md` define los Montes Azurios como más altos, anchos y abruptos en términos generales. La elección más reciente del autor fija una **excepción puntual de altura máxima absoluta** para Valkram, compatible con un sistema Azurios globalmente más elevado/abrupto, pero se requiere armonización editorial futura a escala de Norgard para eliminar ambigüedades. **No se cambia la ficha superior en D.P13.**

**Registro operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json`. Esta nueva decisión autoral no contradice la protección del perfil antiguo `darovan_dp13_physical_profiles_v0.1.json`, cuyos campos nulos corresponden a zonas de estudio sin cota única, no a las nuevas anclas individuales aprobadas.


## Nuevas decisiones autorales de D.P13 — 25/10/2026

**DAR-DP13-ALT-03 — APROBADA:** nombre oficial **«la Viuda»** (grafía exacta facilitada por el autor) para la cumbre excepcional de **~4.200 m**, en el norte de los Montes Valkram, la más alta de Norgard, identificada visualmente entre las letras N y O del título del mapa. El nombre deja de estar UNKNOWN; etimología, coordenadas, glaciar y territorio político preciso siguen UNKNOWN. Tiene prioridad sobre anotaciones anteriores de nombre pendiente.

**DAR-DP13-ALT-04 — APROBADA:** **opción A** para las Montañas Elyra: cumbres más altas de **hasta aproximadamente 2.600 m**. No implica nombrar ni localizar una cumbre concreta, ni fijar toda la altimetría de la península de Taramin. Se conserva el carácter de Elyra como cordillera menor que Valkram, su posición y el alcance no runtime de D.P13.

**Contratos:** `D.P13/12_altitud_valkram_autorizada.md`, `D.P13/13_altitud_elyra_autorizada.md` y JSON de decisión autoral correspondientes, con nuevas pruebas negativas. Las referencias previas a topónimo o alturas UNKNOWN son actas históricas anteriores y quedan resueltas en estos dos puntos, sin modificar D01–D12.


## Decisión autoral DAR-DP13-SNOW-01 — Neveros permanentes en la Viuda (25/10/2026)

**APROBADA — opción B.** En **la Viuda**, cumbre septentrional de los Montes Valkram (~4.200 m), **existen acumulaciones de nieve (neveros) que sobreviven al verano en sectores altos y protegidos**. Se confirma la persistencia localizada de nieve de un año a otro; **no** se afirma que todo el pico permanezca nevado ni que exista un límite altitudinal de nieve uniforme para el conjunto de Valkram.

**No se han aprobado glaciares** con esta decisión. Su existencia real sigue **UNKNOWN**, no debe darse por demostrada ni descartada definitivamente sin otra decisión autoral. No se fijan tamaños, volúmenes, espesores, cotas de aparición, localización métrica de neveros, fechas de deshielo ni caudales. La aportación hídrica por fusión es una **posibilidad causal derivada**, no un nuevo nacimiento de río ni una cuantificación.

**Fuente autoral:** elección expresa de opción B a la pregunta 3 de D.P13, 25 de octubre de 2026.

**Registro estructurado:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `worldHighestSummit.snowPersistence` y `snowPersistenceDetail`. Referencias anteriores a «nieve permanente UNKNOWN» en registros históricos quedan parcialmente superadas **solo para la Viuda**; el régimen del resto de Valkram/Elyra permanece por definir.


## DAR-DP13-PASS-01 — Altitudes orientativas de los principales pasos de Valkram (25/10/2026)

**Decisión expresa del autor: OPCIÓN B (APROBADA).** Los principales **pasos naturales** practicables de los Montes Valkram tendrán un **rango de referencia aproximado de 1.400 a 2.200 metros sobre el nivel del mar**.

Este intervalo describe la **categoría general de los pasos principales**, no la cota de todos los collados, ni una obligación de distribuirlos uniformemente en esas alturas. Pueden existir relieves menores o collados más altos si el canon y la futura topografía lo permiten; la decisión **no autoriza** afirmar nombres, cantidad, emplazamientos, rutas, pasos abiertos durante todo el año, infraestructuras, puentes ni caminos nuevos.

**Comportamiento plausible (DERIVED_CONDITIONAL, no hecho local decretado):** a esas alturas, algunos pasos pueden sufrir nieve, hielo, viento o dificultades de circulación durante episodios fríos. No se aprueban cierres regulares, fechas, duraciones ni cotas de nieve de pasos individuales. **La Viuda (≈4.200 m) y sus neveros de verano permanecen intactos**.

**Dato operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json` → `principalNaturalPasses`. Esta nueva autorización sustituye el UNKNOWN anterior referido al **rango general de pasos principales**, pero no resuelve la altitud individual de ningún paso ni la cartografía métrica. Fuentes: aprobación expresa del autor en conversación D.P13, 25/10/2026, y canon de `Geografía/montanas.md`.


## DAR-DP13-CITY-ALT-01 — Altitud de Treihord (25/10/2026)

**APROBADA — opción A:** banda de referencia de **150–350 m s. n. m.** para el emplazamiento urbano general de Treihord. No se fija una altitud exacta de la ciudad ni de sus ocho barrios, muelles o plazas. Tampoco cota del Belara, pendientes, accesos, nuevos puentes o navegabilidad. La ciudad sigue **junto al Belara, sin que el río la atraviese**, y su puerto continúa siendo exclusivamente industrial para barcazas de poco calado. Este rango es dato de **autor**, no altimetría métrica de un mapa.

Documento: `D.P13/14_altitud_treihord_autorizada.md`; contrato: `Datos operativos/darovan_dp13_treihord_elevation_authorial_v0.1.json`. Uso para D.P16/D.P18 únicamente como referencia, sin iniciar esas fases.


## DAR-DP13-CITY-ALT-02 — Altitud urbana orientativa de Veldora (25/10/2026)

**OPCIÓN B APROBADA POR EL AUTOR:** el emplazamiento general de **Veldora** tiene un rango altitudinal aproximado de **0–60 m s. n. m.**, que admite una franja litoral baja y zonas interiores más elevadas sin fijar cotas individuales. La ciudad permanece como **principal puerto comercial marítimo de Darovan en el Golfo de Veldora**.

No se asignan alturas a muelles, calles, barrios, mar, mareas, lechos o desembocaduras fluviales. Los ríos **Lhera** y **Veldora** conservan su independencia; la identidad del cauce mostrado tras la ciudad en el perfil visual sigue **UNKNOWN (DAR-P07)**. El dato de autor no es un levantamiento topográfico ni genera infraestructura, poblaciones, rutas o WorldState.

Documento: `D.P13/15_altitud_veldora_autorizada.md`. JSON: `Datos operativos/darovan_dp13_veldora_elevation_authorial_v0.1.json`. Decisión destinada a D.P16/D.P18 sin iniciarlas.


## Rectificación de la banda altitudinal de Veldora — 25/10/2026

La decisión autoral **DAR-DP13-CITY-ALT-02** es **opción A, de 0–60 m** para el núcleo urbano principal. La versión que anotaba **opción B (0–150 m)** fue una discrepancia de registro y queda expresamente invalidada, sin modificar el canon hidrológico ni las fases previas. El dato autoral es aproximado, no cartografía métrica.

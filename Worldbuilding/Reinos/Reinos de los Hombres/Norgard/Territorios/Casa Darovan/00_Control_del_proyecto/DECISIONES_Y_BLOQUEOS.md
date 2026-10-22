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
**Autor, 21/10/2026:** «Decisión 1 de D07: elijo la opción B para Veldora».
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

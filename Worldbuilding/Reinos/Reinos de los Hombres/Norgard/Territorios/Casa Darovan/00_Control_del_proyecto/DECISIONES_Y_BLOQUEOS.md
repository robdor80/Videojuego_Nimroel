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

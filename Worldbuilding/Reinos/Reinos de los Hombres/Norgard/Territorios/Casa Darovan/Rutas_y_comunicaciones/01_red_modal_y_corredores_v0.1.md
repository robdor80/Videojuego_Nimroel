# DAROVAN D05 — Red modal y corredores v0.1
**Estado:** planificación y grafo cualitativos, NO CANON NUEVO / NO RUNTIME. Fecha: 21-10-2026.

## Alcance y autoridad
Jerarquía: Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State. Las etiquetas AUTHORED (afirmación expresa), DERIVED (relación causal condicionada), PROPOSAL (estructura técnica) y UNKNOWN (falta de evidencia) clasifican afirmaciones concretas, nunca autorizan por sí mismas una ruta nueva. El JSON D05 es un índice reutilizable en D11, **no** una red transitable ni un grafo con distancias.

## Tres conexiones físicas realmente respaldadas (extremos conceptuales, no trazados)
| ID técnico | Extremos y modo | Evidencia AUTHORED | Límite |
|---|---|---|---|
| d05_road_veldora_treihord | Veldora ↔ Treihord, camino principal | Norgard/Geografía/bosques.md, Bosque de la Linde | Bosque **junto** al camino, sin afirmar paso por dentro, longitud, sentido de carros, puentes o hitos |
| d05_belara_shallow_haul | Puntos de carga fluvial SIN localizar → puerto industrial Treihord, barcaza somera | Treihord.md §§6–7 y rios_y_lagos.md §3 | Sí existe uso fluvial industrial para cargas, NO un tramo geométrico o caudal/capacidad anual |
| d05_vena_restricted | El Crisol ↔ La Bóveda del Grifo, galería bajo custodia | Treihord.md §10 | Conexión privada de máximo valor/documentos; prohibido usarla como vía pública, atajo general o red comercial |

Las aristas entre extremos son **simbólicas**: una arista Veldora–Treihord NO declara carretera recta, ruta libre de obstáculos, longitud o comunicación sin escalas. El cargadero es una función canónica sin nombre ni coordenada; su clave de grafo no funda un embarcadero nuevo.

## Nodos
Se registran las cuatro ciudades manuales, cuatro instalaciones portuarias documentadas, funciones económicas ya acreditadas (minas de Valkram, carga del Belara, carbón Azurios, madera Pilares, industria Treihord), Crisol/Bóveda y dos referencias **NO usables como paradas**: la Linde y Arven. Todos los IDs d05_* son técnicos, no topónimos; ninguna posición espacial ni delimitación.

## Hidrología y conectividad NO confundidas
Belara junto a Treihord, no dentro del casco urbano; barcazas solo de poco calado allí. Lhera se separa de Belara; su navegabilidad es UNKNOWN. Veldora (río) independiente de ambos, aunque comparta golfo con Lhera. El Thalen es un único río con **dos brazos terminales** y Taramin entre ellos; NO hay prueba de canales navegables, puentes, vados ni puerto fluvial en esos brazos. El grafo topológico D02 describe agua, NO navegación de barcos o viajeros.

## Cuatro ciudades y límites de titularidad
Treihord, Veldora, Taramin y Syvaris son las cuatro ciudades canónicas Darovan, no localidades procedurales. Syvaris es insular con puerto seguro en su bahía principal; **una salida de la isla requerirá navegación**, pero no hay itinerario Syvaris↔Veldora/Taramin ni frecuencia/duración acreditados. Arven está frente al Golfo de Veldora, pero su administración UNKNOWN (DAR-P01): sin arista Darovan ni ruta deducida por proximidad. Karsath no es ciudad Darovan.

## Posibilidades de red que NO son conexiones creadas
Carreteras a Taramin, vías de enlace peninsular, pasos de montaña, transbordos concretos Belara/Lhera, cabotaje interpuertos, travesías Syvaris–continente y enlaces Arven solo se conservan como preguntas UNKNOWN o necesidades futuras. No se materializan como aristas PROPOSAL porque una visualización podría interpretarlas erróneamente como rutas existentes.

**Fuentes:** Norgard originales rios_y_lagos.md; bosques.md; mares_y_costas.md; Treihord.md; Grandes Casas; D01/D02/D03/D04; contratos de navegación universal y Norgard E7. Se conservan rutas completas en el JSON D05.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.

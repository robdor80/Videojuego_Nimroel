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

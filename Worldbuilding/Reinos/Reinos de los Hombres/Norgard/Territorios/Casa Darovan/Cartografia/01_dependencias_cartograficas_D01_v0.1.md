# DAROVAN D01 — Dependencias cartográficas y control de capas v0.1

**Estado:** propuesta de inventario de capas, no mapa de juego ni documento canónico.

## Fuentes y límites
1. El recorte de estudio documentado en Geografia_local/00_inventario_y_lectura_del_mapa_v0.1.md y el mapa general son **referencias visuales**: no equivalen a un GIS. La línea roja del recorte D00 carece de valor de frontera jurídica certificada.
2. Geografía, ríos, bosques, montañas y mares de Norgard tienen autoridad **textual**. La imagen sirve para orientar preguntas, no para corregir la hidrografía original ni adjudicar Arven.
3. Los perfiles visuales regionales y de ciudades sirven para representar atmósferas (ej. Veldora con relieve interior, Syvaris más seca en el centro/norte), **no** para derivar coordenadas, puertos, cumbres o cursos exactos.
4. Treihord conserva íntegro su diseño base en Norgard/Ciudades/Casa Darovan/Treihord.md; sin extrapolar un plano a partir de frases de barrios.

## Capas propuestas, sin geometría materializada
| Capa | Tipo | Fuente requerida | Estado D01 |
|---|---|---|---|
| physical_relief_anchors | montes, costa, península e islas | textos geográficos canónicos | inventario cualitativo |
| physical_transitions | laderas y ecotonos posibles | relieve local verificable + canon | DERIVED pendiente |
| watercourse_anchors | identidades, nacimientos/bocas canónicos | rios_y_lagos.md | anclas sin grafo |
| drainage_network | cuencas, afluentes y divisorias | macrorelieve/microrelieve + Core | NO D01: D02 |
| land_cover | masas forestales y transición Taramin/Syvaris | bosques.md, regiones_naturales.md | categorías sin polígonos |
| coastal_segments | golfos, acantilados, calas y costa | mares_y_costas.md, mapa validado | sin vértices |
| administrative_overlay | jurisdicciones confirmadas | Grandes Casas + autor | solo ciudades/Syvaris; Arven UNKNOWN |
| roads_and_access | camino Veldora–Treihord, otros por definir | fuentes de rutas + relieve | relación verbal, sin tracks |

## Validación previa a un plano métrico
- Confirmación autoral de ámbito Darovan continental, situación administrativa de Arven y puntos de borde sensible.
- Determinar cuál es la versión cartográfica aprobada y su sistema de escala/proyección/referencia; **no** transferir automáticamente unidades reales del dibujo.
- Resolver disonancias mapa/texto por revisión humana, sin deformar la red fluvial para encajar trazos decorativos.
- Conseguir o diseñar macrorelieve coherente; ejecutar después análisis de pendientes, divisorias, cuencas y costas.
- Revalidar que los cuatro centros manuales se conservan, Karsath queda fuera, Belara no cruza Treihord, Taramin mantiene los dos brazos Thalen y Syvaris no se homogeneiza.

## Pendientes reservados
D02: agua, cuencas, manantiales e inundación. D03: biomas/microclimas. D05: caminos, cruces y tiempos. D07: mapa urbano. D11: integración y persistencia runtime. La salida cartográfica D01 es un **contrato de precauciones**, nunca un SVG/GeoJSON georreferenciado ficticio.

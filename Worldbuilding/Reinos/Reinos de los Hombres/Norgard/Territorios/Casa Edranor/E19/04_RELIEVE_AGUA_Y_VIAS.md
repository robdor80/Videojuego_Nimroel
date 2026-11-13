# E19 — Altimetría, cuencas, drenaje y red física

## Heightfield 2D
Al crear el DEM real, registrar fuente, raster de alturas, referencia vertical, unidad, resolución, interpolación, tratamiento NoData, corrección de sumideros y fronteras de teselas. Se rechaza cualquier DEM «estimado» solo por el sombreado decorativo del mapa. Las bandas en metros de E13 son escenarios **no medidos**; no son cotas en el espacio real.

Control T01: para toda pareja de tiles adyacentes de un mismo LOD comparar borde compartido tras transformación con tolerancia documentada; no aceptar grietas ni offsets. Separar elevación visual de colisión/navegación.

## Cuencas y agua
Norgard sí documenta río Lurien (Valkram oriental → centro → Lago Antela → Hallheim → Golfo de Norgard) y Lago Antela al sur relativo de Karsath. **No hay segmentos locales acreditados en Edranor**. Ni un cauce dibujado ni un lago ilustrado prueban la delimitación de cuenca o derecho de captación.

Cuando exista DEM y polilíneas revisadas:
- Cada celda fluyente tiene a lo sumo un receptor salvo modelo explícito de bifurcación, y su altura disminuye aguas abajo en el supuesto gravitatorio.
- Comprobar ausencia de ciclos, sumideros interiores no explicados, continuidad de curso y pertenencia de receptor.
- Separar derechos de agua, saneamiento y potabilidad de la mera presencia física de una línea azul.
- Los ríos sin nombre no recibirán hidrónimo nuevo sin ratificación.

## Caminos y accesos
La E16 solo describe **preguntas de accesibilidad**, con grafo físico Gp vacío. El mapa base no certifica pasos, puentes, caminos, postas, muelles ni tiempos de trayecto. No convertir la proximidad Karsath–Lumina–Dorth en ruta.

Para habilitar una arista exigir: traza material georreferenciada, pendientes, superficies/estacionalidad, puentes o vados autorizados, propiedad/servidumbres y continuidad. Mantener dos grafos separados: necesidades de movilidad (E16) y red física (E19/E28).

## Estado en este corte
DEM=null, cuencas=[], hidrografía local=[], aristas físicas=[]; EDD-03 y EDD-07 OPEN. Las pruebas numéricas del validador son **fixtures sintéticos**, sin producir mundo.
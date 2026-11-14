# E19 — Calco vectorial del mapa autoral con contorno Edranor
**Fecha:** 14/11/2026 · **Naturaleza:** CARTOGRAFÍA VISUAL 2D DE AUTOR; **NO** topografía ni fronteras métricas.

## Insumo y procedencia
El autor ha aportado `nimroel_Edranor.jpg` (2048 × 1024; SHA-256 `b5341bb608538aa9bc07c8afae56b9c7264af9f9a8c29fee82e14e63863c303f`). La imagen muestra la misma composición del mapa maestro `Worldbuilding/Nimroel.jpg` (4096 × 2048), con el contorno principal rojo de Edranor y cinco trazos diagonales interiores.

El mapa anotado original está en el **adjunto de la conversación**, no se afirma archivado en GitHub. Para preservación reproducible en el repositorio se incluye su **calco vectorial** (con checksum del insumo y método de extracción). El fichero de líneas es una derivación, no los bytes del JPG.

## Conversión a Godot 2D
- Referencia de marcado: `2048 × 1024 px`, origen superior izquierdo.
- Transformación exacta entre **espacios de píxel**: al mapa maestro `4096 × 2048`, multiplicar `x * 2` y `y * 2`; inversa `x / 2`, `y / 2`.
- Esta operación **NO** calibra distancias reales. `metersPerPixel=null`, `geographicCRS=null`. El rótulo del mapa «400 MILLAS» no se aplica sin una decisión explícita de escala de juego e incertidumbre.
- `author_trace_overlay_2048.svg`: SVG transparente con el contorno principal y rayado. Mostrarlo en Godot en la misma proyección raster, sin inferir colisiones, propiedad, agua, biomas ni nodos.
- `author_trace_raster_2048_v0.1.json`: coordenadas de la curva roja, procedencia, reglas de excepciones y deudas materiales.

## Interpretación del norte
Las dos ramas del trazo rojo llegan hasta el **borde superior visible de la imagen**, sin dibujar una frontera horizontal. El autor ya ha ratificado que Edranor prosigue hacia el extremo norte de Norgard, **sin frontera política interior**. No cerrar el área con una línea artificial de (1086,0) a (1571,0): ese segmento atraviesa mar/dibujo y es solo límite del visor, **no tierra ni límite de Casa**. Por esta razón **no se publica un polígono administrativo canónico ni se aplica relleno territorial**. Se conserva una línea de límite de diseño con 21 puntos de control y cinco trazos diagonales que son **rayado indicativo**, no fronteras.

## Fronteras y excepciones
Al oeste la vertiente oriental de Valkram (Darovan al otro lado); al este la occidental de Azurios; al sur interfaz aproximada con Aethros, próxima a cauce, **sin identificar cauce ni margen como prueba topológica**. Dorth, Lumina y Karsath permanecen Edranor. Hallheim, capital de Norgard y sede de Aethros, se mantiene fuera. Rodas está dentro del contexto geográfico Edranor pero su **administración, justicia, fiscalidad, seguridad y mando militar** dependen íntegramente de Corona/Aethros; solo esta puede convocar los berserkers.

## Auditoría visual
Calco automatizado desde componente rojo continuo, esqueletización y simplificación Douglas–Peucker con tolerancia aproximada de 4 px. Los cinco componentes de rayado se conservan separados. Comparación contra mapa maestro redimensionado: mediana de diferencia absoluta por canal de 2 niveles fuera de los trazos rojos; más del 96 % de esos píxeles tienen diferencia máxima por canal inferior a 15 (diferencias normales de recompresión JPEG). La transformación `×2` es reversible dentro de espacios raster. **La fiabilidad del trazo no implica precisión de costas, cauces, cordales o dimensiones físicas.**

## Puertas de completitud
- **Disponible hoy:** trazo visual vectorial de autor, atlas 2D y registro de autoridad, usable como guía gráfica en el mapa 2D; no requiere más dibujos del autor para esta función.
- **EDD-01:** norte semántico ratificado y trazos oeste/sur/este reproducibles; falta costa/divisoria norte y geometría física de los demás bordes para certificar polígono de jurisdicción.
- **EDD-02:** coordenadas raster calibradas en proporción `2:1` con la imagen maestra; escala métrica física sigue abierta.
- **EDD-03:** DEM y aguas físicas no derivables de dibujo ilustrativo.
- **EDD-07:** traza de caminos y derechos de paso inexistentes en fuente.
- **E28:** futura integración real de Godot y CoreRPG, no probada por este SVG o los JSON.

Las monografías E20–E24 **pueden usar la cartografía visual** para regiones y orientaciones, sin declarar censo, sitios, rutas o edificios materializados.

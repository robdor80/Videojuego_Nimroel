# E19 — Perímetro, anclas y excepciones de soberanía

## Semántica territorial
Orden de autoridad: Nimroel Core → Norgard Defaults → Casa Edranor (delegación) → localidad → World State, **salvo competencias regias expresas de Corona Aethros**. La cartografía física puede cruzar fronteras administrativas; no se ha verificado una geometría vectorial para Edranor.

| Ancla | Lectura confirmada | Autoridad | Punto real |
|---|---|---|---|
| Karsath | oeste relativo de Lumina y Dorth; vino selecto; al norte de Antela | Casa Edranor | UNKNOWN |
| Lumina | meseta de Bosque Alto; blancos y feria anual | Casa Edranor | UNKNOWN |
| Dorth | sede; tintos; borde forestal Azurios | Casa Edranor | UNKNOWN |
| Rodas | **ALDEA** dentro del territorio geográfico de Edranor; X en recorte | **Casa Regente Aethros**: TODO bajo Corona, administración civil, justicia, impuestos, seguridad, mando y convocatoria berserker ratificados | UNKNOWN |
| Hallheim | fuera del perímetro Edranor aunque roce dibujo | Corona Aethros | UNKNOWN |

No hay derecho de tala automática en Bosque Alto, ni propiedad íntegra de Azurios o Bosque Real, ni muelle urbano certificado en Karsath, ni aduana interior de Casa. El **Paso de Vareth** no se ubica aquí.

## Ratificación del autor (14/11/2026)
La delimitación **semántica** ha quedado ratificada: sin frontera política intermedia al norte, hasta el norte geográfico de Norgard; vertiente **oriental de Valkram** para Edranor al oeste; vertiente **occidental de Azurios** para Edranor al este; sur aproximadamente por el curso fluvial indicado en rojo frente a Aethros. Hallheim es la capital de Norgard y sede de la Casa Aethros **fuera** de Edranor.

**Rodas está territorialmente en Edranor.** El autor precisa que por «control» de Aethros se refiere en particular al derecho de **convocar a los berserkers**; no se trata de una frontera territorial nueva. Una ratificación autoral adicional confirma **todas** las competencias de la Corona: administración civil, justicia, impuestos, seguridad y poder militar, incluida la convocatoria berserker. Por ello se mantienen y refuerzan los contratos E07/E09, sin atribuir competencias a Edranor. La pequeña importancia recaudatoria de Rodas es cualitativa; no se fija cuantía ni censo. Fuente detallada: [Ratificación autoral](07_RATIFICACION_AUTORAL_LIMITES_RODAS.md).

## Geometría pendiente: algoritmo de aceptación
1. Reproducir mapa autoral íntegro o acta con vértices ratificados, conservar hash y sistema de imagen.
2. Capturar borde rojo completo y sus extremos, sin interpolar el norte; identificar fuente de cada vértice.
3. Mantener separación entre contorno del territorio administrado y **jurisdicción de Rodas**; el régimen de Rodas es una excepción legal, no automáticamente un agujero geográfico en el polígono. Para un agujero administrativo hace falta delimitación específica.
4. Validar cierre explícito y una única orientación elegida; rechazar auto-intersecciones, segmentos de longitud cero, anillos triviales, agujeros exteriores y solapes de jurisdicción no autorizados. No convertir color de píxel en propiedad.
5. Contrastar Hallheim fuera y anclas internas como **hechos jurídicos/documentales**; el test point-in-polygon solo es válido tras ratificar sus posiciones y geometría.

## Unidades heredadas
U1 interfaz occidental Valkram; U2 Karsath interior; U3 Lumina/Bosque Alto; U4 franja vinícola discontinua; U5 Dorth/Azurios occidental; U6 transición fría; U7 extremo septentrional **NON_EVALUABLE**. Son unidades de estudio, no siete polígonos ni nuevas divisiones legales.

## Puerta EDD-01
Permanece **OPEN**. Prohibido publicar `FeatureCollection` oficial de parcelas, fronteras, rutas o biomas como si fueran localizaciones reales antes de la fuente material.
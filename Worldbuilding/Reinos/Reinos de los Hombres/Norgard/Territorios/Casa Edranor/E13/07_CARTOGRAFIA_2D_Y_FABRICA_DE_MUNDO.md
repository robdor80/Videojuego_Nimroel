# E13 — Protocolo espacial 2D y fábrica reutilizable
**Documento de contrato editorial; no módulo Godot 4.7.2 ni CoreRPG ejecutado.**

## Fuente visual y honestidad geométrica
El recorte E00 con línea roja y X azul tiene **cierre septentrional ausente**. El mapa general «Nimroel» contiene una barra ilustrada de 400 millas; su uso como escala de este recorte requeriría comprobar el sistema de proyección, el recorte, distorsiones, puntos de control y equivalencia de distancias. En E13: CRS=null, transformación=null, pixelPerMeter=null, vertices=[], polilíneas=[], DEM=null. El SVG de E13 es exclusivamente **esquema topológico**, no referencia de coordenadas del mundo.

## Capas propuestas para E19
L0 mapa fuente inmutable y metadatos de licencia/autor; L1 perímetro jurisdiccional, agujeros/excepciones reales; L2 rasgos geológicos y anclas; L3 heightfield 2D con bordes de mosaicos continuos; L4 divisorias y cuencas; L5 hidrográfica con grafo de receptores; L6 climas y suelos de evidencia; L7 vegetación; L8 parcelas y restricciones legales; L9 caminos, puentes y accesos; L10 núcleos y edificios; L11 objetos persistentes/WorldState. Las capas L1–L11 no se declaran existentes en E13.

## Grafo de dependencia causal
Canon y excepciones → geometría base y cotas autorizadas → microrelieve → pendiente/curvatura → cuencas y drenajes → microclima local → suelo/ecosistema → habitabilidad → economía y vías → localizaciones/edificios → identidades persistentes → WorldState. No cambiar el orden por una preferencia gráfica; un río o puente sin soporte topológico debe ser rechazado.

## Especificación técnica recomendada para Godot 2D
- Sistema de mundo 2D único, CRS interno elegido y documentado en E19; conversión de unidades explícita y reversible.
- Separar elementos de fondo, colisión, navegación, agua, jurisdicción y metadatos; sin geometría derivada directamente de píxeles ilustrados.
- Fronteras abiertas no pueden cerrar accidentalmente superficies ni activar propiedad por el algoritmo de relleno.
- Establecer niveles de detalle sin cambiar identidades ni flujos; la resolución de simulación es tarea CoreRPG.
- Distribución procedural condicionada por derechos + ambiente + compatibilidad del entorno, con semilla y versión.
- Exportación vectorial verificable (preferible GeoJSON solo después de CRS estable), tiles referenciables, IDs, control de integridad, migraciones.

## Controles de aceptación para E19 y E28
**T01** continuidad de heightfield entre teselas; **T02** gradiente de agua aguas abajo salvo excepción validada; **T03** cuencas acíclicas; **T04** Rodas bajo Corona aunque un límite visual lo rodee; **T05** Hallheim excluida; **T06** no generar edificios en anclas; **T07** caminos solo sobre trazas transitables; **T08** cambios de estación no modifican geometrías persistentes; **T09** mapa canónico vs diseño vs runtime distinguibles; **T10** reimportación determinista de contenidos.

## Ecosistema de reutilización
Nimroel Core tiene física de drenaje; Norgard Defaults contiene política y calendario; el atlas Edranor define condiciones locales. Treskal es precedente metodológico. No copiar las 99 capas activas a cada Casa, y no crear un segundo motor de clima, economía o psicología.

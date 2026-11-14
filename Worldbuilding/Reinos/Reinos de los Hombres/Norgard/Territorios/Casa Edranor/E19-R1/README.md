# E19-R1 — Geografía física, montañas, valles y toponimia de Edranor
**14/11/2026 · Atlas regional v0.2 · Diseño autoral delegado · No métrico · No runtime**

## Propósito
Construir una **geografía regional reconocible, causal, profunda y reutilizable** siguiendo el precedente real de `Casa Valrik/Geografia_local`, sin copiar Sareno, Theleno, Montes Invernos ni sus costas. Esta entrega amplía el primer esbozo E19-R1 incluido en la PR E19-R0 #87. E19-R0 es su **base obligatoria**; esta rama constituye una PR apilada sobre la rama de R0, no sobre una versión de main que carece todavía de esos documentos.

## Qué se fija y qué no
- **CANON_AUTOR**: oeste, divisoria Valkram (ladera occidental Darovan; oriental Edranor); este, divisoria Azurios (ladera occidental Edranor; oriental Galdren); sur con Aethros, línea administrativa salvo tramo del Lurien; norte sin unión artificial; Rodas aldea regia; Hallheim fuera.
- **CANON_REPO**: nombres, orientación y función de Valkram/Azurios; Lurien, Antela, Bosque Alto y Bosque de los Azurios; especializaciones y escala relativa de Dorth, Lumina, Karsath.
- **DELEGATED_DESIGN**: estructura física secundaria, tipologías de accidentes, relaciones topográficas razonadas y toponimia secundaria seleccionada; aprobada para guiar el diseño, **no** para declarar una cota, un accidente cartografiado, una entidad World State, una explotación real ni una propiedad privada.
- **UNKNOWN**: posiciones y dimensiones exactas, cumbres y collados concretos, identidad de las cuencas menores, pendientes, manantiales verdaderos, nombre efectivo entre habitantes, trama de caminos, cierre geográfico septentrional más allá de lo probado.

## Documentos
| Fichero | Contenido |
|---|---|
| 01_ATLAS_MORFOESTRUCTURAL.md | Grandes sistemas, ocho contextos naturales y continuidad entre ellos |
| 02_VERTIENTES_CRESTAS_Y_PIEDEMONTES.md | Montaña, divisorias políticas, valles de salida, riesgos y restricciones |
| 03_VALLES_CUBETAS_Y_RELIEVE_INTERIOR.md | Gramática de valles, lomas, depresiones y relaciones con anclas humanas |
| 04_GACETERO_DE_TOPONIMIA.md | Nombres canónicos, seis E13 seleccionados, nuevos nombres propuestos y descartes |
| 05_PERFILES_Y_TRANSICIONES_CAUSALES.md | Recorridos ambientales, matrices de causalidad y reglas de generación |
| 06_PARIDAD_VALRIK_AUDITORIA_Y_TRASPASO.md | Control independiente, deuda honesta, decisiones y puerta R2 |
| natural_features_v0.2.json | Registro de accidentes y familias de relieve, autoría, precauciones y vínculos |
| Tools/EdranorE19R1/validate.py | Control positivo, integridad y mutaciones adversariales |

### Cómo leer el atlas
Un nombre de **unidad geográfica de diseño** permite conversar sobre ese paisaje; **no obliga** a que cada colina tenga existencia predefinida. Un **nombre canónico** sí se conserva, pero puede carecer de ubicación local suficientemente precisa. Una **formación menor candidata** no se materializa en una escena hasta que existan relieve, agua y compatibilidad con las decisiones humanas.

### Orden de implementación
**Grandes anclas → familias de relieve → cuencas y receptores (R2) → suelos y microclimas (R3) → corredores y caminos (R4) → ocupación y economía (R5) → auditoría (R6) → Godot 2D técnico.** No confundir el cierre del atlas con cartografía métrica. No usar ningún recurso procedente de la PR #84 descartada.

### Fuentes de autoridad trazables
`Norgard/Geografía/{montanas,rios_y_lagos,bosques}.md`; E00, E01, E02, E03, E07, E13/01–04; E18; E19-R0/03, 06, 07, 08; `Casa Valrik/Geografia_local/{README,montes_invernos_cotas_y_altitudes,microrelieve_y_unidades_de_drenaje,cuencas_manantiales_red_hidrografica_menor,reglas_espaciales_generacion_motor}_v0.1.md` (donde corresponda). La PR #87 conserva el registro de la corrección autoral del 14/11/2026.

**Alcance de certificación R1:** atlas regional de relieve y toponimia **B2**, no B3 espacial ni B4 jugable; no censo ni ruta, cauce o edificio instanciado.

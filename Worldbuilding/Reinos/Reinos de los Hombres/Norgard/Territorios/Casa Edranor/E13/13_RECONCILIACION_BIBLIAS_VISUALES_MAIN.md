# E13 — Reconciliación sobre main avanzado y biblias visuales
**13/11/2026.** E13 nació de `main` `660fcf13b45916cb5df062303f40ef5168558af0`. Antes de abrir la PR, main avanzó a `fb766afa8965cf3890f3792bff373d6ba7757e05` por incorporación de tres biblias visuales Edranor. Esta evolución **no es una contradicción ni una autorización para sobreescribir las nuevas fuentes**.

## Tres fuentes posteriores inspeccionadas directamente
`Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Perfiles locales/Edranor/`:
- `EDRANOR_ENVIRONMENT_VISUAL_BIBLE_v0.1.md`: paisajes, bosques, vid, ríos, estaciones, derechos y compatibilidad NAP; base para pruebas artísticas, NO geografía oficial.
- `EDRANOR_LOCATIONS_VISUAL_BIBLE_v0.1.md`: Dorth bajos/tintos, Lumina pequeña/compacta/plaza alargada/blancos, Karsath reducida/lacustre/vino escaso y Rodas ALDEA regia; las visiones no materializan caminos o edificios.
- `EDRANOR_PORTRAIT_VISUAL_BIBLE_v0.1.md`: diversidad y retratos, once nombres E10 siguen PROPUESTA; ningún NPC legal o de WorldState queda creado.

## Comprobación de compatibilidad E13
1. **Karsath**: la biblia ambiental aporta una referencia **visual seca/semiárida** y paisaje abierto. Se conserva como **VISUAL_APPROVED_CONTEXT**, distinta de una clasificación climática cuantificada. E13/E14 no pueden decretar lluvia anual escasa, desierto, sequía permanente ni idoneidad agrícola medible a partir de la referencia artística. Este matiz complementa, sin invalidar, el clima continental regional cualitativo E03.
2. **Rodas**: montaña nevada lejana y techumbre de pizarra de fuerte pendiente son elementos de composición visual, no prueba de nieve permanente, altitud específica, tundra o jurisdicción Edranor.
3. **Lumina**: pequeña, en entorno de meseta, vinos blancos, plaza alargada/mercado anual. Se conservan la escala y la temporalidad del evento.
4. **Dorth**: arquitectura comparativamente baja y actividad de vino tinto/logística. Las seis relaciones de E07 no pasan a ser barrios catastrales.
5. **Bosque Alto y Azurios**: dos contextos distintos; explotación forestal solo con derechos, Bosque Real meridional bajo Corona.
6. **Personajes**: una representación artística no ratifica nombres, parentescos, señorío ni sucesión E10.
7. **NAP**: formatos, metadatos y perfiles de producción de imagen son instrucciones de assets visuales, no datos físicos para Godot ni una frontera exportada.

## Consecuencias para fases futuras
- E14 cruzará **paisaje visual seco** de Karsath con diagnóstico independiente de suelo, agua y aptitud agrícola; no heredará por defecto un parámetro semiárido numérico.
- E19 deberá utilizar la fuente autoral del perímetro, no capturas ambientales; una escena 16:9 no da un mapa.
- E20–E23 utilizarán las biblias como base visual respetando el atlas físico y las competencias legales.
- E25 no promocionará retratos E10 a personajes reales.
- E28 distinguirá archivo artístico, instancia jugable y autoridad del estado.

**Resultado de reconciliación:** tres nuevas biblias son compatibles con E13. No se modifican ni duplican. Esta nota documenta la nueva procedencia y la referencia de Karsath sin convertir arte en meteorología. La PR E13 conserva el alcance separado de `main`.

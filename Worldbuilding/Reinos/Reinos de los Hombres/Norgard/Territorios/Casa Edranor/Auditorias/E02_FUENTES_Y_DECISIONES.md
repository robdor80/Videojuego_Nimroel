# E02 — Registro de fuentes, autoridad y conciliación

## Fuentes consultadas en GitHub (12/11/2026)
1. \`Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/rios_y_lagos.md\`: **canon explícito** de Lurien (§1) y Antela (§2), y sistemas ajenos para control de contaminación territorial.
2. \`.../Norgard/Geografía/geografia_general.md\`: grandes sistemas, región central, separación geografía/política.
3. \`.../Norgard/Geografía/regiones_naturales.md\`: mesetas centro, bandas frías y dos barreras montañosas; no equivalencia de frontera y relieve.
4. \`.../Norgard/Geografía/montanas.md\`; \`.../Norgard/Geografía/bosques.md\`: Valkram, Azurios, Bosque Alto y bosques de Dorth.
5. \`.../Norgard/Clima/clima_general.md\`: gradientes del Reino, no congelación verificada en cada sitio.
6. \`.../Norgard/Grandes Casas/grandes_casas.md\` y \`.../Norgard/NORGARD.md\`: Edranor, la Corona y Rodas.
7. E00: \`Cartografia/E00_MAPA_Y_LIMITES.md\` y \`Datos operativos/edranor_e00_manifest_v0.1.json\`.
8. E01: \`E01_INDICE.md\`, \`Cartografia/E01_ATLAS_RELIEVE.md\`, \`Cartografia/E01_LIMITES_Y_VERTIENTES.md\`, \`Cartografia/E01_CORREDORES.md\`, \`Datos operativos/edranor_e01_relief_v0.1.json\` y \`00_Control_del_proyecto/TRASPASO_E02.md\`.
9. Capas estructurales: \`Worldbuilding/Sistemas/Nimroel Core/README.md\` y \`Worldbuilding/Sistemas/Norgard Defaults/README.md\`.

## Resolución de aparente contradicción con E00
E00 advierte correctamente: **no bautizar como Lago Antela una mancha azul del recorte sin fuente**. El documento canónico \`rios_y_lagos.md\` **sí afirma expresamente** que existe el lago, al sur de Karsath, conectado con el Lurien. No es inferencia desde píxeles: es incorporación de fuente textual previa. Se mantienen las dudas sobre pertenencia al perímetro, trazado y propiedad de las orillas. La ausencia de nombres en E01 no es evidencia de ausencia de ríos.

## Matriz de autoridad
| Afirmación o decisión | Etiqueta | Límite |
|---|---|---|
| Río Lurien, nacimiento oriental Valkram, Antela, Hallheim, Golfo de Norgard | CANON_REPO | Secuencia regional, sin polilínea |
| Lago Antela al sur de Karsath, entrada y salida del Lurien | CANON_REPO | No verifica su dominio dentro de Edranor |
| Navegación Lurien desde Hallheim al mar | CANON_REPO | No prolongar aguas arriba |
| Edranor principal región del vino | CANON_REPO | No da captaciones ni suelos concretos |
| Norte del mapa sin cierre y Rodas bajo Corona | AUTOR_2026_11_12 + OBSERVACION_MAPA + CANON_REPO | No deducir costas, caudales o control Edranor |
| Cuatro expedientes de cuenca / siete fichas sectoriales | PROPUESTA | Estructura de investigación, **no** hidrografía confirmada |
| Direcciones locales, tributarios, cuencas, usos, puentes y riesgos concretos | UNKNOWN | Requieren geometría/terreno/autor |

## Riesgos bloqueados
\`EDD-01\` cierre septentrional; \`EDD-02\` escala/DEM; \`EDD-03\` afluentes, delimitación, aguas subterráneas, estacionalidad y titularidad del agua; \`EDD-07\` pasos, puentes y vados. No se importa hidráulica de Darovan ni se añade canon sin pruebas. **CI estática no es una validación hidrológica física.**

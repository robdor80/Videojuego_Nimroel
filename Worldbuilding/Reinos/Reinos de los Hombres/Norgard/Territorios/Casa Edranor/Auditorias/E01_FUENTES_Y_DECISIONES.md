# E01 — Cadena de evidencia, conciliación y deuda

## Fuentes del canon en `main` (leídas el 12/11/2026)
1. `Norgard/Geografía/regiones_naturales.md`: centro = llanuras/mesetas, franjas fría/continental, franja boreal/polar del Reino; naturaleza ≠ política.
2. `Norgard/Geografía/montanas.md`: Valkram barrera oeste; Azurios barrera este; ambas pueden coincidir solo parcialmente con límites políticos; Vareth localizado entre Azurios y Velaris.
3. `Norgard/Geografía/bosques.md`: Bosque Alto en meseta de Lumina; Azurios en vertiente occidental con Dorth en los lindes; Bosque Real de Aethros en sector sur.
4. `Norgard/Clima/clima_general.md`: centro frío al norte, continental al sur; polar nacional extremo norte y transición gradual.
5. `Norgard/Grandes Casas/grandes_casas.md`: Dorth/Lumina/Karsath, vino, Rodas control directo de Corona.
6. `Norgard/NORGARD.md`: dos capas física/política, monarquía y cinco Grandes Casas.
7. `Norgard/Territorios/Casa Edranor/Cartografia/E00_MAPA_Y_LIMITES.md`: lectura acordada del trazo rojo, X azul y corte norte (AUTOR_2026_11_12/OBSERVACION_MAPA).
8. `Norgard/Territorios/Casa Edranor/Datos operativos/edranor_e00_manifest_v0.1.json`: invariantes de sede, topónimos y jurisdicción.
9. `Worldbuilding/Sistemas/Nimroel Core/README.md` y `Worldbuilding/Sistemas/Norgard Defaults/README.md`: jerarquía de contratos e infraestructura heredada.

No se ha atribuido al mapa autoral una escala ni un archivo vectorial existente. E01 trabaja sobre la interpretación de E00; la zona recortada no certifica el cierre.

## Matriz de decisión / autoridad
| Decisión E01 | Tipo | Justificación |
|---|---|---|
| Meseta elevada y Bosque Alto en torno a Lumina | CANON_REPO | Bosques, sección 2.1 |
| Bosque Azurios y Dorth en sus lindes occidentales | CANON_REPO | Bosques, sección 2.2 |
| Valkram y Azurios como bordes del centro, no línea política completa | CANON_REPO | Montañas y regiones naturales |
| Karsath más occidental que Lumina/Dorth en recorte | OBSERVACION_MAPA | E00 lectura de anclas |
| Ordenar siete unidades cualitativas mediante IDs | PROPUESTA | Instrumento territorial revocable |
| Relación física exacta entre las unidades | UNKNOWN | No hay DEM ni escala |
| Continuidad y accesibilidad entre núcleos | UNKNOWN | Topología E01 no es carretera E05 |
| Cierre septentrional del perímetro | UNKNOWN | El recorte corta ambos bordes |
| Dominio real sobre Rodas; Hallheim excluida | CANON_REPO + AUTOR_2026_11_12 | E00 auditado |
| Si el extremo polar de Norgard queda dentro de Edranor | UNKNOWN | Gradiente global no prueba alcance local |

## Tensión importante: «franja septentrional»
Que el **Reino** tenga costa norte y regiones plenamente polares no prueba que **Edranor** alcance esa costa. La unidad `edr_e01_far_north_unclosed` es un *contenedor de incertidumbre*, no una declaración de tundra o soberanía.

## Deuda para próximas fases
- E02: `EDD-03` ríos, drenaje, laderas receptoras y cuencas; no derivarlos de píxeles azules.
- E03: aptitud local de suelos, exposición, clima y riesgos estacionales.
- E04: pendientes agrarias, viñedos y tonelería, sin propagación al norte.
- E05: `EDD-07` red de caminos, pasos, accesos al enclave real.
- E07: distinción aldea/ciudad Rodas sin alterar su titularidad.
- Cartografía futura: `EDD-01` cierre norte y `EDD-02` escala/coordenadas autorizadas.

**Sin validar:** georreferenciación, latitudes, superficies, altitud real, lugares de paso, World State persistente, Godot, CoreRPG y Android.

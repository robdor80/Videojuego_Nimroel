# E03 — Atlas de ecosistemas y mosaicos naturales

## 1. Ecosistemas respaldados en Norgard
- Bosque Alto (entorno de Lumina): bosque mixto templado de altura sobre meseta. Coníferas en sectores más fríos/expuestos y robles/hayas en otros ambientes; abundante caza, aldeas en las lindes, explotación forestal importante pero controlada. Madera usada en barricas, tonelería y bodegas. CANON_REPO; perímetro de bosque y tenencia por parcela UNKNOWN.
- Bosque de los Azurios (lindes de Dorth, también Hallheim al sur): mixto continental y montano. En zonas bajas robles, hayas, fresnos y arces; en cotas medias mezcla con pinos/abetos; en altas coníferas, claros de matorral/pastos/bayas; caza abundante. La parte meridional cercana a Hallheim funciona como Bosque Real de Aethros; no asignar TODO Azurios a Edranor.
- Franja norte de Norgard: coníferas boreales (píceas, abetos, pinos, alerces) y abedules en claros; hacia latitudes mayores árboles más bajos y dispersos, luego tundra polar. CANON_REPO para Norgard; pertenencia local a Edranor UNKNOWN.

## 2. Lectura por unidades de E01, sin convertirlas en biomas cartografiados
| Unidad | Interpretación permitida | Validación pendiente |
|---|---|---|
| west_valkram_interface | mosaico de transición de montaña como PROPUESTA | exposición, bosque, altitud y suelo reales |
| karsath_central_west | combinación potencial de espacios cultivados y vegetación de interior como PROPUESTA | inventario del entorno |
| lumina_bosque_alto | referencia explícita a Bosque Alto (CANON_REPO) | superficies, claros y fauna taxonómica |
| central_wine_context | mosaico agrario/vinícola potencial; no monocultivo | parcelas realmente destinadas al vino |
| dorth_azurios_west | referencia explícita a Bosque de los Azurios (CANON_REPO) | lindes, pisos de vegetación y propiedad |
| north_cold_transition | transición boreal regional; hipótesis de aplicación local | presencia real en la Casa |
| far_north_unclosed | referencia polar/tundra solo regional | antes de mapear, cerrar el norte EDD-01 |

## 3. Servicios ecosistémicos e interacción
- Bosques: cubierta del suelo, madera y recursos forestales bajo condiciones de aprovechamiento documentadas. No deducir tasa de tala, riesgo de incendio o derecho de caza concreto.
- Claros y bordes: transiciones de hábitat para muestreo de vegetación y observación de fauna, sin catálogo nuevo de especies.
- Suelo-cubierta-agua: la cobertura afecta a escorrentía y erosión solo si se valida el sustrato y el régimen de lluvia.
- Zona vinícola: compatibilizar hábitats y cultivos; E04 determinará explotación, no E03.

## 4. Inventario de fauna y conservación: límites
«Caza abundante» consta para Bosque Alto/Azurios, pero NO autoriza nombres de animales, densidades, ciclos reproductivos, ataques ni botines. Sin polígonos de hábitat y propiedad tampoco se crean parques, vedados, santuarios ni nuevas competencias administrativas. El Bosque Real ya existente respeta la Corona, sin extenderse automáticamente a Dorth.

## 5. Reglas para arte y generación futura
Los ecosistemas son repertorios candidatos, nunca pintura uniforme ni pesos RNG autorizados. Cualquier generador deberá cruzar clima validado, altitud, agua, suelo, jurisdicción y exclusiones, respetando los núcleos protegidos. E03 no activa generación ni coloca flora/fauna concreta sobre Godot.

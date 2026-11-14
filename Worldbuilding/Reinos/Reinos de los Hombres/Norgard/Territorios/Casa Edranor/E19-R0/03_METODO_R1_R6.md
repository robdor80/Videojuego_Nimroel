# E19 — Procedimiento definitivo de geografía territorial para Edranor

**Autor:** método explícitamente decidido el 14/11/2026. **Referencia real:** Casa Valrik/Geografia_local/README.md; microrelieve_y_unidades_de_drenaje_v0.1.md; cuencas_manantiales_red_hidrografica_menor_v0.1.md; reglas_espaciales_generacion_motor_v0.1.md.

## Corrección fundamental: territorio no es plano técnico
E19 **NO DEBE COMENZAR por píxeles, coordenadas, georreferenciación, CRS ni polígonos**. El autor confirma que Valrik se desarrolló primero por ACCIDENTES NATURALES Y RELACIONES CAUSALES, y exige el mismo nivel para Edranor. Tratar la ausencia de coordenadas como un bloqueo de worldbuilding es un ERROR metodológico.

**Secuencia vinculante:**
1. **Anclas naturales canónicas:** Montes Valkram, Montes Azurios, Lurien, Lago Antela, Bosque Alto, Bosque de los Azurios; Dorth, Lumina, Karsath, Rodas y Hallheim como anclas humanas.
2. **Regiones y vertientes:** delimitar el papel de piedemontes, laderas, valles, meseta, relieves centrales, bosques y transición fría. La geografía no se dibuja sobre el trazo rojo, sino que explica el territorio.
3. **Cuencas y manantiales:** ríos y arroyos menores surgen de pendiente, nieve, lluvias, manantiales y cuencas receptoras coherentes. Solo los grandes cursos canónicos tienen nombre establecido; los secundarios se diseñan y nombran cuando su existencia y conexión quedan fundamentadas. Aplicar el método de Valrik.
4. **Toponimia:** nombrar los accidentes geográficos importantes, con identidad Edranor; reutilizar críticamente las propuestas E13 (rellanos, gradas, resaltes, etc.). Separar nombres canónicos preexistentes de nuevos nombres propuestos/delegados.
5. **Red física razonable:** caminos de valle, pasos de montaña justificados, conexiones productivas, pendientes y estacionalidad; ni trazar rectas entre ciudades ni afirmar que un grafo funcional es una carretera.
6. **Habitabilidad y economía:** elegir viñedos, bosques aprovechables, aldeas, servicios, talleres y corredores por suelo, clima, relieve, agua, derecho y capacidad. La geografía explica por qué existen.
7. **Implementación técnica posterior:** **cuando Godot 2D precise geometría, distancias, colisiones o escenas**, transformar el atlas causal a recursos y coordenadas técnicas. Esta implementación NO es requisito previo para desarrollar ni aprobar la geografía narrativa y funcional a nivel equivalente a Valrik.

## Fronteras fijadas por decisión del autor
- **Valkram:** ladera occidental Darovan; oriental Edranor; divisoria de montaña frontera.
- **Azurios:** ladera occidental Edranor; oriental Galdren; divisoria frontera.
- **Sur Aethros:** límite administrativo salvo tramo del **Lurien** que desemboca en Golfo de Norgard. Se define relación regional; tramo puntual puede precisarse más adelante.
- **Norte:** las líneas rojas NO se unen. No se inventa cierre.
- **Rodas:** aldea de Corona Aethros aunque geográficamente en el contexto Edranor.
- **Hallheim:** fuera de Edranor.

## Trabajo dividido por resultado, no por tecnología
| Bloque | Producto verificable | No exige |
|---|---|---|
| E19-R1 | Atlas regional de unidades, fronteras geográficas, topónimos de grandes accidentes | Coordenadas |
| E19-R2 | Cuencas, afluentes potenciales, divisorias secundarias, dinámica de agua | GeoJSON ni m/píxel |
| E19-R3 | Relieve, suelos, microclimas, bosques y aprovechamientos | Heightfield |
| E19-R4 | Corredores naturales, pasos, caminos y comercio con origen causal | Grafo georreferenciado |
| E19-R5 | Asentamientos y paisaje humano derivados de la geografía | Parcelas métricas |
| E19-R6 | Auditoría transversal de calidad frente a Valrik y coherencia de Norgard | Runtime |
| E19-TEC (cuando proceda) | Export de mundo 2D y geometría para Godot | No condiciona el cierre del atlas territorial |

La fase de ciudad Dorth E20-P01 puede crecer en paralelo; E20-P02/P03 se podrán desarrollar con **trazado conceptual y requisitos espaciales**. Una escena 2D final sí requerirá materialización técnica. No declarar B4 sin Godot, pero tampoco degradar un atlas completo por carecer de coordenadas.

## Evaluación honesta de madurez
**Geografía de lore/regional:** puede alcanzar la profundidad de Valrik con regiones, accidentes nombrados y causas sin vértices. **Materialización 2D:** se evalúa después y separada. El error anterior fue exigir como puerta de todo Edranor la geometría de Treskal ciudad cuando el patrón regional era Valrik territorial.

# E14 — Capacidad, límites y entregas
## Registro de capacidad real
| Magnitud | Valor E14 | Evidencia para resolver |
|---|---|---|
| Parcelas habitables aprobadas | **0** | registro de levantamiento E19 + inspección y título |
| Sitios de nueva ocupación aprobados | **0** | expediente por sitio + E06/E07 y jurisdicción |
| Superficie agrícola y hectáreas | **UNKNOWN** | polígonos, clasificación, derechos y área certificada |
| Capacidad de acogida y agua | **UNKNOWN** | caudales, potabilidad, saneamiento y serie estacional |
| Viviendas/camas reales, densidad | **UNKNOWN** | E20–E26, inspección de vivienda y censo |
| Población total | **UNKNOWN** | E26 abajo→arriba por hogar, no cálculo por hectárea |
| Cuota de corta forestal | **UNKNOWN** | título, cupo, plan de regeneración y protección |
| Vías, ríos y puentes | **ninguno materializado en E14** | E16/E19/E28 con trazado |

**E14 no conoce ni inventa superficies ni intervalos demográficos.** Cero aprobado no significa ausencia de personas en los lugares canónicos: significa cero *parcelas nuevas certificadas por E14*. El censo y los núcleos existentes no se sobrescriben.
## EDD y dependencias
| Deuda | Estado tras E14 | Fase de evidencia |
|---|---|---|
| EDD-01 | OPEN | E19 |
| EDD-02 | OPEN | E19 |
| EDD-03 | OPEN | E19/E28 |
| EDD-04 | OPEN | E26 |
| EDD-05 | OPEN | E25 |
| EDD-06 | RESOLVED_FOR_DESIGN | E07/E12 |
| EDD-07 | OPEN | E16/E19/E28 |
| EDD-08 | OPEN | E27 |

EDD-06 sigue resuelta para **ALDEA** Rodas. EDD-01/02 impiden cerrar geometría y escala, EDD-03 agua, EDD-07 vías; EDD-04 población. Ninguna se cierra por hacer una tabla.

## Entregables para fases posteriores
- **E15 economía vivida:** usar requisitos de cultivo, madera, trabajo y agua como entradas; desarrollar cadenas de vino/barricas y reservas sin inventar viñas actuales.
- **E16 comunicaciones:** definir demanda y accesibilidad entre núcleos, sin rutas reales hasta E19.
- **E19 geometría:** pedir mapa íntegro con límite norte, puntos de control, topología, DEM, suelos, receptor de agua, derechos y protección; identificar parcelas con IDs persistentes.
- **E26 censo:** hogares, capacidad de camas, fuentes de agua, alimento, saneamiento, trabajo y visitantes como subconjuntos, preservando E08.
- **E28 integración:** verificar cruce con CoreRPG, permisos, World State y motor Godot 2D; ningún `runtimeEnabled` antes de esas pruebas.

## Decisiones delegadas
ED14-DEC-01 a 05 figuran en JSON: seis clases, evidencia positiva obligatoria, protección/soberanía prioritaria, negativos contrafácticos y U7 no evaluable. Son decisiones de diseño de ChatGPT bajo luz verde general, no nuevos hechos ratificados por el autor.

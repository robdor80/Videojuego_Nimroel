# DAROVAN D02 — Interacciones territoriales y dependencias v0.1

**Estado:** matriz de relaciones para planificación, NO diseño de obra, asentamiento ni simulador.

## Asentamientos, bosque y agua
| Nodo/área | Dato canónico | Consecuencia D02 (no nuevo canon) | Dueño futuro |
|---|---|---|---|
| Treihord–Belara | Ciudad junto al río, no atravesada. Puerto fluvial industrial y barcazas someras; transporte de mineral/carbon/madera | Mantener relación de borde; validar calado y continuidad de ruta **solo** con estudio; no asignar crecidas ni espigones | D04/D05/D07 |
| Veldora–Golfo Veldora | Puerto comercial, río epónimo Veldora y Lhera ambos vierten al golfo | Dos bocas fluviales diferentes sin confluir interiormente; el río del fondo visual sigue DAR-P07 | D05/D07 + autor |
| Taramin–Thalen | Taramin entre dos brazos del **mismo** Thalen en su tramo terminal, puerto pesquero | Preservar ambas márgenes del brazo; inventario de riesgo y accesos sin inventar puentes, diques ni marismas | D05/D07 |
| Syvaris | Isla Darovan, ciudad en bahía principal; alternancia seco/verde | Agua dulce, captación y abastecimiento pendientes, no deducidos de imagen | D03/D07 |
| Agujas–Lhera | Lhera pasa junto a un límite forestal; interior sin poblados permanentes | Condiciones ribereñas posibles; ninguna licencia para poblado | D03/D06 |
| Bosque de la Linde | Próximo a camino Veldora–Treihord | Puentes/vados y encharcamientos UNKNOWN | D05 |
| Bosque de los Pilares | Pie sur Valkram, relación con entorno terminal Belara y madera de minas | No atribuir arbitrariamente tributarios ni muelles | D04/D05 |
| Taramin peninsular | Norte/centro semiáridos con cauces estacionales, sur más húmedo | Definir erosión, escorrentía y seguridad de asentamientos **solo tras** climatología D03 y DEM | D03/D06 |
| Arven | Isla de Norgard frente a golfo; administración UNKNOWN | No asignar control Darovan ni hidrografía continental | DAR-P01 |

## Interfaz por fases
- **D03 Clima y ecosistemas:** definir gradientes/temporadas y recarga de forma fundamentada; devolver categorías y condiciones de permanencia a cauces aún UNKNOWN. No retrojustificar geografía cambiando anclas.
- **D04 Recursos y producción:** contemplar disponibilidad hídrica y acceso industrial existente (Belara) sin asignar minas, molinos, captaciones ni nuevos usos con coordenadas.
- **D05 Rutas:** únicamente planear conexiones tras ubicar canales reales; calado de barcazas en Treihord como límite canónico. Puentes, vados, carreteras e itinerarios no fijados.
- **D06 Asentamientos:** evaluación de seguridad relativa frente a ribera/vega y acceso al agua una vez mapeados; jamás población permanente dentro de Agujas.
- **D07 Ciudades:** diseño MANUAL de los cuatro núcleos, precisión pendiente en Veldora visual, Taramin entre brazos y Treihord a un lado, sin regenerar ni modificar textos de ciudad original.
- **Cartografía:** geometrías de bocas, vaguadas, divisorias, confluencias y orden detallado de eventos solo después de validar proyección, escala, relieve y líneas de costa.
- **D11 Runtime:** transformar referencias no-runtime en instancia persistente integrada en Core y motor. Serán necesarias pruebas de guardar/cargar, eventos de crecida, independencia de redes, semillas repetibles y navegación en barcaza; ninguna realizada en D02.

## Incertezas registradas sin bloqueo documental
DAR-P01 Arven (autor), DAR-P04 fronteras/escala/cotas (autor o mapa), DAR-P07 río tras Veldora (autor/mapa), orden Belara–bifurcación frente a Treihord, cabeceras Veldora/Thalen, divisorias y redes menores, afluentes, manantiales, régimen estacional fluvial, inundabilidad cuantitativa, relación de orillas y futuros puentes/muelles. No inventar soluciones.

La elección de la denominación de las claves `d02_*` es **técnica**, nunca toponimia oficial.

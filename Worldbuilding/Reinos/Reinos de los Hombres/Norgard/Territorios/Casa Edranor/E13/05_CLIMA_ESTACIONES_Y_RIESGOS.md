# E13 — Clima, estaciones, microclimas y amenazas físicas
**Física causal de diseño**, no predicción meteorológica ni estación real medida.

## Matriz local de hipótesis
| Unidad | Gradiente sustentado | Modificadores a comprobar | Errores vetados |
|---|---|---|---|
| Valkram | montaña/efecto barrera | exposición, altura, sombra de lluvia, ventiscas episódicas | nieve permanente en toda ladera |
| Karsath | continental central | amplitud térmica y helada de parcela | copiar el clima del lago o un régimen de Darovan |
| Bosque Alto | meseta forestal más alta | dosel, claros, orientación, escarcha localizada | lluvia o helada fija |
| Centro vino | contexto continental, vino canónico | grados-día, heladas tardías, déficit hídrico | declarar viña en cada celda |
| Dorth/Azurios | piedemonte y cubierta mixta | viento de valle episódico, sombras, niebla | asignar niebla o Caleran automáticamente |
| Norte frío | gradiente Norgard hacia boreal | nieve episódica, suelo helado, fotoperiodo | importar Zanthir |
| Norte abierto | potencial transición regional | primero resolver pertenencia | asignar tundra/puerto/costa Edranor |

## Ciclo anual estructural sin meses terrestres
**Brotación / primavera:** verificar riesgo de heladas y labores, según clima real y calendario Norgard. **Crecimiento / verano:** balance térmico, disponibilidad de agua, trabajo forestal autorizado y cuidados de la vid. **Vendimia / otoño:** elección de madurez, lluvia y barro si se observan, transporte real a bodega. **Reposo / invierno:** poda y mantenimiento donde procedan; nieve/hielo solo en ubicaciones y episodios compatibles. Son procesos posibles que se conectarán con el calendario del juego, no cuatro scripts autónomos.

## Cuatro microclimas de referencia, todos condicionales
1. **Claros de Bosque Alto:** mayor insolación diurna, variabilidad nocturna; exige claro y meteorología.
2. **Umbría forestal:** más retención de humedad y distinto deshielo potencial; exige orientación de ladera.
3. **Fondo de valle:** inversión térmica/niebla únicamente con valle, estabilidad y humedad suficientes.
4. **Pie de monte:** rachas canalizadas y escorrentía diferenciadas tras verificar exposición.
Ninguno crea un topónimo, un paraje exacto o una alarma permanente.

## Registro de diez escenarios de riesgo (probabilidad e intensidad UNKNOWN)
F01 helada fenológica; F02 tormenta y erosión; F03 encharcamiento radicular; F04 deshielo súbito; F05 sequedad estival; F06 viento fuerte; F07 nieve/hielo en camino material; F08 incendio forestal; F09 pérdida de ladera por saturación; F10 crecida de cauce menor. Cada escenario exige desencadenante + susceptibilidad + exposición + vulnerabilidad. La gravedad puede ser cero si falta uno; un riesgo potencial no es un desastre acontecido.

## Diferenciación de protección
La Casa conserva competencia ordinaria de su jurisdicción, la Corona la de Rodas; mantenimiento de rutas y gestión forestal dependen de título/permiso, no de que un riesgo se observe. El área sur del Bosque Real de Azurios próxima a Hallheim no se administra por Dorth.

## Necesidades de datos y de motor
Resolver series climáticas basadas en clima de Nimroel, elevación autorizada, calendario, suelo, cubierta y agua local. Separar **geografía material** (fija/versionada) de **meteorología y estados temporales**. En Norgard Defaults/CoreRPG ya existen contratos de calendario, actividad, riesgos y memoria: Edranor solo aportará parámetros locales una vez verificados. IA narrativa no declara episodios o daños sin estado de simulación.

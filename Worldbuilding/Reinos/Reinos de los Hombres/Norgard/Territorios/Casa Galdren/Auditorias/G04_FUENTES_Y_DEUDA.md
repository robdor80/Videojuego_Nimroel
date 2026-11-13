# G04 — Auditoría de fuentes, decisiones y asuntos abiertos
**Base:** main tras G03 PR #68, SHA 0cec00d7b05a28972a9e6969279446aa0a6d119a. **Fecha:** 13/11/2026.

## Matriz de autoridad y uso
| Fuente | Aporta | Uso restrictivo G04 |
|---|---|---|
| Norgard/Grandes Casas/grandes_casas.md | Galdren más productiva en agricultura y ganadería; Arleon, Zanthir, rivalidad Darovan | Base territorial, no cifras |
| Norgard/Geografía/bosques.md | Quebrado caballar, Camino Real silvicultura, Riberas agraria | Sin bosque nuevo, propiedad o censo |
| Norgard/Geografía/rios_y_lagos.md | Caleran, Vornarsk/Keldarsk | Respeto estricto a G02 |
| Norgard/Clima/clima_general.md | Zanthir frío y ríos helados | No replicar en Arleon |
| Norgard/Sociedad/calendario_fechas_estaciones_norgard_v0.1.md | **Calendario cerrado de 365 días y cuatro estaciones con meses exactos** | Diferenciar calendario civil de fenología y cosecha locales UNKNOWN |
| Norgard/Sociedad/gastronomia_alimentacion_norgard_v0.1.md | Cereales/legumbres/huerta/fruta/ganado, conservación y cocina Galdren | Catálogo de Norgard ≠ cultivos por unidad Galdren |
| Norgard/Sociedad/aldeas_servicios_y_economia_local.md | Servicios rurales comunes/optativos; override Treskal | No adjudicar a Galdren el mínimo de herrería, ganado doméstico ni rutinas estacionales Treskal |
| Norgard/Gobierno y leyes/sistema_fiscal_y_aduanero_v0.1.md | Unidad fiscal y remesas registradas | No aranceles ni porcentajes nuevos |
| Norgard/Gobierno y leyes/moneda_y_acunacion.md | Clavo/Luna/Corona y ceca de Corona | No moneda Galdren |
| Galdren G01/G02/G03 contratos y atlas | 12 unidades, cinco ríos, 7 referencias de clima, 12 suelos UNASSESSED | No crear topología, parcelas ni simular el motor |

## Conflicto documental de precedencia (G03 → G04)
El traspaso G03 decía «calendario de Nimroel y duración de estaciones» pendientes; esta frase **no es correcta como descripción del calendario CIVIL** a la luz de la fuente canónica superior, que fija doce meses, 365 días y cuatro estaciones con meses exactos. Se registra la corrección de interpretación **en G04**, sin alterar el contrato congelado de G03: los campos UNKNOWN de G03 se leen como fechas de **eventos agrarios/fenología local**, no como negación del calendario civil ya cerrado.

También la sección 13 de servicios rurales detalla trabajos por estación con scope **Norgard/Treskal/village**. Ese ejemplo no canoniza siembra de lino, cerezas o matanza durante meses concretos de Galdren.

## Decisiones aplicadas
- **G04-D01:** canon superior permite listas alimentarias de Norgard, pero elegibilidad de cultivo por parcela continúa UNASSESSED.
- **G04-D02:** el Bosque Quebrado es centro caballar del Reino; sin linaje racial, números, establos ni ventas fijadas.
- **G04-D03:** diferenciación Zanthir minero/frío y Arleon agrario, sin inferir suministro o camino concreto.
- **G04-D04:** seis cadenas como modelos operativos futuros, no transacciones consumadas.
- **G04-D05:** seis relaciones comerciales de estudio, no rutas, tarifas ni almacenes confirmados.
- **G04-D06:** moneda/canon fiscal común; no aduanas interiores; remesas autorizadas y registradas.
- **G04-D07:** fechas de cuatro estaciones civiles CANON, agronomía localizada UNKNOWN.
- **G04-D08:** crisis posibles no son hechos actuales ni generación de daño.

## Deuda de conocimiento y traspasos
Localizar parcelas, suelo, clima y agua; comprobar cultivos y ganados efectivos por explotación; definir propiedad, derechos, jornales, calidad y volumen de existencias; establecer aprovisionamiento, reservas y almacenes; validar rutas, puertos, molinos, ferias; calendarios de trabajo específicos; razas/linajes caballares; permisos de monte y pesca; infraestructura productiva de Zanthir (G05); datos de NPC y hogares (G09); CoreRPG/Godot (G11). Ninguno se rellena por inferencia narrativa.

## Puertas
- Los datos canónicos de origen deben estar en fuentes versionadas, sin inventar productos.
- JSON debe referir G00–G03, enlazar 12 unidades, productos Norgard y 4 estaciones civiles; los 6 procesos y 6 flujos son no-runtime.
- Python debe rechazar mutaciones que importen Treskal, rellenen números, inventen cultivos o transformen un modelo en transacción.
- CI Windows/Linux G00–G04 sobre SHA definitivo; diff solo Casa Galdren, Tools/GaldrenG04 y workflow.

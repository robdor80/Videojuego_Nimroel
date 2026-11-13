# G06 — Fuentes, jerarquía y deuda transversal

**Base exacta:** `main@8610affd134d3134b8cba17b2b43c483331b127a`, G05 PR #70 fusionada. Contratos G00–G05 históricos **inalterados**. G06 no modifica canon superior, CoreRPG ni Godot.

| Fuente vigente | Dato utilizado | Precaución |
|---|---|---|
| Plan Galdren G00–G12 y traspaso G06 | objetivo, seis corredores y redes de estudio | G06 no autoriza infraestructura |
| G01_CORREDORES_HIPOTETICOS y JSON G01 | G01-C01..C06 | no rutas ni contacto físico confirmado |
| G02_TOPOLOGIA_CALERAN y JSON G02 | río único, brazos y enlace oeste→este UNKNOWN | no navegabilidad ni boca exacta |
| G03 climatología / G04 riesgos | hielo confirmado y deshielo regional | no calendario de cierre |
| G04_ABASTECIMIENTO y JSON G04 | seis relaciones G04-F01..F06, servicios Norgard | no precios, contratos o mercados locales |
| G05_PERMISOS, JSON G05 y G05_RESERVA_REGIA | seis relaciones G05-F01..F06; mandato regio permanente | G05-D01 supersede títulos antiguos G00–G04 |
| Norgard/sistema_fiscal_y_aduanero | área fiscal única, tarifas por servicio real | sin aduanas entre Casas |
| Norgard/moneda_y_acunacion | Clavo/Luna/Corona, ceca Hallheim | sin moneda Galdren |
| Norgard/aldeas_servicios_y_economia_local | redes de información rural y precedentes Treskal | no copiar automáticamente establecimientos Treskal |

## Decisiones de diseño G06, sin creación autoral de infraestructura
- **G06-D01**: seis Cxx enlazan por ID la matriz G01 y permanecen STUDY_ONLY.
- **G06-D02**: seis modalidades son hipótesis operativas; 3 hechos de hielo no habilitan ni cancelan viajes.
- **G06-D03**: doce Exx son referencias G04/G05; no se suman flujos duplicados ni se crean transacciones.
- **G06-D04**: seis modelos de mensajería/información respetan conocimiento local; puestos de correo no ratificados.
- **G06-D05**: derechos de Forja bajo Corona permanentes, sin libre acceso ni aduana Galdren.
- **G06-D06**: cero kilómetros, tiempos, puentes, puertos, aranceles, cierres o tarifas no acreditadas.

## Deuda G07/G08/G10/G11
Aprobar contornos geográficos y pendientes, cartografiar puentes/vados y pasos, resolver transición Caleran y riberas, verificar si existe navegación y puertos, delimitar competencias de litoral/Invernos y Vareth, definir asentamientos ordinarios sin invadir ciudades, verificar redes de mensajería y mercados, documentar contratos reales y autoridades/servicios, fijar acceso institucional Forja con autorización regia, crear registros de World State solo en fase de integración, probar rutas y economía con escenarios sintéticos. **Toda ausencia permanece UNKNOWN**.

## Criterio de aceptación
Contrato JSON sin runtime y con referencias cruzadas exactas; validador positivo + mutaciones negativas; CI Windows/Linux en SHA exacto; diff acotado a Galdren, `Tools/GaldrenG06` y workflow G06. El estado de CI y el merge se verificarán por separado, no se presuponen en el acta de creación.

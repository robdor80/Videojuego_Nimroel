# E18 — Registro de hallazgos, deuda y prioridad

Las etiquetas BLOCKER_MATERIAL/BLOCKER_RUNTIME son **puertas de prueba**, no errores de código confirmados ni contradicciones del canon. Las etiquetas TRACKED son pendientes editoriales con fase asignada.

| ID | Tipo | Descripción y acción mínima |
|---|---|---|
| E18-H01 | BLOCKER_MATERIAL | El norte no forma un perímetro validado; bloquear polígonos jugables. |
| E18-H02 | BLOCKER_MATERIAL | No hay escala ni georreferencia autorizada; prohibir conversión m/píxel ficticia. |
| E18-H03 | BLOCKER_MATERIAL | Agua local y derechos de captación sin verificar; no crear servicio/vid a partir de hipótesis. |
| E18-H04 | BLOCKER_MATERIAL | Grafo físico Gp vacío: las cuatro preguntas E05 no son cuatro carreteras. |
| E18-H05 | TRACKED_EVIDENCE | Sin censo, hogares residentes, aforos ni capacidad productiva comprobada. |
| E18-H06 | TRACKED_AUTHORITY | Once nombres de E10 son designId sin legitimidad o NPC activo ratificado. |
| E18-H07 | TRACKED_AUTHORITY | Cronología relativa y memoria de Rodas sin fechas, tratados ni hechos consumados acreditados. |
| E18-H08 | BLOCKER_RUNTIME | Content Pack E11 y C++ sintético no prueban integración territorial Godot ni World State. |
| E18-H09 | TRACKED_EVIDENCE | Dorth/Lumina/Karsath/Rodas/campo carecen aún de monografías y planos implementables E20–E24. |
| E18-H10 | TRACKED_EVIDENCE | Los balances, lotes y producciones son modelos: ninguna instancia económica real creada. |
| E18-H11 | TRACKED_EVIDENCE | Competencias E09 definidas, pero no constan cargos, sedes o permisos concretos materializados. |
| E18-H12 | BLOCKER_RUNTIME | Los 32 casos E17 son contrafácticos: su resultado no debe mutar historia ni ejecutar gameplay. |

## Libro EDD
| Código | Estado vigente | Responsable | Evidencia para cierre |
|---|---|---|---|
| EDD-01 | **ABIERTA** | E19 | Mapa íntegro o vértices ratificados y polígono cerrado |
| EDD-02 | **ABIERTA** | E19 | Tres controles no colineales, calibración reversible y error publicado |
| EDD-03 | **ABIERTA** | E19/E28 | DEM, drenajes, receptores, revisión territorial y comprobación topológica |
| EDD-04 | **ABIERTA** | E26 | Hogares, viviendas y totales reconciliados por localidad |
| EDD-05 | **ABIERTA** | E25 | Aprobación de identidad y legitimidad; expedientes individuales E10 |
| EDD-06 | **RESUELTA PARA DISEÑO** | E07/E12 | Rodas ALDEA de Corona Aethros; resuelto solo para diseño |
| EDD-07 | **ABIERTA** | E19/E28 | Trazas verificadas, pendientes/cruces, continuidad y derechos |
| EDD-08 | **ABIERTA** | E27 | Fuentes/registros y ratificación de hechos consumados, sin cesión presunta |

## Orden recomendado
1. **E19, fuente geográfica:** perímetro norte y escala EDD-01/02, después hidrología y derechos/accesos EDD-03/07. Investigar sin dibujar falsa topología.
2. **E20–E24, comunidades:** monografías por ancla y campo, edificios/cadenas de servicios solo tras prueba material de sitio; Rodas bajo Corona.
3. **E25–E27, autoría humana:** linajes, censo y cronología con decisiones de autoridad separadas de datos propuestos.
4. **E28, ejecución real:** convertir contratos en estado persistente, sincronizar con Godot 2D/CoreRPG y probar hechos/nodos realmente cargados.
5. **E29, cierre:** auditar materialidad y paridad sin obligación de declarar éxito si quedan deuda o bloqueos.

## Reglas de corrección
No marcar EDD como resuelta solo porque aparece citada en tres JSON. Cada cierre requiere fuente verificable, autoridad, caso positivo y adversarial, actualización versionada de contrato y revisión de regresión. Una hipótesis que carece de evidencia permanece pendiente; un veto explícito bloquea incluso ante otras pruebas positivas. Se conserva EDD-06 **para diseño**, sin inferir tratados o transferencias históricas.

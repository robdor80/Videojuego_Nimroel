# E19 — Acta de alcance, decisiones, pruebas y condición de salida

## Decisiones delegadas
| ID | Adoptada | Descartado |
|---|---|---|
| ED19-DEC-01 | Fuente general con hashes binarios, recorte E00 pendiente de bytes | Suponer que el mapa general muestra la línea roja completa |
| ED19-DEC-02 | Preparar CRS interno 2D, sin asignar escala real | Convertir barra de 400 millas en metros/píxel |
| ED19-DEC-03 | Separar frontera física de excepción jurídica Rodas | Declarar Rodas bajo impuestos de la Casa |
| ED19-DEC-04 | Definir L00–L11 y contrato fail-closed | Generar ríos, DEM y caminos a partir de una ilustración |
| ED19-DEC-05 | Mantener E19 abierta con Draft y validaciones de preflight | Marcar fase totalmente concluida por CI sintética |

**Autoridad:** ASSISTANT_DELEGATED_DESIGN; no se reforman canon, sucesión, jurisdicción ni hechos históricos.

## Ratificación autoral posterior a la apertura E19
Constan cinco decisiones `ED19-AUT-01..05` sobre norte, vertientes, sur aproximado, Hallheim y convocatoria berserker de Rodas; se incorporan en [07_RATIFICACION_AUTORAL_LIMITES_RODAS.md](07_RATIFICACION_AUTORAL_LIMITES_RODAS.md). Esto **resuelve la ambigüedad cualitativa del norte**, pero no cierra EDD-01 como polígono ni EDD-02 como escala. La ratificación es del autor; la arquitectura de contrato sigue siendo diseño delegado.

## Entregables con evidencia
- Archivo mundial en repositorio y subida aportada **idénticos bit a bit**: blob SHA, sha256 y longitud verificados.
- Fichas de E00/E01/E02/E13/E16/E18 cruzadas.
- Contrato JSON E19 con capas, anclas, U1–U7 y deudas explícitas, sin georreferencia ni rutas.
- Pruebas de integridad de bytes; mutaciones adversariales del contrato y fixtures de geometría sintética.
- Workflow E19 de Windows/Linux con regresiones y consumidor CoreRPG E11 fijado.

## Puertas materiales abiertas (no paliables por tests sintéticos)
| Deuda | Evidencia imprescindible | Salida |
|---|---|---|
| EDD-01 | original de mapa con perímetro rojo completo O vértices/cierre ratificados, topología validada | Polígono jurisdiccional |
| EDD-02 | ≥3 controles no colineales con distancias/escala defendibles, preferible holdout y residual publicado | Transformación 2D reversible |
| EDD-03 | DEM revisado + drenajes/receptores consistentes, derechos tratados aparte | Agua y cotas útiles |
| EDD-07 | Trazas + pendientes/cruces + derechos de paso y verificación continuidad | Grafo físico no vacío |

No se libera geometría jugable hasta EDD-01/02. Ninguna prueba verde de PR significa que estas cuatro pruebas materiales se hayan satisfecho.

## Estado de aprobación
**PREFLIGHT_DOCUMENTAL_ENTREGADO / E19_CARTOGRAFIA_COMPLETA_PENDIENTE.** Mantener Draft hasta incorporar y auditar material; puede avanzarse en el estudio literario E20–E24 **con limitación expresa**, no en posicionamiento geográfico exacto ni colocación de edificios. E28 integrará runtime cuando esté disponible.

El norte ha sido explicado por el autor como alcance hasta el norte del reino, sin una frontera interior. Para certificar el **polígono**, todavía hace falta recuperar un contorno trazable completo del territorio con divisorias y frontera meridional revisadas, o vértices ratificados con calibración; no basta usar el borde superior de la captura.
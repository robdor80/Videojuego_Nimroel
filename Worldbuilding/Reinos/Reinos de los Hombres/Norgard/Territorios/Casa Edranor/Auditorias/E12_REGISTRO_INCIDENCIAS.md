# E12 — Registro de incidencias y deuda territorial
**Fecha:** 13/11/2026. Una incidencia sin fuente nueva no se «arregla» inventando canon.

| ID | Clase | Hallazgo / riesgo | Actuación E12 | Estado |
|---|---|---|---|---|
| E12-M01 | MENOR | Índices y traspasos E00–E11 conservan estados históricos «no iniciada» / «PR pendiente» | Nota `ESTADO_VIGENTE_E12.md`; no reescribir fuentes bloqueadas por SHA | RESUELTA DOCUMENTALMENTE |
| E12-I01 | IMPORTANTE | La validación E11 verifica fuentes por separado; faltaba puerta E12 cruzada entre once fases | `Tools/EdranorE12/validate.py` + CI E12 Windows/Linux y adversariales | PENDIENTE EVIDENCIA CI E12 |
| E12-I02 | IMPORTANTE | Content Pack E11 estructural podría confundirse con simulación jugable | Cuatro niveles de evidencia y capacidades declaradas `false` | LIMITACIÓN EXPLÍCITA |
| E12-I03 | IMPORTANTE | Rodas dentro del ámbito geográfico podría recibir por error impuestos/jueces/guardia/mando de Edranor | Matriz C01/C08/C11, negativos, jurisdicción desagregada | PREVENCIÓN CONTRACTUAL |
| E12-A01 | RESERVA AUTOR | EDD-01: límite norte; EDD-02: escala y georreferencia | Mantener perímetro cualitativo, sin coordenadas | ABIERTA, NO BLOQUEA DOCUMENTACIÓN |
| E12-A02 | RESERVA AUTOR | EDD-03: hidro local; Antela/Lurien no adscritos físicamente a Edranor | Mantener `UNKNOWN`, sin riberas o rutas fluviales nuevas | ABIERTA |
| E12-A03 | RESERVA AUTOR | EDD-04: población y hogares | No trasladar cifras Darovan/Valrik/Treskal | ABIERTA |
| E12-A04 | RESERVA AUTOR | EDD-05: señoría, heredero, filiación y ratificación de once nombres E10 | Diseño `PROPUESTA_E10`; cero NAME/KIN/NPC legales | ABIERTA, BLOQUEA PROMOCIÓN A NPC |
| E12-A05 | RESERVA AUTOR | EDD-06: Rodas aparece como «ciudad» ocasionalmente en manuscrito | Jerarquía E07: escala aprobada **ALDEA**; armonización narrativa futura | RESUELTA PARA DISEÑO |
| E12-A06 | RESERVA AUTOR | EDD-07: vías, servidumbres y accesos reales | Cuatro preguntas E05, cero aristas reales; no generar pathfinding físico | ABIERTA, BLOQUEA RUTAS |
| E12-A07 | RESERVA AUTOR | EDD-08: hechos y fecha de conflicto/diplomacia sobre Rodas | Cronología relativa propuesta, sin tratados ni fechas | ABIERTA, BLOQUEA HISTORIA FECHADA |
| E12-A08 | DEPENDENCIA TÉCNICA | Falta Godot 4.7.2 2D conectado al pack y lógica territorial simulada | Proponer fase específica posterior NIM/Host/territorio, con tests reales | PENDIENTE POST-E12 |

**Prioridad:** CRÍTICA = cambio de canon o fuente bloqueada, propietario incorrecto, IDs rotos, prueba que deja pasar una falsificación. IMPORTANTE = ausencia de validación o conclusión engañosa. MENOR = estado histórico, referencia editorial.

**No detectada en documentos auditados:** una modificación autorizada que transfiera Rodas a Edranor, cierre el norte o ratifique la genealogía. **No realizarla.**

El CI E12 deberá decidir si E12-I01 queda validada; una conclusión redactada antes del run no equivale a resultado ejecutado.
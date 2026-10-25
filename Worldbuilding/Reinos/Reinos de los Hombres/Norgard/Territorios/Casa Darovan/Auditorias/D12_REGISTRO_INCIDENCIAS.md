# D12 — Registro de incidencias, gravedad, actuación y estado
**Estado:** auditoría de consolidación. Las pruebas se acreditan exclusivamente por los runs concretos de CI de la PR D12.

| ID | Gravedad | Evidencia | Tratamiento | Estado |
|---|---|---|---|---|
| D12-M01 | MENOR | Cabeceras históricas de \`REGISTRO_FASES.md\` indican D08–D11 no iniciadas y PR anteriores pendientes; PR #14–#37 territoriales constan fusionadas | Crear nota de estado vigente y adenda sin borrar el historial | CORREGIDA ADMINISTRATIVAMENTE |
| D12-M02 | MENOR | \`Contratos_y_runtime/README.md\` se redactó en D00 con D11 aún «sin implementar» | Adenda de interpretación actual; no editar contratos históricos | CORREGIDA ADMINISTRATIVAMENTE |
| D12-M03 | MENOR | \`TRASPASO_D12_PREPARATORIO.md\` dice D12 no autorizada: corresponde al cierre D11 | Conservar como documento PREPARATORIO y registrar inicio autorizado el 25/10/2026 | CORREGIDA POR NOTA ACTUAL |
| D12-I01 | IMPORTANTE / RIESGO EVITADO | D00 tiene Arven \`null\` histórico y D11 exige no alterar los 11 blobs bloqueados; anexo 21/10 atribuye Arven a Darovan | Precedencia documentada; guardrails comprueban dato vigente en D01/D02/D09/D10/D11. No editar D00 | RESUELTA SIN MODIFICAR CANON |
| D12-I02 | IMPORTANTE | D11 valida cada fase con tests separados; faltaba validador transversal propio D12 | Nuevo \`Tools/DarovanD12/validate.py\`, negativas in-memory e integración en Actions Windows/Linux | IMPLEMENTADA; RESULTADO DEPENDE DE CI |
| D12-I03 | IMPORTANTE / DEPENDENCIA | D11 C++ confirma catálogo y save/load sintético, no la ejecución de economía, población, trayectos ni personalidad | Clasificar explícitamente en matriz Core/Host, sin modificar motores | PENDIENTE IMPLEMENTACIÓN POSTERIOR |
| D12-A01 | RESERVA AUTOR | DAR-P04/P08 parcial/P09/P10/P11: cartografía, hidrología métrica, clima, minas, itinerarios, volúmenes sin aprobar | Mantener UNKNOWN, no bloquear consolidación documental cualitativa | NO BLOQUEANTE DEL CIERRE DOCUMENTAL |
| D12-A02 | RESERVA AUTOR | Gobierno: regente/herederos, casas menores, magistrados/número fuerzas, tributos precisos | No deducir ni legislar desde D09 | NO BLOQUEANTE |
| D12-A03 | RESERVA AUTOR | D07 detalles urbanos, D08 censos individuales, D10 costumbres/localización de Arven | Conservar PROPOSAL_PENDING_AUTHOR y UNKNOWN | NO BLOQUEANTE |
| D12-A04 | RESERVA AUTOR | Rutas o emplazamientos de escenografía reales y poblaciones instanciadas requieren fuentes o decisiones | No generar automáticamente mediante D06/D08 | BLOQUEANTE SOLO DE MATERIALIZACIONES QUE LOS NECESITEN |

**Criterios:** CRÍTICA = violación de canon, corrupción de IDs/fuentes o validador que permite datos inválidos; IMPORTANTE = insuficiencia de pruebas/contratos o representación engañosa; MENOR = enlace/estado histórico/organización.

No se ha identificado inicialmente una contradicción canónica contemporánea que obligue a reescribir las once fuentes bloqueadas. El dictamen definitivo queda condicionado a las comprobaciones nuevas y a CI final. Si aparecen fallos, actualizar esta acta, reparar y repetir CI; nunca ocultarlos o declararlos aprobados.

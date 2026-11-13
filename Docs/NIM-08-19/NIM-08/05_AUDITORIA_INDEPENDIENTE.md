# NIM-08 P01–P04 — Auditoría final independiente del diseño

Fecha: 12-11-2026. Alcance de esta revisión: verificar artefactos NIM-08 frente a la planificación aprobada, código del pin consultado y criterios V001. **Independencia de método:** comprobación de fuentes reales, contratos, SHA, logs Windows y Ubuntu; no confundir esta revisión con una prueba nativa de la misión.

## Matriz de puertas de NIM-08

| Condición de cierre solicitada | Evaluación | Evidencia y límites |
| --- | --- | --- |
| Plan de NIM-08–19 verificado y reutilizado | CUMPLIDA | cinco archivos de planificación desde ref 40f2df20, conservados en la rama de diseño |
| P01 auditoría Nimroel + CoreRPG | CUMPLIDA | 00_ESTADO_Y_FUENTES, Core pin 4f2828 y PR NIM-07 #40 merged |
| P02 contratos de aldea/hogares/personas/oficios/objetos/localizaciones/tiempo/acciones | CUMPLIDA COMO DISEÑO | ADR y world/action schema 0.1.0; ninguna API runtime afirmada |
| P03 arquitectura y reproducibilidad | CUMPLIDA COMO DISEÑO | fuente -> manifest -> candidato -> autoridad Core -> filtro -> Godot; semilla y no reroll |
| P04 backlog, pruebas y reparto | CUMPLIDA | 02_FIXTURES_Y_ACEPTACION, 03_ENCARGO_CODEX, 06_TRASPASO |
| 28 criterios V001 trazados | CUMPLIDA (TRAZABILIDAD) | 28/28 cotejados contra canon y matriz, ninguno PASS jugable |
| Validación propia estática | CUMPLIDA | run 43217324339, Windows 18/18, Ubuntu 18/18 |
| Separación Core/Nimroel/Godot y reutilización Star Trek | CUMPLIDA COMO ARQUITECTURA | ADR-08-01 a ADR-08-08; ninguna modificación en otros repos |
| NIM-09 sin decisión de arquitectura fundamental bloqueante | CUMPLIDA | proyección de fuentes y manifiesto pueden desarrollarse sin API nativa nueva |
| Experiencia A/B/C, mundo completo, pruebas reales MSI/Tab | FUERA DE ALCANCE NIM-08 | NIM-10–19; no inferir de CI documental |

## Verificaciones negativas y riesgos residuales

- No se añade WorldState en GDScript, ni se tolera reloj ligado a FPS o misión predefinida. Actores, herramienta, trabajo y memoria no existen todavía como estado de dominio completo.
- El schema world-instance describe un candidato futuro. JSON Schema no puede por sí solo demostrar integridad de referencias, contención acíclica, conectividad, autorización, consistencia de hogar/población o atomicidad multientidad. Esas invariantes constan expresamente como obligaciones de runtime/test.
- ActionEngine del pin admite operaciones estructurales; **NO** prueba acción de reparar, mover ni jornada laboral. Simulation::step es atómica por acción, no por el conjunto de una reparación.
- El origen del PDF maestro permanece fuera del checkout, aunque hay huella; los datos operativos V1 deben proceder del árbol Worldbuilding + lock y no de un PDF ambiguo o de una conversación.
- La main de CoreRPG tiene cambios que Nimroel no consume en su pin; cualquier propuesta futura necesita aprobación, revisión ABI, snapshots y Star Trek.
- La ausencia de física Android I4 sigue abierta, aunque PR #40 esté merged. La prueba del MSI de octubre no se extrapola al binario reconciliado.
- El informe no acredita haber ejecutado herramientas nativas ni un juego físico en NIM-08.

## Dictamen

**NIM-08 completada técnicamente a nivel de arquitectura, contratos, auditoría y preparación de la fábrica**. El alcance documental es consistente con P01–P04 y los 28 criterios canónicos permanecen sin degradar.

**Pendiente de gobierno:** revisión/fusión de PR Draft #50 por el propietario; confirmación de CI del último commit documental en la PR; pruebas físicas de NIM-07 Android, que no se transforman en bloqueo artificial para empezar el pipeline no nativo de NIM-09.

**Prohibición de promoción:** no publicar la aldea como jugable ni declarar V001 PASS a partir de este dictamen. NIM-09 requiere una orden independiente.

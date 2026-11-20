# NIM-08 P03/P04 — Fixtures, pruebas futuras y trazabilidad 28/28

**No se duplica la matriz normativa.** Las 28 filas completas, fases responsables, estados PENDIENTE y tres recorridos canónicos A/B/C siguen en ../02_MATRIZ_TRAZABILIDAD_V001.md y en el archivo Worldbuilding/.../MATRIZ_ACEPTACION_V001_v0.1.md. Esta hoja define los contratos técnicos para convertirlas en tests ejecutados. La comprobación Tools/NIM08/check_contracts.py coteja IDs y cardinalidad; no declara aprobar los comportamientos.

## Grupos y rutas de evidencia

| Grupo | IDs | Tipo de verificación futura | Fases |
| --- | --- | --- | --- |
| G | G01–G06 | Generador 100 semillas, constraints, variación, grafo y revisión visual | NIM-10/19 |
| P | P01–P04 | Navegación/descubrimiento real, conversación individual, no misión forzada, ciclo escenas | NIM-12/15/16/17 |
| Q | Q01–Q08 | Ítem físico, legalidad, orden/cola, recursos/progreso, devolución/abandono, conocimiento | NIM-13/14/15/16 |
| S | S01–S06 | Save/restore, reloj fuera de escena, migración, hash lógico reproducible | NIM-14/18 |
| H | H01–H04 | Host local Windows, IA opcional, inspector y experiencia física | NIM-17/19 |

Test harness posterior debe guardar por cada ID: estado, evidencia o motivo PENDIENTE, run_url, run SHA, versión de Core y pack, schema/generador, fixture/región, seed, máquina+OS, pre/post hash, acciones, salida y revisión. Un build APK NO cuenta como PASS_FISICO. H02 es OPCIONAL/EXCEPCION_AUTORIZADA si no se implementa proveedor remoto; nunca se marca PASS de IA por el fallback.

## Tres pruebas doradas (NO ejecutadas en NIM-08)

**A — Ayuda completa:** el agricultor es instancia con trabajo; descubre por fuente, autorización legítima, traslado por ruta, cola y recursos, progreso por tiempo, retirada/devolución, conocimiento del propietario, save/restart; verificar tool.id única y 0 atajos por diálogo.

**B — Pendiente:** con herrero ocupado o material insuficiente se conserva en espera; guardar en mitad, destruir proceso, restaurar mismo ID, orden, materiales, progreso y ubicación; avanzar reloj mediante acción con taller fuera de vista, no por FPS o tiempo real no autorizado.

**C — Indiferencia:** el jugador no descubre, rechaza o abandona; el objeto no desaparece, aldeanos no congelados, consecuencias justificadas y persistidas; acciones de terceros son válidas solo si hay agenda/recursos. Rechazo nunca equivale a resolución mágica.

Variantes obligatorias: herramienta ordinaria alternativa con las mismas reglas; observador conocedor vs no testigo; objeto en manos no autorizadas; herrero ocupado/libre; recurso ausente; taller cerrado; edificio opcional no generado; rutas bloqueadas; save corrupto/pin distinto; semillas diferenciadas sin cambiar políticas.

## Protocolo de resultados

- Test NIM-08 (documental): esquemas JSON bien formados; manifiesto válido o rechazado; 28 IDs sin pérdida, sin atribución PASS; catálogo V001 canónico sin modificaciones. Las pruebas estáticas **no miden la jugabilidad**.
- Test NIM-09: dos proyecciones de fuentes -> mismos bytes/hashes, ref inexistente o fuente no autorizada => fallo.
- Test NIM-10: 100 seeds válidas + 2 repeticiones cada una; estructuras sin huérfanos, rutas verificadas; opcionales variable.
- Test NIM-11–16: semántica con falsos positivos/negativos de derechos, NPC, agenda y comunicación. Harness sin Godot.
- Test NIM-17–18: acciones/observaciones con GDExtension, recuperaciones entre procesos y exportaciones por plataforma.
- Test NIM-19: A/B/C ejecutados, pruebas físicas MSI + Tab S9+, revisión editorial de experiencia y segunda aldea usando mismo algoritmo; evidencia de cada fila.

Cualquier dictamen con menos de 28 IDs trazados o pruebas de equipos sin registrar se considera incompleto.

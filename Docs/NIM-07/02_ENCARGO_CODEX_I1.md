# NIM-07 / I1 — Encargo listo para Codex: conversación principal conectada a CoreRPG

**EJECUTAR SOLO I1.** Base: rama `feat/nim-07-first-rpg-experience`, creada desde `main` en `1865fb7fedb616ef7abdffbb195d3698825d4c8a`. Primero inspeccionar HEAD y conservar todos los cambios ajenos; jamás modificar `main` ni fusionar. Leer `Docs/NIM-07/01_AUDITORIA_ALCANCE_Y_HOJA_DE_RUTA.md` antes de escribir.

## Objetivo único

Hacer que el **usuario escriba en la pantalla principal del juego** una consulta de estado estructural y reciba una respuesta **auténtica, autorizada y saneada** por una `CoreRPGSession` creada mediante la GDExtension NIM-06. **No** convertir una demo en respuesta de Core ni afirmar que se ha generado la aldea V1. I1 utiliza temporalmente las 4 entidades neutras ya probadas; el pack Treskal 4.13 se integra en I2.

No crear pantalla/laboratorio separado. La prueba nativa existente permanece como diagnóstico de NIM-06.

## Lecturas obligatorias

1. `Game/Host2D/scripts/main.gd`, `interaction_pipeline.gd`, `core_port.gd`, `native_world_controller.gd`, `core_save_store.gd`.
2. `Game/Host2D/scripts/native_vertical.gd` y `native_diagnostics_entry.gd`.
3. `Game/Host2D/tests/native_bridge_probe.gd`, `nim06_smoke.gd` y tests NIM01–05.
4. `Game/BridgeCoreRPG/native/README.md`, `Game/BridgeCoreRPG/native/src/bridge.cpp`, `Docs/NIM-06/12_CIERRE_FINAL.md`.
5. `Docs/NIM-01_EXPERIENCIA_CONVERSACIONAL.md`, `Docs/IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md`, `ContentPacks/treskal-villages/README.md`.

## Trabajo concreto

**A. Entrada nativa visible y diferenciada.** Añadir a `main.tscn/main.gd` una opción clara **«Iniciar experiencia CoreRPG (estructura de prueba)»**. Al activarla, el Host de confianza mantiene un `native_world_controller` real durante la sesión de la pantalla, llama a `start()` una sola vez al crear la partida y usa `query()` en turnos siguientes. No crear `WorldState` paralelo en GDScript, no reinicializar por consulta. Un error de librería nativa ausente se presenta como indisponibilidad honesta, nunca como simulador encubierto. Separar sin ambigüedades los modos: maqueta histórica, integración antigua bloqueada y nuevo flujo real conectado. Cambiar subtítulos/indicadores SOLO cuando el flujo nuevo esté realmente activo.

**B. Entrada textual estrecha, local y verificable.** Dar soporte a 2–3 expresiones claras, p. ej. «estado», «¿qué sabe mi personaje?» y «¿qué conozco?», con normalización acotada. Tratar `¿qué veo?` sin inventar percepción visual: indicar que todavía no hay percepción espacial y, si procede, ofrecer el conocimiento estructural autorizado. No asignar servicios, nombres, profesiones, edificios, posiciones, diálogo ni eventos a IDs anónimos. Las frases no soportadas reciben una explicación breve; no se envían a Gemini, Luna ni Sol y **no se ejecuta acción** a partir de texto ambiguo.

**C. Respuesta segura en el historial.** La única fuente de hechos jugables es el `session.context({api_version:1})` con observador ligado. Dar formato entendible a hechos efectivamente presentes; si no hay etiquetas del pack, identificar entradas como entidades estructurales técnicas, no bautizarlas con nombres de Treskal. Distinguir `complete` de `context_status` truncado o error. No mostrar `CoreRPGHost.diagnostics`, revisión, RNG, ActionResult, contexto de otro observador, hechos ocultos, `context_id`, concesiones ni datos de guardado. No fabricar un mensaje de NPC: emisor «SISTEMA · CORERPG (PRUEBA ESTRUCTURAL)». Si el contenido no puede interpretarse con garantías, responder con limitación en vez de afirmar observaciones falsas.

**D. Guardado/continuidad básica opcional de I1.** Si cabe sin ensanchar demasiado el diff, permitir «Guardar prueba estructural» y «Restaurar prueba estructural» desde la misma pantalla usando `native_world_controller.save_slot()/load_slot()`, nunca copias de mundo. Tras restore vuelve a abrirse sesión; no reutilizar handles caducados. No declarar aún persistencia de la publicación V001, que requiere los metadatos de I4. Si esta parte compromete I1, diferirla a I4 con motivo documentado.

**E. Respeto total por los tests previos.** No cambiar el bloqueo contractual de `InteractionPipeline.submit_text(..., MODE_INTEGRATION)` cuando no recibe una sesión. Preferible crear flujo/controlador de conversación nativo adyacente con contrato propio antes que forzar que el pipeline legado anuncie `integration_ready=true` global. No tocar la adaptación de teclado Android de NIM-05 ni el scroll/escala del laboratorio NIM-06; añadir únicamente UI mínima al Host principal. Mantener voz, TTS y diagnóstico proveedor aislados y sin gasto.

## Validación pequeña pero auténtica

1. Tests existentes NIM-01–06 conservan su comportamiento, especialmente `CORE_NOT_CONNECTED` sin sesión y las 129 comprobaciones Core de NIM-06.
2. Añadir **una única** smoke test NIM-07 que, con extensión nativa realmente cargada, compruebe arranque desde controlador usado por la pantalla principal, 2 consultas consecutivas del mismo mundo, salida estructural filtrada, entradas inválidas y rechazo de hechos ocultos. Si se integra guardado, un caso de save/restore y sesión nueva. Sin miles de fixtures ni scripts de estrés.
3. Integrar esa smoke test al workflow **existente** más adecuado; no crear otra infraestructura CI sin necesidad. CI Windows que efectivamente carga la DLL y ejecuta consulta; Linux de control cuando corresponda; Android ARM64 compilación/export como regresión, sin afirmar ejecución física Android desde Actions.
4. Revisión del diff: ninguna clave/API/pago, ninguna modificación de CoreRPG o los pins nativos, ninguna alteración histórica de NIM-06 ni cambios de canon. Presentación legible con teclado en Windows/Android.
5. Conservar evidencia de comandos, jobs, commits y SHA; si se usa un chequeo de UI no físico, etiquetarlo correctamente.

## Entrega esperada

- Implementación limitada y documentada en esta rama, con commits pequeños.
- Informe `Docs/NIM-07/03_RESULTADO_I1.md`: archivos afectados, arquitectura de vida de sesión, flujo real paso a paso, pruebas efectivamente ejecutadas y enlaces a Actions, limitaciones y recomendación I2.
- **No** desarrollar I2, no modificar el Core, no preparar misión «La herramienta rota», no activar APIs facturables y no abrir PR final ni fusionar sin el siguiente encargo de revisión.
- Ante una incompatibilidad real, documentarla e intentar corrección pequeña solo dentro del Host. No sustituir datos Core por datos ficticios.

## Éxito observable de I1

Con una compilación nativa NIM-06 disponible, desde **la pantalla principal** el usuario selecciona «Experiencia CoreRPG», escribe «¿qué conozco?» y recibe en los bocadillos información derivada de la sesión real. Un segundo turno reutiliza el mismo mundo. La pantalla comunica claramente que se trata de una **prueba estructural no equivalente aún a una aldea V1 generada**.

Este éxito no cierra NIM-07: I2 debe integrar el fixture Treskal 4.13 fielmente y validar su contenido antes de atribuirle entidad canónica.

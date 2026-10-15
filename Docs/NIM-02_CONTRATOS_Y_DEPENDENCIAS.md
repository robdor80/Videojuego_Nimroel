# NIM-02 — Contratos, CoreRPG y próximos enlaces

Fecha: 2026-10-15. Especificación de frontera; NO supone integraciones reales funcionando.

## Resultado v1 del pipeline
interaction_pipeline.gd recibe texto, modo (demo o integration) e identificador local de turno.
Devuelve Dictionary con contract_version, turn_id, status, error_code, reply, reply_kind, proposal_type, portrait_demo, speaker_id y world_mutated.
status solo puede ser demo, blocked o rejected en NIM-02. reply_kind system_demo y system NO representan un NPC.
turn_id es correlación de interfaz, no EntityId persistente. No hay WorldState, autoridad, revisión ni acción confirmada en la interfaz.
Limita textos a 1500 caracteres, rechaza vacío o modo incorrecto y mantiene texto en caja tras error.

## Puertos y estados honestos
- core_port.gd: core_available=false; submit devuelve unavailable / CORE_NOT_CONNECTED, world_mutated=false.
- gemini_port.gd: interpretación y narración unavailable / GEMINI_NOT_CONNECTED; sin HTTP, tokens ni generación de hechos.
- voice_port.gd: transcripción/síntesis unavailable / VOICE_BACKEND_NOT_INSTALLED. La escritura siempre permanece accesible.
- interaction_pipeline.gd: ante falta de CoreRPG, integration devuelve blocked sin intentar Gemini.

## Requisitos exactos a coordinar con Codex (CoreRPG, repo independiente)
1. P1 NDK: fijar toolchain, ABI arm64-v8a, API Android, libc++, excepciones/RTTI/PIC; compilar C++20 mínimo y ejecutar una operación real en la Tab S9+ sin el MSI. Registrar commit, logs, NDK, errores y Windows x64 comparable.
2. Contrato C/C++ estrecho para enlace GDExtension del consumidor: init, shutdown, versión/capabilities, EntityId estable, consulta read-only, errores y ownership explícito. No incorporar Godot al Core portable.
3. Completar 4.9: percepción y conocimiento autorizado por observador (sin secretos en prompts).
4. Completar 4.10: validación de propuestas tipadas, resultados, revisión/eventos, idempotencia y simulación; no segundo ActionEngine.
5. Completar 4.12: Context Builder de IA filtrado; el Core verifica, Gemini solo propone y redacta.
6. Preparar 4.13: contenido Nimroel declarativo y persistente, ids/versión; separar canon/host del motor reutilizable.
7. Matriz Windows/Android: snapshot, memoria, errores nativos, guardado user://, fondo/reanudación Android y compatibilidad ABI; nunca declarar éxito ARM64 por mera compilación.

## Flujo futuro autorizado
Entrada textual o ASR editable -> Gemini interpreta como propuestas tipadas -> CoreRPG conoce y valida hechos/acciones -> Gemini narra solo la proyección autorizada -> bocadillo de NPC o sistema -> sherpa-onnx TTS exactamente sobre texto de NPC si hay identidad y voz.
Los mensajes del jugador nunca se leen con voz TTS. Las llamadas remotas requieren consentimiento, seguridad, timeout, control de coste y autenticación segura; jamás claves en un APK público.

## Evidencia por tipo
- CI Godot headless: sintaxis, carga, clasificación demo, bloqueo honesto y regresión de panel.
- CI export Windows: exe+pck de laboratorio; no demuestra arranque real.
- CI export Android: apk y librerías del motor Godot arm64; no demuestra GDExtension Core ni sherpa.
- Test físico usuario: arranque, selector demo/integración, error Core, teclado e historial en MSI y S9+; no acredita partida jugable.

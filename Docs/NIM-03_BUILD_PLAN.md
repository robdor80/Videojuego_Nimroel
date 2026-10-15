# NIM-03 BUILD — Plan ejecutado, dependencias y límites

Fecha: 2026-10-15. Base comprobada: main @ df43be5b2a62b137b8ed77f7900818e39646c272 (PR #18 NIM-02 integrada). Rama: feat/nim-03-build. **PR Draft; prohibido fusionar sin autorización.**

## Auditoría previa
- NIM-01 (PR #13): Host Godot 4.7.2 Standard, 2D, escritorio y tablet, bocadillos, demo, NIM-01 smoke y exportaciones.
- NIM-02 (PR #18): pipeline v1 de texto, contratos y bloqueo honesto, CI y pruebas manuales MSI/Tab S9+. Su CI aprobada no conectaba servicios.
- Se leyó en CoreRPG/main: `include/corerpg/version.hpp`, `include/corerpg/world_state.hpp`, `CMakeLists.txt`, README y roadmap. Incluye versión 0.1.0, `library_version()`, `WorldState::entity_count()`, `revision()`, `contains()`, `next_entity_id()`; es una biblioteca estática C++20. **No se encontró API C/GDExtension ni matriz Android/NDK integrada.** El README/roadmap tiene notas históricas de 4.8 que no sustituyen al estado del código.
- `Worldbuilding/` y canon quedan intactos. Ningún contenido rico ni percepción 4.9 se supone disponible.

## Objetivo realista y pasos
1. **P01 Auditoría**: main, fusiones, código y dependencias. Completada.
2. **P02 Gemini técnico aislado**: servicio Python ligado a 127.0.0.1 en MSI, clave desde `GEMINI_API_KEY` solo en entorno del proceso; petición HTTPS con TLS a Gemini, salida estricta de intención (observar, desplazarse, dialogar, otro). Cliente Godot con botón **Probar Gemini** solo en Windows, sin canon, sin narración NPC ni cambios de Core. Code path implementado. Modelo elegido `gemini-3.5-flash-lite` (estable según documentación oficial del 15/10/2026). **Conexión autenticada real pendiente de clave privada y prueba supervisada**.
3. **P03 sherpa-onnx TTS castellano**: prueba de inferencia REAL separada de Godot en Windows CI con paquete fijado `sherpa-onnx==1.13.8` y modelo público `vits-piper-es_ES-sharvard-medium`, voces 0/1, WAV, duración, factor de tiempo real y SHA-256. Pendiente evidencia CI/escucha MSI. ASR y backend de Godot/Android NO integrados.
4. **P04 CoreRPG**: documentar contrato mínimo de GDExtension + C ABI, sin copiar biblioteca ni desarrollar motor lógico. Esperar coordinación de repo independiente sin detener el resto.
5. **P05 CI**: regresiones NIM-01/NIM-02, NIM-03 parser/seguridad, tests Python, inferencia sherpa, exportación y ABI Windows/Android. **Su estado se verifica con el run del último HEAD, no se anticipa**.
6. **P06 pruebas físicas**: instalar nueva APK (paquete NIM03 distinto); MSI.exe+pck, demo/integración, diagnóstico voluntario con proxy, audio TTS local separado. Android no se considerará conectada a Gemini, Core ni voz hasta ejecución nativa propia.

## Fronteras inviolables
- `interaction_pipeline.gd` sigue bloqueando integración de gameplay con `CORE_NOT_CONNECTED`. El diagnóstico Gemini no es `interpret()` ni `narrate()`, no se mezcla en el pipeline y no crea acciones.
- La clave no se expone al cliente HTTP local, scripts GDScript, GitHub, binarios ni tests.
- El botón de diagnóstico comunica el envío del texto a Google; el servidor bloquea solicitudes con Origin y solo escucha loopback. No es un backend listo para publicación ni para uso multiusuario.
- La tablet ejecuta el videojuego independientemente del MSI. El diagnóstico loopback solo del MSI es una **herramienta técnica**, no dependencia de Android.
- `voice_port.gd` permanece como indisponible mientras no se enlace sherpa local dentro del juego; el WAV de CI NO equivale a una voz NPC.
- No se reproducen mensajes del jugador. La muestra de voz es una frase técnica, no diálogo del canon.

## Criterios de cierre
No declarar NIM-03 cerrada hasta: verde del último HEAD y artefactos verificables, prueba física MSI+S9+ del host, un servicio real con evidencia separada de mocks y autorizado para su alcance, limitaciones documentadas y aprobación explícita de fusión. Si Gemini requiere credencial no suministrada, etiquetar `KEY_REQUIRED`; si falla descarga/modelo nativo, etiquetar `MODEL_OR_DEPENDENCY_PENDING`. **Nunca maquillar estos bloqueos como éxito.**

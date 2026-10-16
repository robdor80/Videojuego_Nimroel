# NIM-03 BUILD — Plan ejecutado, dependencias y límites

Fecha: 2026-10-15. Base comprobada: main @ df43be5b2a62b137b8ed77f7900818e39646c272 (PR #18 NIM-02 integrada). Rama: feat/nim-03-build. **Cierre solicitado por el propietario el 16/10/2026, con excepciones documentadas y autorización de finalizar la fase.**

## Auditoría previa
- NIM-01 (PR #13): Host Godot 4.7.2 Standard, 2D, escritorio y tablet, bocadillos, demo, NIM-01 smoke y exportaciones.
- NIM-02 (PR #18): pipeline v1 de texto, contratos y bloqueo honesto, CI y pruebas manuales MSI/Tab S9+. Su CI aprobada no conectaba servicios.
- Se leyó en CoreRPG/main: `include/corerpg/version.hpp`, `include/corerpg/world_state.hpp`, `CMakeLists.txt`, README y roadmap. Incluye versión 0.1.0, `library_version()`, `WorldState::entity_count()`, `revision()`, `contains()`, `next_entity_id()`; es una biblioteca estática C++20. **No se encontró API C/GDExtension ni matriz Android/NDK integrada.** El README/roadmap tiene notas históricas de 4.8 que no sustituyen al estado del código.
- `Worldbuilding/` y canon quedan intactos. Ningún contenido rico ni percepción 4.9 se supone disponible.

## Objetivo realista y pasos
1. **P01 Auditoría**: main, fusiones, código y dependencias. Completada.
2. **P02 Gemini técnico aislado**: servicio Python ligado a 127.0.0.1 en MSI, clave desde `GEMINI_API_KEY` solo en entorno del proceso; petición HTTPS con TLS a Gemini, salida estricta de intención (observar, desplazarse, dialogar, otro). Cliente Godot con botón **Probar Gemini** solo en Windows, sin canon, sin narración NPC ni cambios de Core. Code path implementado. Modelo elegido `gemini-3.5-flash-lite` (estable según documentación oficial del 15/10/2026). **Conexión REAL verificada en MSI (16/10/2026)**: Gemini 3.5 Flash-Lite clasificó como dialogar y desplazarse; no hay mutaciones del mundo.
3. **P03 sherpa-onnx TTS castellano**: prueba de inferencia REAL separada de Godot en Windows CI con paquete fijado `sherpa-onnx==1.13.8` y modelo público `vits-piper-es_ES-sharvard-medium`, voces 0/1, WAV, duración, factor de tiempo real y SHA-256. **CI superada y ambas voces escuchadas y aprobadas por el propietario**, aunque ligeramente mecánicas. ASR y backend de Godot/Android NO integrados.
4. **P04 CoreRPG**: documentar contrato mínimo de GDExtension + C ABI, sin copiar biblioteca ni desarrollar motor lógico. Esperar coordinación de repo independiente sin detener el resto.
5. **P05 CI**: regresiones NIM-01/NIM-02, NIM-03 parser/seguridad, tests Python, inferencia sherpa, exportación y ABI Windows/Android. **CI verde en commit 8f9bed5, run 38856792436. Revalidar CI del HEAD de cierre documental antes del merge.**
6. **P06 pruebas físicas**: tablet NIM-03 original confirmada por usuario (interfaz y bloqueo Core, no servicio real), MSI comprobado por el usuario: demo e integración, bloqueo Core, fallo seguro sin proxy, conexión real 3.5 y WAV. Se incorpora corrección de teclado Samsung/Bluetooth con prueba geométrica y se requiere una **nueva prueba Android específica** antes de dar ese cambio por validado. Android no se considera conectada a Gemini, Core ni voz.

## Fronteras inviolables
- `interaction_pipeline.gd` sigue bloqueando integración de gameplay con `CORE_NOT_CONNECTED`. El diagnóstico Gemini no es `interpret()` ni `narrate()`, no se mezcla en el pipeline y no crea acciones.
- La clave no se expone al cliente HTTP local, scripts GDScript, GitHub, binarios ni tests.
- El botón de diagnóstico comunica el envío del texto a Google; el servidor bloquea solicitudes con Origin y solo escucha loopback. No es un backend listo para publicación ni para uso multiusuario.
- La tablet ejecuta el videojuego independientemente del MSI. El diagnóstico loopback solo del MSI es una **herramienta técnica**, no dependencia de Android.
- `voice_port.gd` permanece como indisponible mientras no se enlace sherpa local dentro del juego; el WAV de CI NO equivale a una voz NPC.
- No se reproducen mensajes del jugador. La muestra de voz es una frase técnica, no diálogo del canon.

## Criterios de cierre
No declarar NIM-03 cerrada hasta: verde del último HEAD y artefactos verificables, prueba física MSI+S9+ del host, un servicio real con evidencia separada de mocks y autorizado para su alcance, limitaciones documentadas y aprobación explícita de fusión. Si Gemini requiere credencial no suministrada, etiquetar `KEY_REQUIRED`; si falla descarga/modelo nativo, etiquetar `MODEL_OR_DEPENDENCY_PENDING`. **Nunca maquillar estos bloqueos como éxito.**

## Revisión y traspaso de cierre — 16/10/2026

El propietario acuerda dar por concluido el alcance original de NIM-03, sin esperar por los nuevos proveedores de IA. Se cumplen las exportaciones, tests y primer servicio externo auténtico dentro de Godot Windows, más banco TTS externo aceptado. El modo integración de partida NO está conectado a CoreRPG; tampoco hay TTS, narración de NPC ni ASR dentro de Godot.

El ajuste de teclado Samsung/Bluetooth se ha implementado y probado geométricamente en CI, pero **NO se ha verificado físicamente sobre la nueva APK**: se acepta como regresión diferida, no como test superado. Las pruebas funcionales previas de Tab S9+ y Realme ARM64 sí han sido comunicadas y aprobadas por el propietario.

Gemini 3.8 Flash fue reconocido en el catálogo de Google (HTTP 200 y generateContent), pero el servicio devolvió HTTP 503 en varias peticiones mínimas, incluso directamente sin proxy. El modelo no queda validado; revisión puntual posteriormente, sin atribuir la causa a la implementación de Godot.

Mistral Medium 3.5 queda como futuro proveedor candidato, sin clave, sin adaptador y sin validación dentro de Godot; antes de probarlo hace falta comprobar condiciones de la cuenta real, proteger credenciales en backend y crear el adaptador. El saldo gratuito anunciado no se presume garantizado.

Traspaso operativo: Docs/NIM-03_CIERRE_Y_TRASPASO.md. No comenzar NIM-04 desde la rama de NIM-03 sin antes confirmar la fusión de PR #19 a main.

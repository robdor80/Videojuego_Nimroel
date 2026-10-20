# NIM-04 — Auditoría de dependencias CoreRPG/GDExtension y sherpa-onnx

Fecha: 2026-10-16. **Diseño técnico, no implementación nativa.** No se ha conectado ninguna biblioteca C++ a Godot en NIM-04.

## Lectura comprobada del repositorio externo (solo lectura)
- `robdor80/CoreRPG` `main` observado en `d6e2c8fe5a33405bc41b082cf89d6c8036f3c8b8`, fase 4.8.
- `CMakeLists.txt`: biblioteca **STATIC** `CoreRPG`, `C++20`, versión de proyecto `0.1.0`, consumo por headers públicos `include/corerpg`.
- No hay en esa lista pública una ABI C portable/handle opaco o una biblioteca compartida Godot lista para Windows/Android. Esto no descarta desarrollo fuera de `main`; no declarar completadas 4.9, 4.10, 4.12, ni NDK ARM64 por deducción.
- El consumidor Nimroel NO ha cambiado `core_port.gd`: integración de gameplay continúa negándose con `CORE_NOT_CONNECTED`.
- Puntos ya enviados a Codex en `Docs/NIM-03_PEDIDO_CORERPG_CODEX.md`: handle opaco, ownership explícito, consultas read-only y errores sin excepciones cruzando fronteras.

## Dependencias mínimas antes de implementar el puente
1. **Contrato estable en CoreRPG** (otro repositorio, aprobación independiente): `extern "C"` / ABI explícita, versión y capacidades, funciones init/shutdown, consultas read-only, buffers con tamaño, errores enumerados, liberación, integridad de EntityId y snapshot; garantías de no excepción ni ownership de punteros C++ entre módulos.
2. **Win x64**: compilar CoreRPG C++20 con toolchain compatible; GDExtension en Nimroel enlazada con godot-cpp orientado a la API Godot 4.7.2; importación y operaciones de consulta en Host, sin crear otro WorldState.
3. **Android ARM64**: fijar NDK/API nivel/ABI arm64-v8a/libc++/excepciones/RTTI; artefactos `.so` de Core/bridge con dependencias correctas; exportar APK y ejecutar consulta **real** en Tab S9+ sin depender del MSI.
4. **Paridad cross-arch**: serialización de snapshots canónicos, misma revision/ids/contenido en Windows y tablet; estrés de memoria y ciclo suspendido/reanudado Android. Fallos nativos deben dejar UI operativa, sin mutar ni inventar el mundo.
5. **Motor de juego real posterior**: 4.9 visibilidad autorizada, 4.10 verificación de propuestas y 4.12 context builder filtrado antes de dar hechos a los LLM. Solo Core aplica estados.

El proyecto Godot no debe enlazar `CoreRPG STATIC` directamente desde GDScript ni emplear una segunda implementación de `WorldState`. En Godot la extensión compartida es la frontera nativa; dentro puede enlazarse el Core sin contaminar sus headers con Godot. Versionar `godot-cpp` y fijar target de API para pruebas reproducibles. Referencia: https://docs.godotengine.org/en/4.7/tutorials/scripting/cpp/index.html y https://github.com/godotengine/godot-cpp .

## Plan sherpa-onnx para voz local
| Pieza | Estado heredado | Propuesta futura | Condición de aceptación |
| --- | --- | --- | --- |
| Banco TTS WAV castellano | Voz 0 y 1 generadas, escuchadas fuera de Godot | Conservar banco como referencia para comparaciones | La evidencia auditiva heredada no valida audio en juego |
| Reproducción TTS Win | No integrada | Adaptador nativo sherpa C/C++ o puente offline local solo de diagnóstico; transferir PCM a `AudioStreamWAV`/salida de Godot, sin bloquear hilo principal | Frase de prueba no canónica, latencia, memoria y audio audible MSI |
| TTS Android ARM64 | No integrado | Construir librerías nativas y dependencias ONNX arm64-v8a, empaquetado de modelos, ruta de carga writable/user, control de ciclo de vida Android | Audio offline real en Tab S9+ sin MSI, cuantificar tamaño APK/CPU/RAM |
| STT / ASR | No integrado | Captura de micrófono con permiso/consentimiento, buffers de audio para sherpa, transcripción *editable* antes del envío | Grabación/transcripción offline real Win y Tab, latencias, cancelación, permisos |
| Voz NPC | No disponible | Solo texto de NPC de identidad autorizada por Core, voz asignada a NPC y salida idéntica al texto aprobado | Nunca narrar entrada del jugador, sistema demo ni diagnostico |

La documentación sherpa acredita C/C++ y Android ARM64 como objetivos posibles, **no la compatibilidad ya probada con nuestro Host ni un plugin Godot listo**. Referencia: https://k2-fsa.github.io/sherpa/onnx/android/build-sherpa-onnx.html .

## Decisión de ubicación de tareas
- **NIM-04 obligatorio:** conservar puerto de voz como `unavailable`, CI de banco TTS heredado y esta auditoría de dependencias; no bloquear el diagnóstico multiproveedor.
- **Tras contrato nativo CoreRPG:** desarrollar/validar puente GDExtension en fase específica con instrumentación Windows y Android; no reescribir el motor.
- **Fase de voz posterior:** prototipo TTS en Godot Windows, export Android con librerías reales, pruebas físicas, después STT. Los tests acústicos previos se usan como punto de partida, no como prueba de integración.

No se crean `DLL`, `.so`, voces empaquetadas, plugins falsos ni claves de terceros en esta fase documental.


## Política de IA vigente — revisión 20/10/2026

La [política de las tres IA](IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md) asigna **Luna** (diálogo NPC y preguntas off the record al Máster), **Sol 6.1** (presentación detallada de escenas/eventos importantes) y **ChatGPT Plus** (procesamiento externo de ZIP mediante envío y aprobación manual). **CoreRPG conserva la autoridad**; ninguna de estas funciones se implementa por este documento.

La ruta Gemini 3.5/3.8→OpenAI descrita en los planes del 17/10 permanece como **diagnóstico técnico histórico** de NIM-04, no como política de narración en gameplay. `gpt-6-luna` fue seleccionado explícitamente como la Luna oficial verificada y `gpt-6.1-sol` ya se probó con API real en MSI/laboratorios ficticios el 20/10 (issue #29). El broker mantiene consentimiento de pago y fallback desactivados por defecto. Mistral excluido. Ninguna de estas decisiones elimina dependencias de CoreRPG/GDExtension ni altera sherpa-onnx.

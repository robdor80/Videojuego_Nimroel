# NIM-05 BUILD — Plan y criterios de aceptación

Fecha: 17/10/2026. Repositorio: `robdor80/Videojuego_Nimroel`. Rama: `feat/nim-05-build`.
Base comprobada en GitHub: `main` `35c9d22ca3f688c62c709320b20cba565518669d`, PR #21 NIM-04 fusionada. CI del HEAD de NIM-04 (run 38981719349): Godot smoke, sherpa-onnx Windows y exportación Windows/Android **tres jobs correctos**. No equivale a regresión física de los dispositivos ni a integración Core.

## Alcance autorizado

**P01 — Auditoría de continuidad (obligatorio).** Leer y contrastar el código de `Tools/NIM04/provider_proxy.py`, receptor Godot, CI, pruebas, `core_port.gd`, `interaction_pipeline.gd`, voz y `CoreRPG/main`. Mantener una tabla inequívoca: implementado / probado en mocks / probado con API / probado físicamente. No presentar simulaciones como integración.

**P02 — Broker IA robusto (obligatorio, sin red).** Solo `simple: Gemini 3.5 Flash-Lite → GPT-6 Luna` y `complex: Gemini 3.8 Flash → GPT-6 Sol`; Mistral excluido. Respaldo **OFF** por defecto y solo con doble activación `NIMROEL_ENABLE_FALLBACK=1`, `NIMROEL_OPENAI_CONSENT=1`. Nunca realizar aquí llamadas reales. Añadir control de duplicados (identificador de petición efímero), serialización segura de acceso para limitar concurrencia, límites por proceso, recuperación temporal del circuit breaker, timeout y rechazo de salidas no canónicas. Probar explícitamente las carreras y duplicados de diagnóstico pagable. Todos los cambios respetarán clasificador técnico aislado, sin narrativa, NPC ni WorldState.

**P03 — Voz en Godot Windows (experimental y separada).** Prototipo **local, opt-in** que permita generar en tiempo de ejecución una frase técnica no canónica con sherpa-onnx, entregar audio PCM/WAV para escuchar desde Godot sin voz de NPC. Si la cadena no puede ensayarse razonablemente mediante CI, dejarla como prueba local documentada y no marcarla como validada. No alterar `voice_port.gd` a disponible hasta prueba física completa. STT y voz de NPC fuera de NIM-05.

**P04 — Android ARM64 (continuidad).** Mantener exportación y smoke de la APK en CI, sin dependencia del broker Windows ni de PC. **Pendiente explícito**: prueba física de Tab S9+ con teclado Samsung virtual y Bluetooth en APK NIM-05, orientación, historial, envío, IME y recuperación de diseño. No afirmar que funciona en hardware sin prueba humana.

**P05 — CoreRPG (auditoría/preparación documental; sin editar Core).** A fecha de inicio, `CoreRPG/main` `d6e2c8fe5a33405bc41b082cf89d6c8036f3c8b8`: C++20 STATIC (fase 4.8), no ofrece GDExtension ni ABI C estable. Documentar contrato mínimo, ownership, errores, versionado, NDK ARM64, snapshots y paridad. No implementar falsas entidades, ni prometer que 4.9/4.10 están hechas.

## Invariantes de seguridad

- Ningún secreto en GitHub, PCK, APK, EXE ni logs. Proveedor de pago siempre bloqueado salvo consentimiento explícito **de un futuro ensayo controlado**, que no se autoriza en esta fase.
- Broker exclusivamente en `127.0.0.1` Windows, token local y salida del laboratorio técnica. Android sin broker ni API automática.
- `CoreRPG` única autoridad sobre el mundo; `CORE_NOT_CONNECTED` permanece. Modo demo intacto.
- Nada de cambios en `Worldbuilding/`, canon u otros repositorios.
- **No fusionar** la PR; el propietario revisará y hará merge.

## Fases de entrega

1. Auditoría de rutas, riesgos, CI y dependencias. Este plan se publica antes de código.
2. Endurecer broker+contrato Godot, con pruebas negativas offline (duplicados, concurrencia, timeout, 401/403/429/503, consentimiento y recuperación de circuito).
3. Si el P02 está estable, añadir prototipo de voz técnicamente aislado y cubrir su contrato, evitando colisiones con CoreRPG.
4. CI Godot 4.7.2, Python offline, sherpa Windows y export Windows x64 + Android ARM64 sobre HEAD final; comprobar logs y artefactos.
5. Informe de auditoría, fallos conocidos y protocolo manual MSI/Tab. PR Draft sin merge.

## Criterios de cierre

**Verde técnico:** pruebas offline y CI final pasan; cambios fail-closed, sin pagos ni secretos.
**Ámbar pendiente humano:** audio dinámico físicamente audible en MSI y prueba de teclado Tab S9+; no declarar como verde si no se ejecutan.
**Rojo bloqueado:** gameplay Core, NPC, STT, enlace Godot↔GDExtension↔CoreRPG, snapshot nativo cross-arch y pruebas reales de fallback facturable sin nueva autorización.

# NIM-03 — Solicitud lista para conversación CoreRPG/Codex

**Contexto:** consumidor `robdor80/Videojuego_Nimroel`, rama `feat/nim-03-build`. CoreRPG es autoritativo C++20, independiente de Godot y Unreal. Estado de lectura 2026-10-15: main `d6e2c8fe5a33405bc41b082cf89d6c8036f3c8b8`. Proyecto 0.1.0; versión y consultas de entidades ya existen. No implementar aquí lógica duplicada.

## Petición exacta para CoreRPG
1. **Contrato nativo mínimo** documentado (versión ABI >= 1, versión de biblioteca, capabilities, errores estructurados). Diseñar frontera `extern "C"` estable y comprobable, con buffers/cadenas copiados y tamaños explícitos; no filtrar `std::string`, excepciones, `std::span` ni ownership C++ entre módulos; evitar singletons implícitos.
2. **Sesión propia del Core**: handle opaco por instancia, init/shutdown idempotente y consultas `entity_count`, `revision`, `contains(EntityId)`, `next_entity_id` a partir del `WorldState` real que posee CoreRPG. La sesión temporal de prueba no constituye una partida con contenido. No crear `WorldState` nuevo en Godot.
3. **Pruebas C++ nativas**: empty world, identidad estable, iteración read-only, entradas nulas/erróneas, finalización repetida, version mismatch, concurrencia/ownership y garantía de no excepción a través de ABI. Operaciones de creación de entidad SOLO en test Core aislado, sin presentarlas como gameplay.
4. **Windows MSVC x64 + Android NDK arm64-v8a**: fijar versión NDK, API level, C++20, RTTI/excepciones, libc++, PIC, flags de enlace. Ejecutar prueba en ARM64 real (Tab S9+), no dar por validada la plataforma por compilar. Registrar hash del binario, revision y logs, y medir cierre/reanudación.
5. **GDExtension consumidor Nimroel**: preparar recomendación de SDK Godot 4.7.2, ciclo de vida, carga y mensajes sin hacer depender CoreRPG de headers Godot. El bridge host se desarrolla en Nimroel cuando el contrato esté aprobado y se disponga de bibliotecas.

## Versiones y límites
- Versión observada CoreRPG en `CMakeLists.txt`: `0.1.0`; **NO significa** CoreRPG fase funcional 4.10.
- 4.9 Knowledge & Visibility sigue siendo requisito antes de revelar hechos a Gemini. 4.10 acciones antes de mutaciones; 4.12 Context Builder antes de narrativa autorizada.
- GDExtension: elegir ABI/SDL/NDK solo tras prueba, no introducir `libcorerpg.so` placeholder.
- Nimroel Windows y Android deben producir idénticas lecturas para snapshots idénticos, incluyendo pruebas cross-arch de formatos persistentes (4.7/4.8).

**Entrega solicitada a Codex:** propuesta de headers API nativa, decisión de ownership, versión/commit exactos, tests Win/Android con logs, artefactos y lista de cambios estrictamente del repositorio CoreRPG. Abrir PR allí; no realizar merge sin revisión.

**Mientras tanto**, NIM-03 sigue con Gemini diagnóstico y sherpa TTS independientes.

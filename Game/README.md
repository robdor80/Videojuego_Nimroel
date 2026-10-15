# Nimroel RPG — Host 2D conversacional

**Estado 15/10/2026:** NIM-01 PR #13 fusionada; NIM-02 en PR Draft #18, no fusionada. Godot 4.7.2 Standard, interfaz 2D apaisada, base probada visualmente en MSI Windows 11 y Samsung Galaxy Tab S9+.

## Experiencia aprobada
RPG de conversación libre con ilustraciones de ambientación, retratos y bocadillos. Sin necesidad de recorrer un mapa visual ni utilizar hotspots o modelos 3D. La geometría lógica y las aldeas deben generarse proceduralmente y persistir cuando el Core y Content Pack estén disponibles.

Gemini interpreta y redacta el relato; CoreRPG C++20 decide hechos, identidad, acciones y estado; sherpa-onnx es el backend local elegido de ASR y TTS para voces de NPC. Nada de ello está enlazado realmente en esta fase.

## Organización de código
- Host2D/: proyecto Godot con interfaz, laboratorio demo, pipeline de integración bloqueado por seguridad, puertos y tests.
- Interaction/: posibles servicios de producción y conversión de contextos, **aún no implementados**.
- BridgeCoreRPG/: futuro wrapper GDExtension; requiere NDK/Windows y CoreRPG real.
- Content/TreskalV001/: futuro contenido reglado de la prueba V001; no construido en NIM-02.
- Worldbuilding/: canon y recursos; no se modifican para habilitar tests de Host.

## Hitos
- NIM-01: laboratorio y exportables, comprobación física básica en ambos dispositivos.
- NIM-02: contratos, modos demo/integración, CI y paquetes de prueba. La PR requiere revisión humana y no se fusiona automáticamente.
- Integraciones posteriores: P1 CoreRPG Android, fases 4.9/4.10/4.12/4.13, Gemini realmente autenticado y voz sherpa-onnx comprobada.

Referencias: Docs/NIM-02_BUILD_PLAN.md y Docs/NIM-02_CONTRATOS_Y_DEPENDENCIAS.md.

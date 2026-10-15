# Nimroel — Host 2D Godot (NIM-02)

Godot 4.7.2 Standard, renderer GL Compatibility, Windows 11 x64 / Galaxy Tab S9+ Android ARM64, **solo 2D**.

## Estado comprobable
- NIM-01 PR #13 integrada: escritura y bocadillos de demostración ejecutados por el usuario en MSI y Tab S9+.
- NIM-02 PR #18 Draft: la UI usa interaction_pipeline.gd; modo demo y modo integración diferenciados, sin WorldState.
- Ningún motor de gameplay integrado: CoreRPG GDExtension, Gemini autenticado y sherpa-onnx siguen no disponibles.
- CI importa Godot 4.7.2, ejecuta tests NIM-01/NIM-02 y exporta prototipos; no sustituye pruebas de los dispositivos.

## Arranque manual
Desde Godot Standard abrir la carpeta Game/Host2D y ejecutar main.tscn. En modo demo la respuesta del SIMULADOR es determinista. Cambiar a Modo: integración y escribir para observar CORE_NOT_CONNECTED sin acciones de mundo.

## Pruebas de laboratorio
1. godot --headless --editor --path Game/Host2D --import --quit
2. godot --headless --path Game/Host2D --script res://tests/smoke.gd
3. godot --headless --path Game/Host2D --script res://tests/nim02_smoke.gd

Tras la CI de PR, los artefactos NIM02-Godot-Prototype-Windows-Android incluyen exe + pck para MSI y apk ARM64 para Tab S9+, más SHA256SUMS.txt. APK firmado con clave debug temporal; una versión anterior firmada con otra clave puede requerir desinstalación.

## Límites de seguridad
- Nunca guardar claves Gemini ni tokens en GitHub, res:// o APK.
- La demo nunca es un NPC. El puerto CoreRPG no modifica WorldState.
- La voz del jugador no se sintetiza; los futuros NPC pronunciarán exclusivamente textos autorizados.
- No son partidas jugables: no existe un Content Pack Nimroel en ejecución.

Documentos: Docs/NIM-02_BUILD_PLAN.md y Docs/NIM-02_CONTRATOS_Y_DEPENDENCIAS.md. El canon de Worldbuilding/ no se modifica.

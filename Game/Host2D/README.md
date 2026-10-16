# Nimroel — Host 2D Godot (NIM-03 BUILD)

Godot 4.7.2 Standard, GL Compatibility, Windows 11 x64 y Galaxy Tab S9+ Android ARM64, exclusivamente 2D.

## Lo que funciona
- NIM-01 y NIM-02: laboratorio de escritura, bocadillos, historial, interfaz táctil y modo demo determinista. Modo integración conserva bloqueo honesto `CORE_NOT_CONNECTED`.
- NIM-03: botón **Probar Gemini** solo en Windows. **Es un diagnóstico técnico opcional**: envía el texto al proxy loopback del MSI y clasifica intención, si hay clave propia y acceso real a Gemini. No ejecuta jugadas, no crea NPC ni modifica mundo.
- NIM-03: benchmark sherpa-onnx TTS castellano en Tools/NIM03 y CI Windows externa al juego, con audio WAV y métricas. El puerto VoicePort de Godot continúa desconectado.
- CoreRPG GDExtension sigue pendiente del puente nativo en el Core independiente.

## Pruebas Godot
```text
godot --headless --editor --path Game/Host2D --import --quit
godot --headless --path Game/Host2D --script res://tests/smoke.gd
godot --headless --path Game/Host2D --script res://tests/nim02_smoke.gd
godot --headless --path Game/Host2D --script res://tests/nim03_smoke.gd
```
Pruebas Python offline:
`python -m unittest discover -s Tools/NIM03 -p "test_*.py" -v`.

Para probar conexión Gemini real sin clave en APK, véase `Docs/NIM-03_PRUEBAS_Y_ENTREGA.md`. Exportaciones NIM03 CI: `.exe` + `.pck` y `.apk` ARM64 en artefactos de la PR Draft. NIM03 Android utiliza otro identificador de paquete que NIM02.

Nimroel no es aún una partida persistente; la ejecución de los tests y del benchmark no acredita una partida ni voz de NPC. Nunca usar IA como fuente de verdad fuera de CoreRPG.

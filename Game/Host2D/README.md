# Nimroel · NIM-01 Host 2D

**Estado:** primer prototipo de interfaz Godot; conversación y mundo **simulados**. No integra Gemini, CoreRPG, sherpa-onnx, ASR ni síntesis. No es la v0.0.1 jugable.

## Herramientas
- Godot **4.7.2 Standard**, edición sin .NET.
- Windows MSI: Editor Godot para Windows. Desde Godot, abrir la carpeta \`Game/Host2D\`, importar SVG y ejecutar el proyecto con F6/F5.
- Android Tab S9+: exportación futura del **mismo proyecto** con perfil ARM64. No se proclama soporte Android hasta compilar/instalar un APK y probarlo.
- La interfaz de pantalla usa imágenes SVG **provisionales**, no assets de canon ni mapas de aldea generados.

## Pruebas reproducibles (sin claves)
Importar y verificar scripts:

\`\`\`sh
godot --headless --editor --path Game/Host2D --import --quit
\`\`\`

Ejecutar las pruebas:

\`\`\`sh
godot --headless --path Game/Host2D --script res://tests/smoke.gd
\`\`\`

La CI hace estas mismas comprobaciones con binario oficial Godot 4.7.2 en Ubuntu. Una CI verde prueba importación/parsing y demo, **no compila Windows ni Android**.

## Interfaz
- Imagen de ambientación de ejemplo.
- Caja de texto libre + botón Enviar.
- Historial de jugador y simulador claramente etiquetados.
- Control de reiniciar la demostración y retrato provisional en intención de conversación.
- Nunca se modifica un \`WorldState\`; \`demo_gateway.gd\` es únicamente un clasificador fijo para ejercitar la UI.

## Integraciones que no deben falsificarse
- **Gemini:** interpretación y narración de acuerdo con contratos versionados; nunca simular generación libre y presentarla como IA real.
- **CoreRPG:** único mundo autoritativo; bridge C++ GDExtension por plataforma y Content Pack Nimroel real solo cuando esté preparado.
- **sherpa-onnx:** modelo ASR de castellano para entrada hablada y TTS local para respuestas NPC; voz de jugador no se sintetiza. No incluir modelos binarios ni licencias sin evaluación.
- Android solo **Samsung Galaxy Tab S9+**; pruebas de micrófono, APK, permisos, rendimiento y audio requieren dispositivo real.

## Seguridad
No incorporar claves API en el repositorio, export templates, assets \`res://\` o APK distribuido. La eventual distribución a terceros requiere una solución de credenciales apropiada. El prototipo actual no hace peticiones externas.

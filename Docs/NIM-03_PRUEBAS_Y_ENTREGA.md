# NIM-03 — Pruebas y guía reproducible

## Estado de evidencia (no confundir)
| Función | Código | CI de último HEAD | Servicio real | MSI físico | Tab S9+ física |
| --- | --- | --- | --- | --- | --- |
| Host 2D NIM-01/NIM-02 | Sí | Pendiente de comprobar run | Demo local | NIM-02 validado | NIM-02 validado |
| Gemini diagnóstico clasificación (fuera de gameplay) | Sí | Tests negativos/mocks pendientes | Requiere GEMINI_API_KEY + prueba de Google | Pendiente | No implementado |
| sherpa-onnx TTS castellano benchmark | Sí | Inferencia Windows CI pendiente | Pendiente de resultado WAV/JSON | Pendiente | No integrado |
| sherpa-onnx ASR, voz dentro de Godot | No | No | No | No | No |
| CoreRPG GDExtension | No | No | No | No | No |

Estos estados se actualizan **solo con evidencias**. CI Godot valida código y exportación: nunca sustituye dispositivos físicos. El test de proxy en unittest utiliza clasificador fake y **no acredita llamadas a Gemini**.

## Prueba Gemini en el MSI (voluntaria; nunca meter claves en GitHub)
Se necesita Python 3.10+ y una clave propia de Gemini con acceso al modelo elegido. La app siempre funciona en demo sin clave.

1. Abre PowerShell en la raíz de tu copia local del repositorio actualizado a la rama NIM-03.
2. Establece la clave **solo en el proceso local** (no se guarda en disco, \`.env\`, \`res://\` ni APK):
   \`\`\`powershell
   $segura = Read-Host "Clave privada de Gemini" -AsSecureString
   $p = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($segura)
   try { $env:GEMINI_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($p) }
   finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($p) }
   python Tools/NIM03/gemini_diagnostic_proxy.py
   \`\`\`
3. Arranca el NIM-03 .exe con su .pck junto. Introduce \`Hablo con un aldeano\` y pulsa **Probar Gemini**. El botón informa del envío de **ese texto** a Google. Debe aparecer una etiqueta técnica y un aviso de no-partida; nunca respuesta NPC.
4. Cambia a **Modo: integración** y envía el texto. Debe seguir mostrando \`CORE_NOT_CONNECTED\` aunque el diagnóstico técnico funcione.
5. Cierra el servidor; repite el botón. Debe fallar de forma explícita. Prueba demo y reinicio. Repite con texto vacío y mayor de 500 caracteres, sin envío.
6. Guarda evidencia: commit, fecha, modelo, salida \`/health\` sin secretos, captura, errores y costes si existen. **No pegar la clave en ninguna captura o documento**.

No expongas el puerto 8765 a red ni uses la tablet para llamar al proxy; Android requiere un futuro servicio HTTPS autenticado y política explícita para no exponer texto o credenciales.

## sherpa-onnx TTS en Windows — inferencia real, sin clave ni conexión
La CI Windows instala \`sherpa-onnx==1.13.8\`, descarga el modelo oficial
\`https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-es_ES-sharvard-medium.tar.bz2\`,
ejecuta dos voces, sube WAV y \`nim03_tts_metrics_speaker_*.json\`.
Este banco usa una frase técnica y **no está conectado a Godot**. Fuente del modelo:
\`https://k2-fsa.github.io/sherpa/onnx/tts/all/Spanish/vits-piper-es_ES-sharvard-medium.html\`.

MSI manual: instala \`pip install sherpa-onnx==1.13.8 numpy\`; descarga y extrae el modelo en una carpeta local ajena a GitHub, y ejecuta:
\`\`\`powershell
python Tools/NIM03/voice_tts_bench.py --model-dir "RUTA\MODELO\vits-piper-es_ES-sharvard-medium" --output-dir "$env:TEMP\nim03-tts" --speaker 0
python Tools/NIM03/voice_tts_bench.py --model-dir "RUTA\MODELO\vits-piper-es_ES-sharvard-medium" --output-dir "$env:TEMP\nim03-tts" --speaker 1
\`\`\`
Escucha los WAV y registra duración, latencia, factor de tiempo real y SHA256. No cometas WAV/modelos ni grabaciones de voz del usuario. TTS positivo en Windows CI no significa TTS Android.

## APK
La exportación NIM-03 usa paquete \`org.nimroel.rpg.nim03\` para coexistir con el APK NIM-02; estará firmado solo para depuración. En Tab S9+, probar arranque, giro, teclado, historial, demo, integración bloqueada, reinicio y reanudación. No habrá botón de diagnóstico Gemini móvil y no hay todavía micrófono/voz local.

## Aceptación de PR
Se debe revisar la CI del **último SHA de rama**, el artefacto de exportación y el WAV/JSON real. Si falla un job, no presentar la PR como validada. Se espera revisión humana y aprobación explícita antes del merge. 

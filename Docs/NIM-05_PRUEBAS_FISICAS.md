# NIM-05 — Ensayos físicos de aceptación (MSI y Tab S9+)

**No ejecutar llamadas OpenAI ni activar fallback de pago.** Este protocolo no requiere credenciales de Gemini/OpenAI, ni saldo. Todos los textos de prueba son inventados. Ninguna captura debe incluir `NIMROEL_LOCAL_TOKEN` ni claves API.

## A. Prueba Windows — audio dinámico sherpa-onnx en Godot

Requiere descargar de la CI NIM-05 los artefactos del HEAD final: `Nimroel_NIM05_Windows.exe` y su `.pck` juntos. Requiere Python 3.11 o 3.12 x64 en MSI (el runner usa 3.11), altavoces activos, conexión a internet solo durante **instalación** y descarga del modelo público. No se utiliza API pagable.

1. En PowerShell, desde raíz del repositorio, comprobar `py -0p`. Crear entorno independiente con versión disponible y ejecutar:

   ```powershell
   py -3.12 -m venv "$env:LOCALAPPDATA\NimroelTTS-venv"
   $python = "$env:LOCALAPPDATA\NimroelTTS-venv\Scripts\python.exe"
   & $python -m pip install "sherpa-onnx==1.13.8" numpy
   ```
   Si se dispone de 3.11 en lugar de 3.12, sustituir `py -3.12` por `py -3.11` en la primera línea.

2. Descargar **una vez**, a carpeta privada del MSI, el modelo castellano ya usado por CI:

   ```powershell
   $models = "$env:LOCALAPPDATA\NimroelTTS-models"
   New-Item -ItemType Directory -Force -Path $models | Out-Null
   curl.exe --fail --location --retry 3 --output "$models\model.tar.bz2" "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-es_ES-sharvard-medium.tar.bz2"
   tar.exe -xjf "$models\model.tar.bz2" -C $models
   $modelDir = "$models\vits-piper-es_ES-sharvard-medium"
   Test-Path "$modelDir\es_ES-sharvard-medium.onnx"
   ```
   La última instrucción debe devolver `True`. No subir el modelo a GitHub.

3. En **la misma PowerShell** generar el token local y poner explícitamente a cero cualquier prueba de IA facturable:

   ```powershell
   $env:NIMROEL_LOCAL_TOKEN = [guid]::NewGuid().ToString("N")
   $env:NIMROEL_ENABLE_FALLBACK = "0"
   $env:NIMROEL_OPENAI_CONSENT = "0"
   Remove-Item Env:OPENAI_API_KEY -ErrorAction SilentlyContinue
   $tts = Start-Process -FilePath $python -ArgumentList ('Tools/NIM05/tts_local.py --model-dir "' + $modelDir + '"') -PassThru -NoNewWindow
   ```
   Dejar ejecutándose el servicio local. No hace falta levantar `provider_proxy.py`.

4. Lanzar `Nimroel_NIM05_Windows.exe` desde esta misma PowerShell, junto a su `.pck`, por ejemplo:
   ```powershell
   Start-Process ".\Game\Host2D\export\Nimroel_NIM05_Windows.exe"
   ```
   Usar la ubicación real de los artefactos extraídos si es distinta.

5. Con los altavoces activos, dejar la caja de texto vacía y pulsar **Escuchar TTS local**. Debe oírse la frase técnica castellana generada en ese momento y aparecer un mensaje de laboratorio, **no un NPC**. Escribir después `Esta segunda frase también se sintetiza ahora mismo.` y pulsar de nuevo; debe sonar esta segunda frase distinta.
6. Como prueba negativa, cerrar el servicio con `Stop-Process -Id $tts.Id` y volver a pulsar el botón. Debe indicar `TTS_SERVER_NOT_CONNECTED` o similar, sin bloquear la demo. Comprobar que **Modo: integración** sigue diciendo `CORE_NOT_CONNECTED`.
7. Anotar: versión de Windows, fuente del EXE/PCK y su SHA, si las dos frases son audibles, retardo aproximado percibido, CPU/RAM (opcional), error al detener servicio. No registrar audio o frases privadas en repositorios.

**Condición de éxito:** inferencia reproducida y audible *dentro de Godot Windows*, distinta según texto ingresado. El archivo WAV de CI por sí solo **no basta**.

## B. Prueba Android nativa — Samsung Galaxy Tab S9+

1. Descargar exclusivamente `Nimroel_NIM05_TabS9Plus.apk` del artefacto final de la CI NIM-05; comparar con `SHA256SUMS.txt` si está disponible.
2. Instalar la APK en la Tab S9+ (guardar/cerrar antes la instalación anterior si contiene datos de interés). Confirmar que arranca sin conexión con el MSI, sin ordenador y sin broker.
3. **Teclado virtual Samsung**: enfocar caja, escribir `Hola desde la tablet`, pulsar Enviar, abrir/cerrar teclado, desplazarse por historial; confirmar que controles no quedan ocultos y el layout se recupera.
4. **Teclado Bluetooth**: conectar el teclado, escribir y enviar un mensaje, desplazar el historial; desconectar y repetir con teclado virtual. Comprobar que no queda espacio muerto de IME.
5. Probar rotación según configuración de la app y reinstaurar estado. No deben aparecer botones de proveedores IA ni laboratorio de voz Windows.
6. Pulsar **Modo: integración** y enviar algo: resultado esperado `CORE_NOT_CONNECTED`, sin NPC real ni mutación de estado.

**Condición de éxito:** funcionamiento autónomo Android ARM64 y regresión humana de ambos teclados, historial, botón enviar y recuperación visual. Un APK generado por CI **no certifica** este resultado.

## C. Qué NO probar en esta fase

- No establecer `NIMROEL_OPENAI_CONSENT=1` ni `NIMROEL_ENABLE_FALLBACK=1`. La conmutación real pagable exige nueva autorización explícita.
- No simular una escena de NPC real con este banco TTS.
- No afirmar que existe CoreRPG Android por arrancar la APK.
- No instalar modelos en la tablet ni ejecutar el servidor TTS Windows sobre ella: el soporte nativo ARM64 queda pendiente.

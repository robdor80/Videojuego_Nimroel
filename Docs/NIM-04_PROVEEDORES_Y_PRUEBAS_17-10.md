# NIM-04 — Protocolo de proveedor real y pruebas (17/10/2026)

**Protocolo y registro de pruebas:** el 16/10/2026 se confirmó una llamada autenticada real a Gemini 3.8 **directamente desde PowerShell en MSI** (fuera del broker y de Godot); ver evidencia al final del apartado Gemini. Durante la preparación del broker NIM-04 no se emplearon credenciales reales ni se realizaron llamadas a Mistral. El broker y el Host son diagnósticos; CoreRPG NO está conectado.

## Modelos fijados para comparación
| Nivel | Prioridad de partida | Alternativa candidata | Estado |
|---|---|---|---|
| sencilla | Gemini `gemini-3.5-flash-lite` | Mistral Small 4 `mistral-small-2603` | Gemini 3.5 verificado previamente solo en NIM-03; nuevo broker sin verificación real |
| exigente | Gemini `gemini-3.8-flash` | Mistral Medium 3.5 `mistral-medium-3-5` | Gemini 3.8 probado con generación directa autenticada PowerShell/MSI el 16/10; ambos adaptadores NIM-04 siguen sin prueba remota |

Los nombres Mistral son IDs específicos documentados. Los alias `mistral-small-latest` y `mistral-medium-latest` existen, pero **NO** se usan en código: la documentación oficial avisa de posibles cambios silenciosos. Referencias:
- https://docs.mistral.ai/models/mistral-small-4-0-26-03
- https://docs.mistral.ai/models/mistral-medium-3-5-26-04
- https://docs.mistral.ai/inference/model-lifecycle

**No asumir que Gemini y Mistral tienen capacidad narrativa equivalente.** El laboratorio actual solo clasifica intención. Una futura comparación narrativa necesita corpus de prueba inventado/no canónico, rubricado por precisión, alucinaciones, privacidad, latencia, idioma y precio, sin WorldState.

## Cuenta de Mistral — comprobaciones manuales
1. Abrir https://console.mistral.ai/ o el acceso oficial a Studio; comprobar el plan Free de la organización y su apartado de límites/uso: solicitudes por segundo, tokens/minuto, tokens/mes y **saldo asignado a tu cuenta real**. La página pública anuncia USD 10/mes API en Free, pero esta cifra no demuestra que esa bolsa esté acreditada en una cuenta particular. No activar PAYG ni introducir tarjeta sin decisión explícita.
2. En la consola de administración abrir **Privacy**; en **Anonymous improvement data**, desactivar el uso de llamadas API y datos relacionados para mejora/entrenamiento si se desea preservar el material. El ajuste de Vibe/Le Chat es independiente. El modo Free puede permitir entrenamiento salvo opt-out; *opt-out* no equivale a Zero Data Retention.
3. Crear en Studio una workspace y una clave nueva exclusivamente para Nimroel, con nombre/expiración si la interfaz lo permite. Guardarla en un gestor de contraseñas: aparece una única vez. Verificar que Small 4/Medium 3.5 están disponibles en la organización y si requieren habilitación.
4. Zero Data Retention: **no disponible por defecto en Free**; requiere Pay-as-you-go y solicitud aceptada para llamadas compatibles (p. ej. chat completions). No enviar canon sensible hasta evaluar el tratamiento de datos.
Fuentes oficiales: https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key ; https://docs.mistral.ai/admin/billing-usage/usage-limits ; https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training ; https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr

## Prueba Windows MSI — sin claves en Godot, EXE, APK ni GitHub
Con `python3` o `python` 3.10+ y Windows, instalar la rama NIM-04 en el MSI y ejecutar PowerShell desde la raíz del repositorio. La clave solo debe almacenarse en variables **del proceso** y no en ficheros, capturas, argumentos CLI ni perfiles del sistema. El botón solo envía el texto visible de la caja al proveedor seleccionado. **Usar exclusivamente una frase de prueba inventada, no canon privado**.

```powershell
# Testear Gemini sin exponer la clave
$secreto = Read-Host "API key Gemini (privada)" -AsSecureString
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secreto)
try { $env:GEMINI_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr) }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }

# Para probar Mistral, repetir con otra clave, independiente
$secreto = Read-Host "API key Mistral (privada)" -AsSecureString
$ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secreto)
try { $env:MISTRAL_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr) }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr) }

# Token local aleatorio compartido por el broker y la app Windows.
# No forma parte de los binarios ni es la credencial de ningún proveedor.
$env:NIMROEL_LOCAL_TOKEN = [guid]::NewGuid().ToString("N")
$env:NIMROEL_PRIMARY_PROVIDER = "mistral" # o "gemini"; default = gemini
$env:NIMROEL_ENABLE_FALLBACK = "0"        # solo 1 tras aceptar costes/privacidad
$broker = Start-Process python -ArgumentList "Tools/NIM04/provider_proxy.py" -PassThru -NoNewWindow
# Arrancar desde la MISMA sesión PowerShell el Windows EXE NIM-04 (con .pck al lado)
Start-Process ".\Game\Host2D\export\Nimroel_NIM04_Windows.exe"
```

En el Host de Windows, sin entrar en modo integración, escribir `Hablo con un aldeano`, elegir **Sencilla** y pulsar **Probar proveedores**. Debe mostrarse proveedor, modelo, clasificación y latencia. Cambiar a **Exigente** y repetir. La demostración y el bloqueo `CORE_NOT_CONNECTED` deben seguir funcionando aunque el broker no exista.

Para la comparación individual repetir iniciando el broker con `NIMROEL_PRIMARY_PROVIDER` `gemini` / `mistral` y fallback `0`. Solo **después** de validar los dos adaptadores, habilitar `NIMROEL_ENABLE_FALLBACK=1` si se aprueban sus posibles peticiones a otro proveedor. El broker aplica máximo **30 peticiones a proveedores por ejecución** (incluidos segundos intentos) y **no realiza reintentos** dentro de cada proveedor.

Al terminar: `Stop-Process -Id $broker.Id`, cerrar el juego y eliminar con `Remove-Item Env:GEMINI_API_KEY,Env:MISTRAL_API_KEY,Env:NIMROEL_LOCAL_TOKEN -ErrorAction SilentlyContinue`. No persistir la sesión. **El puerto 8766 escucha solo 127.0.0.1, exige token local y no acepta Origin del navegador; no es un backend público HTTPS para Android.** Se requiere conexión a Internet del MSI exclusivamente para las pruebas reales.

## Prueba puntual Gemini 3.8
- Repetir una **sola** clasificación corta con nivel exigente, proveedor Gemini, fallback `0`. Anotar HTTP de generación, fecha, modelo, hora local, latencia y petición facturable si está disponible.
- Si aparece de nuevo `HTTP 503 UNAVAILABLE`, permitir **como máximo un segundo ensayo diferido**, no insistir indefinidamente; registrar `EXTERNAL_UNAVAILABLE`. No confundir ausencia de 429 con acceso garantizado ni suponer causa.
- Si responde, contrastar la salida de la misma frase desde Godot y el broker. Resultado 200 verificado + salida válida = *clasificación diagnóstica*, no narrativa, CoreRPG ni gameplay.

### Evidencia de reintento Gemini 3.8 — 16/10/2026
- **Origen:** salida de PowerShell en MSI aportada por el propietario; no es un log de CI ni una prueba ejecutada por GitHub/Godot.
- **Clave:** `GEMINI_API_KEY` cargada únicamente en el entorno local, confirmada presente. **No se recoge valor ni se incluye ningún secreto.**
- **Endpoint:** Google Generative Language API `v1beta/models/gemini-3.8-flash:generateContent`, encabezado `x-goog-api-key`, JSON con `contents/parts/text`.
- **Primera llamada:** HTTP **400** por un bloque de PowerShell pegado incorrectamente que no construyó bien la variable `$body`; **no** equivale a un 503 del proveedor.
- **Segundo intento con JSON literal válido:** **ÉXITO**, texto del modelo **`GEMINI FUNCIONA`** (petición completada; HTTP 200 implícito por `Invoke-RestMethod` sin excepción). Esto verifica generación real autenticada con ese modelo, no disponibilidad permanente ni su funcionamiento en el broker NIM-04, Godot, modo narrativo, NPC o CoreRPG.
- **Latencia, tokens y coste:** no medidos en esta ejecución; requieren toma explícita de datos. El 503 anterior no se reprodujo con la petición corregida, **sin atribuir causa**.
- **Pendiente NIM-04:** ensayo del broker `provider_proxy.py` con `tier=complex`, proveedor principal `gemini`, fallback deshabilitado, y visualización en Godot Windows. Conservar límite de peticiones y privacidad.

### Ensayos posteriores de clasificación — 16/10/2026

Evidencia proporcionada por el usuario desde PowerShell MSI, no pruebas ejecutadas por GitHub:
- **Broker NIM-04 (código anterior)**: POST autenticado a `127.0.0.1:8766/v1/provider-probe` con `tier=complex`, `text="Hablo con un aldeano"`, fallback `0`; respondió **HTTP local 503** `PROVIDERS_TEMPORARILY_UNAVAILABLE`. El HTTP 503 **lo produce el broker**: no acredita que Google respondiese 503; la implementación anterior agrupaba timeouts, errores de red y HTTP 429/503.
- **Petición directa Google con schema JSON y temperature 0**: timeout desde PowerShell al cabo de ~53 segundos con `-TimeoutSec 45`; sin respuesta remota ni código HTTP confirmado.
- **Petición directa Google con responseMimeType JSON y sin schema ni temperature**: otro timeout desde PowerShell con `-TimeoutSec 35`; sin respuesta ni HTTP remoto confirmado. Por ello no se demuestra que el schema o temperature causen el timeout por sí solos.
- El mensaje posterior `finally : El término 'finally' no se reconoce` es sintaxis de PowerShell por ejecutar `finally` separadamente de `try/catch`; no es respuesta de Google.
- **Intervención en rama NIM-04 pendiente de ensayo remoto:** para `gemini-3.8-flash`, `thinkingConfig.thinkingLevel="low"`, retirada de `temperature`, `maxOutputTokens=512`, timeout de broker **22 s** frente a 12 s anterior (Godot tiene 28 s), respuesta técnica `diagnostic_reason` solo con valores seguros como `timeout`, `network_error` o `http_503`. El modo JSON y la validación estricta de intención permanecen. Cambios basados en documentación Google oficial: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8 y https://ai.google.dev/gemini-api/docs/generate-content/thinking .
- **La modificación no es una prueba exitosa real**, no garantiza menor latencia ni disponibilidad. Requiere reiniciar el broker Python anterior y cargar nueva versión del script, antes de **un único** nuevo ensayo remoto con consentimiento. No se modificó `main`, CoreRPG ni el canon.

## Matriz de evidencias (separando prueba directa y pruebas de integración)
| Caso | Resultado hoy | Latencia | Consumo/coste | Observación |
|---|---|---|---|---|
| Gemini 3.5 / sencilla, broker NIM-04 | PENDIENTE | — | — | No heredar como test de broker la prueba NIM-03 |
| Mistral Small 4 / sencilla | PENDIENTE | — | — | Free y acceso del modelo |
| Gemini 3.8 / exigente, llamada directa PowerShell MSI | **ÉXITO REAL — 16/10**, texto `GEMINI FUNCIONA` | No medida | No medido | JSON válido; API real autentificada, sin broker ni Godot |
| Gemini 3.8 / exigente, broker NIM-04 anterior | FALLÓ: 503 **local** genérico | 12 s configurados; sin métrica medida | No medido | No identifica HTTP remoto ni causa exacta |
| Gemini 3.8 / exigente, Google directo clasificación | TIMEOUT en dos ensayos (JSON schema y JSON simple) | ~53 s primero; >35 s segundo | No medido | No demuestra fallo de disponibilidad ni de schema exclusivamente |
| Gemini 3.8 / exigente, broker corregido + Godot | PENDIENTE | — | — | Requiere versión nueva y prueba física MSI |
| Mistral Medium 3.5 / exigente | PENDIENTE | — | — | Acceso/coste |
| Alternancia en error simulado | SOLO UNIT TEST OFFLINE | — | 0 | No acredita outage real |
| Cambio de proveedor remoto real | PENDIENTE | — | — | Requiere autorización explícita |

## Tablet Tab S9+ — requisito diferido
Descargar la APK `Nimroel_NIM04_TabS9Plus.apk` desde la CI del SHA final, verificar que corresponde al commit y el paquete `org.nimroel.rpg.nim04`. Con teclado Samsung virtual: escribir, leer historial, pulsar Enviar, ocultar teclado y confirmar que cabecera/retrato/pie reaparecen; con Bluetooth: escribir sin IME visible y comprobar que mantiene tamaño completo; alternar ambos con texto conservado. Repetir demo/integración y reanudación. El nuevo panel de proveedores solo existe en Windows; tablet **no** puede llamar a la API.

## Futuro fuera del laboratorio
- Núcleo narrativo real: solo tras WorldState y APIs de conocimiento/acciones CoreRPG (4.9/4.10/4.12) y puente nativo ABI/GDExtension probado Windows+ARM64. Ningún LLM aplica directamente cambios ni inventa hechos autorizados.
- sherpa-onnx TTS: audio de NPC solo después de identidad/voz autorizada; validar reproducción en Godot Windows y después runtime Android real. STT/ASR por micrófono, permisos y tratamiento local en iteración separada.

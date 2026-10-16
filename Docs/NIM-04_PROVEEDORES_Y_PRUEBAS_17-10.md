# NIM-04 — Protocolo de proveedor real y pruebas (17/10/2026)

**Protocolo y registro de pruebas:** el 16/10/2026 se confirmó una llamada autenticada real a Gemini 3.8 **directamente desde PowerShell en MSI** (fuera del broker y de Godot); ver evidencia al final del apartado Gemini. Durante la preparación del broker NIM-04 no se emplearon credenciales reales ni se realizaron llamadas a Mistral. El broker y el Host son diagnósticos; CoreRPG NO está conectado.

## OpenAI: preparativo y contrato técnico de respaldo (17/10/2026)

**Hechos de cuenta vistos en capturas del usuario:** proyecto de OpenAI Platform `Nimroel-RPG` creado; usuario confirma que generó y guardó la clave (no recibida por el asistente ni almacenada en GitHub); facturación `Pay as you go`, **5,00 USD de saldo**, `Auto-reload is OFF`. Esto **no** equivale a una llamada API validada ni a disponibilidad de cada modelo.

**Adaptador offline añadido al broker NIM-04**, implementado con la [Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create), `store: false`, clasificación como etiqueta única de cuatro valores, sin herramientas, sin WorldState ni respuesta narrativa:

| Nivel | Primario gratis | Respaldo OpenAI facturable |
|---|---|---|
| `simple` / Sencilla | `gemini-3.5-flash-lite` | `gpt-6-luna` |
| `complex` / Exigente | `gemini-3.8-flash` | `gpt-6-sol` |

En esta iteración se utiliza **`gpt-6-sol`**, modelo con identificador fijo, no un alias `latest`. La elección de `gpt-6.1-sol` queda para evaluación explícita posterior. Mistral permanece para pruebas directas, no forma parte del fallback automático.

**Guardias obligatorias para evitar gasto involuntario:** `OPENAI_API_KEY` solo en entorno del proceso broker, `NIMROEL_OPENAI_CONSENT=1` requerido para cualquier invocación OpenAI; `NIMROEL_ENABLE_FALLBACK=1` requerido adicionalmente para fallback desde Gemini (valor por defecto deshabilitado); límite `MAX_PAID_PROVIDER_CALLS=4` por proceso de laboratorio y `MAX_PROVIDER_CALLS=30` total; cada solicitud pide hasta 256 tokens de salida y limita la entrada a 500 caracteres. La cuota de llamadas **no es un presupuesto monetario**; para una futura aplicación real se necesita control estricto de costes y servidor seguro. `OPENAI_API_KEY` no debe incluirse en APK, PCK, EXE, commits ni capturas.

**Incidencia real de integración del 17/10/2026:** el usuario ejecutó Nimroel NIM-04 en MSI con `NIMROEL_PRIMARY_PROVIDER=openai`, consentimiento de pago explícito, `Sencilla`, texto `Hablo con un aldeano` y broker `/health = ready`. La UI mostró `INVALID_DIAGNOSTIC_RESPONSE`. Inspección del receptor `Game/Host2D/scripts/provider_diagnostic.gd`: la whitelist `MODELS` solo incluía Gemini/Mistral, por lo que una respuesta 200 del broker con `source=openai` y `model=gpt-6-luna` se rechazaba. **Esta captura por sí sola no certifica modelo OpenAI validado en Godot**, pero identifica un defecto de parseo local (no un HTTP remoto 429). Se amplió whitelist de modelos por nivel, códigos seguros de error de pago y regresiones `nim04_smoke.gd`. **Pendiente descargar el EXE nuevo de CI y repetir solo una prueba para cerrar E2E**; el EXE antiguo no contiene esa corrección. No se ha comprobado el coste descontado del saldo. No reintentar usando el binario antiguo.

**Validación real de OpenAI GPT-6 Luna en Godot Windows — 17/10/2026.** Tras regenerar el EXE con la corrección de whitelist (GitHub Actions 38980077304, todos los jobs verdes), el usuario ejecutó Godot en MSI heredando el entorno local del broker, seleccionó `Sencilla` y envió `Hablo con un aldeano` al laboratorio `Probar proveedores`. **Captura real mostrada por el usuario**: `openai / gpt-6-luna`, `Intención: dialogar · 1531 ms`, `No es respuesta NPC ni modifica el mundo`. **Resultado E2E: ÉXITO REAL** de selección de proveedor, solicitud Responses API, parseo de clasificación y representación Godot para Luna. El modelo devolvió una etiqueta técnica, no generó narrativa ni afectó CoreRPG. El consumo monetario exacto no se ha comprobado en el panel de facturación; el saldo total prepagado era 5,00 USD antes de la prueba. **GPT-6 Sol también validado realmente el 17/10/2026, ver registro a continuación.** No hay nuevas credenciales en el repositorio.

**Validación real de OpenAI GPT-6 Sol en Godot Windows — 17/10/2026.** El usuario cambió el laboratorio de `Sencilla` a `Exigente` en el EXE corregido, mantuvo el texto `Hablo con un aldeano` y pulsó `Probar proveedores`. **Captura real del usuario:** `openai / gpt-6-sol`, `Intención: dialogar · 1391 ms`, `No es respuesta NPC ni modifica el mundo`. **Resultado E2E: ÉXITO REAL** de conexión técnica y clasificación OpenAI Sol dentro de Godot. Comparativa de estas muestras aisladas: Luna 1531 ms y Sol 1391 ms; no representa una medición de rendimiento estadística ni compara calidad narrativa. El coste exacto debitado aún no se ha consultado. No se han conectado NPC ni WorldState; Gemini→OpenAI de respaldo automático sigue pendiente de prueba real controlada, con consentimiento y cupo.

**Pruebas sin coste (offline)** en `Tools/NIM04/test_openai_adapter.py`: ruta exacta, `store=false`, parseo fail-closed, consentimiento requerido, tope local y selección gemini→OpenAI. **Pendiente** validar CI y dos peticiones **reales** dentro de Godot Windows, una a Luna y otra a Sol, con autorización/consentimiento controlado por el usuario. No inferir calidad narrativa de un clasificador de intención. PR #21 permanece Draft sin fusión.

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
- **Situación posterior:** el ensayo del broker con `tier=complex`, proveedor `gemini` y fallback deshabilitado, y la visualización en Godot Windows, quedaron validados posteriormente (véase «Validación positiva Godot + Gemini 3.8»). Mantener límites y privacidad.

### Ensayos posteriores de clasificación — 16/10/2026

Evidencia proporcionada por el usuario desde PowerShell MSI, no pruebas ejecutadas por GitHub:
- **Broker NIM-04 (código anterior)**: POST autenticado a `127.0.0.1:8766/v1/provider-probe` con `tier=complex`, `text="Hablo con un aldeano"`, fallback `0`; respondió **HTTP local 503** `PROVIDERS_TEMPORARILY_UNAVAILABLE`. El HTTP 503 **lo produce el broker**: no acredita que Google respondiese 503; la implementación anterior agrupaba timeouts, errores de red y HTTP 429/503.
- **Petición directa Google con schema JSON y temperature 0**: timeout desde PowerShell al cabo de ~53 segundos con `-TimeoutSec 45`; sin respuesta remota ni código HTTP confirmado.
- **Petición directa Google con responseMimeType JSON y sin schema ni temperature**: otro timeout desde PowerShell con `-TimeoutSec 35`; sin respuesta ni HTTP remoto confirmado. Por ello no se demuestra que el schema o temperature causen el timeout por sí solos.
- El mensaje posterior `finally : El término 'finally' no se reconoce` es sintaxis de PowerShell por ejecutar `finally` separadamente de `try/catch`; no es respuesta de Google.
- **Intervención en rama NIM-04 pendiente de ensayo remoto:** para `gemini-3.8-flash`, `thinkingConfig.thinkingLevel="low"`, retirada de `temperature`, `maxOutputTokens=512`, timeout de broker **22 s** frente a 12 s anterior (Godot tiene 28 s), respuesta técnica `diagnostic_reason` solo con valores seguros como `timeout`, `network_error` o `http_503`. El modo JSON y la validación estricta de intención permanecen. Cambios basados en documentación Google oficial: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8 y https://ai.google.dev/gemini-api/docs/generate-content/thinking .
- **La modificación no es una prueba exitosa real**, no garantiza menor latencia ni disponibilidad. Requiere reiniciar el broker Python anterior y cargar nueva versión del script, antes de **un único** nuevo ensayo remoto con consentimiento. No se modificó `main`, CoreRPG ni el canon.

### Ensayo desde Godot Windows y ajuste posterior — 16/10/2026

Captura suministrada por el propietario: interfaz **Modo: demo**, entrada `Hablo con un aldeano`, selector **Exigente** y botón **Probar proveedores**. Godot mostró `Diagnóstico no disponible (PROVIDER_UNAVAILABLE)`, con demo y CoreRPG intactos. Por tanto **NO está validada la integración Gemini 3.8 desde Godot**. La aplicación antigua descartaba el cuerpo de error técnico del broker (HTTP 502/503), impidiendo saber si fue timeout, 503 remoto o rechazo; no atribuir causa exacta sin evidencia.

**Parche experimental en la PR, pendiente de prueba física:** mantener API Gemini 3.8 con `thinkingLevel=low`, pero retirar exclusivamente para ese modelo el formato `responseMimeType/application-json` y `responseSchema` forzados, dado que el único ensayo directo exitoso anterior fue de texto normal. La salida se rechaza salvo que sea *exactamente* `observar`, `desplazarse`, `dialogar` u `otro` (sin prosa, JSON, instrucciones ni contenido de mundo). Gemini 3.5 conserva esquema JSON validado. La app Godot ahora conserva solo `error_code` y `diagnostic_reason` de una lista cerrada y muestra `timeout` o `http_503` si el broker los comunicó, sin devolver trazas, secretos ni texto de proveedores.

**Nota histórica (anterior al éxito final):** en este punto todavía faltaba una prueba real desde la interfaz Godot. No enviar canon ni habilitar fallback durante el ensayo. **Es necesario actualizar ambos componentes** (broker local Python y EXE/PCK recompilados de la misma revisión de la rama); no sirve la instancia antigua.

### Validación positiva Godot + Gemini 3.8 — 16/10/2026

**PRUEBA REAL SUPERADA (diagnóstico solamente).** Evidencia: captura de Nimroel NIM-04 proporcionada por el propietario, Windows MSI; compilación de GitHub Actions del commit `e5f86ac8c30b029187feac044dd1ac75731c3e89`, ejecución https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38969848950 (3/3 jobs correctos).

- **Preparación:** PowerShell renovado, `GEMINI_API_KEY` local, broker actualizado `provider_proxy.py` escuchando `127.0.0.1:8766`, `NIMROEL_PRIMARY_PROVIDER=gemini`, `NIMROEL_ENABLE_FALLBACK=0`, `NIMROEL_LOCAL_TOKEN` compartido mediante variables de entorno. El EXE se lanzó **desde esa misma sesión PowerShell** para heredar el token.
- **Acción en Godot:** `Modo: demo`; campo `Hablo con un aldeano`; `Laboratorio IA (no NPC): Exigente`; botón `Probar proveedores`.
- **Resultado visible exacto:** `gemini / gemini-3.8-flash`, `Intención: dialogar · 1562 ms`. La aplicación muestra la respuesta técnica tras recorrido **Godot → broker Python → API Gemini 3.8 → broker → Godot**, aproximadamente **1,56 segundos** medidos por el broker.
- **Seguridad y alcance:** sin respaldo Mistral, sin NPC narrativo, sin mutación de WorldState y sin intervención de CoreRPG. No hay tokens consumidos ni coste medidos; es **un éxito puntual**, no garantía de disponibilidad continua.
- **Incidencia de arranque anterior resuelta:** `LOCAL_AUTH_REQUIRED` apareció al ejecutar el EXE sin heredar el token de PowerShell. Se corrigió ejecutándolo mediante `Start-Process` **en la misma sesión**; no se modificó la autenticación del broker ni se deshabilitó su protección.
- **Conclusión delimitada:** validado el diagnóstico real de Gemini 3.8 dentro de Godot/Windows. Siguen pendientes Gemini 3.5 **mediante el broker NIM-04**, Mistral real, cualquier regresión específica de teclado sobre NIM-04 no confirmada individualmente y la integración narrativa/autoridad CoreRPG. El funcionamiento general de la tablet y los dos teclados en NIM-03 han sido confirmados por el propietario. Mantener PR #21 en borrador, sin fusionar sin consentimiento expreso.

### Mistral: pruebas reales desde Godot Windows — 17/10/2026

**Evidencia visual aportada por el propietario**, Nimroel NIM-04 sobre Windows, `Modo: demo`, texto inventado `Hablo con un aldeano`, broker local autenticado, `NIMROEL_PRIMARY_PROVIDER=mistral`, `NIMROEL_ENABLE_FALLBACK=0` y clave de Mistral solo en entorno local. La clave no se ha incluido en ninguna captura ni registro.

- Nivel **Exigente** → modelo configurado `mistral-medium-3-5`: Godot mostró `PROVIDERS_TEMPORARILY_UNAVAILABLE · Motivo: http_429`.
- Nivel **Sencilla** → modelo configurado `mistral-small-2603`: Godot mostró igualmente `PROVIDERS_TEMPORARILY_UNAVAILABLE · Motivo: http_429`.
- Los dos ensayos confirman que la cadena Godot→broker pudo recibir el código técnico del proveedor. `http_429` corresponde a la respuesta HTTP remota que el broker categorizó (no a un límite local 30 llamadas: ese devuelve otro código).
- **No** se ha obtenido clasificación `intent` de Mistral, así que **ninguno de los modelos se considera validado**. La causa concreta del 429 (tasa, tokens, cuota organizativa, saldo, acceso al modelo) no está determinada: el broker no registra el cuerpo de error remoto por privacidad.
- El usuario ha mostrado en Mistral Admin plan gratuito con asignación mensual API/Studio `0 US$ / 10 US# NIM-04 — Protocolo de proveedor real y pruebas (17/10/2026)

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
- **Situación posterior:** el ensayo del broker con `tier=complex`, proveedor `gemini` y fallback deshabilitado, y la visualización en Godot Windows, quedaron validados posteriormente (véase «Validación positiva Godot + Gemini 3.8»). Mantener límites y privacidad.

### Ensayos posteriores de clasificación — 16/10/2026

Evidencia proporcionada por el usuario desde PowerShell MSI, no pruebas ejecutadas por GitHub:
- **Broker NIM-04 (código anterior)**: POST autenticado a `127.0.0.1:8766/v1/provider-probe` con `tier=complex`, `text="Hablo con un aldeano"`, fallback `0`; respondió **HTTP local 503** `PROVIDERS_TEMPORARILY_UNAVAILABLE`. El HTTP 503 **lo produce el broker**: no acredita que Google respondiese 503; la implementación anterior agrupaba timeouts, errores de red y HTTP 429/503.
- **Petición directa Google con schema JSON y temperature 0**: timeout desde PowerShell al cabo de ~53 segundos con `-TimeoutSec 45`; sin respuesta remota ni código HTTP confirmado.
- **Petición directa Google con responseMimeType JSON y sin schema ni temperature**: otro timeout desde PowerShell con `-TimeoutSec 35`; sin respuesta ni HTTP remoto confirmado. Por ello no se demuestra que el schema o temperature causen el timeout por sí solos.
- El mensaje posterior `finally : El término 'finally' no se reconoce` es sintaxis de PowerShell por ejecutar `finally` separadamente de `try/catch`; no es respuesta de Google.
- **Intervención en rama NIM-04 pendiente de ensayo remoto:** para `gemini-3.8-flash`, `thinkingConfig.thinkingLevel="low"`, retirada de `temperature`, `maxOutputTokens=512`, timeout de broker **22 s** frente a 12 s anterior (Godot tiene 28 s), respuesta técnica `diagnostic_reason` solo con valores seguros como `timeout`, `network_error` o `http_503`. El modo JSON y la validación estricta de intención permanecen. Cambios basados en documentación Google oficial: https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.8 y https://ai.google.dev/gemini-api/docs/generate-content/thinking .
- **La modificación no es una prueba exitosa real**, no garantiza menor latencia ni disponibilidad. Requiere reiniciar el broker Python anterior y cargar nueva versión del script, antes de **un único** nuevo ensayo remoto con consentimiento. No se modificó `main`, CoreRPG ni el canon.

### Ensayo desde Godot Windows y ajuste posterior — 16/10/2026

Captura suministrada por el propietario: interfaz **Modo: demo**, entrada `Hablo con un aldeano`, selector **Exigente** y botón **Probar proveedores**. Godot mostró `Diagnóstico no disponible (PROVIDER_UNAVAILABLE)`, con demo y CoreRPG intactos. Por tanto **NO está validada la integración Gemini 3.8 desde Godot**. La aplicación antigua descartaba el cuerpo de error técnico del broker (HTTP 502/503), impidiendo saber si fue timeout, 503 remoto o rechazo; no atribuir causa exacta sin evidencia.

**Parche experimental en la PR, pendiente de prueba física:** mantener API Gemini 3.8 con `thinkingLevel=low`, pero retirar exclusivamente para ese modelo el formato `responseMimeType/application-json` y `responseSchema` forzados, dado que el único ensayo directo exitoso anterior fue de texto normal. La salida se rechaza salvo que sea *exactamente* `observar`, `desplazarse`, `dialogar` u `otro` (sin prosa, JSON, instrucciones ni contenido de mundo). Gemini 3.5 conserva esquema JSON validado. La app Godot ahora conserva solo `error_code` y `diagnostic_reason` de una lista cerrada y muestra `timeout` o `http_503` si el broker los comunicó, sin devolver trazas, secretos ni texto de proveedores.

**Nota histórica (anterior al éxito final):** en este punto todavía faltaba una prueba real desde la interfaz Godot. No enviar canon ni habilitar fallback durante el ensayo. **Es necesario actualizar ambos componentes** (broker local Python y EXE/PCK recompilados de la misma revisión de la rama); no sirve la instancia antigua.

### Validación positiva Godot + Gemini 3.8 — 16/10/2026

**PRUEBA REAL SUPERADA (diagnóstico solamente).** Evidencia: captura de Nimroel NIM-04 proporcionada por el propietario, Windows MSI; compilación de GitHub Actions del commit `e5f86ac8c30b029187feac044dd1ac75731c3e89`, ejecución https://github.com/robdor80/Videojuego_Nimroel/actions/runs/38969848950 (3/3 jobs correctos).

- **Preparación:** PowerShell renovado, `GEMINI_API_KEY` local, broker actualizado `provider_proxy.py` escuchando `127.0.0.1:8766`, `NIMROEL_PRIMARY_PROVIDER=gemini`, `NIMROEL_ENABLE_FALLBACK=0`, `NIMROEL_LOCAL_TOKEN` compartido mediante variables de entorno. El EXE se lanzó **desde esa misma sesión PowerShell** para heredar el token.
- **Acción en Godot:** `Modo: demo`; campo `Hablo con un aldeano`; `Laboratorio IA (no NPC): Exigente`; botón `Probar proveedores`.
- **Resultado visible exacto:** `gemini / gemini-3.8-flash`, `Intención: dialogar · 1562 ms`. La aplicación muestra la respuesta técnica tras recorrido **Godot → broker Python → API Gemini 3.8 → broker → Godot**, aproximadamente **1,56 segundos** medidos por el broker.
- **Seguridad y alcance:** sin respaldo Mistral, sin NPC narrativo, sin mutación de WorldState y sin intervención de CoreRPG. No hay tokens consumidos ni coste medidos; es **un éxito puntual**, no garantía de disponibilidad continua.
- **Incidencia de arranque anterior resuelta:** `LOCAL_AUTH_REQUIRED` apareció al ejecutar el EXE sin heredar el token de PowerShell. Se corrigió ejecutándolo mediante `Start-Process` **en la misma sesión**; no se modificó la autenticación del broker ni se deshabilitó su protección.
- **Conclusión delimitada:** validado el diagnóstico real de Gemini 3.8 dentro de Godot/Windows. Siguen pendientes Gemini 3.5 **mediante el broker NIM-04**, Mistral real, cualquier regresión específica de teclado sobre NIM-04 no confirmada individualmente y la integración narrativa/autoridad CoreRPG. El funcionamiento general de la tablet y los dos teclados en NIM-03 han sido confirmados por el propietario. Mantener PR #21 en borrador, sin fusionar sin consentimiento expreso.

 y ha creado clave desde el enlace directo `/api-keys/new` sin suscribirse. Esa asignación visible no demuestra que el servicio acepte estas peticiones bajo los límites efectivos de su organización.
- **Próxima comprobación sin consumo de API:** Mistral Admin → Límites (y si hace falta Uso), consultar cuotas y acceso efectivos. **No repetir solicitudes hasta aclararlo**, ni activar pagos automáticamente. Conservamos el diagnóstico y la protección de WorldState.

## Matriz de evidencias (separando prueba directa y pruebas de integración)
| Caso | Resultado hoy | Latencia | Consumo/coste | Observación |
|---|---|---|---|---|
| Gemini 3.5 / sencilla, broker NIM-04 | PENDIENTE | — | — | No heredar como test de broker la prueba NIM-03 |
| Mistral Small 4 / sencilla | **HTTP 429 remoto — 17/10** | — | No medido | Godot + broker, cuenta Free; causa exacta pendiente de límites |
| Gemini 3.8 / exigente, llamada directa PowerShell MSI | **ÉXITO REAL — 16/10**, texto `GEMINI FUNCIONA` | No medida | No medido | JSON válido; API real autentificada, sin broker ni Godot |
| Gemini 3.8 / exigente, broker NIM-04 anterior | FALLÓ: 503 **local** genérico | 12 s configurados; sin métrica medida | No medido | No identifica HTTP remoto ni causa exacta |
| Gemini 3.8 / exigente, Google directo clasificación | TIMEOUT en dos ensayos (JSON schema y JSON simple) | ~53 s primero; >35 s segundo | No medido | No demuestra fallo de disponibilidad ni de schema exclusivamente |
| Gemini 3.8 / exigente, Godot + broker previo | **FALLO mostrado en Godot** | No medido | No medido | PROVIDER_UNAVAILABLE, causa oculta por parser anterior |
| Gemini 3.8 / exigente, Godot + broker actualizado sin JSON forzado | **ÉXITO REAL — 16/10**, `dialogar` | **1562 ms (1,56 s)** | No medido | Captura del juego en Windows, commit `e5f86ac8`; solo clasificación técnica |
| Mistral Medium 3.5 / exigente | **HTTP 429 remoto — 17/10** | — | No medido | Godot + broker, cuenta Free; causa exacta pendiente de límites |
| Alternancia en error simulado | SOLO UNIT TEST OFFLINE | — | 0 | No acredita outage real |
| Cambio de proveedor remoto real | PENDIENTE | — | — | Requiere autorización explícita |

## Tablet Tab S9+ — funcionamiento informado por el propietario
**Confirmaciones del 16/10/2026:** el propietario indica que **la tablet funciona bien** con Nimroel y precisa expresamente que **los dos teclados (Samsung virtual y Bluetooth) ya funcionaban en NIM-03**. Registrar ambos teclados como verificados en NIM-03 por testimonio directo del usuario, sin seguir describiéndolos como fallidos. La confirmación de NIM-04 es de funcionamiento general; no se deduce automáticamente que se haya probado de nuevo cada teclado sobre la APK NIM-04 ni la recuperación del diseño tras ocultar IME. No confundir un test NIM-03 confirmado con un test NIM-04 individual no detallado.

**Comprobaciones adicionales de NIM-04, solo si resultan necesarias para cerrar regresiones:** Descargar la APK `Nimroel_NIM04_TabS9Plus.apk` desde la CI del SHA final, verificar que corresponde al commit y el paquete `org.nimroel.rpg.nim04`. Con teclado Samsung virtual: escribir, leer historial, pulsar Enviar, ocultar teclado y confirmar que cabecera/retrato/pie reaparecen; con Bluetooth: escribir sin IME visible y comprobar que mantiene tamaño completo; alternar ambos con texto conservado. Repetir demo/integración y reanudación. El nuevo panel de proveedores solo existe en Windows; tablet **no** puede llamar a la API.

## Futuro fuera del laboratorio
- Núcleo narrativo real: solo tras WorldState y APIs de conocimiento/acciones CoreRPG (4.9/4.10/4.12) y puente nativo ABI/GDExtension probado Windows+ARM64. Ningún LLM aplica directamente cambios ni inventa hechos autorizados.
- sherpa-onnx TTS: audio de NPC solo después de identidad/voz autorizada; validar reproducción en Godot Windows y después runtime Android real. STT/ASR por micrófono, permisos y tratamiento local en iteración separada.

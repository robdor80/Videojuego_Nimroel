# NIM-05 — Auditoría de integración y traspaso técnico

Fecha: 17/10/2026. Base auditada: `Videojuego_Nimroel/main` @ `35c9d22ca3f688c62c709320b20cba565518669d` (NIM-04 PR #21 fusionada). Rama NIM-05: `feat/nim-05-build`.

## 1. Evidencia y límites

| Subsistema | Evidencia real verificada | Estado NIM-05 |
|---|---|---|
| Godot 4.7.2 2D Windows | NIM-04 export y usuario ejecutó clasificación real por proveedores | Conservado; NIM-05 requiere nueva prueba física |
| Android ARM64 Tab S9+ | Exportación CI NIM-04 correcta; teclado previamente ensayado NIM-03 | Exportación y test geométrico; **pendiente prueba física APK NIM-05 virtual y Bluetooth** |
| Gemini 3.5 Flash-Lite | Verificación NIM-03, no nueva prueba física NIM-05 | Clasificador primario sencillo; sin llamadas remotas en esta fase |
| Gemini 3.8 Flash | Godot MSI NIM-04 clasificación real `dialogar` | Clasificador primario exigente, no NPC |
| GPT-6 Luna y GPT-6 Sol | Godot MSI NIM-04 clasificación real individual | Fallback offline probado; **conmutación real NO verificada** |
| Mistral | Decisión definitiva de descarte | Sin proveedor, ruta, clave ni fallback operativo |
| sherpa-onnx WAV | Banco TTS real Windows en NIM-03/04 fuera de Godot | NIM-05 añade servidor local y reproductor Godot de laboratorio; audible MSI **pendiente de ensayo físico** |
| STT/ASR | No integrado | Pendiente de fase posterior |
| CoreRPG | `CoreRPG/main` `d6e2c8fe5a33405bc41b082cf89d6c8036f3c8b8` | 4.8, C++20 `STATIC`; ninguna GDExtension |
| Gameplay/WorldState | `core_port.gd` anuncia `core_available=false` y `interaction_pipeline.gd` responde `CORE_NOT_CONNECTED` | **Bloqueo obligatorio conservado** |

## 2. Endurecimiento broker: diseño y garantías

- `Tools/NIM04/provider_proxy.py` mantiene los dos niveles cerrados: `simple` Gemini 3.5→Luna; `complex` Gemini 3.8→Sol. No hay narrativa ni mutación.
- `request_id` obligatorio (32 dígitos hexadecimales); Godot genera 16 bytes aleatorios criptográficos por pulsación. El servicio tiene ledger efímero protegido por mutex, en RAM, con TTL 300 segundos y máximo 128 entradas. Un mismo ID repetido mientras trabaja retorna HTTP 409 seguro; tras concluir reproduce el resultado anterior **sin repetir llamada**; usar el ID con contenido diferente se rechaza.
- `MAX_CONCURRENT_PROBES=1` para laboratorio. Una solicitud simultánea recibe `LOCAL_PROBE_BUSY`; el cupo y contadores permanecen bloqueados por mutex. Esto limita duplicación en concurrencia, no garantiza exclusión entre procesos.
- Cada petición realiza **como máximo una tentativa por proveedor** (Gemini→OpenAI en caso de caída transitoria habilitada); no se hace reintento automático del proveedor caro.
- Se conservan 30 intentos totales y 4 pagables **por proceso**, `NIMROEL_OPENAI_CONSENT=1` para todas las llamadas OpenAI y `NIMROEL_ENABLE_FALLBACK=1` además para respaldo automático, que permanece OFF por defecto.
- Errores 401/403 o salidas malformadas impiden fallback. 429/5xx/timeouts transitorios pueden conmutar **solo si existe el doble consentimiento**. Circuit breaker por modelo tras 2 fallos transitorios, 60 s de enfriamiento; éxito rearma contador.
- No se guardan credenciales, textos o respuestas libres de API en ficheros o logs; ledger almacena únicamente un hash de la carga y una respuesta técnica estructurada y efímera.

**Límites conscientes:** deduplicación no sobrevive reinicio del broker ni protege contra reenvíos con nuevos IDs, servidor adicional, caída del proceso durante respuesta, ni puede determinar costes precisos. El cupo de 4 llamadas **no es presupuesto en moneda**. Producción requerirá una pasarela de pagos con autorización central, idempotencia durable, controles de gasto y telemetría agregada, sin exponer secretos en clientes.

## 3. Sherpa Windows — circuito de laboratorio

`Game/Host2D/scripts/tts_diagnostic.gd` solo se instancia en Windows. `Tools/NIM05/tts_local.py` escucha `127.0.0.1:8767` y exige `NIMROEL_LOCAL_TOKEN` de la sesión, límite 160 caracteres, propósito técnico fijo, sin encabezados Origin y sin aceptar llamadas de host ajeno. Su respuesta es WAV PCM mono acotado a 2 MB. Carga modelo sherpa-onnx únicamente del disco (sin descarga en ejecución) y sintetiza cada frase desde el texto recibido. Godot utiliza `AudioStreamWAV.load_from_buffer` y `AudioStreamPlayer`.

Es una demostración **en tiempo de ejecución**: no reproduce un fichero WAV pregrabado. Sin embargo, CI Windows solo puede demostrar inferencia y WAV generado, y Godot headless solo valida clases/contratos. **No afirmar que suena en MSI hasta que el propietario lo escuche**. `voice_port.gd` conserva `tts_available=false` y `asr_available=false`; el diálogo NPC sigue desconectado.

En Android no se instancia el puerto de laboratorio ni se distribuyen claves, librerías ONNX o modelos: la prueba de Android es de la UI, no de TTS nativo. Futuro soporte ARM64 auténticamente offline: librerías nativas sherpa y dependencias ONNX, modelo empaquetado, permisos de micrófono solo para STT, prueba de inferencia real en Tab.

## 4. CoreRPG — mínimo enlace previsto (sin cambios en el repositorio Core)

1. Core define ABI estable de consumidor (exported `extern "C"` o interfaz compartida acordada), negociación de versión/capacidades, handles opacos y contrato formal de creación, consulta y liberación. No cruzar módulos con `std::string`, excepciones ni punteros C++ cuya propiedad no sea explícita.
2. En Nimroel se prepara proyecto GDExtension adaptador, sin crear un segundo estado. Se fijará versión exacta de `godot-cpp` para Godot 4.7.2, compilación Windows MSVC/clang compatible y Android NDK ARM64, después de aprobar la ABI.
3. Primer hito verificable: consulta read-only de estado de prueba creado **dentro de Core**; falta de biblioteca → error seguro, nunca mock rotulado como estado real.
4. Validar lifecycle nativo, memoria y excepciones, CPU/ABI, errores, suspensión y reanudación Android; después snapshots canónicos Windows↔ARM64 y autoridades 4.9/4.10/4.12.
5. Hasta esos contratos y pruebas: `CORE_NOT_CONNECTED` obligatorio incluso si Gemini/TTS responde.

## 5. Revisión después de CI y pruebas físicas

Ver `Docs/NIM-05_PRUEBAS_FISICAS.md`. No fusionar PR sin comprobación humana. La CI acreditará import/headless, tests Python/Godot, TTS real en runner Windows y paquetes x64/ARM64. No acreditará uso del micrófono, voz audible MSI, rendimiento tablet ni pagos reales.

## 6. Tareas expresamente diferidas

- **NIM-06 o posterior:** piloto nativo Core↔GDExtension cuando exista contrato aprobado y, en paralelo, ASR local / TTS Android con modelo de distribución, tamaño y memoria probados.
- **Tras nueva autorización económica:** ensayo mínimo de fallback real Gemini→OpenAI con consentimiento y entorno MSI aislado. No realizado ni requerido para cierre de NIM-05.
- **Prueba física humana obligatoria:** escuchar frase TTS generada dentro de Godot, pantalla de teclado y Bluetooth en Tab S9+ con la APK NIM-05.

# NIM-01 — comparación de riesgos Android: Godot frente a Unreal Engine 5.8

**Fecha:** 2026-10-14
**Clase de evidencia:** documentación oficial y examen de CoreRPG/CMake; **sin prototipo UE5 Android ni test GDExtension Android compilado**.
**Motivo:** evaluar si sustituir Godot por Unreal suprime los dos riesgos identificados: integrar CoreRPG C++20 en Android y comunicación por voz (entrada/salida).

## Respuesta ejecutiva

**Unreal facilita algo el consumo de CoreRPG C++ porque permite un módulo/plugin C++ nativo con `*.Build.cs`, pero NO elimina compilar CoreRPG para Android arm64-v8a con NDK ni resolver ABI, STL, empaquetado, ciclo de vida y pruebas de dispositivo.**

**Ambos motores pueden capturar audio; ninguno transcribe por sí solo frases libres del usuario en castellano mediante el motor conversacional Gemini.** El ASR Gemini requiere enviar audio por API, permisos y gestionar errores/latencia. Godot aporta TTS multiplataforma con `DisplayServer.tts_speak()`; Unreal incluye plugin TextToSpeech en `Engine/Plugins/Experimental`, cuya implementación concreta y cobertura Android deben verificarse. También puede hacerse un puente al TTS nativo Android desde Unreal, pero exige integración de plataforma.

Para Nimroel (pantallas 2D ilustradas, retratos, texto y voz, Windows/Android) se conserva **Godot como candidata principal**, con **condición de salida** de un spike real GDExtension + CoreRPG en Android, y un spike de voz. Cambiar de motor antes de estas pruebas no está justificado.

## 1. CoreRPG: qué cambia y qué permanece

| Componente | Godot 4.7 | Unreal Engine 5.8 |
|---|---|---|
| Compilación CoreRPG Android | CMake + NDK arm64-v8a | CMake + NDK o toolchain integrado UE para la librería; requiere arm64-v8a igualmente |
| Adaptación motor↔Core | `godot-cpp` / GDExtension, biblioteca compartida `.so` y `.gdextension` | módulo/plugin nativo C++, `*.Build.cs`, target externo `ModuleType.External`; CoreRPG puede enlazarse como biblioteca estática |
| Gestión ABI/C++ runtime | Sí, comprobar STL, excepciones, símbolos, PIC, ownership | También: compatibilidad de NDK/compilador/STL/excepciones, límites de memoria y ownership |
| APK | Export Godot + GDExtension/Android plugin v2 cuando sea necesario | Unreal Build Tool + UPL/Gradle/Android packaging |
| Prueba imprescindible | Core real crea/consulta entidad en APK Android sin MSI | Exactamente igual |
| Mantenimiento | Bridge Godot en proyecto, dependiente de godot-cpp | Bridge UE específico, dependiente de UE |
| Estado actual | Sin prueba Android de CoreRPG | Sin prueba Android de CoreRPG |

En CoreRPG ya existe `add_library(CoreRPG STATIC)`, `C++20` y `CORERPG_BUILD_CONTENT_JSON=OFF` por defecto. La JSON opcional, los assets APK, las rutas de guardado y el módulo de simulación posterior se evaluarán independientemente del enlace mínimo.

**No crear una segunda copia del WorldState en el Host**, incluso si Unreal utiliza UObject/Actor o Godot Nodes.

**Ganancia de Unreal:** menos capa de bindings específicos. **Costes inevitables:** cross-compilation, validación de plataforma, empaquetado y contratos de CoreRPG.

## 2. Voz de entrada: prácticamente el mismo trabajo

- **Godot**: grabación desde micrófono documentada para Windows/Android; activar entrada de audio, permisos Android, procesar fragmentos.
- **Unreal**: plugin de runtime `AudioCapture` con interfaces y Blueprints, permisos Android (RECORD_AUDIO); comprobar el comportamiento en el dispositivo real.
- **En ambos**: reconocer significado del audio implica transcripción o interpretación con Gemini (API audio→texto), gestionando WAV/otros formatos soportados, límites, internet, latencia, cancelación, eco durante el TTS y ambigüedad. Un plugin opcional de reconocimiento Android exigiría Java/Kotlin/JNI o integración equivalente en ambos.
- No prometer diálogo hablado bidireccional continuo únicamente porque haya captura de audio: para NIM-01 utilizar **pulsar para hablar** y validación de la intención estructurada por CoreRPG.
- Gemini 3.5 Flash-Lite y 3.8 Flash son modelos seleccionados por el autor; no reabrir proveedor aquí.

## 3. Voz de salida: ventaja inicial de Godot, con matices

Godot implementa en `DisplayServer` voces del sistema en Windows y Android: `tts_get_voices_for_language("es")`, `tts_speak`, `tts_stop`; requiere habilitar TTS y que existan voces válidas en el dispositivo. Puede haber latencia e incluso dependencia de servicio de red según voz instalada.

Unreal 5.8 **también dispone** de plugin `TextToSpeech` (categoría Accesibilidad), pero Epic lo enumera bajo `Engine/Plugins/Experimental/TextToSpeech`. La documentación de `ITextToSpeechModule` declara factorías por plataforma **para plataformas permitidas**, no demuestra por sí sola que nuestro APK Android funcione con el plugin. Otra opción es integrar `android.speech.tts.TextToSpeech` mediante plugin Android/Java. Ninguna ofrece por sí sola actuación dramática y voces NPC diferenciadas de calidad generativa.

**Resultado:** no es un problema único de Godot. Godot tiene una API TTS documentada para Android/Windows más inmediata; UE requiere comprobar plugin/plataforma o adaptar TTS Android.

## 4. Coste total de producto Nimroel

**Interfaz:** Godot ofrece Control/UI e imágenes 2D sin cargar el pipeline gráfico pesado de UE5. Unreal UMG puede hacer exactamente la misma pantalla, pero el proyecto Android requiere más atención a tamaño binario, optimizaciones, configuración móvil y recursos por su motor generalista. No atribuir cifras de APK o rendimiento sin comparar prototipos medidos.

**Aprovechamiento:** el usuario ya tiene UE5 instalado para Star Trek, lo cual reduce instalaciones, pero no reduce las obligaciones ARM64/audio de Nimroel. Mantener Godot permite que ambos juegos compartan **CoreRPG como motor lógico** sin compartir framework gráfico.

## 5. Decisión y criterios de revisión

**Mantener Godot para NIM-01 (provisional, sujeta a spike).** No presentar UE5 como solución mágica ni Godot como superior para integración C++.

Cambiar a UE5 si el spike demuestra bloqueos reproducibles de GDExtension Android (ABI, packaging, crashes sin solución razonable, incompatibilidad con versión Godot) o si la calidad/latencia de audio real exige una solución de plataforma que Unreal resuelva demostrablemente mejor en el mismo dispositivo.

**Pruebas de comparación justas:**
1. Mismo commit CoreRPG; crear/consultar ID y conservarlo tras cambio de escena en un APK Android independiente.
2. Grabar una frase de castellano 3–10 s, obtener transcripción Gemini y resolver respuesta textual; medir fallo/latencia.
3. Reproducir respuesta con TTS castellano y detenerla, registrando voz disponible y si requiere red.
4. Instalar en el mismo dispositivo, revisar inicio, tamaño APK, memoria, fallos e incidencias.
5. No afirmar ninguna de estas pruebas como superada hasta contar con registros verificables.

## Fuentes oficiales

- UE5.8 Third-Party Libraries: https://dev.epicgames.com/documentation/en-us/unreal-engine/integrating-third-party-libraries-into-unreal-engine
- UE5.8 Android Support: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-support-for-unreal-engine
- UE5.8 Android UPL: https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-platform-integrations-in-unreal-engine
- UE5.8 Audio Capture: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/AudioCapture
- UE5.8 Experimental TTS: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/TextToSpeech
- Godot 4.7 Android plugins: https://docs.godotengine.org/en/4.7/tutorials/platform/android/android_plugin.html
- Godot GDExtension file: https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html
- Godot 4.7 microphone: https://docs.godotengine.org/en/4.7/tutorials/audio/recording_with_microphone.html
- Godot 4.7 TTS: https://docs.godotengine.org/en/4.7/tutorials/audio/text_to_speech.html
- Gemini audio: https://ai.google.dev/gemini-api/docs/audio

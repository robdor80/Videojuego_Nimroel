# ADR NIM-01 — Selección de Godot para el Host conversacional

**Estado:** APROBADA COMO DECISIÓN TÉCNICA DE NIM-01, con gates obligatorios de validación.
**Fecha:** 2026-10-14
**Decisor de arquitectura:** ChatGPT, con autorización para dirigir NIM-01.
**Alcance de plataformas:** MSI Windows x64 y **solo Samsung Galaxy Tab S9+ Android ARM64**; no hay obligación de soportar móviles ni otros modelos Android.

## Contexto y requisitos

Nimroel es un RPG conversacional 2D con escenarios ilustrados, retratos, historia visible y entrada libre mediante texto y voz. La salida será texto y voz. El objetivo de calidad incluye **voces españolas diferenciadas para el narrador y personajes masculinos/femeninos**, sin confundir un simple ajuste de pitch con una voz natural distinta. El motor lógico portable es CoreRPG C++20; Gemini interpreta/narra y no tiene autoridad sobre el estado del mundo. Los modelos fijados por el autor son Gemini 3.5 Flash-Lite y Gemini 3.8 Flash, sujetos a una integración real por API.

## Decisión

Se selecciona **Godot 4.7.2 Standard** como Host 2D en Windows y Android. Unreal Engine 5.8.2 se mantiene para Star Trek, no para Nimroel.

**Justificación:**
- El valor jugable de Nimroel proviene de simulación, texto, IA y ambientación ilustrada, no de renderizado avanzado 3D.
- Godot dispone de UI, TTS y captura de micrófono multiplataforma documentados; puede exportar proyectos Android ARM64 y usar bibliotecas C++ mediante GDExtension.
- UE5 simplifica parcialmente el enlace de una biblioteca C++ externa como CoreRPG, pero no elimina NDK, ABI, empaquetado Android, permisos ni ASR/Gemini. Su plugin TTS está descrito como experimental; no hay ventaja probada para calidad de voces del dispositivo.
- Limitar Android a una única tablet permite validar de manera focalizada NDK/ABI/voz/rendimiento en un dispositivo fijo. No asumir que funcionar en Windows equivale a funcionar en la Tab S9+.

## Arquitectura requerida

1. **Host Godot:** pantalla, dibujo ilustrado, retratos, teclado/táctil, control del micrófono y reproducción TTS; no WorldState paralelo.
2. **Bridge C++:** `CoreRPG STATIC` compilado para Win x64 y Android ARM64, enlazado en `GDExtension`; versión del bridge y esquema de mensajes separados del modelo de mundo.
3. **Capa IA:** interpretar audio o texto, proponer acciones estructuradas, narrar solo percepciones y resultados autorizados. Fallos de red/API no alteran la simulación.
4. **VoiceManager:** gestiona personajes por ID estable y roles vocales; selección por voz disponible por plataforma (`tts_get_voices_for_language("es")`, `tts_get_voices()`), preferencias persistentes, control de volumen/tono/velocidad, interrupción, cancelación y fallback textual. Los IDs de voces de Windows y Android **no son intercambiables**.
5. **VoiceBackend:** interfaz separada del juego que permite inicialmente `DisplayServer.tts_speak` y, si es insuficiente, un backend adicional Android nativo por plugin Kotlin/Java o un sintetizador con voces distribuidas/licenciadas. No prometer modelos de voz y calidades aún no medidos.
6. **Push-to-talk:** capturar fragmentos, permiso `RECORD_AUDIO` en Android y mostrar transcripción para confirmación de acciones sensibles; salida por texto siempre disponible.

## Condiciones de calidad y aceptación

La selección de motor no equivale a aprobación de los siguientes puntos:

- [ ] APK Godot instalado y ejecutado en **Galaxy Tab S9+**, sin MSI, con interfaz utilizable.
- [ ] Un `WorldState` **real** de CoreRPG enlazado mediante bridge en Android; emisión y recuperación de entidad/revisión, estabilidad tras cambios de escena y app en segundo plano.
- [ ] Misma prueba mínima CoreRPG ejecutada en Windows y Android con resultados deterministas.
- [ ] Entrada escrita y micro de Windows y Tab S9+ probados con transcripción en castellano de frases reales.
- [ ] Gemini interpreta una solicitud; CoreRPG valida; texto narrado refleja únicamente estado autorizado. Ningún mock se presenta como gameplay.
- [ ] TTS castellano comprobado en ambas plataformas: enumeración de voces, prueba audible, interrupción y recuperación.
- [ ] **Objetivo de diferenciación de voz:** narrador distinguible y varias voces masculinas/femeninas (objetivo de pruebas: al menos dos masculinas y dos femeninas de calidad utilizable si se dispone de packs). No marcar satisfecho por 1 voz con cambios de pitch artificiales.
- [ ] Persistir por rol/NPC la **preferencia** de voz, remapeando por plataforma sin afectar a la identidad NPC.
- [ ] Registrar coste/latencia/permisos, fallback texto y acceso a API; no incrustar credenciales Gemini distribuidas en APK ni GitHub.
- [ ] Si los motores TTS instalados no ofrecen variedad suficiente, probar backend alternativo de voces *antes de cerrar el requisito de inmersión*.
- [ ] Documentar cada prueba con commit, dispositivo, SO, API, reproducibilidad, incidencias y resultado.

## Condición de reevaluación

Solo reconsiderar UE5 para Nimroel si los spikes muestran un impedimento concreto y reproducible de Godot (carga GDExtension Android, ciclo de vida/corrupción, fallos audio no solucionables, rendimiento inaceptable) **y** existe un prototipo comparativo UE5 que resuelve objetivamente ese fallo. No cambiar de motor únicamente por tener UE5 instalado o preferir C++ sin prueba.

## Evidencia documental

- Godot GDExtension: https://docs.godotengine.org/en/4.7/engine_details/engine_api/gdextension/index.html
- Godot Android plugin v2: https://docs.godotengine.org/en/4.7/tutorials/platform/android/android_plugin.html
- Exportación Godot Android: https://developer.android.com/games/engines/godot/godot-export
- Godot TTS: https://docs.godotengine.org/en/4.7/tutorials/audio/text_to_speech.html
- Godot DisplayServer: https://docs.godotengine.org/en/4.7/classes/class_displayserver.html
- Grabación micrófono Godot: https://docs.godotengine.org/en/4.7/tutorials/audio/recording_with_microphone.html
- Android TTS: https://developer.android.com/reference/android/speech/tts/TextToSpeech
- UE5 librerías de terceros: https://dev.epicgames.com/documentation/en-us/unreal-engine/integrating-third-party-libraries-into-unreal-engine
- UE5 experimental TTS: https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/TextToSpeech
- Samsung España Tab S9+: https://www.samsung.com/es/mobile-phone-buying-guide/latest-samsung-galaxy-tab-2023/

**Estado de implementación:** no hay evidencias de APK real, audio real, múltiples voces TTS ni bridge CoreRPG ejecutado. Este ADR fija decisión y aceptación; no acredita resultados.

# NIM-01 — auditoría técnica Android/CoreRPG y voz (2026-10-14)

**Estado:** evaluación documental y del código fuente; **sin pruebas reales de compilación Android, enlace GDExtension, voz, micrófono ni ejecución en dispositivo**.
**Alcance:** implementación del Host Nimroel 2D, no una reforma de CoreRPG ni del canon.
**Decisión:** Godot 4.7.2 Standard como Host; CoreRPG C++20 sigue siendo independiente; Gemini 3.5 Flash-Lite habitual y Gemini 3.8 Flash excepcional (modelos elegidos por el autor).

## A. CoreRPG en Android: conclusión

**Viable como diseño respaldado por mecanismos oficiales de plataforma, todavía no demostrado en dispositivo.**

Inspección efectuada del repositorio `robdor80/CoreRPG`:
- `CMakeLists.txt`: target `CoreRPG` **STATIC**, C++20, fuentes portable de lógica de dominio, sin SDK Android/Godot/UE5.
- `CoreRPGContentJson` es una biblioteca STATIC opcional que añade jsoncons y carga de packs; apagada por defecto. **No incluirla en el primer spike**: probar antes la lógica mínima.
- `README.md` y `docs/roadmap.md` tienen texto de estado 4.8 desactualizado; la PR #6 figura **merged**. No confundir eso con haber demostrado soporte Android.
- La Fase P1 del roadmap CoreRPG **ya exige** un spike NDK + aplicación Android real, incluidas pruebas de toolchain, STL, excepciones, identidad y reproducción.
- La serialización actual del Core entrega bytes; el acceso a almacenamiento físico depende del Host, no del Core.

### Diseño concreto de enlace

```text
[Host Godot: escenas, retratos, texto, voz]
              |
    GDExtension / Godot C++ bindings
              |
 [BridgeNimroel: C++20, API estrecha de consultas/acciones]
              |
        [CoreRPG STATIC]
              |
       [WorldState AUTORITATIVO]
```

Se compilan **artefactos diferentes desde las mismas fuentes**:
- Windows x64 -> extensión nativa para Windows + CoreRPG compilado para Windows.
- Android arm64-v8a -> extensión .so C++20 + CoreRPG compilado con Android NDK y STL libc++.

Godot 4.7 dispone de selección de bibliotecas por arquitectura en `.gdextension`. Los plugins Android v2 permiten JNI/Kotlin y GDExtension en AAR si hiciera falta. No es necesario convertir CoreRPG a Kotlin ni compilar el motor Godot completo.

### Requisitos del spike

1. Fijar versión concreta de Android NDK, nivel API objetivo y versión exacta de godot-cpp que corresponda a Godot 4.7.2.
2. Probar CMake Android: `-DANDROID_ABI=arm64-v8a`, `-DCMAKE_TOOLCHAIN_FILE=<ndk>/build/cmake/android.toolchain.cmake`, `-DCMAKE_POSITION_INDEPENDENT_CODE=ON`, `-DBUILD_TESTING=OFF`, `-DCORERPG_BUILD_CONTENT_JSON=OFF`; usar configuración apropiada para Android y comprobar C++20/excepciones/RTTI/STL.
3. Compilar el bridge nativo y empaquetar la extensión arm64 en un APK Godot de prueba, además de la build Windows independiente. **Cuidado:** CoreRPG STATIC enlazado dentro de .so puede requerir -fPIC; la propiedad PIC debe configurarse en la build Android/bridge, no imponerse globalmente sin motivación.
4. Crear/consultar un EntityId real del Core; repetir consulta, descargar UI/escena y confirmar misma identidad; pruebas de RNG y serialización cuando el API sea accesible.
5. Ejecutar APK en dispositivo ARM64 objetivo **sin MSI**; revisar `adb logcat`, errores de carga nativa, memory ownership, app background/foreground, rendimiento y persistencia de save físico usando `user://`.
6. A continuación, evaluar `CoreRPGContentJson` y lectura de assets dentro del APK/almacenamiento extraíble. No asumir que rutas `res://` son rutas filesystem nativas.
7. Registrar commit exacto de CoreRPG, NDK/ABI, APK, dispositivo, pasos, evidencias, éxito/error antes de pasar el check a aprobado.

**Riesgos concretos:** dependencia accidental no portable; PIC/ABI/STL y excepciones; mismatch de interfaz GDExtension; empaquetado de libs por ABI; filesystem de ContentJson; ciclo de vida Android/pausa; idempotencia de acciones; gestión de memoria y threads.

**Mitigación:** un adaptador mínimo y versionado, no exponer toda la API C++ de CoreRPG a GDScript; pruebas Android tempranas con el Core mínimo y sin simular la ejecución de acciones todavía no implementadas.

## B. Voz: tres funciones claramente separadas

**Entrada del jugador:** señal del micrófono. Godot soporta `AudioStreamMicrophone` con input habilitado y `AudioEffectCapture` / `AudioEffectRecord`; Android exige permiso micrófono. Capturar audio **no** es transcribir.

**Transcripción/reconocimiento:** convertir voz a texto. Dos rutas de prueba sin cambiar el Máster Gemini:
1. **MVP prioritario común:** capturar fragmentos push-to-talk y enviar el audio a los modelos Gemini 3.5 Flash-Lite o Gemini 3.8 Flash, que aceptan input de audio y producen output de texto. La entrada estructurada resultante deberá ser una propuesta validable, no gameplay autoritativo. Confirmar formato/tamaño/límites y desempeño real con frases españolas.
2. **Optimización Android posterior:** plugin Android v2 escrito en Kotlin/Java que invoque `SpeechRecognizer`, con estados, `RECORD_AUDIO`, listener, cierre `destroy()` y comprobación opcional de `createOnDeviceSpeechRecognizer` (API 31+). El reconocimiento del dispositivo **no garantiza** offline y el servicio estándar puede enviar audio a servidores. Nunca dictado continuo permanente: pulsar para hablar.
En Windows, el dictado del sistema en caja de texto puede ayudar como fallback manual; no atribuirlo a una integración ASR propia.

**Salida del Máster:** Godot 4.7 incorpora TTS oficial, `DisplayServer.tts_get_voices_for_language("es")`, `DisplayServer.tts_speak()`, `tts_stop()`, `tts_is_speaking()`. Para usarlo, habilitar `audio/general/text_to_speech` y comprobar voces instaladas. Sistema disponible Windows/Android; voz/idioma/latencia/offline dependen de servicios y paquetes del dispositivo. **No añadir TTS cloud al MVP**: si las voces del sistema no satisfacen la calidad narrativa, valorar una opción más expresiva en fase futura explícita, sin confundir los modelos Gemini de texto con modelos de síntesis de voz.

### Flujo de voz propuesto

```text
[Jugador PULSA para hablar] -> [Godot graba audio] -> [ASR Gemini/Android]
                          -> [texto reconocible]
                          -> [Gemini interpreta intención]
                          -> [CoreRPG valida/resuelve] -> [resultado autorizado]
                          -> [Gemini narra TEXTO]
                          -> [UI muestra texto] + [DisplayServer TTS habla]
```

Si el audio se entrega directamente a un modelo con salida estructurada, se puede combinar la transcripción y la primera interpretación dentro de la misma llamada; preservar el texto escuchado para corregir errores y no ejecutar órdenes ambiguas/irreversibles sin confirmación.

### Controles y fallos que debe contemplar la UI

- Toggle voz/texto, botón **pulsar para hablar** sin captura continua, indicador de micrófono, botón silenciar voz, detener locución y volver a leer.
- Transcripción visible/editable antes de enviar acciones sensibles; soporte castellano/es-ES y acentos, nombres propios del universo.
- Si se deniega micrófono o el ASR falla, seguir con escritura.
- Si faltan voces TTS, mostrar narración en texto; no fingir voz ni hacer fallar el juego.
- Impedir eco: detener o suspender ASR durante TTS según el modo.
- Definir cancelaciones, timeout, manejo de ruido, ausencia de internet, reintento manual y límites de tamaño de audio.
- No incrustar claves Gemini en código GitHub ni en APK público. Para prueba personal, introducir credencial del usuario en runtime y guardarla con cautela en almacenamiento protegido cuando sea posible; para distribución general, diseñar un backend/relay o esquema de autenticación que no exponga la clave.
- La app Android no debe depender del MSI. **Gemini remoto sí requiere internet** para conversación libre. Offline puede mantener UI y simulación del Core una vez integrados, pero no inventar un Máster que no está disponible.
- No enviar más contexto oculto del necesario al modelo ni logs de voz no consentidos.

## C. Esfuerzo, priorización y aceptación real

**Bloqueador mayor:** conexión CoreRPG Android con .so/arm64 en APK de prueba (esfuerzo medio; incertidumbre media hasta medición).

**Entrada por micrófono:** captación multiplataforma sencilla en principio; reconocimiento preciso con Gemini es integración API, permisos y manejo de latencia/coste/cancelaciones (esfuerzo medio).

**Salida TTS:** función Godot existente; integrar voz castellana y controles (esfuerzo bajo/medio, aunque calidad de voces variable).

**Orden recomendado:**
1. Verificar apertura del proyecto Godot y pruebas mínimas de interfaz Windows.
2. Añadir TTS de Godot: voz de es-ES si está disponible, lectura/interrupción y modo texto.
3. Implementar push-to-talk y prueba ASR acotada (datos solo de prueba).
4. Spike Android arm64 **con CoreRPG real** y ciclo de vida mínimo.
5. Tras comprobar ambas plataformas, adaptar UX táctil e integrar consultas reales en el orden de fases CoreRPG.

**Criterios de salida técnica para estas dos integraciones:**
- [ ] Core real crea y recupera una identidad en APK Android arm64; no únicamente en PC.
- [ ] Mismo experimento lógico determinista comprobado en Windows/Android.
- [ ] Android arranca la aplicación sin ordenador y sin segundo WorldState.
- [ ] Micro funciona previa concesión del permiso y ASR devuelve texto verificable.
- [ ] TTS castellano reproduce una narración de ejemplo, se interrumpe y no produce bucle de micrófono.
- [ ] Si no hay permiso, voz, conexión o credencial, el juego degrada funciones sin corromper estado.
- [ ] Seguridad de credenciales, coste y datos de voz revisados antes de entrega.

## D. Fuentes oficiales revisadas

- https://docs.godotengine.org/en/4.7/tutorials/platform/android/android_plugin.html
- https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_android.html
- https://docs.godotengine.org/en/4.7/tutorials/export/android_gradle_build.html
- https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html
- https://docs.godotengine.org/en/4.7/tutorials/audio/recording_with_microphone.html
- https://docs.godotengine.org/en/4.7/tutorials/audio/text_to_speech.html
- https://docs.godotengine.org/en/4.7/classes/class_displayserver.html
- https://developer.android.com/reference/android/speech/SpeechRecognizer
- https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite
- https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash
- https://ai.google.dev/gemini-api/docs/audio

## E. Límites de esta auditoría

La evidencia de documentación es suficiente para **mantener Godot como elección técnica razonable**, no para afirmar que ya se completó ninguna prueba: no se ha compilado ni ejecutado APK, no se han cargado librerías GDExtension en Android ni se han enviado peticiones de voz/Gemini desde el Host. El contrato final del bridge dependerá del CoreRPG efectivamente disponible al integrarlo.

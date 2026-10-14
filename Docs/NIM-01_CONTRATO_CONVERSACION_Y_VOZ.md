# NIM-01 — contrato de conversación, entrada multimodal y voces de NPC

**Estado:** Godot + sherpa-onnx elegidos y aprobados por el autor; contrato de interacción definido; **NO IMPLEMENTADO / NO PROBADO**.
**Fecha:** 2026-10-14
**Aprobación de dirección:** el jugador puede escribir o hablar; su participación aparece en bocadillo de jugador y **no se sintetiza**; las respuestas verbales de NPC aparecen en bocadillo de NPC y **sí se sintetizan** con la voz personalizada asignada. La ilustración sigue siendo ambientación 2D, no una interfaz point-and-click.

## 1. Flujo canónico de un turno

```text
[Jugador teclea] --------------------------+
                                           |
[Jugador pulsa para hablar] -> [ASR] -> texto revisable
                                           |
                                           v
                            [Bocadillo del JUGADOR]
                                           |
                                           v
                             [Gemini: interpretar]
                              texto -> propuestas tipadas
                                           |
                                           v
                        [Contexto autorizado y CoreRPG]
              (consultar conocimiento y presencia; validar
                  y ejecutar acciones solo cuando proceda)
                                           |
                                           v
                     [Resultado de hechos AUTORIZADOS]
                                           |
                                           v
                      [Gemini: redactar respuesta NPC]
                                           |
                          +----------------+-------------------+
                          |                                    |
                          v                                    v
                    [Bocadillo NPC]                [sherpa-onnx TTS]
                          |                           voz NPC asociada
                          +------- texto idéntico ---------+--> audio
```

**Texto es fuente única de la respuesta pronunciada:** TTS debe recibir exactamente la intervención autorizada visible en el bocadillo, salvo normalización puramente prosódica (pausas, signos) que no cambie su significado. Evitar que una llamada de IA genere un audio de contenido independiente.

No toda petición implica una acción. Preguntar «¿qué veo?» solo consulta percepción. Si no hay NPC dialogando, el resultado puede ser texto narrativo/sistema sin voz de NPC. No atribuir frases a un personaje que no existe o que no ha podido hablar. Una solicitud puede ser rechazada por el Core; se comunica de forma adecuada, sin inventar éxito.

## 2. Entrada escrita y hablada

**Escritura:** validar longitud y codificación -> mostrar el mensaje del jugador -> enviar texto a Gemini para análisis/intención.

**Voz:** capturar con Godot al pulsar/hablar, con permiso de micrófono en Android; transcribir; mostrar el texto que el sistema ha reconocido en el bocadillo del jugador; permitir corregir antes de enviar o confirmar acciones sensibles. **No reproducir la voz del jugador.**

Rutas técnicamente posibles:
- **Tecnología aprobada para evaluar en dispositivo:** sherpa-onnx **ASR local** para convertir audio a texto en Windows y Android; el mismo proyecto sherpa-onnx dispone de ASR y TTS, pero necesitan modelos distintos. Unificación de bibliotecas NO significa que el modelo de TTS transcriba ni viceversa.
- **Alternativa/fallback:** enviar audio a Gemini multimodal y pedir transcripción o una estructura de intención con evidencia; controlar cuota, red, tipos de audio, ambigüedad y seguridad. Una ruta puede resultar más rápida/precisa en la Tab S9+; elegir tras medidas reales.
- Ambas rutas deben entregar un **formato textual/intermedio equivalente** al flujo escrito. Nunca enviar audio o transcripción directamente a mutación CoreRPG.

No reproducir los mensajes del jugador con TTS. Si el reconocimiento tiene baja confianza o contiene negaciones/órdenes sensibles, presentar transcripción editable y pedir confirmación antes de ejecutar.

## 3. Frontera de verdad, conocimiento y respuesta NPC

La secuencia no se reduce a «Gemini autoriza, Core valida sí/no y devuelve un diálogo». Debe ser:
1. Gemini interpreta y propone una o varias consultas/acciones **tipadas** (ej. percibir, hablar, caminar, entregar, esperar).
2. CoreRPG + reglas del universo determinan lo que existe, dónde está cada actor, qué sabe, si puede recibir la petición y cuál es el resultado; cada paso con nueva validación cuando sea una secuencia.
3. Solo el resultado que **puede conocer el personaje receptor/jugador** se entrega a Gemini para redactar. No filtrar secretos ni la estructura interna completa del mundo.
4. El narrador de diálogo genera texto congruente con el NPC (personalidad/perfil definido) **sin** crear hechos nuevos ni mutaciones.
5. Solo si existe una intervención real de NPC se presenta su bocadillo y se activa su voz. Un NPC también puede callar, negarse o desconocer algo.

La autorización de hechos es exclusiva del CoreRPG; el **host no guarda un segundo WorldState** y el TTS nunca participa en decidir resultados.

## 4. Asignación de voz a actores

```text
SpeakerProfile {
  actor_id: EntityId persistente | "narrator",
  voice_role: identificador semántico (ej. male_adult_01),
  model_id: ID de modelo TTS instalado y compatible,
  speaker_id: opcional en modelo multihablante,
  pace/tone/volume: parámetros de presentación,
  speech_enabled: bool
}
```

- `actor_id` e identidad canónica no dependen de arte, voz ni motor gráfico.
- Voz del jugador: **desactivada para reproducción**; su contenido solo aparece como texto.
- Voz de NPC: **activada por defecto**, si hay un modelo compatible instalado.
- Narración general/no NPC: **texto por defecto**. Una voz de narrador será función opcional independiente cuando se decida, sin mezclarse con la voz de un NPC.
- Buscar varias voces masculinas y femeninas en castellano con licencias compatibles; no prometer cantidades ni naturalidad antes de testear modelos concretos.
- Si no existe modelo o falla sherpa, conservar inmediatamente el texto; no bloquear conversación ni falsear estado.
- Carga diferida/caché de modelos, cola de reproducción, interrupción al hablar de nuevo, protección de eco y voces por rol/NPC estables durante la partida.
- sherpa-onnx TTS es infraestructura de audio de **Host/VoiceBackend**, no se introduce en CoreRPG genérico.

## 5. Actualización simultánea visual y audio

Cuando Gemini devuelva la respuesta autorizada:
- Publicar el bocadillo completo del NPC sin esperar a generar todo el audio.
- Lanzar generación TTS asíncrona y reproducir en cuanto el primer audio esté listo; no bloquear el hilo gráfico.
- Mantener audio y texto semánticamente idénticos; si el NPC emite varias intervenciones, preservar orden y vincular cada clip a su texto/ID de intervención.
- Evitar emitir el mismo audio dos veces por reintentos de red, cambios de escena o recarga.
- Permitir silenciar, parar, repetir, escoger perfil vocal y continuar leyendo texto mientras se produce voz.

No prometer streaming palabra a palabra, sincronización labial ni latencia concreta antes de probar modelo/CPU/ABI en Tab S9+ y MSI.

## 6. Criterios de aceptación (prueba de plataforma, NO acreditados)

- [ ] Una frase escrita aparece en bocadillo del jugador y fluye hasta una propuesta válida para el motor.
- [ ] Una frase hablada se reconoce en castellano en la Tab S9+; se visualiza su transcripción y el mismo flujo funciona sin repetir al jugador en voz.
- [ ] No se ejecuta acción irreversible por audio mal reconocido sin validación/aclaración.
- [ ] Un NPC con identidad real y conocimientos compatibles responde exclusivamente desde contexto autorizado.
- [ ] La respuesta se muestra una sola vez, con bocadillo y audio local sherpa-onnx usando la voz asociada al NPC.
- [ ] Cambiar de NPC selecciona otra voz masculina/femenina española realmente distinta, con evidencia audible; no confundir pitch con un nuevo timbre.
- [ ] La narración general sin NPC y los mensajes del jugador no se leen automáticamente.
- [ ] Apagar voz, denegar micrófono o faltar un modelo conserva interacción escrita.
- [ ] La voz no bloquea la UI ni modifica el WorldState.
- [ ] El juego completo de pruebas se realiza en Windows/MSI y Samsung Galaxy Tab S9+ Android (solo dispositivo Android objetivo).
- [ ] Registrar latencias, uso de memoria, modelos y licencias, calidad, errores de red y rutas de fallback.

## 7. Dependencias y estado

- CoreRPG 4.9 (percepción y conocimiento), 4.10 (acciones/simulación), 4.12 (contextos autorizados) y Content Pack Nimroel 4.13 son relevantes para una conversación real; **no pasar un simulador de UI por diálogo jugable**.
- Gemini 3.5 Flash-Lite habitual y Gemini 3.8 Flash excepcional: elección del autor; integración no acreditada.
- **sherpa-onnx:** motor local aprobado de entrada ASR y salida TTS. Evaluar y seleccionar modelos concretos en castellano, licencias, rendimiento y binding Godot/Android. La aprobación de tecnología no equivale a validar voces concretas o compatibilidad en dispositivo.
- El requisito gratuito de servicio Gemini dentro del EEE es una restricción de proyecto reportada por el autor; validar condiciones de API efectivas antes de publicar/distribuir.

## Referencias oficiales

- https://github.com/k2-fsa/sherpa-onnx
- https://k2-fsa.github.io/sherpa/onnx/c-api/html/
- https://k2-fsa.github.io/sherpa/onnx/android/build-sherpa-onnx.html
- https://github.com/k2-fsa/sherpa-onnx/blob/master/sherpa-onnx/c-api/docs/tts.dox

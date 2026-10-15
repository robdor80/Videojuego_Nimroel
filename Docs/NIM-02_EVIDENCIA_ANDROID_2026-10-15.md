# NIM-02 — Evidencia visual Samsung Galaxy Tab S9+ (Android)

**Fecha de prueba comunicada:** 2026-10-15, capturas visibles 16:15–16:16. **Origen:** 3 capturas del usuario enviadas en conversación (`1000041639.jpg`, `1000041641.jpg`, `1000041643.jpg`). No se incorporan las imágenes al repositorio. **Alcance:** comprobación manual visual, no telemetría, adb, logs ni prueba de llamadas nativas.

## Resultado visual observado
- Aplicación Nimroel RPG abierta en la pantalla apaisada de Galaxy Tab S9+, con cabecera, ilustración de fondo, panel narrativo y botones accesibles.
- Indicadores visibles `MODO INTEGRACIÓN` y `CORERPG / GEMINI / VOZ NO DISPONIBLES`; selector inferior `Modo: integración`.
- Mensajes del jugador en bocadillos distintos de los del sistema, incluyendo consultas de percepción, «avanzo por la aldea» y «hablo con un aldeano». Las tres capturas documentan envío de mensajes y actualizaciones del historial.
- Los resultados de turno son `SISTEMA · CONEXIÓN NO DISPONIBLE` y el mensaje `CoreRPG no está conectado: no se ha iniciado una partida ni ejecutado ninguna acción.` No se atribuye respuesta a NPC ni movimiento autorizado.
- Campo de escritura, botón `Enviar`, botón `Reiniciar demo`, selector de modo y barra de scroll permanecen visibles a pesar del crecimiento del historial; no se reproduce el defecto de NIM-01 de campo de entrada fuera de pantalla.
- La cabecera de algunos mensajes queda parcialmente oculta en la zona superior desplazable de historial; compatible con scroll, pero la captura sola no permite descartarlo como detalle cosmético de layout.

## Semáforo
- **APROBADO VISUALMENTE:** arranque APK en tablet, modo integración, entrada textual observada, bocadillos, error de Core transparente, historial desplazable y controles visibles.
- **NO ACREDITADO** por estas capturas: cambio del modo integración al modo demo y su respuesta posterior; pulsación de `Reiniciar demo` en la tablet; apertura del teclado virtual, permiso de micro, pausa/reanudación, rotación o pruebas de sesión larga.
- **NO IMPLEMENTADO NI PROBADO:** bridge C++ GDExtension CoreRPG real en Android ARM64, Gemini autenticado, sherpa-onnx ASR/TTS y mutación de WorldState real.

## Cierre pendiente
Antes de autorizar la fusión de la PR #18, confirmar cambio de integración a demo con nueva respuesta de simulador y `Reiniciar demo` en Android. Se recomienda probar reanudación desde segundo plano. La PR permanece en Draft; no fusionar automáticamente. Esta evidencia no es la aprobación final de NIM-02.

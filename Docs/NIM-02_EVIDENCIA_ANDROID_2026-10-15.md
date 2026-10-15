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
- **VALIDADO POR DECLARACIÓN DEL USUARIO (15/10/2026):** cambio del modo integración al modo demo, envío de mensaje con nueva respuesta del simulador, pulsación de `Reiniciar demo` y limpieza de historial, así como salida y regreso a la aplicación sin incidencia. Es prueba manual comunicada por el usuario, sin nueva captura/log específico de estas acciones.
- **NO ACREDITADO** por esta evidencia: permiso de micro, rotación, medición de estabilidad prolongada, calidad de voz o latencias; la interacción textual acredita entrada pero no aporta una captura específica del teclado virtual.
- **NO IMPLEMENTADO NI PROBADO:** bridge C++ GDExtension CoreRPG real en Android ARM64, Gemini autenticado, sherpa-onnx ASR/TTS y mutación de WorldState real.

## Cierre pendiente
**Pruebas manuales solicitadas completadas**, incluida reanudación, según confirmación explícita del usuario el 15/10/2026. El alcance de NIM-02 queda validado funcionalmente en Android, limitado a interfaz y puertos sin backend. La PR permanece en Draft; pendiente revisión/autorización de fusión. Esta aprobación NO se extiende a CoreRPG, Gemini, sherpa-onnx ni un mundo jugable.

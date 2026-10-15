# NIM-02 — Validación visual del modo integración en Windows 11

**Fecha:** 15/10/2026. **Equipo objetivo:** MSI Windows 11 (según prueba comunicada por el usuario). **Evidencia:** tres capturas de la app NIM-02 remitidas por el usuario a la conversación; no se adjuntan capturas al repositorio. **Naturaleza de evidencia:** inspección visual, no telemetría, registro de eventos ni prueba de CoreRPG.

## Observaciones verificadas visualmente

- La aplicación muestra el estado `MODO INTEGRACIÓN · CORERPG / GEMINI / VOZ NO DISPONIBLES` y el control `Modo: integración`.
- Al enviar `Qué veo desde donde estoy?` aparece un bocadillo `TÚ` seguido por `SISTEMA · CONEXIÓN NO DISPONIBLE`, indicando `CoreRPG no está conectado: no se ha iniciado una partida ni ejecutado ninguna acción.`
- La prueba `Avanzo por la aldea` presenta también respuesta de sistema de Core no conectado; no declara desplazamiento.
- La prueba `Hablo con un aldeano` presenta respuesta de sistema de Core no conectado; no atribuye parlamento a NPC.
- El historial desplaza el contenido, conservando la barra de entrada y los botones visibles en estas capturas.
- En un intento de envío sin texto se muestra la indicación `Escribe un mensaje antes de enviarlo.`; no se observa una acción de mundo a partir de ese intento.
- La interfaz muestra `Sin hechos del mundo modificados`; esta frase es un indicador visual, no una medición instrumental de WorldState.

## Resultado limitado

**APROBADO visualmente para MSI Windows 11:** modo integración, bloqueo honesto por falta de CoreRPG, bocadillos de jugador/sistema, envío vacío rechazado, entrada visible e historial desplazable.

## Pendientes y exclusiones

- No hay evidencia nueva de pulsación de `Reiniciar demo` ni regreso efectivo a modo demo en estas tres capturas.
- No se verifica redimensionado, reanudación, estabilidad bajo carga, latencia, ni funcionamiento durante una sesión prolongada.
- No existe prueba de integración CoreRPG real, API Gemini autenticada, ASR/TTS sherpa-onnx o lectura real del estado de mundo.
- **Samsung Galaxy Tab S9+ pendiente:** el usuario indica que realizará la prueba cuando tenga disponible la tablet.
- PR #18 continúa en Draft; no fusionar hasta completar revisión y pruebas pendientes.

## Proveniencia

Las capturas se identificaron en la conversación como `image(20261015-113543).png`, `image(20261015-113603).png` y `image(20261015-113625).png`. Son imágenes aportadas por el usuario, no logs ni artefactos de una prueba automatizada.

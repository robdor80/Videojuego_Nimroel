# Nimroel Core — agenda personal y uso del tiempo v0.1

## Autoridad

**CORE UNIVERSAL — namespace AGEN**

Principios obligatorios:

- AGEN01–AGEN09 conservan exactamente su significado;
- el tiempo de un actor no puede duplicarse;
- actividades incompatibles no pueden ejecutarse en paralelo por el mismo NPC;
- una agenda coordina obligaciones de otros sistemas, pero no sustituye su autoridad;
- una intención o GOAL no reserva tiempo por sí sola;
- viaje, espera, descanso, diálogo, cuidado y necesidades consumen tiempo real;
- cambiar de lugar exige ruta y duración compatibles;
- retrasar requiere causa; reprogramar requiere una nueva ventana plausible;
- reprogramar a otra persona exige su disponibilidad o acuerdo cuando corresponda;
- cancelado y perdido son estados distintos;
- LOD no puede resolver simultáneamente intenciones incompatibles;
- la IA puede referirse a la agenda conocida, pero no crear disponibilidad inexistente.


---

## Integración con TIME

AGEN consume el calendario y reloj universal de:

`nimroel_world_time_calendar_contract_v0.1.json`

Una entrada puede usar:

- fecha/hora exacta;
- fecha sin hora;
- franja del día;
- ventana relativa;
- secuencia respecto a otra actividad.

El tiempo exacto está disponible, pero no es obligatorio para toda rutina.

Cuando una expresión relativa crea una obligación persistente, debe resolverse a un ancla no ambigua.

Ejemplo:

`mañana por la tarde`

puede conservar texto visible, pero internamente debe quedar ligado a la fecha correspondiente y a la franja `tarde`.

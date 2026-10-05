# Treskal — conflictos de agenda, retrasos y reprogramación v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO — CAMBIAR UN PLAN DEJA CONSECUENCIAS**

## Objetivo

Definir qué ocurre cuando dos obligaciones compiten o una actividad no sucede en el momento previsto.

---

# 1. Prioridad contextual

No existe una jerarquía universal única.

Pueden influir:

- peligro inmediato;
- cuidado urgente;
- obligación institucional;
- pledge;
- empleo;
- relación;
- necesidad física;
- objetivo;
- posibilidad de reprogramar.

DEC resuelve la elección cuando existe conflicto real.

---

# 2. Retraso

AGEN05 requiere una causa plausible.

Puede proceder de:

- trabajo anterior;
- viaje;
- clima;
- espera;
- accidente;
- conversación relevante;
- falta de recurso;
- cuidado.

El retraso no teletransporta la actividad siguiente.

---

# 3. Reprogramación

AGEN06 necesita:

- nueva ventana plausible;
- disponibilidad;
- aceptación de otras partes cuando corresponda.

Una persona no puede reprogramar unilateralmente el tiempo de otra como si también fuese suyo.

---

# 4. Cancelación

AGEN07 puede ser:

- voluntaria;
- forzada;
- resultado de evento;
- imposibilidad material.

La cancelación puede afectar:

- GOAL;
- PLEDGE;
- TRUST;
- VIEW;
- relación;
- reputación si se conoce.

No ocurre automáticamente.

---

# 5. Actividad perdida

AGEN08 significa que el momento pasó sin ejecución.

Debe distinguirse de:

- cancelación previa;
- retraso todavía recuperable.

Puede requerir explicación o reparación.

---

# 6. Pledge

Si el compromiso temporal estaba ligado a PLEDGE:

un retraso o ausencia puede ser:

- justificado;
- incumplimiento;
- renegociación.

PLEDGE decide el estado del compromiso.

AGEN solo registra qué ocurrió con el tiempo previsto.

---

# 7. Esperas

WAIT puede consumir tiempo de agenda.

Un NPC esperando servicio:

- sigue estando en un lugar;
- puede abandonar;
- puede perder otra actividad.

Esperar no es tiempo fuera del mundo.

---

# 8. Conversación

DIAL puede ocupar tiempo.

Una conversación larga puede:

- retrasar;
- interrumpir;
- ser cerrada

si otra actividad gana prioridad.

---

# 9. Necesidades

NEED puede obligar a introducir:

- comida;
- bebida;
- descanso;
- refugio.

No se programan jornadas infinitas sin mantenimiento cotidiano.

---

# 10. Trabajo pendiente

Una actividad no completada puede:

- moverse;
- quedar bloqueada;
- generar atraso;
- requerir sustitución.

COM, EMP, CHORE y CARE conservan sus consecuencias específicas.

---

# 11. Offscreen

La agenda es especialmente importante fuera de cámara.

Antes de resolver una actividad debe comprobarse:

- que había tiempo;
- que el actor estaba disponible;
- que podía llegar;
- que no existía conflicto superior.

LOD no permite ejecutar todas las intenciones de un NPC en paralelo.

---

# 12. Memoria y expectativas

Una cita incumplida o retraso significativo puede crear:

- MEM;
- EXP;
- TRUST;
- VIEW.

Solo para personas que conozcan el hecho.

---

# 13. IA

La IA puede proponer:

- aplazar;
- cancelar;
- reprogramar;
- priorizar.

El motor valida agenda, viaje, disponibilidad y consecuencias.

---

## Regla final

**En Treskal reprogramar algo no borra el tiempo perdido: cada cambio de agenda altera qué pudo hacer una persona y qué dejaron de poder esperar los demás.**

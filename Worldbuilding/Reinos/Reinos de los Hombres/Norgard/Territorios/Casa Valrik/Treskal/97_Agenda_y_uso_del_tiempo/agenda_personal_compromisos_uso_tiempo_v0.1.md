# Treskal — agenda personal, compromisos y uso del tiempo v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de AGEN reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/agenda_personal_uso_tiempo_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE NPC APROBADO — EL TIEMPO ES UN RECURSO Y NO PUEDE DUPLICARSE**

## Objetivo

Definir una agenda personal que coordine actividades existentes usando el reloj/calendario global cuando haga falta, sin obligar a expresar toda rutina con precisión de minuto.

La agenda debe impedir que un mismo NPC esté comprometido simultáneamente con actividades incompatibles.

---

# 1. Estados operativos

## AGEN01 — tentative_plan

Existe intención temporal aproximada, todavía flexible.

## AGEN02 — scheduled_activity

La actividad tiene una franja, secuencia o momento previsto suficientemente definido.

## AGEN03 — confirmed_commitment

La persona ha asumido un compromiso temporal con peso real.

## AGEN04 — in_progress

La actividad está ocurriendo.

## AGEN05 — delayed

La actividad sigue prevista, pero comienza o continúa más tarde de lo esperado.

## AGEN06 — rescheduled

La actividad se mueve a otro momento plausible.

## AGEN07 — cancelled

La actividad deja de estar prevista antes de ejecutarse.

## AGEN08 — missed

La actividad debía ocurrir y no se realizó.

## AGEN09 — completed

La actividad prevista terminó de forma suficiente.

---

# 2. Tiempo exacto y cualitativo

TIME ya permite que una entrada use:

- fecha/hora exacta;
- fecha sin hora;
- franja del día;
- secuencia relativa;
- después de otra actividad;
- antes de otra obligación;
- ventana temporal.

No toda rutina necesita precisión de minuto.

Cuando una promesa o compromiso persistente nace de una expresión como «mañana por la tarde», el World State la resuelve a la fecha correspondiente y conserva la franja.

---

# 3. Fuentes de agenda

Una entrada puede proceder de:

- EMP;
- CARE;
- REST;
- GOAL;
- PLEDGE;
- HOSP;
- viaje;
- COM;
- visita;
- servicio;
- evento.

La agenda coordina.

No reemplaza al sistema que creó la obligación.

---

# 4. Plan y compromiso

GOAL03 puede contener un siguiente paso.

Eso no significa que ya tenga un hueco reservado.

AGEN convierte una intención temporal en:

- previsión;
- compromiso;
- actividad real.

---

# 5. Conflicto temporal

Dos actividades son incompatibles si requieren al mismo actor:

- en lugares incompatibles;
- con atención exclusiva;
- durante el mismo periodo.

El sistema debe:

- priorizar;
- retrasar;
- reprogramar;
- cancelar;
- marcar ausencia.

No clona al NPC.

---

# 6. Desplazamiento

Cambiar de lugar requiere tiempo de viaje.

Una agenda no puede colocar al NPC:

- en un extremo de la ciudad;
- y acto seguido en otro lugar

sin ruta y tiempo compatibles.

TRAVEL y rutas siguen siendo autoridad.

---

# 7. Margen

Una agenda preindustrial no necesita precisión de calendario moderno.

Puede existir margen natural por:

- distancia;
- clima;
- trabajo;
- espera;
- preparación.

No todo retraso es incumplimiento.

---

# 8. Rutina

HAB y rutina base pueden generar actividades probables.

No todas necesitan entrada persistente.

AGEN se usa cuando:

- existe conflicto;
- compromiso;
- coordinación;
- consecuencia;
- expectativa.

---

# 9. Trabajo

EMP puede aportar patrones de jornada.

AGEN determina si ese trabajador concreto:

- debía estar;
- está;
- llegó tarde;
- fue sustituido;
- está ausente.

EMP conserva el estado laboral.

---

# 10. Cuidado

CARE puede reservar tiempo real.

Una persona que cuida a un dependiente no queda simultáneamente disponible para cualquier trabajo, visita o encargo.

---

# 11. Descanso

REST debe ocupar tiempo.

Una actividad no urgente no puede programarse ignorando REST05.

Una emergencia puede interrumpirlo mediante reglas ya existentes.

---

# 12. Jugador

El jugador puede acordar:

- verse más tarde;
- volver otro día;
- entregar algo antes de una fecha;
- esperar a que termine una tarea.

Solo se registra como compromiso si la interacción realmente lo establece.

---

# 13. IA

La IA puede conocer la agenda relevante del NPC.

Puede responder:

- “ahora no puedo”;
- “cuando termine esto”;
- “vuelve después”;
- “tenía que estar allí”.

No puede crear tiempo libre inexistente para satisfacer al jugador.

---

## Regla final

**En Treskal una persona solo tiene un día cada día: trabajar, cuidar, viajar, descansar y conversar compiten por el mismo tiempo real.**

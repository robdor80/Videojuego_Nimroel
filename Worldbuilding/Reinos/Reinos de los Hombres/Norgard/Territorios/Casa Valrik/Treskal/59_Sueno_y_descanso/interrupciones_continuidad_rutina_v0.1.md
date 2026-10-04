# Treskal — disponibilidad, interrupciones y continuidad de rutina v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Conectar REST con:

- EMP;
- BIZ;
- salud;
- mensajes;
- eventos;
- viajes.

---

# 1. Disponibilidad

Un actor puede exponer:

- available_for_work;
- available_for_social_interaction;
- available_for_emergency;
- current_rest_state.

Estas variables se derivan.

No deben guardarse como verdad independiente si pueden reconstruirse.

---

# 2. Interrupción prioritaria

Una emergencia puede romper REST.

Ejemplos:

- D03;
- ACC05;
- mensaje urgente legítimo;
- peligro doméstico.

Una consulta trivial no tiene la misma prioridad.

---

# 3. Retorno a rutina

Tras una interrupción:

el actor puede:

- volver a dormir;
- pasar a REST07;
- continuar actividad;
- perder parte de su descanso.

No vuelve automáticamente a estado ideal.

---

# 4. Trabajo

EMP02 no significa actividad continua.

Un trabajador puede estar:

- en pausa;
- fuera de turno;
- durmiendo.

El workplace_ref no determina su posición permanente.

---

# 5. Encargos

COM no progresa durante:

- sueño;
- ausencia;
- enfermedad;
- cierre incompatible.

Salvo trabajo de otro miembro real del equipo.

---

# 6. Emergencias nocturnas

Pueden generar:

- movilización de vecinos;
- guardia;
- trabajadores específicos.

No toda la ciudad se despierta automáticamente.

La propagación depende de:

- sonido;
- mensajería;
- proximidad;
- percepción.

---

## Regla final

**La disponibilidad debe surgir de la rutina y del estado, no de que exista una interacción posible en la interfaz.**

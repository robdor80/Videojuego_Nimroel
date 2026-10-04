# Treskal — red de cuidados y disponibilidad doméstica v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Conectar CARE con:

- household;
- EMP;
- REST;
- salud;
- residencia;
- relaciones.

---

# 1. Registro relevante

Una necesidad importante puede mantener:

- care_case_id;
- dependent_ref;
- dependency_type;
- household_ref;
- primary_carer_refs;
- secondary_carer_refs;
- coverage_state;
- location_ref;
- health_ref_if_any;
- support_network_refs;
- last_update_time.

---

# 2. Capacidad de cuidado

Puede derivarse de:

- cuidadores disponibles;
- relación;
- presencia;
- salud del cuidador;
- REST;
- EMP;
- distancia;
- intensidad de necesidad.

No es un recurso abstracto infinito.

---

# 3. Relevo

La cobertura puede transferirse temporalmente.

Ejemplo:

A cuida por la mañana, B por la tarde.

No se fija horario exacto hasta sistema temporal.

---

# 4. Cambio de rutina

Si CARE cambia:

puede modificar:

- workplace attendance;
- viaje;
- compra;
- descanso;
- interacción social.

El sistema causal aplica consecuencias.

---

# 5. Apoyo externo

CARE06 puede depender de:

- vecino;
- familiar de otro hogar;
- persona pagada;
- institución futura si alguna existe.

Debe existir actor real.

---

# 6. Traslado

CARE07 puede enlazar con MOVE/RES.

Mover a una persona por cuidado requiere:

- destino;
- espacio;
- transporte si procede;
- acuerdo/autoridad futura.

---

# 7. Persistencia

La necesidad no se recalcula desde cero al cargar.

Se conserva:

- caso;
- red;
- cobertura;
- cambios históricos relevantes.

---

## Regla final

**La red de cuidados es una red social real: si una persona falta, alguien concreto debe ocupar su lugar o aparece una brecha.**

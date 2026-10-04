# Treskal — respuesta a accidente y continuidad operativa v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Cerrar la secuencia:

**riesgo → incidente → respuesta → recuperación → continuidad o cambio**

---

# 1. Estados de incidente

## ACC01 — hazard_detected

Se detecta una condición peligrosa antes de accidente.

## ACC02 — near_miss

Ocurre incidente sin daño relevante.

## ACC03 — minor_incident

Daño/lesión limitada.

## ACC04 — serious_incident

Consecuencia importante.

## ACC05 — critical_incident

Amenaza grave para persona, estructura o actividad.

## ACC06 — stabilized

Peligro inmediato controlado.

## ACC07 — follow_up

Quedan reparación, salud, investigación o reorganización.

## ACC08 — closed

Consecuencias principales resueltas.

---

# 2. Aplicación

Un ACC importante debe registrar:

- incident_id;
- hazard_type;
- cause_refs;
- location_refs;
- actor_refs;
- tool_or_object_refs;
- injury_refs;
- damage_refs;
- witness_refs;
- state;
- response_refs;
- persistent_consequences.

---

# 3. Detección previa

ACC01 puede provocar:

- mantenimiento;
- pausa;
- cambio de ruta;
- sustitución de herramienta.

Eso puede evitar accidente.

No se premia siempre con evento dramático.

---

# 4. Respuesta inmediata

Orden conceptual:

1. proteger a personas;
2. detener peligro activo;
3. pedir ayuda;
4. asegurar zona;
5. recuperar operación cuando sea seguro.

No se fija protocolo institucional universal.

---

# 5. Continuidad

Tras estabilizar:

el trabajo puede:

- continuar;
- reducirse;
- pausarse;
- cerrar temporalmente.

Depende de:

- personal;
- equipo;
- daño;
- acceso;
- materiales.

---

# 6. Sustitución

Un trabajador lesionado puede generar:

- EMP03/04;
- vacante temporal;
- sustitución;
- retraso.

No aparece reemplazo instantáneo.

---

# 7. Reparación

Herramienta, carro, edificio o estación dañada sigue su sistema:

- TOOL;
- COND;
- repair job;
- BUILD si procede.

ACC no repara nada por sí mismo.

---

# 8. Investigación social

Un responsable puede preguntar:

- qué pasó;
- quién estaba;
- qué herramienta se usó;
- qué se sabía antes.

Eso genera conocimiento.

No crea automáticamente proceso judicial.

---

# 9. Reputación

Puede cambiar solo si:

- el hecho se conoce;
- se interpreta;
- tiene relevancia.

Un accidente inevitable no equivale a mala reputación.

---

## Regla final

**Un accidente termina cuando sus consecuencias se han resuelto, no cuando desaparece el efecto visual inmediato.**

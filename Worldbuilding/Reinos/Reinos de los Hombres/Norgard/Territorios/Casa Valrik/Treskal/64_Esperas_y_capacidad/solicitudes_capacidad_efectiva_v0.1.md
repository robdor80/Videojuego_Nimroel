# Treskal — solicitudes de servicio y capacidad efectiva v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de WAIT reside en `Worldbuilding/Sistemas/Nimroel Core/03_Actividad_y_tiempo/espera_capacidad_servicio_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Unificar capacidad de atención entre negocios, especialistas e instituciones.

---

# 1. Solicitud persistente

Una solicitud relevante puede registrar:

- request_id;
- requester_ref;
- provider_ref;
- service_type;
- location_ref;
- created_time;
- wait_state;
- urgency;
- commitment_ref_if_any;
- required_resources;
- resolution.

---

# 2. Capacidad efectiva

Puede depender de:

- trabajadores presentes;
- capacidad individual;
- estaciones;
- stock/material;
- espacio;
- estado BIZ;
- REST;
- EMP;
- evento.

No equivale a plantilla teórica.

---

# 3. Servicio simultáneo

Algunos servicios permiten:

- varios clientes a la vez.

Otros requieren:

- atención individual.

Lo define service_type.

---

# 4. Duración

No se fija universalmente.

Puede depender de:

- servicio;
- complejidad;
- conversación;
- material;
- interrupción.

---

# 5. Preempción

Una solicitud en curso o pendiente puede ceder prioridad a emergencia.

Debe quedar causa registrada.

No se cancela automáticamente.

---

# 6. Cierre

Si el proveedor cierra:

WAIT puede:

- diferirse;
- abandonarse;
- trasladarse a otro proveedor.

No se resuelve como completed.

---

# 7. Ausencia

Si el proveedor sale o enferma:

la espera puede aumentar.

No se materializa un sustituto salvo EMP válido.

---

# 8. Recursos

Si el proveedor tiene tiempo pero no material:

la solicitud puede quedar WAIT05.

Esto conecta espera con stock.

---

# 9. Reputación

Una espera larga no produce automáticamente mala reputación.

Puede hacerlo si:

- existe compromiso;
- gestión deficiente conocida;
- trato injusto percibido;
- información se propaga.

---

# 10. Persistencia

Una solicitud importante sobrevive:

- LOD;
- save/load;
- ausencia temporal.

No se reinicia al volver a hablar.

---

## Regla final

**La capacidad de servicio se calcula con personas, recursos y tiempo presentes, no con el icono de un establecimiento.**

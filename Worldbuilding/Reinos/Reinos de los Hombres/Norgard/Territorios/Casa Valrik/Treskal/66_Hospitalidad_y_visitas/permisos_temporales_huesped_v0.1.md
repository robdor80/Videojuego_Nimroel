# Treskal — permisos temporales de huésped y convivencia breve v0.1

## Estado

**DISEÑO DE WORLD STATE APROBADO**

## Objetivo

Conectar hospitalidad con:

- P3;
- DOOR;
- REST;
- CARE;
- propiedad;
- residencia;
- consumo.

---

# 1. Registro de estancia

Una estancia relevante puede mantener:

- hospitality_id;
- guest_ref;
- host_refs;
- household_ref;
- location_ref;
- hosp_state;
- allowed_areas;
- start_time;
- expected_end_if_any;
- overnight_allowed;
- object_custody_refs;
- revocation_reason_if_any.

---

# 2. Alcance

allowed_areas puede limitar acceso.

Ejemplo:

- sala común;
- patio;
- habitación asignada;
- comedor.

No se hereda acceso a todo building_id.

---

# 3. Caducidad

El permiso termina cuando:

- concluye visita;
- llega fecha/acuerdo;
- anfitrión revoca;
- invitado se marcha.

El motor debe retirar autorización temporal.

---

# 4. Estancia y residencia

HOSP05 puede convertirse en transición hacia RES.

Pero requiere una actualización explícita de:

- home_location;
- household;
- resident_state.

No ocurre por contador de noches.

---

# 5. Consumo

Un huésped puede aumentar:

- comida;
- agua;
- combustible;
- espacio;
- carga doméstica.

En LOD bajo puede agregarse al household consumption.

---

# 6. Guardado

La estancia relevante persiste en save/load.

El huésped no aparece expulsado o residente por recargar.

---

## Regla final

**El permiso de huésped es temporal, acotado y persistente: cambia acceso y consumo, no identidad ni propiedad.**

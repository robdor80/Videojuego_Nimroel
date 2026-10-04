# Treskal — alojamiento, estancia y memoria de posada v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO**

## Objetivo

Convertir alojamiento en una relación real entre:

- huésped;
- establecimiento;
- habitación/espacio;
- propietario;
- World State.

---

# 1. Estancia

Una estancia relevante puede registrar:

- lodging_id;
- guest_ref;
- inn/business_ref;
- room_or_space_ref;
- arrival_time;
- expected_departure;
- actual_departure;
- payment_state si corresponde;
- incidents;
- access_rights.

---

# 2. Derecho temporal de acceso

Una habitación ocupada por el jugador o NPC puede pasar de:

- P3 privada para extraños;
- a acceso legítimo para el huésped durante su estancia.

Eso no da acceso a:

- otras habitaciones;
- almacén;
- cocina;
- vivienda privada.

---

# 3. Ausencia del huésped

La habitación sigue asignada mientras la estancia continúe.

No se vende inmediatamente a otro NPC porque el huésped salió a la calle.

---

# 4. Equipaje

Un huésped puede dejar pertenencias.

Los objetos persistentes relevantes deben permanecer asociados a:

- habitación;
- huésped;
- establecimiento.

No se borra equipaje al descargar interior.

---

# 5. Disponibilidad

La disponibilidad depende de:

- capacidad;
- huéspedes actuales;
- reservas/compromisos si el futuro sistema los permite;
- habitaciones fuera de servicio;
- evento.

---

# 6. Información del posadero

El posadero no “ve” todo lo que ocurre en habitaciones.

Conoce aquello que:

- presenció;
- le contaron;
- pudo inferir;
- registró de su negocio.

---

# 7. Incidente

Puede ocurrir:

- robo;
- pelea;
- daño;
- enfermedad;
- muerte;
- impago.

El evento afecta:

- reputación;
- acceso;
- guardia;
- huéspedes;
- negocio.

---

# 8. Salida

Al terminar estancia:

- se libera espacio;
- se actualiza población temporal;
- el huésped inicia viaje o cambia alojamiento.

---

# 9. LOD

Una posada fuera de escena puede resolver agregadamente:

- ocupación;
- consumo;
- llegadas;
- salidas.

Los huéspedes persistentes siguen conservando identidad y estancia.

---

## Regla final

**Dormir en una posada de Treskal significa ocupar un lugar concreto dentro de un negocio concreto durante un tiempo real.**

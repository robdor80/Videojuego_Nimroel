# Treskal — encargos artesanales y producción por encargo v0.1

## Estado

**DISEÑO ECONÓMICO/JUGABLE APROBADO — ENCARGOS PERSISTENTES**

## Objetivo

Formalizar el proceso de encargar una pieza o trabajo a:

- carpintero;
- ebanista;
- herrero;
- sastre;
- zapatero;
- constructor;
- otro artesano compatible.

Sin fijar todavía moneda, tarifas ni derecho contractual detallado.

---

# 1. Encargo ≠ compra inmediata

Un encargo crea una obligación de producción futura.

Debe distinguirirse de:

- comprar stock existente;
- pedir presupuesto;
- preguntar disponibilidad.

---

# 2. Estados del encargo

## COM01 — requested

El cliente solicita trabajo.

## COM02 — quoted_or_discussed

Se han discutido:

- requisitos;
- materiales;
- plazo;
- precio/condiciones cuando proceda.

Aún puede no existir aceptación.

## COM03 — accepted

Ambas partes aceptan el encargo.

## COM04 — waiting_materials

Faltan materiales adecuados.

## COM05 — materials_reserved

El material necesario está apartado.

## COM06 — in_progress

Trabajo iniciado.

## COM07 — paused

Interrumpido por causa real.

## COM08 — ready

Trabajo terminado y pendiente de entrega.

## COM09 — delivered

La pieza/trabajo llegó al cliente.

## COM10 — completed

Obligaciones principales cerradas.

## COM11 — cancelled

Cancelado por acuerdo o causa válida.

## COM12 — failed

No pudo completarse y requiere resolución.

---

# 3. Campos mínimos

Un encargo relevante puede registrar:

- commission_id;
- customer_ref;
- provider_ref;
- business_ref;
- requested_work;
- specification;
- material_requirements;
- reserved_material_refs;
- agreed_quality_or_expectation;
- agreed_price_or_payment_terms_if_any;
- deadline_if_any;
- pledge_ref_if_any;
- state;
- progress;
- created_time;
- delivery_ref;
- final_object_ref;
- failure_or_delay_cause.

---

# 4. Especificación

Debe ser suficientemente clara para el trabajo.

Puede incluir:

- función;
- dimensiones futuras si sistema las necesita;
- material;
- acabado;
- calidad;
- personalización;
- destino.

No toda pieza necesita modelado paramétrico detallado.

---

# 5. Aceptación

El artesano puede rechazar por:

- falta de capacidad;
- plazo imposible;
- material inadecuado;
- carga de trabajo;
- falta de herramientas;
- trabajo fuera de especialidad;
- relación.

La UI no obliga a aceptar.

---

# 6. Material

Un encargo puede requerir:

- material del artesano;
- material aportado por cliente;
- material comprado a tercero.

Debe registrarse propiedad y reserva.

---

# 7. Reserva

Al pasar a material reservado:

- deja de ser stock libre;
- sigue existiendo físicamente;
- conserva propietario según acuerdo.

No se duplica para otros encargos.

---

# 8. Sustitución de material

Si falta el material acordado:

el artesano puede proponer alternativa.

No debe sustituirlo en secreto si cambia:

- calidad;
- apariencia;
- durabilidad;
- precio;
- naturaleza del acuerdo.

La aceptación del cliente puede ser necesaria.

---

# 9. Trabajo

El progreso depende de:

- trabajador;
- experiencia;
- tiempo;
- material;
- herramienta;
- interrupciones;
- dificultad.

No avanza por simple temporizador si faltan entradas esenciales.

---

# 10. Varios trabajadores

Un encargo grande puede involucrar:

- maestro;
- trabajadores;
- aprendices;
- otro oficio.

La calidad no se calcula solo con skill del propietario.

---

# 11. Pausa

Puede ocurrir por:

- enfermedad;
- accidente;
- material faltante;
- herramienta rota;
- incendio;
- viaje;
- evento.

La causa persiste.

---

# 12. Plazo

Puede ser:

- explícito;
- aproximado;
- sin plazo.

Si se da la palabra sobre fecha o resultado:

puede vincularse a pledge.

El incumplimiento se evalúa mediante sistema de honor.

---

# 13. Precio

Puede acordarse:

- al aceptar;
- por etapas;
- al entregar;
- según futuro sistema económico.

No se fija fórmula universal.

Un precio acordado no cambia retroactivamente sin causa/renegociación.

---

# 14. Calidad final

Deriva de:

- material;
- preparación;
- trabajador;
- herramientas;
- tiempo;
- dificultad;
- errores;
- acabado.

No de nivel del jugador.

---

# 15. Objeto final

Una pieza personalizada o relevante debe recibir:

- object_id persistente;
- maker_ref;
- material history;
- commission_ref;
- owner_ref;
- condition.

No se rerollea tras entrega.

---

# 16. Entrega

Puede ser:

- recogida en taller;
- entrega por trabajador;
- transporte contratado.

La entrega física importa para piezas voluminosas.

---

# 17. Cancelación

Debe resolver:

- materiales;
- trabajo ya realizado;
- propiedad;
- pago;
- pledge;
- objeto parcial.

No se borra todo al cambiar state.

---

# 18. Fallecimiento o cierre

Si el artesano muere o negocio cierra:

el encargo puede:

- continuar con otro trabajador capaz;
- transferirse;
- devolverse;
- cancelarse;
- fallar.

No desaparece.

---

# 19. Información del cliente

El cliente conoce el progreso solo mediante:

- visita;
- mensaje;
- relación;
- observación.

No recibe barra omnisciente de progreso salvo decisión futura de UI no diegética.

---

# 20. Offscreen

El trabajo puede avanzar fuera de escena si:

- artesano disponible;
- negocio activo;
- material presente;
- herramientas funcionales;
- tiempo suficiente.

---

## Regla final

**Un encargo de Treskal es una cadena real de acuerdos, material y trabajo; la pieza existe porque alguien la hizo.**

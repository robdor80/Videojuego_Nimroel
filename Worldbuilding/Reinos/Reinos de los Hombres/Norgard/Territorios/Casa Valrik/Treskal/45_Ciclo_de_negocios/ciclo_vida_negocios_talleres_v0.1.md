# Treskal — ciclo de vida de negocios y talleres v0.1

## Estado

**DISEÑO ECONÓMICO/JUGABLE APROBADO — NEGOCIOS PERSISTENTES**

## Objetivo

Separar claramente:

- negocio;
- propietario;
- edificio;
- trabajadores;
- stock;
- reputación.

Para que un cambio en uno no destruya automáticamente los demás.

---

# 1. Identidad del negocio

Un negocio persistente puede tener:

- business_id;
- activity_type;
- building_id;
- owner_ref;
- worker_refs;
- stock_refs;
- supplier_refs;
- customer_refs relevantes;
- reputation_refs;
- schedule;
- state;
- name_if_any.

---

# 2. Negocio ≠ edificio

Un edificio puede:

- alojar un negocio;
- cambiar de negocio;
- quedar sin negocio;
- alojar varios usos compatibles.

El building_id permanece aunque el negocio cierre.

---

# 3. Negocio ≠ propietario

Un negocio puede continuar si cambia:

- propietario;
- maestro;
- encargado.

La continuidad depende de:

- trabajadores;
- herramientas;
- stock;
- clientela;
- autorización y legalidad aplicable;
- capacidad.

---

# 4. Estados de negocio

## BIZ01 — preparing

Todavía no opera plenamente.

## BIZ02 — open

Actividad ordinaria.

## BIZ03 — reduced

Opera con capacidad limitada.

## BIZ04 — temporarily_closed

Cierre temporal.

## BIZ05 — relocating

Traslado de actividad.

## BIZ06 — dormant

Existe como entidad/propiedad, pero sin operación activa.

## BIZ07 — permanently_closed

La actividad terminó.

## BIZ08 — transferred_or_reorganized

Está en transición de dueño/estructura.

Este estado no resuelve por sí mismo la legalidad de la transferencia.

---

# 5. Apertura

Un negocio nuevo necesita:

- actividad plausible;
- persona(s) capaces;
- espacio;
- herramientas/instalaciones;
- stock o materiales cuando proceda;
- demanda suficiente o motivo.

No se genera porque haya “slot de tienda vacío”.

---

# 6. Preparación

Antes de abrir puede requerir:

- acondicionar edificio;
- mover herramientas;
- traer stock;
- colocar rótulo;
- crear relación con proveedores.

Puede producir actividad visible antes de la apertura.

---

# 7. Cierre temporal

Puede deberse a:

- enfermedad;
- accidente;
- falta de material;
- viaje;
- reparación;
- evento;
- ausencia de personal.

El business_id se conserva.

---

# 8. Capacidad reducida

Un negocio puede seguir parcialmente activo si:

- falta propietario pero hay trabajador competente;
- falta stock concreto;
- parte del edificio está dañada;
- hay menos personal.

No todo problema equivale a cierre.

---

# 9. Cierre permanente

Puede resultar de:

- decisión;
- muerte sin continuidad;
- ruina económica futura;
- destrucción;
- traslado fuera de ciudad;
- cambio de oficio.

El stock, herramientas y edificio no desaparecen automáticamente.

---

# 10. Muerte del propietario

Puede producir:

- continuidad familiar;
- continuidad por trabajador/encargado;
- pausa;
- cierre;
- transición legal futura.

La herencia exacta se rige por el Punto 8 de Norgard. La participación privada del fallecido entra en el caudal, pero el negocio, sus trabajadores, herramientas, stock y encargos no desaparecen.

---

# 11. Cambio de propietario

Puede conservar:

- business_id si existe continuidad real;
- clientela;
- parte de reputación;
- proveedores;
- trabajadores.

Pero puede cambiar:

- nombre;
- estilo;
- calidad;
- relaciones.

No se decide solo por “mismo edificio”.

---

# 12. Mudanza

Un negocio puede mover actividad a otro building_id.

Debe mover o resolver:

- stock;
- herramientas;
- rótulo;
- trabajadores;
- accesos;
- conocimiento de clientes.

Durante un tiempo puede existir información desactualizada sobre su ubicación.

---

# 13. Reputación

Debe distinguirse:

- reputación del negocio;
- reputación del propietario;
- reputación del maestro/artesano.

Pueden correlacionarse sin ser idénticas.

---

# 14. Nombre

Un negocio puede tener:

- nombre propio;
- nombre basado en propietario;
- descripción funcional;
- ningún nombre formal.

Cambiar de propietario no obliga a renombrar ni conservar nombre.

---

# 15. Stock al cierre

Puede:

- venderse;
- trasladarse;
- quedar almacenado;
- devolverse;
- transferirse;
- deteriorarse.

No desaparece al poner state = permanently_closed.

---

# 16. Encargos abiertos

Al cerrar o cambiar responsable:

pueden:

- continuar;
- transferirse;
- retrasarse;
- devolverse;
- cancelarse.

Cada encargo se resuelve individualmente.

---

# 17. Trabajadores

Un cierre puede causar:

- desempleo;
- traslado;
- contratación por otro negocio;
- aprendizaje interrumpido.

No son parte inseparable del business_id.

---

# 18. Proveedores

La relación con proveedores puede:

- continuar;
- renegociarse;
- romperse.

Un nuevo dueño no hereda automáticamente toda confianza personal.

---

# 19. Descubrimiento del cambio

Los NPC y el jugador conocen:

- cierre;
- mudanza;
- nuevo dueño

según:

- observación;
- mensajes;
- rumor;
- relación.

El mapa puede quedar desactualizado hasta recibir información nueva.

---

# 20. Offscreen

Un negocio puede cambiar de estado fuera de escena.

Al volver:

- rótulo;
- actividad;
- stock;
- NPC

deben reflejar el estado nuevo.

---

## Regla final

**En Treskal los negocios tienen historia: pueden sobrevivir a su dueño, mudarse, decaer o cerrar, pero nada de eso borra mágicamente el mundo que dejan detrás.**


---

# 21. Integración con propiedad y herencia

Punto 8 distingue el negocio de:

- edificio;
- propietario;
- stock;
- herramientas;
- trabajadores;
- reputación.

La muerte del propietario puede activar BIZ08, administración hereditaria, continuidad, cierre temporal, transferencia o liquidación.

Un heredero recibe únicamente la participación que realmente formaba parte del caudal.

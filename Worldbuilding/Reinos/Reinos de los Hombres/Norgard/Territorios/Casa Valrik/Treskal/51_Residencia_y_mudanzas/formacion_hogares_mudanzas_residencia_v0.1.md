# Treskal — formación de hogares, mudanzas y residencia v0.1

## Estado

**DISEÑO SOCIAL/JUGABLE APROBADO — POBLACIÓN PERSISTENTE Y CAMBIANTE**

## Objetivo

Definir cómo puede cambiar la población residencial de Treskal durante una partida mediante:

- formación de hogares;
- separación;
- mudanza;
- acogida;
- llegada de nuevos residentes;
- salida de residentes.

Sin fijar todavía:

- matrimonio legal;
- herencia;
- alquiler;
- compraventa de vivienda;
- empadronamiento formal.

---

# 1. Residente ≠ visitante

Un visitante V01–V09 sigue siendo visitante mientras:

- mantenga estancia temporal;
- no establezca hogar estable;
- no ocurra un cambio real de World State.

Permanecer muchos días no basta por sí solo.

---

# 2. Cambio a residente

Un visitante puede convertirse en residente si confluyen elementos plausibles como:

- decisión de quedarse;
- alojamiento estable;
- trabajo/actividad;
- relación familiar;
- incorporación a un hogar;
- disponibilidad residencial.

No se exige que todos estos factores estén presentes a la vez.

---

# 3. Resident status

Puede manejar estados conceptuales:

## RES01 — resident

Reside de forma estable en Treskal.

## RES02 — temporary_resident_like

Estancia prolongada con fuerte integración práctica, pero aún temporal.

## RES03 — departing

Está cerrando su residencia y prepara salida.

## RES04 — former_resident

Ya no vive en Treskal, aunque mantiene memoria/relaciones.

## RES05 — displaced

Sigue perteneciendo socialmente a Treskal pero perdió temporalmente su vivienda por:

- incendio;
- inundación;
- daño;
- conflicto doméstico;
- otra causa real.

---

# 4. Household lifecycle

Un household_id puede:

- formarse;
- crecer;
- reducirse;
- dividirse;
- fusionarse;
- mudarse;
- extinguirse como unidad doméstica.

Sus miembros mantienen npc_id.

---

# 5. Formación de hogar

Puede surgir por:

- pareja/familia;
- parientes que comparten vivienda;
- adultos que deciden convivir;
- aprendiz residente;
- trabajador residente;
- alojamiento ligado a negocio.

No todos los hogares nuevos necesitan vínculo romántico.

---

# 6. Incorporación

Una persona puede entrar en hogar existente por:

- parentesco;
- acogida;
- aprendizaje;
- trabajo;
- necesidad;
- relación personal.

El motor actualiza:

- household_id;
- home_location_id;
- relaciones de convivencia.

No borra su historia previa.

---

# 7. Salida de hogar

Puede ocurrir por:

- independencia;
- conflicto;
- empleo;
- mudanza;
- viaje prolongado;
- formación de nuevo hogar.

Salir del hogar no rompe automáticamente relaciones familiares.

---

# 8. División

Un hogar puede dividirse.

Ejemplo:

- dos adultos forman una nueva unidad;
- un familiar se muda;
- parte de familia se desplaza por trabajo.

Los objetos compartidos deben resolverse según propiedad/custodia.

La regla jurídica exacta queda pendiente.

---

# 9. Fusión

Dos hogares pueden compartir vivienda temporal o permanentemente.

Puede ocurrir por:

- familia;
- necesidad;
- daño;
- economía;
- cuidado.

No significa que todos los bienes pasen a propiedad común.

---

# 10. Mudanza

Una mudanza relevante puede registrar:

- move_id;
- household_or_person_ref;
- origin_home_ref;
- destination_home_ref;
- cause;
- planned_time;
- actual_time;
- transport_need;
- state.

---

# 11. Estados de mudanza

## MOVE01 — planned

Destino previsto.

## MOVE02 — preparing

Se organizan bienes/traslado.

## MOVE03 — in_progress

El cambio físico está ocurriendo.

## MOVE04 — completed

Nuevo hogar activo.

## MOVE05 — interrupted

No terminó.

## MOVE06 — cancelled

No se realizará.

---

# 12. Bienes

Una mudanza puede mover:

- ropa;
- herramientas propias;
- muebles;
- objetos familiares;
- materiales;
- documentos.

No todo cabe en inventario personal.

Puede requerir:

- carro;
- ayuda;
- tiempo.

---

# 13. Negocio y vivienda

En casas-taller o posadas:

cambiar de vivienda puede afectar:

- empleo;
- negocio;
- acceso;
- rutina.

Pero mover hogar no mueve automáticamente business_id.

---

# 14. Desplazamiento por emergencia

Si una vivienda queda inutilizable:

el hogar puede pasar a RES05.

Opciones de alojamiento:

- familia;
- amistades;
- posada;
- alojamiento temporal compatible;
- otra vivienda disponible.

No aparece una casa sustituta automática.

---

# 15. Presión residencial

La llegada de nuevos residentes y los desplazamientos pueden aumentar:

- residentialPressureState;
- ocupación de posadas;
- viviendas compartidas;
- distancia hogar-trabajo.

La ciudad debe reaccionar antes de crear edificios de la nada.

---

# 16. Salida de Treskal

Un residente puede marcharse.

Debe conservar:

- npc_id;
- relaciones;
- memoria;
- profesión;
- propiedad relevante.

Su home_location_id deja de apuntar a vivienda activa en Treskal.

---

# 17. Regreso

Un antiguo residente puede volver.

No se genera como persona nueva.

Puede:

- recuperar relaciones;
- buscar nuevo hogar;
- volver con hogar distinto.

---

# 18. Nacimiento y muerte

Pueden alterar hogares.

Este documento no define:

- embarazo;
- parto fisiológico;
- herencia;
- tutela legal.

Solo permite que el hogar cambie cuando esos sistemas lo determinen.

---

# 19. Separación social y jurídica

La convivencia puede cambiar antes de que futuros sistemas legales definan:

- matrimonio;
- propiedad;
- herencia;
- obligaciones.

No se inventan consecuencias legales aquí.

---

# 20. LOD

En LOD bajo pueden resolverse:

- household membership;
- housing assignment;
- moves;
- displacement.

Al volver al área:

las personas aparecen donde corresponde al nuevo estado.

---

## Regla final

**La población de Treskal cambia porque personas reales llegan, se quedan, forman hogares, se mudan y se marchan; la ciudad no recalcula habitantes como una tabla estática.**

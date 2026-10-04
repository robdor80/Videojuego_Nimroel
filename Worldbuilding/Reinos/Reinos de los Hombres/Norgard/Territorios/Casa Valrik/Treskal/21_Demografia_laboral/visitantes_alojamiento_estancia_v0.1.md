# Treskal — visitantes, alojamiento y estancia temporal v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO — POBLACIÓN NO RESIDENTE**

## Objetivo

Resolver quién entra en Treskal, dónde permanece y cuándo deja de contar como visitante.

---

# 1. Categorías técnicas

## V01 — Comerciante terrestre

Llega por:

- rutas regionales;
- Villas;
- Pueblos;
- otros territorios.

Motivo:

- comprar;
- vender;
- cerrar acuerdos.

## V02 — Habitante rural de visita

Motivos:

- mercado;
- compra;
- administración;
- justicia;
- salud;
- familia.

## V03 — Marinero o tripulación civil

Vinculado a barco presente.

Puede dormir:

- a bordo;
- en posada;
- en alojamiento relacionado.

## V04 — Comerciante marítimo

Puede combinar:

- barco;
- almacén;
- posada;
- negociación.

## V05 — Representante de Casa menor

Motivos:

- La Casa;
- justicia;
- tributos;
- asuntos territoriales.

Puede viajar con pequeña comitiva según contexto.

## V06 — Litigante, testigo o persona citada

Vinculado a T06.

Puede necesitar estancia de varios días.

## V07 — Trabajador temporal

Motivos:

- carga;
- obra;
- cosecha/logística;
- contrato naval;
- reparación.

## V08 — Proveedor institucional

Puede dirigirse a:

- La Casa;
- Justicia;
- Astilleros Reales.

El acceso depende de autorización.

## V09 — Viajero en tránsito

No tiene por qué realizar actividad económica relevante.

---

# 2. Estado de visitante

Todo visitante relevante puede registrar:

- visitor_id o npc_id;
- origin;
- reason;
- arrival_time;
- expected_departure;
- lodging_ref;
- activity_refs;
- relationship_refs;
- departure_state.

---

# 3. Alojamiento

Puede resolverse mediante:

## Posada

Opción principal para desconocidos con recursos.

## Barco

Tripulaciones pueden permanecer a bordo cuando sea razonable.

## Familia o amistad

Un visitante puede alojarse en hogar conocido.

## Empleador o instalación

Posible para:

- trabajadores;
- aprendices;
- servicio;
- contratos concretos.

## Dependencia institucional

Solo cuando la función lo justifique.

No se presupone alojamiento público gratuito universal.

---

# 4. Capacidad

Las posadas tienen capacidad finita.

Una llegada excepcional puede provocar:

- ocupación alta;
- precios mayores si el sistema económico lo justifica;
- búsqueda de alternativas;
- estancias fuera del centro.

No aparecen habitaciones infinitas.

---

# 5. Duración

Ejemplos:

- mercado: horas;
- trámite: uno o varios días;
- juicio: duración variable;
- mercante: según carga;
- reparación: hasta terminar trabajo;
- contrato temporal: días o más.

No se usa una duración universal.

---

# 6. Entrada y salida

La población temporal debe aumentar al llegar y descender al marcharse.

Si el NPC se materializó como persistente, puede seguir existiendo fuera de Treskal mediante estado de viaje o referencia externa.

---

# 7. Convertirse en residente

Requiere cambio real:

- vivienda;
- empleo o sustento;
- decisión;
- vínculo doméstico;
- traslado.

No basta con permanecer varios días.

---

# 8. Ausencia de un residente

Un residente que sale temporalmente de Treskal sigue siendo residente mientras no cambie su hogar estable.

El World State distingue:

**residencia** de **posición actual**.

---

# 9. Demanda urbana

Los visitantes afectan:

- posadas;
- tabernas;
- mercado;
- tráfico;
- rumor;
- precios puntuales;
- densidad.

No deben alterar permanentemente la capacidad base por una visita ordinaria.

---

# 10. Eventos

D07 llegada importante de mercante puede elevar:

- V03;
- V04.

D11 alta actividad judicial puede elevar:

- V05;
- V06.

D05 convoy de madera puede elevar:

- V07.

---

## Regla final

**Treskal no confunde a quien está hoy en la ciudad con quien pertenece a ella.**

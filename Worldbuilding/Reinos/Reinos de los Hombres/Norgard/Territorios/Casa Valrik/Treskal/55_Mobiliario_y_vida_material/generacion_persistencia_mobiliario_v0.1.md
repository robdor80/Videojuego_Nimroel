# Treskal — generación y persistencia de mobiliario interior v0.1

## Estado

**DISEÑO DE RUNTIME APROBADO**

## Objetivo

Generar interiores variados manteniendo:

- función;
- economía;
- identidad;
- persistencia.

---

# 1. Inputs de materialización

Un interior puede derivar mobiliario desde:

- building_type_U;
- room_function;
- household_template_H;
- occupants;
- occupation_O;
- economic_capacity;
- business_activity;
- storage_need;
- local_material_culture;
- stable_seed;
- persisted_state.

---

# 2. Prioridad

Orden:

1. estado persistido;
2. hechos autorales;
3. necesidades funcionales;
4. capacidad económica;
5. variante determinista.

Nunca al revés.

---

# 3. Clases de persistencia

## furnishing_aggregate

Mobiliario ordinario no interactuado.

## furnishing_persistent

Objeto:

- movido;
- robado;
- dañado;
- reparado;
- regalado;
- marcado;
- narrativamente relevante.

---

# 4. Promoción

Un objeto agregado puede convertirse en persistente.

Debe recibir:

- item_id;
- owner_ref;
- location_ref;
- condition;
- materialization history mínima.

No vuelve al pool agregado.

---

# 5. Variación

Dos hogares similares pueden diferir en:

- disposición;
- cantidad;
- reparación;
- tipo de asiento;
- almacenamiento;
- calidad.

Sin romper necesidades básicas.

---

# 6. Economía

Mayor capacidad económica puede aumentar:

- calidad;
- cantidad;
- especialización;
- espacio.

No obliga a:

- mobiliario nuevo;
- ornamentación excesiva.

---

# 7. Desocupación

Si un hogar abandona un edificio:

el contenido se resuelve según:

- propiedad;
- mudanza;
- venta;
- abandono;
- nuevo ocupante.

No se rerollea el interior completo sin resolver lo anterior.

---

# 8. Nuevo ocupante

Puede:

- conservar muebles existentes;
- retirar algunos;
- traer otros;
- cambiar distribución.

El building_id y su historia persisten.

---

## Regla final

**La generación crea una casa plausible una vez; el World State convierte esa casa en una historia concreta.**

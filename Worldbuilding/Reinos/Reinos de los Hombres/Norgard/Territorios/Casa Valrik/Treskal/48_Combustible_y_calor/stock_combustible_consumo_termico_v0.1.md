# Treskal — stock de combustible y consumo térmico v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO**

## Objetivo

Integrar combustible con:

- hogares;
- negocios;
- clima;
- incendios;
- economía.

---

# 1. Variables mínimas

Un consumidor relevante puede mantener:

- fuel_stock;
- fuel_quality_or_condition;
- expected_use;
- storage_capacity;
- supplier_ref si existe.

---

# 2. Consumo agregado

Puede resolverse por franja o periodo según:

- actividad;
- clima;
- ocupación;
- instalación.

No se quema una unidad por segundo.

---

# 3. Prioridad doméstica

Un hogar con poco combustible puede priorizar:

- cocinar;
- necesidades esenciales;
- calor cuando haga falta.

No se fija una IA doméstica numérica todavía.

---

# 4. Negocio

Una panadería o posada puede reducir servicio si:

- combustible insuficiente;
- horno dañado;
- entrega retrasada.

No produce a capacidad normal ignorando el estado físico.

---

# 5. Reposición

Solo mediante:

- entrega;
- compra;
- transferencia;
- producción/aprovechamiento real.

No existe respawn periódico invisible.

---

# 6. Incendio

El fuel_stock puede actuar como:

- recurso;
- riesgo.

La misma pila que permite cocinar puede agravar incendio si está mal situada.

---

# 7. Visualización

No es necesario mostrar cifra exacta al jugador.

Puede percibir:

- pila llena;
- reserva baja;
- madera húmeda;
- ausencia.

---

## Regla final

**El combustible conecta economía, clima, hogar y fuego; no es un contador aislado.**

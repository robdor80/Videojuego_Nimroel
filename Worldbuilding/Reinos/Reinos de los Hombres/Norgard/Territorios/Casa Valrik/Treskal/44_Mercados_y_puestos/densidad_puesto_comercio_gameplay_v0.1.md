# Treskal — densidad, puesto y comercio de mercado v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO**

## Objetivo

Traducir el mercado a simulación sin materializar siempre a todos los compradores y vendedores.

---

# 1. LOD de mercado

## Bajo

Mantiene:

- conteo de puestos;
- stock agregado;
- demanda;
- actividad;
- incidencias.

## Medio

Materializa:

- puestos relevantes;
- vendedores persistentes;
- flujos;
- entregas.

## Alto

Materializa:

- NPC;
- mercancía relevante;
- conversación;
- compra;
- percepción.

---

# 2. Puesto persistente

Un puesto con vendedor B/A puede mantener identidad entre jornadas.

No significa ocupar siempre exactamente el mismo espacio si el plano futuro no lo garantiza.

---

# 3. Población latente

Compradores ordinarios pueden resolverse como Nivel C.

Si el jugador interactúa con uno:

- promociona;
- recibe identidad;
- conserva relación con mercado.

---

# 4. Compra

Secuencia:

1. seleccionar vendedor;
2. comprobar stock;
3. acordar transacción;
4. validar pago;
5. transferir propiedad/posesión;
6. reducir stock.

---

# 5. Reposición durante jornada

Solo si existe:

- almacén cercano;
- segunda entrega;
- carro;
- productor.

No hay restock automático por tiempo.

---

# 6. Precio

El puesto usa presión de mercado y contexto.

No aplica precio distinto porque el jugador tenga mayor nivel.

---

# 7. Cierre

Cerrar puesto no borra negocio ni vendedor.

Puede cambiar:

- location;
- activity;
- stock location.

---

# 8. Evento

D05/D06/D07 u otro EVT pueden alterar:

- afluencia;
- disponibilidad;
- tráfico;
- demanda.

---

## Regla final

**El mercado puede simplificarse para rendimiento, pero cada compra importante debe seguir teniendo vendedor, stock y transferencia reales.**

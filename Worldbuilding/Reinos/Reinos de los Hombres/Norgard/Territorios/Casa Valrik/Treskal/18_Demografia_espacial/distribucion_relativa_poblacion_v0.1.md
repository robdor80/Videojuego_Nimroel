# Treskal — distribución relativa de población y actividad v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO — SIN PORCENTAJES DEMOGRÁFICOS RÍGIDOS**

## Objetivo

Definir dónde tienden a concentrarse residentes, trabajadores y visitantes sin fijar porcentajes de clase social ni repartir artificialmente los 12.000–18.000 habitantes.

---

# 1. Escala relativa

Se utiliza una escala técnica **0–5**:

- 0 — prácticamente ausente;
- 1 — muy baja;
- 2 — baja;
- 3 — media;
- 4 — alta;
- 5 — muy alta.

No representa porcentajes de población.

---

# 2. Variables

## R — residencia

Cantidad relativa de personas que **viven** en la subzona.

## D — actividad diurna visible

Densidad total esperable durante horas activas.

## W — intensidad laboral

Peso de trabajadores y actividad profesional.

## T — población transitoria

Visitantes, clientes, viajeros o personas que no residen allí.

## N — actividad nocturna

Actividad relativa después del cierre de la mayoría de talleres y mercados.

---

# 3. Matriz Z01–Z14

| Zona | R | D | W | T | N |
|---|---:|---:|---:|---:|---:|
| Z01 — El Puente | 1 | 4 | 2 | 5 | 1 |
| Z02 — Ribera / muelles fluviales | 1 | 4 | 4 | 3 | 1 |
| Z03 — Transferencia y almacenes | 1 | 4 | 5 | 2 | 1 |
| Z04 — Abasto y comercio | 3 | 5 | 4 | 5 | 3 |
| Z05 — Los Talleres | 4 | 5 | 5 | 3 | 3 |
| Z06 — Los Patios | 1 | 4 | 5 | 2 | 1 |
| Z07 — La Casa | 2 | 3 | 4 | 3 | 1 |
| Z08 — La Justicia | 1 | 4 | 4 | 3 | 2 |
| Z09 — Lonja / frente pesquero | 1 | 5 | 5 | 4 | 1 |
| Z10 — Los Muelles / puerto | 2 | 5 | 5 | 5 | 3 |
| Z11 — transición al recinto real | 0 | 3 | 4 | 2 | 1 |
| Z12 — Astilleros Reales | 0 | 5 | 5 | 1 | 1 |
| Z13 — tejido residencial | 5 | 3 | 2 | 1 | 5 |
| Z14 — Los Corrales / periferia | 2 | 4 | 4 | 4 | 2 |

---

# 4. Interpretación

## Z13

Es la mayor reserva residencial.

No significa que toda la población viva en una única zona: vivienda aparece también en Z04, Z05, Z10 y otras áreas mixtas.

## Z12

Tiene actividad laboral muy alta y residencia ordinaria prácticamente nula.

Los trabajadores llegan desde otras partes de la ciudad o periferia.

## Z04/Z10

Presentan mucha población transitoria por:

- mercado;
- puerto;
- posadas;
- comercio.

La densidad visible puede superar claramente a la residencial.

---

# 5. Día y noche

La ciudad cambia de centro de gravedad.

## Día

Picos:

- Z04;
- Z05;
- Z09;
- Z10;
- Z12.

## Noche

La población visible se desplaza hacia:

- Z13;
- viviendas de Z04/Z05;
- posadas y tabernas de Z10;
- puestos de guardia;
- actividad esencial.

No existe cierre total ni actividad nocturna moderna.

---

# 6. Clima

## Lluvia fuerte

Reduce:

- actividad exterior;
- mercado abierto;
- peatones.

Desplaza parte de la actividad hacia:

- talleres;
- tabernas;
- interiores;
- almacenes.

## Temporal

Reduce especialmente:

- Z09;
- Z10;
- actividad marítima.

## Día seco favorable

Aumenta:

- mercado;
- patios;
- muelles;
- trabajos exteriores.

---

# 7. Eventos

Los estados D01–D12 modifican esta matriz.

Ejemplos:

- D05 gran convoy de madera aumenta Z01/Z03/Z06;
- D06 gran día de ganado aumenta Z14;
- D07 gran mercante aumenta Z10/Z04;
- D11 alta actividad judicial aumenta Z07/Z08.

La matriz es **baseline**, no destino fijo.

---

# 8. Residentes reales

El censo no se calcula multiplicando estos valores.

La residencia real se deriva de:

- hogares;
- unidades residenciales;
- edificios;
- World State.

La matriz sirve para:

- spawn visual;
- LOD;
- tráfico;
- audio;
- densidad;
- simulación agregada.

---

# 9. Población latente

El Nivel C puede cubrir parte de D/W/T sin materializar miles de individuos.

Cuando el jugador interactúa con una persona concreta:

- se promociona a Nivel B;
- recibe identidad persistente;
- se descuenta de la población latente correspondiente.

---

# 10. Evitar clonación visual

Aumentar densidad no significa repetir NPC equivalentes.

La población visible debe variar por:

- edad;
- sexo;
- profesión;
- vestimenta;
- carga;
- destino;
- relación con zona.

Siempre dentro del canon visual de Norgard y Treskal.

---

## Regla final

**La ciudad tiene 12.000–18.000 residentes, pero lo que el jugador ve depende de dónde está, a qué hora llega y qué está ocurriendo.**

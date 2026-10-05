# Treskal — inventarios, contenedores y abstracción de objetos v0.1

> **MIGRADO A NIMROEL CORE — documentación derivada.** La autoridad normativa de OWN reside en `Worldbuilding/Sistemas/Nimroel Core/04_Material_y_riesgo/propiedad_posesion_objetos_v0.1.md`. Este archivo conserva explicación y ejemplos de Treskal; ante conflicto prevalece el Core.

## Estado

**DISEÑO TÉCNICO-CONCEPTUAL APROBADO**

## Objetivo

Evitar tanto:

- simular cada cucharilla de 15.000 habitantes;
- como reducir todo a inventarios abstractos sin relación con el mundo físico.

---

# 1. Tres niveles de objeto

## OBJ-A — persistente individual

Para:

- objeto único;
- arma/herramienta relevante;
- llave;
- carta;
- evidencia;
- regalo;
- encargo;
- objeto con historia.

## OBJ-B — lote persistente

Para:

- mercancía;
- madera;
- cereal;
- pescado;
- materiales.

## OBJ-C — utilería contextual

Objetos ordinarios no relevantes individualmente.

Pueden materializarse visualmente desde estado agregado.

---

# 2. Promoción

Un OBJ-C puede promocionarse a OBJ-A si el jugador:

- lo toma;
- lo usa;
- lo marca;
- lo convierte en evidencia;
- establece relación narrativa.

Una vez promovido, recibe ID persistente.

---

# 3. No reroll

Un objeto promovido no cambia:

- aspecto relevante;
- propiedad;
- ubicación histórica

por salir y volver a la zona.

---

# 4. Contenedores persistentes

Un contenedor relevante debe conservar:

- container_id;
- owner_ref;
- location_ref;
- access_state;
- contents_or_aggregate_stock.

---

# 5. Abstracción doméstica

No es necesario listar todos los:

- platos;
- cucharas;
- prendas;
- utensilios

de cada hogar mientras no tengan relevancia.

El interior debe seguir pareciendo plausible.

---

# 6. Inventario NPC

Un NPC no necesita cargar físicamente todo lo que posee.

Debe distinguirse:

- carried;
- stored_at_home;
- stored_at_work;
- entrusted_elsewhere.

---

# 7. Capacidad

La capacidad física importa para objetos voluminosos.

No se fija aquí un sistema exacto de peso/slots.

Pero:

- tronco;
- mueble;
- saco;
- barril

no deben caber en un bolsillo abstracto.

---

# 8. Transferencia

Toda transferencia relevante debe producir un delta de estado.

Esto permite:

- guardado;
- investigación;
- devolución;
- rastreo.

---

## Regla final

**Nimroel debe simular en detalle las cosas que importan y mantener plausibles, pero agregadas, las que todavía no importan.**

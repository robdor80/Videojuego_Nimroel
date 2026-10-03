# Treskal — grafo urbano de navegación v0.1

## Estado

**DISEÑO DE GAMEPLAY APROBADO — CONECTIVIDAD FUNCIONAL**

## Objetivo

Traducir la estructura urbana de Treskal a una red navegable estable para:

- pathfinding;
- viajes de NPC;
- cálculo de rutas;
- tráfico;
- misiones;
- diálogo direccional;
- simulación de bloqueos.

No representa todavía calles exactas.

---

# 1. Principio

Los sectores y subzonas forman un grafo.

Cada conexión debe justificar:

- qué une;
- quién la utiliza;
- qué tráfico soporta;
- qué puede bloquearla o degradarla.

No se añaden conexiones solo para que el mapa sea cómodo.

---

# 2. Tipos de conexión

## Principal terrestre

Apta para:

- peatones;
- caballos;
- carros;
- mercancías.

Prioritaria para tráfico pesado.

## Secundaria urbana

Apta para:

- peatones;
- carga ligera;
- carros de forma limitada según anchura.

## Peatonal/local

Apta principalmente para:

- residentes;
- clientes;
- recorridos de barrio.

## Fluvial

Apta para:

- pequeñas embarcaciones;
- mercancía compatible;
- pesca;
- transporte local.

## Portuaria

Apta para:

- carga marítima;
- embarcaciones;
- servicios de puerto.

## Restringida

Apta solo para:

- personal autorizado;
- trabajadores;
- guardia;
- proveedores institucionales.

---

# 3. Conexiones estructurales T

## T11 ↔ T10

Tipo: principal terrestre.

Uso:

- alimentos;
- ganado;
- viajeros;
- productos rurales.

## T11 ↔ T02

Tipo: principal terrestre.

Uso:

- madera;
- mercancías;
- carros pesados.

## T11 ↔ T05/T06

Tipo: principal / institucional.

Uso:

- mensajeros;
- vasallos;
- administración;
- justicia.

## T11 ↔ T08

Tipo: corredor logístico especializado.

Uso:

- suministros de Astilleros Reales;
- trabajadores;
- materiales.

No debe atravesar T03 innecesariamente.

---

# 4. Puente principal

Conecta la red del interior con la masa urbana principal.

Debe alimentar:

- T02;
- T03;
- accesos hacia T05/T06.

Es un nodo de gran importancia.

Su pérdida temporal por daño o crecida debe afectar rutas y economía.

---

# 5. T01 ↔ T02

Tipo:

- terrestre de carga;
- conexión directa río-almacén.

Uso:

- mercancías fluviales;
- pescado;
- materiales.

---

# 6. T01 ↔ T03

Tipo:

- urbana/comercial.

Uso:

- pasajeros;
- mercancía ligera;
- productos de mercado.

---

# 7. T01 ↔ T04

Tipo:

- productiva.

Uso:

- madera y materiales compatibles;
- artesanos;
- encargos.

---

# 8. T01 ↔ T07

Tipo:

- interfaz río-mar.

Uso:

- circulación portuaria;
- transferencia de determinadas mercancías;
- peatones y trabajadores.

No significa que cualquier embarcación fluvial pueda operar como buque marítimo.

---

# 9. T02 ↔ T03

Tipo: principal urbana/logística.

Debe permitir entregar mercancía al mercado sin convertir el mercado en corredor de paso pesado.

---

# 10. T02 ↔ T04

Tipo: principal productiva.

Uno de los ejes clave de la economía maderera.

---

# 11. T02 ↔ T08

Tipo: corredor logístico de alta capacidad.

Debe permitir mover:

- madera;
- metal;
- suministros.

---

# 12. T03 ↔ T04

Tipo: urbana/comercial.

Conecta clientes, encargos, venta y talleres.

---

# 13. T03 ↔ T05/T06

Tipo: urbana institucional.

Gran flujo peatonal y administrativo.

---

# 14. T03 ↔ T07

Tipo: urbana/portuaria.

Conecta puerto con mercado, posadas y comercio.

---

# 15. T03 ↔ T09

Tipo: urbana local.

Conecta vida residencial con servicios y mercado.

---

# 16. T04 ↔ T09

Tipo: urbana mixta.

Refleja casas-taller y trabajadores residentes.

---

# 17. T04 ↔ T08

Tipo: productiva especializada.

Puede transportar:

- componentes;
- madera preparada;
- herramientas;
- trabajadores especializados.

---

# 18. T05 ↔ T06

Tipo: institucional.

Debe ser corta y fiable.

---

# 19. T07 ↔ T08

Tipo: **separada y controlada**.

Existe continuidad litoral, pero no libre circulación interna.

La conexión pública debe terminar antes del recinto real.

Los proveedores autorizados usan accesos específicos.

---

# 20. T09 ↔ T10

Tipo: transición urbana-rural.

Conecta viviendas con:

- huertas;
- establos;
- periferia;
- caminos secundarios.

---

# 21. Rutas alternativas

La ciudad no debe depender de una sola calle para cada sector.

La cartografía detallada debe crear:

- rutas secundarias;
- desvíos;
- conexiones peatonales.

Pero los grandes flujos deben seguir los corredores funcionales fijados.

---

# 22. Costes de navegación

El coste de una ruta puede variar por:

- distancia;
- anchura;
- pendiente;
- barro;
- tráfico;
- mercado;
- ganado;
- obras;
- crecida;
- evento.

El pathfinding de NPC no debe elegir siempre la distancia geométrica más corta.

---

# 23. Restricciones por actor

Ejemplos:

- peatón puede usar calles estrechas;
- carro pesado evita callejones;
- ganado evita T03 cuando existe ruta periférica;
- civil no atraviesa T08;
- guardia urbana puede usar dependencias propias;
- proveedor autorizado puede acceder a T08 por corredor logístico.

---

## Regla final

**Moverse por Treskal debe responder a la misma lógica que hizo crecer la ciudad: el camino más útil depende de quién eres, qué transportas y qué está ocurriendo.**

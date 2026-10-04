# Treskal — demanda laboral, oficios y generación de hogares v0.1

## Estado

**DISEÑO DE SIMULACIÓN APROBADO — SIN PORCENTAJES LABORALES RÍGIDOS**

## Objetivo

Generar población urbana a partir de las necesidades reales de Treskal.

La ciudad no reparte profesiones mediante porcentajes universales.

El orden correcto es:

**función urbana → capacidad necesaria → puestos/roles → hogares → personas**

---

# 1. Principio

Una profesión aparece porque existe una actividad que la necesita.

Ejemplos:

- talleres de madera → carpinteros, ebanistas, tallistas, aprendices;
- puerto → pescadores, marineros, cargadores, reparadores, comerciantes;
- mercados → vendedores, transportistas, abastecedores;
- La Casa → escribanos, servicio, administración;
- Astilleros Reales → trabajadores navales y proveedores autorizados.

No se generan cien profesiones distintas solo para “dar variedad”.

---

# 2. Familias de ocupación

Los IDs O01–O14 son técnicos.

## O01 — Madera y mobiliario

Incluye:

- carpintería;
- ebanistería;
- talla;
- mobiliario;
- preparación de madera;
- aprendizaje.

Sectores prioritarios:

- T04;
- T02;
- relación con T08.

## O02 — Pesca y actividad marítima civil

Incluye:

- pescadores;
- marineros civiles;
- trabajo de muelle;
- redes;
- pequeñas reparaciones;
- apoyo a embarcaciones.

Sectores:

- T07;
- T01;
- Z09/Z10.

## O03 — Transporte y logística

Incluye:

- carreteros;
- cargadores;
- mozos;
- animales de tiro;
- almacenes;
- clasificación;
- expedición.

Sectores:

- T02;
- T10;
- T11;
- T01;
- T07.

## O04 — Alimentación y mercado

Incluye:

- panificación;
- carnicería;
- venta de alimentos;
- conservación;
- cocina;
- distribución.

Sectores:

- T03;
- T09;
- T10;
- entorno de S07.

## O05 — Posadas, tabernas y servicio al viajero

Incluye:

- posaderos;
- taberneros;
- cocina;
- servicio;
- establos vinculados;
- mantenimiento.

Sectores:

- T03;
- T07;
- accesos T11.

## O06 — Comercio y mediación mercantil

Incluye:

- comerciantes;
- intermediarios;
- compradores;
- vendedores especializados;
- gestión de encargos.

Sectores:

- T03;
- T07;
- T04;
- T02.

## O07 — Administración, escritura y cuentas

Incluye:

- escribanos;
- registro;
- archivo;
- recaudación;
- contabilidad;
- mensajería administrativa.

Sectores:

- T05;
- T06;
- comercio de mayor escala.

## O08 — Justicia y guardia urbana

Incluye funciones de:

- vigilancia;
- custodia;
- apoyo judicial;
- patrulla;
- recepción de denuncias.

No fija:

- rangos;
- tamaño del cuerpo;
- equivalencia militar.

Depende de la futura revisión institucional de Norgard.

## O09 — Trabajo naval de la Corona

Incluye la mano de obra y oficios necesarios en T08.

Puede solaparse profesionalmente con:

- O01;
- herrería;
- transporte;
- cabullería;
- administración.

La adscripción a T08 implica relación institucional con la Corona, no una profesión completamente distinta.

## O10 — Textil, vestido, cuero y calzado

Incluye:

- confección;
- reparación;
- calzado;
- curtido donde sea apropiado;
- venta de tejidos.

Debe respetar separación de actividades contaminantes.

## O11 — Metal, herramientas y reparación

Incluye:

- herrería;
- herrajes;
- reparación;
- herramientas;
- piezas para carros;
- necesidades navales cuando proceda.

## O12 — Salud y cuidados

Incluye:

- curanderas formadas;
- ayudantes cuando existan;
- cuidados domésticos no profesionales.

No crea hospital ni colegio médico.

## O13 — Construcción y mantenimiento urbano

Incluye:

- albañilería;
- cubiertas;
- mantenimiento;
- reparación de caminos;
- drenaje;
- carpintería de construcción.

La demanda puede aumentar tras:

- temporal;
- incendio;
- crecida.

## O14 — Actividad rural de borde

Incluye:

- huertas;
- ganado;
- establos;
- recepción de productos rurales;
- trabajo asociado a T10.

---

# 3. Profesión individual

La familia O no sustituye al oficio concreto.

Un NPC persistente debe recibir una ocupación específica cuando sea necesario.

Ejemplo:

`O01 → ebanista`

no simplemente:

`O01 → trabajador de madera`.

---

# 4. Capacidad antes que plantilla

El sistema debe resolver primero:

- cuánta panificación necesita la ciudad;
- cuántos talleres existen;
- qué volumen mueve el puerto;
- cuántos almacenes funcionan;
- qué actividad tiene T08.

Después determina cuántos roles necesita.

No se parte de:

“15 % de la población son artesanos”.

---

# 5. Trabajo familiar

Un negocio puede incluir:

- propietario;
- pareja;
- hijos en tareas compatibles;
- aprendices;
- trabajadores externos;
- familiares.

No todo trabajo utiliza relación salarial moderna.

---

# 6. Aprendices

Un aprendiz está vinculado a:

- maestro;
- oficio;
- taller;
- hogar propio o del maestro según caso.

No se genera como trabajador autónomo.

Puede progresar mediante World State.

---

# 7. Hogar y empleo

No se obliga a que todos los miembros de un hogar trabajen en el mismo lugar.

Pero son comunes:

- hogar-taller;
- familia de comerciantes;
- familia portuaria;
- continuidad de oficio.

---

# 8. Hogares urbanos técnicos

Los IDs H01–H09 son plantillas sociales, no clases legales.

## H01 — Pareja con descendencia

## H02 — Hogar multigeneracional

## H03 — Persona sola

## H04 — Viudo/a con o sin descendencia

## H05 — Hermanos u otros familiares adultos compartiendo hogar

## H06 — Hogar artesanal con aprendiz residente

## H07 — Hogar con trabajador o servicio residente

Solo cuando la situación económica y social lo justifique.

## H08 — Hogar compartido no familiar

Posible por:

- trabajadores;
- marineros;
- aprendices;
- circunstancias urbanas.

No debe convertirse en piso compartido moderno por defecto.

## H09 — Vivienda asociada a negocio o institución

Ejemplos:

- posada;
- taller;
- dependencias de servicio;
- instalación concreta.

---

# 9. Personas sin ocupación profesional

La población incluye personas que no necesitan profesión:

- niños;
- personas dedicadas principalmente al hogar;
- enfermos;
- ancianos con actividad reducida;
- personas entre trabajos;
- dependientes.

No se fuerza un oficio a cada NPC.

---

# 10. Demanda dinámica

La necesidad laboral puede variar.

Ejemplos:

- gran mercante → más carga y descarga temporal;
- temporal → menos pesca;
- incendio → más reparación;
- gran contrato naval → más presión de materiales y trabajo;
- cosecha → más tránsito rural.

La variación temporal no cambia automáticamente la estructura demográfica permanente.

---

# 11. Mano de obra temporal

Puede proceder de:

- territorio Valrik;
- Villas;
- Pueblos;
- otros lugares.

Se trata como población temporal hasta que exista establecimiento real.

---

# 12. Vacantes

Si un NPC:

- muere;
- emigra;
- enferma;
- abandona oficio,

puede aparecer una vacante real.

La actividad puede:

- reducirse;
- ser cubierta por familiar;
- pasar a aprendiz;
- contratar a otra persona;
- cerrar.

El sistema no genera inmediatamente un reemplazo idéntico fuera de escena.

---

## Regla final

**Treskal genera personas para sostener funciones y hogares; no genera estadísticas y luego intenta justificar por qué existen.**

# Treskal — marco de toponimia urbana v0.1

## Estado

**MARCO PREPARATORIO — DECISIÓN AUTORAL PENDIENTE**

## Situación

El repositorio no contiene todavía una convención general de toponimia de Norgard suficientemente definida como para bautizar barrios, calles o edificios de Treskal sin inventar una regla cultural nueva.

Por tanto, la estructura urbana mantiene IDs técnicos estables y separa:

**identidad técnica → nombre visible futuro**

---

# 1. Regla principal

Los nombres definitivos deben surgir de una convención cultural aprobada.

Hasta entonces:

- T01–T11 permanecen sectores funcionales;
- Z01–Z14 permanecen subzonas técnicas;
- L01–L12 permanecen landmarks técnicos;
- S01–S10 permanecen instalaciones técnicas.

Cambiar un nombre visible futuro no debe cambiar estos IDs.

---

# 2. Fuentes plausibles de toponimia

Una futura convención de Norgard puede permitir nombres derivados de:

## Geografía

- río;
- mar;
- puente;
- desembocadura;
- orientación;
- rasgos locales.

## Oficio y actividad

- madera;
- carpinteros;
- mercado;
- pescado;
- puerto;
- astilleros.

## Historia

- antiguo fundador;
- incendio;
- batalla;
- reconstrucción;
- acontecimiento local.

Solo si esos hechos existen realmente en canon.

## Casas e instituciones

- Casa Valrik;
- Corona;
- cargos;
- instituciones.

Debe evitarse convertir cada lugar en homenaje nobiliario.

## Uso popular

Un nombre oficial y un nombre coloquial pueden coexistir cuando resulte natural.

---

# 3. Nombres que requerirán decisión

Como mínimo habrá que resolver:

- nombre del puente principal;
- nombre o designación del mercado principal;
- nombre del mercado/frente de pescado si lo tiene;
- nombre de la sede Valrik;
- posible nombre del complejo judicial;
- designación popular del acceso a Astilleros Reales;
- nombres de los principales corredores o calles;
- nombres de barrios o áreas urbanas si la cultura los utiliza formalmente.

---

# 4. Barrios oficiales

No se debe asumir que las 14 subzonas técnicas equivalen a 14 barrios con nombre.

La toponimia final puede:

- agrupar varias subzonas;
- dividir una zona extensa;
- mantener áreas conocidas solo por una calle, mercado o actividad.

La forma social de nombrar la ciudad debe preceder al número de barrios.

---

# 5. Evitar nombres fantasy genéricos

No utilizar por defecto construcciones del tipo:

- “Barrio del Cuervo”;
- “Calle de la Espada”;
- “Puerto de la Luna”;
- nombres pseudo-nórdicos sin regla lingüística;
- apóstrofos o grafías exóticas solo para sonar fantásticas.

Un nombre debe poder explicarse dentro de Norgard.

---

# 6. Nombres funcionales provisionales

En documentación de desarrollo se permiten expresiones descriptivas:

- puente principal;
- mercado principal;
- muelles fluviales;
- puerto civil;
- sede Valrik;
- Astilleros Reales;
- patios de madera.

Estas expresiones no bloquean el nombre canónico futuro.

---

# 7. Cartografía y guardados

El motor debe guardar referencias por ID técnico.

Ejemplo:

`landmark_id = L03`

y no depender de:

`landmark_name = "Nombre visible futuro"`

Así la toponimia puede ajustarse durante desarrollo sin romper:

- misiones;
- NPC;
- rutas;
- World State;
- traducciones.

---

# 8. Localización lingüística

Cuando exista un nombre canónico, deberá definirse si:

- se conserva igual en todos los idiomas;
- se traduce por significado;
- posee forma localizada.

Esta decisión pertenece a la futura guía lingüística/toponímica del proyecto.

---

## Decisión autoral necesaria

Antes de bautizar Treskal de forma sistemática necesitamos una **convención de nombres de Norgard**.

No es necesario resolverla para seguir diseñando geometría, NPC o gameplay.

---

## Regla final

**Primero la ciudad adquiere lugares; después la cultura les da nombre.**

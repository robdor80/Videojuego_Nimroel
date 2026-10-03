# Pueblos de Treskal — población, hogares y derivación de edificios

## Estado

**CANON DE GENERACIÓN DEMOGRÁFICA FUNCIONAL APROBADO — v0.1**

## Objetivo

Definir cómo transformar la población total de un Pueblo en hogares, viviendas y edificios funcionales sin fijar familias concretas en el canon.

La instancia concreta pertenece al estado persistente de la partida.

---

# 1. Regla principal

La población se genera primero dentro del rango canónico de **350–900 habitantes**.

Después se divide en **unidades domésticas**.

El número de viviendas no se decide directamente: se deriva de la composición de esas unidades domésticas.

---

# 2. Unidad doméstica

Una unidad doméstica representa a las personas que comparten de forma habitual vivienda, recursos y vida cotidiana.

Puede incluir:

- pareja con hijos;
- pareja sin hijos;
- familia extensa;
- progenitor viudo con hijos;
- persona anciana viviendo con descendientes;
- hermanos u otros familiares adultos;
- adulto solo;
- artesano con aprendiz integrado en el hogar;
- trabajador o ayudante residente cuando la profesión lo justifique.

No existe una única estructura familiar obligatoria.

---

# 3. Ocupación residencial

Como referencia de generación:

- **2–8 residentes** por vivienda es un intervalo común;
- **4–6 residentes** constituye la franja central más frecuente;
- hogares de una sola persona son posibles pero minoritarios;
- casos de más de ocho residentes pueden existir cuando haya familia extensa, aprendices, trabajadores o una razón concreta.

La media final de una instancia ordinaria debería tender aproximadamente a **4,3–5,2 residentes por vivienda ocupada**.

Esta cifra es una herramienta procedural, no una norma social consciente dentro del mundo.

---

# 4. Derivación de viviendas

El generador debe:

1. fijar población total;
2. crear unidades domésticas;
3. asignar residentes;
4. calcular viviendas necesarias;
5. integrar después talleres, comercios y anexos.

No se redondea la población para que encaje en un número predeterminado de casas.

Una vivienda puede alojar:

- una unidad doméstica;
- excepcionalmente dos unidades relacionadas cuando la arquitectura y el parentesco lo justifiquen.

No se generan bloques de apartamentos como solución normal de Pueblo.

---

# 5. Diversidad de hogares

La generación debe evitar una población compuesta únicamente por parejas jóvenes con hijos.

Debe existir una mezcla plausible de:

- infancia;
- jóvenes;
- adultos;
- mayores;
- viudedad;
- hogares sin hijos;
- hogares extensos;
- personas solas;
- aprendices y trabajadores asociados a determinados oficios.

No se fijan todavía porcentajes demográficos universales para todo Valrik.

La composición concreta puede variar entre Pueblos.

---

# 6. Hogar y profesión

Muchos oficios pueden estar físicamente vinculados a la vivienda.

Ejemplos:

- casa-taller de carpintero;
- vivienda con panadería;
- pequeño comercio en la planta o estancia frontal;
- curandera con espacio de trabajo doméstico;
- taberna integrada en vivienda;
- taller con patio posterior.

Por tanto:

**número de servicios != número de edificios adicionales**

El generador debe decidir si cada servicio:

- comparte edificio con vivienda;
- ocupa anexo;
- utiliza edificio independiente.

---

# 7. Edificios no residenciales

Se generan solo cuando la función lo requiere.

Pueden incluir:

- herrería independiente;
- taberna o posada;
- molino;
- almacenes;
- graneros comerciales;
- carnicería;
- talleres;
- edificios vinculados al mercado;
- cobertizos;
- establos;
- otras instalaciones aprobadas.

Los puestos temporales del mercado no cuentan como edificios permanentes.

---

# 8. Anexos

Una vivienda o taller puede generar anexos según actividad:

- cobertizo;
- leñera;
- establo;
- corral;
- pajar;
- almacén pequeño;
- patio de trabajo;
- horno;
- otros elementos funcionales.

Los anexos no deben contarse automáticamente como viviendas.

---

# 9. Diferencias por banda de Pueblo

## P1 — 350–499 habitantes

Tendencia:

- mayor proporción de casas familiares con espacio exterior;
- mezcla frecuente de vivienda y actividad económica;
- menor número de edificios exclusivamente comerciales.

## P2 — 500–699 habitantes

Tendencia:

- mayor densidad central;
- más talleres independientes;
- más edificios dedicados a servicio o almacenamiento;
- mayor separación entre vivienda y determinados oficios.

## P3 — 700–900 habitantes

Tendencia:

- núcleo central más denso;
- mayor número de edificios exclusivamente comerciales o artesanales;
- más posibilidades de una segunda taberna, posada amplia y almacenes;
- periferia residencial y productiva más extensa.

Estas tendencias no convierten un P3 en Villa.

---

# 10. Edificios vacíos y abandono

El generador ordinario no debe crear un número significativo de edificios permanentemente vacíos solo para aumentar visualmente el tamaño del Pueblo.

Edificios abandonados, quemados, en ruinas o sin ocupación requieren:

- historia local;
- evento;
- crisis;
- misión;
- razón económica o narrativa.

---

# 11. Validación demográfica

Antes de persistir la instancia se comprueba:

- que todos los residentes pertenezcan a un hogar, institución o situación explicada;
- que las viviendas puedan alojar a sus residentes;
- que la cantidad de viviendas derive de la población;
- que los servicios tengan trabajadores;
- que los trabajadores residan de forma plausible;
- que no exista una población imposible de sostener con la estructura generada;
- que los edificios no aparezcan sin función.

---

# 12. Persistencia

Una vez generados:

- población;
- hogares;
- relaciones domésticas;
- viviendas;
- ocupaciones;
- edificios asociados

quedan persistidos en el World State.

El jugador debe encontrar a la misma comunidad al regresar, salvo cambios causados por acontecimientos del mundo.

---

## Principio final

**Primero se generan personas y hogares; después se generan las viviendas que necesitan; finalmente los servicios y actividades determinan qué edificios y anexos adicionales aparecen.**

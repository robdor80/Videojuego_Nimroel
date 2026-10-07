# Cierre Punto 10 — Gastronomía / alimentación de Norgard v0.1

## Estado

**PUNTO 10 CERRADO — GASTRONOMÍA / ALIMENTACIÓN**

Marcador:

`CUISINE_POINT_10_CLOSED_NORGARD_CUISINE`

## Cerrado en Nimroel Core

- estado FOOD de lotes alimentarios;
- preparación;
- cocción;
- combustible;
- utensilios;
- conservación;
- deterioro;
- seguridad alimentaria;
- recetas como contratos;
- sustitución;
- comidas agregadas/detalladas;
- integración con NEED;
- restos/WASTE;
- propiedad/transacción;
- estación/clima;
- viaje;
- raciones;
- LOD;
- autoridad de IA.

## Cerrado en Norgard

- base culinaria humana común;
- cereales;
- legumbres;
- huerta;
- fruta;
- productos animales;
- pescado;
- miel/sal/vinagre;
- bebidas;
- grasas;
- panificación;
- ollas/sopas/guisos;
- carne;
- pescado;
- lácteos;
- huevos;
- dulces;
- ritmos de comida no rígidos;
- comida de trabajo;
- posadas/tabernas;
- mercado;
- viaje;
- ejército;
- Armada;
- hospitalidad;
- banquetes;
- desigualdad;
- escasez;
- hambre;
- regionalización de las cinco Grandes Casas;
- Syvaris/Taramin sin flora inventada;
- catálogo de 40 preparaciones canónicas.

## Corpus de referencia

Se utilizó un informe de investigación aportado por el autor basado en:

- los cinco libros publicados de *Canción de Hielo y Fuego*;
- *El Caballero de los Siete Reinos*.

Se extrajeron únicamente patrones de:

- técnicas;
- conservación;
- logística;
- jerarquía social;
- comida de viaje/tropa;
- región;
- estacionalidad;
- uso narrativo.

No se importaron platos, nombres, rituales ni ingredientes fantásticos propios de esas obras.

## Ingredientes nuevos canonizados

- trigo;
- cebada;
- avena;
- centeno;
- guisantes;
- habas;
- lentejas;
- cebolla;
- puerro;
- col;
- nabo;
- zanahoria;
- remolacha;
- manzana;
- pera;
- ciruela;
- uva;
- frutos del bosque como categoría;
- aves domésticas de corral como categoría;
- huevos;
- leche;
- mantequilla;
- queso fresco;
- queso curado;
- miel;
- sal;
- vinagre;
- grasa animal fundida;
- hierbas culinarias locales como categoría.

Se mantienen vacíos deliberados para:

- especies concretas de pescado/marisco;
- flora silvestre detallada;
- especias exóticas;
- aceites vegetales concretos;
- productos propios de Syvaris/Taramin;
- ingredientes fantásticos.

## Regionalización

### Aethros / Hallheim
Cocina de confluencia y corte con productos llegados de todo el Reino.

### Darovan
Puertos, comercio, minería, alimentos transportables y acceso privilegiado a importados cuando existen.

### Edranor
Vino, uva, vinagre y cocina con vino.

### Galdren
Granero, ganadería, pan, gachas, potajes, lácteos y carne.

### Valrik
Pescado, conservas de pescado, guisos/pasteles de pescado y cerveza.

## Economía

Se conservan las anclas del Punto 5:

- pan sencillo: 1 Clavo;
- bebida ordinaria pequeña: 1 Clavo;
- comida sencilla: 2 Clavos;
- comida abundante de taberna: 4 Clavos;
- alimentación básica diaria: 5 Clavos.

Las recetas no fijan precios.

## Validación

- regresión E14 de 100 invariantes;
- pack estático de 60 casos;
- catálogo operativo de 40 preparaciones;
- contrato Core FOOD.

## Pendencias que NO reabren Punto 10

- nombres folclóricos de platos;
- especies concretas de flora/fauna no definidas;
- especias importadas concretas;
- festividades y menús ceremoniales ligados al futuro calendario;
- cultura material detallada de vajilla/utensilios del Punto 13.

## Regla final

**Punto 10 cierra qué puede comer Norgard, cómo lo prepara y cómo cambia según territorio, riqueza, viaje, guerra y estación; el World State decide si ese alimento existe hoy en esa mesa.**

`CUISINE_POINT_10_CLOSED_NORGARD_CUISINE`

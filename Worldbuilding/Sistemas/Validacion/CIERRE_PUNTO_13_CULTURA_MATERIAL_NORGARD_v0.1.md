# Cierre Punto 13 — Cultura material común de Norgard v0.1

## Estado

**PUNTO 13 CERRADO — CULTURA MATERIAL COMÚN**

Marcador:

`MATERIAL_CULTURE_POINT_13_CLOSED_NORGARD_SHARED_MATERIAL_CULTURE`

## Cerrado en Norgard

- nivel tecnológico preindustrial común;
- madera, piedra, pizarra, hierro, acero seleccionado, cerámica y vidrio limitado;
- lana, lino, cuero y fibras ordinarias;
- ropa funcional y calzado;
- mobiliario doméstico;
- almacenamiento;
- cocina y vajilla;
- agua, aseo y jabón simple;
- iluminación por vela/lámpara/antorcha/fuego;
- cerraduras, llaves y herrajes;
- escritura manual;
- papel y pergamino;
- archivos físicos;
- herramientas de carpintería, agricultura, herrería, textil y construcción;
- carros, carretas y transporte menor;
- material sanitario ordinario;
- diferencias por riqueza;
- diferencias regionales sin niveles tecnológicos distintos;
- catálogo operativo inicial de 110 objetos.

## Regla tecnológica crítica

**No existen relojes en Norgard.**

No existen:

- relojes mecánicos;
- relojes de torre;
- relojes de bolsillo;
- relojes de pulsera;
- relojes de agua como sistema civil;
- relojes de arena como sistema civil.

Las campanas:

- existen;
- sirven como señal;
- no funcionan automáticamente como reloj horario.

TIME mantiene precisión interna para el motor, no para los personajes.

## Relación con Punto 12

Punto 12 define cómo funciona el tiempo.

Punto 13 define con qué objetos vive la gente.

Por tanto:

- el motor puede saber `16:37`;
- un NPC puede no disponer de forma material de saber que son exactamente las 16:37.

Esto es intencional.

## Catálogo

`Worldbuilding/Sistemas/Norgard Defaults/Datos operativos/norgard_common_material_object_catalog_v0.1.json`

110 entradas autorizadas.

Una entrada del catálogo:

- permite que el objeto exista;
- no lo materializa;
- no le asigna propietario;
- no garantiza stock;
- no garantiza buen estado.

## Integración con Core

La cultura material usa sistemas existentes:

- OWN;
- COND;
- TOOL;
- WS;
- DOOR;
- BUILD;
- FOOD;
- WASTE;
- FIRE;
- TIME.

No se crea un inventario paralelo.

## Integración con Treskal

Treskal hereda la base tecnológica de Norgard.

Mantiene como sesgos locales:

- excelencia Valrik en madera;
- clima húmedo/marítimo;
- pesca/puerto;
- Astilleros Reales;
- mantenimiento por salitre/humedad;
- stock y economía local.

No necesita una cultura material independiente.

## Dependencias resueltas

Punto 13 cierra las dependencias antiguas de:

- fibras textiles;
- materiales de lavado;
- materiales comunes de herramientas;
- metalurgia cotidiana;
- mobiliario;
- vajilla;
- iluminación;
- escritura;
- cierres y herrajes;
- objetos de medición/señal temporal.

## No definido deliberadamente

Punto 13 no fija:

- estética exacta de cada Gran Casa;
- catálogo completo de objetos especializados navales/militares;
- botánica concreta de tintes;
- especies concretas de madera;
- manufacturas exóticas importadas no canonizadas;
- objetos de otros pueblos.

## Validación

- regresión E17 de 131 invariantes;
- pack estático de 85 casos;
- catálogo de 110 objetos;
- default operativo de Reino;
- regla NO CLOCKS validada.

## Estado de la gran auditoría de Norgard

Con Punto 13 quedan cerrados los grandes bloqueos generales detectados en la auditoría de Norgard.

`blockedPendingCanon` debe quedar vacío.

## Regla final

**Norgard ya posee una base material completa para vivir, trabajar, cocinar, escribir, iluminarse, guardar, transportar, construir y reparar sin introducir tecnología ajena a su época.**

`MATERIAL_CULTURE_POINT_13_CLOSED_NORGARD_SHARED_MATERIAL_CULTURE`

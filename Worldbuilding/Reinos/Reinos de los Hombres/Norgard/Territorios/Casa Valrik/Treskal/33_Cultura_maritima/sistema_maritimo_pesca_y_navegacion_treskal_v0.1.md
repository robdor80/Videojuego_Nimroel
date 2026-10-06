# Treskal — Sistema marítimo, navegación y pesca v0.1

## Estado

**FASE 2B LOCAL CERRADA**

Treskal materializa el sistema marítimo universal y los defaults de Norgard mediante dos ámbitos separados:

- **T07** — puerto civil y pesquero;
- **T08** — Complejo Naval Real de la Corona.

## Flotilla pesquera

La flotilla no posee catálogo de nombres ni clases propias.

Se genera a partir de trabajo pesquero, propietarios, demanda, capacidad portuaria, caladeros, estación, clima, mantenimiento y pérdidas.

La mezcla inicial favorece bajura y costa, con presencia menor fluvial/estuarina y de altura. Las proporciones son objetivos de generación, no cuotas inmutables.

Cada barco materializado pasa a ser una entidad VSL persistente.

## Caladeros

Se definen cuatro ámbitos funcionales sin inventar especies:

- estuario y tramo bajo;
- costa inmediata;
- costa accesible del Mar de Suthiros;
- aguas de altura del Mar de Suthiros.

Su presión de pesca y recuperación forman parte del World State.

## Ciclo económico

caladero → captura → carga del barco → regreso → S07 → venta/conservación/distribución.

Una mala campaña pesquera puede producir menos pescado en mercado. El mercado no genera capturas para rellenar stock.

## Navegación y accidentes

Clima, visibilidad, estado del agua, tripulación, carga y condición del barco modifican salidas y viajes.

Averías, naufragios, rescates, lesiones y pérdidas continúan existiendo fuera de cámara.

## Armada

T08 opera con el sistema E6/E7 de la Armada.

Los grandes navíos son persistentes. Un convoy puede salir, combatir, sufrir daños y regresar a T08 sin que el jugador lo haya presenciado, conservando las consecuencias.

## Frontera T07/T08

La actividad civil no entra ordinariamente en T08.

Una emergencia o autorización explícita puede crear una excepción contextual; nunca cambia la autoridad del recinto.

## Fiscalidad

El Punto 3 se conectará a la llegada, manifiesto, carga, control y salida ya existentes. No hace falta reabrir 2B para añadir impuestos o aduanas.

## Regla final

**La costa de Treskal funciona aunque el jugador no la mire: los barcos salen, pescan, comercian, esperan, se averían, regresan o se pierden dentro de un World State persistente.**

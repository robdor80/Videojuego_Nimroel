# Datos operativos — Villas del territorio de Treskal

Esta carpeta representa en datos estructurados el canon procedural de las tres Villas Valrik.

## Archivos

- `villa_generation_rules_v0.1.json` — reglas comunes, perfiles funcionales, probabilidades, administración, población y espacio.
- `villa_instance_contract_v0.1.json` — contrato de persistencia de una Villa materializada.
- `generation_invariants_v0.1.json` — pruebas de diseño que deberá superar la implementación.

## Particularidad

Las tres Villas no son perfiles intercambiables elegidos al azar.

El perfil funcional es canónico; la generación decide su materialización concreta.

Los nombres, Casas menores y localizaciones exactas podrán añadirse después mediante referencias estables sin obligar a regenerar la estructura de la Villa.

## Persistencia

La población residente, edificios, servicios y layout pertenecen al World State.

La población flotante se mantiene separada y solo modifica el censo residente si una persona se establece realmente.

Una partida existente no debe rerollear una Villa por cambios posteriores de nombre, lore superficial o versión de reglas sin una migración explícita.

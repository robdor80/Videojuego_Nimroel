# Datos operativos — Pueblos de Treskal

Esta carpeta traduce el canon humano de `Pueblos/` a estructuras legibles por herramientas y por el futuro RPG Core.

## Archivos

- `pueblo_generation_rules_v0.1.json` — reglas estáticas de generación: población, probabilidades, modificadores, cobertura, modelos, hogares, espacio y pipeline.
- `pueblo_instance_contract_v0.1.json` — contrato mínimo de persistencia para una instancia generada.

## Separación obligatoria

Los archivos de esta carpeta **no contienen Pueblos concretos**.

El canon define reglas; el generador produce la instancia; el World State conserva el resultado.

NPC individuales, inventarios dinámicos y estado de misiones no deben mezclarse con el contrato estático del asentamiento.

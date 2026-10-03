# Datos operativos — Pueblos de Treskal

Esta carpeta traduce el canon humano de `Pueblos/` a estructuras legibles por herramientas y por el futuro RPG Core.

## Archivos

- `pueblo_generation_rules_v0.1.json` — reglas estáticas de generación: población, probabilidades, modificadores, cobertura, modelos, hogares, espacio y pipeline.
- `pueblo_instance_contract_v0.1.json` — contrato mínimo de persistencia para una instancia generada.
- `regional_generation_rules_v0.1.json` — coordinación entre Pueblos, Aldeas y centros superiores mediante grafo de accesibilidad y aleatoriedad determinista.
- `generation_invariants_v0.1.json` — casos de prueba de diseño que deberá superar el futuro generador.

## Separación obligatoria

Los archivos de esta carpeta **no contienen Pueblos concretos**.

El canon define reglas; el generador produce la instancia; el World State conserva el resultado.

NPC individuales, inventarios dinámicos y estado de misiones no deben mezclarse con el contrato estático del asentamiento.

## Versionado

Una partida existente no debe regenerar silenciosamente un Pueblo cuando cambien las reglas.

Las instancias persistidas deben conservar, como mínimo, la identidad técnica estable, el World Seed y las versiones de reglas y generador necesarias para mantener reproducibilidad.

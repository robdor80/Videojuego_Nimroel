# Nimroel Core

## Estado

**EXTRACCIÓN EN CURSO DESDE EL PROTOTIPO COMPLETO DE TRESKAL**

## Objetivo

Centralizar reglas universales de simulación para que cualquier territorio de Nimroel pueda reutilizarlas sin copiar decenas de capas locales.

## Autoridad

Cuando un sistema figure como `active_core_contract`:

- sus stable IDs son globales;
- su semántica pertenece al Core;
- ciudades y culturas solo definen overrides o contenido propio;
- ante conflicto, el contrato Core prevalece salvo excepción explícita y autorizada.

## Migración

Treskal fue el laboratorio original.

Cada sistema se migra mediante:

1. extracción de reglas universales;
2. creación de contrato Core;
3. preservación de stable IDs;
4. conversión del contrato Treskal en referencia/override;
5. marcado de documentación local como derivada;
6. regresión de compatibilidad.

No se realiza copia activa permanente.

## Fase actual

Extracción ejecutada:

- lote A1: MEM, PERS, EMO / MOOD;
- lote A2: GOAL, DEC, TRUST, VIEW.
- lote A3: STAT, CRED, CONF, DIAL, ATTN, EXP.

Los siguientes sistemas se migrarán por lotes controlados.

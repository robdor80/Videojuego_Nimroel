# Nimroel Core

## Estado

**EXTRACCIÓN DE ALTA CONFIANZA COMPLETA Y VALIDADA ESTÁTICAMENTE**

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
- lote A4: STRS, VAL, SELF.
- lote B1: PREG, CHD, AGE, KIN.
- lote B2: DEP / CARE, CHORE / DOM, REST, NEED.
- lote C1: EMP, AGEN, WAIT.
- lote C2: RES / MOVE, APR, FAV, REQ.

**Fase C — actividad y tiempo: COMPLETA.**
- lote D1: OWN, COND, TOOL / WS.
- lote D2: BUILD, DOOR.
- lote D3: WASTE / WST.
- lote D4: HAZ / ACC, FIRE, ERSP.

**Fase D — material y riesgo: COMPLETA.**
- lote U1: FRI, AFF, RIFT, GIFT.
- lote U2: CONV / VOICE / HEAR, MSG, ED.
- lote U3: K, separado explícitamente de reputación.

**Extracción de namespaces Core de alta confianza: COMPLETA.**

No quedan lotes Core de alta confianza pendientes de esta refactorización. Las futuras ampliaciones dependerán de nuevo canon o de nuevas necesidades de simulación.


## Cierre de refactorización

La extracción desde Treskal queda cerrada mediante regresión estática de contratos.

Resultado:

**TRESKAL_REFACTOR_COMPLETE_AND_STATICALLY_VALIDATED**

Esto valida arquitectura, autoridad, namespaces, bridges, overrides y referencias documentales. Las pruebas runtime/gameplay se ejecutarán cuando estos contratos tengan implementación de motor; no constituyen deuda de la refactorización de worldbuilding.


## Ampliación posterior — geografía física

Tras cerrar la extracción desde Treskal, Nimroel Core puede seguir creciendo con sistemas universales nuevos.

Se ha añadido:

- `physicalGeographyDrainage` → reglas universales de microrelieve, drenaje, cuencas, manantiales e hidrografía menor.

Esto **no reabre la refactorización de Treskal**. Es una ampliación nueva del Core reutilizable por cualquier reino o territorio.

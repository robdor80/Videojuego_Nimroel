# D.P17 — Contrato transversal de integración futura y persistencia

**Estado:** contrato conceptual y escenarios TEST_ONLY; ninguna conexión real C++/GDExtension/Android/Godot ejecutada.

## Comparación con Valrik

La auditoría de Treskal cerró 99 capas locales y su mapa de extracción migró los dominios generales de cognición, relación, empleo, propiedad, sanidad, percepción, tareas y estado al **Nimroel Core / Norgard Defaults**. Aquí se reutilizan los **nombres de namespaces como puntos de consulta**, no se afirman implementaciones específicas del catálogo actual sin verificar en una fase de integración.

**Namespaces inventariados:** MEM, PERS, EMO, MOOD, GOAL, DEC, TRUST, VIEW, STAT, CRED, CONF, DIAL, ATTN, EXP, STRS, VAL, SELF, PREG, CHD, AGE, KIN, DEP, CARE, CHORE, DOM, REST, NEED, EMP, AGEN, WAIT, RES, MOVE, APR, FAV, REQ, OWN, COND, TOOL, WS, BUILD, DOOR, WASTE, WST, HAZ, ACC, FIRE, ERSP, FRI, AFF, RIFT, GIFT, CONV, VOICE, HEAR, MSG, ED, K.

## Pipeline de autoridad

```text
CANON + NORGARD DEFAULTS + OVERRIDE DAROVAN
  → identidad de localidad y contexto físico D.P14
  → derechos y parámetros D09
  → identidad de actor, conocimientos y percepción
  → proveedor real, ruta física y capacidad D.P15/D.P16
  → resolución y mutación exclusiva por CoreRPG
  → evento con ID y fuente, delta persistente
  → información filtrada a observador y narrador IA
```

No basta un JSON para afirmar que un servicio o accidente existe en la partida. La IA puede narrar un evento autorizado, pero no crear su causa, mutar la economía, revelar información no obtenida o cambiar la ruta física.

## Contrato de entrada y salida

**Entrada conceptual:** authoredPlaceId; provenance; verifiedCoordinatesOrUnknown; timeAndSeasonOrUnknown; actualWorldStateOrUnknown; actorKnowledgeAndPermissions; serviceProviderIdOrUnknown; resourceStockOrUnknown; routeGraphOrUnknown.

**Salida conceptual:** allowed_or_rejected; reason_codes; evidence_sources; legal_authority; unchanged_worldstate_when_rejected; proposed_mutations_for_engine_only.

Cuando falta un dato obligatorio se rechaza la acción, se limita a un relato hipotético o se devuelve motivo UNKNOWN según el contexto; no se rellena con una cifra «razonable» no aprobada.

## Escenarios adversariales de diseño

| ID | Escenario de laboratorio | Comportamiento obligatorio | Resultado que se rechaza |
|---|---|---|---|
| DP17-T01 | Veldora descarga e inspección exterior | `REQUIRE_EXISTS_STOCK_CUSTOMS_PERMISSION` | `NO_NEW_DOCK_OR_INTERNAL_CUSTOMS` |
| DP17-T02 | Veldora llega comercio terrestre de Treihord | `REQUIRE_ACCESS_AND_SUPPLY` | `NO_KM_TRAVEL_TIME_OR_STOCK_GUESS` |
| DP17-T03 | Taramin descarga pesquera conceptual | `REQUIRE_VERIFIED_DOCK_LOCATION` | `NO_THALEN_BRANCH_NAVIGABILITY_INFERRED` |
| DP17-T04 | Taramin evaluación de acceso de interfluvio | `REQUIRE_PHYSICAL_BRIDGE_IF_CROSSING` | `NO_NEW_BRIDGE_OR_FORD` |
| DP17-T05 | Syvaris abrigo en bahía | `REQUIRE_BAY_SITE_AND_WEATHER` | `NO_MARITIME_ROUTE_SCHEDULE` |
| DP17-T06 | Syvaris operación naval | `REQUIRE_ROYAL_AUTHORITY` | `NO_DAROVAN_PRIVATE_NAVY` |
| DP17-T07 | Treihord barguería industrial del Belara | `REQUIRE_SHALLOW_DRAFT_AND_ACTUAL_CARGO` | `NO_MERCHANT_OCEAN_PORT` |
| DP17-T08 | Treihord acceso a la Vena | `REQUIRE_RESTRICTED_ACCESS` | `NO_PUBLIC_TRANSIT` |
| DP17-T09 | Arven actividad forestal solicitada | `REQUIRE_RIGHT_AND_SUSTAINABLE_LIMIT` | `NO_AUTOMATIC_FOREST_REDUCTION` |
| DP17-T10 | Agujas asentamiento propuesto | `REJECT_PERMANENT_SETTLEMENT_IN_INTERIOR` | `NO_NEW_VILLAGE` |
| DP17-T11 | Aldea candidata recibe peso regional alto | `REQUIRE_ALL_TEN_DP14_GATES` | `NO_PROBABILITY_EQUALS_REAL_SITE` |
| DP17-T12 | Aldea reclama agua potable por proximidad | `REQUIRE_SOURCE_POTABILITY_RIGHT` | `NO_DRINKING_WATER_BY_RIVER_PROXIMITY` |
| DP17-T13 | Servicios a domicilio en localidad | `REQUIRE_PROVIDER_CAPACITY_AND_TRAVEL` | `NO_INSTANT_PROVIDER` |
| DP17-T14 | Vacante para joven de Norgard | `REQUIRE_WORK_AUTHORIZATION_AND_PROTECTIONS` | `NO_CHILD_EMPLOYMENT_DEFAULT` |
| DP17-T15 | Cambio de hogar y residencia | `REQUIRE_LEGAL_RIGHT_AND_ACTUAL_MOVE` | `NO_TELEPORT_OR_AUTO_PROPERTY` |
| DP17-T16 | Rumor sobre inspección aduanera | `REQUIRE_SOURCE_AND_VISIBILITY` | `NO_AI_OMNISCIENCE` |
| DP17-T17 | Incendio de almacén | `REQUIRE_CAUSE_GEOMETRY_CAPACITY` | `NO_UNCAUSED_INCIDENT` |
| DP17-T18 | Abastecimiento invernal piedemonte | `REQUIRE_REAL_WEATHER_AND_ROUTE` | `NO_FIXED_WINTER_CLOSURES` |
| DP17-T19 | Fhalion receptor de cuenca hipotético | `REJECT_MOUTH_NOT_AUTHORED` | `NO_FHALION_MOUTH_COORDINATES` |
| DP17-T20 | Aldea insular genera NPC persistente | `REQUIRE_VALID_REAL_SITE_AND_STABLE_IDS` | `NO_INSTANT_NPC_IN_LORE` |
| DP17-T21 | Compraventa de metales de Valkram | `REQUIRE_ASSAY_PROVENANCE_AND_LEDGER` | `NO_MINT_IN_TREIHORD` |
| DP17-T22 | Tratamiento de accidente | `REQUIRE_SKILL_MATERIALS_CAPACITY` | `NO_FREE_HOSPITAL_ASSUMPTION` |
| DP17-T23 | Investigación de persona no conocida | `REQUIRE_AUTHORIZED_KNOWLEDGE` | `NO_REVEAL_UNLEARNED_SECRETS` |
| DP17-T24 | Tala, erosión y recuperación del bosque | `REQUIRE_OCCURRED_CHANGE_AND_PERSISTENCE` | `NO_ONE_DAY_FOREST_REGENERATION` |

Cada caso es **TEST_ONLY**. Aquí no se ha invocado simulador, compilador C++ o juego real. El futuro validador estático solo certificará integridad del contrato y prohibiciones; no validará jugabilidad.

## Persistencia y visibilidad

- No alterar definiciones authored en función de una tirada aleatoria o un resultado de conversación.
- Si alguna vez se genera una instancia válida, persistir su identidad/seed/versión/relaciones y registrar deltas posteriores.
- Restringir información narrativa a lo percibido/conocido/autorizado por el personaje.
- Distinguir actor en ciudad de actor a bordo de embarcación: accesos/naval y guardia de la Casa no son intercambiables.
- Conservar ausencias: incapacidad, falta de agua, espera y suministro imposible no deben generar servicios de la nada.

El contrato de D.P17 no introduce nuevos eventos, NPC, edificios ni instituciones.

## Cierre de diseño D.P17 — 11/11/2026

Los 24 escenarios TEST_ONLY y namespaces de referencia se complementan con [D.P17/02 — Situaciones jugables, autoridad y memoria](02_situaciones_jugables_autoridad_y_memoria.md). El segundo documento desarrolla **cinco secuencias de interacción** y tres casos de continuidad social con fuentes, rechazos, espera y persistencia **como requisitos futuros**. D.P17 queda completa **como especificación conceptual**; no se ha implementado ni probado un runtime de Darovan.

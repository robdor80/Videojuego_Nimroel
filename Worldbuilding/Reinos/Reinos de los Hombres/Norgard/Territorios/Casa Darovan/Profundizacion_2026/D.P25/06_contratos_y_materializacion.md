# D.P25/06 — De personaje editorial a entidad persistente: contrato de futuro

**Diseño de integración, NO API existente ni código productivo.** Nimroel usa CoreRPG como autoridad única sobre reglas, estado, posición, atributos, relaciones, objetos, eventos y guardado; Godot 2D presenta, la IA interpreta. D.P25 solo aporta IDs, premisas narrativas y límites verificables.

## Identidad y promoción (nunca automática)
Un futuro `PersonEntityId` necesitará: ficha editorial vigente (`sourceBiographyId`), decisión autoral de materialización, persona única, edad/capacidad cuando sea jurídicamente relevante, tiempo, localización válida, hogar si procede, acceso físico probado, competencias/empleo reales, datos no públicos y cronología. Un `DP25-Pxx` es un **ID editorial**, distinto de `TRH-Nxx` de fuente y de un futuro `PersonEntityId`. No crear entidades por iterar el JSON.

Un origen RUR-S no puede ascender a domicilio o censo si no pasa D06 y D08. Para D.P23/Treihord, el manuscrito de 2.374 líneas tiene precedencia. El país, la justicia y límites territoriales son de Norgard, no de la IA.

## Registro conceptual de relación
```json
{
  "relationshipEntityId": null,
  "fromPersonEntityId": null,
  "toPersonEntityId": null,
  "basisEventId": null,
  "observedAt": null,
  "consentEvidenceIds": [],
  "dimensions": {"trust": null, "respect": null, "affection": null,
                 "suspicion": null, "fear": null, "debt": null},
  "knowledgeOfRelationship": [],
  "worldRevision": null
}
```
Los `null` significan desconocido/sin instancia, **no cero ni neutralidad probada**. Para cada dirección se exige evento justificante; el valor y las escalas se definirán cuando exista contrato CoreRPG real. No usar un único «favor» para sustituir propiedad o competencia. La confianza puede aumentar en A→B y no en B→A.

## Registro conceptual de conflicto
```json
{
  "conflictEntityId": null,
  "editorialConflictId": "DP25-C01",
  "triggerEvidenceIds": [],
  "eligibleActorEntityIds": [],
  "participationConsent": [],
  "requiredRightsIds": [],
  "materialObjectIds": [],
  "knowledgeVisibilityByActor": {},
  "actualRouteIds": [],
  "authorityDecisionIds": [],
  "expectedWorldRevision": null,
  "idempotencyKey": null,
  "status": "NOT_INSTANTIATED"
}
```
Las precondiciones se resuelven contra el estado real y sus fuentes. No aceptar `UNKNOWN` como `true`. Un conflicto sin jugador puede transcurrir solo si el futuro simulador dispone de actos, agenda, autonomía y reglas persistentes; este documento no los implementa.

## Separación verdad, conocimiento, percepción
1. **Verdad del mundo:** un documento existe o no; un barco llegó o no. Lo decide CoreRPG.
2. **Conocimiento/creencia del NPC:** sabe un hecho por observación, escrito que pudo leer, enseñanza o mensaje acreditado; puede guardar interpretación falsa con fuente y confianza, nunca por citar el inventario.
3. **Percepción actual del jugador:** oye, ve o consulta solo lo visible y autorizado, con perspectiva y momento. La IA no revela memorias privadas (VEL-M, TAR-M, SYV-M, TRH-M, RUR-M) sin escena y permiso legítimo.

`heardFrom` debe conservar cadena y versión; escuchar a Sarel no transporta automáticamente esa información a Syvaris. Una falsedad compartida sigue siendo una creencia, no verdad física.

## Actos, atomicidad e idempotencia
Entrada conceptual: `{actorEntityId, editorialSceneId, observedAt, evidenceRefs, rightsRefs, stockRefs, actualAccessRefs, consentRefs, expectedRevision, idempotencyKey}`. Salidas conceptuales: `allowed`, `blocked_missing_evidence`, `blocked_rights`, `blocked_resources`, `blocked_access`, `blocked_time`, `blocked_authority`, `offered_alternative`. Una transferencia real conserva un ID de lote, decrementa origen una vez y acredita recepción una vez; un segundo intento con la misma clave no duplica. No escribir un relato de éxito antes de recibir resultado autorizado.

## Cronología, acceso y distancia
- Veldora–Treihord admite **enlace cualitativo**, no distancia ni tiempo concreto.
- Belara en Treihord: barcaza de actividad industrial de poco calado, no canal universal ni acceso público a La Vena.
- Taramin: dos brazos del mismo Thalen, sin vado/puente/ferry garantizado.
- Arven–Syvaris: no hay enlace acreditado; los personajes pueden hablar de un trato **hipotético**, pero no comunicarse ni comerciar hasta probar transporte.
- En una partida sin lugar real, el encuentro permanece bloqueado, no teletransportado.

## Verificación antes de integración
`D.P25` es un **asset de diseño**. Para generar un content pack de personajes, en una fase distinta se exigirá: canon de origen fusionado; EntityId único; posición válida; presencia y calendario; capacidades; privacidad; relaciones iniciales **explícitamente respaldadas**; competencia/propiedad; contratos de CoreRPG; pruebas Windows y Android/Godot si afectan runtime. D.P26 auditará el paquete, no lo considerará motor implantado.

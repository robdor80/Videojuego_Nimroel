# Nimroel Core — personalidad y rasgos estables v0.2

## Autoridad

**CORE UNIVERSAL — namespace PERS**

La personalidad es un conjunto de tendencias relativamente estables, no una clase rígida ni un guion.

Principios obligatorios:

- varios rasgos coexisten;
- la expresión depende del contexto;
- una acción aislada no reescribe el rasgo;
- personalidad se separa de emoción, habilidad, reputación y moralidad;
- cultura y profesión no clonan personalidad;
- los cambios estables requieren historia significativa;
- NPC procedurales conservan rasgos tras materialización;
- NPC autorales no pueden ser sobrescritos por generación procedural.

La IA usa PERS como sesgo conductual, nunca como obligación absoluta.


---

## Ampliación PERS11–PERS28

PERS01–PERS10 mantienen exactamente su semántica anterior.

Se añaden:

- PERS11 — warmth;
- PERS12 — humor_frequency;
- PERS13 — empathy_expression;
- PERS14 — directness;
- PERS15 — tact;
- PERS16 — rule_orientation;
- PERS17 — authority_deference;
- PERS18 — ambition;
- PERS19 — competitiveness;
- PERS20 — initial_trust_speed;
- PERS21 — intimacy_openness;
- PERS22 — optimism;
- PERS23 — self_confidence;
- PERS24 — forgiveness_tendency;
- PERS25 — teaching_instinct;
- PERS26 — autonomy_need;
- PERS27 — status_sensitivity;
- PERS28 — pride.

La ampliación no exige migración de saves: un perfil antiguo con PERS01–PERS10 sigue siendo válido y puede resolver las dimensiones nuevas únicamente cuando necesite un perfil completo actualizado.

## Perfil persistente

La generación, promoción, persistencia y evolución se desarrollan en:

`personalidad_persistente_generacion_promocion_v0.1.md`

Contratos:

- `nimroel_persistent_personality_profile_contract_v0.1.json`;
- `nimroel_personality_assignment_promotion_contract_v0.1.json`;
- `nimroel_personality_evolution_continuity_contract_v0.1.json`;
- `nimroel_ai_personality_expression_context_contract_v0.1.json`.

## Alcance de producción actual

La mecánica es Core, pero la generación procedural de producción está activada actualmente **solo para humanos de Norgard**.

Ningún pueblo no humano hereda automáticamente recetas o distribuciones humanas.

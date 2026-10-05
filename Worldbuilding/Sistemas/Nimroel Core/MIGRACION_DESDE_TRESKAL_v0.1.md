# Nimroel Core — registro de migración desde Treskal v0.1

## Estado

**MIGRACIÓN ACTIVA**

Treskal continúa siendo el prototipo histórico, pero los sistemas marcados aquí ya tienen autoridad universal trasladada al Core.

| Sistema | Namespace | Core | Treskal |
| --- | --- | --- | --- |
| Memoria | MEM | activo | override de compatibilidad |
| Personalidad | PERS | activo | override de compatibilidad |
| Emoción / ánimo | EMO / MOOD | activo | override de compatibilidad |
| Objetivos | GOAL | activo | override de compatibilidad |
| Decisión | DEC | activo | override de compatibilidad |
| Confianza | TRUST | activo | override de compatibilidad |
| Opiniones | VIEW | activo | override de compatibilidad |
| Integridad de declaraciones | STAT | activo | override de compatibilidad |
| Credibilidad / verificación | CRED | activo | override de compatibilidad |
| Confidencialidad | CONF | activo | override de compatibilidad |
| Dinámica de conversación | DIAL | activo | override de compatibilidad |
| Atención / foco | ATTN | activo | override de compatibilidad |
| Expectativas | EXP | activo | override de compatibilidad |
| Presión / recuperación | STRS | activo | override de compatibilidad |
| Valores personales | VAL | activo | override de compatibilidad |
| Identidad / roles | SELF | activo | override de compatibilidad |
| Embarazo / parto / primera infancia | PREG | activo | override local explícito |
| Desarrollo infantil | CHD | activo | override de compatibilidad |
| Envejecimiento / vejez activa | AGE | activo | override de compatibilidad |
| Parentesco / red familiar | KIN | activo | override de compatibilidad |

## Compatibilidad

Para cada sistema migrado:

- se preservan IDs;
- no se remapean saves;
- Treskal no redefine semántica universal;
- un override local vacío significa herencia completa;
- cualquier excepción futura debe declararse explícitamente.

## Siguiente lote previsto

Fase cognitiva general cerrada salvo K.

K queda para un lote específico porque su autoridad actual está mezclada con información y reputación y debe separarse sin duplicar semántica.

Fase B iniciada:

- B1 ejecutado: PREG, CHD, AGE, KIN.
- siguiente lote: DEP / CARE, CHORE / DOM, REST, NEED.

PREG mantiene únicamente las particularidades locales reales de Treskal sobre entorno y asistencia del parto; no existe doble autoridad sobre el namespace PREG.

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

## Compatibilidad

Para cada sistema migrado:

- se preservan IDs;
- no se remapean saves;
- Treskal no redefine semántica universal;
- un override local vacío significa herencia completa;
- cualquier excepción futura debe declararse explícitamente.

## Siguiente lote previsto

- STAT;
- CRED;
- CONF;
- DIAL;
- ATTN;
- EXP.

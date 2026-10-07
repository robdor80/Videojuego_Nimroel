# Regresión — sistema de salud Core v0.1

## Estado esperado

**NIMROEL_CORE_HEALTH_STATICALLY_VALIDATED**

## Invariantes

1. HLTH no sustituye HCOND.
2. Pueden coexistir múltiples HCOND.
3. No existe barra universal de puntos de vida.
4. Una condición tiene severidad y trayectoria independientes.
5. Sangrado puede persistir entre escenas.
6. Dolor no equivale a severidad estructural.
7. Conciencia requiere causa fisiológica.
8. Herida no implica infección automática.
9. Infección necesita riesgo/causa/tiempo.
10. Enfermedad real y diagnóstico percibido son capas distintas.
11. No toda enfermedad es contagiosa.
12. Contagio requiere vía de exposición plausible.
13. OUTB necesita casos y propagación causal.
14. LOD no crea/borrar brotes.
15. HTRT puede estabilizar sin curar.
16. Tratamiento puede fallar.
17. Tratamiento inapropiado puede complicar.
18. Dormir no cura instantáneamente.
19. Recuperación consume tiempo.
20. Secuelas persisten.
21. NEED puede generar consecuencias HCOND sin desaparecer.
22. WASTE modifica riesgo, no crea enfermedad automática.
23. ACC puede generar varios HCOND.
24. PREG04 puede generar HCOND18.
25. HCOND18 no es automático en todo parto.
26. Recién nacidos usan el mismo principio causal de salud.
27. Muerte no se produce por HP=0 genérico.
28. La IA no crea condiciones.
29. La IA no cura.
30. La IA no mata.
31. La IA no inventa remedios.
32. Procedimientos invasivos requieren competencia y recursos.
33. Anestesia moderna no se presupone.
34. Antibióticos modernos no se presuponen.
35. Diagnóstico de laboratorio moderno no se presupone.
36. Material medicinal necesita canon externo.
37. Curación sobrenatural no se presupone.
38. Fisiología específica de pueblos puede añadir overrides futuros.
39. Save/load conserva condiciones.
40. Off-screen usa las mismas causas que on-screen.

## Regla final

Debe fallar cualquier implementación que trate salud como una barra abstracta, permita curación narrativa instantánea, invente enfermedad/medicina por IA o borre condiciones al cambiar de LOD.

`NIMROEL_CORE_HEALTH_STATICALLY_VALIDATED`

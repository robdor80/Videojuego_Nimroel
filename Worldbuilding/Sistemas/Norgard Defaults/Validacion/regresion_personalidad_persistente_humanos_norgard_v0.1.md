# Regresión — sistema de personalidad persistente de humanos de Norgard v0.1

## Estado esperado

**PERSISTENT_PERSONALITY_SYSTEM_NORGARD_HUMANS_ACTIVE**

## Invariantes principales

1. PERS01–PERS10 conservan significado.
2. PERS11–PERS28 amplían el modelo sin migración obligatoria.
3. A = autoral.
4. B = procedural persistente.
5. C = latente.
6. C→B se resuelve una sola vez.
7. C→B usa seed persistente.
8. Conducta ya observada limita el perfil generado.
9. B→A no rerollea.
10. Guardar/cargar no rerollea.
11. Cambiar LOD no rerollea.
12. Cambiar oficio no rerollea.
13. Cambiar residencia no rerollea.
14. Cambiar rango no rerollea.
15. Profesión no elige receta.
16. Sexo no elige receta.
17. riqueza/clase no eligen receta.
18. Gran Casa no elige receta.
19. localidad no elige receta.
20. cultura modifica expresión, no núcleo.
21. EMO/MOOD/STRS no sustituyen PERS.
22. TRUST/AFF/FRI/RIFT modifican comportamiento relacional, no personalidad global automáticamente.
23. Evolución estable requiere causa y procedencia.
24. No existe drift anual aleatorio.
25. Dos NPC pueden compartir receta pero no perfil exacto.
26. La biblioteca de Norgard contiene 80 recetas abstractas.
27. Ninguna receta usa el nombre de un personaje de referencia.
28. La IA puede expresar personalidad, no mutarla.
29. El motor decide promoción y evolución.
30. La activación actual es solo para humanos de Norgard.
31. Elfos y demás pueblos no humanos quedan bloqueados hasta su capa propia.
32. Treskal hereda el sistema sin override psicológico local obligatorio.

## Cobertura

El pack JSON asociado contiene 60 casos estáticos.

`Validacion/norgard_persistent_personality_validation_pack_v0.1.json`

## Regla final

Debe fallar cualquier implementación que rerollee un NPC persistente, seleccione personalidad por profesión/Casa/sexo, copie un personaje de referencia o active recetas humanas para un pueblo no humano.

`PERSISTENT_PERSONALITY_SYSTEM_NORGARD_HUMANS_ACTIVE`

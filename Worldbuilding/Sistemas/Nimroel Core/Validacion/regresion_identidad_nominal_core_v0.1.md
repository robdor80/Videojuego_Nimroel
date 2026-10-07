# Regresión — identidad nominal Core v0.1

## Estado esperado

**NIMROEL_CORE_NAME_STATICALLY_VALIDATED**

## Invariantes

1. NAME no sustituye npc_id.
2. NAME01 es nombre registrado vigente.
3. NAME02 permite estado provisional/sin registrar.
4. NAME03 conserva nombre legal anterior.
5. NAME04 representa alias/sobrenombre.
6. NAME05 permite identidad nominal desconocida/no resuelta.
7. Cambiar nombre no crea entidad nueva.
8. Nombre anterior permanece trazable.
9. Alias no cambia identidad legal.
10. Apodo no crea parentesco.
11. Título no se convierte en apellido.
12. Oficio no se convierte automáticamente en apellido.
13. K controla quién conoce un nombre.
14. CRED puede intervenir en una afirmación de identidad.
15. Nombre legal puede existir aunque sea desconocido para interlocutor.
16. Recién nacido puede existir antes de tener NAME01.
17. Nombrar no altera PREG.
18. Nombrar no altera KIN.
19. Nombrar no altera CARE.
20. Nombrar no altera RES.
21. Generación cultural debe ser determinista.
22. Generación debe consultar parentesco antes de resolver apellido.
23. Hogar no obliga apellido compartido.
24. Compartir apellido no crea parentesco.
25. Apellidos diferentes no borran parentesco.
26. LOD no rerollea nombre.
27. Save/load no rerollea nombre.
28. Cambio de oficio no cambia nombre.
29. Cambio de residencia no cambia nombre.
30. Cambio de rango no cambia nombre.
31. IA puede usar un nombre conocido.
32. IA no inventa nombre persistente.
33. IA no cambia nombre legal.
34. IA no revela nombre desconocido.
35. IA no infiere parentesco por apellido.
36. IA no infiere título por apellido.
37. Dos NPC pueden compartir nombre visible.
38. npc_id desambigua homónimos.
39. La cultura define repertorio y transmisión.
40. Core no impone reglas nominales humanas a pueblos no humanos.

`NIMROEL_CORE_NAME_STATICALLY_VALIDATED`

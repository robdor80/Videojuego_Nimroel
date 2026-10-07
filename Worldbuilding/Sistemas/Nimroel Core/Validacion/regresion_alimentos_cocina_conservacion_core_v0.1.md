# Regresión — alimentos, cocina y conservación Core v0.1

## Estado esperado

**NIMROEL_CORE_FOOD_STATICALLY_VALIDATED**

## Invariantes

1. FOOD01–FOOD06 representan estado del lote, no receta.
2. Una receta no crea ingredientes.
3. Preparación requiere stock.
4. Preparación térmica requiere combustible cuando procede.
5. Preparación consume tiempo.
6. Herramientas/recipientes pueden ser requisito.
7. Conservación necesita materiales.
8. Conservación necesita tiempo.
9. Conservación no hace eterno el lote.
10. Deterioro depende de contexto.
11. No existe caducidad universal única.
12. Contaminación puede existir sin deterioro visible.
13. Deterioro visible no es el único criterio sanitario.
14. Consumir alimento inseguro puede crear HCOND.
15. Enfermedad no es automática por edad del alimento.
16. Cocinar puede reducir ciertos riesgos.
17. Cocinar no restaura automáticamente FOOD05.
18. NEED01 requiere consumo real.
19. Comida rutinaria puede agregarse.
20. Escasez relevante debe preservarse.
21. Sustituto debe existir.
22. Sustituto debe ser culinariamente plausible.
23. Una receta no fija precio.
24. OWN conserva propiedad.
25. TXN conserva transacción.
26. Restos pueden producir WASTE.
27. Estación puede cambiar disponibilidad.
28. Clima puede cambiar deterioro.
29. Viaje no genera raciones.
30. Instituciones no generan raciones.
31. Raciones ocupan stock y transporte.
32. Raciones pueden deteriorarse.
33. LOD puede agregar consumo rutinario.
34. LOD no borra pérdidas.
35. LOD no borra contaminación relevante.
36. IA puede describir comida existente.
37. IA no inventa ingrediente.
38. IA no materializa plato.
39. IA no ignora combustible.
40. IA no crea canon culinario cultural.

## Regla final

Debe fallar cualquier implementación que convierta una receta en generador de recursos, borre deterioro en LOD o permita a la IA inventar comida.

`NIMROEL_CORE_FOOD_STATICALLY_VALIDATED`

# Regresión — tiempo y calendario Core v0.1

## Estado esperado

**NIMROEL_CORE_TIME_STATICALLY_VALIDATED**

## Invariantes

1. TIME no sustituye AGEN.
2. El tiempo absoluto es monotónico.
3. Un minuto tiene 60 segundos.
4. Una hora tiene 60 minutos.
5. Un día tiene 24 horas.
6. Una semana tiene 7 días.
7. Un año estándar tiene 365 días.
8. No existen bisiestos.
9. La fecha civil tiene 12 meses.
10. Febrero tiene siempre 28 días.
11. La semana comienza en lunes.
12. 1 de enero del año 1 es lunes.
13. No existe año 0.
14. No existen husos horarios por defecto.
15. No existe cambio horario estacional.
16. Guardar/cargar conserva tiempo exacto.
17. LOD no reinicia tiempo.
18. Off-screen no detiene la línea temporal.
19. Un salto temporal procesa consecuencias.
20. La fecha/hora puede expresarse con timestamp exacto.
21. Puede existir ancla de solo fecha.
22. Puede existir franja narrativa.
23. Puede existir ventana relativa.
24. Puede existir vencimiento.
25. La aritmética mensual conserva día si existe.
26. Si no existe, usa último día de mes.
27. La edad cambia por fecha de cumpleaños.
28. La celebración no altera la edad.
29. AGEN puede consumir TIME.
30. TIME no crea obligaciones.
31. Una expresión relativa persistente debe resolverse.
32. La IA puede leer el tiempo autorizado.
33. La IA no puede avanzar el reloj.
34. La IA no puede cambiar vencimientos.
35. La franja narrativa no sustituye luz ambiental.
36. Amanecer/ocaso no se fijan por las franjas.
37. Los nombres civiles no importan religión terrestre.
38. La campaña declara fecha inicial.
39. El año de referencia no refecha historia previa.
40. Toda simulación comparte la misma línea temporal.

`NIMROEL_CORE_TIME_STATICALLY_VALIDATED`

# Regresión E16 — calendario civil de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E16_CALENDAR_POINT_12_COMPATIBLE**

## Invariantes

1. El año tiene 365 días.
2. No existen años bisiestos.
3. Hay 12 meses.
4. Enero tiene 31 días.
5. Febrero tiene 28 días.
6. Marzo tiene 31 días.
7. Abril tiene 30 días.
8. Mayo tiene 31 días.
9. Junio tiene 30 días.
10. Julio tiene 31 días.
11. Agosto tiene 31 días.
12. Septiembre tiene 30 días.
13. Octubre tiene 31 días.
14. Noviembre tiene 30 días.
15. Diciembre tiene 31 días.
16. La semana tiene 7 días.
17. La semana comienza en lunes.
18. Existen lunes a domingo.
19. El día tiene 24 horas.
20. La hora tiene 60 minutos.
21. El minuto tiene 60 segundos.
22. No existe horario de verano.
23. No existen husos horarios internos.
24. 1 de enero del año 1 es lunes como ancla técnica.
25. No existe año 0.
26. 15375 es año de referencia actual.
27. 15374 sigue siendo válido.
28. La campaña declara fecha inicial concreta.
29. Primavera = marzo–mayo.
30. Verano = junio–agosto.
31. Otoño = septiembre–noviembre.
32. Invierno = diciembre–febrero.
33. Cambiar estación no cambia clima instantáneamente.
34. La estación es común y el clima local.
35. Medianoche cambia la fecha.
36. Guardar/cargar conserva fecha y hora.
37. Cambiar LOD no reinicia tiempo.
38. Tiempo off-screen avanza.
39. Saltar tiempo procesa consecuencias.
40. AGEN acepta fecha/hora exacta.
41. AGEN también acepta franja o ventana.
42. Hoy/mañana deben resolverse desde World State.
43. Un vencimiento persistente no queda solo como texto ambiguo.
44. 31 enero + 1 mes = 28 febrero.
45. Un año conserva día/mes.
46. La edad cambia al comenzar el cumpleaños.
47. Celebrar cumpleaños no es requisito jurídico.
48. El luto formal mantiene tres jornadas.
49. Jornada 1 del luto comienza en la fecha en que se conoce/asume la muerte.
50. Noticia tardía no consume jornadas anteriores.
51. Cremación tardía no alarga automáticamente el luto.
52. Alquiler puede usar día/semana/mes/año sin frecuencia obligatoria.
53. Pago mensual no equivale a cada 30 días.
54. Punto 12 no crea semana laboral de cinco días.
55. Sábado no implica descanso automático.
56. Domingo no implica descanso automático.
57. Mercados diarios de Treskal siguen siendo diarios.
58. Una feria especializada puede fijarse por fecha o día.
59. Punto 12 no crea fechas agrícolas automáticas.
60. Fecha/estación puede influir FOOD sin crear stock.
61. Fecha/estación puede influir pesca sin sustituir clima.
62. Punto 12 no importa Navidad.
63. Punto 12 no importa Semana Santa.
64. No existe santoral.
65. Meses/días no implican dioses terrestres.
66. Eventos locales pueden tener fecha.
67. Grandes Casas pueden declarar celebraciones temporales.
68. Corona puede declarar jornadas institucionales.
69. Un evento histórico puede generar aniversario si World State lo conserva.
70. Calendario no crea automáticamente una festividad.
71. Cumpleaños puede existir sin celebración.
72. Matrimonio puede registrar fecha.
73. Adopción puede registrar fecha.
74. Cambio de nombre puede registrar fecha.
75. Contrato puede registrar fecha.
76. Deuda puede registrar vencimiento.
77. Sentencia puede registrar fecha.
78. Muerte puede registrar fecha.
79. Herencia puede registrar apertura temporal.
80. Nacimiento puede registrar fecha/hora.
81. PREG no recibe duración inventada por Punto 12.
82. Hora exacta del motor no implica que NPC la conozca.
83. K puede limitar conocimiento de fecha/hora.
84. AGEN no puede duplicar tiempo.
85. IA no puede adelantar el reloj.
86. IA no puede cambiar un vencimiento.
87. IA no puede declarar festivo un día.
88. IA no puede inventar un aniversario.
89. IA no puede cambiar el día de la semana.
90. Formato interno YYYY-MM-DD es válido.
91. Formato visible D de mes de YYYY es válido.
92. Formato 24h es válido.
93. Franja narrativa no sustituye hora exacta.
94. Madrugada/mañana/mediodía/tarde/noche son capas narrativas.
95. Amanecer/ocaso no se fijan por franja.
96. Punto 12 no fija relojes físicos.
97. Punto 12 no fija campanas ni almanaques.
98. Punto 13 conserva autoridad sobre objetos de medición.
99. El calendario no refecha lore antiguo.
100. Toda simulación temporal usa una única línea de tiempo coherente.

`CALENDAR_POINT_12_CLOSED_NORGARD_CIVIL_CALENDAR`

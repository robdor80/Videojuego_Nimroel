# Regresión E13 — salud y curandería de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E13_HEALTH_POINT_9_COMPATIBLE**

## Casos

1. Salud no usa una barra universal de puntos de vida.
2. Un NPC puede tener varias condiciones simultáneas.
3. HLTH resume funcionalmente; no sustituye HCOND.
4. Una herida superficial no equivale automáticamente a estado grave.
5. Una herida profunda puede mantener sangrado hasta control real.
6. Terminar una escena no detiene sangrado.
7. Dolor y daño estructural son variables distintas.
8. Una lesión puede reducir movilidad sin incapacitar totalmente.
9. Una lesión grave puede dejar secuela persistente.
10. Dormir una noche no cura automáticamente una fractura.
11. Una herida puede infectarse, pero no toda herida se infecta.
12. La infección necesita riesgo, tiempo y causa.
13. Una infección local puede empeorar.
14. Una enfermedad puede existir sin diagnóstico correcto.
15. NPC y motor pueden sostener explicaciones distintas del mismo cuadro.
16. No toda fiebre es contagiosa.
17. Un brote necesita casos y ruta plausible.
18. El LOD no crea ni borra un brote.
19. Un accidente ACC puede crear varios HCOND.
20. ACC no sustituye a HCOND.
21. Deshidratación grave puede producir HCOND16.
22. Falta prolongada de alimentación puede producir HCOND17.
23. Exposición térmica grave puede producir HCOND09.
24. WASTE no causa enfermedad automáticamente.
25. Agua contaminada puede aumentar riesgo cuando existe exposición.
26. PREG04 puede producir HCOND18.
27. Una complicación de parto no es automática.
28. Un recién nacido puede enfermar sin dejar de ser NPC persistente.
29. La muerte sanitaria requiere causa; no HP=0 genérico.
30. La IA no puede crear lesión, enfermedad, infección o muerte.
31. La IA no puede curar.
32. La curandería de Norgard es predominantemente femenina.
33. Un hombre no está legalmente prohibido como curandero.
34. Aprendizaje formal sanitario puede comenzar a los 12.
35. Cumplir 18 no concede competencia automáticamente.
36. Menor de 18 no asume por defecto procedimiento sanitario de máxima responsabilidad.
37. Norgard no presupone hospital central.
38. Norgard no presupone colegio médico.
39. Norgard no presupone licencia regia universal.
40. Una curandera puede trabajar desde su vivienda.
41. Una curandera puede realizar visita a domicilio.
42. La disponibilidad de curandera depende de su agenda y estado.
43. Una especialista no atiende infinitos pacientes a la vez.
44. WAIT puede afectar a la atención sanitaria.
45. Una aldea no recibe curandera automática si no existe una real.
46. Una ciudad grande puede necesitar varias por capacidad, sin cifra fija universal.
47. Una curandera puede especializarse sin crear profesión nacional separada.
48. El prestigio no garantiza éxito.
49. Un mal resultado no demuestra delito.
50. Limpiar, vendar e inmovilizar pueden ser cuidados básicos plausibles.
51. Fracturas y dislocaciones requieren competencia y seguimiento.
52. Amputación es recurso extremo, no tratamiento ordinario.
53. Amputación puede fallar o matar.
54. No existe anestesia moderna por defecto.
55. No existen antibióticos modernos por defecto.
56. No existe diagnóstico de laboratorio moderno.
57. Puede existir conocimiento empírico eficaz sin teoría microbiana.
58. Un material medicinal debe existir canónicamente.
59. No existe "hierba curativa genérica".
60. Punto 9 no inventa flora medicinal concreta.
61. Atención sanitaria puede pagarse en moneda.
62. Atención sanitaria puede pagarse en especie.
63. Atención sanitaria puede formar una deuda válida si hubo compensación acordada.
64. Deuda sanitaria no crea propiedad sobre el paciente.
65. Las anclas económicas no son tarifas obligatorias.
66. Un caso urgente puede desplazar una consulta ordinaria.
67. Priorizar urgencia consume capacidad real.
68. Una curandera puede estar enferma o descansando.
69. Información sanitaria no se hace rumor público automáticamente.
70. Existe norma social de discreción sin código médico moderno.
71. Un riesgo grave a terceros puede justificar comunicación limitada.
72. Un brote local no activa automáticamente restricciones en todo Norgard.
73. Una autoridad local/territorial puede coordinar medidas temporales.
74. La Corona puede coordinar un brote que cruza territorios.
75. No existe ministerio sanitario permanente.
76. No existe duración universal fija de aislamiento.
77. Ejército y Armada pueden usar curanderas/personal sanitario si existen y están asignados.
78. No existe número universal de sanadores por unidad o buque.
79. Una Casa noble puede mantener curandera privada.
80. Curandera privada de una Casa no crea hospital público.
81. El parto puede ocurrir en hogar/alojamiento.
82. No existe maternidad institucional universal.
83. PREG06 puede dejar consecuencias sanitarias reales.
84. Anciano no equivale automáticamente a enfermo.
85. HLTH puede afectar EMP sin crear baja laboral moderna universal.
86. Viajar enfermo no genera atención automática en ruta.
87. Una curandera puede emitir opinión de causa de muerte sin conocer la verdad omnisciente.
88. No existen dioses ni sacerdocio sanitario.
89. No se presupone milagro, resurrección ni magia curativa genérica.
90. Cualquier curación sobrenatural futura requiere contrato propio.

## Regla de regresión

Debe fallar cualquier implementación que cure instantáneamente, invente remedios, teletransporte especialistas, convierta toda fiebre en contagio, use conocimientos médicos modernos no canonizados o permita a la IA mutar HLTH/HCOND/HTRT/OUTB.

Marcador esperado:

`HEALTH_POINT_9_CLOSED_NORGARD_HEALING_TRADITION`

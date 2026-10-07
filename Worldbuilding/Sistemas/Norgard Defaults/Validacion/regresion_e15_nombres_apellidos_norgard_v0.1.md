# Regresión E15 — nombres personales y apellidos de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E15_NAMING_POINT_11_COMPATIBLE**

## Invariantes

1. El nombre visible no sustituye npc_id.
2. NAME01–NAME05 no sustituyen K/KIN/SELF/CRED.
3. Un apodo no se convierte automáticamente en apellido legal.
4. Un título no forma parte automáticamente del nombre civil.
5. Cambiar de nombre no crea un NPC nuevo.
6. Cambiar de nombre no borra obligaciones.
7. Un recién nacido puede estar temporalmente NAME02.
8. Nombrarlo no recrea la entidad.
9. Norgard usa un apellido legal vigente por persona.
10. No existe doble apellido obligatorio.
11. No existe patronímico obligatorio.
12. No existe apellido diferente por sexo.
13. No existe apellido de bastardo.
14. Un progenitor jurídico al registro → su apellido por defecto.
15. Dos progenitores jurídicos pueden elegir uno de sus dos apellidos.
16. No se combinan ambos automáticamente.
17. Falta de acuerdo → apellido de quien dio a luz como fallback registral.
18. Ese fallback no concede más autoridad parental.
19. Reconocimiento posterior de segundo progenitor no cambia apellido automáticamente.
20. Menor sin progenitor conocido recibe apellido ordinario no protegido.
21. Ese apellido no debe marcar orfandad o ilegitimidad.
22. Nacer fuera de matrimonio no altera reglas nominales.
23. Matrimonio no cambia apellidos automáticamente.
24. Cualquiera de los cónyuges puede mantener su apellido.
25. Cualquiera puede solicitar adoptar el del otro.
26. No existe prioridad por sexo.
27. Disolución no revierte apellido automáticamente.
28. Viudedad no revierte apellido automáticamente.
29. Cambio legal adulto requiere registro.
30. Nombre anterior queda trazable.
31. Cambio de nombre no borra deuda.
32. Cambio de nombre no borra delito.
33. Cambio de nombre no borra parentesco.
34. Cambio de nombre no borra matrimonio.
35. Cambio de nombre no borra propiedad.
36. Cambio de menor requiere autoridad válida.
37. Menor maduro debe ser escuchado.
38. Adopción no cambia apellido automáticamente.
39. Adopción puede mantener apellido previo.
40. Adopción puede usar apellido adoptivo mediante resolución.
41. Nombre previo adoptivo queda en historial.
42. Apellido adoptivo no crea sangre.
43. Apellido adoptivo no crea título.
44. Matrimonio con progenitor no cambia apellido del hijastro.
45. Hermanos pueden tener apellidos distintos.
46. Apellidos distintos no borran KIN.
47. Compartir apellido no prueba KIN.
48. Hogar no implica un solo apellido.
49. Apodos pueden persistir como NAME04.
50. Oficio usado como sobrenombre no se vuelve apellido automáticamente.
51. Aethros está protegido.
52. Darovan está protegido.
53. Edranor está protegido.
54. Galdren está protegido.
55. Valrik está protegido.
56. Ninguno se asigna random.
57. Matrimonio con Gran Casa no concede apellido protegido automático.
58. Apellido protegido no concede señorío.
59. Apellido protegido no concede sangre.
60. Apellido protegido no concede sucesión especial.
61. Soberano Aethros mantiene Aethros.
62. Hijos legítimos del monarca usan Aethros.
63. Rama secundaria puede usar otro apellido.
64. Rama secundaria que accede a Corona restablece Aethros.
65. Adopción no crea sangre Aethros.
66. Lord/Lady/Rey/Reina se resuelven fuera de NAME.
67. Dos NPC pueden compartir nombre completo.
68. npc_id desambigua homónimos.
69. La IA no inventa nombre persistente.
70. La IA no revela nombre desconocido.
71. La IA no infiere parentesco por apellido.
72. La IA no concede título por apellido.
73. A = nombre autoral.
74. B = nombre procedural persistente.
75. C = seed nominal latente.
76. C→B resuelve nombre una sola vez.
77. C→B consulta KIN antes del apellido.
78. Un nombre ya observado es vinculante.
79. Guardar/cargar no rerollea nombre.
80. Cambiar LOD no rerollea nombre.
81. Cambiar oficio no cambia apellido.
82. Mudarse no cambia apellido.
83. Cambiar rango no cambia apellido.
84. El generador no usa apellidos protegidos.
85. El generador evita nombres autorales reservados por defecto.
86. Los sesgos regionales no son exclusivos.
87. Un nombre Valrik puede aparecer en Darovan.
88. No existen cinco lenguas nominales por Casa.
89. Nombre legal puede existir aunque su portador no sepa escribir.
90. Variación ortográfica documental no crea NPC nuevo.
91. Herencia se decide por ley, no por apellido.
92. Reputación por apellido depende de conocimiento real.
93. Registro nominal puede contener error/fraude.
94. Pérdida de registro no borra identidad real.
95. Punto 11 no crea santoral.
96. Punto 11 no crea onomástica religiosa.
97. Punto 11 no define nombres élficos.
98. Punto 11 no define otros pueblos.
99. El generador de Norgard solo está activo para humanos de Norgard.
100. Un apellido siempre debe derivar de ley, registro o generación autorizada.

## Regla de regresión

Debe fallar cualquier implementación que rerollee nombres, genere apellidos de Gran Casa al azar, marque bastardía mediante apellido, cambie apellido por matrimonio automáticamente o use el apellido como sustituto de parentesco.

`NAMING_POINT_11_CLOSED_NORGARD_PERSONAL_NAMES_SURNAMES`

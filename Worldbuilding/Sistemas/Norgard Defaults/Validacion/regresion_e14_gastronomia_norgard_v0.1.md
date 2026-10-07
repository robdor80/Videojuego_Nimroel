# Regresión E14 — gastronomía y alimentación de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E14_CUISINE_POINT_10_COMPATIBLE**

## Invariantes

1. Una receta no crea ingredientes.
2. Un plato necesita stock real.
3. Una preparación caliente necesita combustible cuando corresponde.
4. Cocinar consume tiempo.
5. Cocinar puede requerir herramienta o recipiente.
6. FOOD persiste a través de LOD.
7. Pueden existir lotes agregados.
8. Un alimento puede deteriorarse.
9. Conservar no vuelve eterno un alimento.
10. Salazón necesita sal real.
11. Salmuera necesita sal y agua.
12. Ahumado necesita instalación/combustible compatibles.
13. Encurtido necesita medio ácido canónico.
14. Fermentar necesita tiempo.
15. Alimento viejo no enferma automáticamente.
16. Alimento contaminado puede causar HCOND.
17. Cocinar no reinicia mágicamente un lote podrido.
18. NEED01 requiere consumo real.
19. Rutina alimentaria estable puede agregarse.
20. Escasez relevante obliga a bajar a detalle.
21. No existe obligación universal de tres comidas.
22. Trabajo puede incluir comida como compensación.
23. Posada no posee menú infinito.
24. Mercado no posee comida preparada infinita.
25. Un banquete noble consume stock real.
26. Una fiesta puede tensionar mercado local.
27. Viaje no genera raciones.
28. Ejército no genera raciones.
29. Armada no genera raciones.
30. Comida reservada a institución no está libre para venta.
31. Receta no fija precio.
32. Precio sigue World State y Punto 5.
33. Temporada puede alterar disponibilidad.
34. Clima puede alterar deterioro.
35. Corte de ruta puede eliminar importados.
36. Mala pesca puede reducir pescado fresco.
37. Conservado puede sustituir fresco solo si existe stock.
38. Sustitución debe ser culinariamente plausible.
39. Sustitución no crea ingrediente inexistente.
40. La IA no inventa ingredientes.
41. La IA no inventa platos regionales como canon.
42. La IA puede elegir una preparación canónica disponible.
43. PERS/PREF puede generar gustos personales.
44. Cultura no obliga a que todos compartan gusto.
45. MEM puede recordar una comida.
46. EMO puede asociarse a una comida sin cambiar el alimento.
47. FOOD no sustituye OWN.
48. FOOD no sustituye TXN.
49. FOOD no sustituye WASTE.
50. Restos pueden entrar en WASTE.
51. Norgard canoniza trigo.
52. Norgard canoniza cebada.
53. Norgard canoniza avena.
54. Norgard canoniza centeno.
55. Norgard canoniza guisantes.
56. Norgard canoniza habas.
57. Norgard canoniza lentejas.
58. Norgard canoniza cebolla.
59. Norgard canoniza puerro.
60. Norgard canoniza col.
61. Norgard canoniza nabo.
62. Norgard canoniza zanahoria.
63. Norgard canoniza remolacha.
64. Norgard canoniza manzana.
65. Norgard canoniza pera.
66. Norgard canoniza ciruela.
67. Norgard canoniza uva.
68. Norgard canoniza miel.
69. Norgard canoniza sal.
70. Norgard canoniza vinagre.
71. Patata no es básico canónico.
72. Azúcar refinado no es básico común.
73. Especias exóticas no aparecen sin comercio/canon.
74. Agua es bebida normal.
75. No se presupone que todo el mundo beba alcohol por seguridad.
76. Cerveza es común.
77. Cerveza Valrik sigue siendo ordinaria, no bebida de lujo automática.
78. Edranor sigue siendo principal región vinícola conocida.
79. Vino Edranor puede viajar a otras regiones.
80. Galdren sigue siendo granero y zona ganadera principal.
81. Valrik conserva fuerte sesgo pesquero.
82. Darovan puede acceder mejor a importados por comercio, no por spawn.
83. Hallheim puede reunir productos de todo el Reino si llegaron realmente.
84. Syvaris/Taramin no reciben flora nueva por analogía mediterránea.
85. Clase social no bloquea legalmente ingredientes.
86. Riqueza puede aumentar frecuencia/variedad/calidad.
87. Un noble puede comer un guiso sencillo.
88. Una persona pobre puede comer carne si tiene acceso real.
89. Pan puede variar por cereal y molienda.
90. Olla/guiso admite sustituciones plausibles.
91. Carne no se consume diariamente por defecto en todo hogar.
92. Pescado puede ser cotidiano donde existe acceso.
93. Queso curado es apto para viaje cuando existe.
94. Huevos dependen de aves reales.
95. Fruta depende de estación/almacenamiento/comercio.
96. Dulces comunes favorecen miel/fruta frente a azúcar refinado.
97. Hospitalidad no crea pacto religioso de pan y sal.
98. Norgard no copia platos con nombre de las obras de referencia.
99. El catálogo contiene 40 preparaciones canónicas iniciales.
100. Nuevos platos futuros deben respetar el mismo contrato material.

## Regla de regresión

Debe fallar cualquier implementación que materialice comida desde una receta, invente ingredientes por IA, ignore stock/estación/conservación, convierta riqueza en dieta rígida o copie platos distintivos del corpus de referencia como canon de Norgard.

Marcador esperado:

`CUISINE_POINT_10_CLOSED_NORGARD_CUISINE`

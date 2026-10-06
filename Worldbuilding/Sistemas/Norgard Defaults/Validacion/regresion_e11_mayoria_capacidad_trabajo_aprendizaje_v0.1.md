# Regresión E11 — mayoría de edad, capacidad legal, trabajo y aprendizaje de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E11_LABOR_POINT_7_COMPATIBLE**

## Casos

1. La mayoría de edad general se alcanza a los 18 años.
2. Gobernar como soberano desde los 16 no crea mayoría civil general.
3. Entre 0 y 7 años no existe capacidad laboral.
4. Entre 8 y 11 años puede existir ayuda ligera, pero no empleo.
5. Antes de los 12 años no existe aprendizaje profesional formal.
6. Desde los 12 años puede comenzar aprendizaje formal.
7. Entre 12 y 14 el aprendizaje requiere responsable legal y asentimiento del menor.
8. Entre 12 y 14 no existe empleo adulto ordinario.
9. Un aprendiz de 12–14 puede contribuir a producción real.
10. Un aprendiz menor no reemplaza automáticamente a un trabajador competente.
11. Desde los 15 años puede existir empleo juvenil ordinario compatible.
12. Entre 15 y 17 el consentimiento del joven es obligatorio.
13. Un contrato laboral prolongado de 15–17 requiere intervención del responsable legal.
14. Cumplir 15 o 18 años no sube automáticamente el estado APR.
15. CHD no se deriva automáticamente de la edad legal.
16. Un menor no recibe carga laboral adulta por defecto.
17. Ayuda familiar no crea automáticamente EMP.
18. Parentesco no permite trabajo forzado.
19. Norgard no fija una jornada universal de ocho horas.
20. Un horario físicamente imposible no es válido por existir contrato.
21. El trabajo realizado conserva derecho a compensación.
22. Insolvencia del empleador crea deuda, no dinero.
23. No existe salario universal de aprendiz.
24. Un aprendizaje sin formación real puede constituir explotación.
25. Menores de 12 no realizan trabajo peligroso.
26. Entre 12 y 14 el riesgo solo entra como aprendizaje con supervisión suficiente.
27. Entre 15 y 17 el riesgo exige competencia y supervisión/respaldo.
28. Un menor no recibe por defecto la máxima responsabilidad de seguridad.
29. Un trabajador puede finalizar una relación ordinaria; el contrato no lo convierte en propiedad.
30. No existe indemnización universal automática por despido.
31. Una deuda no crea propiedad sobre el deudor.
32. Un aprendiz no puede ser vendido.
33. Un trabajador no puede ser vendido.
34. El trabajo penal pertenece al sistema penal y no es empleo privado.
35. Un combatiente de fuerza territorial, Corona o Armada debe tener 18 años o más.
36. No existe leva armada válida de menores.
37. Un menor puede recibir formación militar/naval no combatiente compatible con su edad.
38. De 0 a 11 años no se impone sentencia penal.
39. De 12 a 14 la responsabilidad penal exige comprensión demostrada.
40. De 12 a 14 no existe muerte, destierro perpetuo, marca, mutilación, azotes ni trabajo penal adulto.
41. De 15 a 17 el máximo ordinario es la mitad del rango adulto.
42. De 15 a 17 no existe muerte, destierro perpetuo, marca, mutilación ni azotes.
43. Desde los 18 se aplica régimen penal adulto.
44. No existe prohibición laboral general por sexo.
45. Los acuerdos cotidianos pequeños de 15–17 pueden celebrarse con capacidad limitada.
46. Las grandes obligaciones patrimoniales de menores siguen dependiendo del Punto 8.
47. La falta de contrato escrito no invalida automáticamente un acuerdo laboral ordinario.
48. Un acuerdo oral puede probarse mediante hechos, pagos, testigos o registros.
49. APR06 significa autonomía técnica, no mayoría de edad.
50. EMP y APR pueden coexistir sin fusionarse.

## Regla de regresión

Debe fallar cualquier implementación que permita empleo infantil ordinario antes de 12, aprendizaje formal antes de 12, combate antes de 18, trabajo forzoso por deuda o parentesco, o que convierta edad en competencia profesional automática.

Marcador esperado:

`LABOR_POINT_7_CLOSED_NORGARD_AGE_CAPACITY_WORK_APPRENTICESHIP`

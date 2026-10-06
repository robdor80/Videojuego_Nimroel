# Regresión E10 — familia, matrimonio, filiación, tutela y adopción de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E10_FAMILY_POINT_6_COMPATIBLE**

## Casos

1. La mayoría general sigue siendo 18 años.
2. La excepción regia de gobierno a los 16 no permite matrimonio antes de los 18.
3. Un matrimonio exige dos adultos, consentimiento libre, autoridad reconocida y dos testigos adultos.
4. El sexo de los contrayentes no altera la validez.
5. Norgard solo reconoce un matrimonio válido simultáneo por persona.
6. Convivencia prolongada no crea matrimonio.
7. AFF05 no crea matrimonio.
8. Compartir hijos no crea matrimonio.
9. Un matrimonio no crea automáticamente hogar compartido.
10. Un matrimonio no crea propiedad conjunta automática.
11. Un matrimonio no convierte al cónyuge en progenitor de hijos previos.
12. Ascendiente/descendiente, hermanos, medio hermanos y tío-sobrina equivalentes están prohibidos.
13. Los primos no están prohibidos por la ley general del Reino.
14. Un matrimonio obtenido por coacción puede ser nulo y los hechos se remiten a delitos ya existentes cuando encajen.
15. Separación de hecho no permite volver a casarse.
16. La Justicia puede disolver un matrimonio por mutuo acuerdo.
17. La Justicia puede disolverlo por causa grave probada.
18. El adulterio no es delito penal por sí solo.
19. La muerte del cónyuge termina el matrimonio.
20. El luto de tres jornadas no crea prohibición posterior de matrimonio.
21. El segundo progenitor no se infiere por matrimonio, pareja o convivencia.
22. La filiación adicional necesita reconocimiento, registro válido o resolución.
23. No existe prueba genética moderna.
24. El World State puede conocer un hecho biológico que la Justicia no pueda demostrar.
25. Nacer fuera del matrimonio no reduce protección penal o civil básica.
26. La sucesión ordinaria Aethros sigue exigiendo sangre y nacimiento dentro de matrimonio válido.
27. Una adopción no crea sangre Aethros.
28. Una boda posterior de los progenitores no convierte retroactivamente a un descendiente Aethros nacido fuera de matrimonio en sucesor ordinario.
29. La filiación parental crea deber de cuidado y representación.
30. No existe preferencia automática de madre o padre por sexo en guarda.
31. El tutor no se convierte en progenitor.
32. La tutela puede ser temporal.
33. Parentesco no convierte automáticamente a una persona en tutor.
34. Una persona adulta puede adoptar individualmente.
35. Una adopción conjunta exige que los dos adoptantes estén casados entre sí.
36. La adopción crea filiación jurídica permanente.
37. La adopción no borra el hecho biológico ni KIN histórico.
38. Un padrastro o madrastra no adquiere filiación por matrimonio.
39. La compra de un menor no puede presentarse como adopción.
40. El matrimonio con un miembro de Gran Casa no concede señorío.
41. El matrimonio con el soberano crea consorte, no soberanía.
42. Los registros jurídicos son evidencia y pueden contener error o fraude.
43. AFF, KIN, CARE, RES, OWN y PREG conservan su autoridad propia.
44. La IA no puede inventar consentimiento, matrimonio, filiación, tutela o adopción.

## Regla de regresión

Debe fallar cualquier implementación que convierta automáticamente pareja en matrimonio, matrimonio en filiación biológica, tutor en progenitor, adopción en sangre dinástica o cónyuge en propietario/soberano.

Marcador esperado:

`FAMILY_POINT_6_CLOSED_NORGARD_FAMILY_LAW`

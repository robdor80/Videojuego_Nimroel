# Regresión E12 — propiedad, herencia y alquiler de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E12_PROPERTY_POINT_8_COMPATIBLE**

## Casos

1. Poseer físicamente un objeto no convierte al actor en propietario.
2. Vivir en una vivienda no convierte al ocupante en propietario.
3. Gobernar un territorio no convierte a una Gran Casa en propietaria de todos sus inmuebles.
4. La Corona puede poseer bienes institucionales distintos del patrimonio privado del monarca.
5. Una Gran Casa puede poseer bienes institucionales distintos del patrimonio privado de su Lord/Lady.
6. El matrimonio no crea comunidad universal automática de bienes.
7. Una herencia recibida individualmente por un cónyuge sigue siendo individual.
8. Una compra conjunta sin cuotas distintas se presume a partes iguales.
9. Un menor puede ser propietario.
10. El tutor no adquiere propiedad sobre bienes del menor.
11. Vender un inmueble relevante de un menor requiere autorización de Justicia.
12. Una transmisión voluntaria de inmueble exige documento/acta y dos testigos adultos.
13. La ocupación prolongada no transfiere automáticamente propiedad.
14. La muerte del propietario no elimina un negocio.
15. El caudal incluye solo bienes y participaciones del fallecido.
16. Bienes institucionales no entran en herencia privada.
17. Las deudas del fallecido se pagan con el caudal antes del reparto.
18. El heredero no adquiere deuda personal ilimitada por aceptar.
19. Puede existir testamento ordinario desde los 18 años.
20. Testamento ordinario exige dos testigos adultos.
21. Puede existir testamento de emergencia con tres testigos adultos.
22. El testamento más reciente válido prevalece.
23. Con descendientes, al menos 1/2 del caudal neto queda reservado a ellos.
24. Con cónyuge y descendientes, el cónyuge conserva al menos 1/4.
25. Cónyuge sin descendientes conserva al menos 1/2.
26. Sin testamento, cónyuge + descendientes = 1/3 y 2/3.
27. Descendientes sin cónyuge = 100 % por ramas.
28. Hijo adoptado hereda como hijo jurídico ordinario.
29. Hijo jurídicamente reconocido nacido fuera de matrimonio hereda como hijo ordinario.
30. Hijastro sin adopción no es heredero descendiente automático.
31. Tutor no hereda por el mero hecho de ser tutor.
32. La herencia civil ordinaria no altera sucesión Aethros.
33. La herencia civil ordinaria no decide el señorío de una Gran Casa.
34. Un heredero indigno requiere declaración judicial.
35. Indignidad no borra parentesco.
36. Un heredero puede renunciar.
37. Un concebido al morir el causante puede reservar cuota si luego nace vivo.
38. Muertes de orden incierto no crean herencia recíproca inventada.
39. Un menor puede heredar sin que el tutor adquiera el bien.
40. Un inmueble indivisible no se duplica para satisfacer cuotas.
41. El alquiler concede uso, no propiedad.
42. Un contrato de alquiler puede ser oral si puede probarse.
43. Impago de renta crea deuda.
44. Impago no transfiere automáticamente los bienes personales del arrendatario.
45. No existe desalojo legal automático mediante fuerza privada.
46. Una disputa de desalojo puede requerir Justicia del Rey.
47. Vender una vivienda no borra automáticamente un alquiler válido conocido/probado.
48. La muerte del arrendador no extingue automáticamente el alquiler.
49. La muerte del arrendatario no expulsa instantáneamente al hogar.
50. La ausencia temporal no equivale a abandono.
51. Bien robado vendido a tercero no adquiere título válido automáticamente.
52. Posesión histórica es evidencia, no prueba absoluta.
53. Un objeto encontrado no se convierte automáticamente en propiedad del hallador.
54. Una transferencia de propiedad no borra automáticamente deuda fiscal ya nacida.
55. OWN, RES y BIZ conservan sus autoridades funcionales.

## Regla de regresión

Debe fallar cualquier implementación que convierta residencia en propiedad, matrimonio en comunidad universal, tutor en dueño, título político en propiedad territorial total, muerte en borrado de deudas/negocios o impago en desalojo violento automático.

Marcador esperado:

`PROPERTY_POINT_8_CLOSED_NORGARD_PROPERTY_INHERITANCE_RENTAL`

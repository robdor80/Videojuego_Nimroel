# Regresión E2 — sistema monetario y acuñación de Norgard v0.2

## Estado esperado

**NORGARD_DEFAULT_E2_MONETARY_POINT_5_COMPATIBLE**

## Casos

1. Solo la Corona de Norgard puede acuñar moneda oficial.
2. La única ceca oficial permanente es la **Ceca Real de Hallheim**.
3. La Ceca depende del Tesoro de la Corona.
4. Una Gran Casa con minas de oro o plata no obtiene derecho de acuñación.
5. **El Crisol no es una ceca**.
6. Solo existen como denominaciones oficiales cerradas **Clavo, Luna y Corona**.
7. 1 Luna = 24 Clavos.
8. 1 Corona = 20 Lunas = 480 Clavos.
9. Clavo: 6,0 g y cobre mínimo 950‰.
10. Luna: 3,6 g y plata 900‰.
11. Corona: 4,5 g y oro 900‰.
12. El metal privado aceptado por la Ceca soporta tasa ordinaria de acuñación del 2,5 %.
13. Los lingotes no son moneda y se valoran por metal/peso/pureza/autenticidad.
14. La moneda extranjera no tiene curso legal obligatorio.
15. Una obligación oficial satisfecha con moneda extranjera debe convertirse a equivalente en Clavos.
16. No existe cambio monetario interno al atravesar territorios de Grandes Casas.
17. Multas: F1=12, F2=48, F3=240, F4=960 y F5=4.800 Clavos.
18. Falsificación y acuñación ilícita remiten al código penal ya cerrado.
19. La fiscalidad utiliza Clavo como unidad contable sin inventar un porcentaje tributario universal.
20. El motor no crea moneda por escribir una cifra en un libro.
21. No se inventan denominaciones adicionales.
22. No se interpreta el gramo técnico como obligación de terminología diegética.

## Regla de regresión

Cualquier implementación que cree una moneda oficial nueva, permita acuñar a una Gran Casa, sitúe la ceca en Treihord o convierta El Crisol en ceca debe fallar esta regresión.

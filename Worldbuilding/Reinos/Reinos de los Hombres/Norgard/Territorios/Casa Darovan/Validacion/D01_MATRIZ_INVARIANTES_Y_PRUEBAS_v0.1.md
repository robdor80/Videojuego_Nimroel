# DAROVAN D01 — Matriz de invariantes y pruebas estáticas

**Estado:** controles de documentación; no se afirma ejecución del motor ni prueba de mapa. La fuente primaria sigue siendo el canon.

| ID | Invariante | Resultado esperado |
|---|---|---|
| D01-01 | PR #14 fusionada antes de D01 | base de rama incluye merge D00 |
| D01-02 | Cuatro ciudades y solo cuatro anclas Darovan | Treihord, Veldora, Taramin, Syvaris; manuales |
| D01-03 | Karsath excluida | ningún territorio Darovan asignado a Karsath |
| D01-04 | Arven no adjudicada | administrativeOwner null en Arven |
| D01-05 | Belara–Treihord | riverCrossesCity = false; puerto industrial poco calado |
| D01-06 | Belara/Lhera | bifurcación de Lhera y bocas distintas, no inversión |
| D01-07 | Veldora río | curso independiente de Belara/Lhera |
| D01-08 | Thalen/Taramin | desembocadura bifurcada del mismo río, ciudad entre brazos |
| D01-09 | Agujas | ningún asentamiento permanente en su interior |
| D01-10 | Taramin/Syvaris | heterogeneidad, no desierto uniforme ni selva uniforme |
| D01-11 | Valkram | eje montañoso, no frontera política automática completa |
| D01-12 | Carta | geometría/altura/coordenadas/bordes exactos NO creados |
| D01-13 | Fuentes | todas las sourcePaths del perfil existen en main base |
| D01-14 | JSON | parseable; IDs de unidades y ciudades únicos |
| D01-15 | Jerarquía | Core → Norgard Defaults → Darovan → Localidad → World State |
| D01-16 | Aislamiento | ningún fichero de Core, Defaults, Valrik, Treihord canónica modificado |
| D01-17 | Runtime | perfil marcado no-runtime, cero entidades materializadas |
| D01-18 | Transferencia D02 | perfil de interfaces sin inventar afluentes, caudales o cuencas |

## Procedimiento reproductible (estático)
1. Leer Datos operativos/darovan_d01_relief_profile_v0.1.json y comprobar análisis JSON estándar, unicidad de IDs, tipado de null y booleans.
2. Comparar las sourcePaths con el árbol real del commit base, no solo nombres de una tabla de auditoría.
3. Inspeccionar diff de la rama frente a main, limitarlo a Casa Darovan.
4. Revisar coherencia semántica manual con documentos originales: montanas.md, rios_y_lagos.md, mares_y_costas.md, bosques.md, regiones_naturales.md, geografia_general.md, Treihord.md y perfiles visuales.
5. Registrar commit inicial/base y SHA final; declarar que las pruebas de runtime siguen pendientes hasta D11.

## Pruebas de regresión negativas
No son hechos geográficos: intentar registrar Eshneva como nuevo río, Belara atravesando Treihord, Veldora como brazo de Lhera, puerto oceánico profundo en Treihord, dos ríos Thalen, pueblo dentro de Agujas, Arven = Darovan, Karsath = Darovan, Taramin todo desierto o Syvaris todo jungla **debe fallar**. Una ruta sin escala y una divisoria que obligue al agua a subir de cota también deben fallar cuando exista simulación.

**Alcance real:** esta matriz es criterio de verificación; los resultados de ejecución concreta se registran en el acta D01.

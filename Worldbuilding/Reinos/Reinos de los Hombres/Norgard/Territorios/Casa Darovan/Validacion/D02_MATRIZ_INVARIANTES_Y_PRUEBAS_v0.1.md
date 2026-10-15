# DAROVAN D02 — Matriz de invariantes y pruebas v0.1

**Ámbito:** controles estructurales/semánticos documentales y script Python; no significa runtime implementado.

| ID | Condición | Verificación |
|---|---|---|
| D02-01 | D01 fusionada en main antes de rama | PR #15 merged=true, base merge 9f3f723 |
| D02-02 | Jerarquía Core→Defaults→Darovan→Localidad→WorldState | lista JSON exacta |
| D02-03 | Nacimiento Belara al oeste norte Valkram | `source` AUTHORED |
| D02-04 | Belara junto Treihord sin atravesarla | `crossesCity=false`, adyacencia y orden respecto bifurcación UNKNOWN |
| D02-05 | Treihord solo barcazas poco calado | `industrial_shallow_draft_only` |
| D02-06 | Belara termina en Golfo Norgard | boca y recorrido grafo |
| D02-07 | Lhera bifurca de Belara, conserva identidad y va a Golfo Veldora | `branchesFrom` y conectividad |
| D02-08 | Agujas contiguo al Lhera y sin poblados | adyacencia y protección |
| D02-09 | Veldora totalmente independiente | red separada, sin aristas entre sistemas |
| D02-10 | Veldora y Lhera solo comparten golfo | no unir por receptor |
| D02-11 | Thalen único y dos brazos terminales | diez aristas, dos salidas del fork |
| D02-12 | Taramin entre brazos, sin inventar geometría ni puente | `cityBetweenTerminalArms` |
| D02-13 | 4 ciudades manuales, Karsath excluida, Syvaris Darovan, Arven UNKNOWN | `cityProtection` |
| D02-14 | No registrar «Eshneva» como río | solo cuatro entidades |
| D02-15 | Sin afluentes ni nacimientos Veldora/Thalen inventados | arrays vacíos y campos null |
| D02-16 | Cuencas y divisorias sin polígonos falsos | `catchmentPolygon=null`, `basinDivides=null` |
| D02-17 | Escorrentía, manantiales y permanencia bajo Core, D03 y campo de relieve | documentos y bloqueo de materialización |
| D02-18 | Taramin semiárida con cauces estacionales como **tipo** (no instancia) | catálogo de categoría vacío de instancias |
| D02-19 | Sin posiciones, aforos, tiempos, pendientes ni geometría runtime | indicadores falsos, nodos vacíos |
| D02-20 | Nodos/aristas únicos, DAG y redes receptoras correctas | recorridos y conjunto de aristas |
| D02-21 | Fuentes originales existentes | `sourcePaths` comprobadas contra repo |
| D02-22 | 8 fixtures de regresión rechazadas | `validate_d02.py` |
| D02-23 | Aislamiento de archivos Darovan | diff GitHub contra main |
| D02-24 | Traspaso D03 sin iniciar D03 | registro y acta |
| D02-25 | No afirmar juego, motor o persistencia real | `runtimeIntegration` no implementada |

## Ejecución de comprobaciones reproducible
Desde raíz Git: `python "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Validacion/validate_d02.py"`.
El script comprueba fuentes, invariantes estrictas de grafo, ausencia de geometría y 8 modificaciones negativas que deben ser rechazadas; no depende de librerías adicionales.

**Límites:** un DAG documental no prueba pendiente real, volúmenes de agua ni funcionamiento del juego. Falta DEM/campo físico, clima D03, cartografía aprobada, integración D11 y prueba efectiva del motor. La validación de GitHub/JSON realizada en D02 se detalla separadamente en el acta.

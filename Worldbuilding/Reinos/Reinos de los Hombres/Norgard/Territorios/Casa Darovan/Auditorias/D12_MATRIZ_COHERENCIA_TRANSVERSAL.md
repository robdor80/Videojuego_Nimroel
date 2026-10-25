# D12 — Matriz de coherencia transversal y pruebas cruzadas
**Alcance:** D00–D11, invariantes contrastables. Los datos no generan hechos canónicos nuevos.

| ID | Cruce | Contrato verificable | Evidencia | Prueba D12 |
|---|---|---|---|---|
| C01 | D00/D01/D02/D06/D07/D08/D09/D10/D11 | Cuatro ciudades manuales, Karsath excluida | Anchors JSON + `manualCityIds` + proyección | Igualdad de IDs, orden y exclusiones |
| C02 | D00/D01/D02/D03/D07/D10 | Belara adyacente, no cruza Treihord | Treihord original, JSON D00–D10 | Booleanos y contradicción negativa |
| C03 | D02/D03/D06/D07/D11 | Cinco ríos, cuatro sistemas | D02 ríos/sistemas + proyección | Coincidencia exacta |
| C04 | D02/D05 | Grafo fluvial topológico NO red de transporte | D02 15 nodos/11 aristas, D05 | Existencia extremos; tipo no cartográfico |
| C05 | D01/D03/D04/D06 | Doce unidades cualitativas | JSON D01–D06 | 12 IDs alineados y únicos |
| C06 | D04/D05/D07/D09/D11 | 3 enlaces físicos documentados | D05 y D11 | Enlaces idénticos, nodos existentes, sin geometría |
| C07 | D04/D05/D11 | 4 relaciones de suministro NO rutas | D05 y D11 | Tipos disjuntos, flag false, distancias null |
| C08 | D04/D08 | Profesiones/ciudades dependen de cadenas D04 reales | Resource chains / occupationFamilies | Claves de cadena existentes |
| C09 | D06/D07 | 9 modelos no crean ciudades manuales ni aldeas reales | generator y city index | 9 modelos, sin WorldState |
| C10 | D07/D08 | Aprobaciones Veldora B / Taramin A / Syvaris A SOLO conceptuales | Actas D07 | Sin creación de rutas/edificios/población |
| C11 | D00/D07/D08/D10 | Treihord conserva ocho barrios y unos 32.000 habitantes | Treihord original, D00 y D10 | Cantidad y guardrail |
| C12 | D08/D11 | Rangos Veldora 29–35k, Taramin 14–20k, ciudad Syvaris 7–10k, total 300–450k | Actas D08, `territoryPopulation` | Valores, sin `populationApprox` inventado |
| C13 | D08 | Medias urbanas 3–5, rurales 4–6; edades 30/60/10; urbano 35–45 %, rural 55–65 % | Lote autoral D08 | Intervalos; suma edades 100; sin censo |
| C14 | D09/D10 | Corona suprema, ley única, Armada de Norgard | Grandes Casas, D09, D10 | Seguridad, legislación, banderas |
| C15 | D10/D11 | Arven es Darovan, identidad cultural UNKNOWN | Decisión 21/10, D10, proyección | Null / UNKNOWN; negativo adversarial |
| C16 | D07/D10 | Origen/oficio no determinan personalidad NPC | D10 guardrails | Rechazo de determinismos |
| C17 | D00–D10/D11 | Once locks SHA; definiciones apuntan a fuente y pointer válido | projection + fuente original | Punteros, rutas, hashes validados por D11 |
| C18 | D11/NIM-06 | Catálogo/puente genérico no equivale a simulación territorial | Matriz D11, capabilities false | Rechazo de flag de ejecución inventado |

## Cuestiones que la matriz NO resuelve
- Un recurso regional (Elyra) no acredita explotación individual.
- El mineral de Valkram y el carbón de Azurios poseen cadena de abastecimiento, no un camino cartografiado nuevo.
- Los 3 enlaces D05 no incorporan geometría, distancia, horario, capacidad ni accesos desconocidos.
- Los cuatro rangos demográficos y porcentajes no producen instancias de habitantes, hogares, inventarios ni empleo.
- Los perfiles culturales son tendencias/contextos, NO reglas duras de conducta individual.
- Fhalion es río independiente pero carece de nacimiento, aforo, desembocadura exacta y navegabilidad determinados.

## Método
Validador Python D12 lee todos los archivos Markdown y JSON de la carpeta territorial, verifica referencias a fuentes de rutas absolutas de proyecto, valida semántica entre fases e introduce mutaciones negativas en memoria. Las pruebas D01–D11 siguen siendo obligatorias, junto con el laboratorio C++ de catálogo D11. Los logs del workflow de la PR son la prueba del resultado real; este documento no sustituye el CI.

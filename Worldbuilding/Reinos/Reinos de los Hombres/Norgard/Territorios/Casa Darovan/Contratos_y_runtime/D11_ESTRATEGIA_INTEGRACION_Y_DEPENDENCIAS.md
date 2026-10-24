# D11-B/C/D — Estrategia de integración y límites verificables

## Cadena de autoridad

Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State. Es precedencia documental/de reglas; no son cinco capas que CoreRPG ContentCatalog 0.1.0 sepa fusionar. Ningún pack físico Core/Norgard inexistente se inventa ni se declara dependency.

## Formatos publicados

1. ContentPacks/darovan-territory/pack/manifest.json + resources: pack nimroel.darovan.territory 0.1.0, cinco ResourceDefinitions (territorio + 4 ciudades). Catálogo Core recibe solo identidades y referencias; no interpreta ciudad, gobernanza ni canon.
2. authoring/projection-v0.1.json: sidecar específico Nimroel, versionado, con 11 fuentes D00–D10 bloqueadas mediante git blob SHA, definición→fase/puntero, 5 ríos, cuatro cuencas cualitativas, 3 conexiones D05, 4 suministros que NO son conexiones físicas, y límites de ejecución. Es dato de AUTORÍA, no input del decoder Core.
3. fixtures/d11-scenarios-v0.1.json: T01–T08 TEST_ONLY y SPECIFICATION_NOT_EXECUTED. No son hechos, partidas, instancias, recetas de acciones ni narraciones históricas.
4. schemas/projection.schema.json + Tools/DarovanD11/validate.py: verifican integridad documental, cambios no autorizados, estados UNKNOWN, referencias y mutaciones adversariales. Los esquemas oficiales de Core se comprueban mediante checkout fijo separado.
5. Tools/DarovanD11/cpp_smoke.cpp: carga real del catálogo CoreRPG y prueba sintética aislada de EntityId/binding/save/load. La semántica local no se ejecuta.

## Política de migración y consistencia

IDs de definición propios e inmutables, nunca derivados del nombre mostrado ni de la posición del archivo. No se reutilizan como EntityId. Una publicación incompatible requiere nueva versión y preflight de hashes/contexto por Host antes de reanudar guardados (precedente CoreRPG 4.13). El catálogo contiene sobres de identidad, no transporta procedencia ni payload. Las referencias se resuelven por DefinitionId/expected_kind, no por rutas físicas.

No hay simulador temporal ni causalidad ejecutable T01–T08: toda prueba estática que afirme existencias o distancias debe fallar. Un fixture C++ puede demostrar que el Core conserva un binding y lo restaura con el catálogo explícito, no que exista Treihord instanciada en el mundo canónico. Nunca se materializan los rangos de población D08 como registros de WorldState.

## Casos previstos y dependencias

| Prueba | Origen | Resultado verificable ahora | Pendiente real |
|---|---|---|---|
| T01 Mineral/Crisol | D04/D05/D09 | Restricciones y procedencia sintéticas | Transformación, propiedad, stock |
| T02 Carbón | D04/D05 | Suministro Azurios registrado como relación NO ruta | Stock, tiempos y escasez |
| T03 Belara | D02/D05 | Barcaza somera en enlace documentado, sin capacidad medida | Transporte causal |
| T04 Veldora | D04/D09 | Aduana exterior sí, interior no | Libro mayor, autoridad y transacciones |
| T05 Taramin | D04/D08 | Perfil de pesca sin barcos/especies inventados | Captura, aprovisionamiento, trabajos |
| T06 Syvaris | D05/D07 | Solo conexiones físicas acreditadas | Mensajería, rutas y navegación |
| T07 Hogares | D08 | Invariantes de identidad, relación y residencia declarados | Hogar, mudanza, propiedad y trabajo |
| T08 Cultura | D10 | Arven UNKNOWN y 17 decisiones autorales comprobables | Personalidad/aprendizaje real |

## Requisiciones técnicas futuras (sin alterar CoreRPG)

- CORE-REQ-D11-01 P1: inventario/stock, procedencia, custodia/propiedad y transformaciones atómicas con rechazos por insuficiencia; pruebas doble gasto, consumo, save/load y misma seed.
- CORE-REQ-D11-02 P1: residencia, empleo, hogares y preservación de identidad/relaciones bajo traslado; pruebas de no confundir parentesco con convivencia y de snapshot.
- CORE-REQ-D11-03 P1: movilidad, disponibilidad de enlaces, rutas autorizadas y suministros separados; pruebas rutas inexistentes, coste UNKNOWN y orden determinista.
- CORE-REQ-D11-04 P2: autoridad, competencias de Corona/Casa, permisos para actores, fiscalidad y libro mayor; pruebas de rechazo de impuestos interiores y suplantación de autoridad.
- CORE-REQ-D11-05 P2: reloj/calendario/eventos y mensajes persistentes; simulación explícita, seeds por streams y reanudación segura.
- CORE-REQ-D11-06 P2: hechos sociales y personalidad autónoma con visibilidad limitada; tests antiesencialismo (ocupación/origen no determinan personalidad).
- NIM-HOST-D11-01 P1: preflight de edición/huellas, sidecar Nimroel validado, adaptador al Core y GDExtension tras cerrar NIM-06; pruebas físicas MSI y Tab S9+ separadas.
- AUTOR-D11-01 bloqueos: ubicaciones de minas, rutas, capacidades, cantidades y cultura Arven no se resuelven de oficio.

**Prioridad:** necesidades de juego reales y diseño CoreRPG independiente. Ninguna propuesta anterior cambia APIs públicas ni autoriza crear sistemas paralelos.

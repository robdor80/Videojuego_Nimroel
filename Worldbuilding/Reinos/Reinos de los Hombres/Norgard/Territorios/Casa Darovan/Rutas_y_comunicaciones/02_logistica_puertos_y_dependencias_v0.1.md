# DAROVAN D05 — Logística, puertos y dependencias v0.1
**NO RUNTIME / NO itinerarios nuevos.** Separación obligatoria: conexión física acreditada ≠ vínculo de abastecimiento ≠ función de puerto.

## Cadenas compatibles con D04
| Cadena | Nivel de evidencia | Medio o ruta |
|---|---|---|
| Minas Valkram → carros → carga fluvial → barcazas Belara → puerto industrial de Treihord | AUTHORED como cadena funcional | Carros y barcazas someras acreditados; carreteras, puntos exactos, puentes, viaje y capacidad UNKNOWN |
| Puerto Treihord → patios, almacenes, mineral/carbón y fundición | AUTHORED como organización industrial | Manipulación interna; no trazar calles ni convertir cada patio en almacén nuevo |
| Carbón Montes Azurios → reservas de Treihord | AUTHORED como dependencia de suministro | Medio, ruta, intervinientes, origen minero concreto y escala UNKNOWN. Prohibido atribuir transporte por Belara sin fuente |
| Madera Bosque de los Pilares → minas Valkram | AUTHORED como uso económico regional | Medio y camino UNKNOWN; Pilares sigue siendo bosque único, sin nueva explotación localizada |
| Huertas y suministro exterior hacia Treihord | AUTHORED en escala general | Proveedores, pueblos de paso y medios UNKNOWN; no dibujar una ruta de alimentos |

La matriz JSON coloca cuatro relaciones de suministro en `supplyRelationsNotRoutes` y las tres conexiones físicas acreditadas aparte; por contrato, ninguna relación de suministro puede ser utilizada automáticamente como camino de CoreRPG. Los pasos de carros a carga fluvial existen como **etapas**; no se localiza ninguna infraestructura concreta ni se prueba un camino cartografiado.

## Puertos
- **Treihord**: puerto fluvial industrial, no gran puerto mercantil; barcazas de poco calado; almacenes/patios y fundiciones atestiguados.
- **Veldora**: puerto comercial importante, almacenes y servicios; fiscalidad exterior solo si concurre frontera fiscal pertinente. Ningún arancel Darovan–otra Gran Casa por mero cruce.
- **Taramin**: función pesquera marina y fluvial; no convertir brazos finales Thalen en canal navegable demostrado. Caladeros, cuotas, capturas y muelles nuevos UNKNOWN.
- **Syvaris**: isla Darovan con puerto seguro en bahía principal, pesca/comercio y calas menores; no bautizar calas ni inventar enlaces de cabotaje, tonelajes o calendario.

## Reutilización de sistemas
`nimroel_vessel_navigation_simulation_contract_v0.1.json` exige identidad, carga, tripulación, conexión navegable, calado, agua y meteorología; Norgard E7 aporta arquetipos funcionales (barcaza, mercante costero, pesquero…), **no** inventarios de naves existentes ni clases propias. Nimroel Core TXN/OBL/LED gobierna transmisión real de bienes y valores; representar una flecha logística no genera mercancía ni pago. Aduanas Norgard E8: sin aduanas internas entre Grandes Casas. El Crisol NO acuña moneda; la Vena es enlace privado protegido.

## Rutas sujetas a verificación posterior
No se conocen kilómetros, coste, tiempos, capacidades de carga, puntos de embarque, sentidos de corriente aplicables ni profundidad a lo largo del año. Una necesidad económica de intercambiar bienes NO acredita vía navegable ni servicio existente. D11 podrá materializar transporte sólo tras aprobar cartografía, stocks, medios y contratos del motor.

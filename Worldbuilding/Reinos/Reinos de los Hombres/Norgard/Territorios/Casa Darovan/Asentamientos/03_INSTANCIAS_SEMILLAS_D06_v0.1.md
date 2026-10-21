# D06 — Identidad, semillas, muestras y diseño de persistencia v0.1

**Laboratorio de diseño, no generador jugable.** `Validacion/d06_generator.py` es una función pura usada por el validador estático; NO contiene acciones CoreRPG, edición de escenas Godot, GIS ni guardado.

## Identificador estable antes de elegir modelo

Para cada muestra: `sha256(JSON_UTF8(["darovan-d06/v0.1", worldSeed, studyZoneId, slotId]))` y prefijo hexadecimal de 16 caracteres bajo `d06_test_`. Los cuatro componentes usan serialización JSON de arrays con `ensure_ascii=False` y separadores `,:`. `slotId` es una clave de prueba sintética y no una posición ni topónimo. Nombre visible, oficio y variante de edificio **no intervienen** en la identidad.

Semilla de elección del modelo: `sha256(JSON_UTF8([worldSeed, stableId, "model", rulesVersion]))`, primeros 8 bytes sin signo, módulo suma de pesos de modelos elegibles **ordenados por ID**. Insertar después otra opción no desplaza secuencias RNG globales. En estas pruebas se permite `allowedModel` explícito para demostrar aisladamente restricciones de modelos, nunca como override de mundo.

Los futuros subsistemas independientes podrán derivar claves diferenciadas `model`, `services/<id>`, `households`, `buildings`, `layout`, pero **D06 no implementa ninguno salvo selección de modelo en laboratorio**.

## Fixture sintético obligatorio

`Datos operativos/darovan_d06_test_fixtures_v0.1.json` contiene seis situaciones ***inventadas para probar validadores***: Pilares, Arven, Linde, Valkram, Syvaris y bosque de Taramin. Los booleanos expresados como `*_verified` significan *supuestos de laboratorio*, **no verificaciones cartográficas reales**. No son aldeas ni puertos nuevos; los IDs `sandbox_*` no aparecen en canon. No representan eventos históricos.

Cada salida tiene `provenance=TEST_ONLY`, `canonical=false`, `materialized=false`, `visibleName=null`, `coordinates=null`, `population=null`, `connectedRoutes=[]`, `serviceInstances=[]`, `buildingInstances=[]`, `worldStateId=null`. Las listas `potentialBuildings` y `potentialServices` son catálogos de diseño, **no objetos activos**.

El validador prueba igualdad bit a bit con igual semilla, cambio de ID con semilla distinta, selección de pesos independiente del orden, rechazo por agua o acceso faltante, autoría urbana, Agujas, rutas, puertos, caudal, aduanas, derechos, nombres y coordenadas.

## Persistencia futura (D11)

Un registro jugable futuro deberá conservar `stableId`, `worldSeed` o referencia segura, `rulesVersion`, `generatorVersion`, procedencia, ancla de emplazamiento real aprobada, revisión cartográfica, fuentes, modelo, decisiones materializadas e identificadores CoreRPG. La carga existente **no se regenera por cambiar el JSON**: conservar estado anterior, migrar explícitamente o aplicar reglas nuevas solo a partidas nuevas. El cambio de nombre visible no cambia ID.

CoreRPG mantiene residencia, población, necesidades, relaciones, propiedad, empleo, bienes, memoria y persistencia real; Godot solo representará el resultado autorizado. Estado dinámico (inundaciones, suministro, condiciones de camino) no debe volver a lanzar la creación permanente. La cobertura de servicios sobre grafos de viaje está **bloqueada** hasta D11, porque D05 no es red de itinerarios.

## Puertas que faltan

- D07: trabajo manual de las cuatro ciudades, puertos y anclas cartográficas sin pasar por el generador.
- D08: rangos propios de Darovan, comunidad residente, hogares, profesiones y necesidades.
- D11: emplazamientos cartográficos, accesibilidad real, contratos, simulación en CoreRPG, UI Godot y pruebas de guardado/carga y ARM64/Windows.

No activar asentamientos reales ni sustituir restricciones UNKNOWN sin decisión del autor.

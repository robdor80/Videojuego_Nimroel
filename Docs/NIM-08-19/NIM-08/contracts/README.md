# Contratos JSON de NIM-08 (borradores de arquitectura)

Estos archivos son artefactos de diseño 0.1.0, NO son Content Pack CoreRPG 0.1.0, NO son API C++ implantada, NO son snapshot ni salvaguarda de I4 y NO declaran la aldea creada. Los schemas se validarán en NIM-09 antes de generar material operativo. Nunca usar el schema remoto para conectar por red; todos los archivos están incluidos localmente.

- generation-manifest-0.1.0.schema.json: source-lock heredado, pack, Core/Godot, contexto y streams técnicos.
- world-instance-0.1.0.schema.json: estructura candidata con referencias cruzadas, personas materializadas y campos de dominio que HOY faltan en CoreRPG.
- action-envelope-0.1.0.schema.json: frontera propuesta petición/resultado. Los intents no existen automáticamente en CoreRPG; actor_id no otorga derechos.
- technical-manifest-example.json: solo ejemplo para tests estáticos. La seed 413001 y los identificadores corresponden al fixture I4; el descriptor de RNG propuesto NO implica que ese bootstrap ya use los nuevos streams.

**Reglas extra-schema para ejecución futura:** referencias internas existentes y sin duplicados; contención sin ciclos; aristas conectadas; population_total = materialized_count + latent_count; size(people) = materialized_count; un solo objeto por ID/EntityId; household members resolubles; propietario distinto del poseedor permitido pero custodia exige autorización; clock y cola sólo cambian por Core; bloqueo ante pin/save incompatible. La semántica cross-field requiere runtime propio y pruebas nativas, no se da por ejecutada con validación de JSON.

# NIM-07 — Auditoría independiente y aceptación técnica de I2

**Fecha:** 27/10/2026. **Rama:** `feat/nim-07-first-rpg-experience`; HEAD de la entrega auditada `03912e1dab11d9de35291f83be7c78c977e03733`. SHA de código ejecutado en CI `b8987b7cd70d92e069e3540b2ec8078ce6554bcd`.

## Dictamen

**I2 aceptado técnicamente, con límites expresos.** Puede comenzar I3 en la misma rama. Ni I2 ni la fase NIM-07 se han fusionado, ni se declara gameplay de aldea plenamente funcional. Esta revisión contrasta directamente el código, el upstream CoreRPG y metadatos de los jobs; no es una nueva ejecución local o física independiente.

## Verificaciones independientes

1. **Cambios delimitados:** comparación del commit anterior `187ab4a6ed03e45b247c9c03eed1c91a1c55801e` con HEAD I2: tres commits, 23 rutas modificadas/añadidas; ningún cambio en `ContentPacks/**`, `Worldbuilding/**`, archivos de política IA o repositorio CoreRPG. No aparece PR de la rama.
2. **Catálogo real:** `Game/BridgeCoreRPG/native/src/v001.hpp` usa `core::content_json` para decodificar JSON y manifiesto, `ContentCatalog::create`, `WorldState::bind_definition` cuatro veces, contención, relaciones, población y conocimiento con Core. `Campaign` mantiene `shared_ptr<const ContentCatalog>`; preparación candidata, validación con Inspector y Persistence, publicación final mediante `Runtime::replace`. `bridge.cpp` implementa `initialize_v001` privilegiado y paso de catálogo a `restore`.
3. **Concordancia upstream:** contrastado contra `robdor80/CoreRPG` SHA `4f282863737bcd8f5add401202a9e1064c133672`, `tests/nimroel_content_pack_test.cpp`, secciones `Fixture` y `remember`: siete identidades, semilla 413001, cuatro vínculos, tres contenciones, tres relaciones de servicios/conexión, asociación poblacional de los dos observadores, 50 total y 2 materializados, conocimiento parcial diferenciado. Ninguna ciudad, inmueble, NPC canónico, profesión o misión añadida.
4. **Autenticidad de publicación:** `Tools/NIM07/stage_pack.py` usa el validador existente, compara hash fijado del lock y distribuye únicamente nueve JSON generados/ignorados. `v001_pack.gd` lee desde `res://` con FileAccess y límites. `v001.hpp` exige inventario exacto, SHA-256 del lock fijado y hashes individuales antes de decodificar recursos, contrato y catálogo. Pines: release `45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`, definiciones `6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5`, lock `669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370`.
5. **Audiencia:** el modo V001 crea una sesión sin permiso de acciones; las preguntas de la IU recorren `CoreRPGSession.context`. `native_conversation.gd` traduce IDs del pack solo para hechos de definición emitidos por Core y de existencia conocida. Las comprobaciones negativas verifican que no aparecen identidades 3,4,7 o metadatos privilegiados para el primer observador. `¿qué veo?` mantiene limitación espacial honesta.
6. **NIM-06/I1 conservados:** instancia neutra I1 independiente, ruta antigua sin sesión bloqueada y diagnóstico separado. Las regresiones figuran en los jobs finales y evidence.
7. **CI final:** `https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709` sobre código `b8987b7c`: jobs `122022957475` Windows y `122022957672` Android/control Linux, ambos SUCCESS, verificados por API de GitHub. La evidencia documenta I2 **37/37**, I1 **48/48**, NIM06 **129/129**, regresiones Host previas; EXE Windows exportado ejecuta I2 **37/37**. Windows PCK y APK ARM64 empaquetan los nueve archivos; la .so Android verifica ELF AArch64, coincidencia de bytes y exportación. La ejecución en Linux de assets Android **no constituye runtime Android**.
8. **Fallo previo resuelto:** run `40453124859` en `ba5b0531` terminó Windows FAIL al invocar pruebas I2 por `--script` en plantilla exportada. Commit `b8987b7c` reutilizó un solo cuerpo de pruebas mediante `--nim07-i2-self-test` y CI posterior verde. El arreglo no alteró el C++ ni el pack.

## Reservas de alcance

- **Pruebas físicas nuevas pendientes** en MSI Windows 11 y Samsung Galaxy Tab S9+; aceptación física de NIM06 no sustituye NIM07.
- **Solo fixture estructural:** sin percepción física/espacial, actividades RPG semánticas, NPC, recorrido, diálogo, generación de aldea ni misión jugable. No debe declararse una primera experiencia RPG completa.
- **Guardado V001 en disco NO disponible**: los métodos de save/load del controlador rechazan con `CONTENT_PERSISTENCE_PENDING_I4`; restore con catálogo solo está probado en memoria. I4 deberá verificar publicación y contexto inicial externos, consistencia atómica y reapertura.
- **División Git:** al auditar, `main` está en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9`; la comparación `main...feat/nim-07-first-rpg-experience` informa rama por delante 12 commits y por detrás 36. No es fallo I2, pero **antes de la PR final de I4 habrá que reconciliar los cambios recientes de main y ejecutar regresiones tras esa integración**. No rebasar o fusionar ramas automáticamente durante I3.
- No se ha ejecutado una prueba independiente fuera de las evidencias CI revisadas. Los 37/48/129 resultados proceden de tests de Codex ejecutados en GitHub y evidenciados, no de un test nuevo por el auditor.

## Siguiente decisión

**Autorizar planificación e implementación de I3**, con alcance ya previsto en la hoja de ruta: consultas deterministas y presentación más útil en la pantalla principal, exclusivamente desde hechos visibles por la sesión. No duplicar I2 ni activar acciones RPG sin contrato semántico. No abrir ni fusionar PR; no activar IA de pago.

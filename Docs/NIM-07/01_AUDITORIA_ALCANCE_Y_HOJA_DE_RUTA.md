# NIM-07 BUILD — Auditoría real, alcance definitivo y hoja de ruta

Fecha: 24/10/2026. Base de lectura: `main` en `1865fb7fedb616ef7abdffbb195d3698825d4c8a`.
Rama de trabajo: `feat/nim-07-first-rpg-experience`.
Estado: **planificación y auditoría; no equivale a implementación ni a pruebas físicas de NIM-07**.

## 1. Estado verificado

- PR #27 NIM-06 fusionada el 24/10/2026, merge SHA indicado arriba. En `main`, Actions NIM-06 (`40099719022`) y regresiones NIM-01–05 (`40099719008`) terminan en **success**.
- El propietario comunica 129/129 comprobaciones físicas superadas tanto en MSI Windows 11 como en Tab S9+ Android ARM64, incluidas persistencia/reapertura y aceptación de scroll y adaptación. No repetir esta fase ni atribuir ese resultado a NIM-07.
- `Game/Host2D/scripts/main.gd`: conversación 2D, entrada, bocadillos, historial, teclado Android, arte provisional. `_on_send` sigue llamando al pipeline demo/bloqueado, no abre sesión nativa de jugador.
- `interaction_pipeline.gd`: `MODE_DEMO` simula; `MODE_INTEGRATION` permanece bloqueado, `integration_ready=false`. No suprimir la protección de las pruebas históricas para fingir integración.
- `core_port.gd`: sabe llamar a `CoreRPGSession.submit` con capacidad explícita y rechaza flujos antiguos sin sesión.
- `native_world_controller.gd` + `native_vertical.gd`: vertical **real pero exclusivamente técnica** con cuatro entidades neutras, contexto filtrado, contención propia y persistencia. No es Treskal.
- `Game/BridgeCoreRPG/native/src/bridge.cpp` registra `CoreRPGHost` (initialize/admin/step/open_session/capture/restore) y `CoreRPGSession` (context/submit/availability/close). Solo la sesión `player` puede colocar o retirar **su propia** contención hacia destinos explícitamente autorizados. No se expone el estado privilegiado a la IU ni a IA.
- `core_save_store.gd` tiene guardado `user://core_saves` con temporal/copia de seguridad; las versiones históricas del Core siguen siendo autoridad.

## 2. Treskal: alcance genuino

- `ContentPacks/treskal-villages`: pack `nimroel.treskal.villages` v0.1.0 / Content Contract 0.1.0; modelo V1 agrícola-maderero y fixture `v001-structural-1` de seed `413001`. Esta publicación **no acredita** plano, edificios, profesiones, NPC nominales, desplazamientos, horarios, misión ni generación completa.
- Cuatro recursos: modelo de aldea, capacidad de herrería básica, capacidad de taberna local y categoría de herramienta agrícola. El fixture declara población 50, 2 identidades materializadas y 48 latentes; conexión externa abstracta.
- `CoreRPG/tests/nimroel_content_pack_test.cpp` demuestra un **fixture de siete identidades**: aldea, nodo de herrería, nodo de taberna, frontera exterior, herramienta y dos observadores anónimos. Vincula definiciones auténticas al catálogo, establece contenciones y relaciones y prueba persistencia; **no prueba gameplay**.
- **Brecha determinante:** la GDExtension NIM-06 actual no expone carga de `ContentCatalog`/ContentJson ni `bind_definition`; `restore` no usa el catálogo de la publicación. Por tanto, clonar los siete IDs en GDScript sin vincular definiciones **NO constituye la integración completa del pack 4.13**. Nunca llamar "aldea V1 cargada" a ese sucedáneo.
- Un actor técnico del fixture no es automáticamente un NPC canónico ni un personaje personalizado. Si se usa uno de los observadores anónimos para la experiencia de pruebas, identificarlo exclusivamente como `personaje de prueba`; no crear nombres/relaciones/hogares/profesiones.

## 3. Política narrativa vigente

Fuente de prioridad: `Docs/IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md` (revisión 20/10/2026).
- Sol `gpt-6.1-sol`: Máster principal, escenas y sucesos relevantes **autorizados**.
- Luna `gpt-6-luna`: diálogos NPC y consulta puntual fuera de personaje.
- ChatGPT Plus: preparación externa y manual de paquetes, sin invocación automática por Godot.
- Gemini y brokers antiguos son diagnósticos históricos, **no** la ruta narrativa aprobada.
- NIM-07 usa interpretación y presentación **deterministas etiquetadas**. No llamar API, no activar pagos, no claves/tokens en clientes ni falsificar mensajes como Luna o Sol.

## 4. Alcance definitivo y entregas

### I1 — Entrada de jugador real desde pantalla principal (primer encargo Codex)
Conectar una opción de experiencia nativa/experimental, claramente distinta de `demo`, con **una instancia persistente por partida** de `CoreRPGHost` y `CoreRPGSession`, reutilizando los puertos y controlador existentes. Comprobar consulta real de contexto y respuesta textual filtrada. En I1 **seguir usando mundo neutral de laboratorio**, etiquetándolo como tal; ninguna escena se hace pasar por Treskal. Sin cambios C++, sin API externa. Regresiones existentes intactas. Este checkpoint no cierra NIM-07.

### I2 — Fixture 4.13 fiel, mínimo y versionado
Tras revisar I1, preparar puente *puntual* de datos de contenido en el adaptador GDExtension **sin cambiar CoreRPG**: cargar bytes verificables desde recursos empaquetados en Windows/Android, validar manifiesto/definiciones/huellas contra publicación confiable, construir `ContentCatalog`, vincular realmente las cuatro definiciones del fixture (incluido uso de catálogo en restauración). Reutilizar el orden y las semánticas probadas en `tests/nimroel_content_pack_test.cpp`; no renombrar nodos de servicio como edificios físicos. Cualquier necesidad de **nueva API de CoreRPG** se documentará como dependencia separada antes de tocar el repositorio Core. Evitar duplicar recursos como segunda fuente de autoridad; empaquetado reproducible desde `ContentPacks/treskal-villages/pack`. Si no es viable en incremento pequeño, comunicar bloqueo real, sin sustituirlo silenciosamente por IDs ficticios.

### I3 — Consultas de jugador y respuesta explicable
Interpretación **cerrada, offline y explícita** para un puñado de peticiones (estado inicial; `¿qué sabe mi personaje?`, `¿qué conozco de este lugar?` y equivalentes estrechos). Generar únicamente hechos de `session.context`, con distinción de hecho conocido/ausencia/desconocido y estado de truncamiento; traducir IDs a etiquetas SOLO si el mismo observador conoce el hecho correspondiente y la etiqueta deriva del pack verificado. `¿Qué veo?` debe expresar honradamente que todavía no existe percepción visual/espacial, sin atribuir visibilidad física o presencia de NPC; puede ofrecer el conocimiento estructural disponible. No simular que un comando de contención es viajar, entrar en un edificio, tomar la herramienta o hablar con aldeanos. Si no existe una acción de juego semánticamente fiel, limitar acciones visibles y registrar dependencia para fase posterior; sí demostrar integridad de las acciones estructurales reales ya disponibles sin etiquetarlas como movimiento.

### I4 — Continuidad y cierre
Reutilizar `CoreSaveStore`, reabrir con nuevas capacidades de sesión tras restore, comprobar el mismo hecho antes/después y el rechazo sin mutación. El guardado dependiente de contenido requiere **metadatos externos** (pack ID/version, huellas de publicación y de contexto inicial) que se verifican **antes** de restaurar bytes Core. No regenerar al reabrir ni aceptar packs distintos sin migración; la identidad de guardado no debe perderse en caso de escritura parcial. Reutilizar el patrón `examples/external_content_restore.hpp` de CoreRPG. Tests concisos del flujo real en Windows y build/export Android; entrega PR Draft sin fusión. Pruebas físicas finales solo cuando exista APK/EXE concreto.

## 5. Invariantes y exclusiones

- CoreRPG conserva la única autoridad de estado/identidad/conocimiento/acciones/revisión/RNG.
- Estado GDScript permitido: handles de Host/sesión, IDs de solicitud, estado UI, etiquetas del pack ya autorizado y metadatos de guardado; **prohibido** replicar WorldState.
- Las sesiones no aceptan actor, observador, permisos, precondiciones o revisiones arbitrarios del jugador; usar contratos cerrados, caducidad y rechazo de replay.
- No tocar `main`, CoreRPG, branches ajenas, canon, NIM-05/06 históricos ni integrar por obligación voz o proveedores. No asumir que Actions prueba runtime Android.
- Escenario V1 **estructural**, no aldea procedural final. Sin misión `La herramienta rota`, NPC inventados, clic obligatorio, mapa 3D, combate ni decenas de fixtures.
- Preservar pruebas NIM01–06, especialmente `CORE_NOT_CONNECTED` en rutas antiguas sin sesión, y separación de diagnósticos Gemini/IA/voz.
- No se activa ningún servicio externo facturable ni se suben credenciales. No comprometer seguridad por una demo vistosa.

## 6. Criterio de aceptación NIM-07

En la pantalla **principal**, crear/reabrir una sesión del fixture autorizado V001 de Treskal, escribir una consulta compatible, ver datos filtrados y entendibles derivados de CoreRPG, sin revelar entidades ocultas ni inventar entorno. Si hay acción soportada y semántica aprobada, recibir un resultado comprobable y persistirlo. Conservar estado entre reinicios. CI Windows + export Android y comprobación física final en ambos dispositivos con evidencia separada. Preparar PR Draft para revisión y fusión **solo por el propietario**.

No declarar terminada la fase mientras solo esté I1 ni mientras el contenido V001 se haya copiado sin vincular definiciones.

## 7. Primer paso autorizado

Ejecutar exclusivamente **I1**, conforme a `02_ENCARGO_CODEX_I1.md`, sobre esta rama y auditar el diff/resultados antes de ampliar el puente de contenido. No generar otro laboratorio separado: toda consulta de prueba debe salir de la pantalla principal del jugador.

# NIM-07 / I2 — Encargo Codex: cargar el Content Pack Treskal V001 en CoreRPG real

**Ámbito estricto:** implementar I2, con los hitos A (preflight/lectura) y B (fixture/consulta). **No implementar I3/I4**, no modificar CoreRPG, canon o IA, no fusionar, no abrir PR final.

## Situación y comienzo seguro

Repositorio: `robdor80/Videojuego_Nimroel`. Trabajar en **la rama existente** `feat/nim-07-first-rpg-experience`; comprobar su HEAD antes de editar y conservar I1 íntegro. `main` está fuera del alcance. Leer primero:

1. `Docs/NIM-07/01_AUDITORIA_ALCANCE_Y_HOJA_DE_RUTA.md`, `03_RESULTADO_I1.md`, `04_AUDITORIA_ACEPTACION_I1.md`.
2. `ContentPacks/treskal-villages/README.md`, `pack/{manifest.json,content-lock.json,integration-fixture.json,nimroel/model-v1.json}`, sus cuatro `resources/`, `Tools/CoreRPG413/{pack.py,validate.py}`, schemas específicos del pack, `Docs/CORERPG_4_13_CONTENT_PACK.md`.
3. `Game/BridgeCoreRPG/native/src/bridge.cpp`, `native/CMakeLists.txt`, `cmake/dependencies.cmake` y `native/README.md`.
4. `Game/Host2D/scripts/{main.gd,native_conversation.gd,native_world_controller.gd,core_save_store.gd}`, tests I1/NIM06, export presets, workflow `.github/workflows/nim-06-native-lab.yml`.
5. En el repo público `robdor80/CoreRPG`, SHA **exacto** `4f282863737bcd8f5add401202a9e1064c133672`: `tests/nimroel_content_pack_test.cpp`, `examples/external_content_restore.hpp`, `CMakeLists.txt`, `include/corerpg/{content_catalog.hpp,persistence.hpp,world_state.hpp,content_json/content_document_decoder.hpp}`.

## Resultado esperado

Desde la **pantalla principal** del Host 2D, nueva opción explícita tipo «Iniciar V001 de Treskal (fixture estructural)». El Host valida la publicación instalada, crea **una única instancia real de CoreRPG** con catálogo y definiciones vinculadas, abre una sesión para un observador anónimo del fixture y puede consultar hechos de ese mundo por la ruta de I1. El modo neutro I1 sigue funcionando. Etiquetar siempre V001 como *fixture estructural*, **NO** como generación procedural, aldea plenamente jugable, jugador con identidad canónica, NPC dialogante, taberna/herrería como edificio físico o herramienta reparable.

## Hito A — Empaquetado y lectura verificada, sin autoridad de mundo duplicada

- Única fuente versionada: `ContentPacks/treskal-villages/pack/`; no editar sus bytes ni crear una segunda copia editable. Crear **un staging reproducible pequeño**, por ejemplo `Tools/NIM07/stage_pack.py`, que valide fuente con el validador existente y copie los nueve archivos a una ruta **generada/ignorada por Git** dentro de `Game/Host2D` para que `res://` funcione en editor/export Windows/Android. Limitarse a esos archivos, incluyendo lock y fixture; nunca arrastrar todo Worldbuilding.
- La identidad de publicación confiable está fijada por el proyecto: pack `nimroel.treskal.villages`, versión `0.1.0`, contrato `0.1.0`, `release_sha256=45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`, `definition_set_sha256=6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5`. No aceptar *automáticamente* una sustitución porque ella misma traiga nuevo lock. Verificar SHA-256 **de cada archivo** y release fingerprint, conjunto exacto de recursos, manifiesto, schema y fixture con límites. Detectar tanto modificaciones como ausencias/añadidos. Usar `Tools/CoreRPG413/validate.py` para preflight offline del pack original; en runtime no requerir Python ni red.
- Hacer que el **Host de confianza** lea bytes `FileAccess` desde `res://` y los pase por un contrato nativo acotado; **no** pasar `res://` a C++ `std::filesystem`, ni asumir rutas nativas disponibles dentro de un APK. Evitar descargas y generación a demanda. No introducir claves ni peticiones de red.
- CoreRPG ya incorpora lector/decoder/catálogos, pero el build actual desactiva `CORERPG_BUILD_CONTENT_JSON`. Habilitar **solo donde se necesite** esa librería opcional, compilando/enlazando `CoreRPG::ContentJson` y usando el `jsoncons` fijado por el mismo CoreRPG. Mantener SHA CoreRPG, SHA godot-cpp, C++20, Windows x64/Android ARM64 y funcionalidades NIM-06. Evitar modificar sin necesidad `Game/BridgeCoreRPG/lab` y sus contratos; si hay que ajustar la configuración compartida, conservar OFF en laboratorio legado y ON únicamente en el puente nativo funcional, de forma auditable.
- La lectura/validación falla **cerrada**, con código de error claro y sin inicialización parcial; el modo neutro I1 no se convierte en reemplazo silencioso de Treskal. No imprimir la totalidad de los bytes ni datos privilegiados a la IU.

## Hito B — Fixture idéntico al de CoreRPG 4.13

Reproducir **dentro de CoreRPG nativo**, no en GDScript, las operaciones del fixture probado en `tests/nimroel_content_pack_test.cpp`, usando el `ContentCatalog` real creado desde los recursos decodificados. No inventar datos:

- Semilla **413001** obtenida de `integration-fixture.json`.
- Crear **7 identidades**: aldea V1, nodo de servicio herrería básica, nodo de servicio taberna local, frontera exterior abstracta, objeto de categoría herramienta agrícola ordinaria y **2 observadores anónimos materializados**.
- Vincular mediante `WorldState.bind_definition` las **4 definiciones reales**, no etiquetas GDScript. El nodo de servicio no implica edificio ni profesional, la herramienta no tiene propietario/estado de reparación implementado y la frontera no es una ciudad vecina inventada.
- Aplicar contención y relaciones del fixture: nodos de servicio dentro de aldea, herramienta dentro del nodo herrería, relaciones village–servicios y village–frontera según categorías de relación fijadas; declarar población 50 y materializar 2 (48 latentes); ligar asociación de los observadores con la aldea, **sin colocarles físicamente allí ni crear viviendas**.
- Conceder conocimiento explícito al primer observador según `remember(Fixture &f)` del test Core, sin filtrar datos del segundo observador. Exponerlo solamente mediante la sesión player autorizada, nunca por diagnósticos del Host.
- Preparar de manera **transaccional** un `Campaign` candidato y catálogo; hacer visible la nueva campaña solo si contenido y bootstrap completos pasan validación. Fallo = ninguna campaña parcialmente creada. Conservar el catálogo válido durante toda la vida de esa campaña y asegurar que los vínculos de definición no queden colgantes. Al reinicializar/restaurar, invalidar capacidades antiguas.
- Si se necesita una nueva operación, añadirla **solo al adaptador privilegiado `CoreRPGHost` de Nimroel** (por ejemplo `initialize_v001`, con request/schema cerrados), no a la sesión pública ni al propio repositorio CoreRPG. No reescribir catálogo o simulador en GDScript.
- **Persistencia:** este incremento NO implementa botones de guardado ni el sidecar definitivo. Si se adapta `restore` en C++ para reconocer un catálogo existente y resolver definiciones, conservar la ruta antigua neutral NIM06 y documentar el límite de **I4**: comparar publicación/huella de contexto verificada antes de leer el save, conservar metadata atómica e impedir regenerar el mundo tras cargar. Prohibido declarar la continuidad V001 entre reinicios como completada en I2.

## Presentación en el Host principal

- Reutilizar `native_conversation.gd`, `main.gd` y `CoreRPGSession.context`; preferir un modo/instancia configurada por el Host frente a duplicar las pantallas de conversación.
- Las consultas cerradas I1 (`estado`, `¿qué conozco?`, etc.) deben responder para el fixture **con datos filtrados de Core**. Extender cuidadosamente el formateador para hechos autorizados relevantes: **existencia, definición, relaciones, población y origen**. No atribuir el contenido de campos JSON del pack a entidades si la vinculación Core no existe. Una definición puede identificarse por nombre/capacidad documental cuando el observador conozca efectivamente esa definición; nunca por la mera posesión del catálogo privilegiado.
- Para `¿qué veo?`: sigue sin haber percepción visual/espacial; indicar el límite, sin fingir recorrido, cercanía física, NPC presentes ni plano. No habilitar acciones de contención como equivalentes a movimiento físico, hablar, recoger, entregar, reparar o esperar.
- No habilitar Gemini, Luna `gpt-6-luna`, Sol `gpt-6.1-sol`, costes ni claves en clientes.
- Conservar acceso I1 a estructura neutral, diagnósticos NIM-06 y maqueta antigua de modo inequívoco; no romper teclado Android ni presentación en diferentes resoluciones.

## Validación acotada, con evidencia real

1. Ejecutar validación reproducible del **pack original** y de la copia temporal instalada y comparar bytes/hashes; analizar que el pack empaquetado sea el mismo tras export Windows y Android. Verificar **desde Godot** lectura `res://` real y contenido en PCK/APK, no solo presencia de archivos en el repositorio.
2. Una **única smoke I2** (aproximadamente 20–40 afirmaciones útiles, no pruebas masivas): creación de V001 desde pantalla principal, catálogo real con cuatro definiciones, siete identidades, población 50/48, relaciones de fixture, consulta autorizada por observador, separación de identidad oculta, rechazo de hash/version/archivo alterado y ausencia de creación parcial. En prueba privilegiada se puede inspeccionar el mundo; el jugador solo ve `session.context`. No copiar `WorldState` a GDScript para probarlo.
3. Ejecutar regresiones I1 48/48, NIM06 129/129 y suites Host previas. Usar el **workflow nativo existente**, ampliando triggers de `ContentPacks/treskal-villages/**` y `Tools/NIM07/**` si hace falta. Windows debe cargar realmente la nueva DLL y probar I2; Linux es control de exportación Android. Android: compilar/enlazar ARM64, verificar ABI, PCK/archivos y APK; **no atribuir ejecución física Android a Actions**.
4. No repetir compilaciones completas para cambios exclusivamente documentales; fijar evidence a SHA exacto del código. Evitar 50 ZIP y pruebas de estrés.
5. Registrar tamaño de binarios/dependencias opcionales para detectar un aumento desproporcionado por `jsoncons`; si falla el enlace Android o el lector, intentar una solución mínima segura y anotar la limitación sin inventar resultados. Nunca cambiar Core/godot-cpp a otra revisión sin justificación y autorización.

## Entrega y límites

Publicar código/CI y `Docs/NIM-07/06_RESULTADO_I2.md` con: datos exactos creados, fuente y huellas, arquitectura y vida del catálogo, qué se informa al jugador, tests por entorno y SHAs/URLs de Actions, consumo/artefactos, carencias pendientes I3/I4. Si detectas necesidad real de API adicional en CoreRPG, **detente en esa dependencia concreta y descríbela**; no la implementes silenciosamente.

No abrir PR final, no fusionar ni modificar `main`, no tocar canon, no generar aldeas procedurales, NPC con nombres, edificios específicos ni misión «La herramienta rota».

**Aceptación I2:** la pantalla principal identifica el modo «V001 — fixture estructural», abre una sesión CoreRPG de una campaña con **catálogo válido y cuatro vínculos de definición**, puede responder a una consulta filtrada con hechos genuinos V001, conserva la separación de observadores y niega un pack incorrecto. El guardado entre reinicios y acciones RPG específicas siguen pendientes.

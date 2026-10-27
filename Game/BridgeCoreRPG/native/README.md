# Puente funcional CoreRPG

Fuentes C++20: `src/bridge.cpp`. Configuración y pins compartidos con el laboratorio
en `../cmake/dependencies.cmake`. La producción no depende del adaptador experimental.
Se compila hacia `Game/Host2D/native/bin`, y el controlador instala el descriptor
`host.gdextension.in` en Host2D. Descriptor y binarios generados quedan fuera de Git.
Un checkout sin compilación mantiene el Host 2D operativo y anuncia nativo ausente.

```
python Tools/NIM06/native_lab.py build --functional --target windows
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
python Tools/NIM06/native_lab.py export-windows --functional
```

Android usa los mismos comandos `build --target android`, un control de exportación
`build --target linux`, `smoke` y `export-android`, todos con `--functional`.
Las herramientas exactas, firma temporal y descargas verificadas están en el workflow.
La compilación se realiza en Actions; no requiere rutas del ordenador del propietario.

La entrada **CoreRPG · prueba nativa** de Host2D abre una vertical estructural real.
El Host de confianza concede un actor propio y dos destinos; el cuarto ID permanece
oculto. La interfaz muestra únicamente contexto autorizado y recibos saneados.
No implementa interpretación de texto ni juego RPG completo.

## API y clasificación

Todos los envelopes usan `api_version: int = 1`. Los esquemas rechazan campos
adicionales, tipos coercibles, versiones incompatibles y límites excedidos.
Resultados: `status`, `error_code`, `api_version` y payload específico. Los enteros
uint64 privilegiados (semilla, revisión, RNG) usan decimal canónico String; IDs de
esta vertical se limitan a 4096 y son int. No se transportan punteros o spans.

`CoreRPGHost` es **privilegiado**, para scripts locales del Host de confianza:

| Método | Solicitud / resultado |
| --- | --- |
| initialize | `{api_version, seed: String, entities: int[1..256]}`; IDs creados por Core |
| admin | `{api_version, operation, ...}`; operaciones detalladas debajo |
| step | `{api_version, actions: Array[0..64]}`; resultados privilegiados y prefijo procesado |
| open_session | `{api_version, observer: int, audience: player/npc/ai, allow_place?: bool, allow_remove?: bool, destinations?: Array[int]}`; `{session}` |
| capture | sin argumentos; `{bytes: PackedByteArray}` del codec Core |
| restore | `PackedByteArray`; valida y publica mundo/RNG juntos, invalida sesiones solo si tiene éxito |
| diagnostics | inicialización, versión/commit Core, revisión e identidades; nunca datos para IA/UI de jugador |
| close | libera campaña e invalida sesiones |

Admin: create_entity; declare_population(entity,total); materialize(entity,count≤256);
learn/revoke(observer,subject,kind[,relation_kind,target]); revoke_knowledge(observer).
FactKind 1 existencia, 2 definición, 3 contención, 4 relación exacta, 5 población,
6 origen.

NIM-07 I2 añade `initialize_v001({api_version:1, files:Dictionary})` únicamente al
Host privilegiado. `files` contiene exactamente los nueve nombres relativos del
pack y sus `PackedByteArray`; no admite rutas filesystem, overrides de semilla,
permisos ni metadatos aportados por jugador. Límites: 64 KiB/documento,
128 KiB/publicación. El SHA-256 del lock aprobado fija a su vez inventario,
huellas de archivos, release y conjunto de definiciones; una sustitución con su
propio lock se rechaza. Los bytes exactos fijados satisfacen los schemas Nimroel
verificados offline; manifiesto y recursos pasan además por los decoders/schema
reales de `CoreRPG::ContentJson` antes de construir `ContentCatalog`.

Preparación reproducible: `python Tools/NIM07/stage_pack.py` desde la raíz
(requiere `Tools/CoreRPG413/requirements.txt`; admite `--core-root`). El driver
funcional lo ejecuta antes de build/import/regresiones/export. Solo se generan
nueve JSON ignorados en `Host2D/generated_content/treskal-v001`; los presets
nativos los incluyen expresamente. Godot lee los bytes desde `res://` con
FileAccess; C++ nunca recibe esa ruta. Sin staging, V001 falla con código claro.

El catálogo inmutable pertenece a Campaign mediante `shared_ptr<const ...>` y
sobrevive a copias transaccionales del mundo. Solo se publica la campaña después
de verificar contenido, bootstrap, Inspector y límites Persistence. Los errores
`CONTENT_*` conservan campaña/capacidades anteriores; éxito invalida capacidades.
Se reproduce el fixture y `remember` del test upstream, sin tiradas de prueba RNG.
La sesión del observador 6 se abre sin permisos de acción; el 7 tiene conocimiento
separado. La presentación recibe exclusivamente contexto de sesión autorizado.

`restore` resuelve definiciones con el catálogo de la campaña ya verificada;
sin catálogo conserva el comportamiento neutral. Esto prepara el mecanismo Core,
**no valida compatibilidad externa de saves V001**: publicación/contexto original
y almacenamiento atómico de metadatos siguen pendientes de I4. El controlador
rechaza save/load de V001 y no ofrece botones de continuidad entre procesos.
`diagnostics` añade conteos privilegiados de catálogo y vínculos, nunca usados
como contexto del jugador. Core, godot-cpp y jsoncons mantienen los SHAs fijados.
ContentJson y HashingContext se habilitan solo en el puente funcional; el laboratorio
legado conserva ContentJson OFF y su perfil de clases original.
Los códigos Core se preservan como `core_status` ordinal del enum upstream; cada
operación está identificada por el esquema y sus tipos en el informe de contratos.

Step admite place(actor,entity,target), remove_containment(actor,entity),
add_relation/remove_relation(actor,entity,target,relation_kind),
roll(actor,stream,minimum,maximum). Cada acción admite expected_revision:String y
preconditions:[{kind:0..2,subject[,related]}]. RuleCheckKind 0 existencia, 1
contenedor directo, 2 sin contenedor. Los rechazos Core no son errores de transporte;
consultar results[].outcome/rejection y processed. Un batch con esquema inválido se
rechaza entero antes de ejecutarse; Simulation conserva su contrato de prefijo
cuando retorna interrupción. No se reenvían automáticamente prefijos ni tiradas.

`CoreRPGSession` es una capacidad limitada; ClassDB puede construir una sesión
vacía, pero no asignarle Runtime ni permisos. No tiene acceso al Host ni a saves.

- context({api_version[,subject,kind,max_selected:0..256,max_content_bytes:0..65536]}):
  ContextBuilder sobre Visibility del observador fijado. Solo facts autorizados,
  procedencia, ausencia conocida, contexto completo/truncado y contadores de vista.
  Devuelve context_id local opaco; la revisión permanece en C++. Caducidad 60 s.
- submit({api_version,context_id,request_id:int>0,operation[,target]}): solo player,
  place sobre sí mismo hacia destino explícitamente permitido y conocido, o
  remove_containment propio con permiso. Actor, grants y precondiciones externos
  se rechazan. Request IDs estrictamente crecientes, ticket consumido tras Core;
  cada nuevo contexto invalida el anterior. Recibo sin ActionResult, RNG o revisión.
- availability() y close(): estado controlado e invalidación explícita.

NPC/AI son consulta, con conocimiento propio, sin iniciativa ni ejecución directa.
No se otorgan permisos por conocer un ID. No hay autenticación remota en un puente
local: la posesión de la sesión y su asignación por el Host son la autoridad.

Límites de campaña: 4096 entidades y por tabla dispersa, 1 MiB de guardado, 64 sesiones,
64 acciones, 64 precondiciones. Consultas seleccionan como máximo 256 hechos.
Los métodos aceptan únicamente el hilo creador. Se rechazan otros hilos antes de
acceder al mundo; no hay worker, callbacks, señales reentrantes ni punteros prestados.

La capa GDScript `core_save_store.gd` decide rutas user://, comprueba I/O y usa
.tmp/.bak para reemplazo recuperable. No garantiza fsync del directorio frente a
pérdida eléctrica; CRC32C detecta corrupción y no autentica modificaciones maliciosas.
Todos los saves y diagnósticos privilegiados permanecen en el Host. Los scripts
hostiles dentro del mismo proceso no están aislados por GDExtension.

Informes permanentes y pruebas físicas: [Docs/NIM-06](../../../Docs/NIM-06/).

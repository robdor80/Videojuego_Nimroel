# Arquitectura de GDExtension

Base Nimroel `6c7ed6a8013b471be0e66dbc4d5bedaeb3541782`; CoreRPG
`4f282863737bcd8f5add401202a9e1064c133672`. Código verificado por CI:
`c071105fcb02e125641594cea4f859dbaad711a2`.
Godot 4.7.2 Standard; godot-cpp oficial `e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`
(API 4.5 compatible hacia versiones menores posteriores, comprobada con 4.7.2).
[Pins y hashes oficiales](evidence/dependencies.json).
Resultados nuevos y enlaces de CI: [evidencia compacta](evidence/ci-summary.json).
Las pruebas físicas no están realizadas.
CI final: [39430632471](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632471), success.
Checkout automático PR `8c990b3e1d3672b951f545e9028b6b6f7dc94259`,
árbol idéntico al HEAD de código (verificado por API). No se ha fusionado en main.

```mermaid
flowchart LR
  UI[Presentación Host2D] --> Port[CorePort / sesión limitada]
  Port --> Session[CoreRPGSession]
  Session --> View[Visibility + ContextBuilder]
  Session --> Actions[ActionEngine]
  Trusted[Host de confianza] --> Host[CoreRPGHost]
  Host --> Core[WorldState + RandomStreams]
  Host --> Simulation[Simulation]
  Host --> Persistence[Persistence]
  Actions --> Core
  View --> Core
  Simulation --> Actions
  Persistence --> Core
  Trusted --> IO[CoreSaveStore / user://]
```

## Vida útil y aislamiento

CoreRPGHost es RefCounted y posee un Runtime privado. Runtime posee una única
campaña activa con WorldState y RandomStreams. Las sesiones solo mantienen
weak_ptr al Runtime; no prolongan la vida del mundo ni contienen un puntero al
Host. Destruir el Host deja las sesiones expiradas. Cada instancia es independiente.
No hay singleton nativo, red, callbacks del Core ni señales reentrantes.

La extensión registra ambas clases al nivel SCENE y no mantiene recursos globales
al cerrarse. `reloadable=false`: no se recarga código mientras hay objetos vivos.
Se acepta únicamente el hilo creador y se devuelve WRONG_THREAD en otro hilo.
Las operaciones y destructores de sesión coordinan el acceso con un mutex.

Inicialización, restauración y cierre incrementan generación y anulan todas las
sesiones. Un restore fallido conserva campaña y generación. IDs/revisiones iguales
no vuelven a autorizar una capacidad antigua. El Host debe abrir nuevas sesiones.

## Comunicación

El contrato de transporte tiene versión 1, campos cerrados y tipos estrictos.
La API Godot usa Dictionary/PackedByteArray; los valores se validan y se convierten
a los DTO C++ tipados del Core. No se serializa memoria, padding, punteros o spans.
Los campos uint64 privilegiados usan decimal String canónico para no truncar a
los 63 bits positivos de Variant. IDs están acotados a 4096 para esta vertical.
[Esquemas completos](../../Game/BridgeCoreRPG/native/README.md).

Session.context fija el observador en C++, crea ObserverView y la selecciona
mediante ContextBuilder. Mantiene procedencia, ausencia conocida y truncamiento.
El context_id es una correlación local creciente, no una revisión ni identidad de
mundo. Cada consulta sustituye el ticket anterior; caduca a los 60 segundos.
Session.submit exige ticket vigente, request_id creciente, actor implícito, permiso
explícito y destino autorizado. La revisión se enlaza solo en memoria nativa.

Los recibos de sesión contienen outcome, request_id, status/error y events vacío.
No hay stream de eventos autorizado en el Core; no se inventa. Las consecuencias
se consultan mediante una vista nueva. No se entrega ActionResult ni revisión.
Solo Host.step obtiene diagnósticos técnicos privilegiados de Simulation.

## Publicación y atomicidad

El adaptador prepara candidatos usando los mismos tipos y operaciones Core; no
implementa un segundo motor. Convierte/valida la solicitud completa antes de
Simulation. Un batch de esquema inválido no procesa prefijo. Core mantiene su
atomicidad por acción y, ante interrupción, su prefijo procesado explícito.
Las cuotas del puente se comprueban antes de publicar el candidato; excederlas
rechaza la operación del puente completa. No hay reintento ni replay automático.
El coste de copiar la campaña es O(estado); es una elección conservadora y acotada,
no una promesa de rendimiento para mundos grandes.

CoreSaveStore posee rutas y I/O; Persistence posee formato, checksum, mundo y RNG.
.tmp/.bak permite recuperar una interrupción entre renombrados, sin prometer una
transacción duradera frente a pérdida eléctrica. Un archivo corrupto no se
sustituye silenciosamente por otro. UI recibe errores y nunca repara estado.

Verificaciones: destrucción, cierre, separación de instancias, restore, contexto,
acciones y rechazo de hilo en native_bridge_probe.gd; resultados nuevos en 04/05.

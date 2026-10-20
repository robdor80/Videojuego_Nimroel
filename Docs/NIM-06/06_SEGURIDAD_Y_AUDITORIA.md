# Seguridad y auditoría

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

## Frontera de confianza

Scripts locales del Host y CoreRPGHost son privilegiados; son parte de la base de
confianza. GDExtension no es un sandbox para scripts/plugins hostiles en el mismo
proceso. CoreRPGSession es una capacidad limitada sin setter de Runtime, observador
o permisos. Construirla por ClassDB deja una sesión sin autoridad.

WorldState e Inspector no se registran. No hay método de sesión para snapshots,
saves, revisión, RNG, conteos globales o resultados técnicos. Las sesiones reciben
únicamente VisibleFact mediante Visibility y ContextBuilder, con presupuestos y
estado de truncamiento. El Host nunca los enriquece desde tablas privilegiadas.
NPC/AI reciben su propia vista de consulta; no existen proveedores ni red nativa.

Los campos actor/observer/grants/revision/preconditions no son aceptados en
solicitudes de sesión. El Host concede actor propio y destinos/operaciones de
forma explícita. La existencia conocida no concede permisos. La UI interactiva
muestra solo vistas/recibos; la revisión queda en diagnóstico técnico de confianza.

## Controles y pruebas

| Riesgo | Control | Comprobación |
| --- | --- | --- |
| Suplantación / ampliación | Esquema cerrado, actor implícito, permiso y destino | actor/grants/campos desconocidos denegados |
| Fuga de secretos | ObserverView y ContextBuilder, sin grants cliente | entidad oculta y ausente devuelven hechos vacíos iguales |
| Repetición / contexto obsoleto | request_id creciente, ticket consumido/caducidad, revisión privada | replay, ticket anterior y revisión obsoleta rechazados |
| Resurrección de capacidades | Generación nueva tras restore/init/close | sesión vieja expirada, incluso mismos IDs |
| Corrupción de save | Límites/CRC32C/codec Core, candidato y publicación conjunta | corrupción/truncado preservan mundo/RNG y sesión |
| Memoria / vida útil | RefCounted, unique_ptr, weak_ptr; sin spans retenidos | cierre/destrucción y Host ausente sin acceso inválido |
| Instancias cruzadas | Runtime por Host | campañas independientes |
| Hilos | propietario fijo y exclusión | llamada desde Godot Thread devuelve WRONG_THREAD |
| Fallo de validación | validación completa antes de efectos y candidato Core | bytes iguales tras rechazo/batch inválido |
| RNG incorrecto | streams Core y snapshot juntos | golden independiente y continuación tras restore |
| I/O / rutas | slot cerrado, user://, límites, .tmp/.bak, errores comprobados | traversal, archivo ausente y reemplazo físico |
| ABI accidental | PE/ELF, deps permitidas, ocultación ELF | verificación binaria y paquete por plataforma |

La autorización de esta vertical permite contención propia; no pretende resolver
permisos sociales, costes, alcance o mecánicas RPG. Rechazos de sesión son genéricos
para no entregar diagnósticos sobre realidad oculta. El Host conserva los motivos
Core para depurar operaciones privilegiadas. No se prometen canales temporales
indistinguibles ni ocultación retroactiva de hechos ya entregados.

## Límites materiales

- 4096 entidades/entradas por tabla, 1 MiB de save, 64 sesiones, 64 acciones y
  precondiciones, 256 hechos seleccionados. Son cuotas de recursos, no reglas RPG.
- CRC detecta corrupción accidental; no autentica saves modificados a propósito.
  Los bytes completos son privilegiados y no se aceptan desde proveedores.
- En los métodos, std::bad_alloc/length_error y excepciones inesperadas se convierten a errores
  controlados. No se promete recuperación de un OOM fatal del propio Godot.
- No se ejecutó inyección exhaustiva de asignaciones, fuzzing ni ASan del puente.
- Caducidad de ticket a 60 s está implementada; no se usa una espera de 60 s como
  prueba de reloj. Sí se prueban consumo, correlación y sustitución de tickets.
- Reemplazo de archivo recuperable no equivale a fsync del directorio ni a
  protección ante modificación maliciosa del sistema de archivos.
- Sesiones y permisos no se persisten; el Host debe autorizar de nuevo al cargar.
- Restores con definiciones requieren catálogo Core y se rechazan sin él. La
  carga de contenido/definiciones no está implementada por este puente.

Auditoría de cambios: no se altera CoreRPG, main.gd, proveedores, voz, pruebas
existentes ni workflow NIM-01. No se escribe en las ramas #22/#23; sus avances externos se registran en 07. La evidencia
final incluye hashes y comparaciones, no secretos ni rutas personales.

Resultado nuevo: 124 checks aprobados por proceso en Windows editor, Windows
exportado y control Linux, incluido aislamiento de dos controladores GDScript.
CorePort no conserva referencias globales a sesiones. PR #22 avanzó externamente
según 07; no se alteró su rama ni se integró su código. No hay ASan ni ejecución
Android que respalden garantías adicionales; siguen pendientes los límites citados.

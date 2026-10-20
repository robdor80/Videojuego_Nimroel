# Incidencias y soluciones

Main integrado: `cd1735b1c9a1bb7507a3b1ce42d96c6d103b0977` (NIM-05 / PR #22).
CoreRPG `4f282863737bcd8f5add401202a9e1064c133672`; godot-cpp oficial
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, API 4.5; Godot **4.7.2 Standard**.
Código verificado: `9924cc38f2fb1162e49ad80779db76c8e5d3f886`.
[CI nativa 39483287563](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563) y
[regresiones 39483287443](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287443): success.
Checkout PR automático `7296c1eb43eaf3da96cc9d995f13bcdb9cb9c7eb`, árbol idéntico al HEAD de código.
[Pins](evidence/dependencies.json) · [Evidencia vigente](evidence/ci-summary.json) ·
[Integración NIM-05 y conservación de fuentes](11_INTEGRACION_MAIN_NIM05.md).
No se ha fusionado ninguna PR ni modificado main. Las pruebas físicas no están realizadas.

| Revisión / run | Hallazgo | Causa y corrección | Resultado |
| --- | --- | --- | --- |
| 87ad6c3e / 39428670160 | Core compila/enlaza en Windows/ARM64, import GDScript falla | Inferencia `var connected :=` sobre resultado Variant sin tipo; se cambia a `var connected: bool` en 49b9b43d | Run cancelado; no se presenta como smoke aprobado |
| 87ad6c3e / 39428670413 | Regresión arranca con script inválido | Misma inferencia; se cancela ejecución obsoleta, se añaden timeouts a procesos de prueba | Repetición completa posterior |
| 49b9b43d / 39428996800 | Primera vertical funcional | Carga, 108 checks y paquete Windows; Android compila/enlaza y APK firma/verifica | success en ambos jobs; antecedente, no evidencia final de cambios posteriores |
| 4e2af91f | Ampliación interactiva | Controlador Host real, pruebas del controlador y golden RNG/hilo | Integrada en CI posterior |
| 7535531e | Separación producción/lab | Extraer configuración de dependencias compartida; producción deja de compilar/depender del adaptador experimental | Se revalida con build nuevo |
| 6b319490 | ABI interna ELF | Static libs podían publicar símbolos C++ internos; añadir --exclude-libs,ALL y verificación de ausencia de WorldState/Inspector/ActionEngine en dyn-syms | Resultado en evidencia final |

Runs pendientes sustituidos por GitHub concurrency no son fallos técnicos ni
pruebas aprobadas. El workflow mantiene un run activo por referencia y sustituye
el pendiente anterior; no se usan resultados de un SHA distinto como si fueran
los de la revisión final.

La sincronización de documentación del editor mediante EditorPlugin procede de
la preparación #26 (incidencia upstream godot-cpp #2024). Se reutiliza: espera
filesystem, abre ayuda RefCounted para unir el hilo, drena callbacks y exige salida
0 sin ERROR. No se atribuye su descubrimiento a esta fase ni se ignoran crashes.

El parseo auxiliar local usó Godot 4.6.3 disponible en Cloud, únicamente para
localizar errores sintácticos; las validaciones de aceptación ejecutan realmente
Godot 4.7.2 en Actions. Todas las compilaciones nativas se realizan en Actions.

Avisos upstream no bloqueantes, cuando aparecen: inicializadores agregados Core
Knowledge/Visibility y referencia opcional themed_icon.xml de plantilla Android.
No se silencian ni se modifica Core para ocultarlos. Dispositivos físicos,
durabilidad eléctrica de I/O, carga ContentJson y métricas siguen pendientes.

## Auditoría de cierre

La revisión `6b319490` completó ambos jobs (run 39429692262), con 121 checks.
La auditoría posterior detectó que el puerto GDScript podía compartir la sesión
entre controladores. `c071105f` elimina todo estado global del puerto: la capacidad
se pasa en cada solicitud. Añade pruebas de dos controladores, acción y cierre
independientes. Run final **39430632471**, Windows/Android success, **124 checks**
en Windows editor, Windows exportado y control Linux. No se presenta el resultado
anterior como prueba de esta corrección.

La PR #22 avanzó externamente a `469f27f376eacbe44fe0fcb5770ae5984befa5cb`
(merge de main, 20/10 13:27:58 UTC). Se consultó de nuevo y se compararon archivos:
ninguna intersección con los modificados por NIM-06. Su rama no fue alterada por
este trabajo. PR #23 avanzó también externamente a
`be7806c5a8d661db35dfb417b5244bf684318732` (13:32:16 UTC), reconciliando
NIM-05/política IA. Se volvió a comparar el listado de archivos: sin intersecciones.
Main y Core mantienen los SHAs auditados. No fue necesaria intervención del usuario.

## Integración posterior de main / NIM-05

- Merge 7b3c2873 desde main cd1735b1, sin conflictos ni descarte de trabajo.
- Ref remota NIM06 no existía en el seguimiento local (origin solo configuraba main);
  fetch explícito de esa ref y comparación local/remota antes de merge/push.
- 9924cc38 amplía regresiones NIM05 y aislamiento de diagnóstico con Core activo.
- CI 39483287563 y 39483287443: success en todos los jobs. 129 checks nativos
  por proceso y 8+29+11 tests Python, seis suites Godot. No hubo fallos técnicos
  de compilación, carga o exportación que requirieran corrección adicional.
- PR23 avanzó externamente de ea564e95 a c3d15241 durante el trabajo; no se
  modifica ni se integra su rama. Evidencia de refs en main-integration-audit.json.

Las secciones previas son historial de la entrega original; el estado actual
se resume en 11 y ci-summary.json. No hubo force push ni fusión de PR.

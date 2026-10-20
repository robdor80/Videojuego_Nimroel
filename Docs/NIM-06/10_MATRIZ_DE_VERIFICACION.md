# Matriz de verificación

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

Las evidencias corresponden al SHA y run de ci-summary.json. No se transfieren
resultados de la preparación #26 a esta fase funcional.

| Requisito | Implementación | Prueba/evidencia | Aceptación |
| --- | --- | --- | --- |
| Main/PR26 y Core reales | Auditoría previa 03 | API/git y SHAs registrados | Verificado |
| PR22/23 independientes | Sin cambios a sus refs/archivos en conflicto | Auditoría final de refs y diff | Verificado; auditoría en 07 |
| Core única autoridad | Runtime privado, llamadas Core, sin mundo GDScript | Mapas enlace + vertical | Verificado en ámbito entregado |
| Registro y carga Godot | CoreRPGHost/CoreRPGSession | Smoke Godot Windows 4.7.2 | Verificado; 04 |
| Host2D real | CorePort, Controller y escena técnica | Tests Controller + paquete exportado | Verificado; 04 |
| Ciclo entidades/acciones/consulta | WorldState, ActionEngine, Visibility/ContextBuilder | Probe nativo | Verificado; 04/05 control Linux |
| Sesiones/roles | Actor fijo, permisos Host, NPC/AI consulta | Spoof/grants/denegaciones/vida útil | Automatizado |
| Revisiones/rechazos | Core expected_revision privado, DTO cerrado | Ciclos/no-op/precondiciones/stale/batch | Automatizado |
| Simulación y RNG | Simulation + RandomStreams | Golden independiente y continuidad | Automatizado |
| Persistencia | Core codec + Store Host | Archivo real, restore, CRC/truncado/atomicidad | Automatizado |
| Seguridad de vista | Solo ObserverView/ContextBuilder | Oculto/ausente, memoria, presupuestos | Automatizado en alcance 06 |
| Windows C++20/enlace/DLL x64 | Toolchain/pins compartidos | PE, dumpbin y mapas | Verificado; 04 |
| Windows exportación/ejecución | EXE/PCK/DLL | Bytes DLL + self-test EXE | Verificado; 04 |
| Android C++20/enlace/SO ARM64 | NDK y STL fijados | ELF183, deps, LOAD16KiB, mapas | Verificado; 05 |
| Android APK íntegro/firmado | Exportador Godot oficial | apksigner/aapt2, SO exacta dentro APK | Verificado; 05 |
| Ejecución Android ARM64 | Sin runtime Android disponible | No sustituida por Linux | Pendiente físico |
| MSI Raider Windows11 | Paquete e instrucciones 09 | No ejecutado físicamente | Pendiente físico |
| Tab S9+ | APK e instrucciones 09 | No ejecutado físicamente | Pendiente específico de aceptación |
| Regresiones NIM01–04 | Scripts existentes intactos | Workflow existente + con extensión | Evidencia 04 |
| Política IA/voz | Sin cambios a proveedores/voz | Diff y regresiones existentes | Verificado; auditoría en 07 |
| Informes en Git | Diez Markdown + evidencia compacta | Commits publicados y lectura GitHub | Verificado por publicación/consulta de PR |
| PR Draft sin merge | PR27 | Estado Draft, base main | Verificado por publicación/consulta de PR |
| Contenido/definiciones | No expuesto aún | Core disponible; lector Host pendiente | No implementado |
| RPG completo/NPC autónomos/eventos públicos | Contratos ausentes o fases posteriores | Documentado 03/08 | No implementado; fuera de vertical |

**Aceptación técnica acotada:** depende de los resultados nuevos 04/05; aun con CI
verde, la validación plena en Tab S9+ permanece abierta. No se declara terminada
la implementación completa de todos los sistemas RPG del videojuego.

Resultado de cierre: run nativo 39430632471 y regresiones 39430632469 success;
124 checks por proceso verificado, 8+29 tests Python y cinco suites Godot previas.
SHA de código c071105f, checkout automático 8c990b3e con árbol idéntico.
Los dos requisitos físicos permanecen pendientes. Catálogos y sistemas RPG futuros
no se marcan como completos; el detalle de cobertura está en 08.

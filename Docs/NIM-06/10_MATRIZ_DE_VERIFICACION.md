# Matriz de verificación

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

Las evidencias corresponden al SHA y run de ci-summary.json. No se transfieren
resultados de la preparación #26 a esta fase funcional.

| Requisito | Implementación | Prueba/evidencia | Aceptación |
| --- | --- | --- | --- |
| Integración main/NIM05 | Merge 7b3c2873, pruebas 9924cc38 | CI 39483287563/39483287443 y auditoría por blobs | Verificado; 11 |
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
| Regresiones NIM01–05 | Scripts existentes intactos | Workflow existente + con extensión | Evidencia 04 |
| Política IA/voz | Sin cambios a proveedores/voz | Diff y regresiones existentes | Verificado; auditoría en 07 |
| Informes en Git | Once Markdown + evidencia compacta | Commits publicados y lectura GitHub | Verificado por publicación/consulta de PR |
| PR Draft sin merge | PR27 | Estado Draft, base main | Verificado por publicación/consulta de PR |
| Contenido/definiciones | No expuesto aún | Core disponible; lector Host pendiente | No implementado |
| RPG completo/NPC autónomos/eventos públicos | Contratos ausentes o fases posteriores | Documentado 03/08 | No implementado; fuera de vertical |

**Aceptación técnica acotada:** depende de los resultados nuevos 04/05; aun con CI
verde, la validación plena en Tab S9+ permanece abierta. No se declara terminada
la implementación completa de todos los sistemas RPG del videojuego.

Resultado de cierre: run nativo 39483287563 y regresiones 39483287443 success;
129 checks por proceso verificado, 8+29+11 tests Python y seis suites Godot previas.
SHA de código 9924cc38, checkout automático 7296c1eb con árbol idéntico.
Los dos requisitos físicos permanecen pendientes. Catálogos y sistemas RPG futuros
no se marcan como completos; el detalle de cobertura está en 08.

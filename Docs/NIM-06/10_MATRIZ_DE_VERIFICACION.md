# Matriz de verificación

Estado vigente: [cierre final y evidencia CI](12_CIERRE_FINAL.md).
Las secciones de CI anteriores conservan sus SHAs y resultados históricos; no acreditan la interfaz corregida.
Pruebas funcionales físicas anteriores: satisfactorias según el propietario en ambos dispositivos.
La interfaz corregida requiere nueva comprobación física.


Las evidencias corresponden al SHA y run de ci-summary.json. No se transfieren
resultados de la preparación #26 a esta fase funcional.

| Requisito | Implementación | Prueba/evidencia | Aceptación |
| --- | --- | --- | --- |
| Integración main actual | Merge c804612d desde 028ea86 | Sin conflictos; conservación Core/IA/voz/broker | Detalle y CI final en 12 |
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
| Ejecución Android ARM64 | CI sin runtime Android | Propietario: GDExtension, 129/129, cero errores | Satisfactoria comunicada; versión anterior |
| MSI Raider Windows11 | Prueba comunicada por propietario | 129/129, acciones y persistencia tras reabrir | Satisfactoria comunicada; versión anterior |
| Tab S9+ | Prueba comunicada por propietario | 129/129, acciones y persistencia tras reabrir | Satisfactoria comunicada; versión anterior |
| Scroll y adaptación nuevos | Contenedores, DPI Android, controles 48/fuente18 | Suite pequeña native_layout_smoke; CI en 12 | Comprobación física nueva pendiente |
| Regresiones NIM01–05 | Scripts existentes intactos | Workflow existente + con extensión | Evidencia 04 |
| Política IA/voz | Sin cambios a proveedores/voz | Diff y regresiones existentes | Verificado; auditoría en 07 |
| Informes en Git | Once Markdown + evidencia compacta | Commits publicados y lectura GitHub | Verificado por publicación/consulta de PR |
| PR Draft sin merge | PR27 | Estado Draft, base main | Verificado por publicación/consulta de PR |
| Contenido/definiciones | No expuesto aún | Core disponible; lector Host pendiente | No implementado |
| RPG completo/NPC autónomos/eventos públicos | Contratos ausentes o fases posteriores | Documentado 03/08 | No implementado; fuera de vertical |

**Aceptación técnica acotada:** depende de los resultados nuevos 04/05; aun con CI
verde, la comprobación física de la interfaz corregida permanece abierta. No se declara terminada
la implementación completa de todos los sistemas RPG del videojuego.

Resultado de cierre: run nativo 39483287563 y regresiones 39483287443 success;
129 checks por proceso verificado, 8+29+11 tests Python y seis suites Godot previas.
SHA de código 9924cc38, checkout automático 7296c1eb con árbol idéntico.
Los dos requisitos funcionales físicos de la versión anterior fueron comunicados como satisfactorios.
Solo la nueva presentación queda pendiente de comprobación física. Catálogos y sistemas RPG futuros
no se marcan como completos; el detalle de cobertura está en 08.

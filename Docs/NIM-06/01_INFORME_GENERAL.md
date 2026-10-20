# NIM-06 BUILD — Informe general

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

## Resultado final

**Puente funcional completado y verificado en el ámbito estructural disponible.**
Windows: carga real en Godot 4.7.2 y ejecutable exportado, **124 comprobaciones
aprobadas en cada proceso**. Android: compilación/enlace ARM64, APK firmado e
integridad de la SO comprobada; **ejecución Android y dispositivos físicos pendientes**.
Control Linux de exportación: 124 comprobaciones aprobadas; no cuenta como Android.

[CI nativa final](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632471)
y [regresiones existentes](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39430632469):
ambas success. NIM01–04 y teclado pasan; Python NIM03: 8/8, NIM04: 29/29,
tanto en Windows con extensión como en el workflow Linux existente. Los tres jobs
del workflow existente (incluidas exportaciones y TTS previo) pasan sin cambiarlo.

No hay bloqueo del Core para esta vertical. La aceptación plena Android requiere
la ejecución física indicada en 09. La carga de catálogos/definiciones y los sistemas
RPG posteriores se identifican expresamente como cobertura no implementada.
Las revisiones posteriores al HEAD de código solo consolidan documentación.

## Entrega

Puente funcional local, sin modificar CoreRPG. Registra CoreRPGHost y
CoreRPGSession, integra un puerto real con Host2D y una vertical interactiva de
entidades, contención, consultas autorizadas y persistencia. También expone
relaciones, población/materialización, conocimiento, precondiciones y tiradas
como operaciones de administración del Host. Todo el estado y las reglas
estructurales residen en instancias reales de CoreRPG.

No implementa todos los sistemas RPG de Nimroel. La integración conversacional
sigue bloqueada sin una sesión vinculada y sin interpretación validada; no se
ha desarrollado IA, voz, diálogo, combate, inventario ni iniciativa NPC.

## Arquitectura y archivos

- `Game/BridgeCoreRPG/native/src/bridge.cpp`: autoridad Host, sesiones y codecs.
- `Game/BridgeCoreRPG/cmake/`: pins y perfil compartidos con el laboratorio.
- `Game/Host2D/scripts/core_port.gd`: transporte hacia una sesión real.
- `native_world_controller.gd`, `native_vertical.gd`, `native_vertical.tscn`:
  flujo interactivo dentro del proyecto 2D, sin copia GDScript del mundo.
- `core_save_store.gd`: rutas user://, comprobaciones I/O y respaldo recuperable.
- `tests/native_bridge_probe.gd`, `tests/nim06_smoke.gd`: vertical, seguridad y continuidad.
- `Tools/NIM06/native_lab.py`, `.github/workflows/nim-06-native-lab.yml`:
  compilación, PE/ELF, carga, contratos, regresiones y paquetes.

El checkout fuente no contiene DLL/SO/EXE/APK. El build instala el descriptor y
las bibliotecas en Host2D. Sin build, el Host sigue abriendo su interfaz 2D y
anuncia `native_available=false`; no presenta una conexión ficticia.

## Estado verificable

El estado definitivo por plataforma y los hashes están en los informes 04/05 y
ci-summary.json. Carga/ejecución Windows y paquete Windows se verifican de forma
independiente. En Android se verifica compilación/enlace/ABI/dependencias/firma y
bytes de la extensión dentro del APK; no se confunden con ejecutar Android.

## Índice permanente

1. [Informe general](01_INFORME_GENERAL.md)
2. [Arquitectura](02_ARQUITECTURA_GDEXTENSION.md)
3. [Contratos y auditoría previa](03_CONTRATOS_CORERPG.md)
4. [Windows](04_PRUEBAS_WINDOWS.md)
5. [Android](05_PRUEBAS_ANDROID.md)
6. [Seguridad](06_SEGURIDAD_Y_AUDITORIA.md)
7. [Incidencias](07_INCIDENCIAS_Y_SOLUCIONES.md)
8. [Pendientes y traspaso](08_PENDIENTES_Y_TRASPASO.md)
9. [Pruebas físicas](09_GUIA_PRUEBAS_FISICAS.md)
10. [Matriz de verificación](10_MATRIZ_DE_VERIFICACION.md)

La entrega permanece en la PR Draft #27. No se fusiona ni se modifica main.
Las PR #22/#23 permanecen intactas. Los informes y evidencia compacta quedan en
Git; los logs voluminosos y paquetes se publican en Actions con retención de 30 días.

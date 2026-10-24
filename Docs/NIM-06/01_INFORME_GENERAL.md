# NIM-06 BUILD — Informe general

Estado vigente: [cierre final y evidencia CI](12_CIERRE_FINAL.md).
Las secciones de CI anteriores conservan sus SHAs y resultados históricos; no acreditan la interfaz corregida.
Pruebas funcionales físicas anteriores: satisfactorias según el propietario en ambos dispositivos.
La interfaz corregida requiere nueva comprobación física.


## Resultado final

**Puente funcional completado y verificado en el ámbito estructural disponible.**
Windows: carga real en Godot 4.7.2 y ejecutable exportado, **129 comprobaciones
aprobadas en cada proceso**. Android: compilación/enlace ARM64, APK firmado e
integridad de la SO comprobada; **ejecución Android acreditada por comunicación del propietario para la versión anterior**.
Control Linux de exportación: 129 comprobaciones aprobadas; no cuenta como Android.

[CI nativa final](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563)
y [regresiones existentes](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287443):
ambas success. NIM01–05 y teclado pasan; Python NIM03: 8/8, NIM04: 29/29 y NIM05: 11/11,
tanto en Windows con extensión como en el workflow Linux existente. Los tres jobs
del workflow existente (incluidas exportaciones y TTS previo) pasan sin cambiarlo.

No hay bloqueo del Core para esta vertical. El propietario comunica aceptación funcional
física de la versión anterior en ambos dispositivos; la interfaz corregida queda pendiente según 12. La carga de catálogos/definiciones y los sistemas
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
12_CIERRE_FINAL.md para la entrega actual; ci-summary.json conserva evidencia histórica. Carga/ejecución Windows y paquete Windows se verifican de forma
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
11. [Integración anterior de main y NIM-05](11_INTEGRACION_MAIN_NIM05.md)
12. [Cierre final, pruebas físicas y verificación actual](12_CIERRE_FINAL.md)

La entrega permanece en la PR Draft #27. No se fusiona ninguna PR ni se modifica main.
PR #22 se integra a través de main; no se modifica PR #23 ni su rama. Los informes y evidencia compacta quedan en
Git; los logs voluminosos y paquetes se publican en Actions con retención de 30 días.

## Integración de main y NIM-05

Main `cd1735b1` integrado sin conflictos mediante `7b3c2873`; ampliación de pruebas
`9924cc38`. Se conserva íntegro el puente nativo y las políticas heredadas.
Las seis suites Godot y 48 tests Python pasan con extensión en Windows y en el
control Linux. El workflow de NIM-05 pasa también síntesis real y exportaciones.
Histórico anterior: evidence/ci-summary-before-main-integration.json; no se reutiliza
su evidencia como si correspondiera a esta compilación. Detalle en 11.

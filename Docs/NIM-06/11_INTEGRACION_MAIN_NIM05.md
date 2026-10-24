# Integración de main y NIM-05 en NIM-06

Histórico de la integración anterior. El main actualizado, las pruebas físicas
comunicadas y la verificación final están en [12_CIERRE_FINAL.md](12_CIERRE_FINAL.md).

Actualización del 20 de octubre de 2026 (Europe/Madrid). Rama exclusiva:
`feat/nim-06-functional-gdextension`. PR #27 permanece Draft; no se fusiona ninguna PR.

## Base, comprobación y merge

- HEAD anterior local/remoto/PR: `eeb179c87cbb27c3b182de2f0bcabff3dff45087`.
- Árbol de trabajo limpio al comenzar, sin cambios pendientes que descartar.
- Sin otros agentes observados en esta sesión ni procesos Git mutando la rama;
  un solo worktree sobre ella. No hay visibilidad global de otros entornos Cloud.
  La cabecera remota coincidía antes del trabajo y se comprobó antes del push.
- Main integrado: `cd1735b1c9a1bb7507a3b1ce42d96c6d103b0977`, merge de PR #22.
- Merge local en NIM-06: `7b3c2873399b52746d4fd367690bfc533c78ce3f`.
- Pruebas ampliadas: `9924cc38f2fb1162e49ad80779db76c8e5d3f886`.
- `git merge --no-ff origin/main`: sin conflictos. No rebase, reset ni force push.
- El remote solo seguía main; se recuperó explícitamente la referencia de NIM-06
  antes de verificar igualdad y publicar, sin cambiar la configuración ni otras ramas.

## Conservación y compatibilidad

[Auditoría por blobs Git](evidence/main-integration-audit.json): adaptador C++, CMake,
pins Core/godot-cpp, puerto, controlador, Store, proyecto y presets de NIM-06
idénticos a la entrega anterior. No se implementan reglas ni arquitectura nuevas.
El Core permanece fijado en `4f282863737bcd8f5add401202a9e1064c133672` y godot-cpp
en `e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`. Motor/plantillas Godot 4.7.2 Standard.
Herramientas y hashes oficiales: [dependencies.json](evidence/dependencies.json).

Los archivos de main.gd, provider_diagnostic.gd, tts_diagnostic.gd, voice_port.gd,
provider_proxy.py, tts_local.py y el workflow NIM01–05 son iguales a main integrado.
Se conserva el ledger/idempotencia del broker, nonce y whitelist de errores;
no se modifica ningún proveedor/modelo ni la autorización de llamadas de pago.

La voz Windows sigue siendo un diagnóstico local opt-in, no una voz NPC ni un
nuevo servicio del adaptador. En Android continúa deshabilitado ese laboratorio
Windows. GDExtension no incorpora red, proveedores, credenciales o síntesis.
La UI carga ambos laboratorios dentro de Host2D sin sustituir sus responsabilidades.

## Ampliación de comprobaciones

`Tools/NIM06/native_lab.py regressions` ejecuta ahora seis suites Godot
(NIM01–05 y teclado) y tres suites Python offline (NIM03/04/05). Se ejecutan con
GDExtension cargada tanto en Windows como en el control Linux de exportación.
El workflow existente de NIM05 se repite íntegro sin modificarlo, incluida síntesis
real sherpa y paquetes prototipo Windows/Android.

El probe nativo añade comprobación con un mundo Core activo: el flujo de texto
sin capacidad no adquiere autoridad; el broker conserva REQUEST_ID_REUSED; la voz
sanea errores externos; mundo/RNG conservan bytes idénticos. No hay llamadas a
proveedores externos ni reproducción física en estas comprobaciones de contrato.

La compilación Android ARM64, ELF/ABI/dependencias, APK/firma/biblioteca exacta se
comprueban por separado de los tests Linux. Windows exporta y ejecuta el paquete
con la misma suite real. Los resultados y hashes nuevos se consolidan en
[ci-summary.json](evidence/ci-summary.json); los anteriores se conservan en
[ci-summary-before-main-integration.json](evidence/ci-summary-before-main-integration.json).

## Pendientes físicos

MSI Raider Windows 11 y Samsung Galaxy Tab S9+: pendientes. No hay ejecución
Android ARM64 en Actions ni dispositivo. La síntesis de voz del runner Windows
no acredita altavoces, latencia o reproducción física del MSI. Seguir 09 y registrar
run, SHA, hashes, JSON y logs del paquete actualizado.

## Resultados nuevos verificados

[CI nativa 39483287563](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563)
y [regresiones NIM01–05 39483287443](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287443):
**success**, todos sus jobs. Checkout automático 7296c1eb43eaf3da96cc9d995f13bcdb9cb9c7eb,
árbol d8de5cb79ee812ff70c06e78ffeaab6bea98022b idéntico a 9924cc38.

| Plataforma / alcance | Resultado |
| --- | --- |
| Windows Core/godot-cpp/DLL x64 | Compilación/enlace y PE correctos |
| Godot Windows y EXE exportado | 129 checks aprobados en cada proceso |
| Regresión Windows con GDExtension | Seis suites Godot; Python 8+29+11 aprobados |
| Android NDK ARM64 | Compilación/enlace, ELF183, deps Android, LOAD16KiB correctos |
| APK nuevo | Firma v2/v3, SDK24/36, SO idéntica dentro del paquete |
| Control Linux con GDExtension | 129 checks, seis suites Godot y Python 8+29+11 aprobados |
| Workflow NIM05 existente | Godot, broker, TTS real y exportaciones aprobados |
| MSI físico / Android ARM64 real / Tab S9+ | No ejecutados; pendientes |

Artefactos: [Windows](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563/artifacts/12291679162),
[Android](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563/artifacts/12290784767).
Los hashes DLL/SO/APK/EXE/PCK/ZIP y del WAV real NIM05 están en ci-summary.json,
04 y 05. Logs compactos permanentes en evidence/*-excerpt.txt.

No se han cambiado CoreRPG ni main por este trabajo. PR23 avanzó externamente
durante la ejecución; los SHAs observados se registran sin modificar esa rama.
La PR27 continúa abierta y Draft. Los commits posteriores al probado solo
consolidan estos informes y no alteran código ejecutable.

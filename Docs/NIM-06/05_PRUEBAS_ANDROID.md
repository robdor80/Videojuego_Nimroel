# Android ARM64 — Pruebas

Estado vigente: [cierre final y evidencia CI](12_CIERRE_FINAL.md).
Las secciones de CI anteriores conservan sus SHAs y resultados históricos; no acreditan la interfaz corregida.
Pruebas funcionales físicas anteriores: satisfactorias según el propietario en ambos dispositivos.
La interfaz corregida requiere nueva comprobación física.


NDK 29.0.14206865, toolchain CMake oficial, ABI arm64-v8a, android-24,
Clang del NDK, c++_static; runner ubuntu-24.04. SDK 36/build-tools 36.0.0,
Temurin 17.0.15+6 para exportación tradicional sin Gradle.

## Comprobaciones ejecutadas por CI

- CoreRPG C++20, godot-cpp y puente compilados y enlazados para Android.
- ELF64 little endian, e_machine=183 AArch64; no es x86_64 del runner.
- Punto de entrada público nimroel_core_init, enlace --no-undefined.
- Bibliotecas estáticas internas ocultas con --exclude-libs,ALL; no se exportan
  WorldState, Inspector ni ActionEngine como ABI pública.
- Lista cerrada de dependencias Android permitidas y segmentos LOAD >=16 KiB.
  Las dependencias concretas se conservan en ci-summary.json.
- APK debug ARM64 exportado por Godot 4.7.2, sin ERROR del exportador.
- Firma verificada con apksigner 36.0.0; clave de laboratorio temporal por job,
  nunca publicada ni guardada en Git. No es una clave de distribución estable.
- aapt2 verifica minSdkVersion 24, targetSdkVersion 36 y ABI arm64-v8a.
- Todas las bibliotecas del APK tienen machine 183 y ubicación lib/arm64-v8a/.
  `libnimroel_core.android.arm64.so` coincide byte a byte con el build verificado.

El APK usa paquete org.nimroel.rpg.nim06functional, versión técnica de diagnóstico.
Incluye la plantilla oficial libgodot_android.so y libc++_shared.so, además del
adaptador con su STL estático. La biblioteca del adaptador no debe adquirir glibc
ni DLL Windows por compilar en Linux.

## Contratos y ejecución

Se compila una biblioteca Linux x86_64 separada para cargar el mismo adaptador en
el editor de exportación y ejecutar los contratos/guardado/RNG de la vertical.
Eso prueba el Host de exportación y el código común, **no una ejecución Android**.
No se ha establecido un proceso Android ARM64 capaz de cargar la SO en este CI:
los runners disponibles son x64 y no se ha ejecutado un emulador ARM64. Un emulador
x86_64 tampoco acreditaría la ABI solicitada. La CI no acredita funcionamiento físico;
el propietario sí comunica una prueba funcional física satisfactoria de la versión anterior.

Samsung Galaxy Tab S9+: el propietario confirma APK instalado/ejecutado, GDExtension
cargada, 129/129 y cero errores, consultas/acciones/restauración, persistencia entre
ejecuciones y no_change esperado. No se aportan logcat, versión Android ni mediciones.
Quedan la nueva interfaz y los comportamientos no comunicados; no se exige una campaña
masiva ni se amplía el alcance. Consulte 09 y 12.

El aviso upstream de aapt2 sobre themed_icon.xml se registra si aparece; no se
parchea la plantilla oficial. No hay prueba visual del icono temático por CI.

## Repetición y evidencia

```
python Tools/NIM06/native_lab.py build --functional --target android
python Tools/NIM06/native_lab.py build --functional --target linux
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py export-android --functional
```

La firma temporal se configura solo en el paso de exportación del workflow.
Run/job, SHA, hashes SO/APK, tamaño, ABI, firma y resultado del control Linux se
conservan permanentemente en evidence/ci-summary.json. Los logs completos y paquetes
son artefactos de Actions, con retención de 30 días. El límite físico no se cambia
por obtener un workflow verde.

## Resultado final nuevo

- [Job Android](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563/job/118837120978): **success**.
- **Clang 21.0.0** del NDK fijado; Core/godot-cpp/puente compilan y enlazan.
- SO **618608 bytes**, ELF64 AArch64 183, LOAD >=16KiB.
- Dependencias observadas: **libm.so, libdl.so, libc.so**.
- ABI C++ interna oculta; nimroel_core_init accesible.
- APK firmado v2/v3, SDK 24/36, solo arm64-v8a, extensión idéntica al build.
- Control Linux **GNU 13.3.0**, Godot 4.7.2, **129 checks aprobados**.
- Ejecución Android en CI: **NO PROBADA**. Prueba física anterior: **satisfactoria según el propietario**.
- [Artefacto publicado](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39483287563/artifacts/12290784767), 30 días.

| Archivo | SHA-256 |
| --- | --- |
| libnimroel_core.android.arm64.so | `c3570bccdeec5b1ff2d1bca0554cd650e64931624c4958632d7366676d00050e` |
| Nimroel_NIM06_Functional.apk | `15567475adb0a2ab92502495d351c6524bc838d1068e9cd42a860d777186a715` |

[Extracto permanente del log](evidence/android-excerpt.txt). Los hashes del ZIP
publicado y del control Linux se conservan en ci-summary.json; el control no es
un artefacto para instalar en Android. La firma temporal no es distribución final.

El control Linux también supera las seis suites Godot NIM01–05/teclado y los
48 tests Python offline (8+29+11) con extensión cargada. El laboratorio de voz
Windows continúa deshabilitado en Android, sin añadir servicios al adaptador.
La biblioteca ARM64 coincide incluso con el hash anterior; el APK y su firma son
nuevos, y sus hashes se registran como evidencia de esta integración.

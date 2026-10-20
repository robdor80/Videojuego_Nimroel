# NIM-06 — Preparación de compilaciones nativas y GDExtension

Fecha de verificación: 19 de octubre de 2026. Fase técnica previa a NIM-06 funcional.

**Resultado: preparación validada en GitHub Actions para las dos arquitecturas.**
Windows carga y ejecuta CoreRPG en Godot 4.7.2; Android compila, enlaza y se incorpora
al APK ARM64 firmado. La ejecución Android real y las pruebas físicas siguen pendientes.

[Ejecución final satisfactoria](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39336167034),
commit compilado `4e21a4bd35c70b263129d2b85a190c0a722ef9ed`.

| Verificación | Windows x64 | Android ARM64 |
| --- | --- | --- |
| CoreRPG C++20 y godot-cpp | Compilados | Compilados mediante NDK |
| Enlace del adaptador con CoreRPG | Correcto, DLL | Correcto, SO |
| Arquitectura leída del binario | PE AMD64 `0x8664` | ELF64 AArch64 `183` |
| Carga en Godot del sistema destino | Probada en runner Windows | No ejecutada |
| Ocho operaciones reales del Core | Probadas en Godot Windows | No ejecutadas en Android |
| Exportación de paquete del laboratorio | No ejecutada; DLL + proyecto | APK exportado y firmado |
| Biblioteca exacta en el paquete | No aplica | Sí, `lib/arm64-v8a/` |
| Dispositivo físico | Pendiente MSI Raider | Pendiente Tab S9+ |

## Base y aislamiento

- Nimroel `main`: `d559072c88554a52b77e84f3c53792af7b428498`.
- CoreRPG `main`: `4f282863737bcd8f5add401202a9e1064c133672`, repositorio público.
- Rama: `prep/nim-06-native-gdextension`, creada exactamente desde ese main de Nimroel.
- PR #22: `feat/nim-05-build`, cabeza observada
  `f7c96478e250e74cdd9e42e9cf96b706de555888`; no modificada.
- PR #23: `docs/nimroel-ai-models-2026-10-17`, cabeza observada
  `6fcfbef0050ac4abddfeae313fdfb5bf7bf84c44`; no modificada.
- No se modifica CoreRPG ni Host2D, no se fusiona ninguna rama ni se escribe en main.

## Qué demuestra el adaptador

`Game/BridgeCoreRPG/lab` es un proyecto Godot 2D independiente. Registra
`CoreRPGLab`, derivada de `RefCounted`, con un único método
`parse_core_version(text)`. Este llama a `corerpg::SemanticVersion::parse`, una
función definida fuera de cabecera en `src/semantic_version.cpp` del Core.

La operación no es una constante: devuelve los componentes de `4.7.2`, `12.34.56`
y `0.0.0`, y rechaza `01.2.3`, `bad`, `4294967296.0.0`, `1.2.3.4` y la cadena vacía.
El código Godot solo comprueba el contrato y muestra el resultado. No decide reglas
ni modifica ningún estado del mundo. No se implementan NPC, inventarios, diálogos,
simulación, IA ni la integración funcional con la interfaz existente.

El target CoreRPG compila todas sus unidades del núcleo; el enlace estático extrae
las necesarias para esta operación. El módulo opcional `CoreRPGContentJson` y las
pruebas unitarias upstream quedan desactivados. Su validación no forma parte de
esta preparación ni se presenta como realizada.

## Dependencias fijadas

| Elemento | Versión o commit |
| --- | --- |
| CoreRPG | `4f282863737bcd8f5add401202a9e1064c133672` |
| godot-cpp oficial | `e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77` (`godot-4.5-stable`) |
| Motor y plantillas | Godot 4.7.2 Standard; SHA-256 de cada descarga fijado en el controlador |
| API del binding | 4.5, precisión simple; perfil `RefCounted` + `OS` y dependencias necesarias |
| CMake / Ninja | 3.31.6 / 1.11.1.3 |
| Python | 3.12.10 |
| Visual Studio | 2022, MSVC v143, toolset 14.44.35207, `/MT`, x64 |
| Android | NDK 29.0.14206865, API mínima 24, ABI `arm64-v8a`, STL estático |
| Exportación Android | Temurin JDK 17.0.15+6, SDK 36, build-tools 36.0.0 |
| GitHub Actions | checkout, setup-python, setup-java y upload-artifact fijados por SHA |

No se encontró etiqueta godot-cpp 4.7.2. El binding oficial estable 4.5 se usa
conforme a su [garantía documentada de compatibilidad hacia Godot menor posterior](https://github.com/godotengine/godot-cpp/tree/e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77#compatibility).
La compatibilidad con el motor aprobado se verifica ejecutando Godot **4.7.2**;
no se ha cambiado el motor del proyecto ni se ha recurrido a `master`.

El NDK y las API Android corresponden a
[Godot 4.7.2 detect.py](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/platform/android/detect.py)
y [config.gradle](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/platform/android/java/app/config.gradle).

La exportación usa el modo tradicional sin Gradle. Se instala y se verifica el
`apksigner` **36.0.0** realmente seleccionado por Godot al exportar al SDK 36;
no se atribuye la firma al 36.1.0 de `config.gradle`, que no se usa en este modo.
La verificación falla si Godot selecciona otra versión de la herramienta.

Los runners hospedados no son imágenes inmutables. Se registran las versiones
concretas de imagen, compilador y SDK en el log y en CMakeCache. Las dependencias
están fijadas; no se afirma que recompilar en otra imagen produzca hashes idénticos.

## Windows x64

- Compilación CoreRPG C++20, godot-cpp y adaptador: **satisfactoria**.
- Enlace completo: **satisfactorio**; mapa con `SemanticVersion` de CoreRPG.
- Biblioteca: `nimroel_core_lab.windows.x86_64.dll`, **349184 bytes**.
- SHA-256: `7bedb75b0d2da7d6a0ee68b5201a8a5b5947d810cea772725a961bc4c53ef127`.
- Arquitectura: **PE AMD64 `0x8664`**, comprobada leyendo la cabecera binaria.
- `dumpbin` verifica el punto de entrada `nimroel_core_lab_init` y las dependencias;
  única dependencia observada: **KERNEL32.dll**; CRT C++ enlazado estáticamente.
- Compilador observado: **MSVC 19.44.35229.0**, toolset **14.44.35207**;
  Windows SDK **10.0.26100.0**, MSBuild **17.14.60+43b635718**.
- Carga en Godot Windows 4.7.2: **satisfactoria**, incluida la importación y el cierre limpio del editor.
- Ejecución de los ocho casos de CoreRPG desde GDScript: **satisfactoria**, marcador `NIM06_CORE_OPERATION_OK cases=8` y código 0.
- Exportación Windows: no ejecutada; se entrega DLL y proyecto de laboratorio para
  abrirlo con el editor Standard. No se presenta como ejecutable exportado ni como
  validación física del MSI.

[Job Windows satisfactorio](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39336167034/job/118346083441),
commit `4e21a4bd35c70b263129d2b85a190c0a722ef9ed`.
[Artefacto Windows](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39336167034/artifacts/12225504371).
Marcadores observados: `NIM06_EDITOR_IMPORT_OK` y `NIM06_CORE_OPERATION_OK cases=8`,
ambos procesos con salida 0 y sin errores de recursos al cerrar.

Evidencias en el artefacto Windows: `windows-configure.txt`, `windows-build.txt`,
`windows-CMakeCache.txt`, `windows-link.map`, `windows-pe.txt`,
`windows-binary.json`, `godot-version.txt`, `godot-import.txt`, `godot-smoke.txt`.

## Android ARM64

- Compilación cruzada CoreRPG C++20, godot-cpp y adaptador: **satisfactoria**.
- Enlace: **satisfactorio**, `--no-undefined`, ambas bibliotecas estáticas integradas.
- Biblioteca: `libnimroel_core_lab.android.arm64.so`, **581600 bytes**.
- SHA-256: `41c4b8f11a7073a759855f302cc64ab31b39b3e26be9a48e85824a415374e0a1`.
- Arquitectura: **ELF64 little endian, AArch64 `183`**, no x86_64 del runner.
- ABI configurada y destino del compilador: `arm64-v8a`,
  `aarch64-none-linux-android24`.
- Compilador observado: **Clang 21.0.0** del NDK **29.0.14206865**.
- Dependencias directas observadas: **libm.so, libdl.so, libc.so** de Android;
  sin glibc Linux ni bibliotecas Windows. El STL del adaptador es estático.
- Segmentos LOAD: alineación mínima **16 KiB**, verificada con `llvm-readelf`.
- Carga y ejecución de la `.so` Android en proceso Android: **no ejecutadas**.
- Control Linux adicional con Godot 4.7.2: **importación, cierre limpio, carga y ocho operaciones satisfactorios** (GCC 13.3.0).
- Exportación APK de laboratorio: **satisfactoria**, sin `ERROR:` del exportador.
  Firma verificada con `apksigner` 36.0.0 (v2 y v3); manifiesto inspeccionado con
  `aapt2` 36.0.0: mínima 24, objetivo 36, `native-code: arm64-v8a`.
- SHA-256 del APK: `c32e3d3cb099b65a3fb460b20df6da36bdb0933e37a719d8f2bec44e7ce65703`.
- El APK incluye la extensión en
  `lib/arm64-v8a/libnimroel_core_lab.android.arm64.so`, idéntica byte a byte a la
  biblioteca generada; todas sus bibliotecas nativas tienen `e_machine=183`.
- Samsung Galaxy Tab S9+: **sin prueba física**.

[Job Android satisfactorio](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39336167034/job/118346083251).
[Artefacto Android y APK](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39336167034/artifacts/12227120807).

El APK incluye también `libgodot_android.so` y `libc++_shared.so` de la plantilla
oficial de Godot; las tres `.so` son AArch64. El adaptador no depende directamente
de ese STL compartido. El inspector compara sus bytes dentro del APK con la `.so`
generada, además de comprobar todos los `e_machine` del paquete.

Evidencias en el artefacto Android: `android-ndk.txt`, `android-clang.txt`,
`android-configure.txt`, `android-build.txt`, `android-CMakeCache.txt`,
`android-link.map`, `android-elf.txt`, `android-binary.json`, `android-export.txt`,
`android-apk.json`, `android-signature.txt`, `android-manifest.txt`. El control Linux mantiene nombres propios `linux-*` y sus
logs Godot; no se confunde con ejecución Android.

## Incidencias y correcciones

1. [Primera ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39332709323),
   commit `1531f2e0`: falla godot-cpp en ambas plataformas porque su unidad
   `src/core/print_string.cpp` incluye `godot_cpp/classes/os.hpp`, que no generaba
   el perfil reducido. CoreRPG sí se compiló. Corrección: añadir `OS` al perfil,
   sin parchear godot-cpp ni CoreRPG. Commit `afcd8291`.
2. En la misma corrección se fija el toolset MSVC `14.44.35207`, observado en el
   runner, para no depender de la selección predeterminada de Visual Studio.
3. [Segunda ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39332926029),
   commit `afcd8291`: las tres bibliotecas se compilan y enlazan en Windows,
   Android y el control Linux. Pasan PE/ELF y dependencias. Sin embargo, la
   importación de Godot termina con `0xC0000005` en Windows y `SIGABRT` en Linux.
   No se cuenta esta ejecución como carga/operación satisfactoria. Se añade un
   control de proyecto vacío y traza nativa para determinar el origen.
4. [Tercera ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39333265966),
   commit `929598c7`: el proyecto vacío importa sin fallo; el laboratorio ejecuta los
   ocho casos y sale con código 0 en Windows y Linux. El error es específico del
   primer cierre del editor con GDExtension, no de la llamada al Core.
   Se identifica la incidencia upstream
   [godot-cpp #2024](https://github.com/godotengine/godot-cpp/issues/2024#issuecomment-5150678579):
   generación diferida de documentación de extensiones durante el primer escaneo.
   Godot `main.cpp` fija `quit_after=1` al procesar `--import`.
   Ensayo de CI `e67cd191`: `--import --quit-after 30 --max-fps 30` pasa en Linux,
   pero no basta en Windows: el contador empieza antes de terminar el primer escaneo.
   No se contabiliza como corrección completa.
5. [Cuarta ejecución de diagnóstico](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39333518759),
   commit `18af8e1b`: el primer import sigue fallando con cierre inmediato; la segunda
   importación bajo gdb sale normalmente al existir ya la caché. No se obtuvo una
   traza de crash en esa segunda importación. Esto coincide con la condición de
   primer escaneo documentada upstream; no se atribuye a gdb una demostración que
   no produjo.
6. [Quinta ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39333684740):
   Linux pasa importación y operación; Windows sigue fallando al cerrar el primer
   import. Android llega a exportar y rechaza la configuración por no habilitar ETC2/ASTC.
   Corrección `433b7f39`: helper de editor que espera `EditorFileSystem.is_scanning()`
   y 30 frames consecutivos sin escaneo (timeout 120 s), con marcador propio y salida
   0 obligatorios; opción `import_etc2_astc=true` reutilizada de Host2D. No se modifica
   ni parchea el motor o el binding, ni se ignoran códigos de error.
7. [Sexta ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39334175178),
   commit `433b7f39`: el helper alcanza su marcador pero el editor aún falla después,
   mientras los ocho casos de CoreRPG siguen pasando. Esto descarta que esperar solo
   el filesystem sincronice el hilo de documentación.
   Corrección `667dcfb2`: `ScriptEditor.goto_help("class_name:RefCounted")`, API pública
   que llama a `EditorHelp::go_to_help` y `_wait_for_thread`, seguida de dos frames para
   procesar callbacks antes de cerrar. Fuente oficial:
   [EditorHelp](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/editor/doc/editor_help.cpp#L3348).
8. [Séptima ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39334544242),
   commit `667dcfb2`: en Windows el proceso editor ya sale con código 0, pero el
   modo `--editor --script` deja recursos auxiliares sin liberar; se rechaza el job
   porque contiene `ERROR:`. Corrección `7505c600`: mover el helper a un `EditorPlugin`
   de laboratorio que usa el árbol normal del editor. Solo actúa con la variable
   `NIM06_IMPORT_ONLY=1`, no cierra sesiones manuales y queda excluido de los paquetes.
   Se mantiene la sincronización pública de documentación, el marcador y salida 0,
   sin aceptar avisos de recursos perdidos como éxito.
9. [Octava ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39334918934),
   commit `7505c600`: ambos jobs pasan. Windows y Linux importan sin errores y
   ejecutan los ocho casos. El APK contiene la extensión ARM64 idéntica a la compilada.
   Auditoría posterior del log: Godot emite `ERROR: No project icon specified` aunque
   exporta con salida 0; usa `apksigner` 36.0.0 de la imagen en vez del 36.1.0 instalado
   adicionalmente. Corrección `7cd522cc`: icono SVG mínimo, instalar build-tools 36.0.0,
   fijar SDK mínimo/objetivo 24/36, comprobar herramienta seleccionada y rechazar
   cualquier `ERROR:` del export. Se añade verificación explícita de firma del APK.
10. [Novena ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39335396808),
    commit `7cd522cc`: vuelve a pasar Windows y el control Linux. El exportador
    rechaza sobrescribir las API mediante opciones `gradle_build/*` sin habilitar
    Gradle. Corrección `d1d0d31e`: dejar esas opciones vacías y comprobar las API
    **24/36 en el manifiesto del APK real con `aapt2` 36.0.0**. Las plantillas exactas
    quedan fijadas por SHA-256; no se introduce una compilación Gradle adicional.
11. [Décima ejecución](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39335755278),
    commit `d1d0d31e`: exportación sin `ERROR:`, firma v2/v3 válida, manifiesto con
    `minSdkVersion:24`, `targetSdkVersion:36` y ABI ARM64. Falla el comprobador porque
    buscaba el nombre antiguo `sdkVersion`. Corrección `4e21a4bd`: leer el campo real
    `minSdkVersion` de `aapt2` 36.0.0, conservando los valores esperados 24/36.
12. Clang informa advertencias `-Wmissing-field-initializers` en CoreRPG
   (`knowledge_internal.hpp` y `visibility.hpp`). No son errores de enlace ni
   incompatibilidades de plataforma. Se conservan visibles y no se modifica el Core.

## Infraestructura y repetición

Se añade un workflow de laboratorio con jobs independientes Windows y Android,
controlados por `Tools/NIM06/native_lab.py`. Se reutilizan Godot Standard,
plantillas y opciones de exportación de Nimroel, con proyecto y paquete Android
propios. Los workflows existentes no compilaban extensiones C++; quedan intactos.
No se copian rutas del MSI ni se necesitan secretos de CoreRPG.

La configuración final del workflow usa `pull_request` y push a `main` con filtros
del laboratorio. La fase de preparación usó temporalmente push a esta rama para
poder compilar antes de crear la Draft. No se escribe en main ni se fusiona para
habilitar CI. Se evita la duplicación de runs por push de rama y PR.

Los artefactos incluyen el proyecto, bibliotecas y evidencias; Android añade el APK.
Retención: 30 días. Los fuentes, scripts, descriptor y presets permanecen en Git;
los binarios generados, cachés y claves de firma temporales están excluidos.

Instrucciones de ejecución y uso de artefactos:
[README del laboratorio](../Game/BridgeCoreRPG/lab/README.md).

## Límites y comprobaciones físicas pendientes

- Windows en Actions no equivale al MSI Raider. En el MSI debe abrirse el proyecto
  de laboratorio con Godot 4.7.2 Standard y comprobarse
  `NIM06_CORE_OPERATION_OK cases=8`, además de una distribución limpia posterior.
- Android: compilar, enlazar y empaquetar no prueban `dlopen`, registro ni ejecución
  en un proceso Android. No se ejecuta un emulador ARM64 ni se presenta un emulador
  x86_64 como prueba de la ABI ARM64.
- En Tab S9+ queda instalar el APK, verificar visualmente el mismo marcador y guardar
  `adb logcat` con la llamada nativa; confirmar ausencia de errores del cargador.
  No se ha probado físicamente ese dispositivo durante esta fase.
- `aapt2` advierte de una referencia opcional a `themed_icon.xml` en los recursos de
  la plantilla Android oficial. Se conserva el aviso; no se modifica la plantilla.
  La firma verifica y el icono principal existe; el aspecto del icono temático queda
  para la prueba física, junto con el resto del paquete.
- No se validan rendimiento, ciclo de vida Android, persistencia, hilos ni el futuro
  contrato de simulación: pertenecen a la implementación funcional de NIM-06.
- Esta preparación no altera la autoridad del Core: Godot solo traduce y presenta.

## Conclusión técnica

**Sí, se puede iniciar NIM-06 funcional con una base técnica razonablemente validada.**
Hay evidencia real de compilación y enlace del Core y del binding en ambos destinos,
de carga y operación en Godot Windows, y de empaquetado correcto de la extensión
ARM64 en un APK firmado. La comprobación adicional en Linux valida el editor anfitrión
de la exportación y no se usa como sustituto de ejecución Android.

La aceptación posterior del puente funcional debe incluir la carga y la operación
reales en la Tab S9+, y confirmar la distribución en el MSI. Esta preparación no
declara superadas esas pruebas ni valida funcionalidades de NIM-06 que aún no existen.
Los cambios se entregan en una PR Draft independiente para revisión humana, sin fusión.

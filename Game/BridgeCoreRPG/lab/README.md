# Laboratorio nativo previo a NIM-06

Preparación técnica aislada. No conecta `Host2D`, no implementa NIM-06 funcional,
no modifica el mundo ni incorpora proveedores externos.

`Godot → CoreRPGLab.parse_core_version(text) → corerpg::SemanticVersion::parse`

El adaptador convierte UTF-8 y traduce el resultado a un `Dictionary`. La aceptación
o rechazo y los componentes numéricos proceden de `src/semantic_version.cpp` de
CoreRPG, compilado y enlazado como biblioteca estática. El código no reproduce su
analizador en Godot. La prueba comprueba tres entradas válidas diferentes y cinco
inválidas, incluido desbordamiento. El mapa de enlace conserva la evidencia de
`SemanticVersion` en la biblioteca final.

## Dependencias y herramientas

- CoreRPG: `4f282863737bcd8f5add401202a9e1064c133672` (main verificado).
- godot-cpp: `e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, etiqueta oficial
  `godot-4.5-stable`, API incluida 4.5, precisión simple. Perfil mínimo `RefCounted` y `OS` (requerido por godot-cpp);
  se compilan el soporte de variantes y las clases necesarias. No se afirma haber
  compilado todas las clases opcionales de Godot.
- Editor y plantillas oficiales **Godot 4.7.2 Standard**, descargados desde
  `godotengine/godot-builds`, con SHA-256 fijados en `Tools/NIM06/native_lab.py`.
- CMake 3.31.6, Ninja 1.11.1.3, Python 3.12.10; acciones fijadas por SHA.
- Windows: runner `windows-2022`, Visual Studio 2022 / MSVC v143 (toolset 14.44.35207), generador x64,
  Release y CRT estático `/MT` común a las tres bibliotecas.
- Android: runner `ubuntu-24.04`, NDK **29.0.14206865**, Clang del NDK,
  toolchain CMake oficial, `arm64-v8a`, `android-24`, `c++_static`.
  JDK Temurin 17.0.15+6, SDK 36 y build-tools 36.0.0 para exportar APK sin Gradle.
  El controlador comprueba el `apksigner` seleccionado, la firma y las API 24/36
  del manifiesto con `aapt2`; el 36.1.0
  de la configuración Gradle upstream no se usa en esta exportación tradicional.
- Los runners hospedados se actualizan: el CMakeCache, el encabezado del job y los
  logs conservan la versión concreta del compilador y de la imagen utilizada.
  Se fijan las dependencias de código y herramientas instaladas; no se promete
  reproducción binaria bit a bit de una imagen de runner cambiante.

No hay etiqueta oficial godot-cpp 4.7.2 en la consulta realizada. Se aplica la
[compatibilidad oficial hacia versiones menores posteriores](https://github.com/godotengine/godot-cpp/tree/e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77#compatibility):
la extensión apunta a la API 4.5 y se prueba con Godot 4.7.2. Por eso el descriptor
usa `compatibility_minimum = "4.5"`; esto no cambia el motor aprobado del proyecto.
No se utiliza `master` ni una dependencia móvil.

El NDK, la API mínima y las versiones de SDK proceden del código oficial de Godot:
[detect.py](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/platform/android/detect.py)
y [config.gradle](https://github.com/godotengine/godot/blob/ed1daf0bf001b61586d9930840f2f1394092c079/platform/android/java/app/config.gradle).

## Ejecución en GitHub Actions

Workflow: `.github/workflows/nim-06-native-lab.yml`. La configuración final se ejecuta
en PR con cambios del laboratorio y en `main` después de una fusión humana, además
de `workflow_dispatch`. Las ejecuciones de preparación enlazadas se lanzaron por
push a la rama aislada; el disparador se ajusta al abrir la Draft para evitar duplicar
compilaciones de una misma revisión mediante push y PR. Los jobs Windows
y Android son independientes. No necesitan secretos de CoreRPG ni rutas del MSI.
Antes de fusionar, puede repetirse la prueba desde **Re-run all jobs** en una de las
ejecuciones enlazadas. La interfaz de `workflow_dispatch` de GitHub requiere que el
workflow esté también en la rama predeterminada; no se fusiona para habilitarla.

El workflow existente de Host2D no compila C++; se mantiene sin cambios. Se reutilizan
Godot Standard, sus plantillas y las opciones de exportación ya usadas por Nimroel,
con un proyecto y un identificador Android propios. El nuevo workflow concentra
solo la compilación nativa; un único controlador Python sirve a ambas plataformas.

Comandos que ejecuta CI, desde la raíz del repositorio:

```sh
python -m pip install cmake==3.31.6 ninja==1.11.1.3
python Tools/NIM06/native_lab.py build --target windows
python Tools/NIM06/native_lab.py smoke
```

En el runner Linux con el SDK/NDK especificado instalado:

```sh
python Tools/NIM06/native_lab.py build --target android
python Tools/NIM06/native_lab.py build --target linux
python Tools/NIM06/native_lab.py smoke
python Tools/NIM06/native_lab.py export-android
```

La importación usa `project/addons/nim06_ci_import/import_lab.gd`, un plugin de
editor habilitado únicamente si el proceso recibe `NIM06_IMPORT_ONLY=1`. Se ejecuta
en el árbol normal del editor; no sustituye su `SceneTree` ni cierra sesiones manuales.
El plugin se excluye de los paquetes exportados. Espera a que
`EditorFileSystem` termine el escaneo y deja procesar 30 frames sin escaneo antes
de cerrar (límite de seguridad 120 segundos). Después abre la ayuda de `RefCounted`
mediante la API pública `ScriptEditor.goto_help`, que espera el hilo de documentación,
y procesa dos frames más para vaciar sus llamadas diferidas. Así se sincroniza la
carga de documentación, que puede continuar después del escaneo. Un cierre inmediato durante el primer escaneo
reproduce el fallo upstream
[godot-cpp #2024](https://github.com/godotengine/godot-cpp/issues/2024).
Un límite global `--quit-after 30` no bastó en Windows, porque empieza a contar
antes de que termine el escaneo. Se exige salida 0, marcador de importación,
ausencia de errores y el resultado de los ocho casos. No se aceptan crashes como éxito.

El control Linux permite cargar la extensión en el editor anfitrión de la exportación.
**No es ejecución de la biblioteca Android**. El APK se firma con una clave temporal
de laboratorio, generada por job y nunca versionada. No es un paquete de producción.

## Verificaciones y artefactos

- Construcción completa del target `CoreRPG` C++20, godot-cpp y la biblioteca compartida.
- Mapa de enlace con símbolos reales de CoreRPG; enlace sin símbolos pendientes en ELF.
- Windows: PE AMD64 `0x8664`, exportación del punto de entrada y listado de dependencias
  con `dumpbin`; rechazo de dependencias dinámicas de runtimes C++ incompatibles.
- Android: ELF64 AArch64 `183`, punto de entrada, lista cerrada de dependencias Android,
  segmentos LOAD con alineación mínima de 16 KiB. El STL C++ queda enlazado estáticamente.
- Carga y llamada a ocho casos desde Godot Windows; control adicional Godot Linux.
- APK: todas sus `.so` deben ser ARM64, y la extensión debe aparecer exactamente en
  `lib/arm64-v8a/libnimroel_core_lab.android.arm64.so`, idéntica byte a byte al resultado
  de compilación. Esto acredita empaquetado, no carga o ejecución en Android.
- Artefactos `NIM06-native-windows-<sha>` y `NIM06-native-android-<sha>` durante 30 días:
  proyecto de laboratorio, bibliotecas, APK Android y evidencias de compilación,
  dependencias, arquitectura, hashes, importación y operación nativa.

Los binarios, cachés y claves no entran en Git. Para probar manualmente, extraer el
artefacto, localizar el proyecto y abrir `project.godot` con Godot 4.7.2 Standard,
o instalar el APK en la tablet. La escena muestra `NIM06_CORE_OPERATION_OK cases=8`
solo si las ocho comprobaciones reales pasan. El script `smoke.gd` devuelve un código
de error si no se registra la clase o falla cualquier resultado.

No se ha automatizado ejecución Android ARM64: un emulador x86_64 no prueba esta ABI.
Quedan para los dispositivos físicos la carga/operación en Tab S9+, y la confirmación
en MSI Raider fuera de CI, incluida la distribución limpia del paquete.

Informe de resultados y ejecuciones: `Docs/NIM-06_PREPARACION_NATIVA.md`.

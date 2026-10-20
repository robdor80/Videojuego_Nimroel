# Guía de pruebas físicas

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

Estas pruebas están **pendientes**. El usuario las ejecutará; no se registran como
superadas por compilar/exportar. Guardar fecha, modelo, versión OS, run/SHA y hashes
junto al resultado y logs. Usar los artefactos del run final de ci-summary.json.

## Windows 11 — MSI Raider

1. Descargar NIM06-functional-windows-<sha> desde Actions y extraerlo completo.
   Localizar Game/Host2D/export. Mantener EXE, console.exe, PCK y DLL en sus rutas
   relativas; no copiar solo el EXE. Comparar hashes con ci-summary.json o el
   windows-package.json del artefacto: `Get-FileHash <archivo> -Algorithm SHA256`.
2. Ejecutar `Nimroel_NIM06_Functional.console.exe`. En Host2D pulsar
   **CoreRPG · prueba nativa**. No requiere abrir el editor ni un servicio de IA.
3. Pulsar **Ejecutar pruebas**: esperar NIM06 FUNCTIONAL PASS, errors vacío y el
   número de checks del informe final (**129**). Recoger stdout y user://nim06-result.json.
4. **Crear mundo técnico** y **Consultar**: cuatro hechos de tres identidades
   conocidas, contención propia en 2; el cuarto ID del mundo no aparece.
5. **Guardar**, **Contener en 3**, **Consultar**: contención referencia 3;
   **Restaurar**, **Consultar**: vuelve a 2. El resto de identidades no cambia.
6. **Cerrar mundo**: consultar devuelve WORLD_NOT_STARTED. Crear mundo y restaurar
   el slot guardado; cerrar el programa, reabrir, crear y restaurar para probar I/O
   entre procesos. No se reejecutan acciones para restaurar.
7. Para un informe automatizado:
   `.\Nimroel_NIM06_Functional.console.exe --headless -- --nim06-self-test > nim06-windows.txt 2>&1`
   Debe salir con código 0 y NIM06_FUNCTIONAL_REPORT ok=true.

Godot guarda user:// bajo %APPDATA%/Godot/app_userdata/<nombre del proyecto>.
Localizar nim06-result.json y core_saves/native_vertical.core. Estos saves completos
son privados del Host: para reportar un fallo compartir primero el JSON técnico y
logs, no el estado de una futura partida con secretos.

## Samsung Galaxy Tab S9+ — Android ARM64

1. Descargar el artefacto NIM06-functional-android-<sha>. Comparar SHA-256 del APK
   con ci-summary.json; no confundir la SO Linux del control con la ARM64 Android.
2. Instalar `Game/Host2D/export/Nimroel_NIM06_Functional.apk`. Opcional con ADB:
   `adb install -r <apk>`. Las claves de debug cambian entre jobs; un conflicto de
   firma requiere guardar datos necesarios y desinstalar la versión de diagnóstico
   anterior antes de instalar. Paquete: org.nimroel.rpg.nim06functional.
3. Limpiar log anterior con `adb logcat -c`, abrir app y entrar a **CoreRPG · prueba
   nativa**. Pulsar **Ejecutar pruebas** y esperar el mismo PASS/ok=true. Confirmar
   que no aparecen errores dlopen, símbolos pendientes ni clase no registrada.
4. Repetir los pasos interactivos 4–6 de Windows con controles táctiles; cerrar
   y reabrir la app entre guardar y restaurar. Probar fondo/reanudación y orientación.
5. Recoger `adb logcat -d -v threadtime > nim06-android-logcat.txt`; anotar versión
   Android, ABI y tamaño de página (`adb shell getprop ro.product.cpu.abilist`,
   `adb shell getconf PAGE_SIZE`). La suite imprime NIM06_FUNCTIONAL_REPORT.
6. En este APK debug puede copiarse el informe con
   `adb shell run-as org.nimroel.rpg.nim06functional find files -name nim06-result.json`
   y luego `adb exec-out run-as <paquete> cat <ruta encontrada>`.

La ejecución física se acepta solo si hay carga real, suite aprobada, acción/vista
autorizada y continuidad después de restaurar. Firma, ABI o presencia de la SO
por sí solas no satisfacen esos puntos. Si falla, conservar log completo, JSON y
paso exacto; no pulsar repetidamente acciones como sustituto de restaurar.

El paquete actualizado conserva el laboratorio técnico de voz NIM05 en Windows;
es opt-in, requiere su proceso local y no es voz NPC. No confundir el WAV generado
en CI con reproducción física del MSI. En Android ese laboratorio sigue deshabilitado.
Usar los artefactos nuevos de 39483287563 y esperar 129 checks, no el paquete antiguo.

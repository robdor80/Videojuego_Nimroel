# Guía de pruebas físicas

Estado vigente: [cierre final y evidencia CI](12_CIERRE_FINAL.md).
Las secciones de CI anteriores conservan sus SHAs y resultados históricos; no acreditan la interfaz corregida.
Pruebas funcionales físicas anteriores: satisfactorias según el propietario en ambos dispositivos.
La interfaz corregida requiere nueva comprobación física.


El propietario ya comunica pruebas funcionales satisfactorias en ambos dispositivos
para la versión anterior: 129/129, cero errores y persistencia entre ejecuciones.
No ha aportado logs, capturas, fecha física ni SHA del paquete; no se inventan.
Esta guía se conserva como procedimiento de reproducción. El pendiente actual es
la interfaz corregida: scroll completo, legibilidad/tacto en pantalla completa y
dividida, controles accesibles y ausencia de solapamientos. Usar los paquetes finales
enlazados en 12, no los hashes históricos de ci-summary.json.

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
Para probar las correcciones visuales usar los artefactos de la ejecución final enlazada en 12.
No hace falta repetir campañas ajenas al scroll y adaptación de pantalla.

# NIM-07 — Auditoría independiente y aceptación técnica de I4

**Fecha:** 27 de octubre de 2026. **Proyecto:** Nimroel RPG. **Rama auditada:** `feat/nim-07-first-rpg-experience`.

**HEAD de entrega:** `02a34ade056f66d1aa679a18096105f5e7c3bcd7`. **Commit del código ejecutado en CI y de los paquetes:** `024121dca46c044f9539ebfbab6b177c6fb82a03`. **Base anterior:** `9f7e7dc2fdf6fa01085eb78f4e0103d7a41c8bb1`.

## 1. Dictamen

**I4 ACEPTADO TÉCNICAMENTE, condicionado al cierre posterior de NIM-07.** La evidencia obtenida satisface el requisito principal: un save V001 contiene un snapshot CoreRPG autenticado contra la publicación instalada, persistido en disco y recuperado en **un segundo proceso diferente**, manteniendo conocimiento alterado, snapshot, RNG, catálogo y cuatro bindings. Las rutas de rechazo conservan la campaña activa y no descargan ni sustituyen contenido.

Esta aceptación **no** implica que NIM-07 esté fusionada, que el APK haya sido ejecutado en la Galaxy Tab S9+ ni que haya pruebas físicas de I4 en el MSI Raider. No hay PR final. El usuario conserva la autorización sobre reconciliación, PR y merge.

## 2. Comprobaciones de código y contratos

### A. Cambios realmente realizados

La comparación `9f7e7dc2...02a34ade` comprende cuatro commits y veinte rutas modificadas/añadidas. Se revisaron el nuevo `Game/Host2D/scripts/v001_save_store.gd`, `core_save_store.gd`, `native_world_controller.gd`, `native_conversation.gd`, `main.gd`, la extensión `native/src/{bridge.cpp,v001.hpp}`, la smoke `nim07_i4_checks.gd`, el driver `Tools/NIM06/native_lab.py` y `Docs/NIM-07/12_RESULTADO_I4.md` con evidencia. No hay cambios en los nueve JSON del Content Pack, las versiones fijadas CMake, `main`, el canon o la política de IA. Se preservan los mecanismos neutros I1/NIM06.

### B. Identidad confiable ANTES de restaurar

`v001.hpp` calcula en el puente los metadatos a partir del pack de nueve archivos ya comprobado con hash fijado de lock y decoders reales CoreRPG. Incluye esquema `1`, ID/versión/contrato V001, SHA-256 de release, conjunto de definiciones y lock, y huella de la receta inicial derivada de los bytes aprobados de `integration-fixture.json`, semilla, observador y versión de bootstrap. Huella de generación: `6ad814ba488e8bc26a9d5d185f530d70f608de34264aef6fe62d3b2d77c063cd`.

`v001_save_store.gd` valida magic `NIMV001\n`, longitud y JSON canónico de metadatos, inventario cerrado, igualdad con valores **instalados**, longitud Core y SHA-256 de la captura **antes** de invocar `restore`. Se documenta correctamente que un SHA no equivale a firma, cifrado o autenticidad frente a modificación maliciosa coordinada. No se accede al estado Core por un proveedor de IA.

### C. Restauración auténtica y transaccional

La nueva operación `CoreRPGHost.prepare_v001_restore` construye un **catálogo verificado sin generar entidades** (cero entidades y bindings, cuatro definiciones) y entrega metadatos del pack original. `native_world_controller._resume_v001` carga/valida en un Host candidato, llama al `CoreRPGHost.restore` ya dotado de `ContentCatalog`, abre una **nueva sesión** del observador autorizado con audiencia `player`, consulta el contexto y **solo entonces** cierra/sustituye el Host previo. Los fallos de envelope, Core o apertura de sesión preservan handles/snapshot anteriores. No hay false fallback al fixture reinicializado, ni permisos de acciones RPG agregados.

### D. Archivo y recuperación

El formato independiente `user://v001_saves/v1/*.nimv001` contiene un solo envelope externo + snapshot Core (máximo 1 050 636 bytes). Usa temporal + flush + verificación/relectura y rotación de backup; comprueba antes de rotar la validez de Core y observador del primario o backup vigente en un Host **aislado**. La restauración de un backup cuando el primario falta se señala; un primario corrupto **no** provoca fallback silencioso: exige «Recuperar copia». Los nombres de slot solo permiten ASCII `A–Z/a–z/0–9/_/-` de 1–32 caracteres. El almacén NIM06 `.core` se mantiene independiente.

**Límite conscientemente documentado:** no se acredita `fsync` o resistencia a pérdidas súbitas de energía, no hay locks entre múltiples instancias y el protocolo no es un sistema general de migración de versiones/packs.

### E. Interfaz

Desde la pantalla principal se puede comenzar una sesión nueva o **reanudar directamente** sin crear previamente el fixture. Dentro de V001 aparecen Guardar, Reanudar y recuperación explícita de backup tras fallo. La UI indica errores sin mostrar snapshots, SHA o rutas. Las consultas I3 conservan su fuente en `CoreRPGSession.context`. El repertorio I1 y las rutas históricas no se convirtieron en mecánicas ficticias.

## 3. Verificación CI independiente y evidencia

Se consultó directamente GitHub API para los runs y sus jobs, y se descargaron y examinaron **los logs originales** de la ejecución final:

- **Run final:** `https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619`, **SUCCESS** sobre `024121dca46c044f9539ebfbab6b177c6fb82a03`.
- **Windows x64**, job `122269401360`: SUCCESS. `NIM07_I4_REPORT`: fase **write 16/16**, PID **6248**; fase **read 97/97**, PID **6024**. El **EXE exportado** también pasó la pareja **write 16/16** PID **6556** → **read 97/97** PID **2104**. Las cuatro salidas comparten SHA del snapshot persistido `274861c8d67d1da117f1a1b58f416b7d5b323d80dc981a9601c2405309090e8d`, distinto del fixture inicial `029eed6f7a4297a4127a7ab56af43ac9a3d3b3f2ea51934c76ca0263a4289245`. Las pruebas de sesión, fallback, corrupción y RNG figuran en la smoke ejecutada. NIM06 **129/129**, I1 **48/48**, I2 **37/37**, I3 **51/51**; Host previos y Python offline satisfactorios.
- **Android ARM64 / control Linux**, job `122269401639`: SUCCESS. Linux ejecutó I4 **113/113** con **dos PIDs 4392 → 4402**, además de I1–I3 y NIM06 correctos. Android compiló .so AArch64, exportó APK firmado, verificó librería, assets e integridad. **NO ejecutó Android en hardware ni emulador**, y el montaje de assets del APK en Linux no sustituye esa prueba.
- Artefacto Windows `12742909763` y Android `12744498215`, sin expirar en la comprobación. Se descargaron ambos ZIP directamente desde GitHub mediante el conector. Comprobación adicional local del auditor: extracción de EXE/PCK/DLL y APK; SHA-256 del PCK Windows `90381d2c1d013aef30340adad19c6f095b47db9f85e239c81c49bc96504dbb5c`, DLL `019be0c2df7291782b30a5aee981a9c0cd8cb9693cf5bf36cdcb86ea9e89e280` y APK `59605354358d1ada8a4950a2129aa945b4a156fd79fc1d3479b08aeba34f49af`, todos coincidentes con el informe. Los ZIP de prueba simplificados de esta conversación conservan **los mismos payloads**; su recompresión no recompila ni cambia binarios.

**Límite de auditoría independiente:** se inspeccionaron fuentes, evidencia y logs CI y se verificaron hashes de artefactos, pero no se ejecutó una compilación o partida adicional en hardware del auditor.

## 4. Pruebas físicas y cierre no cubiertos

1. **Windows 11, MSI Raider GE78 HX:** validación manual I3 14/14 previamente comunicada, **no sustituye I4**. Debe utilizarse el **nuevo paquete I4**, comprobar Guardar → cerrar proceso por completo → abrir nuevo proceso → Reanudar desde la entrada principal → mismos hechos, y segundo guardado. No mezclar .exe/.pck/.dll de distintos commits.
2. **Samsung Galaxy Tab S9+, ARM64:** instalar APK I4, verificar inicio, teclado, Guardar y reanudación tras forzar detención, sin borrar datos. Si cambia la firma de una versión debug anterior, **no desinstalar o borrar datos con partidas que deban conservarse**. Compilar/empacar Android no es prueba física.
3. **Reconciliación Git:** `main` sigue en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9`; `main...NIM07` comparada en la auditoría: NIM07 por delante **22** y detrás **36** commits. El preflight de Codex, `evidence/i4-preflight.json`, muestra cero solapamientos de rutas entre los cambios territoriales de main y los de NIM07 desde la base común; **no garantiza integración semántica**. Requiere autorización para la reconciliación controlada en rama temporal y regresiones del contenido Darovan y NIM07; no hacer rebase/merge/force push automáticamente.
4. **PR/fusión y NIM-08:** pendiente autorización del propietario; no abrir PR final ni fusionar, no dar NIM07 por cerrada, no comenzar NIM08.

## 5. Decisión y siguiente puerta

**I4 técnicamente aceptado.** Siguiente paso autorizado a nivel de preparación: proporcionar los binarios verificados para la **validación física I4** y documentar incidencias de UI sin mezclar versiones. Una vez recopilados los resultados del MSI y de la Tab S9+, solicitar autorización expresa para reconciliar el `main` territorial y pasar regresiones sobre la rama integrada. Después, auditoría de integración, PR y fusión con permiso.

**No se han cambiado `main`, CoreRPG, Content Pack, políticas de IA ni canon durante esta auditoría.**

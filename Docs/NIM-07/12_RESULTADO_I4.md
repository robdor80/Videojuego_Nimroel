# NIM-07 — Resultado I4: guardado y recuperación V001

Fecha: 27/10/2026 UTC. Rama exclusiva: `feat/nim-07-first-rpg-experience`.
Entrada verificada: `9f7e7dc2fdf6fa01085eb78f4e0103d7a41c8bb1`.
**Entrega I4 para auditoría independiente. No cierra NIM-07. Sin PR ni fusión.**

## Implementación y procedencia

- [`1b6345f2`](https://github.com/robdor80/Videojuego_Nimroel/commit/1b6345f2): envelope, escritura segura, candidato con catálogo auténtico, sesiones nuevas y UI.
- [`1d5edee3e3a542e41c1c7edccd2eab6983018695`](https://github.com/robdor80/Videojuego_Nimroel/commit/1d5edee3e3a542e41c1c7edccd2eab6983018695): smoke entre procesos, ejecución desde EXE, regresiones y nombre/versión visible Android. Código inicial de prueba.
- [`024121dca46c044f9539ebfbab6b177c6fb82a03`](https://github.com/robdor80/Videojuego_Nimroel/commit/024121dca46c044f9539ebfbab6b177c6fb82a03): refuerzo de validación Core/observador antes de rotar primario o backup; **SHA final de código compilado**.
- El commit documental posterior añade este informe y evidencia, sin cambiar los paquetes ni repetir CI.

Lecturas previas: hoja de ruta, resultados/auditorías I2 e I3, encargo 11,
controlador/conversación/interfaz/store/pack, puente y publicación original.
Se contrastó `examples/external_content_restore.hpp` de Core fijado: identidad
instalada confiable, comparación externa antes de Persistence y catálogo real.
No se incorpora su cabecera de ejemplo como otra API ni se modifica CoreRPG.

`v001_save_store.gd` añade el envelope; `CoreSaveStore` comparte la restricción de
slots y el patrón temporal/backup. La ruta neutral `.core` y sus contratos siguen
funcionando. El controlador guarda exclusivamente handles, identidad de capacidad,
secuencia y metadatos inmutables; nunca tablas, conocimiento ni otro WorldState.

## Contrato del archivo

Slot visible único `treskal`, ruta `user://v001_saves/v1/treskal.nimv001`.
Los métodos técnicos admiten slots ASCII de 1–32 caracteres `[A-Za-z0-9_-]`;
rechazan traversal, separadores, puntos, Unicode y nombres vacíos. No se usan los
archivos de `user://core_saves/*.core` del laboratorio neutral.

Un paquete contiene, en orden:

| Campo | Codificación / límite |
| --- | --- |
| Magic | Ocho bytes ASCII `NIMV001` + LF |
| Longitud de cabecera | `uint32` little endian, 4 bytes |
| Cabecera externa | JSON UTF-8 canónico, 2–2048 bytes; claves ordenadas, sin espacios, todos los valores son strings |
| Captura | Bytes originales de `CoreRPGHost.capture`, sin conversión ni reinterpretación; 1–1 048 576 bytes |

Máximo de paquete: **1 050 636 bytes**. Se comprueba el tamaño antes de leerlo.
La canonicalización es exactamente `JSON.stringify(metadata, "", true)` de Godot
4.7.2; comparar nuevamente sus bytes con la cabecera rechaza claves duplicadas,
UTF-8 inválido, representaciones alternativas y campos inesperados. El inventario
es cerrado: ocho campos de identidad y dos de integridad.

| Clave de identidad | Valor instalado exigido |
| --- | --- |
| `save_schema` | `"1"` |
| `pack_id` | `nimroel.treskal.villages` |
| `pack_version` | `0.1.0` |
| `content_contract` | `0.1.0` |
| `release_sha256` | `45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af` |
| `definition_set_sha256` | `6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5` |
| `lock_sha256` | `669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370` |
| `generation_context_sha256` | `6ad814ba488e8bc26a9d5d185f530d70f608de34264aef6fe62d3b2d77c063cd` |

Integridad: `core_length` es decimal canónico positivo; `core_sha256` es SHA-256
de la captura completa. Deben coincidir tamaño y checksum antes de `restore`.
Las huellas detectan corrupción e identidad; **no son firmas, cifrado ni defensa
contra un autor que reescriba intencionadamente todo el save y sus checksums**.
No se guardan tokens, sesiones, capabilities, tickets de contexto ni request IDs.

La identidad instalada procede del puente después de verificar los nueve JSON,
el lock fijado por el programa, todas sus huellas y los decoders/ContentCatalog
originales. Nunca se elige contenido de confianza a partir del save. La identidad
compara todas las claves antes de llamar al método nativo `restore`.

## Contexto inicial: entrada exacta y hash

La siguiente cadena ASCII se codifica UTF-8 **sin BOM, con LF y LF final**:

```text
nimroel-v001-generation-context/1
recipe=nim07-v001-bootstrap-1
fixture_sha256=f4911bfca2fb705ecde3c35146239d0db4a64648abf6cee21ce301f542eb692a
world_seed=413001
observer=first-materialized
rng_bootstrap_draws=0
```

SHA-256: `6ad814ba488e8bc26a9d5d185f530d70f608de34264aef6fe62d3b2d77c063cd`.
El puente obtiene la huella del fixture de sus bytes **ya verificados**. Esos bytes
fijan todos los parámetros: `v001-structural-1`, `structural-fixture-1`,
`v001-handoff-0.1`, semilla, población/materialización, región y clases de relación.
`nim07-v001-bootstrap-1` fija el algoritmo y orden de construcción/binding/
conocimiento inicial de I2. Cualquier cambio de receta exige revisión y nueva
versión/huella, no aceptación automática de un hash aportado por el archivo.
No participan el commit Git, el estado mutable ni la tirada de sonda del test.

## Restore transaccional y capacidades

La nueva operación acotada `prepare_v001_restore` reutiliza el verificador y la
construcción de catálogo de I2, con bootstrap deshabilitado. Prepara un Host
candidato con **cero entidades y cero bindings**, catálogo de cuatro definiciones
y metadatos confiables. No crea el fixture para luego hacerlo pasar por una carga.
La smoke comprueba expresamente esta condición.

Tras validar el envelope se llama a `restore` en ese candidato; Core deserializa,
valida y restaura con el `ContentCatalog` autenticado por los pines. Se abre una
sesión nueva `player` del primer observador materializado de la receta (ID 6), sin
permisos de acción; se obtiene su primer contexto. Solo después se cierra el Host
anterior y se publican los nuevos handles. La secuencia del controlador vuelve a
cero; los tickets y las capacidades anteriores no se reutilizan. Un fallo de
contenido, I/O, Core o apertura de sesión descarta el candidato y conserva tanto
los bytes como la capacidad activa anterior. No hay fallback a un fixture nuevo.

La entrada inicial **«Reanudar partida V001 guardada»** permite este flujo sin
iniciar un mundo fresco. «Iniciar V001 de Treskal (fixture estructural)» conserva
el inicio explícito de una experiencia nueva, sin escribir ningún archivo. Dentro
de V001, «Guardar» y «Reanudar» trabajan con el slot indicado; el segundo descarta
los cambios no guardados únicamente cuando la recuperación completa tiene éxito.
Las consultas I3 vuelven a `session.context`; no responden desde el archivo ni
los JSON del pack. La UI recibe textos saneados, sin snapshots, hashes o rutas.

## Escritura, estados de fallo y recuperación

Secuencia síncrona, en el hilo del Host y el mismo directorio:

1. Comprobar el primario existente, o el backup si falta el primario: envelope,
   restore Core y reapertura del observador en un Host verificador aislado. Si
   falla cualquiera de esos pasos, rechazar y conservar todos los archivos.
2. Escribir `.tmp`, `flush`, `close` y releerlo completo con límites, checksum y validación Core/observador aislada.
3. Si existe primario válido, retirar el backup anterior y renombrar primario a
   `.bak`. En cada punto permanece el primario bueno o su copia renombrada.
4. Promover `.tmp` mediante rename al nombre primario. Si falla, intentar devolver
   `.bak` al primario; si también falla, conservar `.bak` y comunicar el error.

| Situación | Comportamiento / código técnico |
| --- | --- |
| Slot inválido | `INVALID_SAVE_SLOT`, sin tocar archivo ni Core |
| Esquema futuro / identidad distinta | `SAVE_SCHEMA_UNSUPPORTED` / `SAVE_CONTENT_INCOMPATIBLE`, sin restore |
| Límite, magic/cabecera, longitud, checksum | `SAVE_LIMIT`, `SAVE_FORMAT`, `SAVE_HEADER`, `SAVE_LENGTH`, `SAVE_CHECKSUM`, sin restore |
| Apertura / lectura | `LOAD_OPEN_FAILED` / `LOAD_READ_FAILED`; preserva sesión |
| Captura Core inválida aunque envelope coherente | `LOAD_REJECTED`; solo el candidato fue restaurado |
| Observador no recuperable | `INVALID_OBSERVER`; no sustituye Host activo |
| Directorio / apertura / escritura temporal | `SAVE_DIRECTORY_FAILED`, `SAVE_OPEN_FAILED`, `SAVE_WRITE_FAILED` |
| Rotación / promoción | `SAVE_BACKUP_FAILED`, `SAVE_COMMIT_FAILED`; este último conserva además `rollback_error` técnico |
| Primario existente inválido/incompatible, incluso checksum coherente pero Core/observador rechazado | `SAVE_EXISTING_INVALID`; no lo rota sobre la copia buena |
| Falta primario y existe `.bak` válido | Recupera esa copia, `recovered_backup=true`, mensaje explícito; no la promueve ni borra |
| Primario corrupto y backup válido | Rechaza; solo «Recuperar copia» carga explícitamente el backup, conservando el primario corrupto |
| `.tmp` parcial | Nunca se carga ni se promociona al reanudar; un guardado posterior válido lo reemplaza |

La UI ofrece «Recuperar copia» tras un error dentro de V001. Si el fallo se produce
en la reanudación inicial, puede abrirse V001 con el botón de inicio y pulsar
«Reanudar» para obtener esa opción; el archivo rechazado nunca se sustituye por
ese inicio. Tras recuperar una copia con primario corrupto, guardar sigue rechazado
hasta conservar/apartar fuera de la aplicación el archivo dañado: no hay reparación
silenciosa ni interfaz de gestión de archivos en I4.

La garantía es frente a fallos observables de I/O y cierres entre renames, con
escritura/verificación completa y última copia buena. Godot no expone aquí `fsync`
de archivo/directorio: **no se promete resistencia a pérdida de energía**. No hay
bloqueo entre dos instancias concurrentes del videojuego; usar una sola instancia
escritora por perfil. No hay migración, nube, varios personajes ni importador de
partidas de otros packs/versiones.

## Pruebas y evidencias

[Evidencia local](evidence/i4-local.json), [preflight/divergencia](evidence/i4-preflight.json).
Godot oficial **4.7.2**, CMake **3.31.6**, Ninja **1.11.1.3**, C++20.
Core `4f282863737bcd8f5add401202a9e1064c133672`, godot-cpp
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, jsoncons
`bcb44594c50c495ee1e690602cdd71455942ad0e`, sin modificaciones.

Una smoke I4, compartida entre lanzador de editor y autoload del EXE, tiene fases
`--nim07-i4-write` y `--nim07-i4-read`. El driver crea almacenamiento temporal
privado para cada pareja y ejecuta **dos procesos OS diferentes**, cerrando el
primero antes de abrir el segundo. El testigo solo vive allí, no se publica ningún
save. No se añaden comandos RPG de mutación a la interfaz del jugador.

La fase de escritura retira de forma privilegiada la contención de la herramienta,
recuerda su ausencia, retira conocimiento de población y consume RNG. Guarda con
el botón real; registra SHA y la siguiente tirada. La segunda ejecución pulsa la
entrada de reanudación fría, comprueba las mismas respuestas I3, captura completa,
cuatro bindings y catálogo, y siguiente tirada idéntica. Después cubre todos los
metadatos, checksum, truncamiento, límite, formato, claves duplicadas/extra,
slots, fallo Core y de reapertura, sesión caducada, permisos, backup, temporal,
fallo de commit y conservación de capacidad/bytes. Comprueba geometría de Guardar/
Reanudar e historial en 1280×720, 800×720 y 640×800; no acredita tacto ni IME físico.

| Local Linux | Resultado |
| --- | --- |
| I4, dos procesos | **113/113**: escritura 16, recuperación/negativos 97 |
| I3 / I2 / I1 | **51/51 / 37/37 / 48/48** |
| NIM-06 | **129/129** |
| NIM01–05 Host, teclado y geometría | PASS |
| Python offline NIM03 / NIM04 / NIM05 | **8/8 / 29/29 / 11/11** |
| Pack original/staging con schemas Core | Nueve archivos idénticos, PASS |

Snapshot inicial del test: `029eed6f7a4297a4127a7ab56af43ac9a3d3b3f2ea51934c76ca0263a4289245`.
Snapshot guardado y recuperado:
`274861c8d67d1da117f1a1b58f416b7d5b323d80dc981a9601c2405309090e8d`.
Esta diferencia y la igualdad posterior prueban que no se regeneró el fixture.
Solo se sustituyen en I2/I3 sus aserciones obsoletas de guardado pendiente por
rechazo de slot inseguro; se conservan sus recuentos y todas las demás pruebas.

Comandos reproducibles:

```sh
python -m pip install cmake==3.31.6 ninja==1.11.1.3 -r Tools/CoreRPG413/requirements.txt
python Tools/NIM06/native_lab.py build --functional --target linux
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
# En Windows, el driver exporta y ejecuta también las dos fases en el EXE:
python Tools/NIM06/native_lab.py export-windows --functional
# En runner Android con SDK/NDK/firma del workflow existente:
python Tools/NIM06/native_lab.py export-android --functional
```

## GitHub Actions y paquetes finales

[40526909619 — **success**](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619),
sobre **`024121dca46c044f9539ebfbab6b177c6fb82a03`**.
[Evidencia permanente](evidence/i4-actions.json): procedencia GitHub, jobs,
reportes, procesos, pins, nueve huellas de contenido y hashes de los ZIP/payloads.
Se descargaron ambos artefactos; sus tamaños/SHA coinciden con los digests de
GitHub. Se contrastaron de nuevo los paquetes con los reportes, la DLL/SO
empaquetada con la compilada, y los nueve assets originales del APK.

| Job | Resultado comprobado |
| --- | --- |
| [Windows x64 — 122269401360](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619/job/122269401360) | DLL PE AMD64 compilada/cargada. I4 **113/113** entre procesos; I3 **51/51**, I2 **37/37**, I1 **48/48**, NIM06 **129/129** y NIM01–05 PASS. EXE exportado ejecuta I4 **113/113** en dos procesos, I3 **51/51**, I2 **37/37**, NIM06 **129/129**. PCK con nueve JSON idénticos; FileAccess/catálogo PASS. |
| [Android ARM64/control Linux — 122269401639](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619/job/122269401639) | SO ELF AArch64, segmentos alineados a ≥16 KiB; APK firmado/exportado SDK24/36, solo ARM64. Biblioteca y nueve assets idénticos al origen. Linux: I4 **113/113** entre procesos, I3 **51/51**, I2 **37/37**, I1 **48/48**, NIM06 **129/129**, NIM01–05 PASS. Assets del APK montados en Linux: catálogo/FileAccess PASS. **Sin ejecución Android física ni emulada.** |

Procesos confirmados para I4 final: local Linux **2623 → 2631**; editor Windows
**6248 → 6024**; **EXE Windows exportado 6556 → 2104**; Linux CI **4392 → 4402**.
Todas las parejas recuperan el mismo SHA de snapshot modificado indicado arriba
y la misma continuidad RNG. Las capacidades se recrean dentro del segundo proceso.

Artefactos finales, retención hasta **26/11/2026**:

- [Windows — 12742909763](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619/artifacts/12742909763): ZIP **37 294 912 bytes**. Usar `Game/Host2D/export/` con EXE, wrapper, PCK y DLL juntos.
- [Android — 12744498215](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40526909619/artifacts/12744498215): ZIP **32 312 287 bytes**. APK en `Game/Host2D/export/Nimroel_NIM06_Functional.apk`.

| Payload final | Bytes | SHA-256 |
| --- | ---: | --- |
| Windows PCK | 202 148 | `90381d2c1d013aef30340adad19c6f095b47db9f85e239c81c49bc96504dbb5c` |
| Windows DLL | 1 741 312 | `019be0c2df7291782b30a5aee981a9c0cd8cb9693cf5bf36cdcb86ea9e89e280` |
| Android APK | 30 785 403 | `59605354358d1ada8a4950a2129aa945b4a156fd79fc1d3479b08aeba34f49af` |
| Android SO | 2 286 696 | `3dddb0e7a978ad26e6c6def38b24197ef47bd4ea5b67a810ede2aba3339bbeb2` |

El EXE oficial conserva su hash de plantilla; el código de esta entrega está en
PCK/extensión. No mover solo el EXE ni mezclar DLL/PCK de otras entregas. La
evidencia incluye también hashes del EXE/wrapper, ZIP y archivo de firma APK.

Primera CI [40525522937 — success](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40525522937)
sobre `1d5edee3`, ambos jobs satisfactorios; [evidencia inicial](evidence/i4-actions-initial.json).
La revisión posterior detectó que un primario con checksum coherente pero Core u
observador inválido no debía rotarse sobre el backup bueno. `024121dc` añade esa
validación aislada y seis comprobaciones; se ejecutó una segunda CI para producir
los paquetes definitivos. No hubo fallos de código en CI ni reintentos de jobs.
Se conservó la matriz existente de dos jobs. El cierre documental no recompila.


## Comprobaciones físicas posteriores del propietario

No se han realizado aquí pruebas físicas nuevas de I4. La aceptación manual I3
comunicada por el propietario no se presenta como prueba I4.

**MSI Raider GE78 HX, Windows x64**

1. Descargar el artefacto Windows de esta entrega y extraerlo completo. Conservar
   EXE, PCK y DLL en sus rutas relativas bajo `Game/Host2D/export/`; ejecutar
   `Nimroel_NIM06_Functional.exe`. El nombre heredado no indica contenido I3.
2. Pulsar «Iniciar V001 de Treskal (fixture estructural)». Consultar `estado`,
   `¿cuántos habitantes hay?` y `¿dónde está la herramienta?`; anotar respuestas.
3. Pulsar **Guardar** y comprobar «Partida V001 guardada». Cerrar completamente
   la aplicación y comprobar en el Administrador de tareas que el EXE ha terminado.
4. Ejecutar nuevamente el mismo EXE y pulsar directamente **Reanudar partida V001
   guardada**, sin iniciar primero el fixture. Comprobar «Partida V001 reanudada»
   y repetir las preguntas: deben coincidir.
5. Repetir Guardar/cerrar/reabrir/reanudar. Dentro de V001, «Reanudar» vuelve al
   último archivo; no equivale al botón de iniciar. Los controles se ocultan al
   pasar a I1/demo y al contraer la entrada por teclado móvil.

El archivo reside en el perfil Godot de la aplicación bajo
`%APPDATA%\Godot\app_userdata\Nimroel RPG — Laboratorio v0.0.1\v001_saves\v1\`.
No depende del directorio del ZIP ni requiere un MSI nuevo. Antes de ensayos
manuales de corrupción, cerrar el EXE y copiar **todo** ese directorio a un lugar
seguro; no editar el único archivo bueno. Un guardado inválido debe dar error y
mantener la sesión activa. «Recuperar copia» debe identificar explícitamente que
se recupera el guardado anterior. CI ya comprueba estas negativas en perfil aislado.

**Samsung Galaxy Tab S9+, Android ARM64**

1. Descargar el artefacto Android, extraer
   `Game/Host2D/export/Nimroel_NIM06_Functional.apk` e instalarlo en la tablet.
   Etiqueta visible **Nimroel V001 I4**, versión `0.0.1-nim07-i4`, código 7,
   paquete conservado `org.nimroel.rpg.nim06functional`.
2. Abrir la aplicación, pulsar «Iniciar V001 de Treskal (fixture estructural)» y
   consultar las mismas frases con teclado táctil o Bluetooth. Ocultar el teclado
   para mostrar los controles de guardado; pulsar **Guardar** y comprobar éxito.
3. Cerrar la aplicación, retirarla de recientes y usar Ajustes → Aplicaciones →
   Nimroel V001 I4 → **Forzar detención** para garantizar el fin del proceso.
   **No** borrar datos/almacenamiento ni desinstalar.
4. Abrirla otra vez y pulsar directamente **Reanudar partida V001 guardada**.
   Repetir consultas y comprobar las respuestas; probar scroll y pantalla dividida.
5. Guardar y repetir el ciclo. Los archivos están en el almacenamiento privado
   persistente de la app (`user://v001_saves/v1/`), no en caché ni junto al APK.

La firma debug temporal de CI puede ser distinta de la del APK I3. Si Android
rechaza una actualización por firma, no desinstalar una versión I4 que tenga
partidas que deban conservarse: guardar antes una copia técnica de los datos y
resolver la instalación de forma controlada. La prueba entre ejecuciones usa el
**mismo APK instalado**, sin reinstalaciones ni borrado de datos. I4 no incluye
exportación/importación de saves ni copias de seguridad del sistema Android.

## Divergencia y plan de reconciliación

Base común `1865fb7fedb616ef7abdffbb195d3698825d4c8a`. `main` observada en
`c12dc6b8162f1f20eb92adb5724714da5d63a7e9`: **36 commits exclusivos**, 55 rutas;
NIM07 tenía **18 exclusivos** al entrar en I4. No hay intersección entre las rutas
cambiadas de ambas ramas desde esa base. Los avances de `main` son documentación,
datos, validadores y workflows territoriales Darovan D12/D.P13; no se han perdido
ni copiado a NIM07. Las listas exactas están en `i4-preflight.json`.

Plan propuesto, **sin ejecutarlo y sujeto a autorización posterior**:

1. Fijar de nuevo los HEAD remotos tras la auditoría y comparar desde la base común.
2. Crear una rama temporal de reconciliación desde NIM07 para conservar la rama
   auditada y preparar una fusión normal, sin rebase ni force push.
3. Revisar el resultado aunque no haya colisiones de archivo: conservar íntegros
   canon, datos y decisiones Darovan; no incorporarlos al fixture ni al pack V001.
4. Ejecutar las regresiones territoriales de `main`, NIM01–07 y exportaciones
   afectadas sobre el resultado integrado real; auditar antes de actualizar NIM07.
5. Solo con aprobación posterior, preparar la PR final. No se abre en esta entrega.

La ausencia de solapamientos reduce riesgo de conflicto textual; no certifica
compatibilidad semántica ni sustituye las comprobaciones tras la reconciliación.

## Integridad, incidencias y límites

No se modifican CoreRPG, godot-cpp, pins, canon, los nueve JSON del pack, política
IA ni NIM05. No se activan Gemini/Sol/Luna, voz ni APIs facturables en V001.
Se preservan modo neutral, demo y diagnósticos históricos, sin invocarlos como
parte de las consultas o la persistencia V001. Sin NPC, desplazamientos, combate,
misiones, percepción espacial ni generación de aldeas.

Incidencia local de infraestructura: dos invocaciones de build se solaparon en el
mismo árbol CMake; se detuvo la duplicada y se completó una compilación secuencial,
seguida de verificación ELF y todas las pruebas. No exigió cambios de dependencias
ni código. La evidencia local corresponde a la biblioteca final verificada.

Pendientes para el cierre de NIM07: auditoría independiente de ChatGPT sobre I4,
prueba física de estos paquetes en MSI/Tab S9+, autorización y validación de la
reconciliación con `main`. **Detenerse aquí; no iniciar NIM08 ni declarar NIM07 cerrada.**

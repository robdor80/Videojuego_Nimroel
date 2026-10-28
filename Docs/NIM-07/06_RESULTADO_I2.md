# NIM-07 — Resultado I2: Treskal V001 real

Fecha: 27/10/2026 UTC. Rama exclusiva: `feat/nim-07-first-rpg-experience`.
Base I1/auditoría conservada: `187ab4a6ed03e45b247c9c03eed1c91a1c55801e`.
**Alcance: I2, fixture estructural con catálogo auténtico. No cierra NIM-07.**
Sin PR ni fusión. I3/I4 y aceptación física permanecen pendientes.

## Implementación y commits

- [`ba5b0531eaacab2725a3c69fd588741b9fb84836`](https://github.com/robdor80/Videojuego_Nimroel/commit/ba5b0531eaacab2725a3c69fd588741b9fb84836): carga verificada, catálogo/binding Core, fixture nativo, presentación principal, smoke y CI. Primera revisión enviada a Actions.
- [`b8987b7cd70d92e069e3540b2ec8078ce6554bcd`](https://github.com/robdor80/Videojuego_Nimroel/commit/b8987b7cd70d92e069e3540b2ec8078ce6554bcd): comparte las mismas 37 comprobaciones entre editor y self-test exportado, mediante `--nim07-i2-self-test`; conserva stdout parcial en timeouts. **SHA final de código/CI**. Sin cambios C++/CMake respecto a la primera revisión.
- El commit documental de cierre añade este informe y evidencia, sin cambiar binarios ni repetir compilaciones por documentación.

`main` remoto se comprobó en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9`
al comenzar. La rama NIM-07 partía de su base histórica; no se rebasa sobre los
cambios ajenos posteriores. No se escribe `main`, otras ramas, CoreRPG, canon,
Content Pack, políticas IA ni otros proyectos.

| Componente | Resultado |
| --- | --- |
| `Tools/NIM07/stage_pack.py` | Preflight offline existente, pin de publicación y staging reproducible de nueve JSON; generado e ignorado por Git |
| `native/src/v001.hpp`, `bridge.cpp` | `initialize_v001` cerrado/privilegiado, SHA-256 nativo, decoders Core, ContentCatalog y bootstrap transaccional |
| CMake nativo | ContentJson y HashingContext solo en puente funcional; laboratorio legado conserva OFF/perfil previo |
| `v001_pack.gd`, controlador | Lectura FileAccess `res://`, bytes acotados hacia C++; sesión de observador anónimo sin permisos de acción |
| conversación/principal | Botón «Iniciar V001 de Treskal (fixture estructural)» en la pantalla existente; conserva acceso I1, maqueta y diagnóstico NIM-06 |
| presets/driver/workflow | Inclusión explícita de JSON; tests I1/I2, comparación de PCK/APK y lectura Godot del contenido exportado |

## Publicación y confianza

Única fuente versionada: `ContentPacks/treskal-villages/pack/`, **sin modificar**.
Identidad `nimroel.treskal.villages`, versión `0.1.0`, Content Contract `0.1.0`.

- Release SHA-256: `45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`.
- Definition set SHA-256: `6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5`.
- Lock completo SHA-256 fijado adicionalmente: `669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370`.

El staging valida schemas Nimroel, referencias, procedencia, huellas y extracción
con las herramientas 4.13 existentes. Con `--core-root` también ejecuta los schemas
Core originales offline; se ejecutó localmente sobre fuente y copia instalada.
CI usa preflight Nimroel sin copiar schemas privados; los decoders nativos ejecutan
los schemas Core embebidos durante el runtime real Windows/Linux.

Se copian exactamente manifiesto, lock, fixture, perfil, procedencia y cuatro
recursos a `res://generated_content/treskal-v001`. No se distribuye Worldbuilding.
El driver hace staging antes de build/import/regresiones/export funcionales.
Un checkout sin staging falla explícitamente; no descarga ni genera contenido.

En runtime, el Host de confianza recorre el directorio con límites (profundidad 3,
24 entradas, nueve archivos), lee bytes con FileAccess y limita cada documento a
64 KiB y el conjunto a 128 KiB. La operación nativa exige exactamente el inventario
aprobado y `PackedByteArray`, comprueba hash del lock y SHA-256 de cada payload,
lee JSON sin BOM/duplicados con Core y decodifica manifiesto/recursos contra sus
schemas reales. `ContentCatalog::create` valida tipos/referencias y cuatro recursos.

El pin del **lock completo** fija el mapa de archivos y ambas huellas de publicación:
aceptar solo esos bytes es más restrictivo que volver a aceptar cualquier documento
que satisfaga los schemas Nimroel. Por eso no se implementa otro motor genérico de
schemas específicos en GDScript/C++; su validez se comprueba offline y su identidad
exacta se exige en runtime. Las huellas no son firmas: la elección de confianza es
el pin del proyecto, no el lock que traiga un pack sustituto. Otra versión requiere
una decisión explícita y cambiar pins; no se acepta automáticamente.

No hay Python, filesystem nativo `res://`, red ni claves en la ruta del videojuego.

## Mundo Core creado y conocimiento

Se reproduce el orden y las operaciones de `tests/nimroel_content_pack_test.cpp`
en CoreRPG fijado. Seed **413001**, tomada del fixture; no se ejecuta la tirada RNG
que el test upstream utiliza solamente como sonda de continuidad.

| ID emitido por Core | Papel técnico | Binding / estructura |
| --- | --- | --- |
| 1 | Agregado de aldea V1 | `models/v1`; población 50, reserva latente 48 |
| 2 | Nodo de servicio | `capabilities/basic-blacksmithing`; contenido en 1 |
| 3 | Nodo de servicio | `capabilities/local-tavern`; contenido en 1 |
| 4 | Frontera exterior abstracta | Sin definición ni asentamiento canónico inventado |
| 5 | Objeto de categoría | `objects/ordinary-agricultural-tool`; contenido en 2 |
| 6 | Primer observador anónimo | Materializado desde 1; sin definición ni ubicación física |
| 7 | Segundo observador anónimo | Materializado desde 1; sin definición ni ubicación física |

Las cuatro definiciones llevan el prefijo `nimroel.treskal.villages:`.
Relaciones Core: `(1, servicio=1, 2)`, `(1, servicio=1, 3)`,
`(1, conexión=2, 4)`, `(6, asociación=3, 1)` y `(7, asociación=3, 1)`.
El resto de la población no recibe IDs; no se crean casas, hogares, profesiones,
horarios, NPC con nombre, mapas ni simulación regional.

`remember` es fiel al test: observador 6 conoce existencia de 1/2/5/6,
definición de 1/2/5, contención de 5, población de 1, ausencia de agregado en 2,
relación de servicio 1→2 y su origen poblacional. El 7 conoce solo existencia de
1/3. **El jugador no conoce 3/4/7 ni la definición de taberna**, aunque el catálogo
real sí contenga esa definición. No se amplía conocimiento al consultar.

## Autoridad, transacción y presentación

Se prepara Campaign y catálogo candidatos, se completa bootstrap y se comprueban
Inspector/Persistence antes de publicar con `Runtime::replace`. Todo fallo conserva
la campaña y capacidades previas; un primer fallo deja Host sin inicializar.
Un éxito invalida sesiones antiguas. El catálogo inmutable está en Campaign mediante
`shared_ptr<const ContentCatalog>`, compartido por copias transaccionales, sin
punteros prestados a payloads Godot ni catálogos colgantes.

GDScript conserva handles y presentación; no almacena entidades, relaciones ni un
segundo WorldState. Cada consulta usa `CoreRPGSession.context`. La IU recibe solo
`status`, texto saneado y `world_mutated:false`; no recibe diagnósticos, bytes,
revisión, RNG, grants ni contexto del segundo observador.

Se mantienen las consultas cerradas I1. Para V001 el formateador admite existencia,
definición, contención, relación, población y origen **solo si están autorizados**;
las traducciones documentales de DefinitionId requieren el hecho de definición y
existencia conocidos. La mera posesión del catálogo no autoriza etiquetas.
Se distinguen ausencia conocida, desconocimiento y truncamiento; las referencias
sin identidad autorizada no se imprimen como IDs. `¿qué veo?` conserva el límite de
percepción visual/espacial. No se habilitan acciones textuales nuevas.

Nodos de servicio no significan edificios ni profesionales; contención no significa
viaje, propiedad o reparación. Los observadores son identidades de prueba, sin
personaje canónico. La pantalla V001 retira el arte provisional, oculta diagnósticos
IA/voz y mantiene la etiqueta **fixture estructural**. No se invoca Gemini, Luna,
Sol ni servicios facturables.

El modo I1 conserva su propia instancia y sesión; volver entre modos no reinicia
la partida de cada modo. Ambos Hosts se liberan al salir de la pantalla.

## Persistencia: preparación limitada de I2

`restore` nativo pasa a Persistence el catálogo verificado ya asociado a Campaign.
La smoke prueba un roundtrip **en memoria**, byte a byte, y caducidad de capacidades.
La ruta neutral anterior sigue funcionando y pasa 129/129 de NIM-06.

Esto no completa continuidad V001: la API privilegiada no compara sidecars de
publicación/contexto original. El controlador rechaza save/load V001 con
`CONTENT_PERSISTENCE_PENDING_I4`; no hay botones nuevos. I4 deberá comparar
metadatos externos antes de leer bytes Core y almacenar todo de forma recuperable,
sin regenerar al cargar. No se declara persistencia entre procesos.

## Verificaciones locales

[Resumen permanente](evidence/i2-local.json). Godot oficial
`4.7.2.stable.official.ed1daf0bf`, CMake 3.31.6, Ninja 1.11.1.3, Linux x86_64.
Core `4f282863737bcd8f5add401202a9e1064c133672`, godot-cpp
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, jsoncons
`bcb44594c50c495ee1e690602cdd71455942ad0e` (el fijado por Core). Sin modificaciones.

| Verificación | Resultado |
| --- | --- |
| Pack original y staging, schemas Core + Nimroel | PASS; nueve archivos idénticos y extracción reproducible |
| Compilación/enlace nativo Linux, ABI/símbolos | PASS; SO 3 401 000 bytes, SHA-256 en JSON de evidencia |
| NIM-06 | **129/129** |
| I1 principal real | **48/48** |
| I1 sin extensión, proyecto temporal separado | **7/7** |
| Única smoke I2, pantalla principal/Core | **37/37** |
| Host NIM01–05, teclado y presentación nativa | PASS |
| Python offline NIM03 / NIM04 / NIM05 | **8/8 + 29/29 + 11/11** |
| PCK real exportado con preset Windows | Nueve payloads idénticos; FileAccess + catálogo nativo PASS en control Linux |
| I2 con `--main-pack` del PCK | **37/37** en editor/runtime Linux; no es ejecución Windows |
| Plantilla Linux oficial con PCK adyacente y self-test explícito | **37/37**, sin editor ni overrides de rutas |
| Diff | `git diff --check` limpio; exclusiones conservadas |

La smoke tiene un único cuerpo (`nim07_i2_checks.gd`), reutilizado por
`nim07_i2_smoke.gd` en editor y por un argumento explícito del autoload existente
en la plantilla exportada; no son dos suites diferentes. La smoke comprueba inicio desde botón principal, catálogo y bindings reales, hechos
filtrados, ausencia conocida, separación del segundo observador, consultas ocultas,
truncamiento, falta de percepción y permisos de acción, integridad de bytes Core/RNG,
fixture por consulta privilegiada de test, fallos hash/versión/archivo ausente/añadido
sin mutación ni invalidación de sesión, primer fallo sin campaña parcial, restore
con catálogo e invalidación, recreación determinista y acceso a I1. También comprueba
geometría del selector en 1280×720, 800×720 y 640×800. No son pruebas de tacto/IME real.

Comandos reproducibles principales:

```sh
python -m pip install cmake==3.31.6 ninja==1.11.1.3 -r Tools/CoreRPG413/requirements.txt
python Tools/NIM07/stage_pack.py --core-root /ruta/a/CoreRPG-fijado
python Tools/CoreRPG413/validate.py --core-root /ruta/a/CoreRPG-fijado
python Tools/CoreRPG413/validate.py --core-root /ruta/a/CoreRPG-fijado --pack Game/Host2D/generated_content/treskal-v001 --installed-only
python Tools/NIM06/native_lab.py build --functional --target linux
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
# En runners respectivos, toolchain y firma temporal existentes:
python Tools/NIM06/native_lab.py build --functional --target windows
python Tools/NIM06/native_lab.py export-windows --functional
python Tools/NIM06/native_lab.py build --functional --target android
python Tools/NIM06/native_lab.py export-android --functional
```

## GitHub Actions, paquetes y consumo

Ejecución final sobre **`b8987b7cd70d92e069e3540b2ec8078ce6554bcd`**:
[40453998709 — success](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709).
[Metadatos, reportes, hashes y primer intento](evidence/i2-actions.json).

| Job | Resultado real |
| --- | --- |
| [Windows x64 — 122022957475](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709/job/122022957475) | **success**; DLL PE AMD64 compilada/cargada; NIM06 **129/129**, I1 **48/48**, I2 **37/37**, Host/regresiones offline; EXE exportado ejecuta NIM06 **129/129** e I2 **37/37**; DLL idéntica y nueve payloads del PCK idénticos al original; lectura FileAccess del PCK + catálogo PASS |
| [Android ARM64/control Linux — 122022957672](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709/job/122022957672) | **success**; SO AArch64/ELF183 y alineación ≥16 KiB; Linux NIM06 **129/129**, I1 **48/48**, I2 **37/37** y regresiones; APK firmado, SDK24/36, solo ARM64, SO idéntica; nueve JSON extraídos del APK idénticos y montados en ZIP para FileAccess + catálogo en Linux. **No ejecución Android** |

El APK distribuye assets individuales; el control toma sus nueve bytes originales,
los monta con rutas `res://` en Godot Linux y ejecuta la verificación nativa.
No se presenta ese control como un PCK Android ni como ejecución del motor Android.
Windows sí ejecuta las 37 comprobaciones dentro del EXE de plantilla exportado.
Los hashes remotos proceden de logs CI, no de una comprobación en dispositivo físico.

Artefactos finales con retención de 30 días, hasta 26/11/2026:

- [Windows — 12711576933](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709/artifacts/12711576933), ZIP **37 238 347 bytes**. En `Game/Host2D/export/`: EXE, wrapper, PCK y DLL. PCK **168 880 bytes**, SHA-256 `8da198d77b4d753bc1ba5475344931553eee1879d090734806b510cfc23e2074`; DLL **1 735 680 bytes**, SHA-256 `9c54ccd4c41bbaa34fb28e6e807f2f112ee94c13b107e8dd8e04899e345f5f93`.
- [Android — 12711812423](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453998709/artifacts/12711812423), ZIP **32 253 331 bytes**. APK `Game/Host2D/export/Nimroel_NIM06_Functional.apk`, SHA-256 `3c2b1e02acb63cd5feba0eeecc08ce04896e9c58497d91768b1abd004d3e1544`; SO **2 281 112 bytes**, SHA-256 `b5485c7e25540ea2f68e7170d3a8abfbef7a1b2e825b5fc7a104c9b9b34bc635`.

Se conservan nombres heredados NIM06, identificados por SHA de ejecución. El EXE
es la plantilla Godot y conserva su hash de I1; el código del Host está en el PCK
y la extensión, cuyos hashes deben acompañar al EXE. El JSON fija también hashes
del wrapper, EXE y ZIP de artefactos. No se publica un MSI nuevo.

ContentJson/jsoncons queda enlazado estáticamente: DLL Windows 1,74 MB, SO Android
2,28 MB y SO Linux CI 3,47 MB. La SO Linux local pasa de 1 101 080 bytes en I1 a
3 401 000 en I2 (aumento aproximado 2,30 MB); no se mezclan hashes entre compiladores.
Los nueve JSON originales suman **17 193 bytes**. No se añadió otra matriz de tests:
se reutilizó el workflow nativo con dos jobs y una smoke de 37 comprobaciones.
Duración final observada: Windows **144 s**, Android/control Linux **180 s**;
API timing: ejecución **183 s**, `billable.total_ms=0` en ambos tipos de runner.
No se han activado servicios IA ni servicios de pago.

Incidencia corregida y conservada en evidencia: el primer run
[40453124859](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40453124859)
sobre `ba5b0531` tuvo Android **success** y Windows **failure** exclusivamente en
el nuevo lanzador I2 empaquetado, tras superar DLL/I1/I2 editor y NIM06 EXE.
La plantilla oficial tiene deshabilitados los overrides de ruta y no selecciona
el test con `--script`; se agotaron 180 s. `b8987b7c` reutiliza un único cuerpo de
pruebas mediante `--nim07-i2-self-test`, siguiendo el patrón NIM06 existente. Se
verificó primero en plantilla Linux oficial con PCK adyacente y después en Windows.
También se conservan salidas parciales ante futuros timeouts. No se cambió C++,
catálogo, pins ni contenido para resolverlo. La segunda CI completa valida el
lanzador corregido y el APK final; no se repite CI por el cierre documental.

## Limitaciones y siguiente auditoría

- Sin ejecución física nueva en Windows/MSI ni Galaxy Tab S9+. El APK se compila,
  firma y verifica; el control Linux de sus assets no ejecuta Android.
- Sin generador procedural, percepción, recorrido, diálogos NPC, profesiones,
  propiedad/reparación de herramienta, combate o misión.
- I3: interpretación/presentación ampliada y acciones semánticamente soportadas,
  exclusivamente después de auditoría independiente. I2 conserva las consultas I1.
- I4: metadatos externos de compatibilidad y continuidad entre reinicios.
- Sin API nueva en CoreRPG ni bloqueos de canon detectados. El siguiente paso es
  auditar I2; no se inicia I3/I4 ni se abre PR final.

# NIM-07 — Resultado I3: consultas en lenguaje natural

Fecha: 27/10/2026, Europe/Madrid. Rama exclusiva: `feat/nim-07-first-rpg-experience`.
Base aceptada: `7321fa811a7f4558fe8c04747d22f3843cefcfc0`.
**Entrega limitada a I3, pendiente de auditoría independiente. No cierra NIM-07.**

## Implementación

Código publicado en [`c5c2cb521b865d54d4953de22bf26ed0b7605837`](https://github.com/robdor80/Videojuego_Nimroel/commit/c5c2cb521b865d54d4953de22bf26ed0b7605837).
El commit documental posterior incorpora este informe y evidencia; no recompila.

La entrada y los bocadillos de la pantalla principal reciben ahora consultas
concretas sobre el conocimiento del observador V001. `native_conversation.gd`
reconoce frases completas mediante una tabla cerrada y produce respuestas
enfocadas. No utiliza regex de extracción, modelos, red ni proveedores de IA.
El resumen inicial y `estado` usan también la presentación comprensible.
La UI mantiene la etiqueta **fixture estructural**, al observador anónimo y la
separación de la prueba neutral I1, demo y diagnóstico nativo.

`CoreRPGSession.context` sigue siendo la única fuente de hechos. El presentador
reutiliza las validaciones de I2: API y contrato de contexto **1**, audiencia
`player`, estados de completitud admitidos, límites de tamaño, tipos de hechos y
procedencia `remembered`/`temporary_grant`. El formateador técnico de I1/I2 se
conserva; no se imprime su salida técnica en las respuestas naturales V001.

Las etiquetas documentales de definiciones solo se aplican cuando el contexto
acredita **existencia y definición** del mismo sujeto. Las relaciones no conceden
por sí solas una etiqueta ni suplen una definición desconocida. No se consulta
el catálogo privilegiado ni los JSON del pack para responder. No se conservan
hechos entre turnos. El controlador retiene únicamente el ID de observador
devuelto por el bootstrap nativo como identidad ligada a su capacidad; el origen
exige además el hecho de tipo 6 para ese sujeto. No se usa el número 6, ni otro
ID fijo, para inferir hechos en el código de respuestas.

## Repertorio completo de entrada

Se admiten mayúsculas/minúsculas, vocales con/sin tilde, `ü/u`, signos de pregunta
opcionales, espacios exteriores y varios espacios ordinarios entre palabras.
Tras esa normalización, debe coincidir **la frase completa**; no se interpretan
órdenes compuestas ni entidades extraídas de texto libre.

| Consulta | Frases admitidas |
| --- | --- |
| Resumen | `estado`, `¿qué sé?`, `¿qué conozco?`, `¿qué sabe mi personaje?` |
| Aldea | `¿qué sé de la aldea?`, `¿qué conozco de la aldea?`, `¿qué conozco de esta aldea?`, `¿qué conozco de este lugar?` |
| Servicios | `¿qué servicios conozco?` |
| Herrería | `¿qué sé de la herrería?`, `¿qué conozco de la herrería?` |
| Población | `¿cuántos habitantes hay?`, `¿qué población conozco?` |
| Herramienta | `¿qué sé de la herramienta?`, `¿qué conozco de la herramienta?`, `¿dónde está la herramienta?` |
| Origen | `¿de dónde procede mi personaje?`, `¿cuál es el origen de mi personaje?` |
| Ayuda | `¿qué puedo preguntar?`, `ayuda` |
| Límite de percepción | `¿qué veo?`, `¿qué veo desde donde estoy?` |
| Límite de posición | `¿dónde estoy?` |
| Acción no implementada | `voy a la herrería`, `hablo con el herrero`, `reparo la herramienta`, `reparar herramienta` |

El resto recibe «Consulta no soportada» y la ayuda. Las solicitudes de acción
anteriores explican que esa acción RPG no está implementada; jamás se envían a
`submit`. Las entradas vacías o de más de 1500 caracteres siguen rechazándose.
La ruta neutral I1 conserva su repertorio y presentación previos.

## Ejemplos y fundamento Core

Los números de tipo son los del contrato nativo fijado, no una ontología nueva.

| Pregunta | Respuesta inicial representativa | Hechos exigidos |
| --- | --- | --- |
| Aldea | «Conoces el modelo de aldea V1 agrícola-maderera.» | Existencia (1) y definición (2) autorizadas `models/v1` |
| Servicios | «Conoces una capacidad de herrería básica asociada a la aldea como servicio.» | Existencia/definición de ambos extremos y relación (4), clase 1 |
| Herrería | Además informa de la ausencia conocida de agregado poblacional de esa capacidad. | Población (5), `present=false`; no significa ausencia de profesionales ni edificio |
| Habitantes | «El agregado de aldea conocido declara 50 habitantes y 48 pendientes de materializar.» | Población (5), `total` y `latent` emitidos por Core, nunca constantes de la respuesta |
| Herramienta | «La herramienta está contenida estructuralmente en la capacidad de herrería básica.» | Existencia/definición de herramienta y destino, contención (3) y referencia autorizadas |
| Origen | «El origen poblacional conocido de tu observador de prueba es el agregado de aldea V1 agrícola-maderera.» | Origen (6) del observador ligado a la sesión y definición/existencia del agregado |

Las respuestas añaden los límites necesarios: no ubicación física, propiedad,
recogida/reparación, vivienda ni procedencia biográfica. No aparecen los IDs
técnicos en las respuestas naturales. La herrería es una **capacidad**, sin
atribuirle edificio ni NPC. El repertorio se limita al primer observador V001;
no constituye un buscador general de recursos o capacidades de futuros packs.

Cuando falta el hecho específico se dice que no consta entre lo que conoce ese
observador: no se deduce ausencia del mundo. Un hecho negativo explícito se
presenta como ausencia conocida. Un contexto truncado lo advierte y no se
completa con datos del fixture. Si falta una etiqueta del destino, se conserva
solo la afirmación estructural autorizada, sin imprimir el ID oculto.

## Verificación local

[Evidencia local](evidence/i3-local.json). Windows x64, Godot oficial
`4.7.2.stable.official.ed1daf0bf`. Se reutilizó para la comprobación local la DLL
auténtica del artefacto Windows de I2, SHA-256
`9c54ccd4c41bbaa34fb28e6e807f2f112ee94c13b107e8dd8e04899e345f5f93`,
coincidente con la evidencia aceptada. **No es una nueva compilación local de C++.**
Las Actions de I3 realizan las compilaciones completas con los pines existentes.

| Verificación | Resultado |
| --- | --- |
| I3, entrada real de la pantalla principal/Core | **51/51** |
| I1, pantalla/sesión neutral | **48/48** |
| I2, pack, catálogo, aislamiento y transacciones | **37/37** |
| NIM-06 | **129/129** |
| NIM-01–05 Host, teclado y disposición nativa | PASS |
| Regresiones offline Python NIM03/NIM04/NIM05 | **8/8 + 29/29 + 11/11** |
| Staging de publicación | Nueve archivos idénticos; pin de release conservado |
| `git diff --check` | Limpio |

Una sola smoke I3, `nim07_i3_checks.gd`, se comparte entre el lanzador de editor
y el argumento explícito `--nim07-i3-self-test` del EXE exportado, siguiendo el
arreglo aceptado de I2. No se utiliza `--script` para seleccionar el test dentro
de la plantilla Windows exportada. No se crea otra pantalla de juego.

Las 51 comprobaciones cubren consultas enfocadas y variantes, ayuda, rechazo de
acciones, desconocimiento de taberna/IDs, percepción y posición no modeladas,
no mutación del mundo/RNG, mismos handles entre turnos y demo/I1/V001, versiones,
audiencia, truncamiento Core, etiquetas sin definición, origen del sujeto
correcto, retiro real de conocimiento de población/definición/contención/origen
y diferenciación de ausencia explícita. Una operación **privilegiada exclusiva
del test** prepara la ausencia de contención; nunca es una acción del jugador.
La sonda de IDs reasignados usa una copia de un contexto real para comprobar que
las etiquetas siguen definiciones y hechos, sin atribuir semántica al número.
Se comprueba también que el guardado V001 continúa bloqueado y salir cierra la
capacidad. No se ejecutan proveedores remotos.

Los únicos cambios de expectativas en I2 son dos aserciones de texto del resumen
(población/ausencia y relación/origen). Conservan su comprobación de los mismos
hechos autorizados y las **37** comprobaciones. I1 y NIM-06 quedan intactos.

Comandos reproducibles sobre extensión disponible:

```powershell
python -m pip install -r Tools/CoreRPG413/requirements.txt
python Tools/NIM07/stage_pack.py
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
```

## GitHub Actions y paquetes

Ejecución de código I3:
[40458842972 — success](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972),
sobre `c5c2cb521b865d54d4953de22bf26ed0b7605837`.
[Evidencia permanente](evidence/i3-actions.json): metadatos GitHub, jobs,
artefactos, reportes, pines y hashes de los paquetes descargados. Ambos jobs
existentes terminaron en **success**, sin reintentos ni nuevas matrices.

| Job | Resultado comprobado |
| --- | --- |
| [Windows x64 — 122038420820](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972/job/122038420820) | Compilación DLL PE AMD64, carga nativa; I3 **51/51**, I1 **48/48**, I2 **37/37**, NIM-06 **129/129** y regresiones Host/Python. EXE exportado: I3 **51/51**, I2 **37/37**, NIM-06 **129/129**. DLL empaquetada idéntica a compilada; nueve JSON del PCK idénticos al pack; lectura FileAccess y catálogo reales correctos. |
| [Android ARM64/control Linux — 122038420476](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972/job/122038420476) | SO ELF AArch64, alineación de segmentos ≥16 KiB; control Linux I3 **51/51**, I1 **48/48**, I2 **37/37**, NIM-06 **129/129** y regresiones. APK ARM64 firmado/exportado; SO idéntica a compilada y nueve JSON idénticos. Assets extraídos montados en Linux: FileAccess y catálogo correctos. **Sin ejecución Android física ni emulada.** |

Artefactos de la ejecución, retención hasta **26/11/2026**:

- [Windows — 12713920984](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972/artifacts/12713920984), ZIP 37 255 956 bytes. En `Game/Host2D/export/`, EXE, wrapper, PCK y DLL. PCK **180 772 bytes**, SHA-256 `f09866be7c2298010845f882a34a2265c75f18fadebc70b0b3bb731abd905fac`; DLL **1 735 680 bytes**, SHA-256 `84a60c90376a57b5d9bbb7194802de4ec6b8735520a55197959db7dcc56270bf`.
- [Android — 12713479484](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972/artifacts/12713479484), ZIP 32 271 058 bytes. APK `Game/Host2D/export/Nimroel_NIM06_Functional.apk`, SHA-256 `c2248440a3eeeacc0cfa3ea65c0369867caeb9710d3e8888421825ef0f457c53`; SO **2 281 112 bytes**, SHA-256 `b5485c7e25540ea2f68e7170d3a8abfbef7a1b2e825b5fc7a104c9b9b34bc635`.

Se conservaron los nombres de paquete heredados NIM06; se identifican por el SHA
de esta ejecución. No se genera MSI nuevo. El EXE es la plantilla Godot: el código
del Host se distribuye en PCK y extensión, por lo que deben acompañarlo. Se
descargaron ambos artefactos y se contrastaron de nuevo los hashes de sus paquetes
con los reportes CI; no es una prueba física. La evidencia recoge también las
huellas del EXE/wrapper y las nueve huellas del contenido de cada plataforma.
El cierre documental no cambia binarios ni provoca otra compilación.

## Integridad y límites de entrega

No se cambian CoreRPG, C++, CMake, versiones fijadas, catálogo, definiciones,
Content Pack, canon ni política IA. El pack mantiene sus nueve archivos y release
SHA-256 `45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`.
Las evidencias incluyen las nueve huellas. No se ha escrito `main`, hecho rebase,
abierto PR ni fusionado la rama. Sin activación de Gemini, Sol, Luna, voz o APIs
facturables en V001.

No se implementan desplazamiento, percepción, edificios, profesiones, diálogos,
NPC, misión, generación de aldea ni acciones RPG. El `submit` estructural ya
existente no se anuncia como esas mecánicas; V001 conserva sus permisos de acción
deshabilitados. Harán falta contratos semánticos y conocimiento autorizado para
interacciones RPG reales; no se simulan como parte de I3 ni se prometen para I4.

I4 sigue pendiente: metadatos externos de pack/contexto inicial, consistencia de
guardado, restore compatible y reapertura sin regenerar el mundo, conforme a los
encargos previos. También queda pendiente reconciliar los avances de `main`
**antes de la PR final**, con regresiones posteriores y auditoría; no durante I3.
La prueba física final en Windows/MSI y Galaxy Tab S9+ no se ha realizado aquí.
Compilar/exportar Android y controlar sus assets en Linux **no ejecuta Android**.

Siguiente paso: auditoría independiente de ChatGPT sobre esta entrega I3.
**No iniciar I4 sin esa auditoría.**

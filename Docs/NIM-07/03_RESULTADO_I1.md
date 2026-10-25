# NIM-07 BUILD — Resultado de I1

Fecha: 25/10/2026 UTC. Rama exclusiva: `feat/nim-07-first-rpg-experience`.
Base conservada: `ee9e192d` (auditoría y encargo existentes).
**Alcance: I1, conversación principal con CoreRPG real y estructura neutra de NIM-06.
No cierra NIM-07 ni integra Treskal/V001.** Sin PR ni fusión.

## Código entregado

| Archivo | Cambio |
| --- | --- |
| `Game/Host2D/scripts/main.gd` | Entrada «Iniciar experiencia CoreRPG (estructura de prueba)» en la misma pantalla principal; turnos nativos en sus bocadillos; indicadores distintos de maqueta e integración antigua bloqueada |
| `Game/Host2D/scripts/native_conversation.gd` | Controlador adyacente de consultas cerradas y formateador que devuelve exclusivamente texto saneado y estado de presentación |
| `Game/Host2D/tests/nim07_smoke.gd` | Única smoke I1, ejecutada sobre la escena principal y las clases nativas reales; opción de control sin extensión |
| `Tools/NIM06/native_lab.py` | Añade esa smoke a las regresiones funcionales existentes, conservando las anteriores |
| `.github/workflows/nim-06-native-lab.yml` | Ejecuta el workflow existente al publicar esta rama; prueba I1 con DLL Windows y control Linux, además del build/export ARM64 existente |

La escena `main.tscn` ya construye la IU desde `main.gd`: no fue necesario cambiar
el recurso ni crear otra pantalla. El diagnóstico nativo de NIM-06 permanece igual.
No se han cambiado C++, CoreRPG, pins, CorePort, WorldController, SaveStore,
InteractionPipeline, pruebas históricas, canon, packs ni política/proveedores IA.

Commits de implementación:

- [`f1fa8647`](https://github.com/robdor80/Videojuego_Nimroel/commit/f1fa8647): conversación principal y smoke.
- [`f4b55c09dde0581d7a7e0980bc8247ff31b835ad`](https://github.com/robdor80/Videojuego_Nimroel/commit/f4b55c09dde0581d7a7e0980bc8247ff31b835ad): incorporación a CI; SHA de código probado por Actions.

## Vida de la sesión y flujo real

1. La pantalla posee un `NativeConversation`, que conserva un único
   `native_world_controller`. No conserva listas de hechos ni copia de WorldState.
2. Al pulsar la entrada nativa por primera vez, llama una vez a `start()` del
   controlador NIM-06. Este crea Host/sesión, prepara las cuatro entidades neutras
   y liga el observador del jugador. El cuarto ID no es conocido por ese observador.
3. Solo tras recibir contexto válido se anuncia CoreRPG conectado. Se retiran el
   fondo y retrato provisionales de la maqueta y se identifica la estructura neutra,
   sin Treskal ni aldea V1. Los controles de proveedores/voz quedan ocultos en este
   modo; no hay llamadas de red en la ruta nueva.
4. Las entradas `estado`, `¿qué sabe mi personaje?` y `¿qué conozco?` llaman a
   `query()` del mismo controlador, que consulta `session.context({api_version:1})`.
   Se admiten mayúsculas, espacios exteriores, signos de pregunta y `que` sin tilde;
   no hay coincidencias por subcadenas ni interpretación libre.
5. El formateador solo interpreta existencia y contención autorizadas. Identifica
   entidades como «entidad estructural técnica #N»; solo muestra una referencia de
   contención si su existencia también está autorizada en la respuesta. Diferencia
   contexto completo/truncado, ausencia explícita y falta de conocimiento. Los
   campos desconocidos no se convierten en afirmaciones de gameplay.
6. La IU recibe únicamente `status`, `reply` y `world_mutated:false`. Nunca recibe
   el envelope nativo completo, diagnósticos, revisión, RNG, context_id, permisos,
   ActionResult, bytes de guardado ni contexto de NPC. El emisor es
   **SISTEMA · CORERPG (PRUEBA ESTRUCTURAL)**.
7. `¿qué veo?` explica que aún no existe percepción visual/espacial y ofrece la
   consulta estructural. Las demás frases explican el límite; vacías o mayores
   de 1500 caracteres se rechazan. Ninguna entrada textual ejecuta acciones.
8. Volver a la maqueta/integración antigua y reactivar la experiencia conserva
   Host y sesión; no se reinicializa por consulta ni por pulsar otra vez la entrada.
   Salir de la pantalla cierra el Host e invalida la sesión. Sin biblioteca nativa,
   la entrada muestra indisponibilidad y no activa ni simula CoreRPG.

Las consultas reutilizan la política de conocimiento explícita del controlador
NIM-06: refrescar mediante Core el conocimiento de contención propia antes de
consultar la sesión. No se deducen posiciones, movimiento, servicios ni NPC desde
esa relación estructural. El contrato antiguo sin sesión conserva
`CORE_NOT_CONNECTED` e `integration_ready=false`.

## Verificación local efectivamente ejecutada

Godot oficial **4.7.2.stable.official.ed1daf0bf**, CMake **3.31.6**, Ninja **1.11.1.3**.
Core fijado `4f282863737bcd8f5add401202a9e1064c133672` y godot-cpp fijado
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77`, sin modificaciones.

```sh
python -m pip install cmake==3.31.6 ninja==1.11.1.3
python Tools/NIM06/native_lab.py build --functional --target linux
python Tools/NIM06/native_lab.py smoke --functional
python Tools/NIM06/native_lab.py regressions --functional
# GODOT: ejecutable oficial 4.7.2 descargado/verificado por el driver anterior.
"$GODOT" --headless --path Game/Host2D --script res://tests/nim07_smoke.gd
# Copia temporal importada del Host, sin native/, .godot/ ni export/ originales:
"$GODOT" --headless --path /workspace/scratch/nim07-without-native \
  --script res://tests/nim07_smoke.gd -- --expect-native-unavailable
git diff --check
```

| Comprobación | Resultado local |
| --- | --- |
| Build/enlace Linux con fuentes fijados, ELF y símbolos | PASS; SO de 1 101 080 bytes; SHA-256 `a2e30e74c5979f0165e86694f420b598dfd1e908888a3dcb2a9dee8021345385` |
| Importación oficial y NIM-06 funcional | **129/129**, cero errores |
| NIM-07 con extensión real | **48/48**, cero errores |
| NIM-07 sin extensión, control separado | **7/7**, cero errores; maqueta disponible y modo nativo inactivo |
| NIM-01–05 Godot, teclado y presentación NIM-06 | PASS |
| Python offline NIM-03 / NIM-04 / NIM-05 | **8/8 + 29/29 + 11/11**, sin APIs IA |
| Diff/alcance | `git diff --check` limpio; sin cambios en las exclusiones anteriores |

[Resumen local permanente](evidence/i1-local.json), separado de la evidencia CI.

La smoke I1 envía consultas mediante la señal del campo de texto principal;
comprueba repetición con los mismos handles y bytes Core/RNG intactos. Una acción
estructural realizada exclusivamente por el test privilegiado comprueba que la
respuesta posterior refleja una consecuencia real, incluso al reactivar el modo.
Prueba exclusión del conocimiento de otro observador, entradas ambiguas/vacías/largas,
truncamiento nativo real, formato desconocido, ausencia conocida y cierre de sesión.
Las variantes sintéticas del formateador son controles negativos, no mundos simulados
usados como prueba de integración.

Se detectó y corrigió desbordamiento de etiquetas de modo/ayuda. La disposición de
entrada y botón pasa en 1280×720, 800×720 y 640×800. Son comprobaciones headless de
geometría Godot, **no pruebas físicas de Windows/Android ni de tacto/teclado real**.
El algoritmo de teclado NIM-05 no cambia; solo se oculta el nuevo botón en modo compacto.
El primer ensayo exploratorio usó por error el alias local `godot` (4.6.3) antes de
importar el descriptor; no cargó la extensión. No se contabiliza como validación:
los resultados anteriores corresponden al ejecutable oficial 4.7.2 y extensión cargada.

## GitHub Actions

Ejecuciones sobre `f4b55c09dde0581d7a7e0980bc8247ff31b835ad`:

- [Workflow nativo Windows + Android/control Linux — 40150161604](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150161604).
- [Regresiones completas NIM-01–05 — 40150167626](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150167626), solicitado mediante `workflow_dispatch` sobre esta misma rama.

Ambos workflows concluyeron en **success**. Evidencia de los logs de Actions y
metadatos de sus artefactos fijados en [i1-actions.json](evidence/i1-actions.json).

| Job | Resultado verificado |
| --- | --- |
| [Windows nativo — 121039844096](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150161604/job/121039844096) | **success**: DLL compilada/cargada; NIM-06 **129/129**, I1 **48/48**, regresiones previas; exportación EXE y ejecución del self-test NIM-06 empaquetado **129/129**; DLL empaquetada idéntica |
| [Android y control Linux — 121039843952](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150161604/job/121039843952) | **success**: SO ARM64/ELF183 y alineación 16 KiB; control Linux con NIM-06 **129/129**, I1 **48/48** y regresiones; APK firmado/exportado, SDK24/36, solo ARM64 y SO idéntica a la compilada |
| [Godot/regresiones NIM-01–05 — 121039865241](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150167626/job/121039865241) | **success**: importación, contratos, suites offline y teclado |
| [TTS local histórico Windows CI — 121039865442](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150167626/job/121039865442) | **success**: inferencia sherpa local; sin integración de voz en I1 ni API IA |
| [Exportaciones históricas — 121039924835](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150167626/job/121039924835) | **success**: regresión Windows/Android sin extensión; estos paquetes NIM05 no son la distribución nativa I1 |

Paquetes nativos que incorporan I1, con nombres heredados y retención de 30 días:

- [Windows, artefacto 12582353690](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150161604/artifacts/12582353690): dentro de `Game/Host2D/export/`, EXE + PCK + DLL. SHA-256 del EXE `9f44a61a9589e5dba56aa5001882d681f4ca6cca992ba3a3a24e23aafddf69af`; el JSON de evidencia conserva también hashes del PCK y DLL.
- [Android, artefacto 12581839110](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40150161604/artifacts/12581839110): `Game/Host2D/export/Nimroel_NIM06_Functional.apk`, SHA-256 `8f96862efe11c51e99f15075341836000081b581ba4f9e785617d3a4f8bf3272`. **Sin ejecución física Android**.

La smoke de conversación I1 se ejecutó con el editor/runtime nativo Windows y
Linux; el self-test ejecutado dentro del EXE exportado es el histórico NIM-06.
No se atribuye una prueba física del flujo conversacional a esas exportaciones.
El commit final solo incorpora informe/evidencia: su código es idéntico al SHA CI
anterior y no requiere repetir los builds por cambios exclusivamente documentales.

## Límites y siguiente revisión

El guardado/restauración opcional de I1 se difiere a I4 para mantener este incremento
centrado en consulta y vida de sesión. No se ofrecen botones que hagan creer que el
historial o la publicación V001 ya persisten. Los métodos históricos de SaveStore y
WorldController conservan sus pruebas, incluida reapertura con capacidades nuevas.

**Bloqueos técnicos de I1: ninguno observado.** La necesidad de compilar/distribuir
la GDExtension y la falta de pruebas físicas nuevas son límites explícitos, no se
suplen con respuestas simuladas. La validación de dispositivos y el contenido de I2
permanecen pendientes de los encargos siguientes.

Faltan I2–I4 y la aceptación física de los paquetes nuevos. No se reutiliza la
aceptación física 129/129 de NIM-06 como prueba de NIM-07. Los nombres heredados
NIM06 de los artefactos/exportaciones del workflow se conservan; el SHA de la
ejecución identifica qué paquete incorpora I1.

Recomendación para I2, después de revisar esta entrega: resolver exclusivamente el
puente de ContentCatalog/ContentJson y binding verificado de definiciones descrito
en la auditoría. Hasta entonces, no atribuir a estos IDs la aldea V1, servicios,
profesiones, edificios o personajes de Treskal. No se ha iniciado ese trabajo,
modificado CoreRPG ni activado IA. `main` y las demás ramas no se han escrito.

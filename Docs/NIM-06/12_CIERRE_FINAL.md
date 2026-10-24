# NIM-06 — Cierre final de GDExtension

Fecha del informe: 24/10/2026 (Europe/Madrid). PR [#27](https://github.com/robdor80/Videojuego_Nimroel/pull/27),
rama `feat/nim-06-functional-gdextension`. PR abierta y en borrador; no fusionada.
Godot **4.7.2 Standard**, presentación 2D. CoreRPG sigue siendo la autoridad exclusiva.

## Pruebas físicas comunicadas por el propietario

| Dispositivo | Resultado comunicado de la versión anterior |
| --- | --- |
| MSI Raider — Windows 11 | Inicio y GDExtension operativos; 129/129, cero errores; consultas autorizadas, acciones aceptadas, guardar/restaurar, persistencia después de cerrar/reabrir y no_change esperado |
| Samsung Galaxy Tab S9+ — Android ARM64 | APK instalado/ejecutado y GDExtension cargada; 129/129, cero errores; acciones/consultas/restauración, persistencia entre ejecuciones y no_change esperado |

Ambos: **validación funcional física satisfactoria comunicada por el propietario**.
No son pruebas ejecutadas por este agente ni evidencia automatizada de Actions.
No se aportaron capturas, logs, fecha de ejecución física, hash del paquete, versión
Android ni mediciones. No se atribuyen las pruebas anteriores a la nueva interfaz.

## Incidencias y correcciones de presentación

1. Respuestas JSON largas sin scroll: ScrollContainer vertical independiente,
   envoltura de tokens largos, sin recortar el contenido; cada respuesta comienza
   arriba. Rueda/barra/gesto pan y soporte táctil normal del contenedor de Godot.
2. Texto y controles pequeños en Tab S9+, especialmente en pantalla dividida:
   contenedores que se ajustan a la ventana; escala lógica Android calculada por DPI,
   independiente del ancho. Fuente 18, botones con altura mínima 48 y barras de 24
   unidades lógicas. Las acciones disponen de scroll propio si falta altura;
   resultado y Volver conservan espacio. El lanzador flotante se oculta dentro del
   laboratorio para evitar que cubra el título. Al salir se restaura la escala del Host.

El ajuste se limita a esta pantalla técnica. El controlador y las llamadas existentes
se conservan; no se cambian reglas, autoridad, sesiones, persistencia ni código C++.

## Integración de main y commits

- Entrega anterior: `27ac85c5b0b23186f5ebb99839a59a2aff516c6f`.
- Main recuperado: `028ea86ec69cf2223d0e47b006cbb84554068b91`.
- Merge local: [`c804612d78b60bfac03264b46789a192cb737fb9`](https://github.com/robdor80/Videojuego_Nimroel/commit/c804612d78b60bfac03264b46789a192cb737fb9), sin conflictos, antes de modificar código.
- Correcciones y comprobación visual: [`0479a2da81fd467b793359e1e7b28a91c8b7e32a`](https://github.com/robdor80/Videojuego_Nimroel/commit/0479a2da81fd467b793359e1e7b28a91c8b7e32a).
- El commit documental posterior publicado junto a estos cambios es la cabecera de
  entrega; su SHA y ejecuciones exactas se registran en la [evidencia final permanente](https://github.com/robdor80/Videojuego_Nimroel/pull/27#issuecomment-6384753666).

Los avances Darovan se heredan de main, sin edición de sus archivos o ramas.
La política IA más reciente se hereda de main; no se altera. Comparación tras el
merge: sin diferencias en BridgeCoreRPG, CorePort, CoreSaveStore, Controller,
InteractionPipeline, Tools/NIM03–05 ni Docs/IA. Pins CoreRPG
`4f282863737bcd8f5add401202a9e1064c133672` y godot-cpp
`e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77` conservados.
No hubo force push, reset destructivo, descarte ajeno ni modificación de otra PR.

## Verificación local y resultado real de GitHub Actions

Godot local **4.7.2.stable.official.ed1daf0bf**, descargado mediante el driver y su
SHA-256 ya fijado: `native_layout_smoke.gd` PASS. Cuatro ventanas (1280×720,
640×800, 800×360 y 360×640), JSON de 80 valores y un token de 600 caracteres en
memoria: texto íntegro, token envuelto, última línea alcanzable, rueda/pan sintéticos,
controles accesibles, escala Android completa/dividida y restauración al salir.
No es prueba física táctil de Android. `git diff --check`: sin errores.

Las siguientes insignias muestran el **resultado real servido por GitHub Actions**
para esta rama, sin escribir una conclusión anticipada en Git:

[![CI nativa](https://github.com/robdor80/Videojuego_Nimroel/actions/workflows/nim-06-native-lab.yml/badge.svg?branch=feat%2Fnim-06-functional-gdextension)](https://github.com/robdor80/Videojuego_Nimroel/actions/workflows/nim-06-native-lab.yml?query=branch%3Afeat%2Fnim-06-functional-gdextension)
[![Regresiones NIM01–05](https://github.com/robdor80/Videojuego_Nimroel/actions/workflows/nim-01-host-check.yml/badge.svg?branch=feat%2Fnim-06-functional-gdextension)](https://github.com/robdor80/Videojuego_Nimroel/actions/workflows/nim-01-host-check.yml?query=branch%3Afeat%2Fnim-06-functional-gdextension)

**[Resultados finales fijados por SHA, enlaces directos a ejecuciones, jobs y paquetes](https://github.com/robdor80/Videojuego_Nimroel/pull/27#issuecomment-6384753666).**
Ese comentario permanente de la PR se actualiza al concluir Actions. Las insignias
son vivas; el comentario fija qué ejecución corresponde a esta entrega, incluso si
la rama avanza. Así se publica el informe completo en Git y se evita recompilar todo
solo para añadir después los resultados documentales. El estado histórico anterior
permanece en [ci-summary.json](evidence/ci-summary.json), con su SHA original;
no es evidencia de la interfaz nueva.

Workflows existentes, una ejecución final de cada uno al publicar la entrega:

| Ámbito | Verificación en Actions |
| --- | --- |
| NIM06 Windows x64 | Build/enlace Core y DLL, PE/dependencias, carga Godot y 129 checks existentes; regresiones NIM01–05/teclado + nueva prueba de presentación; EXE exportado ejecutado y DLL idéntica |
| NIM06 Android ARM64 | Build/enlace SO, ELF183/dependencias/LOAD16KiB; control Linux de 129 checks y regresiones; exportación APK, firma/SDK/ABI y SO exacta. El control Linux no es runtime Android |
| NIM01–05 | Godot 4.7.2, seguridad y aislamiento IA/broker, suites Python offline, teclado, exportaciones Windows/Android y TTS real sherpa en Windows CI |

La prueba de presentación se incorpora al comando de regresiones nativo existente,
sin laboratorio nuevo. No se realizan pruebas de carga/estrés, datasets ni pruebas
masivas de ZIP. Solo los paquetes y descargas normales de los workflows.
No se activan llamadas de pago. No se modifica CoreRPG ni se inicia NIM-07.

## Pendiente auténtico y recomendación de fusión

Pendiente del propietario: comprobar **esta nueva interfaz** en Windows y Tab S9+,
en pantalla completa/dividida, desplazando JSON hasta el final y verificando
legibilidad, pulsación, redimensionado y Volver sin solapamientos. No hace falta
repetir campañas ajenas a estas incidencias. La prueba física anterior se conserva.

Recomendación: con los dos workflows finales satisfactorios y la nueva presentación
aceptada físicamente, NIM-06 está preparado para fusión por el propietario. Antes de
esa comprobación visual queda preparado técnicamente, con aceptación visual pendiente.
La decisión y autorización de fusión corresponden exclusivamente al propietario.
Los sistemas RPG futuros y límites anteriores de 02/03/06/08 permanecen fuera del cierre.

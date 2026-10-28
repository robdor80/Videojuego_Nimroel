# NIM-07 BUILD — Auditoría independiente y aceptación técnica de I3

**Fecha:** 27 de octubre de 2026. **Rama:** `feat/nim-07-first-rpg-experience`.
**HEAD recibido y auditado:** `01ea45d9943093a9d23e2e1be3d7177053ca9e09`. **Código ejecutado:** `c5c2cb521b865d54d4953de22bf26ed0b7605837`.

## Decisión

**I3 técnicamente ACEPTADO.** Autorizar la preparación de I4 y su posterior implementación, una vez revisado su encargo. No confundir este hito con juego RPG completo, aceptación física ni cierre de NIM-07.

## Fuentes revisadas de forma independiente

- Comparación de `7321fa811a7f4558fe8c04747d22f3843cefcfc0...01ea45d9943093a9d23e2e1be3d7177053ca9e09`: dos commits, doce rutas modificadas o añadidas, limitadas a interfaz GDScript, pruebas, driver/workflow y evidencia; no cambia C++, CoreRPG, pins de dependencias, Content Pack ni canon.
- `Game/Host2D/scripts/native_conversation.gd`: repertorio explícito `QUERIES`, `normalize_query`, `_submit_v001`, `format_query`; frases completas, sin proveedor ni extracción libre, y conservación de la ruta I1. Presentador valida contexto por `format_context(context, true)` (versión, audiencia jugador, hechos y procedencia), obtiene existencia y DefinitionId conocidos antes de aplicar etiquetas; recupera `session.context` nuevamente por cada turno. Los comandos de acción, visión y ubicación no ejecutan `submit`.
- `Game/Host2D/scripts/native_world_controller.gd` retiene únicamente la identidad del observador autorizado devuelta por `initialize_v001`; no añade un mundo paralelo ni guarda hechos. La interfaz `main.gd` usa el modo V001 existente y conserva las demás rutas.
- `Game/Host2D/tests/nim07_i3_checks.gd`: única smoke, 51 aserciones. Ejercita entrada real por `LineEdit`, consultas, variaciones, separación de audiencias, IDs reasignados, contexto truncado y rechazo de contratos. Retira hechos mediante el Host privilegiado **solo de prueba** y verifica que el texto cambia; diferencia desconocimiento de ausencia explícita mediante mutación real del Core (que no se atribuye al jugador), compara bytes Core antes/después de consultas, revisa sesiones a través de modos y bloqueo del save V001.
- `Docs/NIM-07/09_RESULTADO_I3.md` y `evidence/i3-{local,actions}.json` registran alcance y huellas, sin nueva compilación por commit documental.
- **GitHub Actions:** `https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40458842972`. Metadatos comprobados: run `success` sobre `c5c2cb521b865d54d4953de22bf26ed0b7605837`; jobs `122038420820` Windows y `122038420476` Android/control Linux con conclusión `success`. Logs descargados por el auditor: Windows `NIM07_I3_REPORT` **51/51**, I2 **37/37**, I1 **48/48**, NIM06 **129/129**; el EXE Windows exportado vuelve a ejecutar I3 **51/51**, I2 **37/37**, NIM06 **129/129** y confirma nueve recursos del PCK. Linux control arroja idénticos resultados para las cuatro suites. APK Android ARM64 construido y publicado, binarios/recursos contrastados; **no se ejecutó Android**.
- Artefactos publicados y verificados en metadatos Actions: Windows `12713920984`, Android `12713479484`, para ese mismo código.
- PR de la rama: ninguna. `main` observada en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9`, intacta. Comparación vigente indica rama **16 ahead, 36 behind** respecto de `main`.

## Límites y reservas

1. **Repertorio cerrado**, no NLP libre, diálogo de NPC ni narración con Sol/Luna/Gemini. La pregunta sobre herramienta produce descripción de contención **estructural**, no localización física. No se introducen movimientos, reparación, compras o encargos. «¿Qué veo?» y «¿Dónde estoy?» siguen siendo limitaciones honestas.
2. **Pruebas físicas nuevas NO realizadas** en MSI Windows 11 ni Galaxy Tab S9+. CI de Android demuestra compilación y empaquetado, no ejecución sobre el dispositivo.
3. **Persistencia V001 inhabilitada** con `CONTENT_PERSISTENCE_PENDING_I4`. El guardado neutral NIM06 no se debe modificar ni usar para cargar V001 sin comprobar identidad de contenido.
4. La prueba de 51 aserciones pertenece a la implementación de Codex: se auditaron código, logs y evidencia de CI, pero el auditor **no ejecutó una suite alternativa en hardware**.
5. **Integración con `main` pendiente:** 36 commits nuevos en `main` desde la bifurcación NIM07. Antes de la PR final debe reconciliarse sin pérdida de los cambios territoriales de Darovan y otras fases, y ejecutar regresiones completas tras esa incorporación. Requiere operación controlada y auditoría; no efectuar rebase/fusión automática en esta etapa.

## Próximo incremento

I4: persistencia durable V001 con envoltura de metadatos externos verificados **antes de invocar CoreRPG::Persistence** (identidad y SHA de publicación, huella de contexto inicial); recuperación transaccional sin regenerar el mundo sobre un save válido, invalidación/reemisión de capacidades de sesión, interfaz mínima de guardar/reanudar y pruebas de cierres/reaperturas y corrupción; conservar NIM06 y las suites I1–I3. Después de código/CI, coordinar pruebas físicas y conciliación con `main` antes de cualquier aceptación final.

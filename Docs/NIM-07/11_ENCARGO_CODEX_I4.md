# NIM-07 BUILD — Encargo Codex I4: guardado/reanudación V001 y preparación de cierre

**Fecha:** 27/10/2026. **Rama de implementación obligatoria:** `feat/nim-07-first-rpg-experience`.

**Estado de entrada:** I1, I2 e I3 aceptados técnicamente; I3 auditado en `Docs/NIM-07/10_AUDITORIA_ACEPTACION_I3.md`. Se autoriza el **diseño y desarrollo de I4 sobre esa rama**, no la modificación de `main`, fusión de PR, cambios de canon, de CoreRPG, políticas de IA ni pruebas físicas declaradas ficticiamente.

## 1. Resultado mínimo que debe observar el jugador

Abrir la pantalla principal, entrar en Treskal V001 verificado, consultar su conocimiento con frases de I3, **guardar** la experiencia, cerrar la aplicación, volver a abrirla, **reanudar** la misma experiencia y recuperar los mismos hechos y las capacidades autorizadas. Un fallo o contenido incompatible no debe destruir ni modificar una partida activa ni sustituirla silenciosamente por la aldea inicial. Esta es **persistencia del fixture V001**, no un sistema completo de partidas para cualquier territorio.

## 2. Contratos y lecturas iniciales

Leer, antes de implementar:
- `Docs/NIM-07/01_AUDITORIA_ALCANCE_Y_HOJA_DE_RUTA.md` (especialmente I4 y criterio de aceptación).
- `Docs/NIM-07/06_RESULTADO_I2.md`, `07_AUDITORIA_ACEPTACION_I2.md`, `09_RESULTADO_I3.md`, `10_AUDITORIA_ACEPTACION_I3.md`.
- `Game/Host2D/scripts/core_save_store.gd`, `native_world_controller.gd`, `native_conversation.gd`, `main.gd` y `v001_pack.gd`.
- `Game/BridgeCoreRPG/native/src/{bridge.cpp,v001.hpp}`; `CoreRPG/examples/external_content_restore.hpp` en SHA fijado `4f282863737bcd8f5add401202a9e1064c133672`.
- `ContentPacks/treskal-villages/pack/{content-lock.json,integration-fixture.json,manifest.json}`, **solo lectura**.

Preservar versiones Godot 4.7.2, C++20, CoreRPG y godot-cpp fijados, sin nuevos paquetes online.

## 3. Metadatos externos de identidad, comprobados ANTES del restore

Guardar un contrato versionado y acotado con la captura Core, pero **fuera de sus bytes de persistencia**:
- `pack_id = nimroel.treskal.villages`, `pack_version = 0.1.0`, `content_contract = 0.1.0`.
- `release_sha256 = 45c143a8e997e74617ab5bf9d12245ce3f59e023f7d677c299440d73897808af`.
- `definition_set_sha256 = 6f90b0f7780d2568eb8060e77da6b94d4347e727f0f95e0a31707da7ff0322f5`.
- Huella del lock aprobado `669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370` (defensa adicional).
- **Huella del contexto de generación inicial** obtenida de una receta fijada/versionada y el fixture autorizado (semilla, identificador del fixture, versión de algoritmo/receta, parámetros relevantes); documentar entrada exacta, canonicalización y SHA-256 esperado. No usar como contexto el estado mutable actual, el commit de Git, ni confiar en el hash que aporta el save para validar otro save.
- Versión de esquema de save **del Host** y opcional huella de integridad de la captura Core, límites y longitud.

La instancia *instalada* se deriva de un Content Pack previamente validado con pines propios del programa y configuración técnica de confianza. Nunca aceptar una publicación autodeclarada por el save. Verificar inventario, metadata sintáctica, longitud, checksum y coincidencia exacta de todas las identidades **antes** de llamar `CoreRPGHost.restore`/`CoreRPG::Persistence`. Incompatibilidad = rechazo explícito y estado Core/sesión original inalterados. No añadir una segunda fuente de entidades/acciones en GDScript.

## 4. Durabilidad del archivo y recuperación

Reutilizar, sin romper, el patrón `CoreSaveStore` y sus restricciones de nombres, pero **no reutilizar el archivo `.core` neutral NIM06 sin separar formato**. Elegir almacenamiento versionado V001 y documentarlo. Se prefiere **un único archivo/paquete atómico** que contenga envelope de metadatos externo y bytes Core; evitar dos ficheros independientes susceptibles de quedar desparejados en caída de proceso. Implementar límites de tamaños, lectura parcial, checksum y códigos estables de error; no guardar material sensible ni tokens.

Guardar por temporal + flush/close + promoción mediante rename con recuperación de backup, sin eliminar la última copia buena ante fallos de escritura, truncamiento, incompatibilidad o commit interrumpido. Respetar limitaciones del almacenamiento `user://` en Windows y Android. No declarar resistencia ante pérdida de energía o garantía fsync si Godot no ofrece esas garantías: describir exactamente la durabilidad alcanzada.

Rechazar nombres de slot maliciosos/traversal, datos excesivos, formatos futuros no reconocidos y blobs corruptos; no probar restauración privilegiada antes de verificar compatibilidad. Recuperación de backup explícita/segura cuando corresponda; no reemplazar un primario corrupto en silencio.

## 5. Reanudación y sesiones

`CoreRPGHost` continúa siendo autoridad única. Después de verificar contenido y envelope, restaurar bytes Core **con su ContentCatalog verificado**, creando un nuevo contexto/session `player` para el observador de prueba correcto y sin permisos de acciones. No reutilizar sesiones/capacidades caducadas, IDs de contexto ni request IDs de la partida previa. Nunca presentar como exitosa una restauración si se ha generado simplemente un fixture fresco que se parece al guardado.

Idealmente probar la restauración sobre un Host candidato aislado y sustituir el Host/sesión activo únicamente si TODOS los pasos prosperan. Si esa arquitectura exige un cambio acotado en el bridge, justificarlo y cubrirlo con tests. La preparación del catálogo al cargar no puede sobrescribir el mundo guardado al completar el restore.

Añadir al **modo V001 de la pantalla principal** controles mínimos y claros de `Guardar` y `Reanudar`, con feedback de éxito/error que no exponga snapshots, catálogos, hashes internos o rutas sensibles al jugador. No habilitarlos en modo demo/I1 ni anunciar acciones RPG nuevas. Mantenibilidad de teclado táctil y diferentes resoluciones.

## 6. Pruebas focalizadas (dos procesos reales)

Hacer una sola smoke de I4 con fases de escritura y reanudación **en ejecuciones separadas de Godot**, no únicamente un roundtrip en memoria. En la preparación, se admite una mutación *privilegiada exclusivamente de test* para diferenciar snapshot del fixture inicial; al reabrir, verificar hechos modificados y mismo snapshot Core/RNG, catálogo y bindings. No agregar comandos RPG falsos a la UI.

Pruebas negativas mínimas y deterministas: metadata de release incorrecta, contexto de generación incompatible, save truncado/corrupto, slot inválido, backup/temporal parcial, fallo de restore y conservación de campaña/sesión anterior. Validar que el Host **no invoca restore** si falla un metadato externo; si es observable, instrumentar aserción directa y mantener límites. Probar caducidad de capacidades previas y reemisión segura.

Reutilizar la CI funcional existente, sin nueva matriz masiva:
- I4 focalizada sobre Godot Windows x64 con extensión real y **EXE exportado**; control Linux.
- Regresiones I3 **51/51**, I2 **37/37**, I1 **48/48**, NIM06 **129/129**, y NIM01–05.
- Android ARM64: compilar/enlazar/exportar APK, validar payload GDExtension y nueve archivos V001; **no equivale a ejecutar Android en Tab S9+**.
- Asegurar que no hay cambios al pack original (nueve JSON), a CoreRPG, pins, canon, NIM05 y política IA; ninguna llamada a Sol/Luna/Gemini o servicio facturable.
- Identificar artefactos con el SHA de código final y dejar enlaces a GitHub Actions. Evitar repetir CI por meras ediciones documentales.

## 7. Divergencia `main` — requisito del cierre

Al auditar I3, `main` estaba en `c12dc6b8162f1f20eb92adb5724714da5d63a7e9` y NIM07 tenía **16 ahead / 36 behind**. Antes de PR final, evaluar los cambios de `main` y preparar plan de reconciliación no destructivo, conservando las nuevas fases territoriales (incluida Darovan D.P13). **No fusionar `main` en esta rama ni hacer rebase/force push automáticamente**. Informar del riesgo y de las posibles colisiones para decisión de ChatGPT/propietario. Si se autoriza integración, repetir regresiones sobre el resultado real.

## 8. Entregables

- Código de I4 en `feat/nim-07-first-rpg-experience`, commits pequeños, sin tocar otras ramas.
- `Docs/NIM-07/12_RESULTADO_I4.md`: contrato del envelope y contexto inicial (huellas verificables), estados y fallos de I/O, pruebas y evidencias, pasos físicos exactos Windows y Tab S9+, límites y plan de divergencia con `main`.
- `Docs/NIM-07/evidence/i4-*.json` con reportes resumidos, hashes y procedencia; no adjuntar saves privados ni secretos.
- Tras implementación, **detenerse para auditoría independiente de ChatGPT**. No cerrar NIM-07, fusionar ni abrir PR final antes de la revisión/consentimiento explícito. Si se desea crear PR Draft tras auditoría y reconciliación, solicitarlo aparte.

**Criterio de aceptación:** guardar V001 y reanudarlo desde una nueva ejecución con metadatos externos compatibles y bytes Core restaurados auténticos, mostrando las mismas respuestas I3; rechazar datos incompatibles sin alterar una sesión activa. La aceptación final de NIM07 también exigirá pruebas físicas Windows/MSI y Samsung Tab S9+, más la resolución de divergencia con `main`.

# NIM-07 — Auditoría de aceptación del incremento I1

**Fecha:** 25/10/2026 (España). **Rama revisada:** `feat/nim-07-first-rpg-experience`; HEAD `8b2bdb312a7b10e9218061ae040425d0833eb898`.
**Base main:** `1865fb7fedb616ef7abdffbb195d3698825d4c8a`.

## Dictamen

**I1 aceptado técnicamente.** No se declara completada NIM-07 ni se fusiona una PR. El flujo de conversación principal funciona con la GDExtension y el mundo neutro de NIM-06, con evidencia de runtime Godot Windows/Linux y verificaciones Android de empaquetado. No se ha ejecutado I1 físicamente en MSI o Tab S9+.

## Evidencia contrastada directamente

- Ramas GitHub: `main` permanece en `1865fb7f`, rama I1 en `8b2bdb31`; comparación `main...feat/nim-07-first-rpg-experience`: 7 commits por delante y 0 por detrás.
- Código y contratos: `main.gd` conecta un controlador `native_conversation.gd` desde la pantalla principal; `native_conversation.gd` conserva `native_world_controller` y acepta únicamente consultas estructurales cerradas; `nim07_smoke.gd` ejercita la interfaz principal, dos/tres turnos con la misma sesión, consultas seguras, ocultación de entidad 4 y ausencia de mutaciones.
- Actions sobre **SHA de código** `f4b55c09dde0581d7a7e0980bc8247ff31b835ad`: workflow nativo `40150161604` y regresiones históricas `40150167626`, ambos `success`.
- Evidencia publicada: `Docs/NIM-07/03_RESULTADO_I1.md`, `evidence/i1-actions.json` y `evidence/i1-local.json`: Godot Windows y control Linux con I1 48/48; NIM-06 129/129; Linux local NIM-07 sin extensión 7/7; APK ARM64 firmado/verificado, no ejecutado en dispositivo.
- El EXE exportado se ejecutó para la **prueba NIM-06 de 129 comprobaciones**, no para la conversación I1. No mezclar pruebas de runtime Godot con pruebas de paquete ni CI con aceptación física.
- Diff I1 delimitado: `.github/workflows/nim-06-native-lab.yml`, `Tools/NIM06/native_lab.py`, `Game/Host2D/scripts/main.gd`, nuevo controlador/smoke y documentación/evidencia. Sin edición del C++ nativo, Content Pack, CoreRPG, canon o IA.

## Límites aceptados y riesgos para I2

1. **Todavía no es Treskal**: los IDs 1–4 son neutros, nunca afirmaciones de profesión, NPC, edificio o localización.
2. No hay persistencia entre procesos del flujo I1; el guardado ligado a publicación se reserva a I4, según lo aprobado.
3. La implementación actual presenta existencia/contención; el fixture V001 requiere hechos de **definición, relaciones, población y origen**. Ampliar la presentación SOLO desde contexto autorizado y sin interpretar contención como movimiento.
4. El build del puente incluye `CORERPG_BUILD_CONTENT_JSON OFF` en `Game/BridgeCoreRPG/cmake/dependencies.cmake`. Habilitar la dependencia opcional requiere un ajuste limitado en la ruta nativa de I2, conservando laboratorio/ABI/SHAs previos.
5. El pack está fuera de `Game/Host2D`: preparar transporte empaquetado de bytes de una **única autoridad** (`ContentPacks/treskal-villages/pack`), con hashes verificados y sin copiarlo manualmente como fuente editable secundaria.
6. CoreRPG exige catálogo para restaurar snapshots que contienen vínculos de definiciones. I2 debe preservar el catálogo durante la vida de la sesión y dejar preparada la API de restore; I4 completará comparación de metadatos de publicación y almacenamiento.
7. El fixture de referencia real de CoreRPG tiene 7 entidades (aldea, 2 nodos de servicio, frontera exterior, herramienta y 2 observadores anónimos), no viviendas/NPC ni plano urbano. Los observadores no están ubicados físicamente en la aldea por defecto.
8. Ningún flujo de pago, Gemini, Luna ni Sol debe activarse por I2.

## Decisión de dirección

Proceder a **I2** en la misma rama, sin crear otro laboratorio, sin reescribir CoreRPG y sin probar físicamente hasta que exista versión de fase coherente. Primer paso I2: plan técnico de empaquetado/lector, catálogo y fixture; segundo paso I2: implementación y validación concisas. El próximo encargo está fijado en `Docs/NIM-07/05_ENCARGO_CODEX_I2.md`.

Este documento es una auditoría de fuentes y evidencias, no constituye una prueba adicional.

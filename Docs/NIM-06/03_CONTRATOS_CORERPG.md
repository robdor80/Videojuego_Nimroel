# NIM-06 — Contratos reales y auditoría previa

Auditoría directa del 20 de octubre de 2026, antes de modificar código.
Nimroel main: `6c7ed6a8013b471be0e66dbc4d5bedaeb3541782`, merge PR #26
confirmado por API; CI posterior `39390087228` y regresiones `39390087072`: success.
CoreRPG main: `4f282863737bcd8f5add401202a9e1064c133672`, sin cambios respecto al encargo.
Rama independiente: `feat/nim-06-functional-gdextension`, desde ese main.

PR #22 abierta, `feat/nim-05-build`, `f7c96478e250e74cdd9e42e9cf96b706de555888`.
PR #23 abierta, `docs/nimroel-ai-models-2026-10-17`,
`6fcfbef0050ac4abddfeae313fdfb5bf7bf84c44`. No se modifican sus ramas.
Se evita editar main.gd, provider_diagnostic.gd, las pruebas NIM-04 y el workflow
NIM-01 que también cambian en esos trabajos. La integración añade una escena
propia dentro de Host2D y mantiene las regresiones existentes.

Revisión: todos los archivos de `Game/BridgeCoreRPG/lab`, informe de preparación,
core_port.gd, interaction_pipeline.gd, main.gd, proyecto y pruebas Host2D;
workflows nativos, Host y contenido; cabeceras públicas Core, implementaciones de
ActionEngine/Simulation, contratos Knowledge/Visibility/ContextBuilder/Persistence,
ADR 0004/0007, frontera IA y catálogo/lector ContentJson. El laboratorio solo
expone SemanticVersion; sus ocho casos no prueban ninguna operación de mundo.

Las rutas Core siguientes se refieren al SHA anterior en
https://github.com/robdor80/CoreRPG/tree/4f282863737bcd8f5add401202a9e1064c133672 .

| Capacidad real | Contrato Core | Operación implementada / frontera |
| --- | --- | --- |
| Crear identidades, revisión | include/corerpg/world_state.hpp | Host.initialize / Host.admin; privilegiado |
| Contención y relaciones | action.hpp, src/action.cpp | Host.step; Session.submit contención propia con actor implícito y permisos explícitos |
| Precondiciones estructurales | rule_check.hpp | Solo solicitudes privilegiadas Host.step |
| Tiradas y streams deterministas | action.hpp, random_streams.hpp | Host.step; no entregar ActionResult a sesiones |
| Paso causal acotado | simulation.hpp, src/simulation.cpp | Host.step, prefijo procesado explícito; sin replay automático |
| Reservas y materialización | entity_structure.hpp, world_state.hpp | Host.admin; sin sprites ni lógica GDScript |
| Aprender/revocar conocimiento | knowledge.hpp, world_state.hpp | Host.admin; no se acepta aprendizaje desde sesión |
| Proyección por observador | visibility.hpp | Session.context, observador fijado por Host |
| Contexto filtrado y acotado | context_builder.hpp | Session.context: hechos, procedencia, ausencia conocida, truncamiento |
| Guardado y restauración mundo+RNG | persistence.hpp, formatos v1/v2/v3 | Host.capture/restore; bytes privilegiados, archivos propiedad Host |
| Inspector | inspector.hpp | No registrado ni expuesto; diagnóstico Host mínimo separado |
| Catálogo, definiciones y ContentJson | content_catalog.hpp, content_json/* | Disponible upstream; integración de contenido aplazada explícitamente |
| SemVer | semantic_version.hpp | Laboratorio conservado como referencia |
| Combate, inventario, diálogo, NPC autónomos, autoridad social, tiempo/cola | No hay contrato ejecutable | No implementado; requiere fases posteriores del Core/juego |

## Decisiones antes del código

Core no autentica ni autoriza actores: ActionRequest.actor es origen, no permiso.
El Host debe conceder operaciones y destinos explícitos; conocer un ID no basta.
Sesiones player podrán actuar solo sobre su propio actor y destinos concedidos.
Sesiones npc/ai serán de consulta: no implementan iniciativa ni proveedores.
No se aceptarán observador, grants, actor, revision ni precondiciones del cliente.

ActionResult, revisión global, snapshots y RNG son privilegiados. Las sesiones
recibirán recibos saneados y deberán regenerar contexto autorizado, nunca
consecuencias crudas. La correlación será opaca y caducará; el binding de revisión
se conservará dentro del Host. Restore/reinicialización/cierre invalidarán sesiones
incluso si coinciden IDs/revisiones. La frontera no aísla scripts hostiles ejecutados
en el mismo proceso: los scripts del Host forman parte de la base de confianza.

ContentJson usa filesystem físico; el contenido APK requiere un lector Host y
catálogo explícito. No es un bloqueo del Core para esta vertical sin definiciones.
Su integración futura se documenta como cobertura no implementada, no se simula.

## Implementación y evidencia final


Estado vigente: [cierre final y evidencia CI](12_CIERRE_FINAL.md).
Las secciones de CI anteriores conservan sus SHAs y resultados históricos; no acreditan la interfaz corregida.
Pruebas funcionales físicas anteriores: satisfactorias según el propietario en ambos dispositivos.
La interfaz corregida requiere nueva comprobación física.


Esquemas cerrados y límites completos: [README nativo](../../Game/BridgeCoreRPG/native/README.md).
La configuración de dependencias se comparte desde Game/BridgeCoreRPG/cmake;
no se modifica código Core ni se importan sus APIs privilegiadas a las sesiones.

Cierre: PR #22 cambió externamente a `469f27f376eacbe44fe0fcb5770ae5984befa5cb`
por merge de main, sin cambios de archivos que colisionen con este trabajo.
La referencia inicial anterior se conserva como evidencia histórica. Main sigue en su referencia inicial. PR #23 avanzó externamente a
`be7806c5a8d661db35dfb417b5244bf684318732` (13:32:16 UTC), reconciliando
NIM-05/política IA. Nueva comparación de archivos sin colisiones. No se escribió
en ninguna de esas ramas.

El puerto final no posee sesión global: cada llamada usa una capacidad explícita.
Se prueba aislamiento también en el Controller GDScript, no solo en C++.

## Actualización posterior: main y NIM-05

La auditoría inicial anterior describe el estado histórico, cuando PR #22 seguía
abierta. Ahora PR #22 está fusionada en main `cd1735b1`, que se ha integrado
en esta rama por autorización del propietario. No cambia ningún contrato Core ni
el adaptador C++; se amplían únicamente pruebas y documentación de compatibilidad.
Estado actual y evidencia nueva: 11 y ci-summary.json. PR #23 sigue fuera de alcance.

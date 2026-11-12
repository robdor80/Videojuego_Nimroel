# NIM-08 P01 — Auditoría, inventario y baseline reproducible

## Captura de estado (12-11-2026)

| Componente | Ref inspeccionada | Hecho comprobado |
| --- | --- | --- |
| Nimroel main | 0130ed95f27d6d450c962fa2557f56b6b569e4a0 | Referencia del código y canon al comenzar NIM-08 |
| Rama de planificación | 40f2df20d72e92810379ed21f04b1ec609df9f4e | Cinco documentos añadidos sobre la misma main (5 ahead, 0 behind); punto de partida de esta rama |
| CoreRPG main (solo lectura) | 76a7b7b485616d8c4994f384a90f123bf333591d | Incluye historia/archivo posteriores, NO asumidos por el juego |
| CoreRPG fijado en Nimroel | 4f282863737bcd8f5add401202a9e1064c133672 | GIT_TAG en Game/BridgeCoreRPG/cmake/dependencies.cmake; no sustituir por HEAD |
| Godot CPP fijado | e83fd0904c13356ed1d4c3d09f8bb9132bdc6b77 | GIT_TAG de la misma fuente; se conserva |
| NIM-07 integración | PR #40, merged=true, closed | Los artefactos I1–I4 están en main. Merge de Git ≠ prueba física de todos los dispositivos |
| V001 fuente | Worldbuilding/.../Casa Valrik/Aldeas/03_Prueba_v0.0.1 | Matriz canónica, encargo opcional y JSON vigentes, sin edición |
| Pack publicado | ContentPacks/treskal-villages/pack/manifest.json | pack_id nimroel.treskal.villages, pack_version 0.1.0, content contract 0.1.0 |

No se encontró archivo AGENTS.md en la enumeración recursiva de main examinada (1946 entradas, respuesta no truncada); se aplican las restricciones expresas del autor y documentos del repositorio. Revalidar si aparece en cambios posteriores.

## Hechos implementados y límites

**IMPLEMENTADO Y VERIFICADO EN EVIDENCIA PREVIA:** NIM-07 I4 proporciona preparación de pack confiable (9 archivos; 4 definiciones), consulta de observador, aldea estructural de 50 residentes declarados, 2 identidades materializadas, 48 latentes sin EntityId, 7 entidades estructurales, y guardado/reanudación mediante envoltorio host NIMV001 + snapshot real Core. La auditoría I4 registró 113/113 (16 escritura + 97 lectura en procesos Windows separados), y la reconciliación registró CI Windows/Android. La PR #40 declara MSI físico probado el 28-10-2026 sobre el paquete I4 previo a reconciliar; **Android físico Samsung Tab S9+ sigue pendiente** en esa evidencia. No se repitieron aquí esos tests.

**ESTRUCTURAL, NO SIMULACIÓN JUGABLE:** Las dos capacidades de servicio son nodos estructurales, no talleres con agentes ni rutas transitables; el objeto está clasificado, no tiene desgaste ni dueño ejecutables. La relación de contención no prueba propiedad o desplazamiento. Las 48 personas latentes no son 48 NPC individuales ya simulados.

**CORE VERIFICADO AL PIN 4f2828:** include/corerpg/action.hpp posee exactamente operaciones PlaceEntity, RemoveContainment, AddRelation, RemoveRelation y StreamRoll. ActionRequest.actor identifica el origen pero NO confiere autorización sobre targets. ActionEngine exige precondiciones, revisión opcional y aislamiento de rechazo; Simulation::step procesa acciones explícitas en orden, no incorpora agenda/reloj ni transacciones de lote. WorldState controla EntityId, contención, relaciones, población, Knowledge. Persistence v1/v2/v3 almacena solo los campos previstos en CampaignSnapshot; NO incorpora como magia layout, derechos, estación, herramienta/condición ni cola de trabajo.

**AUSENTE PARA V001:** parcelas/edificios/puertas/caminos conectados; hogares y composición familiar individual; materialización/actividad de todos los NPC necesarios; ocupaciones; navegación/percepción territorial; herramienta con condición/propiedad/custodia; reloj y scheduler; orden de reparación y recursos; transmisión conocimiento de dominio; orquestador A/B/C; visualización final 2D, restauración de todos estos estados y validación física cruzada.

## Separación de tres tipos de material

1. **Documentación normativa/canon:** Worldbuilding y modelos V1. Define restricciones, no genera entidades por sí sola.
2. **Datos operativos declarativos:** ContentPacks/treskal-villages, authoring/source-lock.json (34 fuentes fijadas en revisión histórica 35c9d22...) y los manifests/schemas actuales. Puede estar cargado sin que exista un simulador del dominio.
3. **Sistema ejecutable:** C++ CoreRPG fijado + Bridge/Host Godot y pruebas nativas. Ningún criterio de mecánica se acredita al redactar un esquema.

## Dependencias compartidas / advertencias

- Reutilizable por Star Trek: identidad, conocimiento, autorización, acciones, tiempo, localización, relaciones, persistencia, auditoría; NIM-08 no cambia el repositorio Star Trek ni CoreRPG.
- CoreRPG HEAD 76a7... no equivale al commit fijado 4f2828...; la existencia de API en HEAD no habilita adoptarla sin permiso de pin/ABI/migración.
- El sobre I4 acepta exclusivamente publicación y receta original de NIM-07; ampliar dominio obliga diseñar almacenamiento transaccional y compatibilidad, no añadir claves a escondidas.
- No presumir firma criptográfica por tener un SHA-256: el Host debe escoger un pack confiable y comprobar bytes.
- NIM-01 exige layout procedural, separación regional/interna y rutas libres sin hotspots obligatorios; Godot es únicamente proyección.
- Políticas de IA en Docs/IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md prevalecen sobre referencias antiguas a Terra. Debe existir flujo local sin API facturable.

## Fuentes puntuales revisadas

- Docs/NIM-07/12_RESULTADO_I4.md y 13_AUDITORIA_ACEPTACION_I4.md; Docs/NIM-07/14_RECONCILIACION_MAIN_Y_AUDITORIA.md; PR #40.
- Game/BridgeCoreRPG/native/src/v001.hpp; Game/Host2D/scripts/core_port.gd y v001_save_store.gd.
- CoreRPG/include/corerpg/{action,simulation,world_state,knowledge,persistence}.hpp en pin actual.
- ContentPacks/treskal-villages/{README.md,pack/manifest.json,authoring/source-lock.json}.
- Worldbuilding/.../Aldeas/01_Modelos/V1_Mixta_maderera_agricola/modelo_v1.md.
- Worldbuilding/.../Aldeas/03_Prueba_v0.0.1/{MATRIZ_ACEPTACION_V001_v0.1.md,ENCARGO_HERRAMIENTA_ROTA_v0.1.md}.
- Docs/NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md; NIMROEL RPG — PROYECTO MAESTRO.pdf (principios generales).

**Auditoría de ejecución actual:** inspección Git y contratos, no compilación C++ ni export Godot ni prueba en dispositivos.

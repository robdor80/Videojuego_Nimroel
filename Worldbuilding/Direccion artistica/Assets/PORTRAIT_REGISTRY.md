# NIMROEL — PORTRAIT REGISTRY

**Estado:** ACTIVE  
**Versión:** 1.0  
**Inicio del registro:** 2026-09-25  
**Ámbito:** todos los retratos aprobados almacenados bajo `Worldbuilding/Direccion artistica/Assets/`

Este documento es la vista humana resumida del registro de diversidad de retratos.

La fuente operativa estructurada es:

`PORTRAIT_REGISTRY.json`

Las reglas obligatorias de consulta y generación están en:

`PORTRAIT_WORKFLOW_RULES.md`

---

## Principio

Cada retrato aprobado representa a **un individuo**, no a un modelo universal de su profesión, sexo, cultura o localización.

El objetivo del registro es impedir que una campaña de generación derive hacia clones o semiclones y ayudar a cubrir de forma progresiva la diversidad permitida por las biblias.

Se pueden repetir características. Lo que se evita es repetir por inercia combinaciones ya sobrerrepresentadas cuando existen alternativas canónicas plausibles.

---

## Convención de archivos

El PNG final y el ZIP del asset deben compartir exactamente el mismo nombre base.

Ejemplo:

- `portrait_treskal_farmer_male_001.png`
- `portrait_treskal_farmer_male_001.zip`

El ZIP debe contener el PNG final y la documentación del asset definida por el workflow vigente.

---

## Retratos aprobados

Actualmente hay **2 retratos aprobados registrados**.

| Asset ID | Localización | Profesión | Sexo | Edad aparente | Rango | Complexión | Cabello | Pérdida de cabello | Vello facial | Rasgo facial / distintivo | Presentación | Pátina |
|---|---|---|---|---:|---|---|---|---|---|---|---:|---|
| `portrait_treskal_farmer_female_001` | Treskal | farmer | female | 44 | adult | robust | dark_ash_brown, tied back, early grey | none | not_applicable | rostro broad-oval, nariz marcada, asimetría sutil, piel curtida | 2 | C |
| `portrait_treskal_farmer_female_002` | Treskal | farmer | female | 19 | young | thin/average | light-medium brown, long loose braid, no grey | none | not_applicable | rostro ovalado estrecho, pecas abundantes, ojos avellana verdosos | 2 | C |

---

## Uso

Antes de generar un retrato nuevo:

1. consultar las biblias visuales vigentes aplicables;
2. consultar `PORTRAIT_REGISTRY.json`;
3. comparar el nuevo retrato con los individuos ya registrados del pool pertinente;
4. identificar rasgos o combinaciones sobrerrepresentadas y huecos de variedad;
5. resolver la apariencia individual **antes** de redactar el prompt final;
6. generar;
7. comprobar anti-clonación;
8. solo después de aprobar el asset, registrar la nueva entrada.

Este registro se actualiza únicamente con retratos aprobados.


---

## Estado de sincronización de binarios

El registro de diversidad se actualiza **inmediatamente después de aprobar el asset y crear/entregar su ZIP local**, aunque el binario todavía no se haya sincronizado al repositorio.

Estados utilizados:

- `local_pending_gitsync` — ZIP creado y entregado para almacenamiento local; aún no confirmado en el repo.
- `synced` — ZIP confirmado en su ruta de Assets dentro del repositorio.

Para `portrait_treskal_farmer_female_001`:

- estado: `local_pending_gitsync`
- ruta prevista: `Worldbuilding/Direccion artistica/Assets/Retratos/Treskal/portrait_treskal_farmer_female_001.zip`
- SHA-256 ZIP local: `697933334b6570c3fdb32eaadd4d506bc4ba2d1b8577aead47227a6ec97163e9`


Para `portrait_treskal_farmer_female_002`:

- estado: `local_pending_gitsync`
- ruta prevista: `Worldbuilding/Direccion artistica/Assets/Retratos/Treskal/portrait_treskal_farmer_female_002.zip`
- edad aparente / búsqueda: ~19 años / franja 17–22
- fondo: agrícola de Treskal, coherente con oficio y localización
- SHA-256 ZIP local: `bd76fdc1bd3969949ea2f1394c02f5c5d1d54614242e0cf6ad29dba48497dd40`

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

- `PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001.png`
- `PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001.zip`

El ZIP debe contener el PNG final y la documentación del asset definida por el workflow vigente.

---

## Retratos aprobados

Actualmente no hay retratos aprobados registrados.

| Asset ID | Localización | Profesión | Sexo | Edad aparente | Rango | Complexión | Cabello | Pérdida de cabello | Vello facial | Rasgo facial / distintivo | Presentación | Pátina |
|---|---|---|---|---:|---|---|---|---|---|---|---:|---|

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

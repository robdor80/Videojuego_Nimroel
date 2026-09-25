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

## Convención de archivos y almacenamiento

El ZIP sigue siendo el paquete de **transferencia ChatGPT → usuario** y comparte el mismo nombre base del asset.

En el repositorio, el formato definitivo es una **carpeta descomprimida por asset**:

```text
portrait_treskal_farmer_male_001/
├── portrait_treskal_farmer_male_001.png
├── portrait_treskal_farmer_male_001_prompt.md
└── portrait_treskal_farmer_male_001_info.md
```

El ZIP no se conserva en GitHub una vez descomprimido y sincronizado.

---

## Retratos aprobados

Actualmente hay **3 retratos aprobados registrados**.

| Asset ID | Localización | Profesión | Sexo | Edad aparente | Rango | Complexión | Cabello | Pérdida de cabello | Vello facial | Rasgo facial / distintivo | Presentación | Pátina |
|---|---|---|---|---:|---|---|---|---|---|---|---:|---|
| `portrait_treskal_farmer_female_001` | Treskal | farmer | female | 44 | adult | robust | dark_ash_brown, tied back, early grey | none | not_applicable | rostro broad-oval, nariz marcada, asimetría sutil, piel curtida | 2 | C |
| `portrait_treskal_farmer_female_002` | Treskal | farmer | female | 19 | young | thin/average | light-medium brown, long loose braid, no grey | none | not_applicable | rostro ovalado estrecho, pecas abundantes, ojos avellana verdosos | 2 | C |
| `portrait_treskal_farmer_female_003` | Treskal | farmer | female | 62 | elderly | thin | grey, gathered under worn headscarf | not_visible | not_applicable | rostro largo y estrecho, envejecimiento marcado, ojos verde-avellana apagados | 2 | C |

---

## Uso

Antes de generar un retrato nuevo:

1. consultar las biblias visuales vigentes aplicables;
   - para cualquier habitante de la zona de Treskal es obligatoria `Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Perfiles locales/Treskal/TRESKAL_PORTRAIT_VISUAL_BIBLE_v0.1.md`;
2. consultar `PORTRAIT_REGISTRY.json`;
3. comparar el nuevo retrato con los individuos ya registrados del pool pertinente;
4. identificar rasgos o combinaciones sobrerrepresentadas y huecos de variedad;
5. resolver la apariencia individual **antes** de redactar el prompt final;
6. generar;
7. comprobar anti-clonación;
8. solo después de aprobar el asset, registrar la nueva entrada.

Este registro se actualiza únicamente con retratos aprobados.


---

## Estado de sincronización de assets

El registro de diversidad se actualiza inmediatamente al aprobar el retrato y entregar su ZIP local.

El ZIP se utiliza únicamente como paquete de transferencia. El estado `synced` se alcanza cuando la **carpeta descomprimida del asset** está confirmada en el repositorio y contiene, como mínimo:

- `<base_name>.png`
- `<base_name>_prompt.md`
- `<base_name>_info.md`

Estados utilizados:

- `local_pending_gitsync` — ZIP entregado al usuario; carpeta definitiva todavía no confirmada en GitHub.
- `synced` — carpeta definitiva confirmada en GitHub.

### Assets de Treskal confirmados

- `portrait_treskal_farmer_female_001` — **synced**  
  `Worldbuilding/Direccion artistica/Assets/Retratos/Treskal/portrait_treskal_farmer_female_001/`
- `portrait_treskal_farmer_female_002` — **synced**  
  `Worldbuilding/Direccion artistica/Assets/Retratos/Treskal/portrait_treskal_farmer_female_002/`
- `portrait_treskal_farmer_female_003` — **synced**  
  `Worldbuilding/Direccion artistica/Assets/Retratos/Treskal/portrait_treskal_farmer_female_003/`  
  edad aparente ~62 años / franja útil 58–68.

### Verificación de la 003

Comprobación realizada el 2026-09-25:

- PNG remoto: Git blob SHA `f31d29790af103024ff930d8c662dc7560e62026`
- `_info.md` remoto: Git blob SHA `539835400cbffa33b6381aceb85912dceeda69f3`
- `_prompt.md` remoto: Git blob SHA `0b6fafbd8d9870d252a0095beb7b2e790d833842`

Los tres coinciden exactamente con los archivos incluidos en el ZIP entregado.

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

Actualmente hay **15 retratos aprobados registrados**.

| Asset ID | Localización | Profesión | Sexo | Edad aparente | Rango | Complexión | Cabello | Pérdida de cabello | Vello facial | Rasgo facial / distintivo | Presentación | Pátina |
|---|---|---|---|---:|---|---|---|---|---|---|---:|---|
| `portrait_treskal_farmer_female_001` | Treskal | farmer | female | 44 | adult | robust | dark_ash_brown, tied back, early grey | none | not_applicable | rostro broad-oval, nariz marcada, asimetría sutil, piel curtida | 2 | C |
| `portrait_treskal_farmer_female_002` | Treskal | farmer | female | 19 | young | thin/average | light-medium brown, long loose braid, no grey | none | not_applicable | rostro ovalado estrecho, pecas abundantes, ojos avellana verdosos | 2 | C |
| `portrait_treskal_farmer_female_003` | Treskal | farmer | female | 62 | elderly | thin | grey, gathered under worn headscarf | not_visible | not_applicable | rostro largo y estrecho, envejecimiento marcado, ojos verde-avellana apagados | 2 | C |
| `portrait_treskal_farmer_female_004` | Treskal | farmer | female | 34 | adult | robust | auburn-chestnut, curly, gathered under light headscarf | none | not_applicable | rostro ancho y redondeado, piel ligeramente curtida, ojos gris-verde / avellana | 2 | C |
| `portrait_treskal_farmer_female_005` | Treskal | farmer | female | 50 | adult | lean/average | dark brown with strong grey streaks, braided back | none_visible | not_applicable | rostro ovalado alargado y angular, pómulos marcados, mirada firme | 2 | C |
| `portrait_treskal_farmer_male_001` | Treskal | farmer | male | 39 | adult | lean/average | medium brown, medium-short, tousled | none | short beard/stubble | rostro ovalado alargado algo angular, piel curtida, mirada directa | 2 | C |
| `portrait_treskal_farmer_male_002` | Treskal | farmer | male | 21 | young | lean/healthy | light brown–dark blond, medium, tousled | none | very light stubble | rostro juvenil ovalado-estrecho, pecas sutiles, ojos avellana-verdes | 2 | C |
| `portrait_treskal_farmer_male_003` | Treskal | farmer | male | 50 | adult | sturdy/broad | dark brown with greying, short-medium | receding/thinning | full salt-and-pepper beard | rostro ancho y curtido, barba entrecana, mirada seria | 2 | C |
| `portrait_treskal_farmer_male_004` | Treskal | farmer | male | 60 | elderly | lean/wiry | grey-brown, short-medium sides/back | crown baldness/receding | short salt-and-pepper beard | rostro largo y estrecho, calvicie parcial, envejecimiento marcado | 2 | C |
| `portrait_treskal_farmer_male_005` | Treskal | farmer | male | 35 | adult | sturdy/athletic working | medium brown, short, tousled | none | short natural stubble | rostro medio-ancho, mandíbula definida, mirada seria-neutral | 2 | C |
| `portrait_treskal_carpenter_male_001` | Treskal | carpenter | male | 43 | adult | sturdy/craftsman | dark brown with early grey, wavy, short-medium | none_visible | short full beard + moustache | rostro medio-ancho curtido, presencia de artesano competente | 2 | C |
| `portrait_treskal_carpenter_male_002` | Treskal | carpenter | male | 30 | adult | lean/capable craftsman | medium brown, short, slightly tousled | none_visible | light stubble | rostro medio-angular joven, mirada enfocada | 2 | C |
| `portrait_treskal_carpenter_male_003` | Treskal | carpenter | male | 62 | elderly | seasoned/sturdy craftsman | grey, short-medium, slightly wavy | none_strongly_visible | short full grey beard + moustache | maestro senior, rostro curtido, mirada calmada | 2 | C |
| `portrait_treskal_carpenter_male_004` | Treskal | carpenter | male | 50 | adult | heavyset/sturdy craftsman | medium brown, short, thinning | receding/thinning | thick moustache + beard shadow | rostro ancho, bigote marcado, presencia robusta | 2 | C |
| `portrait_treskal_carpenter_male_005` | Treskal | carpenter | male | 58 | adult | lean/seasoned craftsman | salt-and-pepper, medium, brushed back | moderate_recession | prominent moustache + beard shadow | rostro largo curtido, presencia de maestro experimentado | 2 | C |

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

Rutas base vigentes:

- `Worldbuilding/Direccion artistica/Assets/portraits/Norgard/Treskal/farmer/female/`
- `Worldbuilding/Direccion artistica/Assets/portraits/Norgard/Treskal/farmer/male/`
- `Worldbuilding/Direccion artistica/Assets/portraits/Norgard/Treskal/carpenter/male/`

Campesinas:

- `portrait_treskal_farmer_female_001` — **synced**
- `portrait_treskal_farmer_female_002` — **synced**
- `portrait_treskal_farmer_female_003` — **synced** — edad aparente ~62 / franja 58–68
- `portrait_treskal_farmer_female_004` — **synced** — edad aparente ~34 / franja 30–38
- `portrait_treskal_farmer_female_005` — **synced** — edad aparente ~50 / franja 46–55

Campesinos:

- `portrait_treskal_farmer_male_001` — **synced** — edad aparente ~39 / franja 35–44
- `portrait_treskal_farmer_male_002` — **synced** — edad aparente ~21 / franja 18–24
- `portrait_treskal_farmer_male_003` — **synced** — edad aparente ~50 / franja 46–55
- `portrait_treskal_farmer_male_004` — **synced** — edad aparente ~60 / franja 56–66
- `portrait_treskal_farmer_male_005` — **synced** — edad aparente ~35 / franja 31–39

Carpinteros:

- `portrait_treskal_carpenter_male_001` — **synced** — edad aparente ~43 / franja 38–48
- `portrait_treskal_carpenter_male_002` — **synced** — edad aparente ~30 / franja 27–34
- `portrait_treskal_carpenter_male_003` — **synced** — edad aparente ~62 / franja 58–68
- `portrait_treskal_carpenter_male_004` — **synced** — edad aparente ~50 / franja 46–55
- `portrait_treskal_carpenter_male_005` — **synced** — edad aparente ~58 / franja 54–62

Todas las carpetas contienen el conjunto estándar del asset: PNG + `_prompt.md` + `_info.md`.

### Verificación de la 003

Comprobación realizada el 2026-09-25:

- PNG remoto: Git blob SHA `f31d29790af103024ff930d8c662dc7560e62026`
- `_info.md` remoto: Git blob SHA `539835400cbffa33b6381aceb85912dceeda69f3`
- `_prompt.md` remoto: Git blob SHA `0b6fafbd8d9870d252a0095beb7b2e790d833842`

Los tres coinciden exactamente con los archivos incluidos en el ZIP entregado.

# NIMROEL — PORTRAIT REGISTRY

**Estado:** ACTIVE  
**Versión:** 1.1  
**Inicio del registro:** 2026-09-25  
**Última actualización:** 2026-09-26  
**Ámbito:** todos los retratos aprobados almacenados bajo `Worldbuilding/Direccion artistica/Assets/`

Este documento es la vista humana resumida del registro de diversidad de retratos.

La fuente operativa estructurada es:

`PORTRAIT_REGISTRY.json`

Las reglas obligatorias de consulta y generación están en:

`PORTRAIT_WORKFLOW_RULES.md`

---

## Principio

Cada retrato aprobado representa a **un individuo**, no a un modelo universal de su profesión, sexo, cultura o localización.

El registro sirve para evitar clones o semiclones, detectar combinaciones sobrerrepresentadas y cubrir progresivamente la diversidad permitida por las biblias visuales.

---

## Convención de archivos y almacenamiento

El ZIP es únicamente el paquete de **transferencia ChatGPT → usuario**.

En GitHub, cada asset aprobado se conserva como una carpeta descomprimida:

```text
<asset_id>/
├── <asset_id>.png
├── <asset_id>_prompt.md
└── <asset_id>_info.md
```

El ZIP no se conserva en el repositorio.

---

## Estado actual

Actualmente hay **39 retratos aprobados registrados y sincronizados** de Treskal.

| Grupo físico | Retratos |
|---|---:|
| farmer | 10 |
| carpenter | 5 |
| blacksmith | 5 |
| healer | 3 |
| children | 6 |
| elder | 6 |
| fisher | 2 |
| tavernkeeper | 2 |
| **TOTAL** | **39** |

Todos los assets enumerados abajo han sido comprobados en `main` y su carpeta contiene el trío estándar **PNG + _prompt.md + _info.md**.

---

## Retratos aprobados

| Asset ID | Profesión / función | Sexo | Edad aparente | Rango | Complexión | Cabello | Pérdida capilar | Vello facial | Rasgos distintivos | Pres. | Pátina | Sync |
|---|---|---|---:|---|---|---|---|---|---|---:|---|---|
| `portrait_treskal_blacksmith_male_001` | blacksmith | male | 45 | 40-50 | broad_powerful_craftsman | dark_brown; light_early_grey | none_visible | full_beard_and_moustache | full dark beard with early grey; broad smith build | 2 | C | **synced** |
| `portrait_treskal_blacksmith_male_002` | blacksmith | male | 40 | 36-45 | broad_powerful_craftsman | dark_brown | none_visible | thick_moustache_short_beard_stubble | thick moustache; short beard shadow | 2 | C | **synced** |
| `portrait_treskal_blacksmith_male_003` | blacksmith | male | 62 | 58-68 | broad_powerful_senior_craftsman | grey; dominant | none_visible | full_grey_beard_and_moustache | grey hair; full grey beard | 2 | C | **synced** |
| `portrait_treskal_blacksmith_male_004` | blacksmith | male | 64 | 60-70 | broad_seasoned_craftsman | grey; dominant | receding_balding_crown | full_grey_beard_and_moustache | receding grey hair; balding crown | 2 | C | **synced** |
| `portrait_treskal_blacksmith_male_005` | blacksmith | male | 50 | 46-55 | very_broad_powerful_craftsman | dark_brown_with_early_grey; early_visible | none_visible | full_dark_beard_with_grey | very broad build; square face | 2 | C | **synced** |
| `portrait_treskal_carpenter_male_001` | carpenter | male | 43 | 38-48 | sturdy_craftsman | dark_brown_with_early_grey; light_early_grey_temples_and_beard | none_visible | short_full_beard_and_moustache | wavy_dark_hair; short_full_beard | 2 | C | **synced** |
| `portrait_treskal_carpenter_male_002` | carpenter | male | 30 | 27-34 | lean_capable_craftsman | medium_brown | none_visible | light_natural_stubble | short_medium_brown_hair; light_stubble | 2 | C | **synced** |
| `portrait_treskal_carpenter_male_003` | carpenter | male | 62 | 58-68 | seasoned_sturdy_craftsman | grey; dominant | none_strongly_visible | short_full_grey_beard_and_moustache | grey_hair; short_full_grey_beard | 2 | C | **synced** |
| `portrait_treskal_carpenter_male_004` | carpenter | male | 50 | 46-55 | heavyset_sturdy_craftsman | medium_brown; minimal_to_slight | receding_thinning_on_top | thick_moustache_with_very_short_beard_shadow | thick_moustache; broad_heavyset_craftsman_face | 2 | C | **synced** |
| `portrait_treskal_carpenter_male_005` | carpenter | male | 58 | 54-62 | lean_seasoned_craftsman | dark_brown_to_grey_salt_and_pepper; substantial_temples_and_throughout | moderate_recession | prominent_moustache_with_light_beard_shadow | swept_back_salt_and_pepper_hair; prominent_moustache | 2 | C | **synced** |
| `portrait_treskal_boy_001` | village_child | male | 13 | 11-14 | slim_youthful | light_to_medium_brown | none_visible | none | freckles; calm observant expression | 2 | C | **synced** |
| `portrait_treskal_farmer_boy_001` | farmer | male | 11 | 9-12 | slim_youthful | medium_brown | none_visible | none | freckles; tousled brown hair | 2 | C | **synced** |
| `portrait_treskal_farmer_boy_002` | farmer | male | 10 | 8-11 | slim_youthful | medium_brown | none_visible | none | freckles; open expression | 2 | C | **synced** |
| `portrait_treskal_girl_001` | village_child | female | 11 | 9-12 | slim_youthful | medium_brown | none_visible | not_applicable | practical braid; freckles | 2 | C | **synced** |
| `portrait_treskal_girl_002` | village_child | female | 12 | 10-13 | slim_youthful | dark_brown | none_visible | not_applicable | long dark-brown braid; hazel-brown eyes | 2 | C | **synced** |
| `portrait_treskal_girl_003` | village_child | female | 10 | 8-11 | slim_youthful | light_medium_brown | none_visible | not_applicable | twin braids; freckles | 2 | C | **synced** |
| `portrait_treskal_elder_female_001` | village_elder | female | 80 | 76-85 | slim_resilient | white_grey; dominant | none_visible | not_applicable | dark headscarf; deep age lines | 2 | C | **synced** |
| `portrait_treskal_elder_female_002` | village_elder | female | 80 | 76-85 | slim_resilient | white_grey; dominant | none_visible | not_applicable | dark headscarf; white-grey hair | 2 | C | **synced** |
| `portrait_treskal_elder_female_003` | village_elder | female | 95 | 90-99 | very_frail_dignified | white; fully_white | none_visible | not_applicable | near-centenarian appearance; white hair under dark headscarf | 2 | C | **synced** |
| `portrait_treskal_elder_male_001` | village_elder | male | 70 | 66-75 | lean_seasoned | grey_white; dominant | mild_recession | full_white_grey_beard | long weathered face; white-grey beard | 2 | C | **synced** |
| `portrait_treskal_elder_male_002` | village_elder | male | 80 | 76-85 | lean_frail_dignified | white; fully_white | thinning | full_white_beard | thinning white hair; full white beard | 2 | C | **synced** |
| `portrait_treskal_elder_male_003` | village_elder | male | 80 | 76-85 | lean_frail_dignified | white; fully_white | receding_thinning | short_white_beard_and_moustache | short white beard; receding white hair | 2 | C | **synced** |
| `portrait_treskal_farmer_female_001` | farmer | female | 44 | 40-49 | robust | dark_ash_brown; early_grey_strands | none | not_applicable | weathered outdoor-work complexion; subtle facial asymmetry | 2 | C | **synced** |
| `portrait_treskal_farmer_female_002` | farmer | female | 19 | 17-22 | thin_average | light_to_medium_brown | none | not_applicable | abundant_freckles_across_face_and_nose; long_loose_braid | 2 | C | **synced** |
| `portrait_treskal_farmer_female_003` | farmer | female | 62 | 58-68 | thin | grey; dominant_fully_grey | not_visible | not_applicable | pronounced_expression_and_age_lines; long_narrow_face | 2 | C | **synced** |
| `portrait_treskal_farmer_female_004` | farmer | female | 34 | 30-38 | robust | auburn_chestnut | none | not_applicable | loose_curls_framing_face; fuller_rounded_facial_structure | 2 | C | **synced** |
| `portrait_treskal_farmer_female_005` | farmer | female | 50 | 46-55 | lean_average | dark_brown_with_strong_grey_streaking; substantial_temples_and_hairline | none_visible | not_applicable | prominent_grey_streaks_through_dark_hair; practical_braided_gathered_hairstyle | 2 | C | **synced** |
| `portrait_treskal_farmer_male_001` | farmer | male | 39 | 35-44 | lean_average_naturally_sturdy | medium_brown; none_obvious | none | short_practical_beard_stubble_medium_brown | outdoor_weathered_complexion; calm_direct_gaze | 2 | C | **synced** |
| `portrait_treskal_farmer_male_002` | farmer | male | 21 | 18-24 | lean_healthy | light_brown_to_dark_blond | none | very_light_stubble_almost_clean_shaven | tousled_windblown_hair; youthful_face_with_subtle_freckles | 2 | C | **synced** |
| `portrait_treskal_farmer_male_003` | farmer | male | 50 | 46-55 | sturdy_broad | dark_brown_with_greying; moderate_to_substantial | receding_thinning | salt_and_pepper_full_beard_and_moustache | receding_hairline; salt_and_pepper_beard | 2 | C | **synced** |
| `portrait_treskal_farmer_male_004` | farmer | male | 60 | 56-66 | lean_wiry | grey_brown; dominant_substantial | receding_with_crown_baldness | short_salt_and_pepper_beard_and_moustache | partial_baldness_thinning_crown; deeply_lined_forehead_and_crows_feet | 2 | C | **synced** |
| `portrait_treskal_farmer_male_005` | farmer | male | 35 | 31-39 | sturdy_athletic_working | medium_brown | none | short_natural_stubble | short_tousled_brown_hair; defined_jaw_with_short_stubble | 2 | C | **synced** |
| `portrait_treskal_fisher_male_001` | fisher | male | 42 | 38-46 | fit_weathered_working | dark_brown; minimal_visible | none_visible | short_beard_and_moustache | rope and net over shoulder; short dark beard | 2 | C | **synced** |
| `portrait_treskal_fisher_male_002` | fisher | male | 58 | 54-62 | fit_weathered_working | dark_brown_with_grey; visible_temples_and_beard | none_visible | full_grey_streaked_beard_and_moustache | greying full beard; weathered lined face | 2 | C | **synced** |
| `portrait_treskal_healer_female_001` | healer | female | 63 | 58-70 | average_seasoned | silver_grey; dominant | none_visible | not_applicable | silver-grey hair under patterned headscarf; kind wise expression | 2 | C | **synced** |
| `portrait_treskal_healer_female_002` | healer | female | 66 | 62-72 | average_seasoned | silver_white; dominant | none_visible | not_applicable | silver-white hair; dark headscarf | 2 | C | **synced** |
| `portrait_treskal_healer_female_003` | healer | female | 30 | 27-34 | average_healthy | medium_brown | none_visible | not_applicable | medium-brown hair gathered back; young healer presence | 2 | C | **synced** |
| `portrait_treskal_tavernkeeper_female_001` | tavernkeeper | female | 25 | 22-28 | healthy_sturdy | dark_brown | none_visible | not_applicable | practical tavern updo; light freckles | 2 | C | **synced** |
| `portrait_treskal_tavernkeeper_male_001` | tavernkeeper | male | 50 | 46-54 | broad_sturdy_working | dark_brown_with_grey; visible_temples_and_beard | mild_recession | full_grey_streaked_beard_and_moustache | broad innkeeper presence; warm approachable expression | 2 | C | **synced** |

---

## Uso obligatorio

Antes de generar un retrato nuevo:

1. consultar las biblias visuales vigentes aplicables;
2. para cualquier habitante de Treskal, consultar obligatoriamente `TRESKAL_PORTRAIT_VISUAL_BIBLE_v0.1.md` o la versión posterior vigente;
3. consultar `PORTRAIT_REGISTRY.json`;
4. construir el pool comparable;
5. detectar rasgos y combinaciones sobrerrepresentadas;
6. resolver la apariencia individual antes del prompt final;
7. generar y comprobar anti-clonación;
8. registrar únicamente después de la aprobación.

---

## Estado de sincronización

Estados utilizados:

- `local_pending_gitsync` — ZIP entregado; carpeta definitiva todavía no confirmada en GitHub.
- `synced` — carpeta definitiva confirmada en GitHub con PNG + `_prompt.md` + `_info.md`.

**Estado de este corte (2026-09-26): 39/39 assets registrados están `synced`.**

Rutas de grupo confirmadas:

- `portraits/Norgard/Treskal/farmer/`
- `portraits/Norgard/Treskal/carpenter/`
- `portraits/Norgard/Treskal/blacksmith/`
- `portraits/Norgard/Treskal/healer/`
- `portraits/Norgard/Treskal/children/`
- `portraits/Norgard/Treskal/elder/`
- `portraits/Norgard/Treskal/fisher/`
- `portraits/Norgard/Treskal/tavernkeeper/`

Este registro se actualiza únicamente con retratos aprobados.

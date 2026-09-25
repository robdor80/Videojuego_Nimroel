# NIMROEL — VISUAL ASSET REGISTRY

Registro general de assets visuales creados mediante el workflow oficial de `Nimroel-Visual-Assets`.

## Estados

- `DRAFT` — en desarrollo.
- `REVIEW` — pendiente de aprobación visual.
- `APPROVED` — aprobado y congelado como referencia válida.
- `REJECTED` — descartado.
- `ARCHIVED_EXTERNAL` — aprobado; binarios pesados archivados externamente.

## Retratos

> **Registro reiniciado el 2026-09-25.**
>
> Diez retratos aprobados bajo el nuevo workflow de diversidad. Los assets se almacenan en GitHub como carpetas descomprimidas; los diez están sincronizados.

| Asset ID | Nombre | Reino / Cultura | Región | Tipo | Presentación | Pátina | Estado | Repositorio | Notas |
|---|---|---|---|---|---:|---|---|---|---|
| `portrait_treskal_farmer_female_001` | Campesina de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | carpeta del asset — synced | Primera entrada del nuevo registro de diversidad; edad aparente 44, complexión robusta, cabello castaño ceniza oscuro con canas tempranas. |
| `portrait_treskal_farmer_female_002` | Campesina joven de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~19 (franja 17–22), complexión esbelta, trenza castaña clara, sin canas, pecas abundantes; fondo agrícola contextual de Treskal. |
| `portrait_treskal_farmer_female_003` | Campesina mayor de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~62 (franja 58–68), complexión delgada, cabello gris bajo pañuelo, rostro largo y envejecido; fondo agrícola contextual de Treskal. |
| `portrait_treskal_farmer_female_004` | Campesina adulta de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~34 (franja 30–38), complexión robusta, rostro ancho y redondeado, cabello rizado cobrizo-castaño bajo pañuelo; huerto agrícola contextual de Treskal. |
| `portrait_treskal_farmer_female_005` | Campesina madura de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~50 (franja 46–55), complexión lean/average, rostro angular alargado, cabello castaño oscuro con canas muy marcadas y recogido trenzado; fondo agrícola junto a agua/río. |
| `portrait_treskal_farmer_male_001` | Campesino de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~39 (franja 35–44), complexión lean/average naturalmente robusta, cabello castaño medio y barba corta; fondo agrícola contextual de Treskal. |
| `portrait_treskal_farmer_male_002` | Campesino joven de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~21 (franja 18–24), complexión esbelta, cabello castaño claro/rubio oscuro, casi sin barba; fondo agrícola contextual de Treskal. |
| `portrait_treskal_farmer_male_003` | Campesino maduro de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~50 (franja 46–55), complexión robusta/ancha, retroceso capilar y barba completa entrecana; formato vertical 4:5. |
| `portrait_treskal_farmer_male_004` | Campesino mayor de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~60 (franja 56–66), complexión delgada/fibrosa, cabello gris-castaño con calvicie parcial y barba corta entrecana; formato vertical 4:5. |
| `portrait_treskal_farmer_male_005` | Campesino adulto de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | carpeta del asset — synced | Edad aparente ~35 (franja 31–39), complexión robusta/atlética de trabajo, cabello castaño corto y barba corta; formato vertical 4:5. |

### Registros obligatorios de retratos

Antes de generar cualquier nuevo retrato se deben consultar obligatoriamente:

- `PORTRAIT_WORKFLOW_RULES.md`
- `PORTRAIT_REGISTRY.json`
- las biblias visuales vigentes que correspondan al asset.

`PORTRAIT_REGISTRY.md` es la vista humana resumida del registro operativo JSON.

La columna **Presentación** utiliza la escala contextual 1–5.

La columna **Pátina** utiliza la escala A–D:

- `A` — excepcional / casi nueva;
- `B` — bien mantenida;
- `C` — uso cotidiano normal;
- `D` — muy trabajada.

Ambas capas son independientes: una persona puede estar aseada y vestir prendas con pátina C o D.

## Escenas

| Asset ID | Nombre | Reino / Cultura | Localización | Variantes | Estado | Prompt base | Binarios | Notas |
|---|---|---|---|---:|---|---|---|---|

## Reglas de registro

Para cada asset `APPROVED` deben quedar registrados:

- ID único;
- nombre;
- categoría;
- reino o cultura;
- región o localización cuando aplique;
- prompt exacto utilizado;
- fuentes canónicas consultadas;
- metadata;
- manifest;
- README;
- estado de los binarios;
- notas de continuidad visual si son necesarias.

Para retratos se aplican además las reglas completas de `PORTRAIT_WORKFLOW_RULES.md`.

Como mínimo deben registrarse:

- nombre base común del asset, PNG, ZIP de transferencia y carpeta de repositorio;
- profesión / función visual;
- sexo;
- rango de edad y edad aparente;
- complexión;
- morfología facial;
- cabello y grado de pérdida de cabello;
- vello facial;
- rasgos distintivos;
- `presentation_state_level` 1–5;
- `clothing_patina_grade` A–D;
- actividad actual o inmediatamente anterior;
- estado base de la ropa;
- rastros concretos de oficio, entorno o viaje;
- grado de aseo reciente;
- estado visible de manos, botas, cabello, barba y equipo.

Para trabajadores físicos, población rural, ropa de faena y viajes de varios días, presentación y pátina son obligatorias.

En escenas, `DAY_BASE` es la imagen madre y toda variante debe derivarse de ella.

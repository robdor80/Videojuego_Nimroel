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
> Dos retratos aprobados bajo el nuevo workflow de diversidad. Ambos ZIP están sincronizados y verificados en el repositorio.

| Asset ID | Nombre | Reino / Cultura | Región | Tipo | Presentación | Pátina | Estado | ZIP | Notas |
|---|---|---|---|---|---:|---|---|---|---|
| `portrait_treskal_farmer_female_001` | Campesina de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | `portrait_treskal_farmer_female_001.zip` — synced | Primera entrada del nuevo registro de diversidad; edad aparente 44, complexión robusta, cabello castaño ceniza oscuro con canas tempranas. |
| `portrait_treskal_farmer_female_002` | Campesina joven de Treskal | Norgard | Treskal | `farmer_female` | 2 | C | APPROVED | `portrait_treskal_farmer_female_002.zip` — synced | Edad aparente ~19 (franja 17–22), complexión esbelta, trenza castaña clara, sin canas, pecas abundantes; fondo agrícola contextual de Treskal. |

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

- nombre base común de PNG y ZIP;
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

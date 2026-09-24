# NIMROEL — VISUAL ASSET REGISTRY

Registro general de assets visuales creados mediante el workflow oficial de `Nimroel-Visual-Assets`.

## Estados

- `DRAFT` — en desarrollo.
- `REVIEW` — pendiente de aprobación visual.
- `APPROVED` — aprobado y congelado como referencia válida.
- `REJECTED` — descartado.
- `ARCHIVED_EXTERNAL` — aprobado; binarios pesados archivados externamente.

## Retratos

| Asset ID | Nombre | Reino / Cultura | Región | Tipo | Presentación | Pátina | Estado | Prompt | Binario | Notas |
|---|---|---|---|---|---:|---|---|---|---|---|
| `PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001` | Campesino de Treskal | Norgard | Treskal | `farmer_male` | 2 | C | APPROVED | `assets/portraits/norgard/treskal/farmer_male/PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001/PROMPT.md` | `assets/portraits/norgard/treskal/farmer_male/PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001/PORTRAIT_NORGARD_TRESKAL_FARMER_MALE_001.zip` | Primer campesino varón de Treskal aprobado. |

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

Para retratos, cuando sea relevante, también deben registrarse:

- `presentation_state_level` 1–5;
- `clothing_patina_grade` A–D;
- actividad actual o inmediatamente anterior;
- estado base de la ropa;
- rastros concretos de oficio, entorno o viaje;
- origen, localización e intensidad de esas marcas;
- grado de aseo reciente;
- estado visible de manos, botas, cabello, barba y equipo.

Para trabajadores físicos, población rural, ropa de faena y viajes de varios días, las dos capas son obligatorias.

En escenas, `DAY_BASE` es la imagen madre y toda variante debe derivarse de ella.

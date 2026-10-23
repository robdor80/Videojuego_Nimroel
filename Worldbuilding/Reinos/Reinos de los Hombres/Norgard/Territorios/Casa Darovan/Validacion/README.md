# Validación — Casa Darovan

- D01: `D01_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` y `validate_d01.py` (PR #15 fusionada).
- D02: `D02_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` y `validate_d02.py` (PR #16 fusionada en main).
- Comprobaciones estáticas remotas JavaScript/JSON D02: **16 positivas y 8 negativas ejecutadas** durante construcción de D02. **Verificación posterior:** el validador Python original D02 se ejecutó sobre réplica semántica de los campos relevantes recuperados de GitHub y superó también 8 pruebas negativas. D01 Python original se ejecutó igualmente con resultado OK. La **repetición en checkout íntegro del MSI se completó con éxito (D01, D02 y D03)**; evidencia en `../Auditorias/D03_VALIDACION_MSI_CHECKOUT_2026-10-15.md` y acta histórica de réplica `../Auditorias/D03_VALIDACION_PYTHON_EN_ENTORNO_AISLADO_2026-10-15.md`.
- Ni la documentación ni estas comprobaciones acreditan simulación de terreno, CoreRPG/Godot, persistencia, navegación o CI de juego.
- Acta: `../Auditorias/D02_CIERRE_Y_VALIDACION_2026-10-15.md`; no elevar propuestas a canon.

- D03: `D03_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` (30 invariantes) y `validate_d03.py` (10 casos negativos). JavaScript remoto realizado sobre perfil y referencias. **Python D03 EJECUTADO — OK** sobre réplica semántica contrastada con GitHub: script idéntico al blob GitHub, JSON D03 canónico idéntico y 10 pruebas negativas superadas. No fue un checkout íntegro: D01/D02/Core se representaron por los campos leídos y las 13 rutas se verificaron remotamente. **D01/D02 Python también EJECUTADOS — OK** en réplicas semánticas contrastadas; **SUPERADO — MSI / checkout íntegro:** ejecución Python D01/D02/D03 OK (8 negativos D02 y 10 negativos D03); **PENDIENTE — GODOT** runtime y **MSI/GIS** pruebas geográficas. Evidencia en `../Auditorias/D03_CIERRE_Y_VALIDACION_2026-10-15.md`.

## D04
`validate_d04.py`: D01+D02+D03, Core libro y Default fiscal Norgard; 16 mutaciones negativas. **Python ejecutado sobre checkout íntegro en GitHub Actions Windows 2022 y Ubuntu 24.04 — ambos SUCCESS (21-10-2026, run 39583142837).** Todos los validadores D01–D04 terminaron STATIC OK. La ejecución física específica de D04 en MSI no se ha efectuado; es opcional, no requisito de cierre estático. Remoto JavaScript previo: 22/22 OK incluidas 16 mutaciones negativas rechazadas. Sin ejecución de Godot/GIS/CoreRPG runtime. Ver [acta CI](../Auditorias/D04_VALIDACION_CI_Y_CIERRE_2026-10-21.md) y matriz D04.

- **D05:** [matriz](D05_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md) / [validador Python](validate_d05.py), red cualitativa y regresiones D01–D04, no-runtime; ver CI real antes de afirmar resultado.

## D06 — Asentamientos ordinarios
- [Matriz D06](D06_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md): trazabilidad D01–D05, nueve modelos, doce prioridades, seis escenarios sintéticos, pruebas de semillas e invariantes.
- `validate_d06.py` con `d06_generator.py` y dos JSON de datos operativos. **20 mutaciones negativas de reglas + 22 de escenarios**; rechazan canonicidad automática, Agujas, navegación, aduanas, colocación sin agua y otros saltos de autoridad.
- Workflow D01–D06 en Ubuntu 24.04 y Windows 2022. Verificar ejecución real de PR, no afirmar `SUCCESS` por existir el archivo.
- **Solo laboratorio y validación estática.** CoreRPG/Godot/GIS/persistencia, densidades y localización real quedan pendientes.

## D10 — Cultura y sociedad
- `D10_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` (matriz de protección de 17 decisiones, perfiles y canon superior).
- `validate_d10.py` verifica fuentes existentes, esquema documental, seis perfiles, dieciséis escenarios `TEST_ONLY`, coherencia D07/D08/D09 y mutaciones negativas.
- Workflow D01–D10 Windows 2022 / Ubuntu 24.04; comprobar resultado de CI real antes de declararlo superado. No es runtime.

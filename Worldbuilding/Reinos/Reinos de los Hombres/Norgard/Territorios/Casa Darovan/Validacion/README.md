# Validación — Casa Darovan

- D01: `D01_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` y `validate_d01.py` (PR #15 fusionada).
- D02: `D02_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` y `validate_d02.py` (PR #16 fusionada en main).
- Comprobaciones estáticas remotas JavaScript/JSON D02: **16 positivas y 8 negativas ejecutadas**. El validador Python se publica para ejecución reproducible en un checkout completo: **no se ha ejecutado en esta sesión**.
- Ni la documentación ni estas comprobaciones acreditan simulación de terreno, CoreRPG/Godot, persistencia, navegación o CI de juego.
- Acta: `../Auditorias/D02_CIERRE_Y_VALIDACION_2026-10-15.md`; no elevar propuestas a canon.

- D03: `D03_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md` (30 invariantes) y `validate_d03.py` (10 casos negativos). JavaScript remoto realizado sobre perfil y referencias. **Python D03 EJECUTADO — OK** sobre réplica semántica contrastada con GitHub: script idéntico al blob GitHub, JSON D03 canónico idéntico y 10 pruebas negativas superadas. No fue un checkout íntegro: D01/D02/Core se representaron por los campos leídos y las 13 rutas se verificaron remotamente. **PENDIENTE:** suite D01/D02 Python y repetición de los tres validadores en checkout íntegro; **PENDIENTE — GODOT** runtime y **MSI/GIS** pruebas geográficas. Evidencia en `../Auditorias/D03_CIERRE_Y_VALIDACION_2026-10-15.md`.

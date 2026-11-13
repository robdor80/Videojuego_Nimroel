# NIM-08 static validator

Solo estándar Python 3.12 (sin paquetes externos ni red). **No genera ni simula una aldea y no ejecuta CoreRPG/Godot.**

Desde raíz del repositorio:

    python Tools/NIM08/check_contracts.py --json
    python -m unittest discover -s Tools/NIM08 -p 'test_*.py' -v

Verifica 28 IDs exactamente contra canon y matriz de planificación, todos pendientes; estructura y referencias locales de tres esquemas Draft 2020-12; ejemplo de manifiesto y pruebas negativas; SHA Git Blob de source-lock ya aprobado, revisión de canon, pack id/version/release SHA256 y pin CMake real. El validador de subconjunto JSON Schema **NO** sustituye un validador JSON Schema completo de producción; NIM-09 debe usar herramienta normativa para la fábrica. Los tests de esquema no confirman invariantes de mundo materializado, partida, persistencia ni plataforma.

CI independiente en .github/workflows/nim08-contracts.yml (Windows/Ubuntu).

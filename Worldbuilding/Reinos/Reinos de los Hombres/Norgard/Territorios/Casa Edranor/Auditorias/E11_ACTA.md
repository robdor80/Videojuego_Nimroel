# Acta técnica E11 — Casa Edranor
**Fecha:** 13/11/2026 · **Estado:** expediente de rama; pruebas remotas pendientes de certificar al crearse la PR.

## Entrega bajo control de cambios
1. Pack `nimroel.edranor.territory` con cinco definiciones estructurales y cero datos jugables.
2. Proyección de autor con once locks SHA de E00–E10 y guardas de competencia.
3. Doce escenarios `TEST_ONLY` sin eventos persistidos por diseño.
4. Validador Python con regresión y mutaciones negativas; consumidor C++ CoreRPG para CI multiplataforma.

## Condiciones de aceptación
- Workflow E11 **verde en su HEAD exacto** tanto Windows 2022 como Ubuntu 24.04.
- Fuente E00–E10 sin deriva, cinco definiciones Core correctas, esquemas oficiales superados y mutaciones rechazadas.
- Compilación C++ y CTest nativo real, separada de la validación estática.
- Diff limitado a archivos nuevos E11 y ContentPacks Edranor, sin modificar canon previo, Game, CoreRPG ni `main` por fuera de la PR.
- Nada de estas pruebas se considerará validación Godot o gameplay.

**Cierre:** pendiente de observación de checks; fusionar solo cuando consten todas las puertas y la autorización del autor.

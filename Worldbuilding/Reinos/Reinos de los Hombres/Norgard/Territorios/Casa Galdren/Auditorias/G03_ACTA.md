# Acta de entrega G03 — Clima, suelos y ecosistemas
**Fecha:** 13/11/2026. **Estado previsto:** `DOCUMENTARY_PLANNING_ONLY`. Autorización de trabajo G03 dada por el autor en su conversación; la aprobación de trabajo NO ratifica un nuevo dato local aún desconocido.

## Contenido sujeto a auditoría
- Siete referencias climáticas cualitativas y doce perfiles derivados de G01.
- Doce expedientes de suelo, todos `UNASSESSED` a escala de parcela; fertilidad regional del Caleran separada.
- Tres bosques orientales descritos desde canon y cuatro referencias de transición/contexto sin nueva jurisdicción.
- Diez escenarios de riesgo: tres hechos cualitativos de hielo, una referencia nival regional y seis hipótesis condicionadas.
- JSON de planificación y validador con mutaciones negativas; CI regresivo G00–G03.

## Controles de aceptación
- [x] Revisar que la rama partió de `1ad65cb5eb5dd449c6dd981cba3b63d96435d69f` y comparar con `main` antes de fusionar.
- [x] Constatar las pruebas G00–G03 Ubuntu/Windows exitosas en SHA de rama y PR.
- [x] Comprobar exactitud de 12 unidades, no nuevas ciudades, ríos, bosques, especies, puntos, suelos medidos ni calendario.
- [x] Comprobar que G02 y límites de Casa/Corona siguen intactos.
- [x] Si todo pasa y hay autorización de cierre, fusionar PR; si falla, mantener en Draft.

**Prohibiciones expresas:** G03 no crea biomas del generador, runtime de CoreRPG, Godot 4.7.2, GDExtension, mapas 2D, clima físico calibrado, cultivos productivos, población, simulación estacional ni jugabilidad. El cierre técnico documental no equivale a aceptación de esas funcionalidades.

## Transferencia
G04 debe consultar el contrato y la deuda, y comenzar únicamente mediante su conversación/fase propia. Los cultivos y cabaña ganadera de G04 no pueden derivarse de temperaturas, humedad, suelo o rendimientos numéricos inexistentes.

## Certificación técnica documental — 13/11/2026
- PR: [#68](https://github.com/robdor80/Videojuego_Nimroel/pull/68); HEAD auditado antes del acta: `48966bd8e56ac0529d79f8aac8e35fa7e4fc3c74`.
- [G03 CI PR #43352925510](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43352925510): **SUCCESS**, Ubuntu 24.04 y Windows 2022. En ambas plataformas pasan G00, G01, G02 y G03.
- Regresiones: G00 **28** negativas, G01 **49**, G02 **58**, G03 **86** ataques negativos rechazados; G03: **7 referencias climáticas, 12 perfiles, 12 expedientes de suelo, 7 referentes ecológicos y 10 riesgos**.
- Workflows adicionales [G00 #43352925548](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43352925548), [G01 #43352925368](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43352925368), [G02 #43352925483](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43352925483): **SUCCESS**, todos sobre el mismo HEAD anterior al acta.
- Diff de fase auditado: 11 altas y un README existente modificado; solo `Casa Galdren/`, `Tools/GaldrenG03/` y workflow de G03. No se modifica `main` directamente.
- Este añadido al acta es administrativo: tras incorporarlo debe confirmarse de nuevo el **HEAD final** y sus verificaciones antes de una eventual fusión.

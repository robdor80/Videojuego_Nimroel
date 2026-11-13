# Acta de entrega G03 — Clima, suelos y ecosistemas
**Fecha:** 13/11/2026. **Estado previsto:** `DOCUMENTARY_PLANNING_ONLY`. Autorización de trabajo G03 dada por el autor en su conversación; la aprobación de trabajo NO ratifica un nuevo dato local aún desconocido.

## Contenido sujeto a auditoría
- Siete referencias climáticas cualitativas y doce perfiles derivados de G01.
- Doce expedientes de suelo, todos `UNASSESSED` a escala de parcela; fertilidad regional del Caleran separada.
- Tres bosques orientales descritos desde canon y cuatro referencias de transición/contexto sin nueva jurisdicción.
- Diez escenarios de riesgo: tres hechos cualitativos de hielo, una referencia nival regional y seis hipótesis condicionadas.
- JSON de planificación y validador con mutaciones negativas; CI regresivo G00–G03.

## Controles de aceptación
- [ ] Revisar que la rama partió de `1ad65cb5eb5dd449c6dd981cba3b63d96435d69f` y comparar con `main` antes de fusionar.
- [ ] Constatar las pruebas G00–G03 Ubuntu/Windows exitosas en SHA de rama y PR.
- [ ] Comprobar exactitud de 12 unidades, no nuevas ciudades, ríos, bosques, especies, puntos, suelos medidos ni calendario.
- [ ] Comprobar que G02 y límites de Casa/Corona siguen intactos.
- [ ] Si todo pasa y hay autorización de cierre, fusionar PR; si falla, mantener en Draft.

**Prohibiciones expresas:** G03 no crea biomas del generador, runtime de CoreRPG, Godot 4.7.2, GDExtension, mapas 2D, clima físico calibrado, cultivos productivos, población, simulación estacional ni jugabilidad. El cierre técnico documental no equivale a aceptación de esas funcionalidades.

## Transferencia
G04 debe consultar el contrato y la deuda, y comenzar únicamente mediante su conversación/fase propia. Los cultivos y cabaña ganadera de G04 no pueden derivarse de temperaturas, humedad, suelo o rendimientos numéricos inexistentes.
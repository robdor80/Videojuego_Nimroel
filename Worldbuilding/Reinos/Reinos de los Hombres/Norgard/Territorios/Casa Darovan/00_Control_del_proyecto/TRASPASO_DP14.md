# D.P13 → D.P14 — Traspaso documental (sin autorización de inicio)

**Fecha:** 25-10-2026. D.P14 no comienza automáticamente ni añade poblaciones en esta rama.

## Entrada preparada

- Las doce unidades D01 conservan IDs y cobertura cualitativa de D.P13.
- El sistema hidrográfico mayor de cinco ríos y cuatro redes permanece bloqueado.
- Para cada emplazamiento hipotético futuro deben consultarse pendiente, cuenca y receptor, agua disponible, drenaje, microclima y riesgo, sin convertir candidatos en hechos.
- `darovan_dp13_physical_profiles_v0.1.json`: perfiles de referencia no-runtime y fuentes.
- `darovan_dp13_hydro_overlay_v0.1.json`: nacimiento/receptor de cauces menores condicionados.
- `darovan_dp13_environment_causal_v0.1.json`: modelo de inferencia y estado persistente futuro.

## Guardrails

No crear asentamientos permanentes en Agujas; no dividir Pilares/Taramin; no inferir suministro potable por bosques, lluvia o bahías; respetar Arven de Darovan pero sin rutas inventadas; no mover las cuatro ciudades; ningún barrio, población nueva ni puente/camino sin apoyo. Mantener sus ocho barrios canónicos en Treihord.

## Requisitos de materialización posterior

Cuando exista cartografía métrica aprobada, resolver altura, divisoria, área aportante, suelo y receptor antes de crear arroyos o declarar seguridad de un lugar. No equiparar `DERIVED_CONDITIONAL` con `AUTHORED`. Futuras capas CoreRPG y host requerirán programación y tests reales; D.P13 no los ha ejecutado.

## Decisiones pendientes no bloqueantes

DAR-P04 y DAR-P08 parcial, nacimientos precisos, cuencas y Fhalion; cartografía de altitudes, cauces y litoral; régimen de vientos y mediciones climáticas, suelos y acuíferos. No se pide respuesta inmediata al autor para continuar el diseño D.P14.

## Cierre delegado de preguntas Q13–Q28 — 25/10/2026

El autor concede autonomía expresa al asistente para escoger las opciones recomendadas de todas las preguntas pendientes. Se registran **16 opciones B (Q13–Q28)**, de las cuales cuatro son nuevas referencias altitudinales: **valles interiores de Valkram 700–1.300 m**, **pasos principales de Elyra 900–1.500 m**, **valles interiores de Elyra 400–900 m**, **lomas del ámbito forestal meridional de Taramin fuera de Elyra 150–500 m**. Las restantes protegen condiciones climáticas, agua menor, suelo, vegetación y riesgos sin inventar mediciones.

Las decisiones son del **asistente por delegación** y no respuestas individuales dadas por el autor; en ningún caso suponen geometría métrica, vientos medidos, glaciares, cauces ubicados o simulación CoreRPG/Godot. Documentación: `D.P13/22_cierre_delegado_preguntas_y_opciones.md`; datos: `Datos operativos/darovan_dp13_delegated_decisions_authorized_v0.1.json`. D.P14 y fases posteriores siguen sin iniciar; PR #39 Draft, main sin fusionar.


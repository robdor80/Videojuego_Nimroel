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



## Actualización de profundización D.P14–D.P18 — 11/11/2026

**Cronología:** esta adenda sustituye únicamente la lectura *actual* de las menciones históricas «D.P14–D.P18 no iniciadas»; no altera el estado de D00–D12 ni D.P13 ya fusionadas.

Por autorización general del autor, se desarrolla consecutivamente en la rama `feat/darovan-dp14-dp18-profundizacion-20261111` y la **PR Draft #41**, sin Codex y sin fusión automática:

- **D.P14:** doce unidades de estudio y diez puertas de elegibilidad física; ningún asentamiento nuevo autorizado por la banda altitudinal.
- **D.P15:** nueve modelos de asentamiento y diez necesidades D08; red funcional con rutas y capacidades pendientes de prueba.
- **D.P16:** cuatro ciudades manuales, doce puertas de análisis urbano, triado de las 99 capas funcionales de Treskal (100 carpetas 01–99 por duplicidad del 34) y trece cadenas funcionales Darovan; **no constituye diseño canónico completo de nuevos barrios de Veldora/Taramin/Syvaris**.
- **D.P17:** 57 namespaces de consulta desde el mapa de extracción Valrik/Core y 24 escenarios `TEST_ONLY`; sin implementación.
- **D.P18:** informe de equivalencia y **12 reservas** claras entre identidad urbana autoral, cartografía y runtime.

Archivos de entrada: `Profundizacion_2026/README.md`, contratos JSON `darovan_dp14_*` a `darovan_dp18_*` y `Tools/DarovanDP14_DP18/validate.py`; GitHub Actions `darovan-dp14-dp18.yml` con pruebas adversariales estáticas. El resultado definitivo depende de GitHub Actions sobre el **último HEAD** de PR #41; los commits anteriores no certifican automáticamente uno nuevo.

**Resultado profesional honesto:** paquete de **diseño funcional y territorial condicional** muy avanzado; no se declara igual de completo que la ciudad de Treskal a nivel de canon urbano ni ejecutable en CoreRPG/Godot. Se requiere decisión del autor para elevar a canon nuevos barrios y singularidades de Veldora, Taramin y Syvaris. Hasta entonces, nuevos topónimos/barrios/edificios singulares permanecen `UNKNOWN` o `PROPOSAL_PENDING_AUTHOR`. Todo lo métrico y de integración física se reserva para una fase posterior.

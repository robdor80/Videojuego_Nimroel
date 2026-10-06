# Nimroel Core — regresión GEO física / drenaje / hidrografía v0.1

## Casos

- GEO-PHY-001: ningún cauce superficial generado asciende contra el gradiente sin excepción física explícita.
- GEO-PHY-002: toda red menor pertenece a una cuenca y termina en un receptor, depresión válida o salida costera.
- GEO-PHY-003: una divisoria no es atravesada por un cauce generado arbitrariamente.
- GEO-PHY-004: todo manantial conserva una causa de alimentación plausible.
- GEO-PHY-005: los cursos permanentes, estacionales y efímeros se distinguen por alimentación y contexto, no por RNG puro.
- GEO-PHY-006: la geometría materializada persiste entre visitas y save/load.
- GEO-PHY-007: el WorldState puede cambiar caudal/actividad sin cambiar identidad del cauce.
- GEO-PHY-008: AUTHORED prevalece sobre GENERATED.
- GEO-PHY-009: UNKNOWN sigue siendo válido cuando faltan datos.
- GEO-PHY-010: clima/microclima modula agua disponible, mientras microrelieve organiza la posición espacial.
- GEO-PHY-011: carreteras y asentamientos pueden modificar el drenaje, pero no borrar sin causa la topografía preexistente.
- GEO-PHY-012: no se exige simulación hidráulica científica completa.

## Resultado esperado

**NIMROEL_CORE_PHYSICAL_GEOGRAPHY_COMPATIBLE**

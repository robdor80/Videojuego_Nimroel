# E06 — Matriz de pruebas sintéticas
Los 15 casos no son ubicaciones creadas ni asentamientos aprobados. Los `sandbox_*` son claves de ensayo sin coordenadas.

## Seis candidatos técnicamente elegibles (solo laboratorio)
- Karsath/centro oeste: viña de ensayo con condiciones de parcela y microclima supuestas.
- Lumina: tonelería auxiliar, clase pueblo con funciones y demanda supuestas.
- Lumina: gestión forestal, clase enclave con residentes simulados y derechos hipotéticos.
- Centro vitícola: agricultura mixta.
- Dorth/Azurios: artesanía con función local.
- Centro: servicios de camino con carretera comprobada **solo en ficción de prueba**; E05 no confirma ninguna carretera real.

## Nueve rechazos obligatorios
Falta de agua; invasión de Rodas; invasión de Hallheim; titularidad de Corona; norte sin cierre; Bosque Real; tala sin derecho; servicio en camino no probado; nombre visible introducido prematuramente.

Se verifican estabilidad de ID, cambio por semilla/slot, independencia del orden de modelos, rechazo al pasar `fixtureKind=REAL`, ausencia de materialización y regresiones E00–E05. Las pruebas negativas de mutación alteran derechos, autoridades, mapas, pesos, anclas, guardas, seed y contratos para demostrar rechazo.

**Limitación:** éxito de Python 3.12 en Linux/Windows valida exclusivamente datos y función pura, no ejecución de Godot, física, rutas ni persistencia.

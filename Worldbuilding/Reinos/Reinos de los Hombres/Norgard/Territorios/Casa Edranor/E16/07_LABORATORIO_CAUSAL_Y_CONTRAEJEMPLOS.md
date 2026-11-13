# E16 — Matriz de casos contrafácticos

El contrato JSON contiene **30 casos hipotéticos** agrupados en movilidad (10), comunicaciones (6), servicios (8) y mantenimiento (6). Se usan para demostrar que las puertas responden cuando falta un dato. Ningún caso ha ocurrido en Nimroel: no hay puente roto, viaje perdido, incendio, alerta o carreta atrapada.

## Reglas de oráculo
- Prueba explícitamente falsa de seguridad, legalidad, capacidad o jurisdicción → **BLOCKED**.
- Prueba sin valor, UNKNOWN o ausente → **PENDING_EVIDENCE**.
- Todas las pruebas de un caso sintético verdaderas → **ELIGIBLE_SYNTHETIC_ONLY**, **nunca** despacho real. Esta distinción protege el motor contra activar servicios por pasar tests de documentación.
- Trazabilidad fiscal: Rodas Corona; sin aduana entre Casas ni impuesto por atravesar una frontera interna.
- Trazabilidad económica: lote real, reservas no duplicadas, entregas con recepción; no descontar dos veces un componente.
- Trazabilidad humana: agente real, tiempos sin solapamientos y acceso a cuidados; no se inventan habitantes para satisfacer un servicio.
- Trazabilidad espacial: no inventar carretera, muelle, vado ni frontera por dibujar una necesidad.

## Casos de integración posterior
E17 podrá construir cadenas de fallo y recuperación: una entrega no cumplida altera inventario disponible, afecta a hogar o taller y puede exigir mantenimiento o solicitud administrativa. Para E28 harían falta objetos en World State, test real del motor, georreferencia E19, agente concreto y derechos; no basta ejecutar el validador Python.

## Negativas obligatorias
Una mutación adversarial debe provocar fallo al cambiar cero infraestructuras por una, al cambiar dueño de Rodas, al permitir peajes, al atribuir viticultura boreal, al abrir U7, al crear una arista física o al ratificar un supuesto como suceso.

# E19-R4.08 — Del atlas a Godot 2D sin carreteras inventadas
**Pipeline propuesto, no implementación.** Godot 4.7.2 Standard (2D) y CoreRPG C++20 conservan versiones y contratos existentes. R4 no toca Game, CoreRPG, ContentPacks ni datos de otras Casas.

## Pipeline autorizado
1. Anclas autorales + cartografía de fuentes (R0).
2. Macro/microrelieve, contextos MF y divisorias (R1), **sin MF-08**.
3. Cuencas HC, cauces existentes/continuidad y receptores (R2; pendientes de localización).
4. Soporte SO, humedad, cubierta CV y efectos ES (R3; no hay instancias actuales).
5. Demanda de tránsito Gd + preguntas Gq (E05/E16/R4).
6. Alternativas no métricas con rechazo por pendiente, suelo, cruces y derecho, nunca «recta óptima» por coste ficticio.
7. **Promoción a Gp** solo si evidencia cartográfica/local, identidad y continuidad de cada tramo, reconocimiento de pasos, obras, derechos, uso y gestor.
8. R5 evalúa asentamientos y servicios **después** de accesibilidad real + agua, saneamiento y empleo.
9. R6 compara Valrik y audita fuentes, cobertura de rutas y deudas reales.
10. E19-TEC crea representación 2D y estados persistentes de rutas acreditadas, con pruebas de guardado/carga y compatibilidad CoreRPG.

## B2, B3 y B4 nunca equivalentes
**B2** = modelos/hipótesis, 12 CT y 8 clases con casos adversariales. **B3** requiere cartografía aceptada, geometrías, continuidad espacial y jurídica, obras identificadas, levantamientos documentados y verificación independiente. **B4** requiere navegación real, segmentos disponibles, estado y memoria persistentes, tránsito NPC/carga y pruebas Windows/Android. Un script que devuelve PASS al JSON solo avala consistencia de B2.

## Tipo de entidad futura RouteSegment
- routeSegmentId estable (no usar CT como ID de tramo), geometryRef, geometryVersion, sourceAuthority, evidenceRefs.
- fromNodeId/toNodeId, parentPhysicalContext, basinId/receiverId si cruza agua, crossingAssetRef con identidad demostrada.
- naturalSurface, supportingSoil, slopeEvidence, seasonObservation, modeAllowed, capacityEvidence.
- landOwner, legalServitude, competentAuthority, restriction, maintainer, lastInspection, repairs.
- authoredStructure versus mutableSurfaceCondition, availability, blockReason, timestamp e historial.
- compatibilidad de vértices, rutas reversibles solo si legal/seguro, alternativa solo si existe.

No fijar todavía geometrías, IDs de instancias, anchos, cotas, tarifas, velocidades, probabilidades de cierre ni tiempos de viaje.

## Validación de conectividad futura
Un camino apto exige que todas las aristas tengan extremos coincidentes y estén aceptadas; que ningún cruce esté UNKNOWN; que tenga permisos para el actor y el modo; que no atraviese terreno excluido; y que estado/horario admitan tránsito. La evaluación de la ruta no muta geografía. Cualquier hueco no se rellena automáticamente. El algoritmo puede declarar «sin ruta acreditada» aunque Gq proponga una pareja.

## Identidad y procedencia
AUTHORED: posición aprobada expresamente por autor/canon. DERIVED: resultado trazable de terreno y reglas. GENERATED: instancia local admisible con semilla y contrato, **sin autorizar canon nuevo**. En todos los casos, la identidad creada se guarda una vez y se referencia desde misiones, tráfico y rumores. Cambiar versión del terreno requiere migración, no mover rutas preexistentes sin expediente.

## Vetas absolutas
No PR #84; no cerrar norte rojo; no MF-08/U7; Rodas Corona; Bosque Real Corona; Bosque Alto solo acceso/autorización probados; no Caleran Dorth, no puerto Karsath ni enlace de agua inventado; no paso Vareth; no medidas Treskal reutilizadas; no Gp derivado de Gq; no afirmar B3/B4 por tests documentales.
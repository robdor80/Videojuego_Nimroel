# E19-R2.06 — Contrato de generación y futura persistencia (solo diseño)

## Contrato de entrada al generador, para E19-TEC/E28
Se requieren: versión de atlas; mosaico de relieve y divisorias *realmente determinado*; lluvias y nieve coherentes con clima; clases de infiltración/suelo verificadas; cobertura boscosa; sistemas mayores canónicos y mapa de receptores/topología validado. Hasta entonces los catorce HS son **SCENARIO_UNLOCATED** y no pueden exportarse como ríos, fuentes ni carreteras de Godot.

## Algoritmo determinista propuesto
1. Bloquear fuentes mayores (Valkram oriental, Lurien, Antela, Hallheim, Golfo) y jurisdicciones de R0/R1. Tratar norte abierto y MF-08 como no evaluables.
2. Para cada celda/región topográfica futura, derivar dirección de pendiente y particiones de aguas; marcar si hay sumidero cerrado con balance explícito.
3. Acumular aportes por lluvia, nieve y almacenamiento; separar escorrentía superficial, infiltración, evapotranspiración y descarga.
4. Identificar convergencias candidatas según relieve y recarga; descartar aquellas sin aportes suficientes o con receptor no resuelto.
5. Seguir aguas abajo sin ciclos; exigir receptor real, lago con salida, humedal con balance o intercambio subterráneo rastreable.
6. Clasificar régimen por continuidad temporal simulada **sin umbral arbitrario de la fase R2**; usar UNKNOWN cuando faltan datos.
7. Evaluar surgencias solo con acuífero/contacto/fractura, recarga y salida. Evaluar humedal solo con depresión y balance.
8. Verificar canon, bosque, Corona, ausencia de calcos PR #84 y NO_B3_B4_CLAIM.
9. Crear identificadores estables de terreno/cauce únicamente en fase técnica autorizada; nombre geográfico solo con procedencia y revisión.
10. Publicar informe de auditoría con los escenarios rechazados, causas y fuentes; no resolver un error añadiendo un «arroyo decorativo».

## Contrato futuro de entidad
Identidad estática: featureId; basinId; physicalType; geometryAndReference; sourceCause; parentFeature; receiverId; directedUpstreamEdges; evidenceRefs; authorityLevel; jurisdiction; regimeClass; editorialStatus; contentVersion; worldStateCompatibilityVersion. Dinámica: timestamp; waterLevel; dischargeClass; active; frozen; sedimentLoadClass; storage; eventCause; lastUpdateRevision. **Ninguna de esas entidades ha sido creada en R2**: JSON contiene únicamente escenarios tipológicos y nulidades expresas. Un cauce seco sigue existiendo como accidente físico; se modifica su estado activo, no se borra y regenera.

## Invariantes de compatibilidad
- Un ID histórico de una fuente/cauce materializado no se recicla; si se corrige su trazado se requiere migración y procedencia.
- Relaciones transfronterizas deben distinguir hidrología natural de jurisdicción administrativa.
- Una ruta, un muelle, una bodega o una aldea requiere su contrato propio y permiso; jamás aparece por ejecutar hidrología.
- Un cambio climático altera aporte y riesgo, no la secuencia canónica del Lurien ni la corona de Rodas.
- La geometría futura no invierte pendiente para encajar una misión; el guion se ajusta a la geografía.
- El guardado debe ser reproducible con semilla y versión cuando se habilite generación. No prometer semilla/algoritmo activo aquí.

## Puertas técnicas posteriores
E19-TEC debe demostrar gradiente de drenaje, conservación aproximada de masa, ausencia de ciclos, resultados deterministas, continuidad entre escenas, casos de sumidero válido, coexistencia de segmentos secos y activos, compatibilidad con World State y denegación de entidades no verificadas. R2 solo verifica el **contrato semántico documental**. Godot 4.7.2 2D y CoreRPG C++20 continúan intactos.

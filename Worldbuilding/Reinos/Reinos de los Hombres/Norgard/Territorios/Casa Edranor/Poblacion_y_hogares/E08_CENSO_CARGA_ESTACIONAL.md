# E08 — Población pendiente, presencia y capacidad estacional

## Estado de la cifra
`EDD-04` sigue **abierta**. No hay censo aprobado para Dorth, Lumina, Karsath, Rodas ni para el total de Casa Edranor. Tampoco existen promedios de integrantes por hogar, estructura etaria, habitantes rurales totales o porcentajes urbano/rural. Los rangos demográficos fijados para Darovan **no se transfieren**. La población de Rodas, si se censara, corresponde a **Corona Aethros** y no se sumaría al total fiscal/jurisdiccional de Edranor sin distinguir contexto geográfico.

## Contadores distintos
- `residentsAtCutoff`: identidades de residencia habitual en el instante de corte, no las personas presentes en cada escena.
- `presentVisitors`: visitantes sin residencia habitual local, contados una sola vez para consumo; no se suman al censo residente.
- `seasonalWorkers`: **subconjunto** de residentes o visitantes, nunca tercera población sumada por defecto.
- `temporaryLodgers`: **subconjunto** de visitantes con derecho de cama; no un duplicado de viajeros/temporeros.
- `jobsFilled`: plazas efectivas, no número de personas; una persona puede tener varios trabajos pero no dos turnos simultáneos.
- `householdMembers`: relación de convivencia, no suma de personas únicas fuera de su residencia.

## Ciclo estacional cualitativo
**Vendimia:** trabajo estacional potencial en Dorth/Lumina/Karsath, solo cuando la parcela y cosecha estén validadas; la capacidad de alojamiento, alimentación, agua y descanso limita la contratación. **Mercado anual de Lumina:** aumenta temporalmente la demanda de espacio, hospedaje, reparación y servicios; E07 no fija fecha, puestos ni número de asistentes. **Invierno y frío septentrional:** presionan combustible, cobijo, abastecimiento y salud, con especial atención a Rodas; sin atribuir tasas, clima exacto ni carreteras. **Baja actividad:** reduce encargos pero no elimina a los residentes ni inventarios reales.

## Fórmulas de auditoría, no población canónica
`P_presente = |residentes presentes ∪ visitantes presentes|`, sobre `PersonId` distintos; `P_alojado = |residentes alojados ∪ visitantes alojados|`. Un temporero con vivienda habitual en Lumina y jornada en Dorth figura como residente solo en Lumina, presencia de Dorth cuando esté allí, y fuerza laboral solo en turnos disponibles. La reserva de demanda futura no es NPC.

`Camas_libres = camas_físicas_habilitadas - ocupantes_con_cama`. `Capacidad_servicio = mínimo de recursos, personal, derechos, acceso y tiempo`. Si cualquiera de los operandos reales es `UNKNOWN`, el resultado operativo no se publica. Los números de fixtures E08 son **hipótesis unitarias sintéticas**, nunca edades demográficas, camas, caudales o habitantes reales.

## Decisiones para el autor
EDD-04 exige aprobaciones explícitas: cifras o intervalos por jurisdicción/localidad, tamaños medios y variabilidad de hogares, censo rural, épocas y volumen de demanda y tecnología local de abastecimiento. E09 no podrá usar «contribuyentes» deducidos de poblaciones no aprobadas.

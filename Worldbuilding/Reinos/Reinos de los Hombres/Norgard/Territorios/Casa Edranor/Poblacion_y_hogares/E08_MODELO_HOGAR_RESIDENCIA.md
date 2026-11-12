# E08 — Hogar, vivienda, residencia y cuidados

## 1. Entidades separadas
`PersonId` identifica a la persona única de World State; `HouseholdId`, una unidad **de convivencia y cooperación**; `DwellingId`, una vivienda física; `ResidenceId`, la relación efectiva persona–lugar; `TenureId`, el derecho de ocupación o uso; `JobAssignmentId`, el trabajo; `BusinessId`/ `ProviderId`, la actividad. Son **interfaces propuestas para E11**, no identidades emitidas ni API CoreRPG confirmada. Un hogar puede ser unipersonal, familiar, multigeneracional o de convivientes sin parentesco. Familia, matrimonio, paternidad, hogar, empleo, propiedad y ocupación jamás se equiparan.

## 2. Derechos y capacidad
Norgard regula matrimonio civil, tutela, filiación, propiedad, herencia y alquiler. La residencia no convierte al ocupante en propietario; el gobierno de Casa no convierte al señor en dueño de todas las casas. Los niños y dependientes no son bienes. Un matrimonio no nace por vivir juntos. Una persona puede compartir vivienda y pertenecer a otro hogar solo si la futura regla de asignación lo acredita: **una única residencia habitual activa para el censo de corte**, sin prohibir desplazamiento ni estancias. El recuento requiere identidad estable; jamás duplicar una persona al aparecer en bodega, casa, posada y taberna.

## 3. Ciclo residencial propuesto
`evidencia de vivienda y uso → capacidad habitable y agua → derecho de ocupación → aceptación/convivencia → ResidenceRecord autorizado → cambio persistido por CoreRPG`. Fallecimiento, traslado, adopción, tutela, separación, arrendamiento, expulsión y retorno requieren sus hechos jurídicos y físicos; ningún hecho se deduce de un diálogo o de un generador. Una casa deshabitada puede existir sin hogar; una familia no acredita un edificio.

## 4. Necesidades diarias
Comida, agua potable, descanso/cama, calor/combustible apropiado al clima, higiene/saneamiento, cuidados de dependientes, tiempos de trabajo y tareas domésticas consumen recursos y horas. Las tareas domésticas se asignan según competencia y disponibilidad, no según sexo ni apellido. Enfermos, personas mayores, niños o transeúntes no se convierten automáticamente en empleados ni en dependientes permanentes.

## 5. Cierre por capacidad
Para aceptar un escenario real: camas **residenciales** ≥ residentes simultáneos; camas de visita ≥ visitantes alojados; agua segura, alimentos y capacidad de evacuación de residuos ≥ demanda total efectiva; disponibilidad de personal y tiempo ≥ turnos y tareas asignadas. Las unidades y consumos por persona deben ser aprobados técnicamente: **ningún caudal, ración, densidad, número o duración es canon E08**. `UNKNOWN` bloquea la instanciación real; no se interpreta como infinito ni como cero.

## 6. Proyección de contenido
Una misma persona podría trabajar en Dorth y vivir fuera, o llegar a Lumina por la feria; solo se contará una vez como residente del hogar habitual y como presencia temporal cuando corresponda. Los libros comerciales y de residencia deben enlazar la misma persona. No inferir movimientos a partir de los enlaces hipotéticos E05.

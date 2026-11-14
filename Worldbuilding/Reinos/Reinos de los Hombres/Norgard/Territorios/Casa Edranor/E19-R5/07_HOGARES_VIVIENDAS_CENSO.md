# E19-R5.07 — Hogares, vivienda, residencia, censo y vida social
## Identidades únicas
No confundir `PersonId`, `HouseholdId`, `DwellingId`, `ResidenceId`, `TenureId`, `JobAssignmentId`, `ProviderId` y `SettlementId`. E08 los concibe como **interfaces propuestas**, no API CoreRPG ya verificada. Una persona puede vivir en un sitio, trabajar en otro, hospedarse temporalmente en tercero, acudir a un mercado en cuarto; solo cuenta una vez en la residencia habitual del censo de corte.

## Orden de personas a edificios
Valrik/Treskal recomienda población → unidades domésticas → viviendas → talleres/anexos, con función y persistencia. En Edranor **no se importa** su media 4,3–5,2 ni su intervalo 2–8: EDD-04 no ha aprobado tamaños de hogar ni totales. Una vivienda puede albergar familia extensa, personas solas, aprendices y convivientes sin parentesco; convivencia no crea matrimonio, paternidad, propiedad o relación laboral. Una herrería dentro de casa no es otra vivienda; un establo no añade camas. Un edificio vacío requiere una historia/estado y no justifica crecimiento artificial.

## Censo y presencia
- **Residentes habituales:** miembros únicos con residencia vigente y jurisdicción acreditada.
- **Presentes:** residentes presentes más visitantes presentes, como conjuntos de IDs sin repetición.
- **Temporeros:** subconjunto de personas presentes según trabajo, NO «tercer censo».
- **Alojados:** quienes ocupan cama real autorizada; la visita consume agua y saneamiento.
- **Trabajos:** asignaciones/turnos; no equivalen al número de personas.
- **Rodas:** puede contarse en mapas de interacción como nodo regio, pero nunca sumarse silenciosamente al total fiscal Edranor.
Nada de lo anterior autoriza un número real hoy.

## Vivienda digna y restricciones
Cubierta/calor, descanso/camas, ventilación razonable, agua potable, evacuación de residuos, acceso de emergencia, estabilidad de suelo, seguridad ante fuego y riesgo estacional. La ayuda doméstica/parental depende de disponibilidad real y acuerdos, no se asigna por sexo. Necesidades de menores y dependientes no transforman a la persona en mercancía o puesto de trabajo.

## Migración y cambio
Nacimiento, muerte, mudanza, arrendamiento, separación, acogida, cambios de oficio o viaje afectan relaciones distintas: el motor debe actualizar la **identidad estable**, la vivienda y los contadores oportunos; no borrar/recrear NPC para cambiarles de casa. Información que conoce el jugador y hechos del World State se separan, igual que en viaje R4. Cualquier migración real exige procedencia narrativa/evento y disponibilidad de cama, alimento, derecho y transporte.

## Puertas para instancia B4
Censo aprobado; entradas de personas únicas; hogares sin duplicados; residencias actuales; viviendas con capacidad; propietarios y ocupantes diferenciados; agua, combustible, comida, saneamiento, tareas, servicios, trabajo, ruta y estados; guardar/reanudar conservando identidad y cambios. Nada de esto se declara ejecutado por esta monografía.

# E15 — El trabajo de las personas y la economía del hogar

## Trabajo de hogar, negocio y estación
Los oficios de E04/E08 describen **funciones candidatas**: cuidador de viña, recolector, prensador, encargado de bodega, tonelero, carpintero, herrero, almacenero, tratante, registrador, carretero, molinero, hornero y reparador. No son NPC, nóminas ni gremios generados. Una familia puede combinar autoconsumo, venta de excedentes, jornada contratada y mantenimiento, pero **el mismo trabajador no se duplica**.

Modelo de jornada futuro: `PersonId + JobAssignmentId + intervalo + lugar + aptitud + autorización + descanso + desplazamiento + cuidados`. La suma de intervalos incompatibles se rechaza antes de simular producción. El jornal recibido no crea alimento si el mercado no dispone de existencias. Un oficio se activa por necesidad, insumos, responsabilidad y contrato, no porque el nombre aparezca en un cartel.

## Edad y salvaguardas del canon de Norgard
| Edad | Participación admitida según E08 |
|---|---|
| 0–7 | sin trabajo ni aprendizaje formal |
| 8–11 | ayuda ligera/observación, nunca cobertura de vacante |
| 12–14 | aprendizaje supervisado, mentor y tutor; no puesto autónomo |
| 15–17 | empleo limitado con consentimiento y seguridad; no tareas peligrosas sin idoneidad |
| 18+ | capacidad contractual general, pero destreza y disponibilidad deben probarse |

La deuda no genera servidumbre; no asignar a menores las tareas peligrosas de tala, prensas o hornos por falta de adultos. Si una contratación falla, la producción se limita: el sistema no recluta trabajadores espontáneos.

## Presupuesto físico y financiero, separados
**Libro físico:** existencias de alimentos, barricas, grano, leña, agua disponible, uva, herramientas y tiempo. **Libro monetario:** créditos y deudas en moneda real de Norgard: Clavo, Luna (24 Clavos) y Corona (480 Clavos). Un recibo de deuda no es una barrica; una cuenta en positivo no asegura que un granero esté lleno. E15 no crea precios ni salarios fijos.

## Cuidados y necesidades previas
Comida, agua potable, descanso, vivienda habitable, saneamiento y cuidado de dependientes forman el costo material previo a cada temporada. La llegada de temporeros requiere cama verificada, alimentación, capacidad y acuerdo: una bodega no puede convertir trabajo disponible en alojamiento infinito. La presión laboral debe repercutir en tareas domésticas y mantenimiento, pero sin fijar estadísticas de habitantes que corresponden a E26.

## Interacciones y conflictos discretos
- **Trabajo de vendimia o reparación:** compete por el mismo horario de una persona; una prioridad desplaza otra.
- **Aprendiz de tonelería:** solo produce con supervisión; no suplanta al oficial.
- **Cuidar a un enfermo:** reduce disponibilidad en un hogar sin eliminarlo del censo ni inventar diagnóstico.
- **Préstamo de carro o herramienta:** hay propietario, autorización, reserva temporal y devolución.
- **Pago aplazado:** registra obligación, no transferencias físicas inexistentes.

Estos escenarios servirán a E17 para cadenas hogar–negocio–administración–memoria y a E26 para vincular hogares reales, sin ejecutarse aquí.

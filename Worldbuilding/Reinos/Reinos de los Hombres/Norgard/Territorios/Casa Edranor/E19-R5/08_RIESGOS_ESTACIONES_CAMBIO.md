# E19-R5.08 — Estacionalidad, riesgos y transformación de la ocupación
## Calendario causal, no efectos automáticos
**Vendimia:** solo hay necesidad extraordinaria de mano de obra si existen cosecha, parcelas, acceso, empleadores y alojamiento. De otro modo, presión potencial. El pico de camas y agua no se traduce en una aldea nueva.
**Feria anual de Lumina:** el espacio de plaza está en E07, pero fecha, comerciantes y asistentes no están fijados. El efecto sobre hospedaje, saneamiento y tránsito requiere datos y eventos.
**Frío septentrional:** combustible, cubierta, ropa, reserva, accesibilidad y enfermedad condicionan ocupación de MF-07/Rodas; sin nieve «siempre activada» ni inventar tundra MF-08.
**Barro, avenida, erosión y helada:** dependen de suelos/agua/estación concretos de R2–R3, exposición y mantenimiento. No se producen por ser invierno o por anotar un riesgo.

## Ciclos que deben poder alterar cobertura
- Desabastecimiento de agua → consumo restringido → trabajos/servicios reducidos → necesidad de reparación o suministro alternativo *si existe*.
- Camino Gp cortado → accesibilidad temporal perdida → almacenamiento y mensajería retrasados, sin cambiar el grafo Gq.
- Vendimia autorizada → visitantes/temporeros aumentan **presencia** → camas/saneamiento/mercado compiten por recursos.
- Corta forestal autorizada → extracción limitada → regeneración → capacidad del bosque en revisión.
- Incendio/inundación/rotura → daños a inmueble real → desplazamiento o reparación con coste y actor.
Son **cadenas de diseño**, no episodios históricos, misiones activas ni relojes ejecutables.

## Máquina de estados futura
`UNASSESSED → EVIDENCE_PENDING → VERIFIED_SITE → OCCUPIED → IMPAIRED/REPAIRED/ABANDONED` es vocabulario conceptual, no transición automática. Cada paso exige registro de fuente, autoridad, fecha, objeto, causa, versión y posible revocación. No pasar de `UNASSESSED` a `OCCUPIED` porque la IA narre «casas» o el mapa muestre tejados.

## Compromisos de consistencia
- Riesgo desconocido ≠ amenaza activa; amenaza activa ≠ daño sin exposición.
- Accesibilidad desconocida ≠ vía cerrada; vía cerrada requiere tramo físico existente.
- Un evento de cosecha no crea litros, precios o jornaleros sin capacidad.
- La población de madrugada y de mercado difiere sin duplicar residentes.
- Una crisis no autoriza traspasar jurisdicción regia ni extraer madera protegida.
- El estado cambia por hechos y se persiste una vez; las escenas cargan el mismo estado.

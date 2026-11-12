# D.P24 — Vida rural del territorio Darovan

**12/11/2026 · fase de autoría editorial rural, con delegación creativa expresa.** Base independiente: `main` en `512434957f248f2513761615a9685ddd6c49c65f`. D.P23/Treihord continúa en PR Draft #46 al iniciar este trabajo: no está incorporado a esta rama ni se presume fusionado. **Sin edición de CoreRPG, Godot, mapas ni entidades de WorldState.**

## Qué se entrega
- [01 · Territorios, nueve comunidades objetivo y límites](01_comunidades_y_paisajes.md): identidades propias, sin aldeas materializadas.
- [02 · Hogares, ritmo diario y año de trabajo](02_hogares_tiempo_y_estaciones.md): economía de cuidados, diversidad doméstica y dependencia estacional.
- [03 · Oficios, recursos y diez circuitos materiales](03_oficios_economia_y_abastecimiento.md): bienes finitos, custodia, acceso y fallos.
- [04 · Doce biografías y relaciones](04_personas_y_relaciones.md): individualidad, conocimiento, redes y fricción.
- [05 · Cuatro memorias privadas y cinco arcos](05_memorias_y_conflictos.md): conflicto humano sin convertir posibilidades en Historia.
- [06 · Ocho escenas multirrol](06_escenas_rurales_multirrol.md): decisiones, respuestas y rechazos legítimos, solo TEST_ONLY.
- [07 · Contratos, protección del canon y auditoría](07_autoridad_cartografia_y_traspaso.md): condiciones verificables para materialización.
- [08 · Acta de decisiones delegadas](08_decisiones_editoriales_delegadas.md): selección creativa aprobada editorialmente, límites explícitos.
- [Inventario de autoría JSON](../../Datos%20operativos/darovan_dp24_rural_editorial_v0.1.json) y validador en `Tools/DarovanDP24/validate.py`.

## Carácter del campo
Darovan no es un anillo invisible de granjas que reabastece automáticamente a las ciudades. La vida rural tiene hogares, propiedades y permisos concretos, recolecciones inciertas, caminos restringidos por la geografía, favores que se recuerdan, trabajo estacional, pérdidas irreversibles y personas con motivos distintos. No todos trabajan la tierra ni todas las familias desean permanecer en su lugar de origen.

## Autoridad y vocabulario
1. `AUTHORED_EXISTING`: solo hechos acreditados en Norgard, Darovan D00–D12 y D.P13, más decisiones previamente ratificadas.
2. `AUTHORED_EDITORIAL_BASE`: nombres, biografías, recuerdos privados e identidad literaria nuevos **seleccionados gracias a la delegación creativa del autor**. Son referencias para crear contenido futuro, no afirmaciones de que hoy existan en el mundo.
3. `FUTURE_OBJECTIVE_CONDITIONAL`: núcleos, lugares e instalaciones con identidad propuesta; exigen sitio, derecho, recursos, comunidad y aprobación de materialización.
4. `TEST_ONLY`: escenas y bifurcaciones hipotéticas; nunca acontecimientos consumados.
5. `UNKNOWN`: ubicación, coordenadas, inventario, proveedores, viviendas, población local, relaciones reales, carreteras no confirmadas y estado persistente. `null` es desconocido, no cero.

**La aprobación editorial no crea un asentamiento.** D06 exige cinco puertas de existencia; D08 exige hogar y proveedores reales; D09/Norgard prevalecen en fiscalidad, seguridad y justicia. La IA no concede recursos. CoreRPG será autoridad lógica y de persistencia en la integración futura.

## Confines protegidos
Cuatro ciudades canónicas: **Treihord, Veldora, Taramin y Syvaris**. Karsath no pertenece a Darovan. El Bosque de las Agujas no tiene asentamientos permanentes interiores. Los Pilares son un solo bosque; Taramin tiene un solo bosque meridional; Arven (Darovan) conserva el Manto Verde de aproximadamente el 90 % y aldeas existentes, concentradas en la costa interior. Belara pasa junto a Treihord y solo se acredita barcaza somera industrial. No hay ferris, puentes, minas, carreteras, muelles, cosechas, animales ni guardias creados por este documento.

## Precondiciones de cierre
Validación de JSON e IDs; correspondencia con las nueve clases D06; referencias a zonas D01; consistencia de estados; prohibición de geometrías, inventarios o runtime ficticios. CI del HEAD de la PR, regresiones vigentes y revisión del diff. Esta fase solo concluye **documentalmente**; su fusión exige autorización independiente conforme al protocolo Darovan. D.P25 podrá tomar estas biografías como candidatas a historias territoriales, sin convertirlas en NPC persistentes por referencia.

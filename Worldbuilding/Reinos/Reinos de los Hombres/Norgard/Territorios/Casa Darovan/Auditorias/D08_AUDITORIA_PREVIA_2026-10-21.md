# DAROVAN D08 — Auditoría previa (21/10/2026)
**Estado:** contraste documental y estático, NO canon nuevo, NO ejecución del juego. Base verificada: `main` `23670e68532447d918c04839369a9962448f2e44`; D07 PR #32 fusionada.

## Entradas obligatorias contrastadas
- `00_Control_del_proyecto/TRASPASO_D08.md`, REGISTRO_FASES, DECISIONES_Y_BLOQUEOS, PLAN_DESARROLLO, D06/D07 y sus JSON y validadores.
- Norgard, ley común: familia (Punto 6), capacidad/trabajo (Punto 7), propiedad (Punto 8), salud (Punto 9); Norgard Defaults operativos correspondientes.
- `Norgard/Sociedad/aldeas_servicios_y_economia_local.md` (servicios rurales canónicos), Nimroel Core `RES/MOVE`, `KIN`, `DEP/CARE`, `CHORE/DOM`, `EMP`, `APR`, `NEED`, `WAIT`, `TXN/OBL/LED`, `OWN`, `FOOD`, `WASTE`.
- CoreRPG `robdor80/CoreRPG` (main 21/10/2026): `docs/adr/0003-generic-population-relations.md`, `include/corerpg/entity_structure.hpp`, `include/corerpg/world_state.hpp`, `src/population.cpp`, `include/corerpg/persistence.hpp`.

## Hallazgos y contradicciones resueltas por precedencia
1. Traspasos D06–D08 y algunos encabezados de REGISTRO/PLAN contienen estados **históricos** (PR todavía Draft, D05 sin fusionar). La realidad de GitHub comprobada prevalece: D00–D07 ya fusionadas. No se reescribe documentación histórica de las fases.
2. CoreRPG **implementa** EntityId, WorldState, relaciones dirigidas con `RelationKind` uint64 asignado por consumidor, población agregada con reserva/invidualización y persistencia de esos hechos. El Core NO implementa semántica jurídica de matrimonio/hogar/empleo ni motor económico de stock o servicio en la API examinada. Los contratos JSON de Nimroel Core son diseño documental, no prueba de soporte runtime.
3. Norgard: convivencia no implica parentesco; matrimonio no implica co-residencia; propiedad, tenencia, ocupación y custodia difieren. Edad: 18 adultez; aprendizaje formal desde 12, empleo juvenil limitado desde 15. Prohibido automatizar un "cabeza de familia" universal o roles domésticos por sexo.
4. Servicios: acceso plausible a agua ≠ pozo construido; atención familiar ≠ curandera profesional; servicio sanitario ≠ hospital; aprendizaje ≠ escuela; taberna ≠ posada; dependencia logística ≠ ruta, y falta de abastecimiento ≠ inventario ficticio. La excepción de herreros de Treskal y de posadas de Valrik NO rige Darovan.
5. D07 permite cuatro ciudades manuales; solo Treihord ~32.000 habitantes. Ninguna población o proporción de hogares para otras ciudades, villa/pueblo/aldea o total de Casa ha sido aprobada. D06 son nueve modelos, seis casos `TEST_ONLY`, no nuevos asentamientos.
6. D05 confirma un vínculo vial Veldora–Treihord, transferencia somera Belara y galería custodiada Vena; el resto de relaciones de suministro no acredita una carretera. Taramin Thalen de dos brazos sin navegación probada; Syvaris puerto seguro y presencia naval de Norgard.
7. Riesgos de simulación: contar dos veces a residentes viajeros, tratar poblaciones latentes de CoreRPG como NPC creados, derivar empleo de profesión, propagar propiedad por matrimonio, atribuir automáticamente cuidador o stock, materializar edificios sin evidencia.

## Salida y bloqueos
Se diseñan modelos de evaluación y contratos **de planificación** para no crear habitantes canónicos. Permanecen `UNKNOWN` población total, poblaciones de Veldora/Taramin/Syvaris, rangos por núcleo, números de hogares, porcentajes laborales, capacidades, emplazamientos, salarios concretos, geometría y movilidad efectiva. Se plantean decisiones sustantivas al autor, sin bloqueo de la validación estática.

**Jerarquía:** Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State. Solo CoreRPG podrá gobernar el estado lógico cuando la integración realmente exista.

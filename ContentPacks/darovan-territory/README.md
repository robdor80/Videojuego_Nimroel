# Casa Darovan — D11, proyección estructural 0.1.0

Publicación de laboratorio no jugable, derivada de D00–D10. Se ha conservado íntegro el canon previo. Pack nimroel.darovan.territory con cinco identidades estables: Darovan y Treihord, Veldora, Taramin, Syvaris. Las referencias tipadas son solo enlaces de catálogo, no enlaces físicos de transporte.

El sidecar authoring/projection-v0.1.json fija once fuentes de fases mediante SHA de blob Git, invariantes de hidrografía, ciudad, movilidad, autoridad y estados de las funcionalidades pendientes. No se incorpora como propiedad ResourceDefinition porque el Content Contract JSON 0.1.0 prohíbe payloads adicionales. Los 8 scenarios TEST_ONLY especifican casos futuros sin declarar ejecución.

Herramientas: python Tools/DarovanD11/validate.py --core-root .darovan-core (requiere jsonschema 4.26.0 y checkout CoreRPG fijo), y CMake Tools/DarovanD11 para prueba real de catálogo C++ aislada. Las mutaciones negativas no son pruebas de reglas económicas o socioculturales.

La pertenencia de Arven a Darovan está aprobada, pero su identidad cultural sigue UNKNOWN; no incluir población o eventos reales. Nunca convertir relación de suministro D05 en carretera ni inventar aduanas interiores. El Content Pack de Treskal 4.13 es precedente técnico independiente, no dependencia física de este pack.

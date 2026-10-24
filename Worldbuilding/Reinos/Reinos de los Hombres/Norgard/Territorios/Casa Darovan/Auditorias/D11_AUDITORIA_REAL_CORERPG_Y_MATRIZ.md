# D11-A — Matriz de compatibilidad Darovan / CoreRPG (revisión de código)

Fecha: 23-10-2026. Nimroel main base a5d25d8e6a1d70015a63b0327837fd0da0004cbd; CoreRPG main fijo 4f282863737bcd8f5add401202a9e1064c133672 (4.13 fusionada). Documento de auditoría, no prueba de ejecución total.

**Lectura:** los estados describen la CAPACIDAD COMPLETA de cada dominio, no la existencia de alguna clase próxima. Solo una primitiva acotada puede alcanzar IMPLEMENTADO Y PROBADO. Las pruebas C++ específicas D11 deben verificarse en Actions antes de afirmar éxito.

| Fase / dominio Darovan | Fuente técnica | APIs CoreRPG realmente identificadas | Estado del DOMINIO | Falta y responsable |
|---|---|---|---|---|
| D00 Control de canon y ámbito | darovan_d00_canonical_anchors_v0.1.json + bootstrap | ContentCatalog / DefinitionId, únicamente identidad | SOPORTADO PARCIALMENTE | Procedencia, jurisdicción y límites en sidecar Nimroel; Host valida publicación |
| D01 Geografía, relieve y Arven | darovan_d01_relief_profile_v0.1.json | Ninguna API de geometría, límites o cartografía; EntityId no es un lugar | SOLO CONTRATO DOCUMENTAL | GIS, espacio y localización: Nimroel/Host y eventual Core genérico |
| D02 Cinco ríos / cuatro sistemas | darovan_d02_hydro_network_v0.1.json | Ninguna API hidrológica o navegación; relaciones tipadas no aportan semántica fluvial | SOLO CONTRATO DOCUMENTAL | Topología, navegación y magnitudes desconocidas: Nimroel/autor |
| D03 Clima y ecosistemas | darovan_d03_climate_ecosystems_v0.1.json | RandomStreams puede reproducir tiradas, pero NO clima, biomas ni estaciones | DEPENDENCIA NO IMPLEMENTADA | Simulación ambiental y calendario genérico, datos Nimroel sin inventar cifras |
| D04 Recursos, minería, Crisol, fiscalidad | darovan_d04_resources_production_v0.1.json | WorldState contención, ActionEngine PlaceEntity; NO stock, propiedad, transformación, dinero ni contabilidad | DEPENDENCIA NO IMPLEMENTADA | Inventarios, economía, producción y transacciones: futuros dominios de CoreRPG; canon local Nimroel |
| D05 Caminos, barcaza y suministros | darovan_d05_mobility_communications_v0.1.json | WorldState contención, Simulation::step orden explícito; NO grafos, ruta, costes ni mensajes | SOPORTADO PARCIALMENTE | Sistema movilidad/comunicaciones Core/Host; no convertir suministro en tramo físico |
| D06 Nueve modelos de asentamiento | darovan_d06_settlement_rules_v0.1.json | RandomStreams/Population/EntityId sí, generación de asentamientos NO | SOPORTADO PARCIALMENTE | Generador Nimroel, validación regional/semillas; no promover fixtures a canon |
| D07 Cuatro ciudades canónicas | darovan_d07_canonical_cities_v0.1.json | Pack 0.1.0 + DefinitionId, ContentCatalog, binding de entidad; no atributos urbanos | SOPORTADO PARCIALMENTE | Índice D11 aporta 5 definiciones; reglas urbanas y WorldState de ciudad requieren adaptador/host |
| D08 Población, hogares, oficios, servicios | darovan_d08_population_services_v0.1.json | declare_population, materialize_population, add_relation, PopulationMembership/Persistence; etiquetas sin empleo, casa o parentesco semántico | SOPORTADO PARCIALMENTE | Residencia, empleo, familia, demanda, stock, traslado de hogar: CoreRPG por decidir/implementar |
| D09 Gobierno, justicia y seguridad | darovan_d09_governance_security_v0.1.json | ActionRequest actor es origen lógico, no permiso; RuleCheck solo estructural, sin jerarquía ni política fiscal | DEPENDENCIA NO IMPLEMENTADA | Autoridad, autorizaciones, presupuesto, órdenes, custodia, justicia y fiscalidad Core/Nimroel |
| D10 Cultura y personalidad autónoma | darovan_d10_culture_society_v0.1.json | learn_fact, Visibility::project, ContextBuilder::build; solo hechos estructurales. Nada infiere actitudes, creencias o relaciones sociales | SOPORTADO PARCIALMENTE | Personalidad, aprendizaje cultural, relaciones afectivas, expresión y autonomía: Core/IA/Host |

## Capacidades genéricas existentes, comprobadas por firmas/código

- ResourceDefinition tiene exactamente DefinitionId y ResourceKind. La versión JSON 0.1.0 solo admite id/kind/references, nunca los ricos valores de dominio.
- ContentCatalog::create y content_json::load_content_catalog validan estructura y enlaces; NO ejecutan referencias semánticas.
- WorldState emite EntityId, contiene entidades, admite bindings, relaciones numéricas y poblaciones agregadas. Los ID son relativos a un mundo, no globales ni IDs de canon.
- ActionEngine::process opera contención/relaciones/tiradas; Simulation::step procesa lotes de manera explícita. Ninguna de ambas aplica reglas Darovan.
- Persistence::capture/serialize/load conserva estructuras admitidas por Core v1/v2/v3; no guarda JSON de canon, tablas de stock o propiedades de hogar. Host controla el preflight de contenido y el almacenamiento.
- Knowledge/Visibility/ContextBuilder son fronteras de hechos estructurales, no implementaciones de personalidad o diálogos.
- CoreRPG 4.13 (prueba de Treskal, tests/nimroel_content_pack_test.cpp) acredita precedente de catálogo, binding, observadores y guardados sintéticos; NO acredita todavía Darovan.
- NIM-06_PREPARACION_NATIVA.md acredita laboratorio Windows GDExtension y empaquetado Android ARM64; no acredita ejecución física de Darovan, ni prueba Samsung.

## Estados de evidencia

IMPLEMENTADO Y PROBADO: primitivas genéricas del Core verificadas por su repositorio y la suite 4.13, sin reclamar su equivalencia a reglas de dominio. IMPLEMENTADO SIN PRUEBA SUFICIENTE: integración física específica Darovan antes del cierre CI D11. SOLO CONTRATO DOCUMENTAL: geografía/hidrología/canon cualitativo. DEPENDENCIA NO IMPLEMENTADA: producción, fiscalidad y personalidad dinámica. BLOQUEADO POR CANON PENDIENTE: rutas/geometrías nuevas, minas localizadas, censos exactos, cultura Arven, autoridades/actores nominales, costes y magnitudes.

**No confundir:** validación Python/JSON = coherencia documental; C++ del catálogo = carga real de 5 sobres; WorldState TEST_ONLY = instancia sintética, nunca historia de Nimroel.

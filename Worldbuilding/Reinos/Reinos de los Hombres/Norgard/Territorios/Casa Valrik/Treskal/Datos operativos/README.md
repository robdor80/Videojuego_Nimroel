# Datos operativos — Treskal ciudad

Treskal es una ciudad canónica diseñada manualmente.

Los JSON de esta carpeta **no son reglas para generar una ciudad aleatoria**. Representan la estructura estable que deberá respetar el diseño manual y, más adelante, el RPG Core.

## Archivos

- `treskal_city_structure_v0.1.json` — topología, sectores funcionales, flujos, mercados, infraestructura urbana, guardia y justicia.
- `treskal_city_design_invariants_v0.1.json` — pruebas de coherencia para futuras revisiones del plano.

## Regla

Los detalles aún no fijados aparecen explícitamente en `unresolvedByDesign`.

No deben rellenarse automáticamente por una herramienta sin pasar por la fase de diseño correspondiente.

- `treskal_street_interior_activity_contract_v0.1.json` — corredores, interiores y activity anchors.
- `treskal_access_and_world_state_contract_v0.1.json` — clases de acceso P0–P5 y contrato de World State.
- `treskal_city_manifest_v0.1.json` — índice maestro de todos los contratos operativos.
- `treskal_population_and_security_matrix_v0.1.json` — pesos relativos de población/actividad y prioridad de seguridad por Z01–Z14.
- `treskal_information_and_reputation_contract_v0.1.json` — propagación de información, rumores y reputaciones por red social.
- `treskal_urban_gameplay_discovery_contract_v0.1.json` — descubrimiento orgánico, investigación y oportunidades emergentes.
- `treskal_labor_household_visitor_contract_v0.1.json` — familias de ocupación O, hogares H y visitantes V.
- `treskal_civil_port_and_storage_contract_v0.1.json` — ciclo de embarcaciones civiles, carga y clases de almacenamiento ST1–ST6.

- `treskal_housing_social_geography_contract_v0.1.json` — asignación residencial, mezcla social y mudanzas.

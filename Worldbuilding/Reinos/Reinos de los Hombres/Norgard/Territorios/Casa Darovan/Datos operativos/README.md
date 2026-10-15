# Datos operativos — Casa Darovan

Perfiles de referencia **NO RUNTIME** bajo Core → Norgard Defaults → Darovan → Localidad → World State.
- `darovan_bootstrap_manifest_v0.1.json` y `darovan_d00_canonical_anchors_v0.1.json`: índices D00.
- `darovan_d01_relief_profile_v0.1.json`: relieve D01, integrado por PR #15.
- `darovan_d02_hydro_network_v0.1.json`: grafo topológico D02 integrado por PR #16 (4 ríos, 3 sistemas, 13 nodos, 10 aristas), SIN polígonos/caudales/afluentes/entidades jugables.
- `darovan_d03_climate_ecosystems_v0.1.json`: **12 unidades D01 cualitativas**, referencias Core/Norgard/D01/D02 y límites ambientales; sin temperaturas, lluvia, suelos, especies, ríos ni runtime.
Consultar `../Hidrografia/README.md`, `../00_Control_del_proyecto/REGISTRO_FASES.md` y el contrato original Nimroel Core.

- `darovan_d04_resources_production_v0.1.json`: 12 unidades D01, 8 cadenas y 19 fuentes, planificación sin nuevos recursos cuantificados ni ejecución del motor, PR #20.

# D.P15 — Red regional de asentamientos, servicios y abastecimiento

**Estado:** modelo funcional de planificación, sin proveedores o localidades nuevas.

## Comparación obligatoria con Valrik

En Valrik se cerró por separado el esqueleto de aldea, pueblo y villa, sus posibilidades, criterios de servicio regional, pesos y persistencia. Darovan **ya posee nueve familias de modelos D06 y D08 para hogares, profesiones y necesidades**. Esta fase no creará un segundo generador ni importará los mínimos demográficos de Valrik; los articula en una red de cobertura que no presume rutas inexistentes.

## Siete capas (orden invariable)

1. **esqueleto_minimo**: comprobar mínima comunidad real, agua y función.
2. **posibilidades**: determinar opciones sin existencia automática.
3. **filtros_fisicos_ley_y_compatibilidad**: superar D.P14 y derechos territoriales.
4. **coherencia_regional**: resolver demanda y servicios existentes de municipios vecinos.
5. **pesos_de_d06**: considerar solo pesos cualitativos 0–4 de D06 después de filtros.
6. **seleccion_de_modelo**: seleccionar un modelo admisible, no obligar a construirlo.
7. **instancia_y_persistencia**: obtener ID estable y persistir solo cuando CoreRPG implemente la instancia.

## Nueve modelos D06 y condiciones

| Modelo | Clases permitidas | Pruebas particulares |
|---|---|---|
| `agricola` | aldea, pueblo, villa | soil_and_cultivation_verified, land_use_rights_verified |
| `ganadera` | aldea, pueblo | grazing_suitable_verified, grazing_rights_verified |
| `pesquera` | aldea, pueblo, villa | coastal_or_fishery_water_verified, safe_landing_verified, fishing_rights_verified |
| `minera_auxiliar` | enclave, aldea | specific_mine_site_authorized, mineral_site_access_verified, site_ownership_verified |
| `metalurgica_auxiliar` | enclave, aldea, pueblo | legal_processing_function_verified, fuel_and_inputs_verified, site_access_for_supplies_verified |
| `forestal_sostenible` | enclave, aldea, pueblo | managed_forest_site_verified, forest_use_rights_verified, sustainable_harvest_verified |
| `servicio_camino` | enclave, aldea, pueblo | attested_road_at_site_verified, local_traffic_demand_verified |
| `insular_mixta` | aldea, pueblo | island_site_verified, local_land_use_verified, insular_food_base_verified |
| `enclave_especializado` | enclave | specific_authorized_function_verified, resident_community_justified_verified |

## Diez necesidades D08

- **food (alimentacion)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **water (agua)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **sanitation (higiene_y_residuos)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **care (cuidados)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **care (salud)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **apprenticeship (aprendizaje)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **housing (alojamiento)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **logistics (transporte)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **maintenance (mantenimiento)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.
- **trade (comercio_y_abastecimiento)**: proveedor y acceso reales; escasez y espera permitidas; nunca inventar capacidad.

## Red de transporte: el gran limitador

D05 solo acredita tres enlaces materiales concretos de carácter **distinto**: camino Veldora–Treihord; tramo Belara para barcazas de poco calado; y galería fortificada restringida Crisol–Bóveda. La última **no es una carretera pública**. Las otras relaciones de suministro D05 son relaciones económicas, no conexiones de transporte dibujadas.

Por tanto **no se autoriza** construir una red all-to-all entre ciudades/islas ni estimar tiempos en kilómetros. Una localidad sin proveedor accesible puede sufrir necesidad no cubierta y no recibe una posada, médico, mercado o barco automático.

## Derechos, población y canon

Los cuatro núcleos `treihord, veldora, taramin, syvaris` son ciudades manuales. Nunca entran en el generador de aldeas/pueblos/villas. Sus rangos demográficos D08 no permiten deducir números exactos de hogares o establecimientos. Las leyes del Reino sobre edad, propiedad, tutela, salud, fiscalidad y ejército se heredan desde Defaults; no se adaptan arbitrariamente a la Casa.

**Salida:** `../Datos operativos/darovan_dp15_settlement_service_network_v0.1.json`. No se acreditan NPC activos, inventarios, ofertas laborales ni WorldState.

## Adenda editorial — 11/11/2026

Los modelos, necesidades y filtros de esta especificación se desarrollan socialmente en [D.P15/03 — Economía vivida](03_economia_vivida_red_regional_y_necesidades.md), con ocho cadenas de trabajo, escasez, custodia, movilidad y decisiones del jugador. **D.P15 completa el diseño regional de relaciones y servicios**, pero no crea proveedores físicos, tiempos de ruta ni red ejecutable.

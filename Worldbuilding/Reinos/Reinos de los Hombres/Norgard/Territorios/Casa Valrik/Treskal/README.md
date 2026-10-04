# Treskal — ciudad

## Estado

**DISEÑO FUNCIONAL BASE CERRADO — DESARROLLO DETALLADO ACTIVO**

Treskal es una ciudad canónica única.

No utiliza el sistema procedural de Aldeas, Pueblos y Villas.

## Documentos

### 00_Canon

- `treskal_canon_consolidado.md` — reúne las reglas ya fijadas sobre la ciudad.

### 01_Estructura_urbana

- `estructura_funcional_treskal_v0.1.md` — áreas funcionales necesarias antes de diseñar el plano.
- `sectores_funcionales_treskal_v0.1.md` — IDs funcionales T01–T11 para organizar el plano sin fijar todavía nombres de barrios.

## Regla

No fijar nombres de barrios, calles o edificios singulares antes de resolver la topología general de la ciudad.

La geografía mundial confirma costa, río y relieve suave. La referencia visual aprobada añade muelles fluviales y pequeñas embarcaciones; sigue pendiente decidir el trazado exacto del río y su relación topológica con el puerto marítimo.

### 02_Topologia

- `opciones_topologia_costa_rio_puerto_v0.1.md` — historial de la decisión A/B/C; Opción A aprobada.
- `topologia_treskal_v0.1.md` — topología canónica de desembocadura integrada.
- `cruce_principal_rio_v0.1.md` — un puente principal aguas arriba de los muelles; cruces secundarios aún no fijados.

## Decisión topológica vigente

**Opción A — Desembocadura integrada.** El río interior alcanza el mar junto a Treskal; los muelles fluviales conectan con la zona de intercambio y el puerto civil, mientras los Astilleros Reales ocupan un sector litoral próximo pero separado.

### 03_Distribucion_urbana

- `esquema_espacial_relativo_v0.1.md` — relaciones de proximidad/separación entre sectores T01–T11.
- `red_viaria_y_flujos_v0.1.md` — jerarquía de calles y corredores de madera, alimentos, puerto e instituciones.
- `sistema_mercados_v0.1.md` — mercado principal, pescado, ganado, madera y comercio portuario.

### Datos operativos

- `treskal_city_structure_v0.1.json` — estructura urbana funcional legible por herramientas y futuro RPG Core.
- `treskal_city_design_invariants_v0.1.json` — restricciones que el plano detallado no puede violar.
- `treskal_npc_population_and_commerce_contract_v0.1.json` — contrato de población NPC, conocimiento, rutinas e inventarios.
- `treskal_urban_navigation_and_identity_v0.1.json` — subzonas, landmarks, navegación e identidad sensorial.
- `treskal_urban_graph_v0.1.json` — grafo abstracto de sectores y conexiones.
- `treskal_dynamic_city_states_v0.1.json` — estados dinámicos y consecuencias urbanas persistentes.
- `treskal_street_interior_activity_contract_v0.1.json` — corredores urbanos, interiores persistentes y activity anchors.
- `treskal_access_and_world_state_contract_v0.1.json` — acceso, autoridad y persistencia mutable.
- `treskal_city_manifest_v0.1.json` — manifest maestro de contratos operativos de Treskal.
- `treskal_population_and_security_matrix_v0.1.json` — matriz de residencia, actividad, tránsito y seguridad por subzona.
- `treskal_information_and_reputation_contract_v0.1.json` — conocimiento K0–K5, rumores y reputaciones por red.
- `treskal_urban_gameplay_discovery_contract_v0.1.json` — descubrimiento, investigación y encargos emergentes.
- `treskal_labor_household_visitor_contract_v0.1.json` — demanda laboral, hogares y visitantes.
- `treskal_civil_port_and_storage_contract_v0.1.json` — operación portuaria civil y almacenamiento.
- `treskal_housing_social_geography_contract_v0.1.json` — vivienda, presión residencial y geografía social.
- `treskal_ai_context_and_output_contract_v0.1.json` — percepción, diálogo IA, validación y disciplina de secretos.
- `treskal_ai_comparative_test_pack_v0.1.json` — 16 fixtures no canónicos para pruebas comparativas de modelos.
- `treskal_materialization_streaming_persistence_contract_v0.1.json` — materialización determinista, LOD lógico y migraciones.
- `treskal_event_causality_contract_v0.1.json` — ciclo de vida EVT, causalidad y propagación de efectos.
- `treskal_arrival_departure_travel_contract_v0.1.json` — aproximaciones APP, viaje territorial y transición de LOD.

## Estado del diseño

La arquitectura funcional base de Treskal está cerrada. Permanecen abiertos los detalles finos: trazado métrico del río y calles, geometría exacta del puente, cruces menores, nombres urbanos, planos arquitectónicos concretos de algunos complejos, rangos de guardia y calendario fino de mercados especializados.

### 04_Infraestructura_urbana

- `agua_residuos_incendios_v0.1.md` — agua, drenaje, residuos, prevención y respuesta ante incendios e iluminación nocturna.
- `guardia_y_justicia_v0.1.md` — funciones de guardia urbana, justicia territorial y límites respecto a Astilleros Reales.

### 05_Tejido_urbano

- `densidades_y_tipologias_edificatorias_v0.1.md` — alturas, densidades y tipologías U01–U14.
- `servicios_cotidianos_y_capacidades_v0.1.md` — redes de servicios y regla capacidad → establecimientos.

### 06_Edificios_singulares

- `catalogo_funcional_edificios_singulares_v0.1.md` — catálogo mínimo S01–S10 sin nombres propios.
- `S01_S02_casa_valrik_y_administracion_v0.1.md` — sede señorial y administración territorial.
- `S03_S05_justicia_custodia_guardia_v0.1.md` — complejo judicial, custodia y guardia urbana.
- `S06_S10_mercados_y_logistica_v0.1.md` — mercados, pescado, madera y ganado.
- `S08_astilleros_reales_v0.1.md` — programa funcional del recinto naval de la Corona.

### 07_Vida_urbana

- `poblacion_presente_y_ritmos_v0.1.md` — residentes, población flotante y ritmo diario/estacional.
- `familia_aprendizaje_y_reputacion_v0.1.md` — familia, oficio, aprendizaje, honor y vida social.
- `practica_funeraria_urbana_v0.1.md` — piras periféricas, retorno de cenizas y variante marítima local.

### 08_Cartografia

- `orientacion_espacial_cardinal_v0.1.md` — orientación relativa de sectores respecto a río, costa, bosque y rutas interiores.

### 09_Economia

- `cadenas_abastecimiento_economia_urbana_v0.1.md` — origen, entrada, transformación y destino de las mercancías principales.

### 10_Poblacion_NPC

- `modelo_poblacion_npc_v0.1.md` — NPC autorales, residentes persistentes y población latente.
- `conocimiento_rutinas_memoria_npc_v0.1.md` — conocimiento limitado, rumores, rutinas y memoria social.
- `comercio_proveedores_inventarios_v0.1.md` — proveedores reales, stock persistente y encargos.

### 11_Identidad_urbana

- `subzonas_urbanas_v0.1.md` — subzonas técnicas Z01–Z14 para convertir sectores en lugares reconocibles.
- `puntos_referencia_y_navegacion_v0.1.md` — landmarks L01–L12 y navegación mediante referencias físicas.
- `lectura_sensorial_y_actividad_v0.1.md` — señales visuales, sonoras y ambientales derivadas de actividad real.

### 12_Historia_urbana

- `capas_crecimiento_relativo_v0.1.md` — siete capas G1–G7 que explican el crecimiento orgánico sin inventar fechas.

### 13_Toponimia

- `marco_toponimia_urbana_v0.1.md` — marco técnico de IDs y nombres visibles.
- `toponimia_treskal_v0.1.md` — primera capa canónica de nombres urbanos de Treskal.

## Dirección visual

El perfil visual vigente de la ciudad es `TRESKAL_CITY_VISUAL_PROFILE_v0.1.md`. Las referencias visuales antiguas quedan subordinadas a ese perfil; las montañas dramáticas inmediatas no son canon.

### 14_Simulacion_urbana

- `grafo_navegacion_v0.1.md` — conectividad T01–T11, puente, restricciones por actor y costes de ruta.
- `estados_dinamicos_urbanos_v0.1.md` — temporales, crecidas, incendios, convoyes, llegadas de barcos y otros estados de World State.

## Convención toponímica vigente

Treskal usa el modelo mixto de Norgard: nombres propios heredados cuando existe historia real y, para la vida urbana cotidiana, nombres descriptivos y populares. Quedan fijados, entre otros, **Puente de los Gemelos**, **Plaza del Abasto**, **Lonja del Pescado**, **Los Talleres**, **Los Patios**, **La Casa**, **Casa de Justicia de Treskal**, **Los Muelles** y **Los Corrales**.

### 15_Vias_y_espacios

- `corredores_urbanos_principales_v0.1.md` — corredores C01–C08 antes del plano métrico y de los nombres de calle.
- `espacios_publicos_menores_v0.1.md` — patios, ensanchamientos, agua, carga y espacios cotidianos.

### 16_Interiores_y_actividad

- `interiores_funcionales_v0.1.md` — reglas de acceso, persistencia y materialización de interiores U01–U14.
- `puntos_actividad_npc_v0.1.md` — anclas A01–A12 para rutinas contextuales de NPC.

### 17_Integracion_juego

- `acceso_autoridad_y_reaccion_social_v0.1.md` — clases P0–P5, permisos y escalada de reacción.
- `contrato_world_state_treskal_v0.1.md` — separación entre canon estático, estado persistente y estado derivado.

### 18_Demografia_espacial

- `distribucion_relativa_poblacion_v0.1.md` — pesos R/D/W/T/N por subzona para densidad, LOD y población visible.
- `seguridad_urbana_por_subzona_v0.1.md` — prioridades de vigilancia sin fijar rangos ni cifras militares.

### 19_Informacion_y_reputacion

- `propagacion_informacion_y_rumores_v0.1.md` — estados K0–K5, canales sociales y distorsión de rumores.
- `reputacion_local_y_profesional_v0.1.md` — reputación personal, familiar, profesional, vecinal, institucional y comercial sin karma global.

### 20_Gameplay_urbano

- `descubrimiento_servicios_y_encargos_v0.1.md` — descubrimiento orgánico de lugares, servicios y encargos.
- `investigacion_urbana_testigos_evidencia_v0.1.md` — testigos, evidencia, contradicciones y conocimiento parcial.
- `oportunidades_encargos_emergentes_v0.1.md` — oportunidades generadas por necesidades reales del World State.

### 21_Demografia_laboral

- `demanda_laboral_oficios_y_hogares_v0.1.md` — familias O01–O14, capacidad laboral y hogares H01–H09.
- `visitantes_alojamiento_estancia_v0.1.md` — visitantes V01–V09, alojamiento y transición a residencia.
- `ciclos_laborales_ausencias_continuidad_v0.1.md` — relevo, ausencias, enfermedad, aprendices y continuidad de negocios.

### 22_Puerto_y_almacenamiento

- `operacion_puerto_civil_y_muelles_fluviales_v0.1.md` — ciclo de embarcación, atraque, carga/descarga y relación río-mar.
- `almacenamiento_perecibilidad_reservas_v0.1.md` — clases ST1–ST6, stock urbano y resiliencia ante cortes.

### 23_Vivienda_y_geografia_social

- `asignacion_vivienda_geografia_social_v0.1.md` — asignación de hogares por espacio, oficio, recursos y proximidad sin segregación rígida.
- `presion_residencial_mudanzas_v0.1.md` — viviendas libres, saturación, desplazamiento y mudanzas persistentes.

### 24_Contexto_IA

- `contrato_narrador_percepcion_v0.1.md` — Modo Máster/Off Story: verdad → filtro perceptivo → contexto autorizado → narración.
- `contrato_dialogo_npc_v0.1.md` — contexto limitado del NPC, memoria, secretos y actividad actual.
- `validacion_salida_ia_v0.1.md` — validación de texto, intenciones y propuestas antes de mutar World State.

### 25_Pruebas_IA

- `metodologia_bateria_comparativa_v0.1.md` — metodología común para comparar OpenAI, Gemini y Mistral sin alterar el contexto semántico.

### 26_Materializacion_y_runtime

- `materializacion_determinista_seeds_v0.1.md` — ciudad autoral con microdetalle determinista y jerarquía de seeds.
- `streaming_lod_persistencia_v0.1.md` — LOD lógico, simulación fuera de escena y continuidad.
- `versionado_migraciones_partidas_v0.1.md` — IDs estables, migraciones y compatibilidad de partidas.

### 27_Eventos_y_causalidad

- `ciclo_vida_eventos_v0.1.md` — instancias EVT, estados de vida y fuentes causales.
- `propagacion_consecuencias_v0.1.md` — efectos compartidos entre rutas, stock, actividad, conocimiento y NPC.

### 28_Entradas_y_viaje

- `entradas_salidas_transicion_territorio_ciudad_v0.1.md` — aproximaciones APP01–APP06 y transición gradual sin muralla.
- `continuidad_viaje_aprendizaje_rutas_v0.1.md` — conocimiento de rutas, viajes NPC y mercancía en tránsito.

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

La topología general ya está resuelta mediante la **Opción A — Desembocadura integrada**. La toponimia urbana se desarrolla con la convención mixta de Norgard y mantiene IDs técnicos estables.

La geografía mundial confirma costa, río y relieve suave. Permanecen pendientes únicamente el **trazado métrico exacto** del río, la geometría detallada del puente y el plano callejero.

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
- `treskal_urban_integration_test_pack_v0.1.json` — 12 escenarios no canónicos de regresión urbana integrada.
- `treskal_materialization_streaming_persistence_contract_v0.1.json` — materialización determinista, LOD lógico y migraciones.
- `treskal_event_causality_contract_v0.1.json` — ciclo de vida EVT, causalidad y propagación de efectos.
- `treskal_arrival_departure_travel_contract_v0.1.json` — aproximaciones APP, viaje territorial y transición de LOD.
- `treskal_consumption_restock_price_pressure_contract_v0.1.json` — consumo agregado, reposición y presión de mercado.
- `treskal_woodcraft_culture_contract_v0.1.json` — cadena artesanal de madera y estados W01–W08.
- `treskal_light_visibility_sound_contract_v0.1.json` — luz, visibilidad, sonido y audición diegética.
- `treskal_maritime_culture_contract_v0.1.json` — cultura marítima, saber del mar y redes sociales portuarias.
- `treskal_health_care_network_contract_v0.1.json` — red de curanderas, cuidados y disponibilidad.
- `treskal_learning_knowledge_transmission_contract_v0.1.json` — aprendizaje, procedencia del conocimiento y continuidad profesional.
- `treskal_hospitality_inn_network_contract_v0.1.json` — hospitalidad, red de posadas y estancias persistentes.
- `treskal_daily_life_family_food_contract_v0.1.json` — ritmos cotidianos, alimentación y redes familiares/vecinales.
- `treskal_word_of_honor_pledge_contract_v0.1.json` — palabra dada, compromisos y reparación social.
- `treskal_wayfinding_signage_addressing_contract_v0.1.json` — orientación humana, rótulos y localización no moderna.
- `treskal_animals_carts_traffic_contract_v0.1.json` — animales, carros, congestión y servicios de transporte.
- `treskal_messaging_letters_delivery_contract_v0.1.json` — mensajería, cartas y entrega física de información.
- `treskal_property_possession_object_contract_v0.1.json` — propiedad, posesión, custodia y objetos persistentes.
- `treskal_wear_maintenance_repair_contract_v0.1.json` — desgaste, obras y reparación persistente.
- `treskal_daily_market_stall_contract_v0.1.json` — mercados diarios, puestos y vendedores MK01–MK05.
- `treskal_business_lifecycle_contract_v0.1.json` — ciclo de vida BIZ01–BIZ08 y continuidad empresarial.
- `treskal_hygiene_laundry_domestic_water_contract_v0.1.json` — aseo, colada, agua doméstica y estado visual.
- `treskal_fuel_cooking_heat_contract_v0.1.json` — combustible, cocina, calor doméstico y stock térmico.
- `treskal_doors_locks_keys_access_contract_v0.1.json` — puertas, llaves, cerraduras y acceso físico.
- `treskal_employment_jobs_vacancies_contract_v0.1.json` — empleo, vacantes, ausencia y cobertura de puestos.
- `treskal_residency_household_mobility_contract_v0.1.json` — residencia, hogares, mudanzas y continuidad de identidad.
- `treskal_construction_building_change_contract_v0.1.json` — construcción, ampliación y evolución persistente del tejido.
- `treskal_clothing_footwear_lifecycle_contract_v0.1.json` — indumentaria, calzado, reparación y uso persistente.
- `treskal_seasonality_accumulated_weather_contract_v0.1.json` — estacionalidad, humedad, barro y secado persistente.
- `treskal_furniture_material_life_contract_v0.1.json` — mobiliario, vida material y persistencia interior.
- `treskal_cross_system_causality_contract_v0.1.json` — integración causal y autoridad de escritura entre sistemas.
- `treskal_tools_workstations_equipment_contract_v0.1.json` — herramientas, estaciones y capacidad productiva.
- `treskal_work_hazards_accidents_contract_v0.1.json` — riesgos laborales, accidentes y continuidad operativa.
- `treskal_rest_sleep_availability_contract_v0.1.json` — sueño, descanso y disponibilidad de NPC.
- `treskal_fire_response_propagation_contract_v0.1.json` — incendios, propagación, evacuación y secuelas.
- `treskal_sanitation_waste_cycle_contract_v0.1.json` — saneamiento, letrinas, residuos y retirada urbana.
- `treskal_death_mourning_funeral_contract_v0.1.json` — muerte, cremación, cenizas y continuidad social.
- `treskal_conversation_privacy_eavesdropping_contract_v0.1.json` — privacidad, audición parcial y conversaciones.
- `treskal_waiting_service_capacity_contract_v0.1.json` — espera, colas y capacidad efectiva de atención.
- `treskal_dependents_care_network_contract_v0.1.json` — cuidados, dependientes y red doméstica de apoyo.
- `treskal_household_hospitality_guest_contract_v0.1.json` — hospitalidad, visitas y permisos temporales de huésped.
- `treskal_household_chores_domestic_load_contract_v0.1.json` — tareas domésticas, carga del hogar y backlog.
- `treskal_apprenticeship_skill_transmission_contract_v0.1.json` — aprendizaje de oficio, mentoría y competencia progresiva.
- `treskal_leisure_social_gathering_contract_v0.1.json` — ocio, sociabilidad, encuentros y familiaridad.
- `treskal_artisan_commission_contract_v0.1.json` — encargos COM01–COM12, calidad y procedencia artesanal.

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

### 29_Economia_simulada

- `consumo_reposicion_circulacion_v0.1.md` — ciclo entrada/producción → stock → uso/venta → consumo/pérdida → reposición.
- `formacion_precios_presion_mercado_v0.1.md` — presión cualitativa de mercado sin fijar moneda ni cifras.

### 30_Cultura_de_la_madera

- `cultura_madera_cadena_artesanal_v0.1.md` — aserrado manual, secado, especialidades y prestigio maderero.
- `estados_madera_gameplay_artesanal_v0.1.md` — estados W01–W08 para lotes y producción.

### 31_Percepcion_urbana

- `luz_oscuridad_visibilidad_v0.1.md` — noche por islas de luz funcional, reconocimiento progresivo y clima.
- `paisaje_sonoro_audicion_v0.1.md` — sonido diegético por actividad, audición y conocimiento derivado.

### 32_Validacion_integrada

- `metodologia_vertical_slice_urbana_v0.1.md` — pruebas de integración entre viaje, economía, NPC, LOD, eventos, acceso y percepción.

### 33_Cultura_maritima

- `cultura_maritima_saber_del_mar_v0.1.md` — experiencia marítima, familias, oficios y relación civil/naval.
- `vida_social_puerto_informacion_v0.1.md` — redes del puerto, visitantes, rumores y circulación de información.

### 34_Salud_y_cuidados

- `red_urbana_curacion_cuidados_v0.1.md` — red distribuida de curanderas, remedios domésticos y atención a domicilio.
- `disponibilidad_curanderas_gameplay_v0.1.md` — capacidad, desplazamiento, materiales y resolución de cuidados.

### 35_Aprendizaje_y_saber

- `aprendizaje_transmision_saber_v0.1.md` — modos ED01–ED07, maestros, escritura, comercio, mar y curandería.
- `estados_aprendizaje_continuidad_profesional_v0.1.md` — aprendiz, trabajador competente, experiencia y maestría sin títulos universales.

### 36_Hospitalidad

- `hospitalidad_urbana_red_posadas_v0.1.md` — red plural de posadas y hospitalidad Valrik a escala urbana.
- `alojamiento_estancia_memoria_posada_v0.1.md` — estancias persistentes, acceso temporal y memoria del alojamiento.

### 37_Vida_cotidiana

- `vida_cotidiana_familia_ritmos_v0.1.md` — franjas del día, hogar, niños, ocio y descanso.
- `alimentacion_abastecimiento_domestico_v0.1.md` — grupos F01–F08 y conexión entre mesa y abastecimiento.
- `redes_familiares_vecinales_cuidado_v0.1.md` — familia, vecinos, ayuda y relaciones persistentes.

### 38_Honor_y_palabra

- `palabra_dada_compromisos_honor_v0.1.md` — compromisos persistentes, estados y causas de cumplimiento/incumplimiento.
- `disputas_honor_reparacion_social_v0.1.md` — reparación informal, mediación y convivencia con la Ley del Rey.

### 39_Orientacion_y_senalizacion

- `orientacion_direcciones_no_modernas_v0.1.md` — landmarks, áreas populares, instrucciones verbales y conocimiento de rutas.
- `rotulos_senales_negocios_v0.1.md` — tipos SG01–SG05 y señalización funcional no moderna.

### 40_Transporte_y_animales

- `animales_tiro_carros_trafico_v0.1.md` — clases TR01–TR06, tráfico, congestión y animales de trabajo.
- `establos_corrales_servicios_transporte_v0.1.md` — estabulación, carreteros, reparación y capacidad finita.

### 41_Mensajeria_y_comunicacion

- `mensajeria_cartas_comunicacion_urbana_v0.1.md` — recados MSG01–MSG05, cartas, documentos y avisos.
- `entrega_conocimiento_fiabilidad_v0.1.md` — entrega, lectura, cadena de custodia y conocimiento.

### 42_Propiedad_y_objetos

- `propiedad_posesion_objetos_persistentes_v0.1.md` — owner/possessor/location/custody y estados OWN01–OWN07.
- `inventarios_contenedores_abstraccion_v0.1.md` — objetos persistentes, lotes y utilería contextual.

### 43_Mantenimiento_y_reparacion

- `desgaste_mantenimiento_reparacion_v0.1.md` — estados COND01–COND07, daños y repair jobs persistentes.
- `obras_espacio_publico_v0.1.md` — calles, drenajes, puntos de agua, desvíos y cuadrillas.

### 44_Mercados_y_puestos

- `funcionamiento_mercados_puestos_v0.1.md` — vendedores MK01–MK05, ciclo diario y stock físico.
- `densidad_puesto_comercio_gameplay_v0.1.md` — LOD de mercado, compras y reposición real.

### 45_Ciclo_de_negocios

- `ciclo_vida_negocios_talleres_v0.1.md` — estados BIZ01–BIZ08, cierres, mudanzas y continuidad.
- `capacidad_competencia_especializacion_v0.1.md` — capacidad urbana, competencia y especialización real.

### 46_Encargos_artesanales

- `encargos_produccion_por_encargo_v0.1.md` — estados COM01–COM12, materiales, plazos y entrega.
- `calidad_errores_procedencia_piezas_v0.1.md` — calidad por proceso, errores causales y procedencia persistente.

### 47_Aseo_y_lavado

- `aseo_lavado_uso_domestico_agua_v0.1.md` — higiene preindustrial, transporte de agua, lavado y secado.
- `limpieza_colada_estado_visual_v0.1.md` — pátina, suciedad contextual, humedad y persistencia visual.

### 48_Combustible_y_calor

- `combustible_cocina_calor_domestico_v0.1.md` — leña, cocina, hornos, almacenamiento y riesgo de incendio.
- `stock_combustible_consumo_termico_v0.1.md` — stock térmico, consumo agregado y reposición real.

### 49_Accesos_fisicos

- `puertas_llaves_cerraduras_acceso_v0.1.md` — estados DOOR01–DOOR07 y separación entre acceso físico y permiso.
- `llaves_permisos_cambios_acceso_v0.1.md` — llaves persistentes, préstamo, revocación y roles.

### 50_Empleo_y_vacantes

- `relaciones_laborales_vacantes_continuidad_v0.1.md` — estados EMP01–EMP08, profesión ≠ puesto y continuidad laboral.
- `cobertura_puestos_disponibilidad_v0.1.md` — vacantes, candidatos, sustitución e incorporación.

### 51_Residencia_y_mudanzas

- `formacion_hogares_mudanzas_residencia_v0.1.md` — hogares, desplazamientos y estados RES01–RES05 / MOVE01–MOVE06.
- `visitante_residente_continuidad_identidad_v0.1.md` — transición visitante→residente sin pérdida de identidad.

### 52_Construccion_y_cambio_edificado

- `construccion_ampliacion_cambio_uso_v0.1.md` — estados BUILD01–BUILD10, obra física, ampliación, cambio de uso y demolición.
- `evolucion_tejido_reutilizacion_v0.1.md` — transformación de edificios sin alterar el macrocanon T/Z/L/S/C.

### 53_Indumentaria_y_calzado

- `indumentaria_calzado_ciclo_uso_v0.1.md` — categorías CL01–CL04 y estados GAR01–GAR06.
- `sastres_zapateros_mantenimiento_v0.1.md` — confección, ajuste, reparación y encargos O10.

### 54_Estacionalidad_y_clima

- `estacionalidad_clima_actividad_v0.1.md` — efectos estacionales sin fijar calendario y memoria ambiental.
- `persistencia_ambiental_secado_v0.1.md` — estados ENV01–ENV06, secado y recuperación material.

### 55_Mobiliario_y_vida_material

- `mobiliario_domestico_vida_material_v0.1.md` — funciones FURN01–FURN07 y vida material doméstica.
- `generacion_persistencia_mobiliario_v0.1.md` — materialización funcional, promoción a persistente y cambio de ocupante.

### 56_Integracion_de_sistemas

- `integracion_causal_sistemas_urbanos_v0.1.md` — autoridad por dominio, orden causal y separación hecho/presentación.
- `cadenas_causales_referencia_v0.1.md` — ocho cadenas de regresión entre clima, economía, objetos, NPC e información.

### 57_Herramientas_y_equipamiento

- `herramientas_equipo_estaciones_trabajo_v0.1.md` — estados TOOL01–TOOL07 y WS01–WS05.
- `mantenimiento_capacidad_productiva_v0.1.md` — cuellos de botella, mantenimiento y efecto sobre producción.

### 58_Seguridad_laboral_y_accidentes

- `riesgos_precauciones_accidentes_v0.1.md` — riesgos HAZ01–HAZ07 y precauciones prácticas preindustriales.
- `respuesta_continuidad_operativa_v0.1.md` — estados ACC01–ACC08 y recuperación tras incidente.

### 59_Sueno_y_descanso

- `sueno_descanso_disponibilidad_v0.1.md` — estados REST01–REST07 y disponibilidad cotidiana.
- `interrupciones_continuidad_rutina_v0.1.md` — interrupciones, retorno a rutina y emergencias nocturnas.

### 60_Incendios_y_respuesta

- `deteccion_respuesta_propagacion_v0.1.md` — estados FIRE01–FIRE08, detección, propagación y respuesta preindustrial.
- `secuelas_evacuacion_recuperacion_v0.1.md` — evacuación, reentrada, desplazamiento y recuperación posterior.

### 61_Saneamiento_y_residuos

- `residuos_letrinas_limpieza_urbana_v0.1.md` — tipos WASTE01–WASTE08, letrinas, pozos negros y limpieza.
- `ciclo_residuos_recogida_destino_v0.1.md` — estados WST01–WST07, recogida, transporte y reutilización.

### 62_Muerte_duelo_y_funeral

- `muerte_duelo_continuidad_social_v0.1.md` — estados MORT01–MORT08 y consecuencias sociales de una muerte.
- `cremacion_cenizas_memoria_urbana_v0.1.md` — destinos ASH01–ASH05 y aplicación urbana del canon funerario norgardiano.

### 63_Privacidad_y_conversacion

- `privacidad_conversaciones_escucha_v0.1.md` — contextos CONV, modos VOICE y privacidad basada en espacio/acústica.
- `audicion_parcial_testigos_filtracion_v0.1.md` — resultados HEAR00–HEAR05, testigos y filtración de información.

### 64_Esperas_y_capacidad

- `espera_colas_capacidad_atencion_v0.1.md` — estados WAIT01–WAIT08 y prioridades no universales.
- `solicitudes_capacidad_efectiva_v0.1.md` — solicitudes persistentes y capacidad derivada de personas/recursos.

### 65_Cuidados_y_dependientes

- `cuidado_ninos_ancianos_dependientes_v0.1.md` — tipos DEP01–DEP05 y estados CARE01–CARE07.
- `red_cuidados_disponibilidad_domestica_v0.1.md` — red de cuidadores, relevos y efecto sobre rutina/empleo.

### 66_Hospitalidad_y_visitas

- `hospitalidad_domestica_visitas_invitados_v0.1.md` — estados HOSP01–HOSP07 y hospitalidad temporal.
- `permisos_temporales_huesped_v0.1.md` — alcance, caducidad, consumo y relación con residencia/acceso.

### 67_Tareas_domesticas

- `tareas_domesticas_carga_hogar_v0.1.md` — tipos CHORE01–CHORE09 y estados DOM01–DOM07.
- `asignacion_tareas_presion_domestica_v0.1.md` — capacidad, backlog y resolución agregada del trabajo doméstico.

### 68_Aprendizaje_de_oficio

- `aprendizaje_relacion_maestro_aprendiz_v0.1.md` — estados APR01–APR06 y relación formativa.
- `practica_competencia_especialidad_v0.1.md` — progreso por evidencia, especialización y coste de supervisión.

### 69_Ocio_y_sociabilidad

- `ocio_sociabilidad_tiempo_no_laboral_v0.1.md` — contextos LEIS01–LEIS07 y tiempo social/no laboral.
- `encuentros_sociales_familiaridad_v0.1.md` — encuentros, familiaridad, relaciones y resolución offscreen.

### 70_Relaciones_afectivas_y_pareja

- `vinculos_afectivos_cortejo_pareja_v0.1.md` — estados AFF01–AFF07, reciprocidad, privacidad y relación con la sociabilidad.
- `pareja_hogar_separacion_continuidad_v0.1.md` — convivencia, hogar, tareas, acceso, separación y memoria persistente.

### 71_Embarazo_nacimiento_y_primera_infancia

- `embarazo_parto_recuperacion_domestica_v0.1.md` — estados PREG01–PREG06, privacidad, trabajo, asistencia y resolución del parto.
- `nacimiento_recien_nacido_primera_infancia_v0.1.md` — creación de NPC persistente, hogar, DEP01/CARE y efectos sobre la vida cotidiana.

### 72_Desarrollo_infantil_y_transicion_juvenil

- `desarrollo_infantil_autonomia_supervision_v0.1.md` — estados CHD01–CHD06, movilidad, cuidado, pares y crecimiento persistente.
- `juego_tareas_aprendizaje_transicion_v0.1.md` — ED/CHORE/LEIS, exposición a oficios y entrada gradual en APR.

### 73_Envejecimiento_y_vejez_activa

- `envejecimiento_autonomia_vejez_activa_v0.1.md` — estados AGE01–AGE06, capacidad, cuidado, sociabilidad y continuidad personal.
- `experiencia_mentoria_reduccion_actividad_v0.1.md` — trabajo adaptado, mentoría, continuidad de negocios y transmisión de saber.

### 74_Amistad_y_circulos_sociales

- `amistad_confianza_continuidad_personal_v0.1.md` — estados FRI01–FRI07, confianza, confidencia, ayuda y amistades a distancia.
- `circulos_sociales_grupos_habituales_v0.1.md` — grupos persistentes, relaciones internas desiguales, rutinas y circulación de información.

### 75_Conflicto_interpersonal_y_reconciliacion

- `conflicto_tension_distanciamiento_v0.1.md` — estados RIFT01–RIFT07, interpretación, evitación, círculos y escalada hacia honor/ley.
- `disculpa_reparacion_reconciliacion_v0.1.md` — disculpa, aceptación, mediación, reparación parcial y reconciliación con memoria.

### 76_Preferencias_y_habitos_personales

- `preferencias_gustos_aversiones_personales_v0.1.md` — PREF01–PREF08, gustos, aversiones, cambios y límites de canon.
- `habitos_costumbres_rutina_flexible_v0.1.md` — HAB01–HAB08, regularidades personales, interrupciones y conocimiento de rutinas.

### 77_Favores_y_reciprocidad

- `favores_ayuda_voluntaria_memoria_v0.1.md` — estados FAV01–FAV07, ayuda real, gratitud y memoria social.
- `reciprocidad_limites_deuda_social_v0.1.md` — reciprocidad no cuantificada, límites, abuso, pledge y continuidad.

### 78_Regalos_y_significado_social

- `regalos_obsequios_transferencia_social_v0.1.md` — estados GIFT01–GIFT07, OWN, aceptación, preferencias y límites relacionales.
- `significado_aceptacion_memoria_regalos_v0.1.md` — intención, interpretación, objetos sentimentales, devolución y memoria.

### 79_Peticiones_y_limites_personales

- `peticiones_aceptacion_rechazo_personal_v0.1.md` — estados REQ01–REQ08, voluntad, aclaración, rechazo y ejecución validada.
- `limites_presion_alcance_permiso_v0.1.md` — permisos acotados, condiciones, revocación, presión social y límites persistentes.

### 80_Secretos_y_confidencias

- `secretos_confidencias_divulgacion_voluntaria_v0.1.md` — estados CONF01–CONF07, saber frente a contar, confidencia y alcance.
- `conservacion_filtracion_ruptura_confidencias_v0.1.md` — filtraciones, escucha, promesas, rumor y consecuencias relacionales.

### 81_Verdad_error_y_versiones_falsas

- `verdad_error_omision_declaracion_v0.1.md` — estados STAT01–STAT08 y separación entre verdad, creencia y declaración.
- `versiones_falsas_contradiccion_descubrimiento_v0.1.md` — continuidad, evidencia, exposición y consecuencias.

### 82_Credibilidad_sospecha_y_verificacion

- `credibilidad_fuentes_sospecha_v0.1.md` — estados CRED01–CRED08, confianza contextual y ausencia de detección sobrenatural.
- `verificacion_evidencia_corroboracion_v0.1.md` — evidencia, testigos, documentos, expertos y actualización de creencias.

### 83_Emociones_y_estado_de_animo

- `emociones_transitorias_causa_expresion_v0.1.md` — EMO01–EMO10, causa subjetiva, expresión y límites perceptivos.
- `estado_animo_persistencia_recuperacion_v0.1.md` — MOOD01–MOOD07, persistencia, recuperación y separación respecto a personalidad.

### 84_Motivaciones_objetivos_e_intenciones

- `objetivos_intenciones_prioridades_v0.1.md` — GOAL01–GOAL08, deseos futuros, prioridades y autonomía del NPC.
- `planes_progreso_bloqueos_abandono_v0.1.md` — planificación limitada por conocimiento, progreso causal, bloqueo y abandono.

### 85_Toma_de_decisiones_y_riesgo

- `decisiones_deliberacion_conflictos_prioridad_v0.1.md` — DEC01–DEC08, alternativas conocidas, prioridades, obligaciones e indecisión.
- `riesgo_incertidumbre_reconsideracion_v0.1.md` — riesgo percibido frente a riesgo real, cambio de decisión y resultados inciertos.

### 86_Estres_presion_y_recuperacion

- `presion_acumulada_carga_cotidiana_v0.1.md` — STRS01–STRS07, acumulación de demandas y efectos contextuales.
- `recuperacion_apoyo_ajuste_rutina_v0.1.md` — apoyo, redistribución, descanso y recuperación sin barra universal.

### 87_Personalidad_y_rasgos_estables

- `personalidad_temperamento_rasgos_v0.1.md` — PERS01–PERS10, tendencias estables sin clases rígidas.
- `expresion_contextual_evolucion_personalidad_v0.1.md` — expresión según contexto, continuidad e identidad a largo plazo.

### 88_Memoria_relevancia_y_olvido

- `memoria_episodica_relevancia_continuidad_v0.1.md` — MEM01–MEM08, recuerdos significativos, detalle y continuidad personal.
- `recuerdo_olvido_revision_experiencias_v0.1.md` — olvido, revisión, recuerdos contradictorios y optimización sin borrar consecuencias.

### 89_Valores_principios_y_conflictos_internos

- `valores_personales_principios_compromiso_v0.1.md` — VAL01–VAL08, importancia personal de principios sin alineamiento moral universal.
- `conflicto_valores_compromiso_revision_v0.1.md` — tensión entre valores, compromiso en acción, reafirmación y revisión sostenida.

### 90_Identidad_personal_y_roles_vitales

- `identidad_personal_roles_autoconcepto_v0.1.md` — SELF01–SELF08, roles reconocidos, identidad central y multiplicidad de roles.
- `transicion_rol_perdida_identidad_persistente_v0.1.md` — pérdida, adaptación, legado e identidad persistente tras cambios de vida.

### 91_Confianza_interpersonal_y_fiabilidad

- `confianza_dominios_historial_v0.1.md` — TRUST01–TRUST08, confianza por honestidad, fiabilidad, discreción, competencia y otros dominios.
- `ruptura_reparacion_limites_confianza_v0.1.md` — daño, reparación, perdón, recomendaciones y límites de la confianza.

### 92_Expectativas_anticipacion_y_sorpresa

- `expectativas_anticipacion_resultados_esperados_v0.1.md` — EXP01–EXP08, anticipación basada en conocimiento, hábitos, confianza y experiencia.
- `sorpresa_desviacion_revision_expectativas_v0.1.md` — resultados inesperados, revisión de expectativas y reacción sin conocimiento del futuro.

### 93_Atencion_foco_y_distraccion

- `atencion_foco_conciencia_situacional_v0.1.md` — ATTN01–ATTN08, foco, vigilancia, atención dividida y límites perceptivos.
- `distraccion_interrupcion_deteccion_periferica_v0.1.md` — señales periféricas, interrupciones, sobrecarga y testimonio condicionado por atención.

### 94_Necesidades_fisicas_cotidianas

- `necesidades_fisicas_autocuidado_v0.1.md` — NEED01–NEED05, comida, hidratación, confort térmico, eliminación y presión de descanso.
- `satisfaccion_interrupcion_consecuencias_v0.1.md` — resolución mediante recursos reales, abstracción cotidiana y detalle cuando la rutina falla.

### 95_Dinamica_de_conversacion

- `dinamica_conversacion_disponibilidad_continuidad_v0.1.md` — DIAL01–DIAL08, disponibilidad, atención, iniciativa NPC y continuidad.
- `temas_interrupcion_cierre_conversacion_v0.1.md` — temas persistentes, interrupción, reanudación y cierre autónomo de diálogo.

### 96_Actitudes_y_opiniones_personales

- `actitudes_opiniones_valoracion_personal_v0.1.md` — VIEW01–VIEW08, valoración subjetiva separada de preferencia, confianza, amistad y reputación.
- `formacion_revision_expresion_opiniones_v0.1.md` — formación, ambivalencia, revisión y expresión pública de opiniones.

### 97_Agenda_y_uso_del_tiempo

- `agenda_personal_compromisos_uso_tiempo_v0.1.md` — AGEN01–AGEN09, agenda cualitativa, tiempo finito y compatibilidad entre actividades.
- `conflictos_agenda_retrasos_reprogramacion_v0.1.md` — retrasos, reprogramación, cancelación, citas perdidas y consecuencias.

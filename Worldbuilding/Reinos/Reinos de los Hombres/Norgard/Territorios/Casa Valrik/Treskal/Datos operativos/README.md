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
- `treskal_ai_context_and_output_contract_v0.1.json` — contexto autorizado para narrador/NPC y validación de salida IA.
- `treskal_ai_comparative_test_pack_v0.1.json` — 16 casos comparativos no canónicos para evaluar modelos IA.
- `treskal_materialization_streaming_persistence_contract_v0.1.json` — seeds, materialización, streaming, LOD y persistencia.
- `treskal_event_causality_contract_v0.1.json` — instancias EVT, causalidad y propagación de consecuencias.
- `treskal_arrival_departure_travel_contract_v0.1.json` — entradas APP01–APP06, salidas y continuidad de viaje.
- `treskal_consumption_restock_price_pressure_contract_v0.1.json` — consumo, stock, reposición y presión cualitativa de precios.
- `treskal_woodcraft_culture_contract_v0.1.json` — cultura maderera, aserrado manual y estados W01–W08.
- `treskal_light_visibility_sound_contract_v0.1.json` — estados de luz, visibilidad, sonido y audición.
- `treskal_urban_integration_test_pack_v0.1.json` — 12 escenarios de integración/regresión de sistemas urbanos.
- `treskal_maritime_culture_contract_v0.1.json` — identidad marítima, saber práctico y redes portuarias.
- `treskal_health_care_network_contract_v0.1.json` — curandería urbana distribuida, materiales y atención.
- `treskal_learning_knowledge_transmission_contract_v0.1.json` — modos ED01–ED07 y progreso profesional conceptual.
- `treskal_hospitality_inn_network_contract_v0.1.json` — hospitalidad urbana, posadas y alojamientos persistentes.
- `treskal_daily_life_family_food_contract_v0.1.json` — vida cotidiana, alimentos F01–F08 y redes familiares.
- `treskal_word_of_honor_pledge_contract_v0.1.json` — pledges persistentes, honor Valrik y reparación social.
- `treskal_wayfinding_signage_addressing_contract_v0.1.json` — landmarks, indicaciones, rótulos SG01–SG05 y localización.
- `treskal_animals_carts_traffic_contract_v0.1.json` — transporte TR01–TR06, establos, carros y animales.
- `treskal_messaging_letters_delivery_contract_v0.1.json` — tipos MSG01–MSG05, estados de entrega y conocimiento.
- `treskal_property_possession_object_contract_v0.1.json` — propiedad OWN01–OWN07, custodia, contenedores y objetos persistentes.
- `treskal_wear_maintenance_repair_contract_v0.1.json` — estados COND01–COND07 y trabajos de reparación.
- `treskal_daily_market_stall_contract_v0.1.json` — ciclo de puestos, tipos MK01–MK05 y LOD de mercado.
- `treskal_business_lifecycle_contract_v0.1.json` — negocio ≠ edificio ≠ propietario y estados BIZ01–BIZ08.
- `treskal_artisan_commission_contract_v0.1.json` — encargos COM01–COM12, materiales reservados, calidad y procedencia.
- `treskal_hygiene_laundry_domestic_water_contract_v0.1.json` — aseo, lavado, agua doméstica y pátina/suciedad contextual.
- `treskal_fuel_cooking_heat_contract_v0.1.json` — leña, consumo térmico, hornos y riesgo de fuego.
- `treskal_doors_locks_keys_access_contract_v0.1.json` — estados DOOR01–DOOR07, llaves y permisos.
- `treskal_employment_jobs_vacancies_contract_v0.1.json` — estados EMP01–EMP08, puestos y vacantes.
- `treskal_residency_household_mobility_contract_v0.1.json` — estados RES/MOVE, hogares y mudanzas persistentes.
- `treskal_construction_building_change_contract_v0.1.json` — estados BUILD01–BUILD10, ampliaciones, cambio de uso y demolición.
- `treskal_clothing_footwear_lifecycle_contract_v0.1.json` — funciones CL01–CL04 y condición GAR01–GAR06.
- `treskal_seasonality_accumulated_weather_contract_v0.1.json` — estados ENV01–ENV06 y memoria ambiental.
- `treskal_furniture_material_life_contract_v0.1.json` — mobiliario FURN01–FURN07 y materialización interior.
- `treskal_cross_system_causality_contract_v0.1.json` — orden causal, dominios y cadenas de integración.
- `treskal_tools_workstations_equipment_contract_v0.1.json` — estados TOOL/WS, mantenimiento y cuellos de botella.
- `treskal_work_hazards_accidents_contract_v0.1.json` — HAZ01–HAZ07, ACC01–ACC08 y respuesta a accidentes.
- `treskal_rest_sleep_availability_contract_v0.1.json` — estados REST01–REST07 y disponibilidad derivada.
- `treskal_fire_response_propagation_contract_v0.1.json` — FIRE01–FIRE08, respuesta y recuperación tras incendio.
- `treskal_sanitation_waste_cycle_contract_v0.1.json` — WASTE01–WASTE08, WST01–WST07 y ciclo de retirada.
- `treskal_death_mourning_funeral_contract_v0.1.json` — estados MORT/ASH, cremación y retorno de cenizas.
- `treskal_conversation_privacy_eavesdropping_contract_v0.1.json` — CONV/VOICE/HEAR, privacidad y conocimiento por oyente.
- `treskal_waiting_service_capacity_contract_v0.1.json` — WAIT01–WAIT08, solicitudes y capacidad de servicio.
- `treskal_dependents_care_network_contract_v0.1.json` — tipos DEP, estados CARE y capacidad de cuidado.
- `treskal_household_hospitality_guest_contract_v0.1.json` — estados HOSP y permisos temporales de visita/estancia.
- `treskal_household_chores_domestic_load_contract_v0.1.json` — CHORE01–CHORE09, DOM01–DOM07 y presión doméstica.
- `treskal_apprenticeship_skill_transmission_contract_v0.1.json` — APR01–APR06, mentoría y transmisión de habilidades.
- `treskal_leisure_social_gathering_contract_v0.1.json` — LEIS01–LEIS07 y encuentros sociales persistentes.
- `treskal_affective_relationship_pairing_contract_v0.1.json` — AFF01–AFF07, cortejo, pareja y continuidad relacional.
- `treskal_pregnancy_birth_early_infancy_contract_v0.1.json` — PREG01–PREG06, parto, nacimiento persistente y primera infancia.
- `treskal_child_development_autonomy_learning_contract_v0.1.json` — CHD01–CHD06, autonomía, supervisión y transición hacia aprendizaje.
- `treskal_aging_late_life_activity_contract_v0.1.json` — AGE01–AGE06, vejez activa, carga adaptada, mentoría y dependencia real.
- `treskal_friendship_social_circles_contract_v0.1.json` — FRI01–FRI07, amistad profunda, confianza y círculos sociales persistentes.
- `treskal_interpersonal_conflict_repair_contract_v0.1.json` — RIFT01–RIFT07, conflicto interpersonal, reparación y reconciliación persistente.
- `treskal_personal_preferences_habits_contract_v0.1.json` — PREF01–PREF08 y HAB01–HAB08, gustos individuales y hábitos flexibles.
- `treskal_favors_reciprocity_informal_debt_contract_v0.1.json` — FAV01–FAV07, ayuda voluntaria, reciprocidad y deuda social informal.
- `treskal_gifts_social_meaning_contract_v0.1.json` — GIFT01–GIFT07, transferencia de regalos, aceptación y significado social.
- `treskal_requests_consent_boundaries_contract_v0.1.json` — REQ01–REQ08, peticiones, rechazo, condiciones y límites personales.
- `treskal_confidential_information_contract_v0.1.json` — CONF01–CONF07, confidencialidad, divulgación y filtraciones.
- `treskal_statement_integrity_contract_v0.1.json` — STAT01–STAT08, verdad, error, omisión y versiones falsas persistentes.
- `treskal_credibility_verification_contract_v0.1.json` — CRED01–CRED08, credibilidad, sospecha, corroboración y verificación.
- `treskal_emotion_mood_contract_v0.1.json` — EMO01–EMO10 y MOOD01–MOOD07, emociones transitorias y tono anímico persistente.
- `treskal_personal_goals_intentions_contract_v0.1.json` — GOAL01–GOAL08, objetivos personales, planificación, bloqueo y progreso causal.
- `treskal_decision_deliberation_contract_v0.1.json` — DEC01–DEC08, deliberación, riesgo percibido, elección y reconsideración.
- `treskal_stress_strain_recovery_contract_v0.1.json` — STRS01–STRS07, presión acumulada, sobrecarga y recuperación causal.
- `treskal_personality_traits_contract_v0.1.json` — PERS01–PERS10, rasgos estables, expresión contextual y evolución lenta.
- `treskal_memory_salience_forgetting_contract_v0.1.json` — MEM01–MEM08, memoria episódica, relevancia, revisión y olvido.
- `treskal_personal_values_principles_contract_v0.1.json` — VAL01–VAL08, principios personales, conflictos y revisión de compromisos internos.
- `treskal_self_concept_roles_contract_v0.1.json` — SELF01–SELF08, identidad personal, roles vitales y transición del autoconcepto.
- `treskal_interpersonal_trust_contract_v0.1.json` — TRUST01–TRUST08, confianza por dominios, daño y reparación.
- `treskal_expectation_revision_contract_v0.1.json` — EXP01–EXP08, anticipación, incertidumbre, sorpresa y revisión de expectativas.
- `treskal_attention_focus_contract_v0.1.json` — ATTN01–ATTN08, foco, distracción, sobrecarga y procesamiento de señales perceptibles.
- `treskal_basic_physical_needs_contract_v0.1.json` — NEED01–NEED05, necesidades físicas cotidianas y resolución cualitativa.
- `treskal_dialogue_dynamics_contract_v0.1.json` — DIAL01–DIAL08, disponibilidad, temas, interrupción y cierre de conversación.
- `treskal_personal_views_attitudes_contract_v0.1.json` — VIEW01–VIEW08, actitudes y opiniones personales con base e historia propias.

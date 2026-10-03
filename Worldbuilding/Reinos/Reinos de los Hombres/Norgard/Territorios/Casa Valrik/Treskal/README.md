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

# D.P14 — Habitabilidad e implantación territorial (diseño condicionado)

**Estado:** cierre de reglas documentales, ninguna celda ni asentamiento autorizado físicamente.

## Método contrastado con Valrik

La metodología Valrik separa esqueleto → posibilidades → coherencia → probabilidades → instancia persistente. Darovan D06 conserva ese orden; D.P14 inserta **diez puertas de elegibilidad física** antes de que un peso regional pueda decidir nada. Se protege el canon con el orden:
`autoridad → relieve/suelo → agua potable → cuenca/riesgo → derecho territorial → acceso real → sustento → cobertura → comunidad → instancia`.

La *posibilidad* no prueba emplazamiento; un enclave minero necesita explotación concreta y no se transforma por magia en un pueblo. El mapa ilustrado de Nimroel no es cartografía georreferenciada.

## 10 puertas de evaluación

1. **authored_anchor:** Clasificación de unidad y prohibiciones del canon y ciudad manual separada. Evidencia: source_status, protected_anchor.
2. **topography:** Pendiente, estabilidad, geomorfología y condición del sitio. Evidencia: approved_site_coordinates, validated_terrain.
3. **water_supply:** Abastecimiento legal y potabilidad comprobada; río no equivale a agua potable. Evidencia: source_identity, seasonal_reliability, potability, access_right.
4. **drainage_risk:** Riesgo de crecida, erosión, costa y helada si está justificado. Evidencia: topography, basin, exposure.
5. **legal_land_use:** Titularidad y usos permitidos bajo Norgard/Casa. Evidencia: jurisdiction, land_use_rights.
6. **accessibility:** Acceso real comprobado, no la mera relación comercial abstracta. Evidencia: verified_physical_route_or_access.
7. **food_and_sustenance:** Base económica comprobada y cobertura alimentaria. Evidencia: resource_or_supply_proof, local_capacity.
8. **network_coverage:** Cobertura de salud, cuidados, empleo, servicios y abastecimiento. Evidencia: provider_exists, capacity, travel_access.
9. **community:** Diferenciar enclave productivo de comunidad residente. Evidencia: resident_community_evidence, legal_residence.
10. **persistence:** Instancia solo después de elegibilidad, ID y semilla estables. Evidencia: world_state_authority, versioned_generation.

## Matriz de 12 ámbitos de estudio y advertencias

| Unidad D01 | Modelos D06 con peso positivo (solo posibilidad) | Guarda |
|---|---|---|
| `d01_valkram_oeste` | ganadera, minera_auxiliar, metalurgica_auxiliar, forestal_sostenible, enclave_especializado | Ningún yacimiento nuevo: toda actividad minera exige explotación concreta, título, accesos y riesgos |
| `d01_elyra_paso_peninsular` | ganadera, enclave_especializado | La ganadería y refugios requieren derechos, agua y acceso real; minería Darovan no se infiere |
| `d01_norte_transicion` | agricola, ganadera, forestal_sostenible, enclave_especializado | El cultivo o pastoreo necesita ventana efectiva de uso y asentamiento legal |
| `d01_aguja_litoral` | Ningún modelo D06 habilitado | Su borde litoral es una posibilidad distinta, nunca lugar automáticamente habilitado |
| `d01_belara_treihord` | agricola, ganadera, minera_auxiliar, metalurgica_auxiliar, servicio_camino, enclave_especializado | La cercanía de río no prueba agua potable o llanura inundable; proteger ocho barrios |
| `d01_veldora_litoral` | agricola, ganadera, pesquera, servicio_camino, enclave_especializado | La carretera cualitativa Veldora–Treihord no aprueba conexiones locales o rutas nuevas |
| `d01_linde_caminos` | agricola, ganadera, forestal_sostenible, servicio_camino, enclave_especializado | Puestos y posadas solo bajo demanda, acceso acreditado y derechos |
| `d01_pilares_sur` | agricola, ganadera, forestal_sostenible, enclave_especializado | Sostenibilidad, titularidad, recuperación forestal y trazabilidad minera/combustible obligatorias |
| `d01_taramin_norte_centro` | agricola, ganadera, pesquera, enclave_especializado | Barrancos estacionales no garantizan agua permanente; Taramin no se genera |
| `d01_taramin_bosque_sur` | agricola, ganadera, pesquera, forestal_sostenible, enclave_especializado | Lomas 150–500 m solo referencia, sin dividir bosque ni crear industria maderera |
| `d01_syvaris` | agricola, ganadera, pesquera, insular_mixta, enclave_especializado | Bosques dispersos; no se autorizan rutas marítimas o puertos de las calas |
| `d01_arven_contexto` | ganadera, pesquera, forestal_sostenible, insular_mixta, enclave_especializado | Manto Verde ~90 % y aldeas costeras ya conocidas, sin crear aldeas nuevas o talar la masa continua |

Los pesos D06 (0–4) **no son porcentajes ni probabilidades de presencia**, ni definen cuántas aldeas existen. Una referencia altitudinal D.P13 **no sustituye** una malla de elevación de un sitio y no implica accesibilidad, potabilidad, cosecha ni pasto.

## Resultado demostrable

Se puede determinar **qué hace falta demostrar para implantar un lugar** y qué propuestas rechazar. No se puede determinar aún la lista de casillas habitables o una distancia al pozo/mercado. La documentación no crea propietarios, aldeas, hidrología menor, puertos, puentes ni porcentajes de superficie utilizable.

**Datos:** `../Datos operativos/darovan_dp14_habitability_planning_v0.1.json`; heredados D01, D02, D03, D06 y D.P13.

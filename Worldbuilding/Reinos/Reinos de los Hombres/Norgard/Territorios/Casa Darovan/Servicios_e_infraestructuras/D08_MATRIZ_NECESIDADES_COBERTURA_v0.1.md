# D08 — Matriz de necesidades y cobertura territorial v0.1
**Distinción decisiva:** necesidad funcional ≠ presencia probada de edificio, negocio, profesional o infraestructura. El JSON marca todos los establecimientos físicos NUEVOS como listas vacías.

| Necesidad | Resolución potencial por regla superior | Requisitos reales / ausencia admisible |
|---|---|---|
| Alimentación | hogar, producción, comercio | alimento existente, preparación, conservación y acceso; carencia puede persistir |
| Agua | pozo/fuente/manantial/arroyo **solo si sitio verificado** | potabilidad, extracción y tiempo; no dibujar fuentes nuevas |
| Higiene/salubridad | tareas `CHORE`, gestión `WASTE` | separación agua/residuos, contenedor, transporte y destino reales |
| Cuidados | hogar, red efectiva, especialista | `CARE`: capacidad, presencia, vínculo y tiempo; no cuidador automático |
| Salud | autocuidado, curandera formada, visita | `HLTH`, competencia, materiales y traslado; Norgard **sin hospitales públicos universales** |
| Aprendizaje | transmisión doméstica, mentor, oficio | `APR`, supervisión y edades; **sin escuelas obligatorias por ciudad** |
| Alojamiento | vivienda ocupada legalmente, posada posible | `RES/OWN`, espacio/derecho; **posada no garantizada en aldea Darovan** |
| Transporte | conexión/modalidad acreditada | D05: accesos físicos comprobados, no rutas creadas por demanda |
| Mantenimiento | hogar, reparador, herrero/carpintero condicionado | herramientas, capacidad, materiales, presupuesto y espera |
| Comercio/abasto | producción doméstica, vecino, especialista, mercado | `TXN/WAIT`, mercancía real, proveedor real; no tienda omnipresente |

## Perfiles de consulta — no dotaciones automáticas
- **Treihord:** ciudad ~32.000; verificar demanda elevada de agua, alimentos, residuos y cuidados junto a trabajo industrial. El Crisol y La Vena mantienen condiciones de seguridad; no modificar barrios, plazas, puertas o canon.
- **Veldora:** cadenas de comercio/aduana exterior/almacenes/talleres y sectores orgánicos aprobados conceptualmente; higiene portuaria, espera comercial y vivienda mixta por analizar. Sin redes, muelles o aforos nuevos.
- **Taramin:** atención especial a manejo de pescado, residuos, agua y actividad en su zona pesquera conceptual; no navegar por los dos brazos del Thalen ni asignar puentes o muelles.
- **Syvaris:** puerto seguro y bahía principal con presencia naval **de Norgard**; cobertura insular de alimentos, agua, cuidados y logística de estudio, sin asumir ferris ni puertos en calas.
- **Aldea/pueblo/villa/enclave D06:** examinar las nueve familias de modelos y exigir evidencia por sitio, sin rangos poblacionales de Valrik, gremios/profesionales automáticos o localidades nuevas.
- **Agujas interior:** sin población permanente. **Arven:** territorio Darovan, no quinta ciudad ni ruta marítima acreditada.

## Lectura de resultado
Por cada necesidad: `necesidad` + `cobertura evaluable` + `fuente aprobada` + `disponibilidad/capacidad real UNKNOWN si no existe evidencia`. Nunca igualar prestación conceptual con instalación existente. A la llegada de datos concretos, consultar ocupación, agendas, materiales, cola/urgencia, coste e inventarios sin privilegiar automáticamente al jugador.

## Requisitos pendientes
Aprobación poblacional, cantidades de viviendas, fuentes de agua y vías de acceso locales, capacidad efectiva de servicios, catálogo de negocios individuales, personal/competencias concretas, stocks, rutas medibles. D08 no establece ninguno.

# DAROVAN D01 — Perfil operativo de relieve, no-runtime

**Estado:** especificación documental NO CANÓNICA. Archivo de datos adjunto: Datos operativos/darovan_d01_relief_profile_v0.1.json.

## Propósito
Un único índice cualitativo para ingeniería futura; **no** contiene campo de elevaciones, GIS, mapa de tiles, bounding boxes, posiciones, polígonos, porcentajes inventados ni parámetros de simulación. No asigna pueblos, climas locales cuantitativos ni superficies forestales nuevas.

## Contrato de lectura
- Cada unidad física posee clave técnica estable d01_*, descripción, referencias a fuente y administrativeOwner. El valor null significa UNKNOWN y **no** se traduce como Darovan por defecto.
- Los cuatro cityAnchors están protegidos como ciudades manuales. La relación entre un lugar confirmado de Darovan y su entorno físico no transmite propiedad a todo el entorno.
- Los constraints indican prohibiciones o hechos ya escritos en canon; no autorizan al motor a generar datos.
- Contiene anclas hidrográficas **solo como restricciones D02**, no como grafo navegable.
- Los posibles microrelieves se copian como **enumeración de tipos de Nimroel Core**, no como instancias cartográficas. Cualquier elemento nuevo necesita macrorelieve real y trazabilidad, nunca azar sin contexto.
- El orden de dependencias subordina drenaje a relieve y capa humana a cauces. No se permite que una ruta o aldea arbitraria imponga la cuenca que le conviene.
- Las clasificaciones AUTHORED, DERIVED, GENERATED, DYNAMIC y UNKNOWN son las de Core. Los textos de D01 constituyen **planificación**, no registros AUTHORED nuevos.

## Matriz rápida de transferencia
| Receptor | Datos D01 | Obligación del receptor |
|---|---|---|
| D02 Hidrografía | relaciones Belara/Lhera/Veldora/Thalen, unidades de transición, prohibiciones | calcular conexión y sentido de flujo desde terreno, no inventar cuencas |
| D03 Clima | gran norte frío, occidente oceánico, Taramin seca-gradual, Syvaris heterogénea | no inventar grados, lluvias o fechas de nieve |
| D04 Recursos | Valkram oro/plata, Pilares maderero, costa | no colocar minas y muelles sin mapa validado |
| D05 Rutas | camino Veldora–Treihord, relación de puntos, barreras montañosas/litorales | caminos, pasos y tiempos necesitan autoridad |
| D06 Asentamientos | prohibición de poblar Agujas, transiciones forestales y costeras | no generar instancias en esta fase |
| D07 Ciudades | cuatro anclas manuales con paisajes asociados | preservar Treihord y diseños urbanos canónicos |
| D11 Runtime | JSON como referencia de validación | integrar/normalizar mediante contrato real antes de ejecutar |

## Control de versiones y estabilidad
Cambios de fuente futura no deben retocar silenciosamente la geografía de la partida: Core requiere persistencia de geometría materializada. Si el autor aprueba límites o cotas, se emitirán fuentes separadas con versión, migraciones y control humano. Ninguna clave d01_* implica un topónimo lore.

## Referencias
Worldbuilding/Sistemas/Nimroel Core/Datos operativos/nimroel_physical_geography_drainage_contract_v0.1.json, Worldbuilding/Sistemas/Nimroel Core/Geografia fisica/geografia_fisica_drenaje_hidrografia_v0.1.md, Norgard/Geografía/*.md y norgard_regions_v0.1.json. Los originales prevalecen siempre sobre este derivado.

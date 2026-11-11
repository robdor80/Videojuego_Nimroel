# D.P18 — Auditoría final de profundidad y cierre de D.P14–D.P18 (versión rescatada)

**Fecha:** 11/11/2026. **Ámbito:** revisión editorial, de coherencia canónica y de trazabilidad; **no auditoría de motor ejecutable**.  
**Status de edición:** propuesta de cierre de las **cinco capas de diseño** una vez verificadas pruebas finales de la PR #41. No se confunde con fusión en main ni con construcción completa del territorio.

## 1. Por qué se rehizo la entrega

La entrega inicial D.P14–D.P18 contenía buenas prohibiciones y matrices, pero buena parte de su peso estaba en JSON, 70 mutaciones negativas, 99 capítulos indexados y cuatro fichas de ciudad con los mismos doce campos pendientes. Su error fundamental era **confundir cobertura formal con profundidad creativa**.

El rescate conserva el material técnicamente útil y añade una capa de **vida territorial**, que ahora puede leerse, imaginarse y usarse como punto de partida jugable:

- D.P14: doce perfiles con vida humana, presión ambiental, decisiones de emplazamiento, conflictos plausibles y estaciones.
- D.P15: nueve modelos D06 y diez necesidades D08 reinterpretados a través del trabajo, hogares, escasez, custodia, intercambio y **ocho cadenas narrativas**.
- D.P16: **cuatro documentos de ciudad reescritos de forma distinta**, con ambientes, espacialidad funcional, ritmo humano, protagonistas potenciales y **21 semillas de escena**, más una comparativa.
- D.P17: además de 24 escenarios negativos TEST_ONLY y catálogo de herencia, **cinco recorridos de acción** y tres historias sociales persistentes de diseño.
- D.P18: las doce lagunas del dictamen original se mantienen, pero separando **ausencias de diseño editorial** de **materialización urbana, cartográfica y runtime prevista para otras fases**.

No han surgido 21 misiones ejecutables ni una sola población nueva por escribir esas situaciones: son **artefactos de autoría y especificación**, no objetos del WorldState.

## 2. Tabla de suficiencia honesta por fase

| Fase | Evidencia creativa nueva | Pasa su objetivo de diseño | Lo que NO dice haber terminado |
| --- | --- | --- | --- |
| D.P14 habitabilidad | D.P14/02 doce paisajes humanos, estaciones y cuatro pruebas narrativas; D.P14/01 diez puertas | **SÍ: planificación territorial/ecológica** | Malla de terreno, solares, fuentes/pozos nuevos, posiciones de asentamientos |
| D.P15 red regional | D.P15/03 ocho cadenas de trabajo/servicios y causalidad social; D.P15/01–02 nueve modelos/diez necesidades | **SÍ: diseño de red económica y carencias** |  Proveedores instanciados, censo real, inventarios, rutas y tiempos |
| D.P16 cuatro ciudades | Cuatro fichas reescritas y D.P16/03 comparativa con 21 escenas distintas | **SÍ: anteproyectos diferenciados** | Nuevos barrios canónicos, ciudadanos nominados, plano urbano cerrado |
| D.P17 interacciones | D.P17/02 cinco acciones y tres historias sociales con autoridad/memoria; D.P17/01 casos de contrato | **SÍ: especificación funcional conceptual** | Código de simulación, API pública, integración C++/Godot y pruebas físicas |
| D.P18 auditoría | Comparación local/Treskal, clasificación de 12 huecos, presente informe y traspaso | **SÍ: auditoría documental de alcance** | Un mundo ya materializado y equivalente a Treskal en plano urbano |

**La distinción es deliberada.** No afirmamos «cuatro ciudades terminadas» ni «Casa Darovan completamente jugable». Sí afirmamos que estas cinco fases aportan suficiente contenido para desarrollar Veldora en D.P20 **sin volver a iniciar sus matrices**.

## 3. Revisión de las doce lagunas originales, sin maquillarlas

| Código | Tema | Situación tras rescate | Trabajo correctamente asignado |
| --- | --- | --- | --- |
| P18-G01 | Veldora: barrios/huella | **Anteproyecto rico**, todavía sin barrios canónicos ni geometría | **D.P20 Veldora** + cartografía futura |
| P18-G02 | Taramin: interfluvio/fachada pesquera | **Anteproyecto rico**, sin puentes/puertos autorizados | **D.P21 Taramin** + evidencia hídrica/cartográfica |
| P18-G03 | Syvaris: bahía/sectores civil y naval | **Anteproyecto rico**, sin planos o dependencias nuevas | **D.P22 Syvaris** + autoridad naval real/cartografía |
| P18-G04 | Treihord: geometría precisa | Ya hay **canon urbano completo** (ocho barrios/cuatro plazas/puertas) y nueva lectura de juego | **D.P23** para vida adicional sin rediseño; cartografía métrica después |
| P18-G05 | Relieve y casillas de doce áreas | D.P14 da criterio humano, D.P13 cotas de referencia | Terreno/DEM y escala reales, fase material futura |
| P18-G06 | Nacimientos, bocas y red menor | Cinco ríos/cuatro sistemas conservados, Fhalion boca exacta UNKNOWN | Fuente cartográfica/topológica posterior |
| P18-G07 | Rutas y tiempos | Sólo tres enlaces materiales D05 de naturaleza distinta; servicios condicionados | Grafo físico y capacidades al construir el mundo |
| P18-G08 | Censo exacto/hogares | Rangos D08 protegidos; jamás multiplicar hogares por habitantes | Datos concretos de autor o población procedural persistente |
| P18-G09 | Profesionales, edificios, capacidad | Arquetipos y secuencias listas; no se crea proveedor automático | D.P20–D.P25 al definir NPC/locales + runtime |
| P18-G10 | NPC nominados y genealogías | Roles y conflictos **no estereotipados** preparados | D.P20–D.P25: autoría concreta con aprobación |
| P18-G11 | Variables ambientales medidas | Mecanismos e impactos humanos explicados sin inventar mm o viento | Cartografía/calibración física posterior |
| P18-G12 | Ejecutable CoreRPG/host | D.P17 conceptual robusta y D11 Content Pack de identidad | Fase de ingeniería posterior con pruebas Windows/Android |

**No marcar G01–G12 como «cerradas» numéricamente**: hacerlo falsearía las dependencias. La capa de diseño puede estar terminada aunque la siguiente capa de autoría o ejecución siga por hacer. Los huecos se transforman en una lista ordenada de **entregas futuras, no defectos ocultos**.

## 4. Control de canon: treinta comprobaciones de continuidad

### Geografía e hidrografía
1. Treihord se mantiene junto al Belara, nunca atravesado por él.
2. El uso Belara/Treihord para barcazas pesadas es somero e industrial.
3. Lhera nace como separación del Belara y adquiere nombre/curso propios.
4. El río Veldora es independiente del sistema Belara/Lhera.
5. Fhalion sigue separado y su desembocadura precisa no se inventa.
6. Thalen es un único río con **dos brazos terminales** que dejan Taramin entre ellos.
7. Las doce unidades D01 no se han convertido en comarcas políticas ni polígonos.
8. La Viuda y las cotas aprobadas de Valkram/Elyra no pasan a alturas de parcelas.
9. Bosque de los Pilares es uno; Bosque de Taramin también es uno.
10. Interior del Bosque de las Agujas sin residentes permanentes.
11. Manto Verde ~90 % de Arven; Arven bajo Casa Darovan.
12. Syvaris tiene gradiente seco/verde y bosquetes dispersos, no selva homogénea.

### Sociedad, ley y economía
13. Se mantienen Treihord, Veldora, Taramin, Syvaris como cuatro ciudades manuales.
14. Poblaciones: ~32.000 / 29–35 mil / 14–20 mil / 7–10 mil (ciudad, no isla).
15. Treihord conserva ocho barrios, cuatro plazas, cuatro puertas.
16. La Bóveda está al N/NE del casco, fuera de antigua muralla; la muralla histórica circunda El Recinto.
17. El Crisol ensaya/refina/funde lingotes pero **no acuña**.
18. El carbón de Treihord procede de Azurios, sin ruta ficticia.
19. La Vena es galería restringida, no tránsito público.
20. Veldora conserva varios sectores comerciales orgánicos y aduana **exterior** real.
21. Taramin mantiene una zona pesquera principal de criterio, no puerto fluvial inventado.
22. Syvaris concentra actividad en bahía y tiene **Armada Real**, no Darovan.
23. Justicia del Rey y normativa de Norgard prevalecen; la Casa no legisla por su cuenta.
24. Los NPC mantienen individualidad y conocimientos adquiridos; no hay personalidad por barrio, oficio o isla.
25. No se han creado NPC con apellido protegido ni un Lord/Lady gobernante por inferencia.
26. No se han inventado hospitales públicos universales, escuelas obligatorias, fábricas modernas ni monedas.
27. Matrimonio/duelo, instituciones y comercio se mantienen bajo reglas superiores; no nuevas fiestas ni ritos canónicos.
28. Existen sólo las rutas materiales D05 acreditadas; una oferta comercial no es un camino.
29. No se generan tiendas, barcos, recursos, casas o habitantes por exigirlos una escena.
30. La IA narra hechos filtrados; CoreRPG mantiene la realidad y el guardado.

**Resultado de esta auditoría documental:** las nuevas propuestas respetan estas anclas en su texto. Los 30 puntos NO constituyen un test ejecutable sobre un mapa inexistente.

## 5. Valrik/Treskal: comparación válida y comparación imposible

**Valrik/Treskal aporta método:** separación de espacios y responsabilidades; topología, servicios, memoria, instituciones, empleo, vida cotidiana, historia, cartografía y simulación; las reglas generales pasan a Core/Norgard en vez de copiarse en cada Casa.

**Darovan D.P14–D.P18 aporta ahora:** diferencia entre medio físico y actividad humana, cadena económica, cuatro identidades urbanas legibles, situaciones narrativas, autoridad legal y diseño de persistencia.

**No son equivalentes todavía en extensión final:** Treskal tiene base funcional urbana y cartografía métrica propia; Veldora, Taramin y Syvaris **todavía no** tienen barrios canónicos completos, personas relevantes y localización geométrica. Es precisamente el objetivo de D.P20–D.P22, mientras Treihord requiere densificación sobre su original.

Contar cien carpetas o 57 namespaces de referencia sólo confirma que se **indexaron**, no que se revisó cada regla, y mucho menos que un NPC real pueda recorrer un mapa.

## 6. Orden a partir de esta entrega (sin nuevas vueltas)

- **D.P20: Veldora**, ciudad única en profundidad y con aprobación de contenido canónico.
- **D.P21: Taramin**.
- **D.P22: Syvaris**.
- **D.P23: Treihord**, completar vida sobre el canon original.
- **D.P24: asentamientos ordinarios y vida rural**.
- **D.P25: NPC relevantes, relaciones y conflictos territoriales**.
- **D.P26: coherencia total y auditoría final de autoría**.

Cada fase nueva se abre en **otra conversación**, una tras otra; no reabrir D.P14–D.P18 para repetir matrices. Los pendientes métricos/implementación no deben impedir el diseño literario si se declaran y se respetan.

## 7. Qué significa cerrar D.P14–D.P18

**Cierre editorial propuesto:** cinco entregas de **diseño** suficientes y coherentes, con archivos nuevos y reescritos, cada una con objetivo y límites concretos. El canon nuevo sigue reservado al autor; no lo convierten en aprobado los tests de Python.

**Cierre técnico de PR:** comprobar GitHub Actions **en el HEAD exacto tras los cambios**, revisar regresiones D.P13 y D01–D12 y certificar que no se ha alterado el catálogo de D11 ni el runtime.

**Cierre Git:** sólo tras autorización expresa de fusión al repositorio principal. La PR permanece Draft mientras tanto. No confundir «documentación lista para revisión» con «ya fusionado».

Esta auditoría no se sustituirá por un contador de archivos. Un capítulo se acepta por **contenido específico, coherencia con sus fuentes y posibilidad real de usarlo para jugar o seguir construyendo**, no por su tamaño.

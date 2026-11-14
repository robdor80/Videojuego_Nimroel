# E20-P00 — Auditoría comparada Valrik/Treskal ↔ Casa Edranor

**Fecha:** 14-11-2026. **Base de lectura:** main en 223f1e49adfbc73be6a80c6ce36e7aab506450c2. **Estado:** AUDITORÍA DE SUFICIENCIA, NO CIERRE DE E20. **Autoridad:** mandato autoral del 14-11-2026: Valrik/Treskal es el suelo de calidad obligatorio para cada territorio, con adaptación regional y sin duplicar sistemas universales.

## 0. Dictamen

**NO CONFORME / PARIDAD NO ACREDITADA.** Edranor E00–E18 posee un corpus de diseño B2 bastante amplio y coherente, pero ninguna de las diez dimensiones de la matriz E18 ha alcanzado B3 o B4. Las cuatro monografías E07 no constituyen ciudades ni aldeas materializadas; los modelos E13–E17 son estudios o contrafácticos. La PR E19 #84 fue CERRADA SIN FUSIÓN y DESCARTADA por el autor: ni sus geometrías ni sus contratos podrán reciclarse o citarse como fuente aceptada.

No se degrada el valor de E00–E18 como investigación. Sí se prohíbe emplearlo para afirmar que Edranor está al nivel de Valrik. **No se certificará E20-Dorth ni E21–E29 por rellenar índices, contratos vacíos o número de escenarios.** Si faltan pruebas, el estado será BLOQUEADO o DISEÑO, no COMPLETADO.

## 1. Método y universo inspeccionado

Se inspeccionaron exhaustivamente los **árboles de rutas** de los dos territorios en main (objetos Git de Casa Valrik fe9795fd... y Casa Edranor f0f5472c...), y se revisaron en profundidad documentos y contratos rectores del territorio, Treskal, E07, E13 y E18. La comparación de **contenido** es dirigida por capacidades y evidencias; el inventario de rutas no equivale a declarar que se han leído individualmente todos los párrafos de los 639 archivos. Esta limitación se registra expresamente para no falsear una auditoría total de contenido.

| Magnitud observada en los árboles | Valrik/Treskal | Edranor |
|---|---:|---:|
| Archivos | 437 | 202 |
| Markdown | 298 | 180 |
| JSON | 135 | 21 |
| GeoJSON | 1 | 0 |
| SVG | 3 | 1 |
| Bytes de objetos en el árbol territorial | 3.666.824 | 794.848 |
| Archivos bajo Treskal / Edranor-Ciudades | 368 | 7 |
| Parcelas métricas ordinarias acreditadas | 2.175 en Treskal | 0 |

**Advertencia:** tamaño y cantidad no son medidores de calidad. La mayor parte de los 99 ámbitos de Treskal se refiere a funciones reutilizables, no a 99 módulos que cada ciudad deba copiar. La evidencia decisiva es: fuentes verificadas → entidades y conexiones identificables → reglas locales coherentes → operaciones y persistencia testeables.

Fuentes rectoras directas:
- [Valrik — territorio](../../Casa%20Valrik/territorio_valrik.md).
- [Treskal — canon consolidado](../../Casa%20Valrik/Treskal/00_Canon/treskal_canon_consolidado.md).
- [Treskal — auditoría funcional 01–99](../../Casa%20Valrik/Treskal/AUDITORIA_CIERRE_FUNCIONAL_TRESKAL_v0.1.md).
- [Treskal — plan métrico canónico v1.0](../../Casa%20Valrik/Treskal/08_Cartografia/mapa_canonico_definitivo_treskal_v1.0.md).
- [Treskal — contrato cartográfico y export](../../Casa%20Valrik/Treskal/Datos%20operativos/treskal_canonical_map_contract_v1.0.json).
- [Edranor — matriz E13](../E13/08_MATRIZ_PARIDAD_DAROVAN_VALRIK_EDRANOR.md).
- [Edranor — matriz E18](../E18/01_MATRIZ_DIEZ_DIMENSIONES.md).
- [Edranor — deuda E18](../E18/03_HALLAZGOS_DEUDA_Y_PRIORIDAD.md).
- [Edranor — dictamen E18](../E18/04_DICTAMEN_Y_TRASPASO_E19.md).
- [Edranor — plan E13–E29](../E13/09_PLAN_MAESTRO_E13_E29.md).
- [Edranor — anclas E07](../Datos%20operativos/edranor_e07_canonical_nuclei_v0.1.json).
- [Edranor — auditoría operativa E18](../Datos%20operativos/edranor_e18_maturity_audit_v0.1.json).
- PR descartada E19: https://github.com/robdor80/Videojuego_Nimroel/pull/84 .

## 2. Qué aporta realmente Valrik

### 2.1 Territorio y red de asentamientos

La Casa Valrik administra el extremo oriental de Norgard. Su identidad —honor, hospitalidad, excelencia maderera, oficio artesanal y construcción naval bajo autoridad de la Corona— está formulada en el territorio maestro y se traduce en red de abastecimiento rural. Tiene tipologías diferenciadas de aldea, pueblo y villa, perfiles funcionales, requisitos mínimos y cobertura compartida de servicios, reglas probabilísticas y generación regional determinista con identidades persistentes. Por ejemplo, la herrería básica rural no puede eliminarse alegando cobertura genérica: es particularidad local validada.

Hay corpus en **Aldeas (12 archivos), Pueblos (19) y Villas (15)** y reglas de generación para la región de Treskal, no solo una lista de topónimos. Estos contratos tampoco implican que cada aldea exista ya como entidad cargada en Godot.

### 2.2 Treskal: modelo funcional y ciudad espacial

Treskal tiene **99 ámbitos numerados de capacidad funcional**: estructura urbana; topología; infraestructura; viviendas; edificios singulares; mercados; NPC; reputación; percepción; viaje; actividad laboral; familia y ciclo vital; bienes; propiedad; cuidado; conversación; memoria; IA; simulación, etc. El cierre funcional declara **base de diseño**, no ejecución completa.

Treskal supera el diseño conceptual cartográficamente con **10 puntos métricos cerrados**:
- referencia local **TRESKAL_LOCAL_METRIC_V1**, unidades en metros y norte +Y;
- **12 sectores funcionales T01–T12** previstos en el encaje (11 polígonos sectoriales del export, conforme al contrato);
- **13 instalaciones singulares S01–S13**, una desglosada en componentes;
- **18 vías principales C01–C18**, **12 calles locales L01–L12**, **12 zonas de tejido UF01–UF12**;
- **110 bloques B001–B110** y **2.175 parcelas P0001–P2175**;
- export **GeoJSON de 2.404 entidades con ID estable** y tres planos SVG (técnico, operativo, legible para lore);
- pruebas documentadas de compatibilidad y restricciones, incluida la corrección del acceso continental al complejo naval T08.

Esta es la clase de evidencia material que Edranor no posee: **no significa que Edranor deba tener 2.175 parcelas, un puerto, 13 instalaciones ni 99 documentos**. Debe tener su propio tejido verificado y cubrimiento funcional adecuado al tamaño y la actividad.

### 2.3 Lo que tampoco debe fingirse sobre Valrik

La auditoría de cierre de Treskal distingue explícitamente **BASE FUNCIONAL** de **runtime final**. Los 99 ámbitos y los contratos no demuestran que existan ya NPC ejecutándose, mundos poblados o interiores finalizados. La comparación da por demostrada la materialización cartográfica de Treskal y la riqueza funcional de sus contratos, **no B4 integral ni un videojuego terminado**.

## 3. Estado de Edranor E00–E18 confrontado con esa referencia

| Dimensión | Acreditado para Edranor | Diferencia real con el patrón | Semáforo de aceptación |
|---|---|---|---|
| Geografía / relieve | E01/E13: 7 unidades de estudio; U7 no evaluable | No cierre norte, CRS, geometría métrica, DEM ni malla validada | BLOQUEO MATERIAL |
| Clima / agua / suelos | E02/E03/E13/E14: cadenas físicas y aptitudes condicionales | No cuencas, pozos, parcelas ni microclimas anclados a terreno verificado | DISEÑO B2 |
| Producción / recursos | E04/E15: uva, vino, bosques, tonelería, balances y escenarios | Sin titulares, viñas, cosechas, lotes, barricas, rendimientos ni derechos materializados | DISEÑO B2 |
| Asentamientos | E06 arquetipos; E07: Dorth/Lumina/Karsath/Rodas | 7 fichas urbanas frente al corpus funcional de Treskal; sin red ni trazado local probado | BLOQUEO MATERIAL |
| Población / hogares | E08/E14: oferta, demanda, oficios, servicios, 24 opciones sintéticas | Sin censo o viviendas/hogares/vecinos conciliados y ubicados | DISEÑO B2 |
| Administración / defensa | E09/E16: competencias y reglas de jurisdicción | Sin cargos efectivos, sedes localizables, responsables, efectivos u órdenes realistas instanciadas | DISEÑO B2 |
| Cultura / memoria | E10, E17: tradiciones, cronología relativa y posibilidades | Sin escenas vividas con personas y sucesos de autoridad confirmada | DISEÑO B2 |
| Personajes / redes | E10: 11 propuestas de nombres/personajes, E17 causalidad | Sin biografías individuales plenamente legitimadas, hogares, horarios, vínculos persistentes | DISEÑO B2 |
| Conflictos / consecuencias | E10/E17: ganchos, 32 contrafácticos | No hay sucesos ocurridos, decisiones ni efectos persistidos | DISEÑO B2 |
| Contratos / implementación | E11 Core sintético, E13–E18 JSON y validadores | No escenas Godot/World State territorial jugable, carga y salvado de entidades Edranor | BLOQUEO RUNTIME |

**Calificación de referencia:** E18 sitúa las diez dimensiones Edranor en B2, ninguna en B3/B4. No se sube de nivel por tener un número alto de pruebas sintéticas o documentos.

## 4. Comparación de las localidades: debe haber identidad real, no cambio de etiquetas

| Localidad | Identidad protegida y evidencia E07 | Lo que debe convertirse en realidad verificable |
|---|---|---|
| **Dorth (E20)** | Ciudad sede; vinos tintos; recepción/prensado, bodegas, administración subordinada, borde de Azurios | Huella propia, barrios/sectores, edificios y accesos con IDs, bodegas con capacidad, hogares, productores, inventarios, guardia/justicia, flujos y secuencias narrativas |
| **Lumina (E21)** | Núcleo pequeño sin muralla; blancos de altura; plaza alargada, mercado **anual**, umbral del Bosque Alto | Plaza a escala proporcionada, bodega familiar y viviendas verificadas, calendario y ocupación ferial, bosques con titularidad/licencia, vida cotidiana no industrial |
| **Karsath (E22)** | Producción vinícola muy limitada/selecta, horizonte de lago; entorno más abierto y escasa vegetación | Vista lacustre espacialmente comprobada sin inventar orilla urbana, pocos productores concretos, custodia de lotes, derechos y accesos |
| **Rodas (E23)** | **ALDEA REGIA** bajo Corona Aethros, no Casa Edranor; druídica no templo; berserkers extraordinarios | Viviendas bajas, plaza y Casa Druídica contigua, mandos **regios**, hogares y oficios comunes, custodia y reglas de acceso; sin tributos ni órdenes de Edranor |
| **Campo (E24)** | 7 unidades, viticultura selectiva, bosque regulado, ocupación condicionada | Tipologías locales no calcadas de Valrik, comunidades realmente elegibles, accesibilidad, agua, familias, unidades productivas y abastecimiento |

No corresponde asignar a Lumina los rangos poblacionales de Valrik, ni añadir a Dorth su puerto, ni copiar los astilleros, los puentes o las proporciones de Treskal. **Paridad es densidad de resolución y coherencia operativa, no uniformidad geográfica o demográfica**.

## 5. Ausencias prioritarias con trazabilidad

| ID | Puerta insatisfecha | Evidencia suficiente para levantarla |
|---|---|---|
| P20-01 | Norte territorial y perímetro | Límite completo aprobado y geometría cerrada, con procedencia |
| P20-02 | Escala | Origen, escala reversible y controles documentados; diferencia mapa regional versus escala urbana |
| P20-03 | Agua y relieve local | Terreno/drenaje, relaciones de cuenca y verificación; no inventar captación |
| P20-04 | Red viaria física | Grafo **Gp** real con caminos, pasos, pendientes, cruces y derechos; Gd/Gq no lo sustituyen |
| P20-05 | Plano de Dorth | Zonas, edificios, calles, patios y puntos de actividad con geometría e IDs estables |
| P20-06 | Demografía y residencia | Hogares y viviendas reconciliados, residentes, trabajo, capacidad y movilidad |
| P20-07 | Instituciones efectivas | Oficinas, cargos, autoridad de la Corona, custodias, registros y justicia local |
| P20-08 | Producción local | Bodegas/viñas/madera con acceso y permiso, lotes trazables, almacenaje, consumo y merma |
| P20-09 | Vida material | Agua doméstica, saneamiento, mantenimiento, calor, salud, posadas, comercio y transporte, ajustados al lugar |
| P20-10 | Vida social | NPC con vínculo, trabajo, agenda, aprendizaje, familiaridad, reputación, riesgos, relato y memoria |
| P20-11 | Consecuencia narrativa | Misiones y estados realmente sucedidos y guardados, no solo ganchos o contrafácticos |
| P20-12 | Contrato espacial | Export persistente, geometría trazable, ID técnico independiente del nombre y regresión de la carga |
| P20-13 | Arte y escala | Biblia visual local aplicada sin estandartes ambientales, monstruosidades ni contradicciones del paisaje |
| P20-14 | Integración Godot/Core | Entidades consumidas por Godot 2D y CoreRPG con pruebas de entrada/salida, reproducibilidad y persistencia |
| P20-15 | Reglas de mundo universales | Reutilización explícita de Core y Norgard Defaults, sin reimplementar 99 sistemas |
| P20-16 | Control adversarial | Tests que rechazan puerto en Dorth sin fuente, muelle Karsath, murallas Lumina, fiscalidad Edranor en Rodas y tala sin licencia |

**Clasificación:** P20-01/02/03/04/05/06/08/12 bloquean B3 material; P20-11/14 bloquean B4; restantes requieren instancias verificadas y coherentes para demostrar suficiencia. La ausencia de prueba no equivale automáticamente a contradicción de canon.

## 6. Deuda anterior que permanece abierta

La deuda E18 **EDD-01 perímetro norte, EDD-02 escala, EDD-03 agua local, EDD-04 censo, EDD-05 personajes, EDD-07 caminos y EDD-08 historia** permanece ABIERTA. **EDD-06 Rodas** está resuelta únicamente **para diseño y jurisdicción**, no para materialización o sucesos históricos. E19 #84 no cerró ninguna de estas puertas: fue descartada.

El material E00–E18 y los 5 DefinitionIds E11 **no** equivalen a un NPC, un mercado o un evento jugable. El grafo Gp vacío y los edificios sin coordenadas no pueden pasar inadvertidos en nuevas actas.

## 7. Criterio vinculante a partir de esta auditoría

1. **Bloquear ascenso de B2 a B3** sin mapa/entidades/IDs/evidencia material verificable. Bloquear B4 sin funcionamiento, World State y persistencia probados.
2. **Auditar por capacidades y por lugar**: una localidad se comprueba en espacio, producción, población, servicios, gobierno, cultura, relaciones, economía, riesgo y relato. No basta copiar cláusulas de E14 a E20.
3. **Diseñar al tamaño real** de cada núcleo. El patrón de Treskal exige solución integral, no cantidad fija de parcelas o edificios.
4. **Tomar Valrik como patrón mínimo obligatorio también en futuras Casas**, con un inventario de funciones que el territorio herede de Core/Norgard y una matriz de excepciones locales verificables.
5. **No crear un segundo motor local** para economía, personalidad, clima, calendario, sociabilidad, trabajo o IA. El mundo local ofrece datos, arte, reglas propias y casos, no duplicación de lógica universal.
6. **No copiar ni reflotar E19 #84**: rehacer el procedimiento de fuentes desde cero conforme a los 10 puntos del plano de Treskal, ajustando método a topografía regional.
7. **No cerrar por fecha o por número de fase**: E29 no significa final obligatorio; abrir E30+ si sigue faltando densidad, escala, biografías o ejecución.
8. **La autorización delegada permite diseño**, no fabricar fuentes de cartografía, leyes soberanas, sucesiones o acontecimientos históricos que no estén acreditados.

## 8. Conclusión ejecutiva

**E20-Dorth queda en fase preparatoria (P00) y bloqueado para cierre.** Reabrir el trabajo espacial de E19 mediante una nueva actuación **E19-R** (sin tocar la PR descartada) es dependencia necesaria para la cartografía autorizada. En paralelo se permiten investigaciones, fichas de necesidades, catálogo de capacidades locales y propuestas explícitamente NO MÉTRICAS, sin declararlas producción territorial terminada.

Esta auditoría no concede conformidad a Edranor. Establece la condición objetiva para poder concederla más adelante.

# DAROVAN D02 — Cuencas, divisorias, manantiales y riesgo hídrico v0.1

**Naturaleza:** reglas de coherencia e interfaces D02; sin polígonos, cotas, caudales ni pronóstico simulado. Aplicación universal subordinada a Nimroel Core.

## Cuenca no equivale a territorio político
- **Sistema Belara–Lhera:** red comunicada con **dos receptores marinos** (Golfo de Norgard y Golfo de Veldora). Es una **divergencia canónica**; el software no puede obligar a que toda red tenga una única boca. Cuencas parciales, subcuencas y divisoria exacta permanecen `UNKNOWN`. El flujo que se distribuye en la bifurcación no tiene porcentaje fijado.
- **Sistema Veldora:** red superficial **independiente** con receptor Golfo de Veldora. Su fuente y su divisoria son `UNKNOWN`; no afirmar que nace en Elyra/Valkram, ni conectarla por un afluente al Lhera.
- **Sistema Thalen:** red de península meridional con **dos brazos terminales** pertenecientes al mismo río y receptor Golfo de Norgard. Un interfluvio urbano Taramin está documentado; NO afirmar que sea isla permanente, que ambos brazos lleven siempre el mismo caudal o que exista un puente.
- **Syvaris y Arven:** no se asignan ríos nominados ni cuencas cerradas. Syvaris Darovan, Arven administración no acreditada; la isla no se absorbe en el sistema continental por proximidad.

Los **golfos** son receptores, **no** aristas de unión hidrográfica continental. Compartir el Golfo de Veldora no une automáticamente el Veldora con el Lhera.

## Reglas físicas de alta prioridad (Core)
1. Macrorelieve AUTHORED → malla altimétrica verificada → microrelieve → pendiente y sentido → divisorias y áreas de captación → acumulación → manantiales candidatos → inicio de cursos → conexiones → humedales/inundables → clasificación temporal → capa humana → persistencia.
2. Cada celda de escorrentía natural avanza a igual o menor potencial hidráulico en su trayecto; ascenso requiere **obra hidráulica** explícita y evaluada, no «corrección» aleatoria. Las crestas separan vertientes; un collado no es automáticamente trasvase.
3. Un tributario necesita captación o surgencia sustentable y vértice de unión real; nunca «cruce visual sin conexión» ni confluencia aguas arriba que contradiga canon. **D02 NO CREA NINGÚN AFLUENTE CONCRETO.**
4. Depresiones sin desagüe visible requieren hipótesis comprobable de infiltración, evaporación o balance cerrado; no declarar lagos endorreicos nuevos.
5. Manantiales: registrar **causa plausible** entre nivel freático, contacto litológico, fractura, acuífero colgado, pie de ladera o recarga por lluvias/deshielo. Sin geología, freático y clima local, todas las ubicaciones son UNKNOWN.
6. El caudal y la permanencia dependen de área de captación, recarga, almacenamiento, infiltración y estación. No clasificar Belara, Lhera, Veldora o Thalen como **perennes** únicamente por estar dibujados o nombrados: se desconoce su régimen cuantitativo.
7. **Taramin norte/centro:** canon regional contiene **barrancos/cauces estacionales** (Norgard, geografia_general.md §8 y regiones_naturales.md §7). Esto acredita un **tipo de elemento**, no un arroyo identificado, frecuencia anual ni ubicación cartográfica. Hacia el sur existe transición más húmeda y forestal, pero no se traslada mecánicamente un umbral de generación.
8. **Valkram / Elyra:** las laderas y los fondos de valle pueden concentrar aguas por física de drenaje, pero no asignar cursos por estar una ladera cerca de una ciudad; el Belara sí posee origen norte-occidental canónico. Contrastar sentido de cada drenaje con campo de elevación futuro.
9. **Syvaris:** heterogeneidad seca/húmeda y calas abrigadas no autorizan acuíferos, pozos, arroyos o ríos específicos. **Agujas:** bosque cercano al Lhera pero su interior carece de asentamientos permanentes; no representar drenaje como permiso de poblamiento.
10. **Inundabilidad:** son **susceptibles de comprobación**, no automáticamente inundables, planicies bajas conectadas al río, fondos de valle, uniones, depresiones y brazos terminales del Thalen. No fijar cotas de crecida, frecuencias, parcelas ni daños. D07 revisará ambas orillas de Taramin; D05 cruces, D06 localización segura de asentamientos.
11. **Estacionalidad y estados:** `perennial | seasonal | ephemeral` solo tras datos hidroclimáticos (D03); después pueden existir estados `dry | low | normal | high` como WorldState sin cambiar identidad ni posición.
12. Geometría e ID de cauce materializado son persistentes. Cambios fuertes de curso requieren **evento persistente**, autorización física y migración de datos; no redibujar al cargar.

## Catálogo de hipótesis NO materializadas
| Ambiente D01 | DERIVED posible | Prueba necesaria antes de convertir en datos | Bloqueo |
|---|---|---|---|
| Vertiente occidental Valkram | afluencia por vaguadas/piedemonte | modelo altimétrico + divisorias + aportes | D01/D02 cualitativo; D03 y mapa |
| Linde Agujas-Lhera | escorrentía y humedad ribereña | posición del cauce y microrelieve | D03 y cartografía |
| Pilares / pie meridional | drenajes locales hacia receptor por determinar | pendientes y conectividad real | cartografía |
| Península Taramin seca | barrancos estacionales como **categoría canónica** | microcuenca, clima local, receptor | D03, D07 |
| Taramin tramo Thalen terminal | riesgo potencial en ambas márgenes | cotas, inundación dinámica y obra urbana | D07/D11 |
| Isla Syvaris | pequeños drenajes por definir, no afirmados | lomas, suelo, lluvias, costas | D03/D07 |
| Isla Arven | posibles escorrentías forestales, no cartografiadas | permisos jurisdiccionales y datos físicos | DAR-P01 |

## Condiciones de bloqueo para generador futuro
Rechazar: inversión de gradiente; enlace Veldora–Belara/Lhera; receptor marino equivocado; cauce sin captación; paso de divisoria sin explicación; duplicación de Thalen; pérdida de IDs; cambios de geometría solo por RNG; sedes habitadas dentro de Agujas. Bloquear materialización si faltan dimensiones físicas para esas comprobaciones. El grafo D02 es **solo referencia de planeamiento**, sin generación habilitada.

**Fuentes primarias:** `Worldbuilding/Sistemas/Nimroel Core/Geografia fisica/geografia_fisica_drenaje_hidrografia_v0.1.md`; `Norgard/Geografía/rios_y_lagos.md`; `geografia_general.md`; `regiones_naturales.md`; `montanas.md`; `bosques.md`; `Norgard/Clima/clima_general.md`.

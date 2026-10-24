# D07 — Matriz de hechos, fuente y nivel de autoridad v0.1

**Ámbito:** cuatro ciudades únicas manuales. Referencia máquina: Datos operativos/darovan_d07_canonical_cities_v0.1.json. La documentación local añade condiciones pero no reemplaza las fuentes aprobadas.

## Fuentes con precedencia
- T = Norgard/Ciudades/Casa Darovan/Treihord.md (**CANON, diseño base cerrado**).
- C = Norgard/Grandes Casas/grandes_casas.md.
- V = Biblia visual/Culturas/Norgard/NORGARD_VISUAL_PROFILE_v0.1.md y Datos operativos/norgard_settlements_v0.2.json (**perfiles aprobados; sin plano urbano general**).
- G = Norgard/Geografía/rios_y_lagos.md, mares_y_costas.md, regiones_naturales.md, bosques.md; Clima/clima_general.md.
- F = Norgard/Defaults fiscal/aduanero y navegación civil/pesca.
- D = matrices y datos operativos D01–D06; decisiones expresas de autor (21/10/2026) sobre Arven, río Veldora y Fhalion.

| Ciudad | Hecho respaldado | Fuente primaria / cruce | Etiqueta | No permite inferir |
|---|---|---|---|---|
| Treihord | Capital, ~32.000 habitantes | T §§1–2; C | AUTHORED | cifras de hogares, profesiones o nuevos barrios |
| Treihord | Ocho barrios, cuatro plazas, cuatro puertas, núcleo antiguo amurallado | T §§3–5; anclas D00 | AUTHORED | rediseño o duplicación del canon |
| Treihord | Belara junto, nunca dentro; barcazas industriales someras | T §§6–7; G ríos; D02/D05 | AUTHORED | puerto mercante marítimo, agua potable automática, puentes |
| Treihord | Crisol ensaya/refina, no acuña; Bóveda y Vena custodiada | T §§8–12; F | AUTHORED | ceca, acceso público a Vena |
| Treihord | Carbón de Azurios, metales de Valkram | T §7; D04/D05 | AUTHORED | ruta física de carbón o mina localizada |
| Veldora | Principal puerto comercial; comercio exterior, aduanas, almacenes, gremios | V §§16; C; F | AUTHORED | aduanas entre Casas, muelles o instalaciones nuevas |
| Veldora | Golfo occidental; río Veldora independiente y detrás en visual | G ríos/costas; V; decisión DAR-P07 | AUTHORED | cruces, recorrido urbano o navegación fluvial |
| Veldora | Crecimiento orgánico, piedra/teja, 2 y algunas 3 plantas | V §16 y v0.2 | AUTHORED | número/nombre de barrios y plano |
| Veldora | Sectores ricos alejados de muelles; isla boscosa frente a costa | V §16; G costas/bosques | AUTHORED | trazado o identificación cartográfica exacta de isla visual |
| Taramin | Entre dos brazos finales del mismo Thalen | G ríos; D02; V §18 | AUTHORED | dos ríos, puentes, vados, navegación de cada brazo |
| Taramin | Pesca marítima/fluvial, productos marinos, aceite de ballena | V §18/v0.2; C | AUTHORED | especies, cuota, capturas, edificios o muelles |
| Taramin | Funcional no monumental, ciudad media | V §18/v0.2 | AUTHORED | trazado o habitantes |
| Taramin | Región de transición seca y Bosque de Taramin diverso | G regiones/bosques; clima; D03/D04 | AUTHORED | talas industriales o sequías simuladas |
| Syvaris | Isla Norgard/Darovan, ciudad de bahía y calas sin nombres | C; G costas; D01 | AUTHORED | isla exterior, puertos nuevos, itinerarios |
| Syvaris | Más pequeña que Taramin; puerto seguro y presencia naval Norgard | V §19/v0.2; Defaults navegación | AUTHORED | armada Darovan, flota/capacidad inventada |
| Syvaris | Pesca, comercio, productos del mar y aceites | V §19/v0.2 | AUTHORED | stocks o autosuficiencia cuantitativa |
| Syvaris | Clima cálido parcialmente seco, sur verde, bosques discontinuos | V, G regiones/bosques, clima, D03 | AUTHORED | desierto, bosque continuo, arquitectura totalmente blanca |
| Todas | Excluidas del generador D06 | D00/D06 + decisión DAR-A01 | AUTHORED | municipios procedurales o ciudad quinta |
| Darovan | Arven bajo Casa Darovan, Karsath bajo otra Casa | decisión autor y C; D01–D06 | AUTHORED | convertir Arven en quinta ciudad o abrir rutas |

## Separación de capas
- **AUTHORED:** hechos con referencias, no editados ni reinterpretados como mapa.
- **DERIVED:** coherencias negativas («no es prueba de ruta», «no obliga a puente»), no hechos nuevos.
- **PROPOSAL_PENDING_AUTHOR:** ideas de interfaz urbana para evaluación, sin nombre/posición de barrio, ubicación de edificio ni instancia gameplay.
- **UNKNOWN / pending_autor:** dato sustantivo aún sin aprobación, registrado con valor nulo; futuros valores métricos además exigen cartografía, medición o prueba.
- **World State:** no se instancia entidad de ciudad ni se concede estado de población, propiedad, inventario, travesía o servicio por existir esta matriz.

**Regla editorial:** el documento de Treihord que ya es canon prevalece frente a cualquier simplificación del perfil visual; no crear una «nueva Treihord» para corregir diferencias de detalle.

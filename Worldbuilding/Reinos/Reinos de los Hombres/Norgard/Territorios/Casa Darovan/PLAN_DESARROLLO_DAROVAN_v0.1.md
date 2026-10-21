# Darovan — plan de desarrollo integral v0.1
**Estado:** PLAN DE TRABAJO (NO CANON). **Inicio:** 15-10-2026. **Responsable de aprobar canon:** autor.

## Convenciones y criterios de aceptación generales
- Jerarquía: `Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`.
- Cada entrega diferencia `canon_fuente`, `inferencia_mapa`, `propuesta_tecnica`, `pendiente_autor`.
- Treihord conserva su documento canónico actual; lo demás añade referencias y capas operativas, no lo reemplaza.
- Veldora, Taramin, Syvaris y Treihord son lugares canónicos individuales; **nunca** se generan como asentamientos ordinarios.
- Los documentos aprobados de Valrik son referencias metodológicas, no perfiles transferibles.
- No se afirma funcionamiento runtime por disponer de contratos JSON; requiere integración real con CoreRPG/Godot y pruebas.
- En cada fase: inventario de fuentes, especificación separando niveles, datos operativos si procede, comprobación de referencias y JSON, informe de deuda y PR propio o incrementos auditables. **No merge automático.**

## D00 — Auditoría y arranque [FUSIONADA EN MAIN; PR #14]
- Inventario del canon, fuentes, perfiles, reglas y alcance. Diferencias de línea roja y frontera.
- Comparación con árboles Valrik/Treskal y Core/Defaults.
- Registrar resolución canónica Belara (Eshneva descartado para Darovan por decisión del autor), y detectar dudas pendientes (Arven, casas menores/figuras nobles).
- Entregables: auditoría, inventario del mapa, este plan y manifiesto inicial no-runtime.
- **Cierre 15-10-2026:** estructura territorial y de ciudades preparada; anclas de Treihord y cuatro ciudades auditadas; fuentes trazadas; protocolo de una fase por conversación y una PR por fase; pendientes preservados. Ver `Auditorias/D00_CIERRE_Y_VALIDACION_2026-10-15.md`.
- **Salida:** fuentes trazadas, ninguna alteración de canon, pendientes registrados. La PR debe ser autorizada para fusionar; D01 no comienza en esta conversación.

## D01 — Límites, subregiones y geografía física [FUSIONADA EN MAIN; PR #15]
- Delimitar cualitativamente montaña, costa, bahías, islas, península, gradientes y relaciones políticas sin cartografía falsa.
- Separar capas físicas/administrativas y puntos de control; capa georreferenciada solo cuando exista plano/escala.
- Aplicar contrato Core `nimroel_physical_geography_drainage_contract_v0.1.json`.
- **Salida D01 (15-10-2026):** marco físico y 12 unidades cualitativas con fuentes, perfil JSON no-runtime, interfaz cartográfica, matriz de 18 controles, acta y traspaso D02. **Cierre documental, NO canon nuevo ni implementación runtime.** PR #15 fusionada en main (9f3f723b0e7b2b78567c6397bba7099bfe658b0a).

## D02 — Hidrología y drenaje [FUSIONADA EN MAIN; PR #16]
- Grafos Belara/Lhera/Veldora/Thalen, cuencas, afluentes plausibles, manantiales y arroyos con límites estrictos.
- Zonas de inundación, estacionalidad, vados, navegabilidad y recursos hídricos sin caudales inventados.
- **Salida D02 (15-10-2026):** 4 ríos, 3 sistemas topológicos, 13 nodos, 10 aristas; cuencas cualitativas, perfil JSON no-runtime, reglas, validador y acta. Sin afluentes, caudales, medidas ni geometría inventados; PR propia para revisión y sin merge.

## D03 — Climas y ecosistemas [FUSIONADA EN MAIN, PR #17]
- Clima del litoral Veldora, Valkram, transición fría norte, península Taramin y Syvaris; microclimas y suelos.
- Evitar falsa homogeneidad: costa atlántica, altura, sotavento, valle, corredor seco y protegido.
- **Salida D03 (15-10-2026):** 3 documentos climáticos/ecológicos, 12 unidades D01 trazadas, JSON de planificación NO RUNTIME, 30 invariantes, script de regresión, acta y traspaso D04; sin grados, lluvias, cumbres, especies o ríos nuevos.
- **Estado vigente:** validadores Python D01/D02/D03 superados por el autor en MSI checkout completo 15-10-2026; PR #17 fusionada squash 191bcd5. Godot/GIS siguen pendientes; NO RUNTIME.

## D04 — Recursos y economía territorial [DOCUMENTALMENTE CERRADA; PYTHON CI WINDOWS/LINUX OK; PR #20]
- Oro/plata/minas, fundición y ensayo, carbón importado de Azurios, madera de Pilares, agricultura, pesca/puertos y transportes.
- Revisar fiscalidad E8, moneda E2, transacciones Core, sin aduanas internas entre Grandes Casas.
- **Salida D04:** 4 documentos, 12 unidades, 8 cadenas, 19 fuentes y validador Python con 16 negativos; 22 controles JS remotos superados. **21-10-2026: Python D01–D04 STATIC OK tanto en Windows 2022 como Ubuntu 24.04 con checkout íntegro de GitHub Actions (run #39583142837).** No se ha ejecutado físicamente D04 en el MSI; esa repetición es opcional, no condición de cierre estático. Godot/GIS/CoreRPG runtime no ejecutados por D04. PR #20 sujeta a verificación de estado real para merge; no canon nuevo.

## D05 — Red de transporte, rutas y comunicaciones [PENDIENTE]
- Corredores existentes (Veldora–Treihord), transporte mineral/Belara, accesos a Taramin, cabotaje y Syvaris.
- Caminos, puentes, vados, barcazas, mercantes, barcos pesqueros, mensajería y tiempos derivados por terreno cuando exista escala.
- **Salida:** grafo modal básico, nodos y restricciones, sin kilómetros/itinerarios ficticios.

## D06 — Asentamientos ordinarios y generación procedural [PENDIENTE]
- Aldeas → pueblos → villas; enclaves mineros, pesqueros, forestales, agrícolas, isleños y servicios de ruta.
- Esqueleto obligatorio → posibilidades → condiciones → pesos regionales → modelos → instancias y seed.
- Diferenciar distribución espacial, servicios y límites logísticos de rangos Valrik.
- **Salida:** modelos Darovan verificables y datos no canónicos de prueba.

## D07 — Las ciudades canónicas [PENDIENTE]
- **Treihord:** extracción de referencias, necesidades operativas, validación con canon vigente **sin rediseñar**; cartografía técnica solo cuando proceda.
- **Veldora:** auditoría previa de su perfil aprobado y diseño manual puerto comercial/aduanas/almacenes y ciudad.
- **Taramin:** auditoría previa y diseño manual puerto pesquero, desembocadura bifurcada Thalen, abastecimiento.
- **Syvaris:** auditoría previa, bahía principal, calas, puerto y biomas internos diferenciados.
- Cada ciudad: fases de diseño individual con autorización del autor en decisiones de identidad, personajes o acontecimientos.
- **Salida:** matrices de anclas canónicas, sin reemplazar ciudades por generador.

## D08 — Hogares, población, servicios y profesiones [PENDIENTE]
- Integrar Core de población/relaciones/empleo/residencia, ley Norgard y perfil de demanda laboral.
- Cadenas de abastecimiento, cuidados, salud, educación, posadas, transporte y servicios locales.
- Cálculos cuantitativos solo después de aprobar rangos Darovan; sin trasplantar Valrik.
- **Salida:** cobertura de servicios, presupuesto lógico hogares–trabajo–inventarios.

## D09 — Gobierno, fiscalidad, defensa y seguridad [PENDIENTE]
- Delegaciones Casa/Corona, Justicia del Rey, guardias urbanas, guardia de Casa, custodia de minas, puertos y caravanas.
- Reutilizar Norgard E4, E5, E6, E8 y E9. No crear armada autónoma Darovan.
- Componentes políticos sensibles (señor, herederos, casas menores, historias) requieren autor.
- **Salida:** atribución de competencias y contratos de incidencia, seguridad/custodia.

## D10 — Cultura y sociedad local [PENDIENTE]
- Contraste de élites comerciales, trabajadores de minas, comunidades pesqueras, rutas e insularidad.
- Heredar Norgard (nombres, familia, ritos, cultura material, toponimia) sin inventar tradiciones universales.
- **Salida:** perfiles diferenciados de subregiones y variantes locales autorizadas.

## D11 — Integración técnica y pruebas [PENDIENTE]
- Datos con IDs persistentes y trazabilidad fuente; precedencia y versionado.
- Validar JSON/schema real, integridad de referencias, derivación de overrides y determinismo.
- Escenarios: ruta mina–Crisol, bloqueo de carbón, barcaza Belara, comercio exterior Veldora, pesca Taramin, travesía Syvaris, migración de hogares; todos **fixtures de prueba, no sucesos canónicos**.
- Pruebas de continuidad con Norgard/Core/Valrik, ausencia de duplicación y persistencia del world state.
- **Salida:** reporte de regresión estática; runtime SOLO cuando el motor esté integrado y ejecutado.

## D12 — Auditoría integral y cierre territorial [PENDIENTE]
- Comparar canon, perfil geográfico, pueblos, cuatro ciudades, rutas, economía, clima y contratos.
- Resolver por el autor los bloqueos de canon; consolidar referencias sin copias.
- Emitir ficha de versión, matriz aprobaciones y deuda real.
- **Salida:** propuesta de cierre a revisión humana; canon solo tras decisión de autor.

## Dependencias y política de desbloqueo
- **Autor:** solo decisiones sustantivas de historia/geografía/política/ciudades/NPC importantes. Es lícito continuar documentos independientes.
- **Terreno o mapa métrico:** cotas, distancias, tiempos y cuencas exactas siguen provisionales.
- **Core RPG:** la integración ejecutable no se presupone completada; contratos estáticos sí se pueden preparar ya.
- **Arven:** no asignar administración Darovan sin confirmación.
- **Belara (RESUELTO 15-10-2026):** por decisión explícita del autor prevalece el canon de GitHub; Belara pasa junto a Treihord, no por su casco urbano. «Eshneva» en el manuscrito es una discrepancia editorial pendiente de revisión del texto, **no** una dependencia de canon o de desarrollo.
- **PR:** revisión por autor, **nunca fusionar `main` sin permiso expreso**.

## Continuidad de conversaciones
Darovan 1: D00 **integrada en main** mediante PR #14. Darovan 2: D01 **fusionada por PR #15**. Darovan 3: D02 **fusionada en main por PR #16**. Darovan 4: D03 **FUSIONADA PR #17, Python MSI D01–D03 OK**, habiendo leído `00_Control_del_proyecto/TRASPASO_D03.md`. Darovan 5: D04 **documentalmente entregada a PR #20, Python CI Windows/Linux OK (21-10-2026)**. Darovan 6: D05 condicionada a merge D04 y TRASPASO_D05.md. Una fase por conversación. No presumir merge ni pruebas runtime. Actualizar `Estado` de cada fase con commit por incremento.

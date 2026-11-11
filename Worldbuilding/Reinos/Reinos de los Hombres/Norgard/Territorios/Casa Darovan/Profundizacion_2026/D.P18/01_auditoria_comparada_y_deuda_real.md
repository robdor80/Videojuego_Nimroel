# D.P18 — Auditoría de remate territorial de Casa Darovan frente a Casa Valrik/Treskal

**Fecha:** 11/11/2026 · **Alcance:** auditoría cruzada de D00–D12, D.P13 y nueva profundización D.P14–D.P18. **No es una certificación de mapa/vida urbana en runtime**.

## Resultado sustantivo

Darovan posee **diseño territorial documental profundo y validable**. El trabajo nuevo ha completado matrices de elegibilidad, redes condicionales de servicios, inventarios urbanos y contrato transversal de simulación futura. Se mantienen cuatro ciudades manuales y doce ámbitos físicos.

Sin embargo, **no está justificado declarar que Darovan tiene el mismo nivel local y urbano que Treskal**. La referencia de Valrik tiene 99 capítulos funcionales numerados del 01 al 99 (100 carpetas por duplicidad de 34); hay un proceso explícito de extracción de sus reglas comunes a Core/Norgard. D.P16 se ha basado en ese índice y en el mapa de extracción, pero **no convierte sus contenidos locales en historia, barrios o calles de Darovan**.

## Métricas de entregables efectivamente trazados

| Fase | Producto | Cantidad | Advertencia |
|---|---|---:|---|
| D.P14 | twelveStudyUnits | 12 | Matriz de ámbitos, no parcelas |
| D.P14 | eligibilityGates | 10 | Puertas que exigen evidencia local |
| D.P15 | settlementModels | 9 | Reutiliza modelos D06 y no los vuelve a generar |
| D.P15 | serviceNeeds | 10 | Servicios conceptuales, sin proveedores |
| D.P16 | manualCityPlans | 4 | Cuatro fichas urbanas, sin planos geométricos |
| D.P16 | treskalIndexedFolders | 100 | Inventario metodológico; número 34 duplicado en la referencia |
| D.P17 | globalNamespaceCandidates | 57 | Consultas futuras a Core/Norgard, sin integración ejecutada |
| D.P17 | testOnlyScenarios | 24 | Escenarios conceptuales, no pruebas físicas |

## Matriz de suficiencia temática

| Eje | Darovan D00–D.P18 | Valrik/Treskal como referencia | Dictamen |
|---|---|---|---|
| Geografía física | D01–D03 + D.P13, cotas autoradas y reglas de 12 ámbitos | clima de 10 capítulos y geografía local específica | Comparable en **reglas y profundidad conceptual**, no en mapa métrico |
| Economía y rutas | D04/D05, redes/suministro no confundidos con carreteras | puerto, madera, abastecimiento, red local y sectores T | Profundidad regional aceptable, rutas físicas pendientes |
| Asentamientos | D06 + D.P14/D.P15, nueve modelos y diez necesidades | aldeas/pueblos/villas con esqueleto, posibilidades, coherencia y generación | Contrato conceptual elaborado; **no crear instancias** |
| Cuatro ciudades | D07, D08/D09/D10 + D.P16 por ciudad | Treskal manual con 99 capas y T/S funcionales | **No equivalentes en detalle local y plano** |
| Psicología, relaciones, vida diaria | Núcleos globales Core/Norgard; consulta D.P17 | extraídos desde Treskal según mapa de extracción | Reutilizar sin copiar overrides Valrik |
| Persistencia y ejecución | D11 estructural + D.P17 `TEST_ONLY` | contratos Core y pruebas IA comparativas | No se acredita runtime territorial de Darovan |
| Gobierno/fiscalidad | D09 y normativa Norgard, Corona/guardias/aduanas | Norgard + Valrik, protocolo regio, fuerza Valrik | Compatible, sin transferir cuotas ni cuerpos Valrik |
| Autoría y metrología | D.P13, D.P18 y anclas D07/D08 | auditoría final de Treskal pre-plano métrico | Mantener UNKNOWN donde no hay canon o mapa |

## Deuda real clasificada por fuente de solución

| ID | Bloque abierto | Tipo | Causa y próximo paso |
|---|---|---|---|
| P18-G01 | Plano de huella de Veldora | `NEEDS_AUTHORIAL_URBAN_DESIGN_AND_CARTOGRAPHY` | Número/nombres de barrios, muelles concretos y traza no autorizados |
| P18-G02 | Plano de huella de Taramin | `NEEDS_AUTHORIAL_URBAN_DESIGN_AND_CARTOGRAPHY` | Ubicación zona pesquera principal y de cruces de los dos brazos del Thalen no decidida |
| P18-G03 | Plano de huella de Syvaris | `NEEDS_AUTHORIAL_URBAN_DESIGN_AND_CARTOGRAPHY` | Posición de instalaciones civiles/navales y sectores de la bahía no decidida |
| P18-G04 | Geometría detallada Treihord | `NEEDS_CARTOGRAPHY_WHILE_PRESERVING_CANON` | Ocho barrios canónicos y Belara no se mueven; faltan ejes/cartografía exacta |
| P18-G05 | Cartografía física de 12 unidades | `NEEDS_APPROVED_GEOMETRY` | Las bandas de D.P13 no crean DEM ni escala métrica |
| P18-G06 | Cauces y receptores menores | `NEEDS_BASIN_TOPOLOGY` | Fhalion y otras bocas precisas no localizadas; preservar red D02 |
| P18-G07 | Rutas materiales y tiempo de viaje | `NEEDS_TOPOLOGY_AND_GEOMETRY` | D05 acredita solo 3 vínculos de naturaleza diferente; sin todos los enlaces |
| P18-G08 | Censos y hogares exactos | `NEEDS_AUTHOR_OR_GAME_INSTANCE` | Rangos D08 no se transforman en recuento de proveedores o pobladores |
| P18-G09 | Instalaciones y proveedores concretos | `NEEDS_AUTHOR_OR_GAME_INSTANCE` | No asumir hospitales, escuelas, guardias o puestos por cada población |
| P18-G10 | NPC nominados y genealogías concretas | `NEEDS_AUTHOR_LORE_DECISION` | Core/Norgard permite NPC genéricos; personajes importantes requieren autoría |
| P18-G11 | Parámetros ambientales medidos | `NEEDS_EVIDENCE_OR_CALIBRATION` | No deducir mm lluvias, viento prevalente o permeabilidad exacta de altitudes |
| P18-G12 | Integración ejecutable en CoreRPG/Godot | `NEEDS_FUTURE_IMPLEMENTATION` | El contenido de esta rama no materializa sistema C++, GDExtension ni exportables |

**La distinción importa:** los vacíos G01–G03/G10 requieren decisiones de **identidad de lore o plano urbano** si se pretenden convertir en canon. No son permisos para inventarlos. Los vacíos de cartografía y runtime requieren fuente técnica y ejecución posterior, y el autor ya ha indicado que ese trabajo será futuro.

## Cuatro niveles de cierre

1. **Documentación territorial:** cobertura sustancial y matrices de compatibilidad creadas; ningún edificio ficticio.
2. **Contrato verificable:** archivos JSON + validador CI Windows/Linux para detección de cambios adversariales y regresiones; el resultado del HEAD deberá comprobarse.
3. **Canon local completo:** **no acreditado aún** para Veldora/Taramin/Syvaris: no existen barrios/tipologías singulares autorizados equivalentes al detalle de Treskal.
4. **Terreno y simulación ejecutable:** aplazados expresamente; no puede afirmarse cierre material por este pack.

## Resolución del conflicto «casa terminada»

Puede cerrarse **el paquete de profundización documental condicional** sin fingir que los perfiles de ciudad son planes urbanos cerrados. No debe comunicarse «Casa Darovan completamente equivalente a Treskal» ni «los cuatro municipios ya funcionan en juego».

Antes de elevar planes de Veldora, Taramin o Syvaris a canon local cerrado, se requerirá una decisión sobre su **estructura urbana autorada** (número/nombres de barrios y ubicación funcional real), a tratar con el usuario. Mientras tanto no se bloquea la validez de las matrices y contratos entregados.

## Pruebas

Se ha incluido validación estática de contrato y mutaciones adversariales; **los resultados reales de GitHub Actions han de verificarse en el HEAD de la PR antes de afirmar SUCCESS**. Se mantienen todas las pruebas existentes D01–D12 y D.P13.

**Registro JSON:** `../Datos operativos/darovan_dp18_territorial_closure_audit_v0.1.json`.

## Ampliación de auditoría funcional — triado 99 capas y cadenas propias

El registro `Datos operativos/darovan_dp16_valrik_functional_coverage_v0.1.json` contrasta **100 carpetas reales 01–99** de Treskal (doble 34) y las agrupa por nivel de responsabilidad **de modo provisional**, sin suponer que todos esos archivos hayan sido revisados línea a línea o que los módulos Core estén probados en el host. Incorpora **13 cadenas funcionales propias de Treihord/Veldora/Taramin/Syvaris/Arven**, con pruebas de legitimidad y prohibición de rutas o instalaciones ficticias.

Este triado completa el **índice de trabajo**, pero **no resuelve** los bloques de urbanismo canónico G01–G03 ni la cartografía G04–G07. Las decisiones personales y de topónimos siguen reservadas al autor.

# DAROVAN D03 — Clima, ciclo hídrico, riesgos e interfaz D04 v0.1

**Documentación causal, NO RUNTIME.** Las flechas son dependencias físicas, no resultados de simulación ni mapas de peligro.

## Modelo causal
- **Relieve, latitud, costa, cubierta** + **UNKNOWN atmósfera** (lluvia, temperatura, viento, calendarios) → disponibilidad de precipitación/nieve y evapotranspiración.
- **Precipitación y nieve/deshielo** + **suelo UNKNOWN** (permeabilidad, saturación, almacenamiento) → infiltración, recarga potencial y escorrentía.
- **Escorrentía** + **pendientes/divisorias UNKNOWN** → red topológica D02, sin canales menores materializados.
- **Recarga/almacenamiento** + **aportes** + **demanda** → disponibilidad estacional y posibles estados del agua, únicamente cuando haya datos suficientes.
- **Estados del agua, vegetación y suelo** + exposición → restricciones y riesgos por comprobar en D04–D11.

El clima NO localiza cauces por sí mismo. No declarar permanentes los ríos por estar nombrados ni suponer que llevan el mismo caudal en cada estación.

## Aplicaciones a ambientes
| Área | Entrada AUTHORED | Pregunta que queda abierta |
|---|---|---|
| Taramin norte/centro | Clima semiárido, suelo pedregoso, barrancos estacionales como categoría | ¿Cuánto escurrimiento/infiltración y en qué época? No clasificar Thalen como estacional |
| Taramin sur | Más humedad, Bosque Taramin con gradiente | ¿La cubierta retiene agua o hay recarga medible? No asegurar pozos/cosechas |
| Valkram y Elyra | Montañas, Belara con fuente al oeste/norte de Valkram | ¿Nieva? ¿dónde y cuándo deshiela? Cotización meteorológica desconocida |
| Norte frío | Transición fría/boreal | ¿Hay hielo o cierre de rutas locales? Sin extrapolar heladas documentadas de Zanthir |
| Veldora y Agujas | Océano/golfo, bosque Agujas con Lhera a un lado | ¿Qué variación real de humedad/suelos hay? Lhera y río Veldora NO confluyen por compartir golfo |
| Pilares | Claros y extracción maderera para minas | ¿Influye la cubierta alterada sobre sedimentos y suelo? Impactos no acreditados |
| Syvaris | Isla cálida, parcialmente seca, refugios verdes | ¿Existen reservas de agua dulce? No afirmar acuíferos ni arroyos |
| Arven | Bosque e isla ante golfo | Administración no aprobada: solo contexto físico |

## Matriz de riesgos POTENCIALES; no ocurrencias ni zonas peligrosas establecidas
| Candidato | Verificación necesaria | Etapa receptora |
|---|---|---|
| Erosión en ladera o barranco pedregoso | lluvia, pendiente, litología y cubierta | D04 producción de suelo; D05 rutas |
| Inundación en márgenes Belara/Lhera | secciones y niveles de agua, topografía, datos temporales | D05/D07 |
| Inundación junto a ambos brazos terminales del Thalen | hidráulica de los dos brazos y cotas de Taramin | D07/D11 |
| Sedimentación por uso forestal Pilares | inventario de corta, erosión y aportes | D04/D11 |
| Nieve/hielo sector alto o septentrional | estación/temperatura/cota reales | D05/D11 |
| Estrés de abastecimiento | balance agua-demanda, almacenamiento y usos | D04/D08 |
| Exposición litoral Veldora/Syvaris | viento, oleaje, materiales y cotas | D05/D07 |

**No se atribuyen amenazas, frecuencias ni daños** a ciudades, caminos o explotaciones existentes. Riesgo candidato ≠ evento canónico.

## Integridad D01/D02 y Core
1. Belara junto a Treihord, nunca por su casco; Lhera derivado del Belara; Veldora independiente; Taramin entre dos brazos del único Thalen.
2. Permanencia de los cuatro ríos principales: UNKNOWN; no infiera origen Veldora/Thalen o bifurcación Belara respecto de Treihord.
3. No crear afluentes, surgencias, humedales, caudales, rutas, puentes o parcelas inundadas desde gradientes cualitativos.
4. La geometría e identidad materializadas persistirán; World State podrá alterar estado del agua sin reescribir las redes.
5. Ciudades manuales Treihord, Veldora, Taramin, Syvaris; Karsath excluida, Arven administrativa UNKNOWN, sin poblados interiores Agujas.

## Salida D04 — preguntas condicionantes para recursos y producción
- **Minería:** oro/plata en Valkram/Elyra; no inventar yacimientos locales ni productividades. Carbón de los Azurios para Treihord según canon industrial.
- **Silvicultura:** madera del bosque Pilares para minas; aprovechar cobertura, regeneración y suelos sin fijar tasa. Linde no maderero relevante, Agujas salvaje sin poblados; Taramin usos locales y Syvaris poca explotación.
- **Agricultura:** no asignar cultivos ni rendimientos por temperatura cualitativa; precisar agua, calidad/espesor del suelo, estación y demanda.
- **Puertos/pesca:** enlazar navegación civil Norgard Defaults E7, disponibilidad de agua, seguridad marítima y estacionalidad cuando existan datos; no inventar caladeros.
- **Transporte fluvial:** Belara permite barcazas poco profundas en Treihord; no deducir navegabilidad anual sin hidroclimatología.
- **Fiscalidad y comercio:** mantener Norgard Defaults E2, E7, E8; clima no cambia competencias ni habilita aduanas internas.

**Bloqueos de cuantificación (no de cierre documental):** datos atmosféricos y calendario, DEM/cartografía, suelo/hidrogeología, mar y oleaje, demandas por localidad. Se transfieren a D04/D05/D07/D11, no se resuelven ficticiamente.

**Fuentes:** Norgard/Clima/clima_general.md; Geografía/{geografia_general,regiones_naturales,montanas,bosques,rios_y_lagos,mares_y_costas}.md; Nimroel Core/Geografia fisica/geografia_fisica_drenaje_hidrografia_v0.1.md y contrato JSON; Darovan D01/D02.

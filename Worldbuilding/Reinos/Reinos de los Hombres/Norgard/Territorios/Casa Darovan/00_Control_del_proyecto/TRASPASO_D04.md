# Darovan 5 — Traspaso a D04 (Recursos y producción)

**TRASPASO D03 → D04 EJECUTADO.** D03 fusionada PR #17 (squash 191bcd5); D04 creada desde main df43be5 y publicada en PR #20. D01–D03 Python superados en MSI sobre checkout completo. Los apartados siguientes son instrucciones históricas de entrada a D04, no tareas pendientes; continuar por TRASPASO_D05.md.

## Puerta de entrada
1. Verificar en GitHub D03 merged=true y HEAD main; leer registro de fases, decisiones/bloqueos, protocolo PR y acta D03.
2. Leer originales de Norgard: geografía, montañas, bosques, clima, hidrografía, costa; canon de Treihord y perfiles visuales de cuatro ciudades.
3. Leer los tres documentos D03 en Clima_local, JSON D03, matriz/validador, D01 relieve JSON, D02 hidro JSON, Core físico y Defaults relevantes (E2, E7, E8).
4. Crear rama propia feat/darovan-d04-recursos-produccion desde main, commits y PR D04 independiente, SIN merge automático. Una fase por conversación.

## Recepción cualitativa vinculante para trabajo (no canon nuevo)
- **Minería y Crisol:** oro/plata en Valkram y Elyra; Treihord aprovecha cadena minera y puerto industrial fluvial. Carbón industrial de Azurios según canon, no ubicar carbón inventado en Valkram. No asignar cantidades, reservas, minas concretas nuevas, rendimientos ni propietarios no documentados.
- **Madera:** Bosque de los Pilares abastece minería, sistema único con claros; estudio de extracción/regeneración/estabilidad. Agujas antiguo sin poblados permanentes; Linde sin explotación relevante; Taramin bosque único con aprovechamiento local; Syvaris pequeños bosques sin intensidad industrial.
- **Agricultura, ganadería y agua:** norte/centro Taramin semiárido no desértico; sur forestal más húmedo; Syvaris parcialmente seca, calas verdes. No convertir paisaje en rendimiento agrícola o disponibilidad de pozo sin datos de suelo, recarga, estación y demanda.
- **Pesca y puertos:** Taramin, Veldora y Syvaris son ciudades manuales; utilizar Norgard Defaults E7 y contrato Core acuático. No inventar bancos de pesca, cuotas o temporales meteorológicos.
- **Flujo Belara–Lhera / Veldora / Thalen:** conservar topología exacta D02. Treihord junto a Belara (no atravesada), barcazas someras; Lhera nace del Belara; río Veldora independiente; Taramin entre dos brazos terminales del mismo Thalen. El tipo de cauces estacionales de Taramin NO autoriza calificar al Thalen como estacional.

## Recursos que D04 puede diseñar sin crear canon
Esquemas cualitativos de cadenas de extracción-transformación-consumo-almacenamiento-transporte; restricciones de cobertura, humedad, suelo, seguridad hídrica y riesgos hipotéticos; IDs de referencia, fuentes, dependencias y validaciones estáticas. No diseñar a ciegas el detalle de parcelas, explotaciones, cultivos o negocios con nombre.

## Decisiones y dependencias abiertas
- **DAR-P01:** Arven sin adscripción; ninguna producción se declara tributaria de Darovan por estar enfrente de Veldora.
- **DAR-P04:** fronteras, cotas, escala, suelos, parcelas y altimetría desconocidas.
- **DAR-P07:** identidad del cauce en ficha visual detrás de Veldora UNKNOWN.
- **DAR-P08:** ubicación bifurcación Belara/Lhera respecto de Treihord; cabeceras de Veldora/Thalen; caudales, divisorias, régimen y trazados UNKNOWN.
- **DAR-P09 (D03):** parámetros por región de precipitación, nieve, estación, viento, suelo y capacidad de recarga, así como riesgos verificables, pendientes de documentación/aprobación. No bloquear economía descriptiva por falta de cifras.
- Dependencias D05 transporte, D07 ciudades y D11 runtime; conservar identidad/geometría una vez materializadas.
- Test reproducible Python D01/D02/D03 **SUPERADO — MSI 15-10-2026** sobre checkout completo; pruebas numéricas de terreno **PENDIENTE — GODOT/MSI/GIS**.

**Se respeta Core → Norgard Defaults → Casa Darovan → Localidad → World State. No elevar inferencias a canon sin el autor. D04 autorizada y ejecutada documentalmente en Darovan 5; PR #20 no fusionada. D05 NO iniciada.**

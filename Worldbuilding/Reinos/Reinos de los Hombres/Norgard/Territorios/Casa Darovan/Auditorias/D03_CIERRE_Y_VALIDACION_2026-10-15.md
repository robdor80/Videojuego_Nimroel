# DAROVAN D03 — Acta de cierre documental y auditoría (15-10-2026)

**Estado:** DOCUMENTALMENTE CERRADA — rama feat/darovan-d03-clima-ecosistemas; PR hacia main para revisión del autor, **SIN FUSIONAR**. No eleva hipótesis a canon, no crea parámetros climáticos de ejecución ni activa Nimroel Core/Godot.

## Base GitHub verificada antes de comenzar
- D00 PR #14 y D01 PR #15 integradas.
- D02 PR #16 comprobada **merged=true**; su commit de fusión **34c9652eba2bd0fed33ab6a3931f24400a39b812** era exactamente HEAD de main al crear la rama D03.
- Rama D03 creada desde ese SHA, sin modificar main. La PR permanece sometida a revisión y merge exclusivamente por el autor.

## Investigación de canon realizada
Leídos originales Norgard: Clima/clima_general.md; Geografía/geografia_general.md, regiones_naturales.md, montanas.md, bosques.md, rios_y_lagos.md, mares_y_costas.md; perfil visual norgard_regions_v0.1.json. Consultados registros, traspaso, plan y auditoría Darovan; D01 relieve y D02 hidrografía (documentos y JSON). Leídos contrato físico de Core en MD y JSON y README Norgard Defaults. No se ha inferido contenido del canon a partir de resúmenes conversacionales.

## Entregables D03
1. Clima_local/01_gradientes_climaticos_regionales_v0.1.md — gradientes y fuentes de cada zona.
2. Clima_local/02_ecosistemas_suelos_y_microclimas_v0.1.md — vegetación local, suelos conocidos/desconocidos, microclimas condicionales.
3. Clima_local/03_clima_agua_riesgos_y_d04_v0.1.md — ciclo hidrológico, riesgos hipotéticos, interfaz para recursos y producción.
4. Datos operativos/darovan_d03_climate_ecosystems_v0.1.json — **12 unidades de estudio D01**, 13 referencias de fuentes, protección del grafo D02 y campos no medidos NULOS. Estado **planning_reference_not_runtime**.
5. Validacion/D03_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md — **30 invariantes** canónicas y técnicas.
6. Validacion/validate_d03.py — script para ejecución local con pruebas de consistencia D01/D02/Core y **10 fixtures negativos**.
7. 00_Control_del_proyecto/TRASPASO_D04.md — puerta de entrada, dependencias y decisiones pendientes; **NO inicia D04**.
8. Registro de fases, decisiones/bloqueos, plan, READMEs e índices sincronizados.

## Evidencia de verificaciones REALMENTE ejecutadas
**JavaScript mediante conector GitHub, NO Python:** 
- Lectura de JSON final desde la rama y parseo correcto.
- **16 grupos de comprobaciones positivas** sobre JSON realmente publicado: autoridad, estructura de 12 IDs, nulos climáticos, fuentes, indicadores anti-canon, ciudades, Arven, Agujas, bosques, cuatro ríos, conexiones, Thalen, límites de datos y no-runtime.
- **10 mutaciones negativas** sobre copias del JSON publicado, todas correctamente rechazadas: administración falsa de Arven, Belara cruzando Treihord, Lhera sin Belara, Veldora conectada, Thalen sin ambos brazos, temperatura inventada, especies inventadas, bosque Taramin fragmentado, poblados Agujas y permanencia fluvial fingida.
- **9 contrastes adicionales** con JSON D01, D02 y contrato Core leído de la rama: OK; conjuntos de unidades y ríos coherentes, sin adscripciones no justificadas.
- **13 referencias sourceRefs** recuperadas efectivamente desde GitHub: 13/13 localizadas.
- Comparación base 34c9652... frente a rama: antes del acta, **15 commits, 14 archivos, 0 fuera de Casa Darovan**, rama adelantada y sin commits detrás; después del acta, comprobar nuevamente los totales.
- Ninguna fuente original de Norgard, Core, Treihord u otra Casa modificada.

**No ejecutado:** validate_d01.py, validate_d02.py ni validate_d03.py dentro de checkout completo; ningún pipeline GitHub Actions acreditado; ningún entorno Godot, generador de relieve, GIS, meteorología, navegación, prueba de persistencia ni cálculo de escorrentía usado. La validación JavaScript no suple estos pasos.

## Pendientes, diferenciando naturaleza
| Estado | Necesidad | ¿Bloquea cierre documental? |
|---|---|---|
| **PENDIENTE — MSI** | Ejecutar Python validate_d01.py, validate_d02.py, validate_d03.py desde copia íntegra del repositorio | No; antes de declarar validación local completa |
| **PENDIENTE — MSI / GIS** | Altimetría, topografía, mapas y suelos verificados; exposición de laderas y drenaje regional | No; sí para modelización espacial |
| **PENDIENTE — GODOT** | Integración física, estaciones, agua dinámica, eventos, persistencia y juego en funcionamiento | No; sí para certificar runtime D11 |
| **PENDIENTE AUTOR** | DAR-P01 Arven, DAR-P04 cartografía, DAR-P07 río visual, DAR-P08 red fluvial detallada, DAR-P09 climatología/suelos | No para entrega cualitativa; sí donde afecte a canon o materialización |
| **NO IMPLEMENTADO** | Mapas de bioma, especies/temperaturas/cotas/caudales/estaciones con números | Deliberadamente fuera de D03 |

## Líneas rojas conservadas
Belara junto a Treihord, nunca atravesada; Lhera bifurca desde Belara; Veldora independiente; Thalen único con dos brazos finales y Taramin entre ambos; cuatro ciudades canónicas; Karsath fuera; Arven sin dueño confirmado; Agujas sin poblados; Bosques Pilares/Taramin como masas únicas; Syvaris forestación dispersa y clima no homogéneo. Riesgo potencial no equivale a riesgo existente ni suceso ocurrido.

**Conclusión:** D03 se entrega como **paquete documental cualitativo sometido a revisión autoral**, sin falsa precisión ni nuevas afirmaciones canónicas. El autor decide si fusiona la PR. D04 no iniciada.

# Territorio de Casa Darovan — índice de desarrollo
**Estado:** D00–D02 integradas en main (PR #14, #15 y #16). D03 cerrada documentalmente, PR propia para revisión, **SIN FUSIONAR**. La documentación D01 es NO CANÓNICA y no activa el motor. La documentación de trabajo **NO eleva a canon**.
**Sede administrativa:** Treihord. **Ámbito:** occidente de Norgard, incluida la isla de Syvaris.

## Fuentes de autoridad (no duplicarlas)
- [Treihord canónica](../../Ciudades/Casa%20Darovan/Treihord.md): **CANON — DISEÑO BASE CERRADO**. El diseño urbano permanece en su fichero original.
- [Grandes Casas](../../Grandes%20Casas/grandes_casas.md): pertenencia de Treihord, Veldora, Taramin y Syvaris a Darovan.
- [Geografía general de Norgard](../../Geografía/geografia_general.md), [ríos](../../Geografía/rios_y_lagos.md), [mares e islas](../../Geografía/mares_y_costas.md), [montañas](../../Geografía/montanas.md), [bosques](../../Geografía/bosques.md), [regiones naturales](../../Geografía/regiones_naturales.md) y [clima](../../Clima/clima_general.md).
- [Nimroel Core](../../../../../Sistemas/Nimroel%20Core/README.md) y [Norgard Defaults](../../../../../Sistemas/Norgard%20Defaults/README.md).
- [Referencia metodológica Valrik](../Casa%20Valrik/): reutilizar procedimiento, no trasladar parámetros locales.

## Jerarquía obligatoria
`Nimroel Core → Norgard Defaults → Casa Darovan → Localidad → World State`.
La Casa **no sustituye** contratos activos de rango superior. Un override requiere ámbito, justificación y compatibilidad comprobada.

## Archivos de Darovan 1
1. [Auditoría de canon y reutilización](Auditorias/2026-10-15_auditoria_canon_reutilizacion_v0.1.md).
2. [Inventario geográfico y cartográfico](Geografia_local/00_inventario_y_lectura_del_mapa_v0.1.md).
3. [Hoja de ruta](PLAN_DESARROLLO_DAROVAN_v0.1.md).
4. [Metodología de asentamientos](Asentamientos/METODOLOGIA_ASENTAMIENTOS_DAROVAN_v0.1.md).
5. [Manifiesto de referencias — NO runtime](Datos%20operativos/darovan_bootstrap_manifest_v0.1.json).

## Separación de contenidos
- **Ciudades canónicas:** Treihord, Veldora, Taramin y Syvaris: diseño deliberado/manual. La fuente aprobada de Treihord **no se mueve ni modifica**.
- **Asentamientos ordinarios:** aldeas, pueblos, villas, puestos e instalaciones: arquetipos/instancias con restricciones y semillas, sujeto a compatibilidad regional.
- **Subámbitos de diseño, sin atribuir nuevos límites administrativos:** litoral Veldora/Arven, cuenca Belara, Valkram/Elyra, península Taramin, isla Syvaris, norte frío.
- **Registro de incertidumbres:** toda interpretación cartográfica o pendiente de autor se marca. Ningún documento de esta etapa crea topónimos, NPC importantes, cifras de población o fronteras nuevos.

## Reanudación y fase siguiente
D03 se inició tras comprobar merge PR #16 y leer **00_Control_del_proyecto/TRASPASO_D03.md**. Para D04, exigir merge de PR D03 y leer **00_Control_del_proyecto/TRASPASO_D04.md**. Consultar las fuentes originales y el manifiesto, no asumir que la PR equivale a ejecución runtime. Una fase por conversación y rama; prohibido fusionar sin autorización.

## Organización establecida en D00 (15-10-2026)
- [`00_Control_del_proyecto/`](00_Control_del_proyecto/README.md): registro de fases, protocolo PR/commits, decisiones y traspaso D01.
- [`Auditorias/`](Auditorias/D00_CIERRE_Y_VALIDACION_2026-10-15.md): cierre D00, matriz de fuentes y auditoría original.
- [`Geografia_local/`](Geografia_local/README.md), [`Hidrografia/`](Hidrografia/README.md), [`Clima_local/`](Clima_local/README.md), [`Cartografia/`](Cartografia/README.md): medio físico y documentación del mapa.
- [`Recursos_y_produccion/`](Recursos_y_produccion/README.md), [`Rutas_y_comunicaciones/`](Rutas_y_comunicaciones/README.md), [`Economia_y_abastecimiento/`](Economia_y_abastecimiento/README.md): producción, transporte y economía.
- [`Asentamientos/`](Asentamientos/README.md): aldeas, pueblos, villas e instancias, no ciudades canónicas.
- [`Ciudades/`](Ciudades/README.md): Treihord, Veldora, Taramin y Syvaris, todas de diseño manual.
- [`Poblacion_y_hogares/`](Poblacion_y_hogares/README.md), [`Servicios_e_infraestructuras/`](Servicios_e_infraestructuras/README.md), [`Administracion_y_fiscalidad/`](Administracion_y_fiscalidad/README.md), [`Seguridad_y_defensa/`](Seguridad_y_defensa/README.md), [`Cultura_y_sociedad/`](Cultura_y_sociedad/README.md): capas sociales e institucionales.
- [`Contratos_y_runtime/`](Contratos_y_runtime/README.md), [`Datos operativos/`](Datos%20operativos/README.md), [`Validacion/`](Validacion/README.md): integración futura y verificación.

La presencia de una carpeta **no** significa que su fase haya empezado o finalizado. Ningún dato de D01–D12 se declara implementado con esta estructura.

## Darovan 2 — D01, entrega documental (PR #15)
- [Marco físico y orografía](Geografia_local/01_marco_fisico_y_orografia_v0.1.md).
- [Unidades naturales y corredores cualitativos](Geografia_local/02_subzonas_y_corredores_cualitativos_v0.1.md).
- [Perfil operativo de relieve](Geografia_local/03_perfil_operativo_del_relieve_v0.1.md).
- [Dependencias cartográficas](Cartografia/01_dependencias_cartograficas_D01_v0.1.md).
- [Perfil JSON de planificación NO runtime](Datos%20operativos/darovan_d01_relief_profile_v0.1.json).
- [Validación estática D01](Validacion/D01_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md) y [acta de cierre](Auditorias/D01_CIERRE_Y_VALIDACION_2026-10-15.md).
- [Traspaso D02](00_Control_del_proyecto/TRASPASO_D02.md), condicionado al merge autorizado de PR #15.

## Darovan 3 — D02: documentación y grafo no-runtime (PR #16 fusionada)
- [Red y grafo](Hidrografia/01_red_hidrografica_y_grafo_v0.1.md), [cuencas y reglas](Hidrografia/02_cuencas_divisorias_y_reglas_v0.1.md), [dependencias](Hidrografia/03_interacciones_territoriales_y_traspaso_v0.1.md).
- [JSON D02](Datos%20operativos/darovan_d02_hydro_network_v0.1.json), [matriz](Validacion/D02_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md), [validador Python](Validacion/validate_d02.py), [acta](Auditorias/D02_CIERRE_Y_VALIDACION_2026-10-15.md) y [traspaso D03](00_Control_del_proyecto/TRASPASO_D03.md).
- **No** hay ríos menores inventados, cuencas métricas, caudales, nuevos asentamientos, geometría ni validación del motor. D03 documentada después de la fusión de D02, sin canon nuevo.

## Darovan 4 — D03: clima y ecosistemas (PR para revisión, SIN MERGE)
- [Gradientes](Clima_local/01_gradientes_climaticos_regionales_v0.1.md), [ecosistemas](Clima_local/02_ecosistemas_suelos_y_microclimas_v0.1.md) y [agua y riesgos](Clima_local/03_clima_agua_riesgos_y_d04_v0.1.md).
- [Perfil JSON NO RUNTIME](Datos%20operativos/darovan_d03_climate_ecosystems_v0.1.json), [matriz D03](Validacion/D03_MATRIZ_INVARIANTES_Y_PRUEBAS_v0.1.md), [validador](Validacion/validate_d03.py), [acta](Auditorias/D03_CIERRE_Y_VALIDACION_2026-10-15.md) y [TRASPASO D04](00_Control_del_proyecto/TRASPASO_D04.md).
- D03 no crea temperaturas, precipitaciones, especies, cauces, límites ni biomas jugables. D04 no iniciada.

## D04 — estado 15-10-2026
D01–D03 integradas en main y Python MSI superado. D04: rama `feat/darovan-d04-recursos-produccion`, PR #20 para revisión (no fusionar automáticamente), sin canon nuevo ni runtime. Ver `Recursos_y_produccion/`, `Economia_y_abastecimiento/`, acta D04 y TRASPASO_D05.md.

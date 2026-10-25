# Darovan D.P13 — temperaturas, estaciones y heladas

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Fundamentos, sin trasplantar Valrik

La temperatura depende de época, masa de aire, latitud relativa, influencia oceánica, altitud real, orientación, sombra y situación atmosférica. Una región fría no determina que todos sus puntos estén helados y una isla cálida no está completamente exenta de episodios anómalos. No se transfieren regímenes de Montes Invernos ni temperaturas diarias de Treskal.

## Matriz de las doce unidades — respuesta térmica territorial

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | enfriamiento relativo condicionado por altura, sombra y orientación |
| `d01_elyra_paso_peninsular` | altitud reduce temperatura relativa, península introduce contraste costa/interior |
| `d01_norte_transicion` | más frío relativo al sur, con heterogeneidad local por altitud y mar |
| `d01_aguja_litoral` | influencia marina y transición fría local actúan como moduladores, sin magnitudes |
| `d01_belara_treihord` | interior occidental con modulaciones de valle, viento y cercanía al agua |
| `d01_veldora_litoral` | amortiguación oceánica relativa, sin temperatura específica |
| `d01_linde_caminos` | microcontraste día/noche bajo cubierta frente a despejado |
| `d01_pilares_sur` | gradiente dosel-claro y pie de monte-ladera |
| `d01_taramin_norte_centro` | mayor oscilación potencial en sectores interiores expuestos, sin cifras |
| `d01_taramin_bosque_sur` | mayor humedad sur según canon; temperatura regulada por bosque y mar |
| `d01_syvaris` | rasgos semitropicales, contrastes de sombra y exposición insular |
| `d01_arven_contexto` | influencia marítima posible, diferencia con Syvaris no cuantificada |

## Estacionalidad por contexto

| Contexto | Primavera | Verano | Otoño | Invierno |
|---|---|---|---|---|
| Norte frío | Deshielo posible donde hubo acumulación | Mayor agua líquida sin garantía de calor | Enfriamiento y heladas de transición | Mayor probabilidad relativa de hielo/nieve |
| Valkram / Elyra | Contraste cota-sombra y fusión condicionada | Frescor relativo en alturas reales | Heladas tempranas posibles en altura | Retención nival donde el episodio y la cota lo permitan |
| Veldora / Golfo | Moderación oceánica, variabilidad | Amortiguación de extremos relativa | El mar puede moderar el enfriamiento | Humedad y temperaturas moduladas, sin nieve fijada |
| Belara/Treihord y La Linde | Cambio entre zonas abiertas/sombra | Contrastes por dosel y distancia al mar | Secado más lento bajo cubierta | Posibles inversiones si existe valle estable |
| Pilares | Respuesta combinada pie de monte/cubierta | Menos calentamiento bajo dosel cerrado | Persistencia de humedad tras lluvias | Nieve local condicionada al relieve |
| Taramin norte-centro | Alternancia entre húmedo excepcional y seco | Mayor secado potencial en terreno expuesto | Rehumectación solo tras aporte | Frío de episodio, sin nieve habitual impuesta |
| Taramin bosque sur | Transición húmeda modulada por cubierta | Microclima forestal de sombra | Suelo húmedo condiciona enfriamiento | No copiar régimen nival del norte |
| Syvaris | Cambios suaves relativos sin cifras | Sectores abiertos vs protegidos | Influencia marítima y humedad variable | Isla de rasgo cálido, sin atribuir heladas ordinarias |
| Arven | Bosque puede retrasar secado | Amortiguación bajo dosel | Persistencia de humedad si llueve | Temperaturas exactas y nieve desconocidas |

## Regla de helada y sensación térmica

Una helada requiere evento suficientemente frío, enfriamiento del suelo y situación local; las vaguadas estables pueden retener aire frío, las crestas expuestas más viento y el dosel puede amortiguar extremos. La sensación humana añade humedad y viento sin redefinir la temperatura. Fechas, umbrales, duración y altitudes de cuajado están `UNKNOWN`.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/montanas.md), [ríos](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/rios_y_lagos.md), [bosques](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/bosques.md), [clima](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Clima/clima_general.md), [regiones](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/regiones_naturales.md); D01/D02/D03 y [auditoría D12](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

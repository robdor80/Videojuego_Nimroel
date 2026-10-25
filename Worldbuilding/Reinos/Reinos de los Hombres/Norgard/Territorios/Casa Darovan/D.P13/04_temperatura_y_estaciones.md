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

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## DAR-DP13-HILLS-01 — Colinas del norte y centro de Taramin (25/10/2026)

**AUTOR APROBÓ OPCIÓN B:** las colinas **del norte y centro de la península de Taramin, fuera de Elyra**, tienen **elevaciones características aproximadas de 300–600 m s. n. m.** Es rango de las **colinas del sector**, NO una altitud uniforme de toda la zona, un máximo de la península o una cifra válida para las Montañas Elyra.

No modifica la altura del núcleo de Taramin (**0–40 m**), ni la referencia alta de Elyra (hasta **~2.600 m**); sigue el canon de colinas ocres y transición semiárida, Thalen de dos brazos terminales y Bosque de Taramin meridional. No define cotas individuales, barrancos específicos, ríos, rutas, localidades, precipitaciones ni terreno ejecutable.

**Trazabilidad:** `D.P13/20_colinas_norte_centro_taramin_autorizadas.md` y `Datos operativos/darovan_dp13_taramin_north_central_hills_authorial_v0.1.json`. Sin modificar D01–D12 ni iniciar D.P14–D.P18.


## DAR-DP13-FOOTHILLS-01 — Piedemonte occidental de Valkram (25/10/2026)

**APROBACIÓN DEL AUTOR, opción B:** las **elevaciones características de las estribaciones occidentales de los Montes Valkram** se sitúan aproximadamente entre **400 y 900 m s. n. m.** No es un rango uniforme para cada ladera, valle, aldea, ni la cota máxima de la cordillera. Mantiene las cumbres (3.600–4.200 m), **la Viuda (~4.200 m)**, los pasos naturales principales (1.400–2.200 m) y la altura urbana general de **Treihord (150–350 m)** como referencias distintas.

No modifica el curso del **Belara**, que pasa junto a Treihord sin atravesarlo. La unidad `d01_valkram_oeste` sigue siendo un ámbito cualitativo y no una frontera política. No se atribuyen pendientes medidas, bosque altitudinal concreto, nuevos ríos, caminos, pasos, núcleos ni terreno generado.

Documentación: `D.P13/21_piedemonte_occidental_valkram_autorizado.md`. Contrato: `Datos operativos/darovan_dp13_valkram_west_foothills_authorial_v0.1.json`. D.P18 queda pendiente.


## Elecciones restantes de D.P13 cerradas

Ver `D.P13/22_cierre_delegado_preguntas_y_opciones.md` y su contrato JSON; las bandas altitudinales y reglas son **diseño delegado**, sin sustituir mediciones ni datos espaciales. El capítulo conserva sus premisas e incertidumbres.

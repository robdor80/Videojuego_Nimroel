# Darovan D.P13 — relieve, exposición y microrelieve

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Estratos de relieve

1. **Macrorelieve AUTHORED:** cordilleras Valkram/Elyra, franja litoral y relieve peninsular/insular de las fuentes superiores. No añadir montañas nominadas.
2. **Relieve intermedio DERIVED_CONDITIONAL:** laderas, fondos, interfluvios, collados y piedemontes pueden nacer donde un modelo de alturas los justifique, sin declarar su existencia individual.
3. **Microrelieve GENERATED futura:** vaguadas, terrazas, pequeñas depresiones, barrancos y pendientes requieren continuidad topológica, pendientes compatibles, identidad estable y receptores.
4. **Limitadores:** una terraza fluvial requiere historia/relación con cauce y cotas, un humedal necesita convergencia y drenaje lento, un collado no habilita por sí mismo ruta ni conexión entre cuencas, y un acantilado no equivale a puerto.

## Matriz de las doce unidades — familias plausibles de microrelieve

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | crestas, interfluvios, laderas, fondos montanos y piedemonte si lo confirma el relieve |
| `d01_elyra_paso_peninsular` | crestas, lomos, collados candidatos, laderas y valles de salida |
| `d01_norte_transicion` | lomas, valles fríos, depresiones y afloramientos según terreno futuro |
| `d01_aguja_litoral` | laderas arboladas, vaguadas, borde de acantilado y franjas costeras solo donde haya soporte |
| `d01_belara_treihord` | ribera, lomas y depósitos fluviales como clases candidatas, sin terrazas concretas declaradas |
| `d01_veldora_litoral` | franjas litorales, lomas interiores, pequeñas vaguadas solo con terreno acreditado |
| `d01_linde_caminos` | borde forestal, claros y ondulaciones; ningún cauce ni cruce existente añadido |
| `d01_pilares_sur` | colinas, claros, vaguadas, laderas y pies de monte plausibles |
| `d01_taramin_norte_centro` | lomas, roquedos, vaguadas y barrancos de drenaje episódico |
| `d01_taramin_bosque_sur` | lomas, valles y pies de monte donde los sustente la geometría |
| `d01_syvaris` | lomas secas, roquedos, calas resguardadas y taludes litorales existentes como clases |
| `d01_arven_contexto` | colinas/vaguadas y litoral interior si relieve lo respalda; no imponer forma métrica |

## Matriz de las doce unidades — restricciones de orientación y divisorias

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | Contraste cresta-ladera y desagüe descendente; no extender divisoria al límite político |
| `d01_elyra_paso_peninsular` | Orientación montañosa afecta exposición; ningún paso se convierte en corredor autorizado |
| `d01_norte_transicion` | Sin límite latitudinal fijo; una zona climática no equivale a frontera |
| `d01_aguja_litoral` | No inventar playa accesible en acantilado ni rebajar abruptidad por generación |
| `d01_belara_treihord` | Mantener el río exterior al casco; sin nuevo puente ni vado |
| `d01_veldora_litoral` | No mezclar dos bocas fluviales ni situar ciudad entre brazos inventados |
| `d01_linde_caminos` | Gradiente borde-interior del bosque no define relieve nuevo |
| `d01_pilares_sur` | Claros no dividen en bosques canónicos nuevos |
| `d01_taramin_norte_centro` | Semiárido no equivale a desierto ni excluye puntos localmente húmedos |
| `d01_taramin_bosque_sur` | Transición vegetal gradual, no tres masas forestales distintas |
| `d01_syvaris` | Bahía principal canónica sin geometría; protección local no justifica acuífero |
| `d01_arven_contexto` | Bosque continuo a escala insular, con aperturas locales documentadas |

## Algoritmo conceptual sin parámetros inventados

1. Reservar las anclas, ciudades, costas, bosques y los cinco ríos/4 sistemas vigentes; no desplazarlos.
2. Construir macroelevación compatible con las fuentes; si no hay geometría, dejar altitud y pendiente UNKNOWN.
3. Proponer formas menores sobre superficie continua, sin invertir cursos principales ni crear geometría imposible.
4. Calcular pendientes locales, concavidad, conectividad de vaguadas y divisorias reales.
5. Rechazar una geometría que sitúe el Belara cruzando Treihord, colapse los brazos del Thalen o una Veldora con el Lhera.
6. No asumir que riqueza minera en Valkram o Elyra autoriza un yacimiento explotado en una celda concreta.
7. Las modificaciones humanas autorizadas deberán conservar trazas topográficas persistentes; D.P13 solo prepara el contrato.

## Gradiente e incertidumbre

Escala relativa `alta/media/baja` describe comparaciones **solo si existe referencia geométrica**; no se utilizan metros, kilómetros, grados ni porcentajes creados. En zonas sin medidas, pendiente, cota, exposición solar y vertiente específica permanecen `UNKNOWN`.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## Resolución autoral de altitud — 25 de octubre de 2026

**DAR-DP13-ALT-01 (APROBADA):** Montes Valkram, **opción B**: cordillera muy alta. Rango orientativo de **3.600–4.200 m para las grandes cumbres**, no para la totalidad del macizo ni cada montaña individual. Es una escala de diseño expresamente aprobada por el autor; las cotas de valles, cumbres secundarias, pasos, cabeceras y localidades permanecen sin definir.

**DAR-DP13-ALT-02 (APROBADA):** una cumbre excepcional situada en el **sector norte de Valkram**, representada en el mapa del autor **entre la N y la O del rótulo «NORGARD»**, es **la mayor elevación de todo Norgard** y alcanza **aproximadamente 4.200 metros sobre el nivel del mar**. Su nombre propio, coordenadas, laderas exactas, jurisdicción precisa, extensión nival y existencia de glaciares permanecen **UNKNOWN**. «Cumbre septentrional de Valkram» es una descripción, NO un topónimo nuevo.

**Compatibilidad transversal pendiente:** `Geografía/montanas.md` define los Montes Azurios como más altos, anchos y abruptos en términos generales. La elección más reciente del autor fija una **excepción puntual de altura máxima absoluta** para Valkram, compatible con un sistema Azurios globalmente más elevado/abrupto, pero se requiere armonización editorial futura a escala de Norgard para eliminar ambigüedades. **No se cambia la ficha superior en D.P13.**

**Registro operativo:** `Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json`. Esta nueva decisión autoral no contradice la protección del perfil antiguo `darovan_dp13_physical_profiles_v0.1.json`, cuyos campos nulos corresponden a zonas de estudio sin cota única, no a las nuevas anclas individuales aprobadas.


## Anclas altimétricas aprobadas el 25/10/2026

La cumbre septentrional de Valkram, **la Viuda (~4.200 m)**, es la elevación más alta de Norgard. Las Montañas Elyra tienen cumbres de hasta **~2.600 m** (opción A). Son anclas del autor que no convierten las doce zonas cualitativas D01 en polígonos con cota. Sin nombre adicional para cumbres de Elyra ni límites de nieve fijados.

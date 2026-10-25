# Darovan D.P13 — vientos, humedad, nieblas y visibilidad

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## No existe una rosa dominante Darovan autorizada

A diferencia del borrador Valrik, que formula direcciones estacionales concretas para Treskal, las fuentes Darovan no fijan una dirección prevalente anual ni estacional. Se determina primero `weatherAirflowDirection` de un episodio válido y después se estudia exposición de costa, vertiente, barrera y corredor. Barlovento y sotavento se calculan **en cada episodio**. Un relieve sin orientación medida no puede etiquetarse unilateralmente como barlovento.

## Matriz de las doce unidades — exposición y viento

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | canalización en valle, aceleración en cresta; dominante UNKNOWN |
| `d01_elyra_paso_peninsular` | vientos cruzados y efecto embudo en pasos solo con geometría válida |
| `d01_norte_transicion` | exposición a irrupciones frías potencial, dirección dominante UNKNOWN |
| `d01_aguja_litoral` | exposición en costa y protección del dosel; dirección UNKNOWN |
| `d01_belara_treihord` | corredores de viento posibles según valle materializado |
| `d01_veldora_litoral` | brisa mar-tierra plausible como proceso, no dirección dominante anual |
| `d01_linde_caminos` | dosel amortigua viento; corredor del camino puede exponer sectores |
| `d01_pilares_sur` | dosel reduce exposición local, claros son distintos |
| `d01_taramin_norte_centro` | viento expuesto en lomas, sin rosa anual autorizada |
| `d01_taramin_bosque_sur` | viento costero y exposición local no fijados |
| `d01_syvaris` | brisa local plausible, viento anual específico UNKNOWN |
| `d01_arven_contexto` | viento litoral modulado por bosque, direcciones no fijadas |

## Matriz de las doce unidades — humedad, niebla y reducción de visibilidad

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | bruma en hondonadas protegidas solo con saturación y calma |
| `d01_elyra_paso_peninsular` | niebla de valle posible bajo condiciones de humedad y estabilidad |
| `d01_norte_transicion` | escarcha, bruma y baja visibilidad requieren humedad y enfriamiento |
| `d01_aguja_litoral` | humedad bajo cubierta y bruma condicional, visibilidad también obstruida por arbolado |
| `d01_belara_treihord` | niebla ribereña condicional, sin atribuirla a la ciudad cada mañana |
| `d01_veldora_litoral` | niebla costera condicional por contraste térmico y humedad |
| `d01_linde_caminos` | bruma baja plausible con humedad y calma, no permanente |
| `d01_pilares_sur` | zonas bajas umbrías pueden conservar humedad relativa |
| `d01_taramin_norte_centro` | niebla poco favorecida en suelos secos salvo aportes localizados y episodio adecuado |
| `d01_taramin_bosque_sur` | sombra y verdor pueden sostener humedad, niebla necesita condiciones reales |
| `d01_syvaris` | humedad/niebla costera solo según condiciones, visibilidad por bruma posible |
| `d01_arven_contexto` | persistencia de humedad bajo dosel plausible tras aporte real |

## Condiciones mínimas de fenómenos

1. Brisa litoral: necesita contraste térmico tierra-mar y geometría costera; no equivale a viento rector permanente.
2. Viento orográfico: aceleración en cresta, canalización por valle y sotavento solo si flujo y relieve guardan relación real.
3. Humedad alta junto a agua: proximidad no basta; requiere aporte atmosférico o superficial y respuesta térmica.
4. Niebla de valle: humedad cercana a saturación, pérdida de temperatura y escasa dispersión; no siempre hay niebla por existir valle.
5. Niebla marítima: contraste de masas de aire/agua y viento compatibles, con pérdida de visibilidad gradual.
6. Visibilidad reducida: puede deberse independientemente a niebla, precipitación, ventisca local, polvo o cubierta forestal.
7. Persistencia de niebla requiere estabilidad; viento suficiente o calentamiento puede disiparla, con memoria de humedad residual.
8. Bosque de las Agujas: la visibilidad por dosel cerrado es estructural y distinta de una niebla meteorológica.

## Escalas de lectura

`regionalWeather` describe masa de aire, `localModifiers` la costa, relieve y vegetación, `observerVisibility` el estado perceptible. No se invierte la causalidad haciendo llover por existir un bosque ni declarando niebla eterna junto al río.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## Elecciones restantes de D.P13 cerradas

Ver `D.P13/22_cierre_delegado_preguntas_y_opciones.md` y su contrato JSON; las bandas altitudinales y reglas son **diseño delegado**, sin sustituir mediciones ni datos espaciales. El capítulo conserva sus premisas e incertidumbres.

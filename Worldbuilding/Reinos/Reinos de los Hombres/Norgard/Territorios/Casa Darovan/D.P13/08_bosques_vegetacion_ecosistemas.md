# Darovan D.P13 — ecosistemas, bosques y regeneración

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Identidades canónicas que no deben diluirse

- Agujas: coníferas antiguas, caza mayor, sin población permanente interior.
- La Linde: pequeño bosque junto a camino existente; poca caza y explotación maderera poco relevante.
- Pilares: una masa forestal con claros; madera ligada a minas, sin nuevas concesiones.
- Taramin: un único bosque longitudinal cuya composición cambia de coníferas en norte hacia mixto y subtropical húmedo al sur; no tres bosques independientes.
- Syvaris: conjuntos dispersos, isla cálida parcialmente seca con sectores protegidos más verdes; no selva continua.
- Arven: Manto Verde de coníferas continuo aprox. 90% de la isla, madera poco explotada y aldeas principalmente de costa interior ya documentadas.

## Matriz de las doce unidades — cubierta y mosaicos

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | vegetación condicionada por exposición y pisos altitudinales no cartografiados |
| `d01_elyra_paso_peninsular` | mosaicos de montaña no permiten inferir especies arbóreas nuevas |
| `d01_norte_transicion` | bosque boreal/subpolar como referencia regional, no cobertura uniforme |
| `d01_aguja_litoral` | coníferas antiguas y caza mayor; sin aldeas ni pueblos permanentes interiores |
| `d01_belara_treihord` | márgenes vegetados como cobertura posible sin bosque nominado nuevo |
| `d01_veldora_litoral` | cubierta costera no equivale a bosque continuo; Linde es bosque distinto |
| `d01_linde_caminos` | coníferas; no incrementar recursos cinegéticos o madereros |
| `d01_pilares_sur` | coníferas con claros; tala documentada sin inventar nuevas zonas de explotación |
| `d01_taramin_norte_centro` | matorral, breña y pasto duro, sin especies añadidas |
| `d01_taramin_bosque_sur` | continuidad de coníferas→mixto→subtropical húmedo del mismo bosque |
| `d01_syvaris` | bosquetes dispersos y matorral; sur más verde, no selva continua |
| `d01_arven_contexto` | Manto Verde ~90 %, pocas talas, buena caza documentada |

## Causalidad ecológica

1. La vegetación responde a clima, agua, suelo, perturbaciones y tiempo; no se cambia bioma por un solo día lluvioso.
2. El dosel modifica sombra, viento, evaporación e intercepción sin provocar lluvia por sí mismo.
3. Los claros alteran radiación y secado, pero no cambian la identidad del Bosque de los Pilares ni el de Taramin.
4. Humedad temporal del suelo y regeneración vegetal son procesos con distintas escalas de tiempo; persistencia separada.
5. Episodio seco sostenido puede estresar la cubierta, pero la muerte de bosque exige gravedad/duración que el juego deberá modelar.
6. Perturbaciones reales futuras dejan huella con identidad y fuente: tala autorizada, incendio ocurrido o recuperación.
7. Ninguna especie, recurso mineral o industria nueva se instancia por una probabilidad de bioma.

## Fauna y explotación

Las menciones a caza en Agujas/Arven/Linde son anclas cualitativas. No se fabrican especies, cantidades de animales, parcelas, cupos ni red de comercialización en D.P13. Todos esos hechos requieren sus fuentes o fases posteriores.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

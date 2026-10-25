# Darovan D.P13 — cuencas, afluentes, manantiales y dinámica hídrica

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Redes fijadas e invariantes

- **Belara–Lhera:** bifurcación con identidades propias; Belara junto a Treihord y desemboca en Golfo de Norgard, Lhera en Golfo de Veldora. Desconocidos el reparto de aguas y la posición de separación respecto de Treihord.
- **Veldora:** independiente, desemboca en Golfo de Veldora; relación nominal con la ciudad, sin conexión al sistema anterior.
- **Fhalion:** curso menor independiente al sur del Veldora; nacimiento, desembocadura exacta y condiciones del cauce `UNKNOWN`.
- **Thalen:** en la península, doble brazo terminal alrededor de Taramin, desembocadura en Golfo de Norgard; no crear un segundo río ni un puente.

**Las cuatro redes son topológicas, no polígonos de cuenca verificados.** En cada una se distinguen `majorAnchor`, divisorias pendientes, `microcatchmentCandidates`, `minorChannelCandidates`, y receptores autorizables por geometría, nunca afluentes ya existentes.

## Matriz de las doce unidades — potenciales condicionados por unidad

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | Cabeceras tributarias potenciales, receptor final sujeto a divisoria; Belara solo donde la fuente lo establece |
| `d01_elyra_paso_peninsular` | Cuencas de vertiente a resolver; prohibido conectar automáticamente con Thalen, Fhalion u otros |
| `d01_norte_transicion` | Escorrentía y agua helada posibles; ningún río Darovan se declara congelado |
| `d01_aguja_litoral` | Lhera junto a un límite; drenaje directo costero solo con cuenca válida |
| `d01_belara_treihord` | Belara canónico; caudal, llanura de inundación y orden relativo de separación del Lhera UNKNOWN |
| `d01_veldora_litoral` | Lhera y Veldora conservan identidad y cuenca separada salvo Belara→Lhera |
| `d01_linde_caminos` | pequeños drenajes solo si acumulan agua por terreno futuro |
| `d01_pilares_sur` | densidad de cauces menores condicionada por piedemonte, no asignada por nombre del bosque |
| `d01_taramin_norte_centro` | barrancos estacionales como clase regional, sin instancias nominadas ni permanencia de Thalen alterada |
| `d01_taramin_bosque_sur` | microcuencas con recarga condicionada; no convertir Thalen en afluente del bosque |
| `d01_syvaris` | drenajes cortos insulares posibles con pendiente, ninguno nominable sin autor |
| `d01_arven_contexto` | red de drenaje isleña según pendientes, sin manantiales ni cauces confirmados |

## Reglas de nacimiento y conectividad

1. Primero se determina una divisoria mediante cotas: una cuenca no puede cruzarla salvo conducción expresamente autorizada.
2. Cauce menor: exige pendiente convergente, área aportante, disponibilidad de agua y receptor topológicamente válido.
3. Manantial: requiere recarga, contacto de materiales o descarga subterránea justificada; no nace por cercanía decorativa a bosque/cala.
4. Curso permanente, estacional o efímero: depende de balance de agua y contexto, no del nombre de la unidad ni de probabilidad aislada.
5. Humedal: requiere depresión o terreno bajo, aporte y drenaje insuficiente; no crear lagos extensos por defecto.
6. Un segmento tiene receptor aguas abajo o sumidero físico plausible; jamás extremo abierto sin justificación.
7. La vinculación de una microcuenca concreta a un sistema no se decide por proximidad en el mapa ilustrado.
8. Cauce mayor y brazos canónicos permanecen estables; fluctuación de caudal no cambia identidad de los cinco ríos.

## Regímenes y riesgos: mecanismos, no hechos localizados

Caudal cualitativo `bajo/medio/alto` en una instancia futura depende de lluvia reciente y acumulada, deshielo, infiltración, aportes aguas arriba y extracción autorizada; sin valores de aforo ni certeza de permanencia de los cinco ríos. Las crecidas rápidas requieren lluvia intensa sobre cuenca con respuesta corta; las lentas, aportación amplia y almacenamiento; sequía y estiaje requieren balance estacional. Erosión local exige esfuerzo hidráulico y suelo vulnerable. El caso Belara/Treihord exige especial cautela por el puerto industrial existente, sin declarar frecuencia de inundaciones ni prohibir su uso por conjetura.

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

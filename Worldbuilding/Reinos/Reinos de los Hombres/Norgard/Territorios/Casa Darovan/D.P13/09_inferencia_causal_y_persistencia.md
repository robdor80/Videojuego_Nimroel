# Darovan D.P13 — pipeline, causalidad, generación y persistencia

**Estado:** diseño territorial derivado, NO CANON NUEVO · SIN GEOMETRÍA MÉTRICA · NO RUNTIME. Fecha: 25-10-2026.

La autoridad de hechos corresponde a Norgard y a las decisiones expresas del autor. Los mecanismos propuestos son **DERIVED_CONDITIONAL**: no crean rasgos físicos existentes ni hechos de mundo. Cualquier entidad menor generada es futura y requiere topografía. Las doce zonas son claves de estudio D01, no fronteras.

## Orden obligatorio

```text
AUTHORED (Norgard y Darovan) → macrorelieve → microrelieve
→ pendientes y divisorias → cuencas → cauces menores candidatos
→ clima de episodio + estación → nieve, lluvia y escorrentía
→ suelos, cobertura, humedad, erosión → transitabilidad y habitabilidad
→ WorldState persistente (solo futura implementación)
```

No se derivará un arroyo de una tirada meteorológica sin cuenca; ningún narrador de IA podrá situar un nuevo río. Se distinguen estructura física persistente, potencial procedimental aún no materializado y estado transitorio del episodio.

## Matriz de las doce unidades — riesgo plausible contextual

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | deslizamiento o erosión posible con suelo saturado y pendiente |
| `d01_elyra_paso_peninsular` | escorrentía torrencial condicionada, nunca cauce nombrado nuevo |
| `d01_norte_transicion` | helada y deshielo pueden degradar firme según material |
| `d01_aguja_litoral` | erosión de borde costero o ramas caídas: peligros solo potenciales |
| `d01_belara_treihord` | inundación del sector industrial requiere geometría y umbral conocidos |
| `d01_veldora_litoral` | temporales marítimos solo como tipo de riesgo, sin fecha ni frecuencia |
| `d01_linde_caminos` | barro, ramas y visibilidad afectan tránsito futuro sin declarar corte |
| `d01_pilares_sur` | tala sin medidas correctoras puede elevar erosión, no desastre observado |
| `d01_taramin_norte_centro` | escorrentía erosiva y polvo bajo condiciones contrastadas |
| `d01_taramin_bosque_sur` | fuego/erosión solo como peligros condicionales |
| `d01_syvaris` | escasez local de agua o erosión solo tras balance de suelo/lluvia |
| `d01_arven_contexto` | incendio y deterioro como posibilidades, no sucesos históricos |

## Matriz de las doce unidades — filtros para D.P14/D.P15

| Unidad | Perfil condicional y excepción |
|---|---|
| `d01_valkram_oeste` | fuertes pendientes y drenaje conflictivo: evaluación previa de cualquier asentamiento |
| `d01_elyra_paso_peninsular` | pendiente, accesos y exposición limitan futuros trazados |
| `d01_norte_transicion` | habitabilidad dependiente de protección y disponibilidad de agua |
| `d01_aguja_litoral` | asentamientos permanentes prohibidos en interior del bosque |
| `d01_belara_treihord` | proteger puerto de poco calado, barrios y anclas de ciudad |
| `d01_veldora_litoral` | cautela ante inundabilidad litoral y disponibilidad de agua dulce |
| `d01_linde_caminos` | mantener camino existente, no inventar puentes ni variantes |
| `d01_pilares_sur` | evaluar aprovechamiento forestal sin crear nuevas aldeas |
| `d01_taramin_norte_centro` | agua regular no puede presumirse por presencia de barrancos |
| `d01_taramin_bosque_sur` | no inventar talas, pueblos o pasos a partir de gradientes |
| `d01_syvaris` | ciudad, bahía y calas protegidas; no inventar puerto adicional |
| `d01_arven_contexto` | aldeas costeras ya citadas sin añadir emplazamientos ni rutas |

## Reglas de identidad y causalidad verificable

1. La semilla y versión del Content Pack crean candidatos solo bajo anclas y geometría válidas; idéntica entrada produce idéntica salida.
2. Las entidades físicas GENERADAS requieren identificador estable, relación de cuenca, receptor y cadena de causa; no existen en el canon antes de materialización.
3. Temperatura, acumulación de lluvia, reserva de nieve, humedad de suelo, caudal y cobertura vegetal son variables distintas con retardos temporales.
4. Un desborde no destruye asentamiento automáticamente; su efecto exige alcance espacial, duración, exposición y sistemas ejecutados.
5. Guardar delta de WorldState separado de definiciones authored e IDs de entidad: los cambios duraderos no se regeneran al volver.
6. La IA narrativa consume hechos, visibilidad y causas del mundo; no crea meteorología, senderos, fuentes o biomas de autoridad propia.
7. Resolver conflictos por precedencia y versión; no sobrescribir manualmente anclas con datos de una sesión generada.
8. Sin implementación física CoreRPG/Godot, ninguna descripción del contrato se considera prueba de juego operativo.

## Estados hipotéticos reproducibles

| Caso TEST_ONLY | Resultado admisible | Resultado rechazado |
|---|---|---|
| Lluvia intensa Taramin | Activación temporal de barranco con cuenca y pendiente | Río canónico Thalen pasa a efímero |
| Nevadas condicionadas en Valkram | Reserva temporal y posterior deshielo hacia receptor válido | Glaciar permanente creado sin aprobación |
| Linde tras lluvia y días secos | Barro decreciente según drenaje, tránsito y secado | Camino mojado eternamente o reseteado sin causa |
| Syvaris tras episodio húmedo | Cala protegida temporalmente húmeda si recibe agua | Atribución de manantial/pozo autorizado desde el verdor |
| Arven tras tala puntual autorizada en futuro | Huella local y lenta regeneración sin fragmentación canónica | Reducción arbitraria de bosque 90% en su totalidad |

## Trazabilidad y resolución de incertidumbres

Fuentes originales prioritarias: [relieve de Norgard](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/montanas.md), [ríos](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/rios_y_lagos.md), [bosques](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/bosques.md), [clima](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Clima/clima_general.md), [regiones](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Geograf%C3%ADa/regiones_naturales.md); D01/D02/D03 y [auditoría D12](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Darovan/Auditorias/D12_INVENTARIO_CANON_Y_AUTORIDAD.md). [Valrik/Treskal](https://github.com/robdor80/Videojuego_Nimroel/blob/main/Worldbuilding/Reinos/Reinos%20de%20los%20Hombres/Norgard/Territorios/Casa%20Valrik/Geografia_local/reglas_espaciales_generacion_motor_v0.1.md) proporciona metodología, no condiciones ni cifras transferibles. Sin cotas, geometrías, magnitudes de lluvia ni red de corrientes instancia; las incógnitas se conservan como `UNKNOWN`. Las variaciones solo se aplicarán a un `WorldState` cuando exista implementación autorizada.

## DAR-DP13-CITY-ALT-01 — Altitud de Treihord (25/10/2026)

**APROBADA — opción A:** banda de referencia de **150–350 m s. n. m.** para el emplazamiento urbano general de Treihord. No se fija una altitud exacta de la ciudad ni de sus ocho barrios, muelles o plazas. Tampoco cota del Belara, pendientes, accesos, nuevos puentes o navegabilidad. La ciudad sigue **junto al Belara, sin que el río la atraviese**, y su puerto continúa siendo exclusivamente industrial para barcazas de poco calado. Este rango es dato de **autor**, no altimetría métrica de un mapa.

Documento: `D.P13/14_altitud_treihord_autorizada.md`; contrato: `Datos operativos/darovan_dp13_treihord_elevation_authorial_v0.1.json`. Uso para D.P16/D.P18 únicamente como referencia, sin iniciar esas fases.


## DAR-DP13-CITY-ALT-03 — Taramin, opción A (25/10/2026)

**APROBADO POR EL AUTOR:** el **núcleo urbano principal de Taramin** tiene una banda altitudinal de referencia aproximada de **0–40 m s. n. m.**. No define una altitud exacta de barrios, muelles, nivel de agua, pendientes o plano georreferenciado. Mantiene un único **Thalen** con **dos brazos terminales** entre los que se sitúa la ciudad; las conexiones físicas, navegabilidad y emplazamiento exacto de estructuras permanecen UNKNOWN. No se crea isla, puente, vía, canal, puerto adicional ni escenario de inundación.

Documento: `D.P13/16_altitud_taramin_autorizada.md`. Registro: `Datos operativos/darovan_dp13_taramin_elevation_authorial_v0.1.json`. La cifra es una decisión autoral y no una topografía métrica ejecutada; no inicia D.P16/D.P18.


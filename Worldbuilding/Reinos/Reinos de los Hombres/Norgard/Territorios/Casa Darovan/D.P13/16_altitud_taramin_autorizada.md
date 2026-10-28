# D.P13 — Altitud urbana aproximada de Taramin

**Fecha:** 25/10/2026 · **Decisión autoral:** `DAR-DP13-CITY-ALT-03` · **Opción A** · **Estado:** AUTHORED (dato de diseño aprobado, no medición ni runtime).

## Banda altitudinal aprobada

El autor aprueba **0–40 metros sobre el nivel del mar** como banda de referencia aproximada del **núcleo urbano principal de la ciudad de Taramin**, importante puerto pesquero de Darovan situado en el tramo final del **río Thalen**. El valor representa la referencia general de emplazamiento, **no la cota exacta de cada calle, barrio, muelle, embarcadero, ribera o edificación**. No se fija un punto medio.

## Invariantes de hidrografía y canon urbano

- El río **Thalen mantiene su identidad de un solo río con dos brazos terminales**. Taramin está situada **entre ambos brazos**; esta ubicación ya era canónica en Norgard, D02 y D07.
- La elección de una cota baja **no crea** una isla cartográfica, un canal, un brazo adicional, un nuevo muelle, un puente, una calzada, ni atribuye navegabilidad a ninguno de los brazos.
- Taramin conserva el papel portuario pesquero, con actividad marítima y fluvial ya descrita en D07, sin concretar instalaciones nuevas.
- El régimen semiárido de transición de la península **no queda redefinido** por la altitud urbana.

## Condicionantes para la materialización posterior

La futura representación requerirá emplazamiento de ribera y costa, pendientes, altura del agua, variaciones hidrológicas, accesos y superficies urbanas. Un terreno costero bajo podría necesitar evaluación de inundabilidad, pero **ninguna frecuencia, superficie, umbral, gravedad o suceso de inundación** está autorizada todavía. Los niveles del Thalen, de la marea y de muelles siguen UNKNOWN.

## Registro e impacto

- `../Datos operativos/darovan_dp13_taramin_elevation_authorial_v0.1.json`: dato autoral y guardas estructuradas.
- Referencias: `Geografía/rios_y_lagos.md`, `Grandes Casas/grandes_casas.md`, D01 y D07.
- Contrato para el futuro D.P16/D.P18; **no inicia esas fases**, no modifica D01–D12 ni implementa nada en CoreRPG/Godot.

**Origen de la decisión:** aprobación expresa de la opción A (0–40 m) por el autor en la conversación D.P13, 25 de octubre de 2026.

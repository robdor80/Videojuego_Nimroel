# D.P13 — Territorio físico completo · Casa Darovan

**Fecha:** 25-10-2026 · **Rama:** `feat/darovan-dp13-territorio-fisico` · **Autoridad:** diseño DERIVED_CONDITIONAL, sin nuevos hechos canónicos.

## Itinerario de estudio

- `00_comparacion_fuentes_y_metodo.md` — contraste Valrik/Treskal y autoridad.
- `01_regiones_y_subzonas.md` — cobertura de doce unidades.
- `02_relieve_y_microrelieve.md` — capas de terreno y divisorias.
- `03_cuencas_y_agua_menor.md` — ríos, cuencas y red menor candidata.
- `04_temperatura_y_estaciones.md` — temperaturas y cuatro estaciones.
- `05_lluvia_nieve_y_deshielo.md` — precipitación, hielo y balance hídrico.
- `06_viento_humedad_niebla.md` — exposición, viento y visibilidad.
- `07_suelos_drenaje_erosion.md` — suelos y respuesta al agua.
- `08_bosques_vegetacion_ecosistemas.md` — identidad y dinámica forestal.
- `09_inferencia_causal_y_persistencia.md` — integración ambiental.
- `10_contratos_y_validacion.md` — JSON, pruebas y host futuro.
- `11_auditoria_suficiencia.md` — evaluación comparable con Valrik/Treskal.

## Datos

En `../Datos operativos/`: `darovan_dp13_physical_profiles_v0.1.json`, `darovan_dp13_hydro_overlay_v0.1.json`, `darovan_dp13_environment_causal_v0.1.json`. La carpeta D.P13 no sustituye fuentes D01–D03. Estados espaciales concretos, política, nuevas poblaciones y hechos de juego quedan fuera de su alcance.

## Verificación

`python Tools/DarovanDP13/validate.py`, regresiones D01–D12 y CI Windows/Linux. **Documento de diseño, no juego en funcionamiento.**


## Ampliación autoral de altimetría

- `12_altitud_valkram_autorizada.md`: opción B y cumbre septentrional de ~4.200 m, la más alta de Norgard, con ubicación visual aproximada y nombre oficial **la Viuda** (DAR-DP13-ALT-03).
- `../Datos operativos/darovan_dp13_valkram_altitude_authorial_v0.1.json`: anclas elevacionales **AUTHORED**, independientes del perfil de doce zonas todavía sin cotas.

- `13_altitud_elyra_autorizada.md`: opción A de Montañas Elyra, cumbres máximas de hasta ~2.600 m, sin inventar un pico individual.
- `../Datos operativos/darovan_dp13_elyra_altitude_authorial_v0.1.json`: altura orientativa de Elyra por decisión expresa del autor.

- **DAR-DP13-SNOW-01:** opción B de nieve para **la Viuda**: neveros localizados que sobreviven al verano en zonas altas y protegidas. No afirma glaciares, cota de nieve, ni permanencia nival general de Valkram.

- **DAR-DP13-PASS-01:** principales pasos naturales de Valkram con rango altitudinal orientativo **1.400–2.200 m**, sin crear pasos nominados, rutas ni geometría de terreno.

- `14_altitud_treihord_autorizada.md`: banda urbana autoral **150–350 m** (opción A), sin cotas individuales ni plano métrico.
- `../Datos operativos/darovan_dp13_treihord_elevation_authorial_v0.1.json`: ancla de altitud referencial de Treihord.

- `15_altitud_veldora_autorizada.md`: Veldora opción A; franja urbana de referencia **0–60 m** junto al golfo, sin cotas de muelles ni barrios.
- `../Datos operativos/darovan_dp13_veldora_elevation_authorial_v0.1.json`: ancla de altitud expresamente aprobada para Veldora.

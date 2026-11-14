# E19-R3 — Suelos, microclimas, vegetación y aprovechamiento natural
**14 de noviembre de 2026 — diseño territorial B2, no plano B3 ni ejecución B4.**

Continuación *apilada* de E19-R2 (PR #90, `50a284cf33d59465332623c8a46c5e1d41cdb664`) sobre R1 #89 y R0 #87. Ninguna geometría descartada de #84 se recupera. El estándar obligatorio es la **profundidad causal de Valrik/Treskal**, no sus biomas ni sus cotas.

## Entregables
1. [01_PERFILES_SUELO_DRENAJE.md](01_PERFILES_SUELO_DRENAJE.md): 12 prototipos de suelo, infiltración, reserva, erosión, tránsito y criterios de aptitud.
2. [02_MICROCLIMAS_Y_GRADIENTES.md](02_MICROCLIMAS_Y_GRADIENTES.md): 11 reglas causales de exposición, frío, dosel, agua y nieve.
3. [03_VEGETACION_Y_MOSAICOS.md](03_VEGETACION_Y_MOSAICOS.md): 10 coberturas de diseño, sucesión, mosaicos productivos y bosques protegidos.
4. [04_APROVECHAMIENTO_Y_DERECHOS.md](04_APROVECHAMIENTO_Y_DERECHOS.md): 10 cadenas de recurso con titularidad, límites y regeneración.
5. [05_ESTACIONALIDAD_Y_MEMORIA.md](05_ESTACIONALIDAD_Y_MEMORIA.md): ocho ciclos causales con persistencia, riesgos y consecuencias.
6. [06_ATLAS_POR_CONTEXTOS.md](06_ATLAS_POR_CONTEXTOS.md): siete fichas integradas MF-01..07, MF-08 vedado.
7. [07_CONTRATO_GENERACION_2D.md](07_CONTRATO_GENERACION_2D.md): relaciones de inferencia, autorización y futura persistencia.
8. [08_PARIDAD_VALRIK_Y_PRUEBAS.md](08_PARIDAD_VALRIK_Y_PRUEBAS.md): matriz de comparación y rechazos.
9. [09_ACTA_R3_Y_TRASPASO.md](09_ACTA_R3_Y_TRASPASO.md): estado, deudas y puertas R4/R5/R6.
10. `environment_v0.4.json`: contrato de tipologías y prohibiciones, **cero instancias físicas**.
11. `Tools/EdranorE19R3/validate.py` y CI Windows/Linux con regresión R0–R2 y pruebas adversariales.

## Fuentes rectoras (solo lectura)
- `Casa Valrik/Clima_local/07_suelos_y_drenaje.md`, `08_vegetacion_y_microclimas.md`, `09_reglas_de_inferencia_para_juego.md` y `Geografia_local/microrelieve_y_unidades_de_drenaje_v0.1.md`.
- Edranor E03 (Suelos, Clima, Ecosistemas), E04 (Viticultura), E13/06, E15 y E17.
- E19-R1/`natural_features_v0.2.json` y E19-R2/`hydrology_v0.3.json`.

**Lectura obligatoria:** `SO-*`, `MU-*`, `CV-*` y `RN-*` son **familias, reglas o cadenas de estudio**, no entidades creadas. Sus condiciones requieren pruebas locales posteriores. `UNKNOWN` no significa cero y `POTENCIAL` no significa aprobado.

## Gobierno de incertidumbre
Aprobada para **diseñar**: distinción de relieve, suelo, cobertura, condición hídrica, microclima y usos con procedencia. Sin acreditar: ubicación/área de parcelas, valores físicos, explotaciones, límites forestales, pluviometría, grados-día, caminos, caudales y derechos de extracción. Ni Godot ni CoreRPG ni World State son modificados.

La calidad Valrik se alcanza **en este estrato documental** mediante cadenas causa→estado→uso→riesgo→persistencia y pruebas de rechazo. La paridad cartográfica y jugable completa continúa pendiente de R4–R6 y E19-TEC.

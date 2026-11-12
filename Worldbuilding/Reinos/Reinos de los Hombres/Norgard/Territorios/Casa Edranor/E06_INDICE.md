# EDRANOR E06 — Asentamientos ordinarios y generación procedural
**Fecha:** 12/11/2026 · **Estado:** fase de diseño + laboratorio determinista; **NO RUNTIME**, no aldeas colocadas en Nimroel.

E05 está fusionada en main; E06 no convierte las cuatro preguntas de carretera E05 en itinerarios ni la economía E04 en parcelas.

## Entregables
1. [Esqueleto y exclusiones](Asentamientos/E06_ESQUELETO_ELEGIBILIDAD.md).
2. [Ocho arquetipos territoriales](Asentamientos/E06_ARQUETIPOS_Y_ECONOMIA.md).
3. [Siete unidades y pesos cualitativos](Asentamientos/E06_PESOS_REGIONALES.md).
4. [Semillas, identidad estable y persistencia](Asentamientos/E06_SEMILLAS_Y_PERSISTENCIA.md).
5. [Quince pruebas de laboratorio](Asentamientos/E06_ESCENARIOS_SINTETICOS.md).
6. [Fuentes y decisiones](Auditorias/E06_FUENTES_Y_DECISIONES.md), [acta](Auditorias/E06_ACTA.md) y [traspaso E07](00_Control_del_proyecto/TRASPASO_E07.md).
7. Contratos: `Datos operativos/edranor_e06_settlement_rules_v0.1.json` y `edranor_e06_synthetic_fixtures_v0.1.json`. Código puro: `Tools/EdranorE06/lab.py`, prueba `validate.py`, CI Windows/Linux.

**Cinco lugares protegidos:** Dorth, Lumina, Karsath, Rodas (Corona real) y Hallheim (fuera del territorio). E07 diseñará manualmente sus núcleos pertinentes; E06 no les asigna poblaciones ni nombres.

**Jerarquía:** Nimroel Core → Norgard Defaults → Casa Edranor → Localidad → World State. Las pruebas `TEST_ONLY` no confirman posiciones, cultivos, derechos ni edificios.

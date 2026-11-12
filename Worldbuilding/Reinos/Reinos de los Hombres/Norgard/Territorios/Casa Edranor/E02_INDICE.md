# Casa Edranor — E02 | Hidrología y drenaje
**Fecha:** 12/11/2026 · **Tipo:** planificación cartográfica documental no-runtime · **Base:** \`main\` con E01 fusionada en PR #52.

## Resultado
La revisión del canon regional recupera **Río Lurien** y **Lago Antela**, ausentes como nombres concretos en E01 porque aquella fase aplazaba la verificación de hidrografía. No se inventan ríos. El Lurien nace al este de Valkram, forma Antela al sur de Karsath, sigue hacia Hallheim y desemboca en el Golfo de Norgard. Su **navegabilidad solo está confirmada desde Hallheim hacia el mar**. Ser un hecho regional no demuestra que el cauce ni toda la ribera de Antela pertenezcan administrativamente a Edranor.

- [Atlas hidrográfico](Cartografia/E02_ATLAS_HIDROGRAFICO.md): hechos canónicos, ubicación relativa y límites.
- [Cuencas y divisorias](Cartografia/E02_CUENCAS_DIVISORIAS.md): áreas de estudio sin polígonos ni vertientes adjudicadas.
- [Drenaje y riesgos](Cartografia/E02_DRENAJE_Y_RIESGOS.md): procesos condicionales y pruebas de campo/cartografía necesarias.
- [Agua para los usos locales](Agua_y_usos/E02_AGUA_Y_VITICULTURA.md): demandas de estudio sin derechos, infraestructura ni abastecimiento inventados.
- [Cruces y E05](Cartografia/E02_CRUCES_Y_MOVILIDAD.md): cuatro corredores E01; cruces \`UNKNOWN\`.
- [Matriz de fuentes](Auditorias/E02_FUENTES_Y_DECISIONES.md); [acta](Auditorias/E02_ACTA.md); [traspaso E03](00_Control_del_proyecto/TRASPASO_E03.md).
- [Contrato de planificación](Datos%20operativos/edranor_e02_hydrology_v0.1.json); \`Tools/EdranorE02/validate.py\`; \`.github/workflows/edranor-e02.yml\`.

**Invariantes:** Dorth/Lumina/Karsath de Edranor; Rodas geográficamente contextual, pero jurisdicción, fiscalidad y berserkers de la Corona; Hallheim fuera; norte recortado y abierto. Herencia \`Nimroel Core → Norgard Defaults → Casa Edranor → Localidad → World State\`. Esta fase **no** entrega cartografía 2D, escenarios de inundación simulados, conexión Godot ni ejecución CoreRPG.

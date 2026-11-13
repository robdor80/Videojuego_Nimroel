# GALDREN G03 — Clima, suelos y ecosistemas
**13/11/2026 · v0.1 · planificación documental; NO runtime.**
**Base:** G02 fusionada en `main` mediante PR #67; SHA `1ad65cb5eb5dd449c6dd981cba3b63d96435d69f`.

## Entrega y criterio
1. [Gradientes y microclimas](Clima/G03_GRADIENTES_Y_MICROCLIMAS.md): siete referencias climáticas de estudio y doce fichas ligadas exactamente a G01-U01..U12.
2. [Atlas de suelos](Suelos/G03_ATLAS_EDAFOLOGICO.md): fertilidad regional confirmada, capacidad agrícola local aún UNASSESSED y protocolo de comprobación por parcela.
3. [Atlas ecológico](Ecosistemas/G03_ATLAS_ECOLOGICO.md): tres bosques orientales canónicos, sistemas boreales y contactos vecinos; flora existente y sin fauna inventada.
4. [Estacionalidad y riesgos](Riesgos/G03_ESTACIONALIDAD_Y_PELIGROS.md): evidencia de hielo separada de nueve escenarios, tres de ellos hechos cualitativos confirmados, y restantes estudios.
5. [Contrato JSON](Datos%20operativos/galdren_g03_climate_soils_ecosystems_v0.1.json): plan de representación referenciable con `runtimeEnabled=false`.
6. [Fuentes y deuda](Auditorias/G03_FUENTES_Y_DEUDA.md), [acta](Auditorias/G03_ACTA.md) y [traspaso G04](00_Control_del_proyecto/TRASPASO_G04.md).
7. `Tools/GaldrenG03/validate.py` y `.github/workflows/galdren-g03.yml`: pruebas positivas, mutaciones negativas y regresión G00–G03 en Windows/Linux.

## Restricciones que se mantienen
- Las doce unidades G01 son ámbitos naturales de estudio, **no provincias**. El borde rojo autoral no es polígono legal, climático, de suelo o bioma.
- **Arleon y Zanthir** son Galdren; **Treskal** es Valrik, **Dorth** Edranor, **Hallheim** Corona. Forja Estelar es instalación estratégica de titularidad UNKNOWN, administrada ordinariamente por Galdren y bajo mando regio en guerra.
- El **Caleran** es un único sistema nacido en vertiente occidental de Azurios, con llanuras orientales y bifurcaciones inferiores; su conexión topográfica oeste→este no está resuelta. Vornarsk y Keldarsk se congelan en invierno, sin desembocaduras conocidas.
- No situar toda la franja polar, los Montes Invernos o los bosques próximos dentro de Galdren; no crear glaciares, afluentes, especies, yacimientos, aldeas, puertos, carreteras ni cifras.
- El **Bosque Quebrado** es la principal región caballar de Norgard; su ubicación natural no otorga dominio automático a una Casa.
- Clima, suelo y ecosistema son capas independientes; las etiquetas de estudio no son casillas de Godot ni reglas de CoreRPG.

## Jerarquía de herencia
Nimroel Core → Norgard Defaults → Casa Galdren → Localidad → World State.

Esta fase no valida coordenadas, pluviómetros, termómetros, perfiles edáficos, niveles freáticos, mapas de riesgos, fenología o calendario absoluto. Ningún dato aquí se presenta como simulación ejecutada ni gameplay.
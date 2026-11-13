# GALDREN G06 — Comunicaciones y redes económicas
**13/11/2026 · v0.1 · DOCUMENTARY_PLANNING_ONLY.** Base de fase: G05 fusionada PR #70; main `8610affd134d3134b8cba17b2b43c483331b127a`. G06 no activa transporte, mensajería, comercio, economía, carreteras ni contenido jugable.

## Resultado y límites
La fase integra **seis corredores G01 de estudio**, **doce relaciones económicas (G04 seis + G05 seis)**, **seis modelos de información** y **seis modalidades de transporte/competencia**. Son **consultas** para la futura red, no una malla conexa demostrada. Cero carreteras, puentes, vados, estaciones, puestos, puertos, tarifas, concesiones o rutas creados.

## Entregables
1. [Corredores y prioridades de verificación](Comunicaciones/G06_CORREDORES_Y_PRIORIDADES.md).
2. [Modalidades, hidrografía y estación](Comunicaciones/G06_MODALIDADES_Y_ESTACIONALIDAD.md).
3. [Mensajería, avisos y conocimiento](Comunicaciones/G06_MENSAJERIA_Y_CONOCIMIENTO.md).
4. [Doce conexiones económicas no verificadas](Economia/G06_MATRIZ_DE_INTERCAMBIO.md).
5. [Control económico, impuestos y trazabilidad](Economia/G06_CONTROL_Y_TRAZABILIDAD.md).
6. [Logística de la reserva regia](Forja_Estelar/G06_LOGISTICA_REGIA.md).
7. [Riesgos y niveles de evidencia](Riesgos/G06_RIESGOS.md).
8. [Fuentes y deuda](Auditorias/G06_FUENTES_Y_DEUDA.md), [acta](Auditorias/G06_ACTA.md), [traspaso G07](00_Control_del_proyecto/TRASPASO_G07.md).
9. [Contrato G06](Datos%20operativos/galdren_g06_communications_economic_networks_v0.1.json), validador `Tools/GaldrenG06/validate.py`, CI `.github/workflows/galdren-g06.yml` para Windows/Linux.

## Jerarquía vigente
**Arleon y Zanthir**: Casa Galdren. **Hallheim**: Corona/Aethros. **Treskal**: Valrik; **Dorth**: Edranor. **Forja Estelar**: instalación en contexto Zanthir, de dominio, administración y mando **directos y permanentes de Corona/Aethros** en paz y guerra (G05-D01). La Corona tiene la ceca de Hallheim, Clavo/Luna/Corona y autoridad fiscal del reino; **no hay aduanas internas entre Casas**. El Metal Estelar solo procede de los Montes Azurios. La presencia de un pueblo o un topónimo vial no prueba carreteras o libre acceso a reservas.

## Geografía no resuelta
Transición Azurios occidental→llanuras orientales del Caleran, dos brazos del mismo río, riberas y bocas, pasos de Invernos, derechos en zonas compartidas, fuentes/salidas del Vornarsk y Keldarsk, puerto de Zanthir y navegabilidad **UNKNOWN**. El hielo invernal de esos dos ríos y de la bahía sí es cualitativamente canónico; no hay calendario de cierres ni pérdidas confirmadas.

## Estado técnico
Los expedientes y JSON están deliberadamente **desconectados del runtime** (`runtimeEnabled=false`). Validación JSON/Python no acredita generación de mundos, CoreRPG C++20, Godot 4.7.2 2D, Windows x64, Android ARM64 ni jugabilidad.

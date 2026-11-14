# E19-R5.11 — Acta de alcance, criterios de cierre y traspaso E19-R6
**Fecha:** 14-11-2026. **Base:** R4 `17664ebd54f9553d1a652c79f4a851c169da629c`. **Carácter:** diseño B2; el cierre técnico se consigna únicamente tras pruebas, diff y CI del HEAD final.

## Entregas y evidencias
- 12 textos contando README y 11 monografías, contrato JSON v0.6, validador adversarial y workflow multiplataforma.
- 8 contextos MF, de ellos 7 evaluables para estudio y MF-08 vetado.
- 19 programas OS de **preguntas**, 0 emplazamientos/aldeas/villas/viviendas/parcelas/servicios reales.
- Cuatro perfiles de trabajo rural, tres esqueletos funcionales para asentamientos ordinarios y cuatro anclas excluidas del generador Edranor (Dorth, Lumina, Karsath, Rodas), además de Hallheim exterior.
- Sd demanda, Sq cobertura hipotética, Sp red de proveedores verificados vacía.
- Reglas de hogar/residencia, agua, saneamiento, tenencia, permisos, conservación, riesgos, calendario y persistencia.
- Paridad de **método** con Valrik, con deuda B3/B4 explícita y 30 rechazos de diseño.

## Regresión obligatoria
Ejecutar R0/R1/R2/R3/R4 y R5 en Linux y Windows sobre HEAD final; comprobar árbol exclusivamente aditivo y datos padres intactos. Pruebas de contrato inmutables, escenarios sintéticos elegibles y rechazados, y mutaciones por cada guardia. Revisar resultado de GitHub Actions antes de cambiar estado de PR. Cualquier test que confirme «tiene carreteras» sin Gp medido es un falso positivo.

## Deudas bloqueantes
1. EDD-01/02: norte sin cierre, polígonos de pertenencia, huellas y relieve medidos.
2. EDD-03: agua potable, receptores, estacionalidad, caudales y cruces.
3. EDD-04: población por núcleo y jurisdicción, rural, hogares y variación estacional.
4. EDD-07: Gp, servidumbres, modos, distancias y capacidad.
5. Regímenes de Bosque Alto/Bosque Real, tenencias y autorizaciones concretas.
6. E19-TEC: parcelas, ocupación B3, representación Godot 2D y trazabilidad.
7. E26/E28: identidad real de residentes, sistemas económicos y persistencia CoreRPG.

## Traspaso específico R6
Revisar ortogonalmente las dependencias E05 (vías), E06 (generación), E07 (anclas), E08 (censo), E09 (competencia), E14 (ocupación), E15 (economía), E16 (servicios), E17 (causalidad), E18 (madurez) y R0–R4. Contrastar 30 adversarios y mantener diferencias materiales frente a Valrik. La certificación documental no implica ciudad o territorio jugable.

## Integración segura
PR R5 **Draft contra rama R4**, que a su vez depende de R3→R2→R1→R0. Integrar en orden y auditar todos los HEAD; no fusionar R5 directamente a main ni modificar otras casas, CoreRPG, Game o ContentPacks.

# Registro de fases — Casa Darovan
**Fecha de comprobación:** 21-10-2026. **Estados comprobados en GitHub el 21-10-2026:** D00–D04 integradas en main; D01–D03 Python MSI superados; D01–D05 Python GitHub Actions Windows/Linux superados. D05 documental cerrada y validada en CI Windows/Linux; PR #30 preparada para revisión, no fusionada; decisión de merge reservada al autor.

| Fase | Entrega | Estado | Conversación |
|---|---|---|---|
| D00 | Canon, auditoría, estructura, metodología y protocolo | **FUSIONADA en main, PR #14** (merge commit 73aa5c4691a3dc07ca588c07a7ce267a69fdd085) | Darovan 1 |
| D01 | Geografía y orografía | **FUSIONADA EN MAIN, PR #15**, merge 9f3f723b0e7b2b78567c6397bba7099bfe658b0a | Darovan 2 |
| D02 | Hidrografía y cuencas | **FUSIONADA EN MAIN, PR #16**, merge 34c9652eba2bd0fed33ab6a3931f24400a39b812; no-runtime | Darovan 3 |
| D03 | Clima y ecosistemas | **FUSIONADA MAIN, PR #17 squash 191bcd5; PYTHON MSI D01–D03 SUPERADO**; 12 zonas de estudio cualitativas; no-runtime/no canon nuevo | Darovan 4 |
| D04 | Recursos y producción | **FUSIONADA EN MAIN**, PR #20, commit d4a07ba25f8560d5005a52aafc763699917f2388; CI D01–D04 Windows/Linux OK; no runtime | Darovan 5 |
| D05 | Movilidad y comunicaciones | **DOCUMENTALMENTE CERRADA Y CI ESTÁTICA WINDOWS/LINUX OK**; PR #30 en revisión, SIN FUSIONAR; no canon nuevo ni runtime, merge exige autor | Darovan 6 |
| D06 | Asentamientos procedurales | NO INICIADA | Darovan 7 |
| D07 | Ciudades canónicas | NO INICIADA | Darovan 8 |
| D08 | Población y servicios | NO INICIADA | Darovan 9 |
| D09 | Administración y defensa | NO INICIADA | Darovan 10 |
| D10 | Cultura y sociedad | NO INICIADA | Darovan 11 |
| D11 | Contratos y motor | NO INICIADA | Darovan 12 |
| D12 | Auditoría integral | NO INICIADA | Darovan 13 |

**Evidencia:** MSI físico (15-10-2026): D01/D02/D03 `STATIC OK` en checkout local (acta D03). CI Windows 2022 + Ubuntu 24.04 (21-10-2026): D01/D02/D03/D04/D05 `STATIC OK` en checkout íntegro de la rama D05 (run `39587112092`, [acta](../Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md)). No prueba Godot/GIS/runtime ni MSI físico D04/D05. PR #20 **ya fue fusionada**; D05 PR #30 está abierta sin merge.

**Protocolo:** una fase/conversación/rama, PR propia, sin merge automático. La validación documental NO acredita canon nuevo, mapa métrico ni juego ejecutado. D00–D04 están integradas; D05 requiere aprobación de PR #30. D06 aún no se ha iniciado.

## Inicio D05 comprobado 21-10-2026
GitHub confirmó PR #20 fusionada y `main` en `d4a07ba25f8560d5005a52aafc763699917f2388` antes de crear rama D05. D05 documenta red modal, datos, validación y traspaso D06 sin comenzar D06. [CI de la PR #30 D01–D05](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39587112092) superada en Ubuntu y Windows, con 30 negativas D05 rechazadas. [Acta D05](../Auditorias/D05_CIERRE_Y_VALIDACION_2026-10-21.md). El commit final de auditoría se verificará nuevamente en Actions.


### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.

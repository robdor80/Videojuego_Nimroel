# DAROVAN D08 — Auditoría final y entrega para revisión (21/10/2026)
**Estado:** DESARROLLO DOCUMENTAL Y REGRESIONES ESTÁTICAS COMPLETADOS. **PR Draft #34 SIN FUSIONAR**. El autor conserva la decisión de revisión/fusión. D09 NO INICIADA.

## Cadena de verificación
- Base `main` D07 verificada: `23670e68532447d918c04839369a9962448f2e44`, PR #32 fusionada.
- Rama `feat/darovan-d08-hogares-poblacion-servicios`; primera entrega `8ced1dac563dad6afa829d896e22436afcf7bab1`.
- GitHub Actions real [run #39677333900](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39677333900), sobre exactamente ese SHA: **SUCCESS** en `ubuntu-24.04` y `windows-2022`.
- `Validacion/validate_d08.py`: comprobación de integridad de 25 referencias documentales, ocho cadenas D04, nueve modelos D06, cuatro ciudades manuales D07, diez necesidades de servicio, doce familias ocupacionales funcionales, siete fixtures de prueba `TEST_ONLY` y **35 mutaciones negativas rechazadas**. Workflow conserva la regresión D01–D07 sin cambiar sus validadores.
- `Datos operativos/darovan_d08_population_services.schema.json` declara estructura de D08; validador Python realiza la comprobación específica, no se atribuye uso de una librería externa jsonschema.
- **Nota de HEAD:** un commit documental posterior que añada esta acta requiere una segunda CI en su SHA final antes de considerar el HEAD validado.

## Qué está acreditado y qué no
- Sí: coherencia **estática** de fuentes, índices y reglas; independencia de los ejemplos sintéticos; prohibición de cifras/capacidades nuevas; protección de Treihord ~32.000 y elecciones Veldora B, Taramin A, Syvaris A únicamente conceptuales.
- No: creación de NPC, reservas poblacionales cargadas en WorldState, salarios reales, inventarios, viajes, alojamientos, servicios, IA, ejecución de CoreRPG, ejecución de Godot o persistencia de una sesión D08.
- CoreRPG aporta identidades, reservas, relaciones y persistencia genérica. Los contratos Nimroel Core `RES/KIN/CARE/EMP/APR/CHORE/NEED/WAIT/TXN/OWN/FOOD/WASTE` son fuentes documentales, no interfaces implementadas por CoreRPG para estas mecánicas.

## Decisiones y riesgos explícitamente abiertos
- Población distinta de Treihord, total de Darovan, proporciones urbano/rural, estructura por edades, tamaños medios de hogar y dotaciones: **UNKNOWN**; aprobación autor obligatoria antes de usarlos como canon.
- Nuevas instituciones, subclases sociales, gremios, personas importantes, oficios singulares, planos o edificios: no creados. Propuesta sustantiva futura requiere consulta de una decisión cada vez.
- D05 abastecimiento ≠ ruta; Thalen brazos terminales sin navegabilidad acreditada; Belara industrial somero; Syvaris sin armada Darovan; Veldora sin aduanas entre Grandes Casas; Arven Darovan sin quinta ciudad; Agujas sin asentamientos interiores; D06 fixtures no canónicos.
- D11 reserva API/adaptadores/IDs numéricos de relaciones, snapshots, GIS y pruebas runtime; D09/D10 no se anticipan.

## Archivos entregados
- `Auditorias/D08_AUDITORIA_PREVIA_2026-10-21.md`; modelos en `Poblacion_y_hogares/`; matriz en `Servicios_e_infraestructuras/`.
- JSON de planificación, esquema y fixtures en `Datos operativos/`; matriz de invariantes y validador en `Validacion/`.
- Adendas en plan, registro y decisiones; traspaso **preparatorio**, no inicio, `00_Control_del_proyecto/TRASPASO_D09.md`.

**Criterio de cierre:** CI final del HEAD verde, revisión de PR #34 y aprobación expresa del autor para cualquier fusión. D08 no canoniza sus propuestas ni sustituye los Defaults de Norgard.

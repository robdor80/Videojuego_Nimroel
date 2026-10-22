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

## Adenda de revisión autoral posterior (22/10/2026)
El autor aprobó DAR-D08-01 Veldora, opción B, como **rango canónico de 29.000–35.000 habitantes** (no número exacto). Véase `D08_RESOLUCION_DAR-D08-01_VELDORA_2026-10-22.md`. Esta adenda modifica exclusivamente el alcance de la afirmación original de «solo Treihord con demografía conocida». Ningún valor se materializa en WorldState. Taramin/Syvaris/total siguen UNKNOWN. El HEAD de GitHub Actions original no sirve para validar este cambio: es imprescindible CI del nuevo commit antes de declarar este incremento en verde. PR #34 permanece Draft.

## Segunda adenda autoral — Taramin — 22/10/2026
El autor aprueba **Taramin, DAR-D08-01 opción B, intervalo canónico 14.000–20.000 habitantes**, sin cifra exacta. Acta `D08_RESOLUCION_DAR-D08-01_TARAMIN_2026-10-22.md`. Es una modificación ulterior a la adenda Veldora y a la auditoría histórica inicial, sin alterarlas retroactivamente. La cifra de Syvaris y el total territorial siguen UNKNOWN; no se añade ciudad, edificio, NPC ni instancia CoreRPG. La validación nueva exige un CI de HEAD actualizado Windows/Linux, sin depender del anterior run de Veldora. PR #34 sigue Draft y sin fusionar.

## Tercera adenda autoral — Syvaris — 22/10/2026
Aprobado el intervalo canónico **7.000–10.000 habitantes** para la **ciudad de Syvaris** (opción B, `DAR-D08-01`); documentación fuente `D08_RESOLUCION_DAR-D08-01_SYVARIS_2026-10-22.md`. No se equipara población urbana e insular. Se mantiene el total territorial como UNKNOWN y las fichas previas de Treihord/Veldora/Taramin sin alterar. El presente informe del 21/10 es histórico: el nuevo HEAD exige CI adicional en Windows y Linux. D08 sigue exclusivamente documental/estático. PR #34 Draft sin fusionar.

## Cuarta adenda autoral — Total territorial (22/10/2026)
El autor ha aprobado **DAR-D08-01 total Casa Darovan B: 300.000–450.000 habitantes**. Acta `D08_RESOLUCION_DAR-D08-01_TOTAL_DAROVAN_2026-10-22.md`. El rango incorpora ciudades y habitantes rurales e insulares de Darovan; no representa el reino Norgard ni la isla Syvaris aislada. Los censos exactos, distribución y la población de asentamientos no definidos permanecen nulos. La anterior mención del total como UNKNOWN es histórica: continúa desconocido el **censo puntual**, ya no el intervalo autoral. No ejecutar `PopulationRecord` ni crear asentamientos. CI correspondiente al nuevo HEAD obligatoria; anteriores runs no validan el incremento. PR #34 Draft sin fusionar.

## Quinta adenda autoral — Hogares urbanos (22/10/2026)
La aprobación **DAR-D08-02 opción B** fija **3–5 personas por hogar urbano, como rango de media urbana**. Acta `D08_RESOLUCION_DAR-D08-02_HOGARES_URBANOS_2026-10-22.md`. La propiedad nueva no es un censo ni un rango normativo por vivienda; hogar y familia siguen conceptos independientes. Los promedios rurales y territoriales, medias exactas, cantidades de hogares y viviendas, y edades continúan desconocidos. Cualquier afirmación histórica anterior de ausencia de datos de tamaño medio queda matizada por esta aprobación urbana. CI del HEAD con estos cambios es imprescindible; D08 sigue documental y PR #34 no fusionada.

## Adenda de cierre documental autoral — 22/10/2026 (sujeta a CI final)
Aprobadas en un lote las cinco elecciones de `D08_RESOLUCION_LOTE_FINAL_2026-10-22.md`: hogar rural B (media 4–6), edades 1B (30/60/10), 2C (sin perfiles de edad cuantificados por campo/ciudad, ni suponer igualdad), urbano/rural 3C (35–45 % / 55–65 %) y política 4A (nada singular nuevo en D08). Cierre de **decisiones de canon general D08**; persisten incógnitas para la materialización futura. Los cuatro núcleos canónicos no agotan el reparto urbano: brecha documental identificada, sin asentamientos nuevos. Datos de planificación, esquema y validador ampliados con **36 negativos nuevos** (125 en D08). Los resultados de CI antiguos no validan el presente HEAD; antes de dar D08 por verificable exigir Windows/Linux en el SHA de este lote. PR #34 Draft sin fusionar, D09–D11 no iniciadas. Una aprobación de fusión sigue siendo decisión separada del autor.

## Incidencia técnica y corrección de validación — 22/10/2026
El primer workflow del lote final, [run #39766738468](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/39766738468), falló únicamente al ejecutar las pruebas negativas D08: una mutación heredada intentaba eliminar el nombre de incógnita antiguo `rural_mean_household_size_range`, ya correctamente sustituido tras aprobar el rango rural. Python lanzó `ValueError: list.remove(x): x not in list` **fuera del bloque de capturas esperado**. Se corrige el test para comprobar la nueva incógnita vigente `rural_mean_household_size_exact`. No se cambia ninguna decisión de canon, esquema, modelo o materialización. Hace falta CI de nuevo HEAD antes de considerar la entrega válida.

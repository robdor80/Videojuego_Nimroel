# E14 — Acta de alcance, auditoría y condiciones de fusión
**Estado editorial: CERTIFICADA Y FUSIONADA el 13/11/2026.** Certificación exclusivamente documental, contractual y C++ sintética; no certifica parcelas reales ni integración jugable.

## Pruebas de aceptación H01–H10
| Puerta | Evidencia exigida |
|---|---|
| H01 | 7 IDs E01/E13 íntegros; U7 NON_EVALUABLE |
| H02 | Dorth/Lumina/Karsath/Rodas/Hallheim y autoridad intactos |
| H03 | EDD-01 y EDD-02 abiertos; norte sin cierre, CRS nulo |
| H04 | cero viña boreal automática; Karsath no es ribera verificada |
| H05 | sin tala/uso ni vivienda en bosque protegido sin títulos |
| H06 | sin inventar carretera, cauce, puente ni permiso a partir de aptitud |
| H07 | 10 riesgos E13 con cadena causal y ausencia de incidentes asumidos |
| H08 | 24 alternativas de uso y 18 vetos de U1–U6, U7 ninguna |
| H09 | contratos y pruebas contra E01, E06, E07, E08, E13 y mutaciones negativas |
| H10 | JSON no-runtime y ningún resultado jugable Godot/CoreRPG declarado |

## Auditoría de suficiencia
Las 24 alternativas son un repertorio espacial y económico por estudiar, no un mapa aprobado. Ninguna parcela tiene geometría, suelo certificado, título, paso, población o actividad ejecutada. La evaluación se mantiene a nivel de **contrato + laboratorio sintético**, distinta de las pruebas C++ E11 heredadas. Se conserva el E13 ya certificado y se repiten sus validadores en CI de E14.

**Prohibición transversal:** alterar E00–E13, el SHA lock E11 o canon superior; cambiar Rodas, inventar vecinos o importar clima/censo/cotas Darovan/Valrik; dar por aprobados usos a partir de puntuación. Revisar diff y SHA antes de fusionar. Si CI falla, mantener PR Draft.

## Acta de certificación final · 13/11/2026
- **PR E14:** [#78](https://github.com/robdor80/Videojuego_Nimroel/pull/78), 13 archivos nuevos auditados y ninguna edición a E00–E13, Canon, otras Casas, Game, CoreRPG o ContentPacks.
- **HEAD exacto de la prueba:** `df081fae19aa73109db6e7d4334ec297953d4876`.
- **CI E14:** [run #43497085374](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/43497085374), **SUCCESS** en Ubuntu 24.04 y Windows 2022. En ambos: regresiones E00–E10, E12 y E13, contratos E11 con CoreRPG fijado, C++20 consumidor y CTest **1/1 PASS**.
- **Validador E14:** **177 pruebas sintéticas de prerrequisitos + 57 mutaciones contractuales adversariales rechazadas** en ambos sistemas; seis unidades con cuatro alternativas y tres negativos cada una; U7 no evaluable, diez riesgos sin incidentes activados, cinco anclas protegidas.
- **Regresión asociada al HEAD probado:** **15/15 workflows GitHub Actions SUCCESS** para la PR (incluidos workflows históricos E00–E13 y el nuevo E14).
- **Auditoría de diff y main:** 13 archivos acotados a `E14/`, índice E14, JSON E14, `Tools/EdranorE14` y workflow; `main` base `efc94a7c48f89925acb140ad90f5c1ac034dc244` sin deriva antes de fusionar.
- **Fusión:** PR #78 fusionada con squash `37354a6331bf67b7cfd13af8eba86edff26298da`, comprobado como HEAD de `main` al cierre de la PR.

**Alcance:** documentación y laboratorio puro probados, **no** plano, parcela, censo, permiso, edificio, camino, drenaje local, servicio físico ni secuencia de Godot/World State. Se mantienen **EDD-01/02/03/04/05/07/08 ABIERTAS**; EDD-06 Rodas **RESOLVED_FOR_DESIGN**. Fase E15 no iniciada.

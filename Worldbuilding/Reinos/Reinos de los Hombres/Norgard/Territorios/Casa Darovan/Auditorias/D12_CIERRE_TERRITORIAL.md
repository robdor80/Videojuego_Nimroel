# D12 — Acta de cierre territorial de Casa Darovan
**Fecha de inicio:** 25/10/2026. **Naturaleza:** auditoría documental y técnica, no aprobación creativa.
**Dictamen técnico A:** FAVORABLE para cierre documental y técnico territorial, con reservas explícitas y sin fusión automática. **No significa Darovan jugable**. Se requiere autorización del autor para fusionar la PR.

## A. ¿Puede cerrarse el ciclo documental D00–D12?
**Dictamen técnico favorable tras primera CI integral:** Los datos y contratos de D00–D11 constituyen una base territorial coherente, con once fuentes congeladas, decisiones autorales conservadas, cuatro ciudades manuales, protección hidrográfica y límites de simulación declarados. Para recomendar cierre documental/técnico D12 sin reservas críticas debe superarse íntegramente D01–D12 en Windows/Linux, incluidas pruebas C++ D11, y quedar resuelta cualquier nueva incidencia crítica.

No se afirma que todas las incertidumbres de canon estén resueltas, que el terreno esté cartografiado a escala verificable ni que el territorio sea jugable.

## B. ¿Está preparado para integración jugable?
**Sí como base de autoría y catálogo**, no como juego funcionando. Aprovechables: cinco definiciones y referencias CoreRPG, locks de D00–D10, datos cualitativos D01–D10, ocho escenarios de especificación. **Pendientes:** subsistemas de recursos, hogares, movimiento, gobierno/fiscalidad, reloj/eventos, autonomía NPC y adaptador del Host. Se exige ejecución real y nuevas pruebas físicas MSI y Samsung Tab S9+ antes de afirmar materialización jugable.

## C. ¿Existen bloqueos del autor?
**No hay constancia de un bloqueo autoral que obligue a inventar canon para cerrar la documentación cualitativa.** Sí hay reservas para la ejecución: DAR-P04 (cartografía), resto de P08 (hidrografía), P09 (clima/suelos), P10 (explotaciones), P11 (logística/volúmenes), personas y competencias individuales D09, detalle de ciudad D07, censos D08, cultura Arven D10. Mantener UNKNOWN o PROPOSAL_PENDING_AUTHOR donde corresponda es una decisión conservadora válida; para aprobar escenas, rutas, personas o hechos nuevos se consultará al autor.

## Prohibiciones de cierre artificial
- No confundir SUCCESS de Python o catálogo C++ con simulación de reglas económicas, sociales, diplomáticas, geográficas o de combate.
- No convertir T01–T08 TEST_ONLY en acontecimientos del mundo.
- No editar el canon de fases históricas para hacer pasar pruebas.
- No fusionar PR ni borrar la rama D12 sin autorización expresa.
- No abrir automáticamente D13, una fase de CoreRPG o de Nimroel.

## Resultado y trazabilidad
**Evidencia de validación inicial de la PR #38:** [GitHub Actions #40178146688](https://github.com/robdor80/Videojuego_Nimroel/actions/runs/40178146688), HEAD `71fdb5b44bb5c83056cf21dd3a7d841e148b6df6`, SUCCESS en Windows 2022 y Ubuntu 24.04. Se leyeron automáticamente 162 archivos territoriales (131 MD, 19 JSON), se verificaron 282 referencias de fuente y se rechazaron 17 mutaciones negativas D12. Regresiones D01–D11 y validación del contrato CoreRPG superadas; 23 negativas D11 rechazadas; C++ y CTest D11 superados en ambos sistemas operativos.
**Condición administrativa final:** este acta describe el resultado probado en el HEAD indicado; tras cualquier commit posterior, debe existir nuevo CI SUCCESS sobre el HEAD definitivo. La PR conservará en su descripción el enlace a esa CI. NO constituye permiso del autor para fusionar.

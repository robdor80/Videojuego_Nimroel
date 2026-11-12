# Casa Edranor — Plan de desarrollo E00–E12
**Inicio aprobado:** 12/11/2026. **Política:** una fase, conversación, rama y PR; fusionar solo por aprobación del autor. Cada fase separa canon de propuesta y no proclama implementación de motor a partir de JSON.

| Fase | Ámbito | Salida exigible |
|---|---|---|
| **E00** | Auditoría, identidad, perímetro rojo, Rodas | Fuentes, atlas, plan, herencia, JSON no-runtime, validación, acta y traspaso |
| **E01** | Límites físicos y relieve | Unidades cualitativas oeste/centro/este/norte, vertientes y corredores, sin cotas ficticias |
| **E02** | Hidrología y drenaje | Cursos sustentados, divisorias y cuencas, agua de uso vinícola, `UNKNOWN` explícitos |
| **E03** | Clima, suelos y ecosistemas | Franja polar/boreal, zonas cultivables no uniformes, riesgos climáticos |
| **E04** | Economía y viticultura | Ciclo uva-vino-bodega-comercio, tonelería Bosque Alto, redes productivas |
| **E05** | Caminos y comunicaciones | Grafo Dorth–Lumina–Karsath y accesos a Rodas con jurisdicción real separada |
| **E06** | Asentamientos ordinarios | Arquetipos, elegibilidad y semillas, nunca sobre los cuatro lugares protegidos |
| **E07** | Dorth, Lumina, Karsath y Rodas | Diseño manual de los tres núcleos Edranor y aldea real; resolver escala editorial de Rodas |
| **E08** | Hogares, población y servicios | Núcleos sociales y empleo vinculados a producción, sin cifras tomadas de otras Casas |
| **E09** | Administración, justicia, impuestos y seguridad | Competencias Edranor/Corona, Guardia de Casa y fuerzas, E4/E5/E8/E9 |
| **E10** | Historia, cultura, personajes y conflictos | Señor y herederos, origen del señorío, costumbres, desarrollo diplomático de Rodas |
| **E11** | Integración contractual y pruebas | Stable IDs, Content Pack, regresión, validación de motor **solo si realmente ejecutada** |
| **E12** | Auditoría y cierre territorial | Comparación exhaustiva, deuda y acta de cierre; aprobación humana |

## Mecanismos y puertas comunes
1. Al entrar en cada fase: comprobar `main`, PR previa, canones e instrucciones; nunca suponer merges.
2. Heredar `Nimroel Core → Norgard Defaults → Casa Edranor → Localidad → World State`.
3. Identificar `CANON_REPO`, `AUTOR_2026_11_12`, `OBSERVACION_MAPA`, `PROPUESTA`, `UNKNOWN`.
4. IDs estables y espacios de nombres por capa; no copiar activos de Valrik/Treskal/Darovan ni una supuesta economía común de vino para el norte.
5. Protección inalterable: Dorth, Lumina, Karsath, Rodas, Hallheim. Los cuatro primeros figuran en el recorte, pero Rodas es REAL y Hallheim queda fuera.
6. Cada fase documentará fuentes, datos de planificación si proceden, pruebas, límites de verificabilidad, acta y traspaso, sin iniciar la siguiente.
7. Sin acreditación de gameplay, Godot o CoreRPG por pruebas meramente estáticas.

## Bloqueos para fases siguientes (no bloquean E00)
`EDD-01` cierre septentrional de la línea roja; `EDD-02` escala real y georreferenciación; `EDD-03` cursos y lagos; `EDD-04` censos; `EDD-05` líder/heredero/historia; `EDD-06` aldea vs ciudad Rodas en manuscrito; `EDD-07` rutas y accesos; `EDD-08` cronología de pretensiones sobre Rodas.

**E01 no se ejecuta aquí.** Si E00 sigue como PR, E01 no puede nacer de una `main` que carezca de este trabajo salvo nueva autorización expresa.

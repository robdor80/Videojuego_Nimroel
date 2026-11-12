# D.P25 — Personajes relevantes, relaciones y conflictos territoriales de Darovan

**12/11/2026 · Selección creativa aprobada por delegación expresa del autor · AUTORÍA EDITORIAL, no simulación.** Esta fase no crea NPC en WorldState, familias jurídicas, misiones, lugares físicos, registros judiciales, contratos, caravanas, puentes ni rutas.

## Situación y dependencias verdaderas
- Base Git: `main` en `512434957f248f2513761615a9685ddd6c49c65f`, posterior a D.P22/PR #45 fusionada.
- D.P23 Treihord: **PR Draft #46**, HEAD `6ee4f4a672a138e29feefb558e41bbf10fbce64e`, no fusionada al crear esta fase.
- D.P24 vida rural: **PR Draft #47**, HEAD `b0b14db66f1cf1ca0e9eb27f28cde403e3e16a89`, no fusionada al crear esta fase.
- D.P25 trabaja en una **rama independiente** para no incorporar implícitamente #46 ni #47. **Bloqueo de merge:** resolver #46 y #47 primero; volver a comparar biografías, IDs y conflictos con sus versiones fusionadas. La validación local certifica solo consistencia documental; no certifica disponibilidad futura de esas ramas ni funcionamiento en Android.
- Autoridad textual: Proyecto Maestro Nimroel → Norgard/D00–D12/D.P13 → cuatro ciudades; para Treihord prevalece el manuscrito original sobre D.P23; la capa rural de D.P24 es objetivo editorial, no nueve asentamientos acreditados.

## Alcance entregado
1. [01 — Reparto territorial y relevancia](01_reparto_y_relevancia_territorial.md): **27 protagonistas editoriales seleccionados de 52 biografías** existentes/propuestas; no duplicación de historias.
2. [02 — Red de relaciones y hogares](02_red_de_relaciones_y_hogares.md): **30 aristas dirigibles** entre personas, vínculos condicionales, privacidad y familias sin genealogías inventadas.
3. [03 — Diez conflictos territoriales](03_conflictos_y_cadenas_causales.md): causalidad, competencias, desencadenantes, recursos y desenlaces no obligatorios.
4. [04 — Poderes, justicia y mediación](04_poderes_y_justicia.md): Corona, Casa, oficios, ciudadanos y garantías.
5. [05 — Diez pruebas narrativas multirrol](05_escenas_multirrol_y_memoria.md): TEST_ONLY, con perspectiva, información y rechazos legítimos.
6. [06 — Contrato futuro para CoreRPG](06_contratos_y_materializacion.md): relaciones asimétricas persistentes, información y actos verificables.
7. [07 — Decisiones delegadas](07_decisiones_editoriales.md): ocho decisiones creativas y límites del permiso.
8. [08 — Auditoría y entrega a D.P26](08_auditoria_y_deuda.md): fuentes, dependencias y pruebas negativas.
9. [Inventario JSON D.P25](../../Datos%20operativos/darovan_dp25_personajes_relaciones_conflictos_v0.1.json); validador `Tools/DarovanDP25/validate.py`; CI `.github/workflows/darovan-dp25.yml` en Ubuntu y Windows.

## Premisa
**Un conflicto territorial no es un acontecimiento inevitable y una relación literaria no es una relación activa.** Los personajes canónicos importantes son autorales, no procedurales; el motor CoreRPG gestiona su estado. La IA interpreta a las personas, pero no inventa su posición, sus recuerdos conocidos, relaciones, inventarios o derechos.

Los 52 perfiles fuente son **diez Veldora + diez Taramin + diez Syvaris + diez Treihord + doce rurales**. D.P25 destaca 27 por su capacidad de articular distintos conflictos, **sin descartar ni rebajar** los otros 25. Los cinco orígenes conservan sus IDs previos y el carácter editorial. No se crea ni confirma Lord/Lady Darovan, familia noble, mando regio, cargo militar, parentesco, hogar o empresa nueva.

## Invariantes
Cuatro ciudades Treihord/Veldora/Taramin/Syvaris; Karsath queda fuera. Treihord ~32.000 y ocho barrios intactos, Belara contiguo, barcaza industrial somera, El Crisol sin ceca, La Vena custodiada, Justicia del Rey también en La Costra. Veldora: puerto exterior, aduana de Corona; vínculo terrestre **cualitativo** Veldora–Treihord, sin geometría. Taramin: un Thalen con dos brazos, un bosque al sur, rutas y cruces desconocidos. Syvaris: Armada **Real** de Norgard, no privada Darovan. Arven Darovan, Manto Verde ~90 %, **ningún ferry acreditado**. Los Pilares, un único bosque; Bosque de las Agujas, sin aldeas permanentes interiores. Sin aduanas internas, ceca nueva ni carreteras, fuentes, minas o convoyes inventados.

## Estados editoriales
`AUTHORED_EXISTING`: canon previo verificable. `AUTHORED_EDITORIAL_SELECTED`: selección creativa D.P25 que mantiene fuente y biografía, no hecho del mundo. `FUTURE_CONDITIONAL_RELATION`, `FUTURE_CONDITIONAL_CONFLICT`: diseño pendiente de evidencia y ejecución. `TEST_ONLY`: simulación literaria sin consecuencias. `UNKNOWN`: dato `null`, nunca se sustituye por una conjetura. La aprobación creativa no es permiso de fusionar.

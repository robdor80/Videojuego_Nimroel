# D.P20 — Veldora, ciudad mercantil vivida

**Fecha:** 11/11/2026 · **Estado:** APROBACIÓN PARCIAL (DAR-DP20-01 A: nombres populares; DAR-DP20-02 B: personalidad tradicional y gremial; DAR-DP20-03 B: doce establecimientos previstos; DAR-DP20-04 A: diez biografías base; DAR-DP20-05 A: cuatro recuerdos personales); decisiones 06–08 pendientes · **Integración en CoreRPG/Godot:** NO.

Este paquete desarrolla Veldora **como ciudad singular**, no como plantilla de puertos ni ampliación automática de D.P16. Su materia prima es el canon de Norgard/D07–D10 y D.P13, y el anteproyecto D.P16. La PR aporta autoría urbana, negocios, personas posibles, relaciones, escenas y obligaciones de implementación; **integra al canon seis nombres populares, el carácter cultural, doce objetivos futuros de establecimientos, diez biografías base y cuatro recuerdos personales; las instancias físicas de personas y locales, la geometría y los conflictos jugables siguen pendientes**.

## Lectura recomendada

1. [01 — La ciudad y sus seis ámbitos candidatos](01_ciudad_y_tejidos_urbanos.md): identidad espacial, recorridos dramáticos y vida de calle.
2. [02 — Lugares, casas, talleres y establecimientos](02_lugares_oficios_y_establecimientos.md): doce propuestas enlazadas y sus restricciones.
3. [03 — Ritmos cotidianos, economía e instituciones](03_vida_cotidiana_y_cadenas_materiales.md): qué cambia durante una jornada y por qué.
4. [04 — Personas y relaciones](04_personajes_hogares_y_relaciones.md): diez individuos **propuestos**, no arquetipos clonados.
5. [05 — Historia local, relatos y episodios](05_memoria_urbana_y_conflictos.md): conflictos entrelazados y memoria persistente.
6. [06 — Escenas jugables desde varios puntos de vista](06_escenas_y_ramas_de_decision.md): pruebas literarias de Veldora y sus desenlaces.
7. [07 — Cartografía y futuro motor](07_cartografia_contratos_y_cierre.md): lo que falta para un entorno real y verificaciones.
8. [08 — Resoluciones reservadas al autor](08_decisiones_autorales.md): paquete listo para aprobar, corregir o rechazar sin canonizar supuestos.

**Registro técnico:** [Datos operativos/darovan_dp20_veldora_proposals_v0.1.json](../../Datos%20operativos/darovan_dp20_veldora_proposals_v0.1.json). El esquema es un inventario editorial no ejecutable. Validación estática: Tools/DarovanDP20/validate.py y CI Windows/Linux.

## Anclas inmutables de Veldora

- **AUTHORED:** principal puerto mercante exterior de Norgard, Golfo de Veldora; 29.000–35.000 habitantes como **intervalo**, no censo; cota urbana general 0–60 m, no callejero.
- **AUTHORED:** crecimiento mercantil orgánico; **varios sectores comerciales** aprobados en DAR-D07-01 opción B, no bazar único; piedra y madera, teja, calle empedrada, dos plantas comunes y algunas tres; zonas acomodadas más apartadas de muelles.
- **AUTHORED:** puerto, almacenes, gremios y talleres; **aduana exterior de la Corona** con apoyo de la Casa; no aduanas entre Casas.
- **AUTHORED:** río Veldora independiente de Belara/Lhera; no se deducen puentes, bocas, navegación ni muelles de río. La gran isla boscosa de la referencia visual no se identifica automáticamente con Arven.
- **AUTHORED:** vínculo terrestre cualitativo Veldora–Treihord; sin trayecto, duración, puente, peaje ni establecimientos intermedios acreditados.
- **AUTHORED (DAR-DP20-01 A):** «Borde de las Marcas», «Patios de la Cuenta», «Calles del Trato», «Patios del Oficio», «Tejas Serenas», «Vuelta del Camino», seis denominaciones populares superponibles, **no barrios administrativos ni polígonos delimitados**.
- **AUTHORED (DAR-DP20-02 B):** personalidad cultural **predominantemente tradicional y gremial** (redes familiares, oficios, artesanía, reputación heredada), compatible con el puerto mercante exterior. No se aprueban gremios, privilegios o leyes nuevos.
- **AUTHORED_FUTURE_OBJECTIVE (DAR-DP20-03 B):** los doce nombres y funciones de establecimientos VEL-L01–VEL-L12 son objetivos futuros. **No** hay locales activos, coordenadas, parcelas, propietarios, inventarios ni recursos creados.
- **AUTHORED_BIOGRAPHY_BASE (DAR-DP20-04 A):** diez nombres, roles y biografías VEL-N01–VEL-N10 aprobados como base canónica para futuros NPC. **No** se crean personas, hogares, parentescos, EntityId, inventarios, relaciones activas ni ubicaciones.
- **AUTHORED_PERSONAL_MEMORY (DAR-DP20-05 A):** M1 promesa incompleta (Liria), M2 error de copia (Edris), M3 reparación apresurada (Naia), M4 ración prestada (Fenra). Son **recuerdos privados**, sin fechas, crónicas públicas ni sucesos de WorldState.

## Semántica de autoridad

**AUTHORED** = reconocido en fuentes existentes. **AUTHORED_FUTURE_OBJECTIVE** = compromiso editorial aprobado para desarrollo posterior, sin afirmar existencia física. **AUTHORED_BIOGRAPHY_BASE** = nombre, rol y biografía aprobados para futuro NPC, sin entidad ni vida simulada. **AUTHORED_PERSONAL_MEMORY** = antecedente biográfico íntimo aprobado, sin suceso público ni evento en WorldState. **DERIVED_CONDITIONAL** = consecuencia posible si existen recursos, permisos y contexto. **PROPOSAL_PENDING_AUTHOR** = creación nueva que el autor debe aceptar antes de ingresar al canon. **TEST_ONLY** = escena hipotética que nunca entra en WorldState.

No hay calles, establecimientos, NPC, barcos, cantidades, contratos ni cronologías nuevos ejecutados. La IA no puede usar estas propuestas como evidencia de presencia real. Esta fase tampoco declara que los siete bloques P18-G01/G09/G10/cartografía/rutas estén resueltos. El objetivo de D.P20 es **autoría profunda comprobable**, no fingir un mapa o una simulación.

**Siguiente etapa, no iniciada aquí:** D.P21 Taramin. D.P25 podrá cruzar personajes de las cuatro ciudades solo con canon aprobado.

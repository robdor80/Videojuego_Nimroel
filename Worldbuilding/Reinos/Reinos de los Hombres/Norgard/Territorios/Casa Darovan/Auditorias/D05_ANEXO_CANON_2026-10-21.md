# D05 — Anexo de canon aprobado y auditoría documental (21-10-2026)

**Alcance:** incorporar las decisiones expresas del autor sobre Arven y los ríos, corrigiendo incongruencias geográficas detectadas en la verificación visual, sin abrir D06 ni cambiar CoreRPG/Godot ni `main`.

## Resolución del autor



### Anexo canónico aprobado por el autor — 21/10/2026

Las referencias de esta fase que afirmaban **Arven UNKNOWN**, **cuatro ríos** o **río Veldora no identificado** son históricas y se sustituyen por esta decisión expresa del autor:

- **DAR-P01 RESUELTA:** Arven pertenece formalmente a Casa Darovan. No se autoriza por ello puerto, travesía o ruta comercial nueva.
- **DAR-P07 RESUELTA:** el cauce verde junto al sur de Veldora es el **río Veldora**, independiente del sistema Belara/Lhera.
- **DAR-P08 PARCIALMENTE RESUELTA:** cinco ríos nombrados según flechas del mapa confirmado: **Belara** (azul, río principal desde el norte y junto a Treihord), **Lhera** (rojo, rama del Belara hasta el litoral al norte de Veldora), **Veldora** (verde), **Fhalion** (amarillo, nuevo río menor al sur del Veldora), **Thalen** (violeta, al otro lado de las montañas con dos brazos finales alrededor de Taramin). **Cuatro sistemas hidrográficos:** Belara/Lhera, Veldora, Fhalion, Thalen.
- **DAR-P04 aún abierta:** la escala gráfica de **400 millas** aportada por el autor no constituye levantamiento topográfico verificado. Nacimientos exactos, caudales, cotas, recorridos métricos, bifurcación Belara/Lhera, desembocadura precisa del Fhalion, puentes, vados, navegación y accesos siguen pendientes. No deducir rutas a Arven o por Fhalion.

**Corrección retroactiva de las referencias documentales D01–D05, no una reapertura de sus implementaciones ni runtime.** El grafo D02 pasa a 5 ríos / 4 redes / 15 nodos / 11 enlaces topológicos simbólicos, manteniendo D05 sus 17 nodos logísticos y 3 conexiones modales acreditadas. Los hitos documentados anteriormente permanecen como actas de lo que se sabía en aquella fecha.


## Evidencia y límites

El autor aportó una captura del mapa y asignó un color a cada curso, confirmó el nombre **Fhalion** para el río amarillo y asignó Arven a Darovan. Los documentos canónicos de Norgard ya diferenciaban Belara, Lhera, Veldora y Thalen. La corrección elimina la lectura equivocada que hacía de Fhalion el supuesto segundo brazo del Thalen. **Las etiquetas no constituyen geometría GIS ni autorizan ruta navegable.**

Se actualizan las fuentes `Norgard/Geografía/rios_y_lagos.md` y `mares_y_costas.md`, datos operativos D01–D05 y validadores de todas las fases. Los estados de cierre históricos son verificaciones de su momento, no declaraciones permanentes de que Arven siga sin dueño. El cambio respeta las cuatro ciudades canónicas y el carruaje y la barcaza industrial preexistentes.

## Pruebas de cierre

Ejecutar el workflow `Darovan static regression D01-D05` en Windows y Ubuntu para el HEAD final de la PR #30. Verificar D02 cinco ríos y cuatro redes, 15 nodos, 11 aristas; D05 Arven Casa Darovan, Fhalion sin navegabilidad ni enlace nuevo y 17 nodos. Toda comprobación es **estática / NO RUNTIME**.

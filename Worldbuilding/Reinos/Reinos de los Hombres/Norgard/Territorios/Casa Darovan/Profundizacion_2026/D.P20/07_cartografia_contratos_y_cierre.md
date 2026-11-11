# D.P20 — Veldora: puertas de cartografía, integración y aceptación

**Estado:** especificación de futura producción, **sin malla de terreno, callejero ni runtime**. P18-G01, G07, G09, G10 y G12 continúan abiertos en su dimensión material/autoría hasta resolución efectiva. La calidad de esta entrega no se mide por fingir polígonos.

## Qué tenemos y qué falta

**Anclado en fuentes:** ciudad frente al Golfo de Veldora; actividad marítima principal del Reino; río Veldora distinto de Lhera y Fhalion; bosque/montañas de fondo y gran isla de referencia visual; núcleo a 0–60 m de referencia; varios sectores comerciales orgánicos; sectores acomodados apartados de muelles; carretera cualitativa a Treihord.

**No anclado:** orientación/longitud de la línea costera, huella del puerto, profundidad de aguas, mareas, cauces precisos, geometría de islas, puntos de entrada, plazas, barrios, puentes, elevación de cada calle, parcelas, capacidad de almacenes, edificios, itinerarios, distancias y tiempos. El catálogo D11 tiene una **identidad de ciudad**, no un mapa navegable.

## Tres escalas distintas

1. **Escala territorial:** D01–D.P13 gobierna relieve y aguas, sin convertir bandas altitudinales en un DEM. Una flecha en el mapa del autor no es una carretera transitable.
2. **Escala urbana de autoría:** seis ámbitos candidatos U01–U06, doce lugares L01–L12 y diez personajes N01–N10 explican **qué debería existir si se aprueba**, no dónde.
3. **Escala operativa de CoreRPG/Godot:** EntityId, coordenada validada, propiedad, ocupación y conexiones reales deberán llegar de sistemas futuros; la escena usa estas entidades, nunca crea recursos que falten.

## Propuesta de orden de cartografía, sin ejecutar

**G1.** Bloquear fuentes y versión del mapa, resolver escala y proyección autorizadas. **G2.** Levantar costa/relieve y cauces sin modificar hidrología. **G3.** Delimitar el puerto marítimo que ya existe y accesibilidad segura, sin añadir muelles. **G4.** Someter a decisión oficial número/nombres/carácter de barrios, distribución comercial y emplazamiento de sectores acomodados. **G5.** Situar casas y talleres **aprobados** con derecho de ocupación, capacidad y abastecimiento. **G6.** Registrar calles/conectividad real, accesos y enlaces urbanos; conservar que camino a Treihord no aporta por sí solo kilometraje ni puntos intermedios. **G7.** Probar desplazamiento, interacción y persistencia con escenarios sintéticos. **G8.** Activar contenidos aprobados solo tras validación de motor y permisos.

Ninguno de esos pasos puede saltarse porque un documento literario describe un paseo.

## Especificación de instanciación (conceptual, no API)

Cada lugar aprobado requerirá: id canónico distinto de etiqueta mostrada; geometría/entrada si proceden; propiedad y ámbito legal; funciones; capacidad física; inventario inicial **autorizado**; rutas permitidas; contratos y acceso; eventos que modifican su estado; versión y procedencia.

Cada persona aprobada requerirá: id persistente, hogar/ocupación posibles, edad y protecciones aplicables, intereses individuales, inventarios y consentimiento, relaciones direccionales, conocimiento con fuente, rol y ámbito de autoridad, agenda sin teletransportes, eventos recordados y visibilidad.

Cada operación con un lote requerirá: id único, titular, custodio, calidad/estado, volumen real, origen declarado vs verificado, restricciones aduaneras exteriores, intentos idempotentes, transacciones atómicas y guardado. **La aduana no se ejecuta** hasta disponer de procedimientos en Core/Norgard.

## Aceptación editorial: ocho preguntas con respuesta concreta

1. ¿Reconocemos a Veldora sin llamarla «puerto genérico»? **Sí:** custodia, inspección real y comercio urbano repartido, con casos humanos.
2. ¿Se distinguen sus habitantes? **Sí como propuestas:** diez biografías distintas, obligaciones cruzadas y conocimiento acotado.
3. ¿Hay espacios para imaginar una escena? **Sí:** seis ámbitos y doce lugares con actividad propia.
4. ¿Hay contenido urbano más allá de negar inventos? **Sí:** jornadas, episodios, trabajo, casa, dinero, errores y diálogo.
5. ¿Hemos aprobado nombres, solares y personas reales? **NO:** falta resolución expresa del autor.
6. ¿Existe plano físico de Veldora con accesos? **NO:** cartografía y autoría métrica pendientes.
7. ¿Hay juego real en CoreRPG? **NO:** los textos son propuestas, no worldstate.
8. ¿Podemos comenzar D.P21 sin reabrir matrices? **Sí**, tras cierre editorial de D.P20; sin atribuir a Veldora el canon que aún no se apruebe.

## Deuda visible al cerrar esta rama

- **P18-G01:** resuelto a nivel de **opciones de autoría urbana**, no como plano/huella canónica.
- **P18-G09:** doce negocios diseñados **provisionalmente**, no proveedores instanciados.
- **P18-G10:** diez biografías **propuestas**, no NPC activos o genealogías aprobadas.
- **P18-G07/G05/G06/G11:** rutas, relieve, hidrología y medidas siguen por demostrar.
- **P18-G12:** ingeniería de CoreRPG + Godot pendiente.
- **Nueva dependencia:** aprobar U/L/N/H y decidir qué se canoniza antes de localizarlo.

**Resultado que puede certificarse con esta PR:** entrega de autoría profunda, trazabilidad del canon, validador de inventario y CI. **Resultado que NO puede certificarse:** ciudad física, simulación en vivo, población por hogar, personajes en juego o equivalencia cartográfica con Treskal.

**Siguiente fase reservada:** D.P21 Taramin. Ningún fichero D01–D12, D.P13–D.P18, ContentPacks ni CoreRPG se modifica por este paquete.

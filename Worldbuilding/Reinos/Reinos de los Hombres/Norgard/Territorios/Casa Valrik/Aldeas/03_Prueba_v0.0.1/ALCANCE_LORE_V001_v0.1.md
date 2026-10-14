# Cierre de lore específico — Nimroel RPG v0.0.1

**Estado:** CERRADO PARA PREPARAR LA PRUEBA. La implementación no está certificada.
**Alcance:** solo la primera aldea V1 del territorio de Treskal; no implica cierre del resto de Norgard ni de Treskal ciudad.

## 1. Premisa aprobada

Un viajero sin biografía, clase, reputación o misión principal impuesta llega por un camino rural próximo a una aldea ordinaria del territorio administrado por la Casa Valrik. Su identidad jugable podrá elegirse en otra capa; esta prueba no añade trasfondo obligatorio. El jugador descubre a las personas y servicios por exploración.

La aldea deriva del **modelo V1 mixto maderero-agrícola**. Para el primer ensayo se utiliza la referencia orientativa V1 de **40–60 habitantes**, siempre dentro del rango general canónico de aldeas **35–100**. Es una selección de alcance de la prueba, no un límite nuevo de todas las V1.

Se conserva agricultura, ganadería local e influencia perceptible de una ruta maderera; no se inventa una aldea fortificada, un aserradero formal, una ciudad miniaturizada ni una guarnición fija por defecto.

## 2. Lo que existe necesariamente

- Viviendas domésticas suficientes para los hogares realmente generados.
- Agua potable funcional y accesible, sin imponer un pozo único.
- Base de subsistencia rural, áreas auxiliares proporcionales, punto de reunión y al menos una vía de salida.
- **Taberna local** o espacio vecinal equivalente; no se convierte automáticamente en posada.
- **Capacidad local de herrería básica**, aunque el titular combine oficios; maestría excepcional no obligatoria.
- Habitantes con identidad estable y pertenencia a hogares coherentes; los detalles de personalidad, memoria y vínculos dependen de sus respectivos contratos y de las capacidades efectivamente implementadas.
- Una explotación agrícola con necesidad plausible de reparar una herramienta, un objeto individualizado y una persona que pueda solicitar ayuda; esta es una **precondición del guion de prueba**, no un requisito permanente de todas las aldeas.

## 3. Lo que sigue sujeto a generación

Población exacta dentro de la banda de prueba, hogares, nombres, familias, profesiones complementarias, habilidad del herrero, calidad o localización exacta de la taberna, fuentes de agua, plano, distribución de cultivos, corrales y viviendas. Posada, molino, carpintería, carretero y curandera **siguen siendo opcionales**.

No se fijan heroísmo del protagonista, noble linaje, nombres de la aldea, edad de NPC, salarios, monedas, cuantías, duración universal de la reparación ni probabilidad fija de servicios todavía no parametrizados.

## 4. Generación, región y persistencia

- Seguir: geografía y red regional → categoría/modelo → grafo de accesibilidad → capacidades obligatorias → servicios opcionales condicionados → corrección regional mínima → hogares/edificios/layout → persistencia.
- Si la prueba no carga toda la región, un **fixture de contexto regional explícito y versionado** aporta rutas, servicios vecinos y recursos necesarios; no debe fingirse que una tirada aislada equivale a generación regional completa.
- Derivar decisiones reproducibles de World Seed + ID estable de aldea + subsistema + versión de reglas, y claves propias cuando proceda. Los nombres visibles no constituyen IDs.
- Guardar la instancia creada y las acciones posteriores; cargar o regresar no rerolleará viviendas, personajes ni servicios.
- Para la v0.0.1 puede materializarse solo un subconjunto visible de los habitantes, manteniendo la población lógica restante sin regenerarla.

## 5. Experiencia jugable mínima

1. Llegar sin conocer el asentamiento.
2. Explorar una o más áreas conectadas y descubrir taberna, herrería y vecinos.
3. Conversar/consultar sin conocer hechos que el personaje aún no ha aprendido.
4. Encontrar de modo no obligatorio el problema de una herramienta agrícola rota.
5. Ayudar a tramitar una reparación **o** ignorar/declinar/abandonar la situación.
6. Avanzar tiempo mediante acciones verificadas y observar cambios de estado condicionados.
7. Guardar, cerrar y reanudar conservando tiempo, entidad, propiedad, encargo y progreso.

Una interacción puntual puede fallar o quedar en espera por falta de tiempo, materiales, herramientas o disponibilidad del profesional; no se fuerza un final favorable.

## 6. Autoridad de los hechos

CoreRPG, a través de sus sistemas de acciones y simulación cuando existan, autoriza y conserva hechos. Las reglas específicas Nimroel concretan cuándo una herramienta se repara, qué se consume, si un NPC está disponible y a quién pertenece el objeto. El Host 2D solo visualiza y solicita; la IA Terra/Luna, cuando se integre, narra usando un contexto de conocimiento autorizado. Ninguna frase de diálogo modifica por sí sola propiedad, estado de reparación ni tiempo.

## 7. Exclusiones de la v0.0.1

No se exige para aprobar: combate, magia, romance, sistema político completo, travesías navales, economía regional exhaustiva, cientos de ubicaciones, árboles de habilidades extensos, IA remota obligatoria, rutinas completas de la totalidad de los habitantes o assets finales NAP. Se pueden usar elementos visuales provisionales y una interacción estructurada sin IA para el primer ensayo técnico.

No introducir templos o instituciones religiosas normales, murallas, castillo, estación militar permanente ni tecnología ajena al entorno.

## 8. Significado del cierre

El **lore necesario para definir la prueba** se cierra con esta selección. No se cierran los modelos de aldeas para todas las partidas, ni se consideran implementados sus parámetros pendientes. Los valores de tuning, esquemas, algoritmos y adaptadores se concretarán en el trabajo de Content Pack e integración sin ampliar el canon por accidente.

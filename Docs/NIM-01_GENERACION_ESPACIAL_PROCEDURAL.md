# NIM-01 — generación espacial procedural y navegación lógica

**Estado:** diseño de integración propuesto para implementación; no ejecutado.
**Autoridad heredada:** metodología de asentamientos de Treskal, generación regional determinista y V1 maderera-agrícola de Worldbuilding; PR #12 define la prueba, no una aldea prefijada.
**Alcance:** documentación técnica del juego; no modifica canon ni asigna probabilidades definitivas.

## 1. Aclaración esencial

**Toda aldea ordinaria generada debe recibir también un layout/plano espacial generado proceduralmente.** No se dibujan manualmente planos para cada aldea, ni se predetermina su callejero. El layout resultante se persiste como parte de la instancia de partida.

El jugador no necesita visualizar un mapa exhaustivo. En Nimroel v0.0.1, el plano es un **modelo lógico consultable** para localizar lugares, conectar caminos, resolver movimientos, tiempos y percepciones. Los fondos 2D son una representación contextual, no un plano obligatorio ni una lista de hotspots.

El generador regional y el generador de layout aldeano son capas diferentes y coordinadas:
- **Grafo regional:** la posición de la aldea en la red, rutas, recursos, vecinos y cobertura de servicios; usa mapa/región real o un fixture explícito versionado para el ensayo.
- **Grafo/estructura interna de aldea:** conexión de entradas, caminos, agrupaciones de hogares, taberna, herrería, agua, áreas productivas, campos y lugares opcionales generados.

No usar un fixture regional pequeño para fingir que se ha generado de verdad todo el territorio.

## 2. Generación en orden coherente

1. **Contexto regional estable:** World Seed, ID estable de asentamiento, versión, grafo de caminos/costes y recursos/servicios del entorno.
2. **Modelo y capacidades:** V1, población y hogares; garantizar viviendas suficientes, agua, subsistencia, vía externa, espacio de reunión, taberna y herrería básica; resolver servicios opcionales conforme a contexto regional.
3. **Asignación de actividades y parcelas lógicas:** ubicar unidades domésticas, huertos, corrales, talleres y producción agrícola/maderera con espacios proporcionados. El número de parcelas deriva de la instancia: no introducir un catálogo fijo de aldeas.
4. **Layout procedural:** disponer caminos orgánicos, agrupaciones de casas bajas, rutas de acceso a agua, salida de carros, relación espacial con campos y ruta maderera; situar actividades ruidosas/peligrosas con separación plausible cuando corresponda.
5. **Conectividad/validación:** desde la entrada accesible deben poder alcanzarse los servicios y lugares requeridos mediante conexiones funcionales; reparar bloqueos/errores del layout con cambios mínimos deterministas y registrar las correcciones.
6. **Identidades y ocupación:** asignar IDs a localizaciones y entidades, enlazar hogares y actividades con sus nodos reales. Nombres visibles no son IDs.
7. **Persistencia:** guardar configuración inicial, seed/versiones, conexiones, ubicaciones y modificaciones posteriores; al cargar, no generar otro plano.

El orden y las relaciones deben heredar las reglas canónicas. Los algoritmos, tamaños de nodos, pesos, distancias, duraciones y clases de obstáculos son parámetros técnicos **pendientes** de concretar, no nuevo canon.

## 3. Aleatoriedad determinista y estabilidad

Claves de derivación: **World Seed + ID estable de asentamiento + subsistema + versión de reglas**, con claves propias para hogares, edificios, caminos y NPC cuando corresponda. Evitar una secuencia aleatoria global que cambie arbitrariamente todos los resultados cuando se añade un servicio.

Diferentes semillas/contextos pueden producir aldeas V1 distintas, incluidas diferencias en trazado, distribución y servicios opcionales. **La misma semilla + versiones + contexto produce la misma instancia inicial**. Una partida ya creada conserva su layout aunque cambie la versión del generador; si alguna versión exige cambios, la migración debe ser explícita.

La población lógica puede permanecer totalmente persistente sin tener sprite. Un NPC que se mueve entre ubicaciones actualiza su estado lógico, no su presencia en una ilustración.

## 4. Navegación, percepción y lenguaje natural

El módulo espacial, unido a las capacidades de conocimiento/percepción de CoreRPG cuando existan, debe responder preguntas limitadas por observador y contexto:
- «¿Qué veo desde aquí?» -> localización actual, acceso visual plausible, entorno inmediato, NPC que realmente estén presentes y señales percibibles.
- «Camino desde la entrada hacia la taberna» -> ruta por conexiones reales, si son transitables, consumo de tiempo válido y nueva ubicación tras ejecución correcta.
- «¿Dónde está la herrería?» -> el motor no revela su posición al jugador que no la conoce, aunque exista en el plano. Puede conseguir esa información al explorar o preguntar a alguien que realmente la sabe.
- «Busco a un aldeano» -> consulta/acción de búsqueda con disponibilidad, ubicación y condiciones actuales; no se crea NPC solo porque el jugador lo pide.

La implementación podrá partir de un **grafo de lugares y conexiones**, con atributos espaciales suficientes para probar rutas, alcance, proximidad y visibilidad. No exige inicialmente mallas 3D, colisiones de sprites, tilemaps ni una imagen exclusiva por edificio. Si en el futuro se necesita geometría más precisa, debe complementar los mismos IDs y estado, no reemplazarlos arbitrariamente.

Los límites de visión, duración de recorridos, obstáculos y disponibilidad no los inventa la IA: surgirán de parámetros del modelo y la simulación. La IA solo formula propuestas de consulta/acción y narra el resultado autorizado.

## 5. Representación de escenas 2D

El Host elige fondo en función de una **categoría de lugar, ambiente y condiciones visuales válidas**. Puede reutilizar una ilustración de camino rural en varias aldeas V1. El fondo no determina cuántas casas hay, dónde está la herrería o qué vecinos existen.

Durante una interacción se muestra el retrato asociado al ID persistente del NPC; si no existe retrato compatible, la identidad lógica sigue existiendo. No son necesarios hotspots obligatorios.

## 6. Fronteras de implementación

- **Nimroel específico**: generación V1, grafo interno, rutas, servicios, reglas de localización, proyecciones visuales y fixture de contexto regional.
- **CoreRPG**: autoridad estructural disponible (4.5–4.8); conocimiento/visibilidad (4.9), acciones/simulación (4.10), inspector (4.11) y contenido concreto (4.13), a integrar cuando existan.
- **Host**: representa fondo, diálogo y retrato. No conserva un segundo mundo ni inventa movimientos.
- **IA**: interpreta lenguaje natural y narra resultados; no genera geografía persistente a demanda ni mueve entidades saltándose el motor.

Los snapshots actuales de CoreRPG no garantizan por sí solos guardar la geometría ni todos los campos de dominio Nimroel. Su integración persistente requiere payloads/adaptadores versionados posteriores.

## 7. Pruebas previstas

- Múltiples semillas generan aldeas V1 con distribuciones distintas y requisitos obligatorios satisfechos.
- Misma seed + versión + fixture produce IDs, conexiones y layout inicial idénticos.
- Todos los nodos obligatorios son accesibles o registran una excepción legítima validada, sin atajos visuales.
- Devolver jugador a la aldea o recargar conserva exactamente la distribución; nunca reroll silencioso.
- Un trayecto no puede completarse por narración si no existe ruta válida.
- Lo que la IA cuenta se limita a lo que el jugador puede percibir/conocer.
- Una ilustración genérica no impide descubrir un lugar que el layout lógico contiene.
- Con más de una aldea de prueba, no hay obligación de repetir el mismo plano; la validación regional permanece separada de la local.

Relacionar evidencias con V001-G01..G06, P01..P04, S01..S06 y H03..H04 de la matriz canónica. No declarar tests aprobados hasta ejecutar código real.

**Conclusión:** procedural es tanto el contenido de la aldea como la distribución espacial de ese contenido; persistente es tanto el quién y el qué como el dónde y el cómo se conecta.

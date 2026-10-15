# NIM-01 — experiencia conversacional y presentación 2D

**Estado:** decisión de dirección jugable registrada; modelos Gemini designados por el autor; integración técnica y pruebas pendientes.
**Ámbito:** videojuego Nimroel, no nuevo canon del mundo.
**Referencia narrativa:** PR #12, aldea V1 y encargo opcional «La herramienta rota».
**Fecha de decisión:** 2026-10-14.

## 1. Intención aprobada por el autor

La experiencia no es una aventura de apuntar y hacer clic ni un mapa donde deban verse todos los objetos interactuables. La referencia es una partida de rol tradicional con Máster: el jugador **habla o escribe libremente** lo que observa, pretende hacer o desea preguntar.

- **Fondos 2D ilustrados**: ambientación del lugar o situación; no son mapas exhaustivos ni fuente de verdad.
- **Retratos 2D**: representación de interlocutores cuando se conversa; no sustituyen al NPC persistente.
- **Texto / voz**: entradas alternativas hacia un mismo flujo de intenciones; no hay obligación de seleccionar un hotspot o recorrer un mapa con un sprite.
- **IA como director narrativo e intérprete**: entiende peticiones, formula preguntas de aclaración, narra percepciones y resultados autorizados.
- **CoreRPG como árbitro**: conserva el mundo, autoriza observaciones y resuelve acciones, tiempo y consecuencias.
- **Reglas/Content Pack de Nimroel**: concretan el significado del universo sin meter el canon en CoreRPG genérico.

La modalidad conceptual es **RPG conversacional guiado por lenguaje natural con presentación 2D ilustrada**. No equivale a la antigua «opción A» de escenas conectadas mediante clics obligatorios. Las opciones visibles de ayuda pueden ofrecer accesibilidad, pero jamás constituir el único camino de interacción.

## 2. Experiencia observada

Un turno puede contener una consulta, una acción, una conversación o varios pasos que deban resolverse sucesivamente:

- «¿Qué veo desde donde estoy?» => consulta de percepción dependiente del observador, ubicación, condiciones y conocimiento.
- «Avanzo por la aldea y busco a algún aldeano» => propuesta de desplazamiento/búsqueda: el motor valida el movimiento; solo después consulta quién puede encontrarse allí.
- «¿Dónde está el herrero?» => la IA no revela datos que el jugador desconoce; puede dirigir una pregunta a un NPC, siempre que sea accesible y el NPC posea información válida.
- «Tomo el útil y se lo llevo al herrero» => acciones con custodia, permisos, transporte, disponibilidad, tiempo y resultados separados.
- «Me marcho sin ayudar» => no existe obligación de activar/completar el encargo; las actividades del mundo pueden continuar sin el jugador.

Los resultados exactos dependen de la aldea generada y del estado real de la partida. Los ejemplos no fijan NPC, profesiones adicionales, objetos, rutas ni situaciones canónicas concretas.

## 3. Canal técnico: propuesta → validación → narración

```text
Jugador (texto / voz transcrita)
    |
    v
Intérprete de intención (IA; o intérprete acotado para pruebas sin IA)
    |
    v
Propuesta tipada: consultar percepción / desplazarse / hablar / entregar / esperar...
    |
    v
Adaptador Nimroel -> CoreRPG + reglas de contenido
    |
    +--> Consulta de estado/percepción autorizada para ese personaje (sin mutación)
    |
    +--> Solicitud de acción validable; posibles múltiples pasos, con resultados reales
    |
    v
Resultados estructurados, hechos visibles, causas y límites de conocimiento
    |
    v
Narrador IA restringido al resultado y a datos autorizados
    |
    v
Host 2D: respuesta textual/audio opcional + fondo contextual + retrato pertinente
```

**Nunca** convertir la salida libre de la IA en mutación directa de WorldState. El narrador no puede inventar propiedad, reparación, tiempo avanzado, NPC aparecidos, secretos o recompensas. El contexto debe ser específico del observador. Los datos meramente atmosféricos tampoco deben contradecir el estado real.

Si la petición es ambigua, no se decide por sorpresa una acción irreversible: pedir aclaración o presentar una propuesta validable. Si la interpretación agrupa acciones, resolverlas en orden, revalidando cada resultado antes del paso siguiente; no afirmar que todas tuvieron éxito. Los fallos y límites se comunican de forma jugable, sin filtrar secretos ocultos.

## 4. Escenarios sin dependencia del píxel

La representación gráfica se elige a partir de contexto de localización, región y momento de la experiencia; puede ser general, estilizada o reutilizada por distintas instancias compatibles. El catálogo de fondos no determina qué servicios existen ni qué NPC están presentes.

**El plano de cada aldea también se genera proceduralmente**: su ubicación y conexiones regionales preceden a la generación de hogares, edificios, caminos y distribución interior; el layout resultante se persiste en la partida. No hay plano aldeano fijo ni diseño manual por instancia. El motor consulta ese grafo espacial interno para rutas, presencia, accesibilidad y, cuando se implementen reglas suficientes, visibilidad. El plano lógico no tiene por qué mostrarse al jugador ni coincidir píxel por píxel con los fondos artísticos.

Véase [NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md](NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md).

- Una taberna puede existir lógicamente aunque no aparezca en la imagen de entrada.
- Una herrería puede encontrarse mediante diálogo o exploración, sin hotspot visible.
- Los retratos se vinculan a IDs lógicos de NPC por un manifest de assets; su ausencia no borra al NPC.
- Una nueva escena ilustrada puede acompañar un cambio de lugar autorizado, sin asumir que cada lugar necesita arte exclusivo.

La UI prioriza el contexto narrativo, caja de entrada, historial de conversación y fondo; retrato durante diálogo. Controles secundarios pueden facilitar repetir, consultar historial, guardar/cargar y accesibilidad. Evitar doble autoridad de estado en GDScript o UI.

## 5. Voz, red y degradación honesta

La intención de producto admite **voz y escritura**. Los modelos de interpretación/narración elegidos previamente por el autor son **Gemini 3.5 Flash-Lite** para uso habitual y **Gemini 3.8 Flash** para tareas exigentes. La condición de uso del proyecto es disponer de un servicio gratuito en el EEE, según la decisión comunicada por el autor; esta documentación no constituye verificación independiente de disponibilidad, cuota o IDs de API. **No se abre una nueva selección comparativa de modelos en NIM-01.** La voz necesita una capa de transcripción (ASR) y, si se desea, síntesis de voz (TTS), separadas del modelo de interpretación y de CoreRPG.

La experiencia conversacional libre requiere un intérprete suficientemente capaz: el prototipo sin IA puede usar comandos de prueba o un parser acotado, **pero no debe presentarse como equivalente a la IA narradora**.

La aplicación debe poder arrancar y diagnosticar su estado sin IA remota. Esto **no** significa que el modo libre completo funcione offline: dependerá del proveedor/modelo y de lo demostrado en cada plataforma. Android debe funcionar sin PC, pero no se asume todavía IA local en Android. La disponibilidad de la narración y del reconocimiento de voz se documentará por separado.

## 6. Alcance de NIM-01 versus v0.0.1

**NIM-01 (arquitectura y arranque):**
1. Seleccionar Host 2D adecuado para panel narrativo, fondo, retrato y entradas Windows/Android.
2. Probar en Windows una pantalla de conversación con fondo contextual y retrato provisional.
3. Definir contratos de intención, consulta, resultado y presentación (como contratos Nimroel provisionales, no APIs actuales de CoreRPG).
4. Preparar test con respuestas estructuradas ficticias claramente identificadas para validar la UI, sin alterar ningún WorldState.
5. Evaluar por separado dictado/transcripción y exportación Android.
6. Mantener la PR Draft y evidenciar exactamente qué se construyó/probó.

**Después de NIM-01:**
- Generador V1 contextual, población/identidades y asignación de vistas.
- CoreRPG 4.9 para conocimiento y percepción; 4.10 para acciones/simulación.
- CoreRPG 4.12 para Context Builder; integración del intérprete/narrador real con frontera segura de resultados.
- CoreRPG 4.13 y Content Pack Nimroel para dominio de prueba.
- Validar la matriz V001 del paquete de lore antes de declarar jugable la v0.0.1.

## 7. Criterios específicos de aceptación UX (propuestos)

- No obliga a clicar edificio, persona u objeto representado en la imagen para interactuar con el mundo.
- Permite escribir una pregunta libre y presenta una respuesta basada en contexto autorizado **cuando el subsistema de IA esté integrado**.
- Permite formular intención de acción libre; el motor valida la mutación y el narrador informa del resultado.
- Nunca utiliza un retrato, un hotspot ni la selección de fondo como fuente de verdad del mundo.
- Si no hay IA, se identifica explícitamente como **modo técnico limitado**, no como modo conversacional plenamente funcional.
- Se verifican por separado entrada de texto, entrada por voz, salida narrada, lógica del Core y exportación Windows/Android.

## 8. Cuestiones técnicas por resolver, no decisiones de lore

- Framework Host 2D y API estable de integración con CoreRPG.
- Integración técnica y límites efectivos de los modelos Gemini ya elegidos, con mecanismo de control de cuotas/errores; no volver a elegir proveedor en NIM-01.
- Generación procedural del layout y navegación lógica documentadas aparte; su implementación se planifica con el generador V1.
- Alcance real del dictado y TTS en Windows y Android.
- Contratos de intents multietapa, cancelación, aclaraciones y temporización.
- Selección de fondos/retratos e integración de assets NAP existentes sin mover los originales.
- Fijar umbrales de experiencia y evidencia para declarar jugable la versión 0.0.1.

**Regla rectora:** el jugador imagina y declara; la IA interpreta y narra; CoreRPG decide y conserva. La imagen acompaña, nunca limita las posibilidades que permite el mundo.

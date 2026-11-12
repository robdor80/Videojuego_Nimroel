# NIM-08 a NIM-19 — Plan Maestro para la primera aventura jugable y la fábrica de mundos

**Fecha:** 12/11/2026. **Estado:** PLANIFICACIÓN PROPUESTA, no autorización de implementación. **Versión documental:** 1.0.
**Repositorio:** robdor80/Videojuego_Nimroel. **Base de trabajo documental:** main @ 0130ed95f27d6d450c962fa2557f56b6b569e4a0.
**CoreRPG consultado:** main @ 76a7b7b485616d8c4994f384a90f123bf333591d.
**Rama exclusiva de planificación:** plan/nim08-19-fabrica-mundos-v001-20261112.
**Alcance territorial:** una **aldea procedural V1 mixta agrícola-maderera del territorio de Treskal, Casa Valrik**; no la ciudad canónica de Treskal.

## 1. Propósito y decisión arquitectónica

**No fabricar una misión cerrada ni una aldea exclusiva de demostración.** Desarrollar una cadena reutilizable que transforme canon autorizado en reglas/Content Packs versionados, genere una instancia coherente y persistente, ejecute acciones validadas y presente sus consecuencias desde Godot 4.7.2 2D. La situación optativa «La herramienta rota» es la **prueba de aceptación integral** de esa maquinaria, no la fuente de sus reglas universales.

Cadena única:

    Worldbuilding/canon (fuente, no ejecución)
      -> selección + procedencia + normalización
      -> Content Pack declarativo + contratos de dominio
      -> generador Nimroel (semillas, contexto y reglas)
      -> CoreRPG (única autoridad de estado, acciones, conocimiento y RNG)
      -> GDExtension/Host (adaptador autorizado; sin WorldState paralelo)
      -> Godot 2D (fondos, retratos, texto, voz; nunca decide hechos)
      -> snapshot Core + metadatos versionados -> restauración sin reroll.

CoreRPG se mantiene **agnóstico de Nimroel y de Star Trek**. Las reglas específicas de aldeas, oficios y reparación pertenecen al contenido/adaptador de Nimroel; si falta una primitiva genericizable se plantea, prueba y versiona por separado en CoreRPG. No se escribirá un segundo motor mutable en GDScript ni se hará pasar una relación de contención por un trayecto, un edificio por un nodo de servicio o una narración por una reparación.

**Resultado mínimo obligatorio:** los tres itinerarios A (ayuda completa), B (reparación pendiente con continuidad) y C (indiferencia/abandono con mundo activo) del documento canónico, **en un ejecutable Windows y en APK Android**, con los criterios esenciales V001-G/P/Q/S/H realmente verificados. El juego debe funcionar mediante interfaz local sin API facturable; Sol/Luna se añaden exclusivamente bajo consentimiento y con las mismas autorizaciones de contexto.

## 2. Baseline y observaciones verificadas

- La rama histórica NIM-07 (333f7d12...) es actualmente ancestral de main (comparación GitHub: 0 commits ahead, 111 behind); sus archivos I1–I4 están presentes en main. **Esto acredita integración Git, no validación física de I4**. Volver a comprobar estado y regresiones antes de cualquier ejecución de NIM-08.
- NIM-07 cargó un Content Pack auténtico de nueve archivos, **cuatro definiciones**, una aldea de 50 habitantes declarados, dos identidades materializadas y siete entidades estructurales; I4 probó guardado/restore real con 113/113 verificaciones entre procesos, Windows CI y APK Android compilado. **No creó hogares, NPC nominales, plano, rutinas, inventario completo ni misión jugable**.
- CoreRPG main ya tiene EntityId, contención/relaciones, población latente, Knowledge/Visibility, ActionEngine/Simulation explícita, ContentCatalog/ContentJson, ContextBuilder y Persistence; el ActionOperation genérico observado solo ofrece colocar, retirar contención, añadir/quitar relación y tirar dados. **No existe una acción genérica actual de reparar herramienta, avanzar calendario laboral o ejecutar IA autónoma**.
- Los documentos normativos V001 están en Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Aldeas/03_Prueba_v0.0.1/. Sus 28 IDs de aceptación permanecen criterios, no pruebas superadas por su mera escritura.
- Política IA vigente: Docs/IA/POLITICA_MODELOS_NIMROEL_2026-10-17.md, revisión 20/10: Sol escenas/significativos, Luna NPC/consultas puntuales, ChatGPT Plus creación manual externa. Documentación V001 antigua menciona «Terra»: no introducir ese proveedor ni alterar política por inercia.
- El legado NIM-01_GENERACION_ESPACIAL_PROCEDURAL.md exige layout también procedural, grafo regional separado, IDs estables, rutas y representación 2D ilustrada, sin hotspots obligatorios.

## 3. Árbol de fases y responsabilidad

    NIM-07 [base integrada; confirmar certificación física antes del cierre formal]
       |
       +-- NIM-08  Gobierno, auditoría, contratos y vertical dorada       CHATGPT
       |      | 
       +-- NIM-09  Fábrica de contenidos canon -> paquetes              CHATGPT
       |      |
       +-- NIM-10  Generación de aldeas, edificios y layout             CODEX (ChatGPT diseña)
       |      |
       +-- NIM-11  Hogares, población, NPC y profesiones                 CODEX (ChatGPT prepara)
       |      |
       +-- NIM-12  Localizaciones, desplazamiento y percepción          CODEX (ChatGPT define)
       |      |
       +-- NIM-13  Objetos, condición, propiedad y custodia              CODEX (ChatGPT define)
       |      |
       +-- NIM-14  Tiempo, trabajos, talleres y autonomía NPC           CODEX (ChatGPT define)
       |      |
       +-- NIM-15  Conocimiento, conversaciones y descubrimiento        MIXTO (ChatGPT -> Codex)
       |      |
       +-- NIM-16  Encargo opcional «La herramienta rota»               MIXTO (ChatGPT -> Codex)
       |      |
       +-- NIM-17  Experiencia Godot 2D y narrativa opcional            MIXTO (ChatGPT -> Codex)
       |      |
       +-- NIM-18  Persistencia total, regresión y robustez             CODEX (ChatGPT audita)
       |      |
       +-- NIM-19  Certificación A/B/C y método de expansión            CHATGPT + AUTOR
       |
       +-- PILOTO POSTERIOR: segunda aldea/territorio con los MISMOS contratos;
                           si requiere código duplicado, la fábrica no está lista.

**Modelo de asignación:** ChatGPT planifica cada fase, produce contratos, fixtures, documentos y pruebas de escritorio y audita el resultado. Codex entra **solo en las subfases nativas o de integración compleja**. El propietario decide canon, gasto, publicación y merge; participa en pruebas físicas. No se obliga a Codex a investigar Lore ni a redactar materiales que puedan resolverse externamente.

## 4. Fases detalladas, incrementos y puertas de aceptación

### NIM-08 — Cimentación y contratos (responsable: ChatGPT; Codex NO)

- **P01** auditoría de main actual, NIM-07 y CoreRPG; distinguir implementado, simulado y ausente; revisar APIs/pins y dependencias de Star Trek.
- **P02** matriz contractual canónica V001 (28 casos), invariantes, fuentes y autoridad; escenario A/B/C sin fijar nombres, geografía o recompensas.
- **P03** diseño de arquitectura por capas, entidades/IDs, tipos de payload, mutaciones y rollback, diferencia Core genérico vs dominio Nimroel, secuencias de generación, reloj y persistencia. ADR de extensiones genéricas potencialmente reutilizables por Star Trek.
- **P04** descomposición en encargos Codex pequeños con criterios y aserciones; inventario de datos reutilizables, modelo de coste y puertas de riesgo.
- **Entrega:** especificaciones, mapa de dependencias, matriz de aceptación y plan con nombres versionados; **sin modificar runtime**.
- **Puerta:** ningún requisito funcional sin autoridad, destino y prueba; ninguna función CoreRPG supuesta sin comprobar.

### NIM-09 — Fábrica de contenido (responsable: ChatGPT; Codex SOLO si integración nativa lo exige)

- **P01** inventario trazable de fuentes de Valrik/Treskal V1 y contratos Nimroel Core (TOOL/COND/OWN/WAIT/TIME/MEM); localizar parámetros aprobados vs tuning técnico sin elevarlo a canon.
- **P02** contrato de proyección de fuentes a datos operativos: manifest, IDs semánticos, nombres/etiquetas, refs, hashes, fuentes, schema, versionado, normalización y errores.
- **P03** extractores/validadores y fixtures con Python u otras herramientas manejables directamente por ChatGPT, pruebas negativas, build repetible y firma de procedencia por SHA; **no se edita manualmente pack generado**.
- **P04** generar los perfiles de ejemplo V1, región técnica explícita y matriz de restricciones obligatorias/opcionales; validar que valores sin fuente sean parámetro experimental etiquetado, nunca canon.
- **Entrega:** **pipeline reproducible Canon -> Manifest -> Pack**, esquemas y generador/checkers de build, sin código específico de la misión.
- **Puerta:** misma entrada + versiones -> mismos bytes/hashes; fuente no autorizada, referencia huérfana o nueva versión sin migración => rechazo.

### NIM-10 — Aldea y layout real (responsable implementación: Codex; diseño/datos/pruebas: ChatGPT)

- **P01** contexto regional estable o fixture explícito; IDs de asentamiento, semilla derivada por subsistema y versión.
- **P02** generación V1: agua, subsistencia, camino externo, espacio comunitario, viviendas suficientes, capacidad de herrería y taberna; servicios opcionales condicionados.
- **P03** grafo de edificios/parcelas/caminos, accesos a interiores, recursos/parcelas y validación de conectividad/correcciones mínimas; no mapa fijo ni ciudad miniaturizada.
- **P04** instancia estructural autoridad Core, reglas especializadas Nimroel y aserciones deterministas en 100 semillas; traza de por qué se escogió cada valor.
- **Entrega:** **una aldea diferente por semilla**, misma por repetición, con edificios y caminos de verdad en el mundo lógico.
- **Puerta:** V001-G01..G06, incluyendo 100 semillas y ausencia de servicios falsamente obligatorios. Sin sprites obligatorios.

### NIM-11 — Población y sociedad (responsable implementación: Codex; perfiles/contratos: ChatGPT)

- **P01** hogares suficientes, personas con ID persistente, composición demográfica de instancia, vínculos familiares y pertenencias sin clonar identidades.
- **P02** perfiles de ocupación plausibles, agricultor y capacidad de herrería garantizados **como roles de generación**, oficio múltiple permitido; sin determinar nombres/sexo/edad por canon nuevo.
- **P03** ubicación inicial, acceso a vivienda, relaciones y conocimientos por observador; mecanismos de activación selectiva para población no visible.
- **P04** pruebas de consistencia ocupacional, hogares, cardinalidad, población latente vs materializada y guardados.
- **Entrega:** aldea poblada lógicamente; todos los residentes relevantes para la prueba poseen identidad estable, no un conjunto de retratos inventados.
- **Puerta:** 50 residentes de la semilla dorada contabilizados coherentemente; no afirmar que 48 latentes poseen EntityId antes de materializar; NPC de la misión reales y persistentes.

### NIM-12 — Espacio, movilidad y percepción (responsable implementación: Codex; casos: ChatGPT)

- **P01** contrato genérico de localización, grafo, interiores, permisos/accesos, origen y rutas con costes.
- **P02** acciones validadas de trasladarse/entrar/salir/buscar, actualizaciones de ubicación y tiempo; distinción contención estructural versus desplazamiento.
- **P03** proyección player-safe de vista y conocimiento: lugar/entorno/personas presentes sin revelar taberna, herrero ni ruta no descubiertos.
- **P04** navegación libre por texto o comandos accesibles; sin depender de hotspots y sin simular movimiento desde un texto narrado.
- **Entrega:** poder llegar realmente a la herrería y encontrarse o no con residentes según su estado.
- **Puerta:** V001-P01/P04 (parte espacial), rutas negativas, observador sin omnisciencia, guardado de localizaciones.

### NIM-13 — Objetos, derechos y estado material (responsable implementación: Codex; contratos: ChatGPT)

- **P01** ítem individual con ID persistente, categoría de herramienta agrícola, condición/desgaste/daño y capacidad de reparación, no una mera definición.
- **P02** propiedad, posesión, custodia autorizada, transporte, pérdida/entrega y permisos distintos; derechos no derivados de tener un ID.
- **P03** reglas de operaciones con precondiciones, resultados explicables, reversión ante fallos y actualización de conocimiento pertinente.
- **P04** pruebas de intento no autorizado, duplicación, entrega parcial, integridad y reanudación.
- **Entrega:** herramienta rota con identidad, condición y dueño/poseedor distintos cuando proceda; movimientos materiales genuinos.
- **Puerta:** V001-Q01/Q02; hablar no otorga propiedad, agarrar no implica permiso y «reparada» no es un booleano ficticio.

### NIM-14 — Tiempo, servicios y actividades autónomas (responsable implementación: Codex; reglas/fixtures: ChatGPT)

- **P01** reloj de campaña, calendario/ticks explícitos y políticas de coste temporal; **no depender de FPS**.
- **P02** capacidad del herrero, estación, insumos, cola/orden de trabajo, recursos, ocupación, disponibilidad y compromisos.
- **P03** progreso determinista condicionado, interrupción y reanudación, tareas de NPC sin sprite/escena abierta; revalidar recursos durante cada paso.
- **P04** escenarios: ocupado, taller cerrado, recurso insuficiente, pausa, progreso parcial y resultado; métricas de rendimiento y continuidad.
- **Entrega:** herrero con cola real que puede reparar solo si concurren condiciones, aunque el jugador esté en otro lugar.
- **Puerta:** V001-Q03..Q05, S03. Sin completar al cerrar app ni por tiempo de reloj real sin política aprobada: la simulación avanza por tiempo de juego autorizado.

### NIM-15 — Diálogo y conocimiento localizado (ChatGPT diseña/contenido; Codex integra)

- **P01** contrato conversación con actor, interlocutor accesible, turno, fuente, conocimiento observable, afirmación/negación/desconocimiento y testigos.
- **P02** preparación ChatGPT de recursos lingüísticos, personalidades derivables y casos de prueba, sin nombres/biografías obligatorios no canónicos.
- **P03** integración de acciones de conversación, aprendizaje/memoria, transmisión plausible y descubrimiento opcional del problema; separación clara entre decir algo y cambiar verdad física.
- **P04** pruebas cruzadas de observadores con conocimientos divergentes, NPC no testigo, ocupaciones e interrupciones.
- **Entrega:** hablar de verdad con residentes; la información depende de quién habla, qué sabe y si está disponible.
- **Puerta:** V001-P02/Q08, no spoiler, no telepatía ni cambio de WorldState por texto. **Primero modo offline determinista**.

### NIM-16 — Orquestación del encargo opcional (ChatGPT diseña; Codex integra)

- **P01** máquina narrativa de estados exacta del documento canónico: no_descubierto, descubierto, no_aceptado, rechazado, ayuda_ofrecida, entrega_pendiente, reparación_solicitada, en_espera, en_curso, pausada, reparada_pendiente_entrega, no_viable, ayuda_abandonada, resuelta. La máquina del encargo NO sustituye los contratos de objeto/orden/propiedad/tiempo.
- **P02** orquestador de objetivos/eventos derivado de hechos verificados, nunca del texto de la IA; descubrimiento espontáneo opcional y sin fuerza del guion.
- **P03** itinerarios A/B/C completos: reparación/devolución; trabajo pendiente tras regreso; ignorar/abandonar con continuidad autónoma.
- **P04** pruebas de decisiones, no-op, acciones inválidas, interrupciones, devolución real y persistencia de estados desacoplados.
- **Entrega:** primera misión totalmente funcional en un harness de lógica sin Godot.
- **Puerta:** V001-P03, Q06/Q07, itinerarios A/B/C y ausencia de «quest_completed» mágico que imponga verdad.

### NIM-17 — Experiencia en Godot 2D (ChatGPT UX/arte/diálogo; Codex integración compleja)

- **P01** ChatGPT define interfaz limpia: narración, entrada libre, historial, retrato presente, fondo por categoría autorizada, guardar/reanudar y diagnósticos separados.
- **P02** integración Godot/GDExtension del flujo de consulta -> propuesta -> validación Core -> consecuencia -> respuesta/escena; sin mapas de hotspots obligatorios y sin tablas de verdad en GDScript.
- **P03** catálogo de fondos/retratos y reglas de selección por estado/ID, placeholders lícitos; controles táctiles, escalado, teclado, rendimiento MSI/Tab S9+.
- **P04 opcional con autorización separada:** narrador Sol para escena nueva y Luna para NPC/consultas, siempre player-safe, gateway seguro, consentimiento, corte monetario, no mutación directa. Sin consentimiento, modo local determinista plenamente recorrible.
- **Entrega:** partida visual y conversacional real ejecutada por Godot, sin equiparar ilustraciones con fuentes de hechos.
- **Puerta:** V001-H01 y P04 visual, flujo A/B/C en Host con interfaz local; H02 solo si se autoriza y prueba, o excepción explícita registrada.

### NIM-18 — Persistencia integral, regresiones y compatibilidad (responsable implementación: Codex; ChatGPT audita)

- **P01** ampliar el formato y el inventario de guardado I4 para incluir de manera autoritativa el dominio realmente implementado: layout, localización, hogares, actores, herramienta, orden de taller, reloj, eventos y conocimiento.
- **P02** restauración transaccional/versionada, huellas del Content Pack, generadores/semillas y migrations explícitas; negativa ante incompatibilidad sin pérdida del estado.
- **P03** pruebas entre procesos Windows y Linux, export Windows y APK Android, mismas acciones/semilla/snapshot, caminos A/B/C, condiciones negativas, proceso interrumpido y backup.
- **P04** CI y diagnóstico de determinismo, memoria/CPU, invariantes, errores y aislamiento Core/Host; actualizaciones de versión compatibles con los pins.
- **Entrega:** vida completa de campaña entre reinicios, no solo persistencia del esqueleto NIM-07.
- **Puerta:** V001-S01..S06, sin reroll ni clones; toda acción después de cargar continúa exactamente desde el estado guardado.

### NIM-19 — Certificación funcional y traspaso a escala (ChatGPT + propietario; Codex solo defectos complejos)

- **P01** ejecutar matriz V001 completa (28 IDs), 100 semillas válidas y los tres itinerarios A/B/C, con auditoría independiente de todos los fallos y pendientes.
- **P02** pruebas físicas MSI Raider Windows 11 y Galaxy Tab S9+ Android ARM64; teclado/voz si se ha integrado, errores UI, rendimiento y guardado real.
- **P03** **prueba de replicabilidad**: crear una segunda aldea V1 con otra semilla y preparar una proyección territorial adicional mediante la MISMA cadena. Darovan se utilizará como candidato únicamente con fuentes, versiones y decisiones aprobadas.
- **P04** publicar manual de fábrica, versiones de esquemas, checklist de portabilidad, evidencias, límites y reglas para desplegar nuevos modelos y territorios; PR/fusión solo autorizada.
- **Entrega:** vertical V001 certificada + playbook de crecimiento + manifiesto de evidencia reproducible.
- **Puerta definitiva:** demostrar que no hay que crear código específico «para la herramienta» para materializar una segunda aldea; si falla esa generalidad, corregir infraestructura antes de escalar.

## 5. Estrategia para economizar Codex

1. **ChatGPT termina primero el P01/P02 documental de cada fase**, incluyendo decisiones, contrato, fixtures, tests positivos/negativos y una lista de cambios permitidos/prohibidos. Debe intentar escribir también validadores Python y herramientas no nativas cuando el riesgo sea controlable.
2. **Codex solo recibe P03/P04 o el núcleo nativo realmente necesario**, con prompt que señale **modelo GPT-6 y razonamiento Alto** cuando el trabajo sea complejo. No darle encargos de lectura general del Lore, búsquedas abiertas sin límites ni diseño improvisado.
3. Dividir cada entrega técnica en PR Draft pequeñas, con CI focalizada y regresiones, evitando repetir compilaciones completas cuando no cambian contratos nativos. ChatGPT audita antes de ampliar la fase. **No fusionar sin permiso del autor.**
4. Agrupar en un mismo encargo Codex cambios compatibles ya especificados (sin fusiones enormes ni dependencia circular); no crear ramas simultáneas que alteren la misma ABI GDExtension o los mismos pins.
5. Usar parsers locales y respuestas deterministas para ensayar todo A/B/C **sin gastar API**. Sol/Luna solo si se autorizan expresamente costes y seguridad. Generación de recursos narrativos/visuales por ChatGPT no es programación nativa.
6. Mantener un backlog claro de tareas reservadas a Codex, desbloqueadas por contratos completos; si no hay cuota, seguir preparando documentos/fixtures/arte sin detener el avance.

## 6. Dependencias, riesgos y prohibiciones

- **Riesgo 1 — CoreRPG compartido:** cada extensión genérica puede afectar Star Trek. Exigir ADR, compatibilidad, tests genéricos, nuevo pin y no modificar Core por conveniencia de Nimroel. No arrastrar reglas de Norgard al núcleo universal.
- **Riesgo 2 — Dos fuentes de verdad:** Godot no replica ni autoriza estado; el generador Nimroel entrega una configuración, pero Core persiste y resuelve. El payload de dominio debe pertenecer a un agregado autoritativo validado; **nunca una segunda simulación independiente en UI**.
- **Riesgo 3 — Save parcial:** I4 solo preserva Core y metadatos del fixture; los nuevos dominios deben quedar cubiertos por una transacción/restauración íntegra antes de certificarse. No depender solo de reejecutar seed ni guardar la UI.
- **Riesgo 4 — Proceduralidad falsa:** la semilla dorada V001 no basta. Exigir otras semillas, comprobaciones de 100 casos, invariantes, propiedades y caminos alternativos; no hacer de la aldea un guion fijo.
- **Riesgo 5 — Lore como código:** el canon no se copia manualmente a ficheros ejecutables. Siempre manifest, procedencia, mapeo, verificación y contrato. Los parámetros de ensayo son técnicos y no decisiones canónicas.
- **Riesgo 6 — IA omnisciente:** el texto de Sol/Luna no es estado, no ve hechos ocultos, y no muta el mundo. La política de pago requiere consentimiento y gateway.
- **Riesgo 7 — Mundo congelado:** agentes y órdenes avanzan cuando avanza el tiempo de simulación autorizado, con independencia de escena; no se promete tiempo transcurrido mientras la app está cerrada.
- **Riesgo 8 — Alcance descontrolado:** no añadir de golpe combate, magia, economía regional completa, religión, ciclo político o cientos de asentamientos. Solo los contratos mínimos reutilizables para V001.

## 7. Gobierno, evidencia y autorización

- Este plan no autoriza iniciar implementación de NIM-08/09 ni modificar CoreRPG. El cierre formal de NIM-07 y sus pruebas físicas se verificará separadamente.
- Cada fase produce **ACTA**, **CONTRATO**, **FIXTURES**, **MATRIZ DE PRUEBAS**, **RESULTADO CODEX si aplica**, **AUDITORÍA CHATGPT** y **TRASPASO** en Docs/NIM-XX/ o enlaces indexados.
- Evidencia mínima por ejecución: SHA de Nimroel, SHA de CoreRPG, schema/pins, SHA de Content Pack, versión de generador, world seed/settlement ID/fixture regional, plataforma, proceso y tiempo simulado, inputs, estado/resultado observado, hashes de snapshot, CI, incidencias y aprobación.
- Las versiones pueden avanzar sin destruir partidas; toda diferencia incompatible necesita migración explícita o rechazo seguro.
- **No se declara verde un criterio V001 solo por estar escrito en un documento, compilado un APK, o existir un sprite.**
- El propietario aprueba: canon, cambios de alcance, API de pago, promoción de Content Pack, PR/fusión, publicación final y equivalencia del piloto territorial.

## 8. Documentos compañeros

- **02_MATRIZ_TRAZABILIDAD_V001.md**: 28 casos y responsable/evidencia de cada uno.
- **03_PLAYBOOK_FABRICA_MUNDOS.md**: receta de fabricación, separación de autoridad, manifiestos, reconstrucción y expansión territorial.
- **README.md**: índice y estado de esta planificación.

**Regla final:** La primera aldea valida la maquinaria; no se diseña la maquinaria alrededor de una sola aldea.
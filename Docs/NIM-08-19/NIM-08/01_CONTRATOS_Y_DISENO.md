# NIM-08 P02/P03 — Arquitectura definitiva de diseño, contratos y ADR

Versión NIM08-ARCH-0.1.0. **Contrato de DISEÑO**, no implementación ni cambio de ABI. No introduce nuevos tipos en CoreRPG existente.

## ADR-08-01 — Una sola autoridad, sin WorldState espejo

Secuencia normativa: fuente canónica aprobada -> authoring/selección/lock -> pack declarativo -> generador de dominio Nimroel -> operaciones CoreRPG verificadas -> vista autorizada -> transporte GDExtension -> escena Godot 2D. El Host coordina sesiones, permisos de acceso, almacenamiento de bytes y presentación, nunca decisiones físicas; IA solo propone y relata, no escribe hechos.

El generador de Nimroel es una **función de preparación determinista**, no un segundo simulador vivo. Cuando un dominio requiere un campo mutable hoy ausente en Core (p.ej. reparación/progreso/posición), se declara una dependencia de primitiva genérica o de extensión autoritativa del Core. **Queda prohibido** persistir una segunda fuente de verdad mutable en JSON/GDScript/GDExtension mientras Core mantiene otra. No considerar aceptable el sistema hasta integrar esas operaciones/serialización y prueba transaccional. La decisión sobre modificar CoreRPG corresponde a autorización futura.

## ADR-08-02 — Identidad y tipos de estado

- Identidad de construcción: stable_settlement_key, source_anchor, región, world_seed (decimal en texto), versions; jamás derivada del nombre visible.
- Identidad semántica externa: namespace/territory/settlement/role/ordinal estable; normalización UTF-8 y orden de claves definido. Conversión a EntityId numérico Core solo al materializar **en orden determinista** y con tabla de resolución persistida. No confundir dos actores del mismo oficio.
- Población: total declarado/latente/materializado se cuenta sin duplicar; un residente latente no recibe afirmaciones individualizadas ni EntityId ficticio. Roles requeridos para la prueba sí se materializan con ID antes de usarlos.
- Edificio y localización son tipos diferentes; capacidad de herrería/taberna no impone edificio independiente; hogar = unidad social + asignación residencial, no sinonimia de contención.
- Posición, grafo/puertas/rutas y sus costes se deciden y mutan por autoridad; los fondos no aportan topología.
- Derechos: propietario, poseedor físico, custodio autorizado y ubicación son campos independientes. Daño, condición, materiales consumidos, orden y consecuencias no equivalen a un texto o flag de misión.
- Conocimiento: distinguir desconocido, ausencia conocida y presencia conocida; registrar observador, fuente, hecho y tiempo. Filtrar también errores/rechazos, informes, logs y contexto IA.
- Tiempo: tiempo simulado discreto, enteros de unidad fijada por pack, avance solo por operación autorizada. No depende de FPS, red ni reloj de pared.

## ADR-08-03 — Contratos de diseño y evolución

Archivos versionados junto a este documento:
- contracts/world-instance-0.1.0.schema.json: estructura **propuesta** de instancia lógica y sus referencias, adecuada como contrato de handoff futuro de Core, NO snapshot implantado.
- contracts/action-envelope-0.1.0.schema.json: forma conceptual de propuesta, decisión/rechazo y consecuencia. Un comando de texto no pasa a acción por sí mismo.
- contracts/generation-manifest-0.1.0.schema.json: procedencia, políticas, hashes y generación reproducible; mantiene intacto el Content Contract Core 0.1.0.
- contracts/technical-manifest-example.json: ejemplo exclusivamente técnico, no lote canónico ni mundo generado.

Los nombres y campos de los esquemas son contratos de frontera **candidatos** para NIM-09+ y pueden recibir evolución compatible antes de prometer API nativa. Identificadores de contrato exactos, sin usar $schema para hacer llamadas por red. Manifest: rechazar campos desconocidos, hashes mal formados, referencias huérfanas, versiones no apoyadas o canon sin lock; sólo datos aprobados o parámetros TUNING_EXPERIMENTAL.

## ADR-08-04 — Construcción reproducible y permisos

1. Fijar repo SHA, hashes de fuentes aprobadas (source-lock existente), Core pin, versiones de schema/reglas/generador, seed y contexto regional explícito. Canon cambiante requiere nueva edición, nunca alteración implícita de partidas.
2. Normalizar documentos seleccionados de forma trazable: path y anchor/pointer exactos, categoría CANON | DATOS_OPERATIVOS | TUNING_EXPERIMENTAL, regla de proyección y justificación. Valor sin fuente marcada => fallo.
3. Resolver dependencias del Content Pack mediante DAG versionado; orden topológico estable, luego orden lexicográfico de IDs semánticos; serializar UTF-8/LF, claves ordenadas, finales LF; SHA-256 por archivo y hash de conjunto. Reutilizar protocolo de Tools/CoreRPG413; evitar esquema incompatible nuevo por capricho.
4. Derivar streams independientes por subsistema desde SHA-256 de codificación sin ambigüedad: prefijo de protocolo, longitud de cada campo, world_seed, stable_settlement_key, region_fixture_hash, subsystem y generator_version. Reducir a ancho del RNG fijado mediante algoritmo documentado en NIM-10; no usar std::hash, orden de filesystem ni seed global mutable compartido.
5. Generar región sólo desde fuente/fixture declarado (NIM-10 no suplanta la red territorial completa), luego constraints V1, edificios/layout/conectividad, hogares, residentes/roles, objetos, reloj inicial. Fallos no autorizan añadir molino, aserradero, murallas o biografías por defecto.
6. Validar referencias/constraints; emitir un manifiesto y **instancia candidata inmutable**; materializar de modo determinista mediante operaciones autorizadas en Core. Si falta operación Core, la generación de ese aspecto se bloquea, no se simula en Godot.
7. La campaña conserva seed/contexto, mapa de IDs, pack original y estado completo del Core. Restaurar **sin regenerar ni avanzar tiempo**; validar contenido instalado, CRC/longitudes/hash y compatibilidad antes de reemplazar estado; transacción que preserve el save anterior en fracaso. Migración es una operación explícita separada y auditable.
8. Para dos ejecuciones independientes con mismas entradas: comparar bytes de pack, tabla IDs, layout y hash de estado Core inicial; 100 seeds y negativos en NIM-10/19. Aleatoriedad de estilo narrativo no afecta resultado lógico.

## ADR-08-05 — Comandos, eventos y rollback

Ruta de interacción: intento de usuario -> interpretación local opcional -> propuesta tipada (actor, objetivo, expected_revision, observador/capacidad, datos necesarios) -> autenticación de sesión -> autorización de dominio + precondiciones -> transacción autoritativa Core -> consecuencia y revisión -> observación filtrada -> texto/ilustración opcionales.

Rechazos obligatorios: actor inexistente, destino no conocido, ruta ausente, permisos insuficientes, objeto ajeno, falta de material, horario/capacidad invalida, target duplicado, revisión obsoleta, guardado incompatible. Una negativa/no-op no debe mutar estado ni RNG ni gastar tiempo simulado; errores externos jamás filtran hechos no autorizados. El paso Simulation::step actual es atómico **por acción** y puede procesar prefijos; un workflow multiacción (reparar/entregar) requiere futura transacción o compensación demostrada, no asumir batch atómico.

Solicitud de herrería = orden persistente con disponibilidad/material/cola reales. Entrega de objeto, mejora de condición, pago, recepción y conocimiento son eventos diferentes. La máquina opcional «La herramienta rota» **deriva** su progreso de hechos autorizados; no altera físicamente cosas por una etiqueta de quest. Probar segundo tipo de herramienta ordinaria modificando datos, no código especial.

## ADR-08-06 — Conocimiento, IA, escenas y observabilidad

Core admite knowledge estructural sin inferencia de dominio; las memorias sociales y transmisiones exigidas se implementarán bajo contrato nuevo, no se presuponen. Fuente y audiencia de cada hecho con permisos mínimos; vista del observador incluye sólo identidad/ubicación/nombre conocido, opciones habilitadas y explicación redactada para esa audiencia. Trazas privilegiadas fuera de la interfaz del jugador; redacción segura de errores. IA Sol/Luna solo con autorización independiente y contexto seguro. Modo local sin proveedor remoto es obligatorio.

El render elige fondo/retrato por clase de escena y dato observable, nunca por suponer que el NPC existe. Interfaz 2D Windows/Android sin dependencia obligatoria de hotspots; navegacion textual libre desde rutas autorizadas.

## ADR-08-07 — Reutilización CoreRPG / Star Trek

| Mecánica | Core genérico potencial | Adaptador Nimroel específico | Ejemplo en Star Trek |
| --- | --- | --- | --- |
| Identidad y relación | EntityId, índices estables, relation registry | hogar/oficio/familia Valrik | tripulación, puesto, mando |
| Localización/rutas | posición, grafo, acciones, visibilidad | caminos, interiores aldeanos | cubiertas, corredores, turboascensor |
| Tiempo/agenda | reloj, tickets, scheduler determinista | horarios de taller, cosecha | turnos de guardia, mantenimiento |
| Objetos/estado | ítem, condición y tenencia | herrería, permisos de custodia | equipo, inventario, reparaciones |
| Conocimiento | observador, fuente, difusión segura | rumor y memoria rural | informes clasificados/PADD |
| Persitencia/historia | snapshot, archivo/recuperación, migration | versión de pack/canon Nimroel | save de campaña, historia temporal |

**No se importa contenido entre juegos ni se cambia Core.** Antes de cualquier PR Core exigir demostración neutral en tests Core, análisis de ABI, pin actual de cada juego, migración/save y regresiones cruzadas; aprobación específica del autor para cambiar pin/repositorios.

## ADR-08-08 — Invariantes de cierre

I01 única autoridad; I02 canon con fuente; I03 seed+versiones deterministas; I04 IDs/no duplicación; I05 grafo transitado real; I06 estado NPC independiente de escena; I07 propiedad/posesión/custodia distintas; I08 no aprendizaje omnisciente; I09 reloj sólo por acción; I10 transacción/rollback; I11 recuperación sin reroll; I12 pack/API versionados; I13 sin IA pagada necesaria; I14 mismo Core genérico posible para otro juego. Cada uno se asigna al menos a una verificación V001 o al test transversal de Docs/NIM-08-19/02_MATRIZ_TRAZABILIDAD_V001.md, **hoy todos pendientes de ejecución integral**.

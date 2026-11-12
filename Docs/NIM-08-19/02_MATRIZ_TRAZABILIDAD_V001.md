# V001 — Matriz de trazabilidad y aceptación de «La herramienta rota»

**Estado:** matriz de planificación; **todos los criterios de la misión jugable continúan PENDIENTES de ejecución/certificación**. La evidencia NIM-07 de un fixture estructural no convierte automáticamente en PASS los requisitos completos V001. Fecha: 12/11/2026.

**Fuente normativa:** Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik/Aldeas/03_Prueba_v0.0.1/MATRIZ_ACEPTACION_V001_v0.1.md, junto a ENCARGO_HERRAMIENTA_ROTA_v0.1.md y contrato_prueba_v001_v0.1.json.

**Reglas de interpretación:** los 28 IDs se conservan literalmente; esta matriz asigna planificación técnica y evidencia sin sustituir ni rebajar el canon. Estados permitidos: PENDIENTE, BLOQUEADO, FAIL, PASS_AUTOMATICO, PASS_HOST, PASS_FISICO, EXCEPCION_AUTORIZADA. **Un build no es PASS_FISICO**. Evidencia obliga SHA, seed, versión, plataforma y pasos.

## G — Generación aldeana (6)

| ID | Fase principal | Responsable implementación | Verificación exigida | Estado |
| --- | --- | --- | --- | --- |
| V001-G01 | NIM-10 | Codex; ChatGPT audita | Población 35–100; fixture V001 en banda 40–60, sin fijarla universalmente; comparar instancias | PENDIENTE |
| V001-G02 | NIM-10 | Codex; ChatGPT audita | **100 semillas** con hogares suficientes, agua, entrada, producción, taberna y herrería básica | PENDIENTE |
| V001-G03 | NIM-10 | Codex | Variar semillas: molino/posada/carpintería no obligatorios ni imposibles; requisitos fijos intactos | PENDIENTE |
| V001-G04 | NIM-10 | Codex | Misma semilla/contexto/versiones = mismos IDs, mundo inicial/layout/decisiones; nombre no cambia ID | PENDIENTE |
| V001-G05 | NIM-10 | Codex | Grafo regional/fixture explícito; rutas y cobertura; correcciones deterministas mínimas trazadas | PENDIENTE |
| V001-G06 | NIM-10 + NIM-19 | ChatGPT diseña; Codex genera; autor revisa | Layout abierto V1 con casas bajas/campos/ruta maderera, sin muralla ni aserradero formal por defecto | PENDIENTE |

## P — Jugador y descubrimiento (4)

| ID | Fase principal | Responsable implementación | Verificación exigida | Estado |
| --- | --- | --- | --- | --- |
| V001-P01 | NIM-12 + NIM-17 | Codex | Llegar sin omnisciencia; descubrir taberna, herrería y habitantes por rutas reales | PENDIENTE |
| V001-P02 | NIM-15 | ChatGPT especifica; Codex integra | Diálogo con agricultor/vecino; respuestas desde hechos/observador autorizados | PENDIENTE |
| V001-P03 | NIM-16 | ChatGPT especifica; Codex integra | Ignorar/no aceptar misión no congela aldea ni impide guardar | PENDIENTE |
| V001-P04 | NIM-12 + NIM-17 | Codex | Entrar/salir escenas o interiores sin duplicar identidades ni NPC persistentes | PENDIENTE |

## Q — Situación de la herramienta (8)

| ID | Fase principal | Responsable implementación | Verificación exigida | Estado |
| --- | --- | --- | --- | --- |
| V001-Q01 | NIM-13 | Codex | ID estable del objeto, daño creíble y propietario/poseedor separados | PENDIENTE |
| V001-Q02 | NIM-13 | Codex | Ofrecer/transportar sin autorización no transfiere propiedad ni custodia ilícita | PENDIENTE |
| V001-Q03 | NIM-14 | Codex | Herrero ocupado admite espera/rechazo, sin trabajo instantáneo ni prioridad del protagonista | PENDIENTE |
| V001-Q04 | NIM-14 | Codex | Reparación progresa por trabajador + estación + materiales + tiempo; narrar no muta | PENDIENTE |
| V001-Q05 | NIM-14 | Codex | Falta de material/cierre pausa o aplaza, sin completarse indebidamente | PENDIENTE |
| V001-Q06 | NIM-16 | Codex | Reparación terminada y devolución/recepción real con propiedad/custodia/condición consistentes | PENDIENTE |
| V001-Q07 | NIM-16 | Codex | Rechazo/abandono conserva objeto y permite, si procede, solución autónoma de NPC | PENDIENTE |
| V001-Q08 | NIM-15 | Codex | NPC sin testimonio no sabe acuerdo; procedencia/transmisión plausible antes de conocer | PENDIENTE |

## S — Tiempo, persistencia, determinismo (6)

| ID | Fase principal | Responsable implementación | Verificación exigida | Estado |
| --- | --- | --- | --- | --- |
| V001-S01 | NIM-18 | Codex | Guardar antes de conocer NPC; restaura IDs, hogares, servicios, seed, hora | PENDIENTE |
| V001-S02 | NIM-18 | Codex | Guardar durante trabajo; restaura daños, materiales, cola, profesional, avance y plazo | PENDIENTE |
| V001-S03 | NIM-14 + NIM-18 | Codex | Tiempo simulado válido: actividad fuera de escena sin depender de sprite | PENDIENTE |
| V001-S04 | NIM-18 | Codex | Guardar tras ayudar o abandonar; memorias/resultados se mantienen y no se duplican ítems | PENDIENTE |
| V001-S05 | NIM-18 | Codex | Cambiar generador: conservar save anterior o migración explícita; no reroll | PENDIENTE |
| V001-S06 | NIM-18 | Codex | Mismo estado/seed/acciones = mismo resultado lógico, aunque narración varíe | PENDIENTE |

## H — Presentación y diagnóstico (4)

| ID | Fase principal | Responsable implementación | Verificación exigida | Estado |
| --- | --- | --- | --- | --- |
| V001-H01 | NIM-17 + NIM-19 | ChatGPT UX; Codex integración; autor físico | EXE Windows juega vertical local sin Android, red ni IA remota | PENDIENTE |
| V001-H02 | NIM-17.P04 (opcional) | ChatGPT contrato; Codex solo con permiso | IA con player-safe context; sin spoilers/alteraciones. **Si no se habilita**, EXCEPCION_AUTORIZADA documental, no PASS ficticio | PENDIENTE |
| V001-H03 | NIM-19 | ChatGPT auditor | Diagnóstico de fuente, pre/post, rechazo y mutaciones sin duplicar WorldState | PENDIENTE |
| V001-H04 | NIM-19 | Autor + ChatGPT | Experiencia humana de aldea viva, misión no forzada y consecuencias coherentes, en hardware | PENDIENTE |

**Nota H02:** la matriz V001 antigua menciona Terra/Luna. La revisión posterior de política vigente atribuye escenas a Sol y diálogo/consultas a Luna. No se reactiva Terra por este texto ni se presupone API pagada; el modo local es condición indispensable incluso si la ruta IA se aprueba luego.

## 2. Itinerarios dorados A/B/C — definición de evidencias

### A. Ayuda completa (harness y luego Godot Windows/Android)

1. Crear aldea V1 válida desde semilla + región estable.
2. Jugador llega sin mapa completo y puede explorar otras actividades.
3. Descubre problema de un agricultor mediante fuente que realmente lo sabe.
4. Consigue autorización para portar/entregar un objeto individual con propietario distinguible.
5. Encuentra herrero real mediante ruta y disponibilidad; solicita trabajo.
6. Si ocupado o sin recursos, queda en espera. Con recursos/condiciones vigentes, el reloj hace progresar la orden de manera verificable.
7. Recoge y **devuelve** el objeto; se comprueba titularidad, poseedor, condición, location, conocimiento del agricultor y estado de encargo.
8. Guardar/cerrar completamente/reanudar; repetir consultas y verificar mismo estado y sin doble objeto.

**Rechazos obligatorios:** teletransporte narrado; revelar secreto por conocer ID; entregar sin autorización; herramienta duplicada; texto de IA que complete trabajo; saltar cola; reparar sin material; completar sin devolver.

### B. Trabajo pendiente durante la ausencia

1. Descubrir y tramitar una orden que pueda permanecer en cola/en curso.
2. Registrar material, tiempo restante, actor, condición y compromiso.
3. Guardar mientras está pendiente. Reiniciar proceso/reanudar.
4. Avanzar tiempo de mundo por una acción válida mientras el jugador está fuera del taller; comprobar avance, pausa o espera justificables.
5. Volver a consultar al trabajador y objeto, sin reroll ni trabajo instantáneo.

**Rechazos obligatorios:** progresión por FPS, por cerrar app sin política, borrado de cola al cargar, NPC creado desde fondo, simultaneidad imposible de trabajos.

### C. Indiferencia / rechazo / abandono

1. Crear una aldea sin aceptar automáticamente el problema.
2. Ignorar la fuente o rechazar ayudar; otras acciones siguen disponibles y se puede guardar.
3. El objeto y la necesidad continúan; el agricultor/herrero pueden actuar por políticas explícitas y recursos reales, o no.
4. Salir, reanudar y constatar consecuencias; misión no aparece como fracaso/éxito forzoso por no intervenir.
5. Si hay memoria de rechazo o abandono, solo los observadores con vía de conocimiento legítima reaccionan.

**Rechazos obligatorios:** NPC inmovilizado esperando jugador; borrar herramienta; cancelar orden real por una bandera narrativa; secretos compartidos automáticamente.

## 3. Pruebas transversales no sustituibles por los 28 IDs

- **Autenticidad:** cada dato autorizado derivado de pack versionado, fixture y Core, no de nombres/IDs hardcodeados en Godot.
- **Generación:** 100 semillas válidas, propiedades y negativos; misma seed idéntica, otras seeds variación plausible; claves por subsistema.
- **Integridad:** 0 referencias huérfanas, 0 residentes duplicados, toda vivienda/herrero/nodo accesible o causa válida registrada; contención acíclica.
- **Seguridad:** dos observadores diferentes, datos secretos ocultos, estados desconocido/no/existe separados, sin leakage por errores.
- **Concurrencia/salvaguarda:** una instancia escritora o bloqueo explícito, rollback verificado ante save incompatible/corrupto; no prometer resistencia total a fallo eléctrico sin fsync.
- **Escala:** segunda semilla V1 y segundo contexto territorial con igual pipeline, sin copiar código de la misión.
- **Plataformas:** Windows real y APK ARM64 real **en dispositivo**; la CI Android sola no cuenta como test físico.
- **IA:** rutas Sol/Luna opcionales, consentimiento y presupuestos, salidas no autoritativas; prueba offline completa como respaldo.
- **Trazabilidad:** cada PASS incluye commit, SHA Content Pack, versión de generador, seed, fixture, plataforma, pasos, logs y auditor.

## 4. Registro de evidencia por criterio

Para cada ID se mantendrá en GitHub un registro con:
- id, fecha, estado y responsable;
- source_refs + canon_hash + pack_hash;
- Nimroel SHA, CoreRPG SHA, Godot, ABI/OS y device;
- world_seed, stable_settlement_id, region_fixture_version y generator_version;
- pre-state hash, acción/consulta autorizada, rechazo/resultado, post-state hash;
- trace del proceso, save/reopen y salida CI o captura manual cuando corresponda;
- incidencias, desviaciones aprobadas y PR de solución.

**Nada se marca PASS hasta comprobar ese comportamiento en el nivel requerido (unidad, integración, host y físico).**

## 5. Condición de cierre

NIM-19 cierra solo cuando A/B/C son recorribles y la matriz tiene todos los **esenciales** en PASS al nivel exigido, o excepciones explícitamente aprobadas **antes** de anunciar la versión jugable. H02 es opcional según fuente canónica y política vigente; su ausencia no puede presentarse como una prueba IA superada. El grado de materialización de NPC no visibles debe declararse con precisión: un residente latente sin EntityId no se presenta como un NPC individual simulado.

La primera aventura no es un patrón rígido de misiones: **es una prueba de la fábrica de entidades, acciones, tiempo, conocimiento, persistencia y presentación**.
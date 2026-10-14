# Matriz de aceptación — Nimroel RPG v0.0.1 (primera aldea V1)

**Estado:** CRITERIOS DE PRUEBA DEFINIDOS; NO EJECUTADOS.
**Enfoque:** distinguir test lógico automatizado, integración del Host 2D y comprobación humana de experiencia. Sin dar resultados verdes por contrato escrito.

## A. Generación y canon aldeano

| ID | Tipo | Preparación / acción | Condición de éxito |
| --- | --- | --- | --- |
| V001-G01 | automatizable | Generar múltiples instancias V1 válidas | Cada aldea conserva 35–100 habitantes; fixture inicial selecciona banda orientativa 40–60. |
| V001-G02 | automatizable | Generar 100 semillas en contexto regional válido | Todas tienen hogares suficientes, agua, acceso territorial, subsistencia, taberna y capacidad de herrería básica. |
| V001-G03 | automatizable | Variar semillas y servicios opcionales | Molino/posada/carpintería no aparecen como obligatorios ni desaparecen requisitos fijos. |
| V001-G04 | automatizable | Generar dos veces con semilla y versiones iguales | El contenido inicial, IDs y decisiones estables coinciden; el nombre visible no altera el ID. |
| V001-G05 | automatizable | Generar mediante fixture regional con grafo | Cobertura y rutas se respetan; si hay corrección, es mínima y queda registrada. |
| V001-G06 | revisión | Inspeccionar layout V1 | Aldea abierta, casas bajas, campos y ruta maderera; sin muralla ni aserradero formal como estándar. |

**Precaución:** 100 semillas es una meta de prueba propuesta, no probabilidad canónica ni afirmación de cobertura exhaustiva.

## B. Jugador y descubrimiento

| ID | Tipo | Preparación / acción | Condición de éxito |
| --- | --- | --- | --- |
| V001-P01 | Host | Llegar a la aldea sin haber visitado su núcleo | Puede desplazarse y descubrir taberna, herrería y habitantes; no recibe un plano omnisciente obligatorio. |
| V001-P02 | integración | Hablar con agricultor o vecino | La información mostrada procede de contexto y fuente reales; no hay conocimientos globales por defecto. |
| V001-P03 | integración | No aceptar ni descubrir el encargo | La aldea conserva actividades y posibilidad de guardado; no obliga a completar misión. |
| V001-P04 | Host | Entrar y salir de escena o interior disponible | La entidad lógica de los NPC no depende de la representación visual ni se duplica. |

## C. Situación «La herramienta rota»

| ID | Tipo | Preparación / acción | Condición de éxito |
| --- | --- | --- | --- |
| V001-Q01 | automatizable | Crear útil dañado con dueño/poseedor | Tiene un único ID estable, daño plausible y relaciones separadas de posesión/propiedad. |
| V001-Q02 | automatizable | Ofrecer objeto sin autorización | No se transfiere propiedad; el motor valida custodia y permisos. |
| V001-Q03 | integración | Pedir servicio al herrero ocupado | Puede quedar en espera sin completarse instantáneamente ni desplazar compromisos previos. |
| V001-Q04 | automatizable | Ejecutar progreso con recursos, trabajador, estación y tiempo | Cambia solo por acciones/ticks válidos; una narración no repara ni consume recursos. |
| V001-Q05 | automatizable | Quitar recurso necesario o cerrar el taller | Orden permanece aplazada/pausada, sin resultado imposible. |
| V001-Q06 | integración | Completar y devolver el útil | Propiedad/custodia/condición concuerdan y el agricultor puede reconocer la entrega. |
| V001-Q07 | integración | Rechazar o abandonar ayuda | No elimina el objeto ni interrumpe necesariamente soluciones autónomas NPC. |
| V001-Q08 | integración | Informar a un NPC no testigo | No conoce automáticamente el acuerdo; fuente y transmisión explican cualquier conocimiento posterior. |

## D. Tiempo, persistencia y coherencia

| ID | Tipo | Preparación / acción | Condición de éxito |
| --- | --- | --- | --- |
| V001-S01 | automatizable | Guardar antes de conocer a un NPC y recargar | Identidad, hogares, servicios, hora y semilla se conservan. |
| V001-S02 | automatizable | Guardar durante la reparación y restaurar | Condición del útil, materiales, cola, actor, progreso y plazos no se reinician. |
| V001-S03 | automatizable | Avanzar tiempo mientras la herrería no está visible | El progreso ocurre solo si procede; ningún NPC requiere sprite activo para existir. |
| V001-S04 | automatizable | Guardar/cargar tras ayudar o abandonar | Se mantienen consecuencias y estados de memoria pertinentes, sin duplicar objetos ni encargos. |
| V001-S05 | automatizable | Cambiar versión de generador tras guardar | El guardado viejo permanece válido o requiere migración explícita; nunca reroll silencioso. |
| V001-S06 | automatizable | Repetir historia con mismo estado/seed/acciones | Mismo resultado lógico; diferencias de texto narrado no alteran los hechos del motor. |

## E. Presentación y diagnóstico

| ID | Tipo | Preparación / acción | Condición de éxito |
| --- | --- | --- | --- |
| V001-H01 | Host Windows | Arrancar en PC sin Android, red o IA remota | Es posible recorrer y ejecutar la vertical mínima mediante controles locales. |
| V001-H02 | integración IA opcional | Pedir texto a Terra/Luna con contexto limitado | El texto no revela secretos, adjudica recompensas ni cambia el mundo sin operación válida. |
| V001-H03 | inspector | Verificar estados antes/después de una acción | Hay diagnóstico de fuente, decisión, fallos y mutaciones, sin sustituir el Core por datos de UI. |
| V001-H04 | revisión | Inspección humana del recorrido | Se percibe una pequeña aldea viva, sin misión forzada y con resultados coherentes. |

## F. Criterios de salida por etapa

- **Preparación de lore:** aprobada con alcance, situación y pruebas escritas; no implica implementación.
- **Prueba técnica CoreRPG:** los tests disponibles de entidad/población/persistencia y casos de contrato compatibles pasan en entornos validados. Los tests futuros no se reportan como ejecutados.
- **Integración temprana:** al menos creación/carga del mundo y primeras acciones autoritativas mediante Content Pack Nimroel y Host de prueba.
- **v0.0.1 jugable:** los requisitos V001-G, P, Q, S y H esenciales se verifican; cualquier exclusión o degradación de funcionalidad debe declararse y aprobarse **antes** de decir "lista".

Se documentarán resultados con: commit de CoreRPG, commit de Nimroel, semilla/fixture, versiones, plataforma, pasos realizados, resultado observado, incidencia y evidencia. Mantener claramente separados "pendiente", "fallido" y "aprobado".

## Dependencias y traspaso

- **CoreRPG:** 4.9 conocimiento; 4.10 acciones/simulación; 4.11 inspector; 4.12 contexto/IA; 4.13 soporte de primer Content Pack Nimroel. La numeración es hoja de ruta, no garantía de capacidades ya integradas.
- **Nimroel:** serializar parámetros del modelo, añadir mundo de prueba, adapter/Content Pack, Host 2D independiente de Unreal, lógica narrativa del encargo y pruebas.
- **NAP:** permite arte definitivo más adelante; quedan autorizados placeholders para ejecutar v0.0.1.
- **Android:** validar Host Android nativo y NDK en otro hito; no declarar compatibilidad con base en un build de Windows.

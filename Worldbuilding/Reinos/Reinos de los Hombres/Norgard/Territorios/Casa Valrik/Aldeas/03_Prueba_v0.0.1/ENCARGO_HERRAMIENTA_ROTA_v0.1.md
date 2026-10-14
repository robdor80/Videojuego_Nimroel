# Encargo opcional v0.0.1 — «La herramienta rota»

**Estado:** situación narrativa de prueba aprobada; especificación funcional para futura implementación.
**Tipo:** necesidad cotidiana emergente, descubrible y no obligatoria. No es la trama canónica de todas las aldeas.
**Lugar:** aldea V1 del territorio de Treskal, generada dentro de una red regional plausible.

## 1. Situación de partida

Una persona que trabaja en una explotación agrícola tiene una herramienta dañada o inutilizable que necesita para una tarea real. El objeto **existe en el mundo** y tiene ID, estado, propietario, poseedor y localización diferenciados. La pequeña herrería local puede, en condiciones apropiadas, reparar herramientas ordinarias.

El agricultor puede pedir ayuda porque tiene trabajo pendiente. No está esperando inmóvil a que aparezca un protagonista. El herrero conserva sus ocupaciones, compromisos y límites de materiales. El jugador puede enterarse por conversación directa o por otra fuente plausible de la aldea, como la taberna, siempre que esa fuente haya adquirido antes la información.

No se impone nombre, sexo, edad, familia, recompensa, fecha, clima, ubicación exacta de casas ni clase de herramienta antes de que la partida genere esos detalles. La reparación debe ser un trabajo sencillo compatible con la **herrería básica**, no un artefacto extraordinario.

## 2. Actores y objetos necesarios

| Rol de prueba | Relación con el mundo | Restricción |
| --- | --- | --- |
| Trabajador agrícola | Residente, solicitante/propietario o poseedor legítimo del útil | No siempre espera o busca al jugador |
| Profesional de herrería básica | Capacidad obligatoria de aldea; identidad persistente | No garantiza servicio instantáneo |
| Tabernero y vecinos conocedores (opcionales) | Vías de descubrimiento | No reciben conocimiento universal |
| Jugador viajero | Puede proponer, transportar, esperar o abandonar | No gana propiedad por recoger el útil |
| Herramienta | Objeto persistente con condición y custodia | No aparece duplicada tras una carga |
| Solicitud/orden de reparación | Relación persistente entre actor, objeto y servicio | Existe solo si la situación realmente se registra |

## 3. Secuencia posible, nunca cadena obligatoria

**Descubrimiento:** el jugador nota el problema, escucha una conversación o pregunta por trabajos. Si no descubre nada, la aldea sigue funcionando.

**Oferta:** el jugador puede aceptar ayudar, negarse, aplazar la respuesta o marcharse. Una promesa formal solo nace si las reglas de compromisos la reconocen: aceptar una conversación no crea automáticamente un juramento Valrik.

**Entrega al herrero:** se verifica qué persona lleva el objeto y con qué autorización, si hay acceso a la herrería, tiempo, materiales, capacidad y peticiones anteriores. El herrero puede aceptar, posponer o rechazar con causa. El jugador nunca desplaza una cola de trabajo automáticamente.

**Trabajo:** la reparación progresa solo cuando existen mano de obra, estación/herramientas, materiales, acceso y tiempo suficiente. Puede continuar fuera de escena; puede pausarse justificadamente. La duración exacta procede de contenido y reglas, no de este relato.

**Devolución:** completar una reparación no transfiere por arte de magia el útil al agricultor. Debe producirse entrega, retirada por el propietario u otro movimiento legal. Si vuelve a su propietario, la necesidad inicial puede darse por atendida. La reparación funcional no implica aspecto impecable.

**Consecuencias:** el afectado puede recordar la ayuda y actuar de acuerdo con lo que conoce; otros NPC solo reaccionan si reciben información mediante una vía válida. La situación puede terminar resuelta, quedar pendiente, ser rechazada o abandonada por el jugador.

## 4. Estados de prueba — sin sustituir los contratos de dominio

La siguiente máquina de seguimiento es **del encargo**, no una redefinición de estados TOOL/COND/WAIT del Nimroel Core:

```text
no_descubierto
   └─ hecho_conocido → descubierto
                        ├─ no_aceptado (puede persistir)
                        ├─ rechazado_por_jugador
                        └─ ayuda_ofrecida
                              ├─ entrega_pendiente
                              ├─ reparacion_solicitada
                              │      ├─ en_espera
                              │      ├─ en_curso
                              │      ├─ pausada
                              │      ├─ reparada_pendiente_entrega
                              │      └─ no_viable
                              └─ ayuda_abandonada
reparada_pendiente_entrega + devolución válida → resuelta
```

El seguimiento narrativo puede variar por jugador; la reparación **puede acontecer por iniciativa de los NPC** independientemente de que el jugador participe. La marca de "ayuda_abandonada" no borra una orden de reparación real ya creada.

El motor discrimina **estado del encargo**, **estado de la herramienta**, **estado de la orden**, **posesión**, **propiedad**, **tiempo** y **conocimiento individual**. No usar un único booleano de `quest_completed` como sustituto.

## 5. Conductas y límites que se probarán

- Si el jugador retira el objeto sin permiso, no se convierte en suyo; si se deja en manos del herrero, este pasa a custodiarlo solo por una operación autorizada.
- Una reparación no puede completarse por decir "ya está" durante un diálogo.
- El profesional ocupado puede dar una fecha estimada sin que se garantice el resultado; no hay prioridad automática del jugador.
- La carga debe conservar trabajo parcial, compromiso, ubicación y estado; no resetear el progreso.
- Salir de la escena no cancela automáticamente una reparación válida, pero tampoco la completa sin procesar el tiempo y sus condiciones.
- Si el agricultor deja de necesitar el útil por una circunstancia real, la petición puede cambiar sin obligar a finalizar la misión.
- Ayudar puede generar gratitud, pero no se fija automáticamente dinero, reputación, amistad ni recompensa.

## 6. Tres itinerarios de aceptación mínimos

A. **Ayuda completa:** descubrir → obtener autorización → llevar el objeto → tramitar reparación → esperar progreso efectivo → devolución → persistencia tras recarga.

B. **Ayuda pendiente:** descubrir → gestionar solicitud → cerrar o salir antes de que acabe → regresar → comprobar que persona, útil, cola y progreso mantienen continuidad.

C. **Indiferencia/abandono:** no descubrir, rechazar o dejar de intervenir → comprobar que el mundo y los NPC continúan con consecuencias propias; no imponer fracaso instantáneo ni pausa universal del tiempo.

## 7. Dependencias técnicas

Requiere traducción específica desde contratos existentes `nimroel_tools_workstations_equipment_contract_v0.1.json`, `nimroel_wear_maintenance_repair_contract_v0.1.json`, `nimroel_property_possession_object_contract_v0.1.json`, `nimroel_waiting_service_capacity_contract_v0.1.json` y `nimroel_memory_salience_forgetting_contract_v0.1.json`, además del calendario. Estos contratos **no son todavía ejecución en CoreRPG**.

No fijar aquí esquemas de carga, valores de monedas, materias primas o fórmulas de reparación que aún necesiten diseño de Content Pack y reglas de motor.

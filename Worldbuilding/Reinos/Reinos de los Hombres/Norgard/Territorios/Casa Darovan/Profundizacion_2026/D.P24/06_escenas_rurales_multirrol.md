# D.P24/06 — Ocho escenas jugables hipotéticas, ocho maneras de no forzar la realidad

**Regla común:** todo lo siguiente es `TEST_ONLY`; no existe misión activada, NPC instanciado, tiempo transcurrido, viaje, registro judicial ni inventario creado. El narrador propone; CoreRPG futuro verifica precondiciones, consuma acción y guarda consecuencias. Los personajes solo conocen hechos que puedan conocer.

| ID | Situación y perspectivas | Respuestas y bifurcaciones | Rechazo o límite correcto | Estado futuro a persistir |
|---|---|---|---|---|
| RUR-E01 | **La reserva**: Mara quiere retener comida; Dela espera entrega; visitante necesita comprar | mostrar propiedad y disponibilidad; negociar cantidad o plazo; renunciar | no vender alimento inexistente ni duplicar saco | stock, compromiso, consentimiento y memoria |
| RUR-E02 | **La corta**: Toren quiere madera; Saira comprueba permiso; tercero necesita reparar | posponer; solicitar titularidad; usar material alternativo realmente existente | no talar en Pilares sin derecho ni romper regeneración | permiso consultado, lote, reserva forestal, relación |
| RUR-E03 | **La noche**: Eren solicita alojamiento; residente calcula camas y leña | acogida, intercambio de trabajo, indicación de sitio acreditado o negativa | no crear posada, cama ni camino | cama/combustible, obligación, confianza |
| RUR-E04 | **La caja de herramientas**: Olven necesita reparación antes de un traslado; Eren podría ayudar | pedir presupuesto en materiales, ofrecer espera, suspender viaje | no forzar encuentro entre S04 y S07; no mover carga sin acceso | herramienta, trabajo, inventario, tiempo |
| RUR-E05 | **La sed**: Elma desea sostener animales; Cail quiere dedicar tiempo a aprender | priorizar agua para necesidades urgentes conforme a derechos, buscar acceso real, posponer aprendizaje | el río regional no da agua potable o abrevadero a una parcela seca | agua, capacidades, jornada, pacto |
| RUR-E06 | **El paso**: Veya recibe consulta; caminante cree conocer un atajo; Arel posee una cautela distinta | pedir pruebas, reconocer ignorancia, explorar dentro de posibilidades, esperar o regresar | no afirmar puente, sendero o tiempo de viaje sin cartografía | conocimiento del lugar y decisión, solo tras exploración |
| RUR-E07 | **La costa interior**: Mira quiere limitar extracción; Neris contempla un traslado por agua | verificar permiso y barco, negociar cantidad, posponer o rechazar | no habilitar ferry, puerto, tala intensiva ni fauna nueva en Arven | recurso, consentimiento, acceso, conocimiento |
| RUR-E08 | **El precio del frío**: Arel prevé necesidad de abrigo; familia quiere intercambiar forraje | revisar reservas, buscar pacto, distribuir trabajo y cuidados | sin animales ni forraje instanciados, ninguna transferencia; no declarar invierno fijo | reservas, fatiga, reputación, necesidades |

## E01 — Diálogo de muestra, no respuesta obligatoria

**Viajero:** «Pago por todo lo que puedas traer».  
**Mara:** «Que puedas pagarlo no significa que me sobre».  
**Dela:** «Si prometiste un saco, necesito saber de cuál hablamos».  
**Opciones respetables:** comprobar si se prometió un lote preciso, reformular la cantidad, esperar, dejar constancia de una discrepancia, desistir. **No es una escena de “campesina tacaña”; nadie conoce automáticamente las reservas del otro.**

## E02 — El conflicto no equivale a culpa

**Toren:** «Si la viga no llega, alguien dormirá bajo la lluvia».  
**Saira:** «Y si cortamos donde no debemos, el problema durará más que la lluvia».  
Resolver con un permiso, una madera legítima o una negativa aceptada tiene más valor que una prueba de carisma que dispense leyes de Norgard.

## E06 — El valor dramático de no saber

**Caminante:** «Dicen que se atraviesa por detrás de las piedras».  
**Veya:** «Yo no puedo garantizar un lugar que no he comprobado».  
Una conversación no crea un vado; el jugador puede obtener información, pero no teletransportarse a una ruta imaginaria.

## E07 — La isla es finita

**Mira:** «El Manto Verde no es un almacén sin fondo».  
**Neris:** «También hay familias que necesitan reparar sus casas».  
No se decide automáticamente quién tiene razón. El problema solo puede resolverse si hay cuota, acceso, material, derecho y consecuencias evaluables.

## Matriz mínima para futura implementación
Cada escena necesita `sceneId`, `participantsInstantiated`, `triggerEvidence`, `localAccessVerified`, `knowledgeMask`, `legalAuthority`, `stockLedger`, `timeBudget`, `possibleChoices`, `refusalPaths`, `stateDelta`, `memoryRecipients` y `idempotencyKey`. La transición exige un único commit lógico de CoreRPG; una respuesta de IA no modifica jamás WorldState. Si el jugador retorna a la escena, los hechos ya consumados no se repiten por narración.

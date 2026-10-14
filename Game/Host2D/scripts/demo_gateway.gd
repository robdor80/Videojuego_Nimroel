extends RefCounted
## NIM-01: enrutador determinista de interfaz de pruebas.
## No consulta ni modifica CoreRPG. No es un LLM ni un parser de producción.

static func route(raw_text: String) -> Dictionary:
	var message: String = raw_text.strip_edges()
	if message.is_empty():
		return {
			"proposal_type": "empty",
			"demo_response": "Escribe una pregunta o una intención.",
			"portrait_demo": false,
			"world_mutated": false
		}

	var normalized: String = message.to_lower()
	var intent: String = "unclassified"
	var explanation: String = "La entrada se ha recibido. La clasificación libre corresponde a Gemini y su resolución al motor; no se ha ejecutado ninguna acción."

	if normalized.contains("veo") or normalized.contains("observo") or normalized.contains("mi alrededor"):
		intent = "query_perception"
		explanation = "Consulta de percepción reconocida para la demostración. CoreRPG deberá determinar qué se percibe desde la localización actual; no hay descripción del mundo validada todavía."
	elif normalized.contains("avanzo") or normalized.contains("camino") or normalized.contains("voy a") or normalized.contains("me acerco"):
		intent = "propose_movement"
		explanation = "Intención de desplazamiento recibida. La ruta, el tiempo y la nueva posición requieren una acción validada por CoreRPG. No se ha desplazado a nadie."
	elif normalized.contains("hablo") or normalized.contains("pregunto") or normalized.contains("converso"):
		intent = "propose_dialogue"
		explanation = "Intención de conversación recibida. La existencia, presencia, disponibilidad y conocimientos del interlocutor deben verificarse. No ha respondido ningún NPC real."
	elif normalized.contains("herrero") or normalized.contains("herrería") or normalized.contains("herreria"):
		intent = "query_information"
		explanation = "Consulta sobre un servicio recibida. La localización y el conocimiento del personaje dependen de la aldea generada, todavía no cargada."
	elif normalized.contains("guardo") or normalized.contains("guardar"):
		intent = "propose_save"
		explanation = "La orden de guardado se ha identificado, pero no existe un WorldState de partida conectado. Ningún archivo de guardado se ha creado."

	return {
		"proposal_type": intent,
		"demo_response": explanation,
		"portrait_demo": intent == "propose_dialogue",
		"world_mutated": false
	}

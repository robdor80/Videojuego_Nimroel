extends RefCounted
## Contrato de frontera Gemini para NIM-02. NO hay HTTP ni credenciales.
## Gemini propone y redacta; NUNCA valida hechos ni muta WorldState.

const API_VERSION := 1
const STATUS_UNAVAILABLE := "unavailable"

static func capabilities() -> Dictionary:
	return {
		"backend": "gemini",
		"api_version": API_VERSION,
		"interpretation_available": false,
		"narration_available": false,
		"reason": "No existe cliente Gemini autenticado ni contexto autorizado de CoreRPG."
	}

static func interpret(_player_text: String, _authorized_context: Dictionary) -> Dictionary:
	return {
		"status": STATUS_UNAVAILABLE,
		"error_code": "GEMINI_NOT_CONNECTED",
		"proposals": [],
		"world_mutated": false
	}

static func narrate(_authorized_result: Dictionary) -> Dictionary:
	return {
		"status": STATUS_UNAVAILABLE,
		"error_code": "GEMINI_NOT_CONNECTED",
		"speaker_id": "",
		"text": "",
		"world_mutated": false
	}

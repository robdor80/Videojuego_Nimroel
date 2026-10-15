extends RefCounted
## NIM-02: frontera única entre texto de interfaz y futuros servicios.
## MODO DEMO usa únicamente respuestas etiquetadas como simulador.
## MODO INTEGRACION se bloquea de forma explícita hasta disponer de
## CoreRPG y Gemini probados. Este archivo NO crea un segundo WorldState.

const DemoGateway = preload("res://scripts/demo_gateway.gd")
const CorePort = preload("res://scripts/core_port.gd")
const GeminiPort = preload("res://scripts/gemini_port.gd")
const VoicePort = preload("res://scripts/voice_port.gd")

const MODE_DEMO := "demo"
const MODE_INTEGRATION := "integration"
const MAX_MESSAGE_CHARS := 1500
const CONTRACT_VERSION := 1

static func capabilities() -> Dictionary:
	return {
		"contract_version": CONTRACT_VERSION,
		"core": CorePort.capabilities(),
		"gemini": GeminiPort.capabilities(),
		"voice": VoicePort.capabilities(),
		"integration_ready": false
	}

static func submit_text(raw_text: String, mode: String = MODE_DEMO, turn_id: int = 0) -> Dictionary:
	var text: String = raw_text.strip_edges()
	if text.is_empty():
		return _result("rejected", "EMPTY_TEXT", "Escribe un mensaje antes de enviarlo.", turn_id)
	if text.length() > MAX_MESSAGE_CHARS:
		return _result("rejected", "TEXT_TOO_LONG", "El mensaje supera el límite de 1500 caracteres.", turn_id)
	if mode != MODE_DEMO and mode != MODE_INTEGRATION:
		return _result("rejected", "INVALID_MODE", "Modo de interacción no reconocido.", turn_id)

	if mode == MODE_DEMO:
		var demo: Dictionary = DemoGateway.route(text)
		return {
			"contract_version": CONTRACT_VERSION,
			"turn_id": turn_id,
			"status": "demo",
			"error_code": "",
			"reply": str(demo.get("demo_response", "")),
			"reply_kind": "system_demo",
			"proposal_type": str(demo.get("proposal_type", "unclassified")),
			"portrait_demo": bool(demo.get("portrait_demo", false)),
			"world_mutated": false,
			"speaker_id": ""
		}

	# No llamar a un LLM con mundo desconocido y no presentar respuestas de
	# prueba como resultados del Core. Cada servicio anuncia disponibilidad real.
	if not bool(CorePort.capabilities().get("core_available", false)):
		return _result("blocked", "CORE_NOT_CONNECTED", "CoreRPG no está conectado: no se ha iniciado una partida ni ejecutado ninguna acción.", turn_id)
	if not bool(GeminiPort.capabilities().get("interpretation_available", false)):
		return _result("blocked", "GEMINI_NOT_CONNECTED", "Gemini no está conectado: no se ha interpretado ninguna intención.", turn_id)
	return _result("blocked", "INTEGRATION_NOT_VERIFIED", "La cadena completa todavía no se ha validado en esta versión.", turn_id)

static func _result(status: String, error_code: String, explanation: String, turn_id: int) -> Dictionary:
	return {
		"contract_version": CONTRACT_VERSION,
		"turn_id": turn_id,
		"status": status,
		"error_code": error_code,
		"reply": explanation,
		"reply_kind": "system",
		"proposal_type": "",
		"portrait_demo": false,
		"world_mutated": false,
		"speaker_id": ""
	}

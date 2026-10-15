extends Node
## NIM-03: diagnóstico opt-in, solo Windows/loopback. NO es gameplay.
## Envía únicamente el texto del cuadro al proxy local: ninguna clave viaja
## dentro de Godot. No se interpreta ni modifica el WorldState.
signal probe_finished(result: Dictionary)

const MAX_CHARS := 500
const PROXY_ENDPOINT := "http://127.0.0.1:8765/v1/intent-probe"
const ALLOWED_INTENTS := ["observar", "desplazarse", "dialogar", "otro"]
var _request: HTTPRequest
var _busy: bool = false

func _ready() -> void:
	_request = HTTPRequest.new()
	_request.timeout = 15.0
	add_child(_request)
	_request.request_completed.connect(_on_completed)

func probe(raw_text: String) -> void:
	var text: String = raw_text.strip_edges()
	if text.is_empty() or text.length() > MAX_CHARS:
		probe_finished.emit(_fail("INVALID_TEXT"))
		return
	if OS.has_feature("mobile"):
		probe_finished.emit(_fail("MOBILE_DIAGNOSTIC_NOT_CONFIGURED"))
		return
	if _busy:
		probe_finished.emit(_fail("DIAGNOSTIC_BUSY"))
		return
	_busy = true
	var payload: String = JSON.stringify({"purpose": "diagnostic_intent", "text": text})
	var err: Error = _request.request(
		PROXY_ENDPOINT, PackedStringArray(["Content-Type: application/json"]),
		HTTPClient.METHOD_POST, payload
	)
	if err != OK:
		_busy = false
		probe_finished.emit(_fail("LOCAL_PROXY_NOT_CONNECTED"))

func _on_completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	_busy = false
	if result != HTTPRequest.RESULT_SUCCESS:
		probe_finished.emit(_fail("LOCAL_PROXY_NOT_CONNECTED"))
		return
	probe_finished.emit(parse_response(response_code, body))

static func parse_response(response_code: int, body: PackedByteArray) -> Dictionary:
	# No confiar en el servicio sin esquema verificado; nunca reproducir su
	# texto libre como narración ni convertirlo en propuesta CoreRPG.
	if response_code != 200:
		if response_code == 503:
			return _fail("GEMINI_KEY_NOT_CONFIGURED")
		return _fail("GEMINI_DIAGNOSTIC_UNAVAILABLE")
	if body.size() > 2048:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	var parsed: Variant = JSON.parse_string(body.get_string_from_utf8())
	if not parsed is Dictionary:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if parsed.get("status", "") != "ok" or parsed.get("source", "") != "gemini":
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if parsed.get("kind", "") != "technical_diagnostic" or parsed.get("world_mutated", true) != false:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	var intent: Variant = parsed.get("intent", "")
	if not intent is String or not ALLOWED_INTENTS.has(intent):
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	return {
		"status": "ok", "intent": intent, "world_mutated": false,
		"reply_kind": "technical_diagnostic", "speaker_id": ""
	}

static func _fail(code: String) -> Dictionary:
	return {
		"status": "unavailable", "error_code": code, "world_mutated": false,
		"reply_kind": "system", "speaker_id": ""
	}

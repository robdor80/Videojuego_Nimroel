extends Node
## NIM-04: SOLO laboratorio MSI. Este resultado no equivale a interpretación
## de acciones ni conversación NPC y nunca entra en interaction_pipeline.gd.
signal probe_finished(result: Dictionary)

const MAX_CHARS := 500
const ENDPOINT := "http://127.0.0.1:8766/v1/provider-probe"
const TIERS := ["simple", "complex"]
const INTENTS := ["observar", "desplazarse", "dialogar", "otro"]
const MODELS := {
	"simple": {"gemini": "gemini-3.5-flash-lite", "openai": "gpt-6-luna"},
	"complex": {"gemini": "gemini-3.8-flash", "openai": "gpt-6.1-sol"}
}

var _http: HTTPRequest
var _busy: bool = false

func _ready() -> void:
	_http = HTTPRequest.new()
	_http.timeout = 28.0
	add_child(_http)
	_http.request_completed.connect(_completed)

func probe(raw_text: String, tier: String = "simple") -> void:
	var text: String = raw_text.strip_edges()
	if OS.has_feature("mobile"):
		probe_finished.emit(_fail("MOBILE_PROBE_DISABLED"))
		return
	if text.is_empty() or text.length() > MAX_CHARS or not TIERS.has(tier):
		probe_finished.emit(_fail("INVALID_PROBE"))
		return
	var token: String = OS.get_environment("NIMROEL_LOCAL_TOKEN")
	if token.is_empty():
		probe_finished.emit(_fail("LOCAL_AUTH_REQUIRED"))
		return
	if _busy:
		probe_finished.emit(_fail("DIAGNOSTIC_BUSY"))
		return
	var nonce: PackedByteArray = Crypto.new().generate_random_bytes(16)
	if nonce.size() != 16:
		probe_finished.emit(_fail("LOCAL_ID_UNAVAILABLE"))
		return
	_busy = true
	# El broker deduplica este identificador aleatorio durante cinco minutos.
	# No es una identidad del jugador ni un identificador de entidad CoreRPG.
	var payload: String = JSON.stringify({
		"purpose": "diagnostic_intent", "tier": tier,
		"text": text, "request_id": nonce.hex_encode()
	})
	var err: Error = _http.request(
		ENDPOINT,
		PackedStringArray(["Content-Type: application/json", "X-Nimroel-Token: " + token]),
		HTTPClient.METHOD_POST, payload
	)
	if err != OK:
		_busy = false
		probe_finished.emit(_fail("LOCAL_PROXY_NOT_CONNECTED"))

func _completed(result: int, response_code: int, _headers: PackedStringArray, body: PackedByteArray) -> void:
	_busy = false
	if result != HTTPRequest.RESULT_SUCCESS:
		probe_finished.emit(_fail("LOCAL_PROXY_NOT_CONNECTED"))
		return
	probe_finished.emit(parse_response(response_code, body))

static func parse_response(code: int, body: PackedByteArray) -> Dictionary:
	if code != 200:
		if code == 403:
			return _fail("LOCAL_AUTH_REQUIRED")
		if code == 429:
			# La cuota de llamadas local incluye un cupo facturable separado.
			# Solo aceptar códigos seguros: nunca imprimir mensajes upstream.
			if body.size() <= 512:
				var cap_doc := JSON.new()
				if cap_doc.parse(body.get_string_from_utf8()) == OK and cap_doc.data is Dictionary:
					var details: Dictionary = cap_doc.data
					if details.get("status") == "unavailable" and details.get("world_mutated", true) == false and details.get("error_code") == "LOCAL_PAID_CALL_CAP_REACHED":
						return _fail("LOCAL_PAID_CALL_CAP_REACHED")
			return _fail("LOCAL_CALL_CAP_REACHED")
		# Solo trasladar codigos tecnicos definidos por nuestro broker local.
		# Nunca mostrar cuerpos de Google/OpenAI ni contenido libre remoto.
		if (code == 409 or code == 502 or code == 503) and body.size() <= 512:
			var error_doc := JSON.new()
			if error_doc.parse(body.get_string_from_utf8()) == OK and error_doc.data is Dictionary:
				var details: Dictionary = error_doc.data
				var error_code: Variant = details.get("error_code", "")
				var reason: Variant = details.get("diagnostic_reason", "")
				var allowed_codes := [
					"PROVIDERS_TEMPORARILY_UNAVAILABLE", "PROVIDER_AUTH_UNAVAILABLE",
					"PROVIDER_KEY_NOT_CONFIGURED", "PROVIDER_OUTPUT_REJECTED",
					"PROVIDER_REQUEST_REJECTED",
					"PAID_PROVIDER_NOT_AUTHORIZED", "LOCAL_PAID_CALL_CAP_REACHED",
					"LOCAL_PROBE_BUSY", "LOCAL_DUPLICATE_IN_PROGRESS",
					"REQUEST_ID_REUSED", "LOCAL_REQUEST_CACHE_FULL"
				]
				var allowed_reasons := [
					"timeout", "network_error", "http_429", "http_500",
					"http_502", "http_503", "http_504"
				]
				if details.get("status") == "unavailable" and details.get("world_mutated", true) == false:
					if error_code is String and allowed_codes.has(error_code):
						var safe_reason: String = reason if reason is String and allowed_reasons.has(reason) else ""
						return _fail(error_code, safe_reason)
		return _fail("PROVIDER_UNAVAILABLE")
	if body.size() > 2048:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	var document := JSON.new()
	if document.parse(body.get_string_from_utf8()) != OK:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	var value: Variant = document.data
	if not value is Dictionary:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if value.get("status") != "ok" or value.get("kind") != "technical_diagnostic":
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if value.get("world_mutated", true) != false:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	var tier: Variant = value.get("tier")
	var source: Variant = value.get("source")
	var intent: Variant = value.get("intent")
	var model: Variant = value.get("model")
	var fallback: Variant = value.get("fallback_used")
	var latency: Variant = value.get("latency_ms")
	if not tier is String or not TIERS.has(tier):
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if not source is String or not MODELS[tier].has(source):
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if not model is String or MODELS[tier][source] != model:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if not intent is String or not INTENTS.has(intent):
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	if not fallback is bool or not (latency is float or latency is int) or latency < 0 or latency > 90000:
		return _fail("INVALID_DIAGNOSTIC_RESPONSE")
	return {
		"status": "ok", "reply_kind": "technical_diagnostic",
		"source": source, "model": model, "tier": tier, "intent": intent,
		"fallback_used": fallback, "latency_ms": int(latency),
		"world_mutated": false, "speaker_id": ""
	}

static func _fail(code: String, reason: String = "") -> Dictionary:
	return {
		"status": "unavailable", "error_code": code,
		"diagnostic_reason": reason,
		"world_mutated": false, "reply_kind": "system", "speaker_id": ""
	}

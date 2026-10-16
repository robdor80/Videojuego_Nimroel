extends SceneTree
## Offline: respuestas sintéticas para verificar fail-closed; no prueban ningún LLM.
const Provider = preload("res://scripts/provider_diagnostic.gd")
const Pipeline = preload("res://scripts/interaction_pipeline.gd")

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	var good: Dictionary = {
		"status": "ok", "kind": "technical_diagnostic",
		"source": "mistral", "model": "mistral-small-2603", "tier": "simple",
		"intent": "dialogar", "fallback_used": true,
		"latency_ms": 19, "world_mutated": false
	}
	var parsed: Dictionary = Provider.parse_response(200, JSON.stringify(good).to_utf8_buffer())
	if parsed.get("status") != "ok" or parsed.get("reply_kind") != "technical_diagnostic":
		errors.append("NIM04 respuesta mock válida rechazada")
	if parsed.get("world_mutated", true) or parsed.has("reply"):
		errors.append("NIM04 diagnóstico con poder de partida")
	# Regresión real detectada el 17/10: Godot rechazaba una respuesta OpenAI 200
	# válida porque faltaban openai/Luna/Sol en MODELS.
	for pair in [["simple", "gpt-6-luna"], ["complex", "gpt-6-sol"]]:
		var openai_ok: Dictionary = good.duplicate(true)
		openai_ok["source"] = "openai"
		openai_ok["model"] = pair[1]
		openai_ok["tier"] = pair[0]
		openai_ok["fallback_used"] = false
		var parsed_openai: Dictionary = Provider.parse_response(200, JSON.stringify(openai_ok).to_utf8_buffer())
		if parsed_openai.get("status") != "ok" or parsed_openai.get("model") != pair[1]:
			errors.append("NIM04 Godot rechaza OpenAI válido: " + str(pair[1]))
		openai_ok["model"] = "gpt-6-sol" if pair[0] == "simple" else "gpt-6-luna"
		if Provider.parse_response(200, JSON.stringify(openai_ok).to_utf8_buffer()).get("status") == "ok":
			errors.append("NIM04 permite modelo OpenAI de nivel equivocado")
	var paid_error: Dictionary = {"status": "unavailable", "error_code": "PAID_PROVIDER_NOT_AUTHORIZED", "world_mutated": false}
	if Provider.parse_response(503, JSON.stringify(paid_error).to_utf8_buffer()).get("error_code") != "PAID_PROVIDER_NOT_AUTHORIZED":
		errors.append("NIM04 oculta rechazo explícito de proveedor de pago")
	paid_error["error_code"] = "LOCAL_PAID_CALL_CAP_REACHED"
	if Provider.parse_response(429, JSON.stringify(paid_error).to_utf8_buffer()).get("error_code") != "LOCAL_PAID_CALL_CAP_REACHED":
		errors.append("NIM04 oculta límite local facturable")
	paid_error["error_code"] = "OTHER_UNTRUSTED_ERROR"
	if Provider.parse_response(429, JSON.stringify(paid_error).to_utf8_buffer()).get("error_code") != "LOCAL_CALL_CAP_REACHED":
		errors.append("NIM04 muestra código de error no autorizado")
	var broken: Array[Dictionary] = [
		{"status": "ok", "kind": "npc", "source": "mistral", "model": "mistral-small-2603", "tier": "simple", "intent": "dialogar", "fallback_used": false, "latency_ms": 19, "world_mutated": false},
		{"status": "ok", "kind": "technical_diagnostic", "source": "mistral", "model": "mistral-medium-3-5", "tier": "simple", "intent": "dialogar", "fallback_used": false, "latency_ms": 19, "world_mutated": false},
		{"status": "ok", "kind": "technical_diagnostic", "source": "gemini", "model": "gemini-3.8-flash", "tier": "simple", "intent": "dialogar", "fallback_used": false, "latency_ms": 19, "world_mutated": false},
		{"status": "ok", "kind": "technical_diagnostic", "source": "mistral", "model": "mistral-small-2603", "tier": "simple", "intent": "ejecutar", "fallback_used": false, "latency_ms": 19, "world_mutated": false},
		{"status": "ok", "kind": "technical_diagnostic", "source": "mistral", "model": "mistral-small-2603", "tier": "simple", "intent": "dialogar", "fallback_used": false, "latency_ms": 19, "world_mutated": true},
		{"status": "ok", "kind": "technical_diagnostic", "source": "mistral", "model": "mistral-small-2603", "tier": "simple", "intent": "dialogar", "fallback_used": "yes", "latency_ms": 19, "world_mutated": false},
	]
	for example in broken:
		if Provider.parse_response(200, JSON.stringify(example).to_utf8_buffer()).get("status") == "ok":
			errors.append("NIM04 aceptación de esquema inseguro")
	if Provider.parse_response(503, PackedByteArray()).get("status") == "ok":
		errors.append("NIM04 503 aceptado")
	var timeout_error: Dictionary = {"status": "unavailable", "error_code": "PROVIDERS_TEMPORARILY_UNAVAILABLE", "diagnostic_reason": "timeout", "world_mutated": false}
	var timeout_parsed: Dictionary = Provider.parse_response(503, JSON.stringify(timeout_error).to_utf8_buffer())
	if timeout_parsed.get("error_code") != "PROVIDERS_TEMPORARILY_UNAVAILABLE" or timeout_parsed.get("diagnostic_reason") != "timeout" or timeout_parsed.get("world_mutated", true):
		errors.append("NIM04 se perdio codigo tecnico timeout del broker")
	timeout_error["diagnostic_reason"] = "http_503"
	if Provider.parse_response(503, JSON.stringify(timeout_error).to_utf8_buffer()).get("diagnostic_reason") != "http_503":
		errors.append("NIM04 no distingue HTTP 503 remoto de timeout")
	timeout_error["diagnostic_reason"] = "API_KEY_SUPER_SECRETA"
	if Provider.parse_response(503, JSON.stringify(timeout_error).to_utf8_buffer()).get("diagnostic_reason") != "":
		errors.append("NIM04 permite texto remoto en diagnostico")
	timeout_error["error_code"] = "ATAQUE_NPC"
	if Provider.parse_response(503, JSON.stringify(timeout_error).to_utf8_buffer()).get("error_code") != "PROVIDER_UNAVAILABLE":
		errors.append("NIM04 permite texto ajeno del broker")
	timeout_error["error_code"] = "PROVIDERS_TEMPORARILY_UNAVAILABLE"
	timeout_error["world_mutated"] = true
	if Provider.parse_response(503, JSON.stringify(timeout_error).to_utf8_buffer()).get("error_code") != "PROVIDER_UNAVAILABLE":
		errors.append("NIM04 acepta supuesta mutacion de mundo")
	if Provider.parse_response(200, "not-json".to_utf8_buffer()).get("status") == "ok":
		errors.append("NIM04 basura aceptada")
	if Pipeline.submit_text("Hablar", Pipeline.MODE_INTEGRATION).get("error_code") != "CORE_NOT_CONNECTED":
		errors.append("NIM04 ha desbloqueado CoreRPG")
	if Pipeline.submit_text("Hablar", Pipeline.MODE_DEMO).get("status") != "demo":
		errors.append("NIM04 ha alterado demo")
	if errors.is_empty():
		print("NIM-04 SMOKE PASS: multiproveedor solo diagnóstico y Core intacto.")
		quit(0)
	else:
		for item in errors:
			push_error("NIM-04 SMOKE FAIL: " + item)
		quit(1)

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

extends SceneTree
## NIM-03 smoke sin red: los positivos remotos se certifican separadamente.
const Diagnostic = preload("res://scripts/gemini_diagnostic.gd")
const Pipeline = preload("res://scripts/interaction_pipeline.gd")

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	var trusted: Dictionary = Diagnostic.parse_response(200, JSON.stringify({
		"status": "ok", "source": "gemini", "kind": "technical_diagnostic",
		"intent": "observar", "world_mutated": false
	}).to_utf8_buffer())
	if trusted.get("status") != "ok" or trusted.get("reply_kind") != "technical_diagnostic":
		errors.append("Resultado diagnóstico válido no reconocido")
	for suspect in [
		{"status": "ok", "source": "gemini", "kind": "technical_diagnostic", "intent": "ejecutar", "world_mutated": false},
		{"status": "ok", "source": "gemini", "kind": "technical_diagnostic", "intent": "observar", "world_mutated": true},
		{"status": "ok", "source": "gemini", "kind": "npc", "intent": "observar", "world_mutated": false},
		{"status": "ok", "source": "fake", "kind": "technical_diagnostic", "intent": "observar", "world_mutated": false},
	]:
		var rejected: Dictionary = Diagnostic.parse_response(200, JSON.stringify(suspect).to_utf8_buffer())
		if rejected.get("status") == "ok" or rejected.get("world_mutated", true):
			errors.append("Respuesta de diagnóstico insegura aceptada")
	if Diagnostic.parse_response(503, PackedByteArray()).get("error_code") != "GEMINI_KEY_NOT_CONFIGURED":
		errors.append("Clave ausente mal identificada")
	if Diagnostic.parse_response(200, "{malformed".to_utf8_buffer()).get("status") == "ok":
		errors.append("JSON inválido aceptado")
	if Pipeline.submit_text("Avanzo", Pipeline.MODE_INTEGRATION).get("error_code") != "CORE_NOT_CONNECTED":
		errors.append("Regresión: la prueba de Gemini ha abierto gameplay sin Core")
	if Pipeline.submit_text("Hola", Pipeline.MODE_DEMO).get("status") != "demo":
		errors.append("Regresión: modo demo")
	if errors.is_empty():
		print("NIM-03 SMOKE PASS: diagnóstico aislado, parser fail-closed, Core intacto.")
		quit(0)
	else:
		for error in errors:
			push_error("NIM-03 SMOKE FAIL: " + error)
		quit(1)

extends SceneTree
## NIM-05: solo mocks de contrato Godot; ni API ni reproducción física.
const Provider = preload("res://scripts/provider_diagnostic.gd")
const Pipeline = preload("res://scripts/interaction_pipeline.gd")
const VoicePort = preload("res://scripts/voice_port.gd")

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	for pair in [
		[409, "LOCAL_DUPLICATE_IN_PROGRESS"],
		[409, "REQUEST_ID_REUSED"],
		[503, "LOCAL_PROBE_BUSY"],
		[503, "LOCAL_REQUEST_CACHE_FULL"],
	]:
		var body: Dictionary = {
			"status": "unavailable", "error_code": pair[1],
			"world_mutated": false
		}
		var result: Dictionary = Provider.parse_response(pair[0], JSON.stringify(body).to_utf8_buffer())
		if result.get("error_code") != pair[1] or result.get("world_mutated", true):
			errors.append("NIM05 error local seguro no conservado: " + str(pair[1]))
	var good: Dictionary = {
		"status": "ok", "kind": "technical_diagnostic",
		"source": "openai", "model": "gpt-6-luna", "tier": "simple",
		"intent": "otro", "fallback_used": true,
		"latency_ms": 24, "world_mutated": false
	}
	var parsed: Dictionary = Provider.parse_response(200, JSON.stringify(good).to_utf8_buffer())
	if parsed.get("status") != "ok" or not parsed.get("fallback_used", false):
		errors.append("NIM05 ruta fallback offline rechazada")
	if parsed.has("reply") or parsed.get("world_mutated", true):
		errors.append("NIM05 broker invade la narración")
	if Pipeline.submit_text("Hola", Pipeline.MODE_INTEGRATION).get("error_code") != "CORE_NOT_CONNECTED":
		errors.append("NIM05 desbloqueo indebido del Core")
	if VoicePort.capabilities().get("tts_available", true):
		errors.append("NIM05 declaró falsamente TTS de NPC disponible")
	if errors.is_empty():
		print("NIM-05 SMOKE PASS: fallback solo diagnóstico, Core y NPC bloqueados.")
		quit(0)
	else:
		for item in errors:
			push_error("NIM-05 SMOKE FAIL: " + item)
		quit(1)

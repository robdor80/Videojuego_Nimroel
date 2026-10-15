extends SceneTree
## NIM-02: validar ruta de turnos sin confundir demostración con juego real.

const Pipeline = preload("res://scripts/interaction_pipeline.gd")
const GeminiPort = preload("res://scripts/gemini_port.gd")
const CorePort = preload("res://scripts/core_port.gd")
const VoicePort = preload("res://scripts/voice_port.gd")

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	var cap: Dictionary = Pipeline.capabilities()
	if cap.get("integration_ready", true):
		errors.append("Integración completa anunciada sin prueba")
	if bool(cap.get("core", {}).get("core_available", true)):
		errors.append("CoreRPG marcado como disponible")
	if bool(cap.get("gemini", {}).get("interpretation_available", true)):
		errors.append("Gemini marcado como disponible")
	if bool(cap.get("voice", {}).get("asr_available", true)):
		errors.append("ASR marcado como disponible")

	var empty: Dictionary = Pipeline.submit_text("   ", Pipeline.MODE_DEMO, 1)
	_assert(empty, "rejected", "EMPTY_TEXT", false, errors)
	var long_text: Dictionary = Pipeline.submit_text("a".repeat(Pipeline.MAX_MESSAGE_CHARS + 1), Pipeline.MODE_DEMO, 2)
	_assert(long_text, "rejected", "TEXT_TOO_LONG", false, errors)
	var invalid: Dictionary = Pipeline.submit_text("Hola", "bogus", 3)
	_assert(invalid, "rejected", "INVALID_MODE", false, errors)
	var demo: Dictionary = Pipeline.submit_text("Hablo con un aldeano", Pipeline.MODE_DEMO, 4)
	_assert(demo, "demo", "", false, errors)
	if demo.get("reply_kind", "") != "system_demo" or demo.get("speaker_id", "!") != "":
		errors.append("La demo finge un interlocutor real")
	if demo.get("proposal_type", "") != "propose_dialogue":
		errors.append("La demo pierde la clasificación NIM-01")

	var blocked: Dictionary = Pipeline.submit_text("Avanzo", Pipeline.MODE_INTEGRATION, 5)
	_assert(blocked, "blocked", "CORE_NOT_CONNECTED", false, errors)
	if blocked.get("reply_kind", "") != "system" or blocked.get("portrait_demo", true):
		errors.append("La ausencia de Core se disfraza de respuesta NPC")
	if blocked.get("turn_id", -1) != 5:
		errors.append("No se conserva la identidad local del turno")
	if GeminiPort.interpret("Hola", {}).get("status", "") != "unavailable":
		errors.append("Gemini interpreta sin backend")
	if GeminiPort.narrate({}).get("text", "x") != "":
		errors.append("Gemini narra sin contexto verificado")
	if CorePort.submit({"action": "move"}).get("world_mutated", true):
		errors.append("Core ausente declara mutación")
	if VoicePort.synthesize("npc_demo", "Hola").get("status", "") != "unavailable":
		errors.append("Voz no enlazada sintetiza")
	var load_error: Error = change_scene_to_file("res://main.tscn")
	if load_error != OK:
		errors.append("La escena de Nimroel no se puede cargar")
	else:
		await process_frame
		await process_frame
		var scene: Node = current_scene
		if scene == null:
			errors.append("No existe escena principal")
		else:
			if not scene.has_method("submit_turn_for_test"):
				errors.append("La UI no utiliza el nuevo pipeline")
			else:
				var actual: Dictionary = scene.submit_turn_for_test("¿Qué veo?", Pipeline.MODE_INTEGRATION)
				_assert(actual, "blocked", "CORE_NOT_CONNECTED", false, errors)
			if scene.get_node_or_null("PanelConversacion/Contenido/BarraInferior/Pie/ModoIntegracion") == null:
				errors.append("No se muestra selector de modo")
			if scene.get_node_or_null("PanelConversacion/Contenido/CabeceraRelato/EstadoServicios") == null:
				errors.append("Falta estado visible de los servicios")
	if errors.is_empty():
		print("NIM-02 SMOKE PASS: flujo seguro, estados honestos y UI compatible.")
		quit(0)
	else:
		for error in errors:
			push_error("NIM-02 SMOKE FAIL: " + error)
		quit(1)

func _assert(actual: Dictionary, status: String, error_code: String, mutated: bool, errors: Array[String]) -> void:
	if str(actual.get("status", "")) != status:
		errors.append("Estado incorrecto: " + str(actual))
	if str(actual.get("error_code", "")) != error_code:
		errors.append("Código incorrecto: " + str(actual))
	if bool(actual.get("world_mutated", true)) != mutated:
		errors.append("WorldState supuestamente modificado")

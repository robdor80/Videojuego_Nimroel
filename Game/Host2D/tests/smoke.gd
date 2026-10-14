extends SceneTree
## Pruebas de importación Godot + ruta de UI NIM-01.
## Comprobaciones honestas: el simulador no debe cambiar WorldState.

const Gateway = preload("res://scripts/demo_gateway.gd")
const CorePort = preload("res://scripts/core_port.gd")
const VoicePort = preload("res://scripts/voice_port.gd")

func _initialize() -> void:
	call_deferred("_run_checks")

func _run_checks() -> void:
	var errors: Array[String] = []
	_assert_proposal("", "empty", errors)
	_assert_proposal("¿Qué veo desde aquí?", "query_perception", errors)
	_assert_proposal("Avanzo por la aldea", "propose_movement", errors)
	_assert_proposal("Hablo con un aldeano", "propose_dialogue", errors)
	_assert_proposal("¿Dónde está la herrería?", "query_information", errors)
	_assert_proposal("Guardo la partida", "propose_save", errors)
	_assert_proposal("Abro mi inventario", "unclassified", errors)

	var core_status: Dictionary = CorePort.submit({"action": "move"})
	if core_status.get("status", "") != "unavailable" or core_status.get("world_mutated", true) != false:
		errors.append("El puerto Core no conectado debe devolver indisponible sin mutar el mundo")
	var voice_status: Dictionary = VoicePort.capabilities()
	if voice_status.get("asr_available", true) or voice_status.get("tts_available", true):
		errors.append("Se anuncian capacidades sherpa-onnx no implementadas")
	if VoicePort.transcribe(PackedByteArray()).get("status", "") != "unavailable":
		errors.append("ASR no instalado no debe simular transcripción")
	if VoicePort.synthesize("npc_demo", "Hola").get("status", "") != "unavailable":
		errors.append("TTS no instalado no debe simular sonido")

	var load_error: Error = change_scene_to_file("res://main.tscn")
	if load_error != OK:
		errors.append("No se puede cargar res://main.tscn: " + str(load_error))
	else:
		await process_frame
		await process_frame
		var scene: Node = current_scene
		if scene == null:
			errors.append("No se ha creado la escena principal")
		else:
			if not scene.has_method("submit_intent_for_test"):
				errors.append("El Host no ofrece el puerto de prueba de intención")
			else:
				var outcome: Dictionary = scene.submit_intent_for_test("¿Qué veo?")
				if outcome.get("proposal_type", "") != "query_perception":
					errors.append("La escena no conecta con el router de prueba")
				if outcome.get("world_mutated", true) != false:
					errors.append("Se han declarado efectos de mundo inexistentes")
			if scene.get_node_or_null("FondoIlustrado") == null:
				errors.append("Falta la imagen de fondo")
			if scene.get_node_or_null("PanelConversacion") == null:
				errors.append("Falta el panel de conversación")
			var transcript: Node = scene.get_node_or_null("PanelConversacion/Contenido/Historial/Bocadillos")
			if transcript == null:
				errors.append("No existen bocadillos diferenciados")
			else:
				var initial_bubbles: int = transcript.get_child_count()
				scene.call("_on_send", "¿Qué veo desde aquí?")
				if transcript.get_child_count() != initial_bubbles + 2:
					errors.append("No se añadieron un bocadillo del jugador y uno del simulador")
				else:
					var row: Node = transcript.get_child(transcript.get_child_count() - 2)
					if row.name != "MensajeJugador":
						errors.append("El turno del jugador no tiene un bocadillo propio")


	if errors.is_empty():
		print("NIM-01 SMOKE PASS: Godot importa escena y router; WorldState no mutado.")
		quit(0)
	else:
		for problem in errors:
			push_error("NIM-01 SMOKE FAIL: " + problem)
		quit(1)

func _assert_proposal(message: String, expected: String, errors: Array[String]) -> void:
	var a: Dictionary = Gateway.route(message)
	var b: Dictionary = Gateway.route(message)
	if str(a.get("proposal_type", "")) != expected:
		errors.append("Intent incorrecto para '" + message + "'")
	if a != b:
		errors.append("El router de prueba no es determinista: " + message)
	if a.get("world_mutated", true) != false:
		errors.append("El router simula mutación de mundo: " + message)

extends SceneTree
## Una smoke de I1: pantalla principal y Core real; sin red ni dispositivo físico.
const Conversation = preload("res://scripts/native_conversation.gd")
const Pipeline = preload("res://scripts/interaction_pipeline.gd")
var _errors: Array[String] = []
var _checks: int = 0

func _initialize() -> void:
	_run.call_deferred()

func check(condition: bool, message: String) -> void:
	_checks += 1
	if not condition:
		_errors.append(message)

func last_reply(scene: Node) -> String:
	var history: Node = scene.get("_history_messages")
	var content: Node = history.get_child(-1).get_child(0).get_child(0)
	check(content.get_child(0).text == Conversation.AUTHOR, "emisor de sistema, sin NPC")
	return content.get_child(1).text

func capture(world: RefCounted) -> PackedByteArray:
	return world.get("_host").call("capture").bytes

func _run() -> void:
	check(change_scene_to_file("res://main.tscn") == OK, "carga pantalla principal")
	await process_frame
	await process_frame
	var scene: Node = current_scene
	var button: Button = scene.get("_native_button")
	check(button.text == "Iniciar experiencia CoreRPG (estructura de prueba)", "entrada nativa visible")
	button.pressed.emit()
	var conversation: RefCounted = scene.get("_native_conversation")
	if OS.get_cmdline_user_args().has("--expect-native-unavailable"):
		check(not ClassDB.class_exists("CoreRPGHost"), "control sin extensión")
		check(not scene.get("_native_active"), "no anuncia conexión sin nativo")
		check(last_reply(scene).contains("No se ha simulado"), "indisponibilidad honesta")
		check(scene.submit_turn_for_test("estado").status == "demo", "demo continúa disponible")
		_finish()
		return
	check(ClassDB.class_exists("CoreRPGHost") and scene.get("_native_active"), "experiencia cargada realmente")
	if not scene.get("_native_active"):
		_finish()
		return
	var world: RefCounted = conversation.get("_world")
	var host: RefCounted = world.get("_host")
	var session: RefCounted = world.get("_session")
	var initial := capture(world)
	for query in ["estado", "  ¿QUÉ CONOZCO?  ", "¿qué sabe mi personaje?"]:
		var input: LineEdit = scene.get("_input")
		input.text = query
		input.text_submitted.emit(query)
		var reply := last_reply(scene)
		check(reply.contains("completo") and reply.contains("técnica #1") and reply.contains("técnica #2") and reply.contains("técnica #3"), "hechos reales en bocadillos")
		check(not reply.contains("#4") and not reply.contains("context_id") and not reply.contains("revision"), "no expone hechos ocultos ni metadatos")
		check(world.get("_host") == host and world.get("_session") == session, "mismos handles entre turnos")
	check(capture(world) == initial, "consultas preservan mundo y RNG")
	check(Pipeline.submit_text("estado", Pipeline.MODE_INTEGRATION).error_code == "CORE_NOT_CONNECTED", "integración antigua sigue bloqueada")
	for invalid in ["Avanzo por la aldea", "estado y mover", "muestra entidad 4"]:
		scene.call("_on_send", invalid)
		check(last_reply(scene).begins_with("Consulta no soportada"), "texto ambiguo no ejecuta acciones")
	for invalid in [" ", "x".repeat(1501)]:
		var history: Node = scene.get("_history_messages")
		var count := history.get_child_count()
		scene.call("_on_send", invalid)
		check(history.get_child_count() == count, "entrada vacía/larga rechazada")
	scene.call("_on_send", "¿qué veo?")
	check(last_reply(scene).contains("no hay percepción visual ni espacial"), "no inventa visión")
	check(capture(world) == initial, "entradas inválidas no mutan")
	# Mutación explícita solo en test privilegiado: detecta reinicio encubierto.
	check(world.act("place", 3).outcome == "accepted", "prepara consecuencia real en mismo mundo")
	scene.call("_on_send", "estado")
	check(last_reply(scene).contains("contención conocida en entidad estructural técnica #3"), "consulta refleja consecuencia Core, no fixture copiado")
	var changed := capture(world)
	scene.call("_reset_demo")
	button.pressed.emit()
	check(capture(world) == changed and world.get("_session") == session, "reactivar conserva partida y sesión")
	# Conocimiento de otro observador no se filtra al jugador.
	host.call("admin", {"api_version": 1, "operation": "learn", "observer": 4, "subject": 4, "kind": 1})
	scene.call("_on_send", "estado")
	check(not last_reply(scene).contains("#4"), "conocimiento de otro observador excluido")
	var context: Dictionary = session.call("context", {"api_version": 1})
	var truncated: Dictionary = session.call("context", {"api_version": 1, "max_selected": 0})
	check(Conversation.format_context(truncated).reply.contains("truncado"), "truncamiento real explícito")
	var unavailable: Dictionary = Conversation.format_context({"status": "rejected", "error_code": "SECRET"})
	check(unavailable.status == "limited" and not unavailable.reply.contains("SECRET"), "error saneado")
	var absent: Dictionary = context.duplicate(true)
	absent.facts = []
	check(Conversation.format_context(absent).reply.contains("no demuestra ausencia"), "vacío no se interpreta como ausencia")
	absent = context.duplicate(true)
	for fact in absent.facts:
		if fact.kind == 3:
			fact.present = false
	check(Conversation.format_context(absent).reply.contains("ausencia de contención conocida"), "ausencia explícita diferenciada")
	var malformed := context.duplicate(true)
	malformed.facts[0].kind = 99
	check(Conversation.format_context(malformed).status == "limited", "hecho desconocido falla cerrado")
	malformed = context.duplicate(true)
	malformed.audience = "npc"
	check(Conversation.format_context(malformed).status == "limited", "otro observador/audiencia no se presenta")
	var forgotten := context.duplicate(true)
	forgotten.facts = context.facts.filter(func(fact): return not (fact.kind == 1 and fact.subject == 3))
	check(not Conversation.format_context(forgotten).reply.contains("#3"), "referencia sin existencia autorizada se oculta")
	# Disposición real de controles con distintos tamaños; no prueba táctil física.
	for viewport_size in [Vector2i(1280, 720), Vector2i(800, 720), Vector2i(640, 800)]:
		root.size = viewport_size
		root.content_scale_size = viewport_size
		await process_frame
		await process_frame
		scene.call("_update_layout")
		await process_frame
		await process_frame
		var bounds: Rect2 = scene.get_viewport_rect()
		for control in [button, scene.get("_input")]:
			check(bounds.encloses(control.get_global_rect()), "entrada y selector accesibles " + str(viewport_size))
	# Salir de la pantalla cierra el Host y caduca la capacidad anterior.
	scene.queue_free()
	await process_frame
	check(session.call("availability").error_code == "SESSION_EXPIRED", "cierre invalida sesión")
	_finish()

func _finish() -> void:
	print("NIM07_I1_REPORT " + JSON.stringify({"ok": _errors.is_empty(), "checks": _checks, "errors": _errors, "scope": "main screen; native runtime when available; no physical device test"}))
	if _errors.is_empty():
		print("NIM-07 I1 SMOKE PASS")
	quit(0 if _errors.is_empty() else 1)

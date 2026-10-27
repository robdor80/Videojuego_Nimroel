extends RefCounted
## Smoke focalizada: entrada principal, contexto nativo y límites. Sin proveedores.
const Conversation = preload("res://scripts/native_conversation.gd")
var errors: Array[String] = []
var checks := 0
var tree: SceneTree

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		errors.append(message)

func ask(scene: Node, text: String) -> String:
	var input: LineEdit = scene.get("_input")
	input.text = text
	input.text_submitted.emit(input.text)
	return scene.get("_history_messages").get_child(-1).get_child(0).get_child(0).get_child(1).text

func safe(text: String) -> bool:
	for forbidden in ["taberna", "#3", "#4", "#7", "local-tavern", "context_id", "revision", "413001", "estás en", "misión", "herrero"]:
		if text.to_lower().contains(forbidden):
			return false
	return true

func admin(host: RefCounted, subject: int, kind: int, operation: String = "revoke") -> void:
	check(host.call("admin", {"api_version": 1, "operation": operation, "observer": 6, "subject": subject, "kind": kind}).status == "ok", "Core " + operation + " fact " + str(kind))

func run(scene_tree: SceneTree) -> void:
	tree = scene_tree
	check(tree.change_scene_to_file("res://main.tscn") == OK, "pantalla principal")
	await tree.process_frame
	await tree.process_frame
	var scene := tree.current_scene
	scene.get("_v001_button").pressed.emit()
	check(scene.get("_native_active"), "botón V001 abre sesión real")
	if not scene.get("_native_active"):
		_finish()
		return
	var conversation: RefCounted = scene.get("_v001_conversation")
	var world: RefCounted = conversation.get("_world")
	var host: RefCounted = world.get("_host")
	var session: RefCounted = world.get("_session")
	var before: PackedByteArray = host.call("capture").bytes
	var samples := {
		"¿Qué conozco de esta aldea?": "modelo de aldea V1 agrícola-maderera",
		"¿Qué servicios conozco?": "herrería básica asociada a la aldea como servicio",
		"¿Qué sé de la herrería?": "ausencia de agregado poblacional",
		"¿Cuántos habitantes hay?": "50 habitantes y 48 pendientes de materializar",
		"¿Qué conozco de la herramienta?": "categoría de herramienta agrícola ordinaria",
		"¿Dónde está la herramienta?": "contenida estructuralmente en la capacidad de herrería básica",
		"¿De dónde procede mi personaje?": "No indica ubicación actual, vivienda ni procedencia biográfica",
		"  ¿QUE   POBLACION CONOZCO?  ": "50 habitantes",
		"¿Qué sé?": "origen poblacional conocido",
	}
	for text in samples:
		var answer := ask(scene, text)
		check(answer.contains(samples[text]), "respuesta enfocada: " + text)
		check(safe(answer), "sin hechos ocultos o ficción: " + text)
	check(ask(scene, "¿Qué puedo preguntar?").contains("¿qué servicios conozco?"), "ayuda disponible")
	for action in ["voy a la herrería", "hablo con el herrero", "reparo la herramienta"]:
		var answer := ask(scene, action)
		check(answer.contains("todavía no está implementada") and safe(answer), "límite de acción " + action)
	check(ask(scene, "¿Qué veo?").contains("no hay percepción visual ni espacial"), "sin percepción inventada")
	var location := ask(scene, "¿Dónde estoy?")
	check(location.contains("ubicación actual no está modelada") and safe(location), "origen no equivale a ubicación")
	check(ask(scene, "estado y voy a la herrería").begins_with("Consulta no soportada"), "no extrae peticiones compuestas")
	check(ask(scene, "¿Qué sé de la taberna?").begins_with("Consulta no soportada"), "no revela definición oculta")
	check(world.get("_session") == session and world.get("_host") == host and host.call("capture").bytes == before, "mismas capacidades; consultas sin mutación ni RNG")
	scene.call("_reset_demo")
	scene.call("_start_native")
	scene.call("_start_v001")
	check(world.get("_session") == session and host.call("capture").bytes == before, "volver demo/I1/V001 conserva sesión y bytes")
	var context: Dictionary = session.call("context", {"api_version": 1})
	# La semántica procede de definiciones y hechos, nunca del número de entidad.
	var remapped := context.duplicate(true)
	for fact in remapped.facts:
		fact.subject += 100
		if fact.reference > 0:
			fact.reference += 100
		if fact.target > 0:
			fact.target += 100
	check(Conversation.format_query(remapped, "tool", 106).reply.contains("contenida estructuralmente en la capacidad de herrería básica"), "IDs arbitrarios no asignan semántica")
	check(Conversation.format_query(context, "origin", 7).reply.contains("no consta"), "origen ajeno no se atribuye al jugador")
	var truncated: Dictionary = session.call("context", {"api_version": 1, "max_selected": 0})
	var answer: Dictionary = Conversation.format_query(truncated, "population", 6)
	check(answer.reply.contains("truncado") and answer.reply.contains("no consta") and not answer.reply.contains("50"), "truncamiento Core sin inventar población")
	for key in ["api_version", "context_contract_version", "audience"]:
		var malformed := context.duplicate(true)
		malformed[key] = 99 if key != "audience" else "npc"
		check(Conversation.format_query(malformed, "summary", 6).status == "limited", "rechaza contrato/audiencia " + key)
	var other: RefCounted = host.call("open_session", {"api_version": 1, "observer": 7, "audience": "player"}).session
	check(Conversation.format_query(other.call("context", {"api_version": 1}), "services", 7).reply.contains("no consta"), "existencia sola no autoriza etiqueta ni catálogo")
	# Retirar hechos REALES prueba que cada respuesta vuelve a consultar Core.
	admin(host, 1, 5)
	var unknown := ask(scene, "¿Cuántos habitantes hay?")
	check(unknown.contains("no consta") and not unknown.contains("50") and not unknown.contains("48"), "población retirada deja de contestarse")
	admin(host, 2, 2)
	var no_label := ask(scene, "¿Dónde está la herramienta?")
	check(no_label.contains("no tiene una etiqueta autorizada") and not no_label.contains("herrería"), "relación/ID no autoriza etiqueta sin definición")
	admin(host, 5, 3)
	check(ask(scene, "¿Dónde está la herramienta?").contains("Su contención no consta"), "desconocido no equivale a ausencia explícita")
	var removed: Dictionary = host.call("step", {"api_version": 1, "actions": [{"operation": "remove_containment", "actor": 6, "entity": 5}]})
	check(removed.status == "ok" and removed.results[0].outcome == "accepted", "test privilegiado prepara ausencia real de contención")
	admin(host, 5, 3, "learn")
	check(ask(scene, "¿Dónde está la herramienta?").contains("ausencia de contención de la herramienta"), "ausencia explícita Core se distingue de desconocimiento")
	admin(host, 6, 6)
	check(ask(scene, "¿De dónde procede mi personaje?").contains("no consta"), "no infiere origen desde relaciones o fixture")
	var changed: PackedByteArray = host.call("capture").bytes
	check(ask(scene, "estado").contains("no consta") and host.call("capture").bytes == changed, "consultas posteriores preservan nuevo estado Core")
	check(world.save_slot("../invalid").error_code == "INVALID_SAVE_SLOT", "I4 rechaza slot inseguro sin escribir")
	scene.queue_free()
	await tree.process_frame
	check(session.call("availability").error_code == "SESSION_EXPIRED", "salir cierra sesión")
	_finish()

func _finish() -> void:
	print("NIM07_I3_REPORT " + JSON.stringify({"ok": errors.is_empty(), "checks": checks, "errors": errors, "device_execution": "NOT TESTED"}))
	if errors.is_empty():
		print("NIM-07 I3 SMOKE PASS")
	tree.quit(0 if errors.is_empty() else 1)

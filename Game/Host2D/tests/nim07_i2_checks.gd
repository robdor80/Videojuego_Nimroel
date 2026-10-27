extends RefCounted
## One bounded I2 smoke, also executable against Windows PCK / Android assets.
const Pack = preload("res://scripts/v001_pack.gd")
const Conversation = preload("res://scripts/native_conversation.gd")
var errors: Array[String] = []
var checks := 0
var tree: SceneTree
func run(scene_tree: SceneTree) -> void:
	tree = scene_tree
	await _run()
func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		errors.append(message)
func reply(scene: Node) -> String:
	return scene.get("_history_messages").get_child(-1).get_child(0).get_child(0).get_child(1).text
func _run() -> void:
	var bundle := Pack.read_bundle()
	check(bundle.status == "ok" and bundle.files.size() == 9, "FileAccess res:// nine files")
	if bundle.status != "ok":
		_finish()
		return
	check(tree.change_scene_to_file("res://main.tscn") == OK, "main screen")
	await tree.process_frame
	await tree.process_frame
	var scene := tree.current_scene
	scene.get("_v001_button").pressed.emit()
	check(scene.get("_native_active") and scene.get("_subtitle").text.contains("V001"), "V001 started via main")
	if not scene.get("_native_active"):
		_finish()
		return
	var conversation: RefCounted = scene.get("_v001_conversation")
	var world: RefCounted = conversation.get("_world")
	var host: RefCounted = world.get("_host")
	var session: RefCounted = world.get("_session")
	var diagnostics: Dictionary = host.call("diagnostics")
	check(diagnostics.entities == 7 and diagnostics.catalog_size == 4 and diagnostics.definition_bindings == 4, "real Core identities/catalog/bindings")
	var before: PackedByteArray = host.call("capture").bytes
	var input: LineEdit = scene.get("_input")
	input.text = "estado"
	input.text_submitted.emit(input.text)
	var response := reply(scene)
	check(response.contains("modelo de aldea V1") and response.contains("herrería básica") and response.contains("herramienta agrícola ordinaria"), "authorized Core definition bindings")
	check(response.contains("declara 50 habitantes y 48 pendientes de materializar") and response.contains("ausencia de agregado poblacional"), "known population and absence")
	check(response.contains("asociada a la aldea como servicio") and response.contains("origen poblacional conocido de tu observador"), "authorized relation and origin")
	check(not response.contains("#3") and not response.contains("#4") and not response.contains("#7") and not response.contains("taberna"), "hidden identities/definition excluded")
	check(not response.contains("context_id") and not response.contains("revision") and not response.contains("413001"), "no privileged metadata")
	var other: RefCounted = host.call("open_session", {"api_version": 1, "observer": 7, "audience": "npc"}).session
	var other_context: Dictionary = other.call("context", {"api_version": 1})
	check(other_context.facts.size() == 2 and other_context.facts[1].subject == 3, "second observer has separate knowledge")
	check(Conversation.format_context(other_context, true).status == "limited", "NPC audience rejected by presenter")
	var extra: RefCounted = host.call("open_session", {"api_version": 1, "observer": 6, "audience": "player"}).session
	check(extra.call("context", {"api_version": 1, "subject": 3}).facts.is_empty(), "hidden subject query empty")
	check(Conversation.format_context(extra.call("context", {"api_version": 1, "max_selected": 0}), true).reply.contains("truncado"), "truncation explicit")
	scene.call("_on_send", "¿qué veo?")
	check(reply(scene).contains("no hay percepción visual ni espacial"), "no invented vision")
	scene.call("_on_send", "reparar herramienta")
	check(reply(scene).begins_with("Consulta no soportada"), "no I3 gameplay")
	var issued: Dictionary = session.call("context", {"api_version": 1})
	check(session.call("submit", {"api_version": 1, "context_id": issued.context_id, "request_id": 1, "operation": "place", "target": 1}).error_code == "OPERATION_DENIED", "V001 session has no movement grants")
	check(host.call("capture").bytes == before, "queries/rejections preserve Core/RNG")
	check(world.save_slot().error_code == "CONTENT_PERSISTENCE_PENDING_I4", "no unverified content save")
	# Test-only privileged session: observe real world tables without exporting WorldState.
	for subject in [1, 2, 3, 4, 5, 6, 7]:
		host.call("admin", {"api_version": 1, "operation": "learn", "observer": 4, "subject": subject, "kind": 1})
	for spec in [{"subject": 3, "kind": 2}, {"subject": 2, "kind": 3}, {"subject": 3, "kind": 3}, {"subject": 6, "kind": 3}, {"subject": 7, "kind": 6}, {"subject": 1, "kind": 4, "relation_kind": 2, "target": 4}, {"subject": 7, "kind": 4, "relation_kind": 3, "target": 1}]:
		var request: Dictionary = spec.duplicate()
		request.merge({"api_version": 1, "operation": "learn", "observer": 4})
		check(host.call("admin", request).status == "ok", "privileged fixture table check " + str(spec))
	var inspector: RefCounted = host.call("open_session", {"api_version": 1, "observer": 4, "audience": "ai"}).session
	var facts: Array = inspector.call("context", {"api_version": 1}).facts
	check(facts.any(func(f): return f.subject == 3 and f.kind == 2 and f.definition_id.ends_with("local-tavern"))
		and facts.any(func(f): return f.subject == 2 and f.kind == 3 and f.reference == 1)
		and facts.any(func(f): return f.subject == 3 and f.kind == 3 and f.reference == 1)
		and facts.any(func(f): return f.subject == 6 and f.kind == 3 and not f.present)
		and facts.any(func(f): return f.subject == 7 and f.kind == 6 and f.reference == 1)
		and facts.any(func(f): return f.subject == 1 and f.kind == 4 and f.relation_kind == "2" and f.target == 4 and f.present)
		and facts.any(func(f): return f.subject == 7 and f.kind == 4 and f.relation_kind == "3" and f.target == 1 and f.present), "real service containment, boundary, origins and association; observer uncontained")
	var stable: PackedByteArray = host.call("capture").bytes
	for change in ["hash", "version", "missing", "extra"]:
		var bad: Dictionary = bundle.files.duplicate(true)
		if change == "hash":
			bad["resources/models/v1.json"][0] = 0
		elif change == "version":
			bad["content-lock.json"] = bad["content-lock.json"].get_string_from_utf8().replace("0.1.0", "0.1.1").to_utf8_buffer()
		elif change == "missing":
			bad.erase("integration-fixture.json")
		else:
			bad["extra.json"] = "{}".to_utf8_buffer()
		var rejected: Dictionary = host.call("initialize_v001", {"api_version": 1, "files": bad})
		check(rejected.status == "rejected" and host.call("capture").bytes == stable and session.call("availability").status == "ok", "transactional rejection " + change)
	var empty: RefCounted = ClassDB.instantiate("CoreRPGHost")
	check(empty.call("initialize_v001", {"api_version": 1, "files": {}}).status == "rejected" and not empty.call("diagnostics").initialized, "no partial first campaign")
	check(host.call("restore", stable).status == "ok" and host.call("capture").bytes == stable and session.call("availability").error_code == "SESSION_EXPIRED", "catalog-aware in-memory restore invalidates old capabilities")
	check(host.call("initialize_v001", {"api_version": 1, "files": bundle.files}).status == "ok" and host.call("capture").bytes == before, "deterministic rebuild matches initial Core bytes")
	for viewport_size in [Vector2i(1280, 720), Vector2i(800, 720), Vector2i(640, 800)]:
		tree.root.size = viewport_size
		tree.root.content_scale_size = viewport_size
		await tree.process_frame
		await tree.process_frame
		scene.call("_update_layout")
		await tree.process_frame
		await tree.process_frame
		check(scene.get_viewport_rect().encloses(scene.get("_v001_button").get_global_rect()), "V001 selector accessible " + str(viewport_size))
	scene.call("_start_native")
	check(scene.get("_native_conversation").get("_world").get("_host").call("diagnostics").entities == 4, "neutral I1 retained independently")
	scene.queue_free()
	await tree.process_frame
	_finish()
func _finish() -> void:
	print("NIM07_I2_REPORT " + JSON.stringify({"ok": errors.is_empty(), "checks": checks, "errors": errors, "device_execution": "NOT TESTED"}))
	if errors.is_empty():
		print("NIM-07 I2 SMOKE PASS")
	tree.quit(0 if errors.is_empty() else 1)

extends RefCounted
## Única smoke I4: el driver arranca write/read como procesos independientes.
const Save = preload("res://scripts/v001_save_store.gd")
const Conversation = preload("res://scripts/native_conversation.gd")
var errors: Array[String] = []
var checks := 0
var tree: SceneTree
var phase: String
var proof: Dictionary = {}

class RestoreSpy extends RefCounted:
	var calls := 0
	func restore(_bytes: PackedByteArray) -> Dictionary:
		calls += 1
		return {"status": "ok"}

func check(ok: bool, message: String) -> void:
	checks += 1
	if not ok:
		errors.append(message)

func put(path: String, bytes: PackedByteArray) -> void:
	var file := FileAccess.open(path, FileAccess.WRITE)
	check(file != null, "test abre archivo")
	if file != null:
		file.store_buffer(bytes)
		file.close()

func roll(host: RefCounted) -> String:
	var result: Dictionary = host.call("step", {"api_version": 1, "actions": [{"operation": "roll", "actor": 6, "stream": 413, "minimum": 1, "maximum": 1000000}]})
	check(result.status == "ok" and result.results[0].outcome == "accepted", "sonda RNG privilegiada de test")
	return result.results[0].roll_value

func response(scene: Node) -> String:
	return scene.get("_history_messages").get_child(-1).get_child(0).get_child(0).get_child(1).text

func run(scene_tree: SceneTree, requested_phase: String) -> void:
	tree = scene_tree
	phase = requested_phase
	check(tree.change_scene_to_file("res://main.tscn") == OK, "pantalla principal")
	await tree.process_frame
	await tree.process_frame
	var scene := tree.current_scene
	var path := Save.path_for("treskal")
	var witness_path := Save.DIRECTORY.path_join("i4-witness.json")
	if phase == "write":
		# CI uses a fresh temporary user directory; never delete an owner's saves.
		check(not FileAccess.file_exists(path), "directorio de prueba aislado y vacío")
		scene.get("_v001_button").pressed.emit()
		var conversation: RefCounted = scene.get("_v001_conversation")
		var world: RefCounted = conversation.get("_world")
		var host: RefCounted = world.get("_host")
		check(host != null and scene.get("_native_active"), "inicia V001 real por botón")
		if host == null:
			_finish()
			return
		var catalog_only: RefCounted = ClassDB.instantiate("CoreRPGHost")
		var bundle: Dictionary = preload("res://scripts/v001_pack.gd").read_bundle()
		var prepared: Dictionary = catalog_only.call("prepare_v001_restore", {"api_version": 1, "files": bundle.files})
		check(prepared.status == "ok" and catalog_only.call("diagnostics").entities == 0 and catalog_only.call("diagnostics").definition_bindings == 0 and catalog_only.call("diagnostics").catalog_size == 4, "preparar restore verifica catálogo SIN generar fixture")
		check(prepared.metadata.generation_context_sha256 == "6ad814ba488e8bc26a9d5d185f530d70f608de34264aef6fe62d3b2d77c063cd", "huella fija de receta canónica inicial")
		var initial: PackedByteArray = host.call("capture").bytes
		var removed: Dictionary = host.call("step", {"api_version": 1, "actions": [{"operation": "remove_containment", "actor": 6, "entity": 5}]})
		check(removed.status == "ok" and removed.results[0].outcome == "accepted", "mutación test distinta del fixture")
		check(host.call("admin", {"api_version": 1, "operation": "learn", "observer": 6, "subject": 5, "kind": 3}).status == "ok", "Core recuerda ausencia actualizada")
		check(host.call("admin", {"api_version": 1, "operation": "revoke", "observer": 6, "subject": 1, "kind": 5}).status == "ok", "retira conocimiento de población")
		roll(host)
		var saved: PackedByteArray = host.call("capture").bytes
		check(saved != initial, "bytes y RNG difieren del fixture inicial")
		var tool: String = conversation.submit_text("¿Dónde está la herramienta?").reply
		var population: String = conversation.submit_text("¿Cuántos habitantes hay?").reply
		check(tool.contains("ausencia de contención") and population.contains("no consta"), "respuestas del estado modificado")
		scene.get("_save_button").pressed.emit()
		check(response(scene).contains("Partida V001 guardada"), "Guardar real de la UI")
		var loaded := Save.read_package(path, world.get("_metadata"))
		check(loaded.status == "ok" and loaded.bytes == saved, "archivo contiene bytes Core auténticos")
		check(host.call("capture").bytes == saved, "guardar no consume RNG ni modifica mundo")
		var witness := {"writer_pid": OS.get_process_id(), "core_sha256": Save.digest(saved), "tool": tool, "population": population, "next_roll": roll(host), "metadata": world.get("_metadata")}
		proof = {"writer_pid": OS.get_process_id(), "snapshot_sha256": Save.digest(saved), "initial_sha256": Save.digest(initial), "generation_context_sha256": world.get("_metadata").generation_context_sha256}
		put(witness_path, JSON.stringify(witness).to_utf8_buffer())
	else:
		var witness = JSON.parse_string(FileAccess.get_file_as_string(witness_path))
		check(witness is Dictionary, "testigo de ejecución anterior")
		if not witness is Dictionary:
			_finish()
			return
		check(int(witness.writer_pid) != OS.get_process_id(), "DOS procesos Godot independientes")
		proof = {"writer_pid": int(witness.writer_pid), "reader_pid": OS.get_process_id(), "snapshot_sha256": witness.core_sha256, "generation_context_sha256": witness.metadata.generation_context_sha256}
		var conversation: RefCounted = scene.get("_v001_conversation")
		var world: RefCounted = conversation.get("_world")
		check(world.get("_host") == null, "reanudación fría sin inicializar fixture")
		scene.get("_resume_entry").pressed.emit()
		check(scene.get("_native_active") and response(scene).contains("Partida V001 reanudada"), "reanuda desde entrada principal")
		var host: RefCounted = world.get("_host")
		if host == null:
			_finish()
			return
		var session: RefCounted = world.get("_session")
		var saved: PackedByteArray = host.call("capture").bytes
		check(Save.digest(saved) == witness.core_sha256, "mismo snapshot Core completo y RNG")
		check(conversation.submit_text("¿Dónde está la herramienta?").reply == witness.tool, "misma ausencia guardada; no fixture")
		check(conversation.submit_text("¿Cuántos habitantes hay?").reply == witness.population, "mismo conocimiento revocado")
		check(host.call("diagnostics").catalog_size == 4 and host.call("diagnostics").definition_bindings == 4, "catálogo auténtico y bindings restaurados")
		check(roll(host) == witness.next_roll, "continuidad RNG entre procesos")
		scene.get("_resume_button").pressed.emit()
		check(session.call("availability").error_code == "SESSION_EXPIRED", "restore exitoso caduca capacidad anterior")
		check(host.call("diagnostics").initialized == false, "Host anterior cerrado tras commit")
		host = world.get("_host")
		session = world.get("_session")
		check(session.call("availability").status == "ok" and world.get("_request_id") == 0, "nueva capacidad y secuencia reiniciada")
		var context: Dictionary = session.call("context", {"api_version": 1})
		check(session.call("submit", {"api_version": 1, "context_id": context.context_id, "request_id": 1, "operation": "remove_containment"}).error_code == "OPERATION_DENIED", "nueva sesión sin permisos de acción")
		var installed: Dictionary = world.get("_metadata")
		check(installed == witness.metadata, "misma identidad instalada verificada")
		var original := FileAccess.get_file_as_bytes(path)
		var spy := RestoreSpy.new()
		# Every metadata field checked before restore, including correct DefinitionIds
		# but wrong publication/context/schema. Spy proves no Core restore call.
		for key in installed:
			var wrong := installed.duplicate()
			wrong[key] = "2" if key == "save_schema" else "incompatible"
			put(path, Save.encode(saved, wrong))
			var denied := Save.load_save(spy, "treskal", installed)
			check(denied.status == "rejected" and spy.calls == 0, "metadata rechazada antes de restore: " + key)
			check(world.load_slot("treskal").status == "rejected" and world.get("_host") == host and world.get("_session") == session and session.call("availability").status == "ok" and host.call("capture").bytes == saved, "incompatibilidad conserva campaña y sesión: " + key)
		# Corruption, truncation, future magic, excess size, unknown keys, duplicate keys.
		var corrupt := original.duplicate()
		corrupt[-1] ^= 1
		var future := original.duplicate()
		future[0] = 0
		var excessive := PackedByteArray()
		excessive.resize(Save.MAX_PACKAGE + 1)
		for broken in [original.slice(0, 10), original.slice(0, -1), corrupt, future, excessive]:
			put(path, broken)
			check(Save.load_save(spy, "treskal", installed).status == "rejected" and spy.calls == 0, "corrupción rechazada antes de restore")
			check(world.load_slot("treskal").status == "rejected" and session.call("availability").status == "ok" and host.call("capture").bytes == saved, "corrupción conserva partida activa")
		var unknown := installed.duplicate()
		unknown["extra"] = "unknown"
		put(path, Save.encode(saved, unknown))
		check(Save.load_save(spy, "treskal", installed).error_code == "SAVE_HEADER" and spy.calls == 0, "inventario externo cerrado")
		var header_size := original.decode_u32(8)
		var duplicate_header := ("{\"save_schema\":\"1\"," + original.slice(12, 12 + header_size).get_string_from_utf8().substr(1)).to_utf8_buffer()
		var duplicate := original.slice(0, 12)
		duplicate.encode_u32(8, duplicate_header.size())
		duplicate.append_array(duplicate_header)
		duplicate.append_array(saved)
		put(path, duplicate)
		check(Save.load_save(spy, "treskal", installed).error_code == "SAVE_HEADER" and spy.calls == 0, "claves duplicadas rechazadas")
		var wrong_core := Save.encode("not Core bytes".to_utf8_buffer(), installed)
		put(path, wrong_core)
		check(world.load_slot("treskal").error_code == "LOAD_REJECTED" and world.get("_host") == host and session.call("availability").status == "ok" and host.call("capture").bytes == saved, "fallo Core real conserva Host y capacidad activos")
		var neutral: RefCounted = ClassDB.instantiate("CoreRPGHost")
		neutral.call("initialize", {"api_version": 1, "seed": "42", "entities": 1})
		put(path, Save.encode(neutral.call("capture").bytes, installed))
		check(world.load_slot("treskal").error_code == "INVALID_OBSERVER" and world.get("_host") == host and world.get("_session") == session and host.call("capture").bytes == saved, "fallo de reapertura de sesión conserva partida activa")
		for slot in ["../treskal", "", "a/b", "a\\b", "a.b", "á", "a".repeat(33)]:
			check(world.save_slot(slot).error_code == "INVALID_SAVE_SLOT" and world.load_slot(slot).error_code == "INVALID_SAVE_SLOT", "slot inseguro rechazado")
		put(path, original)
		# Core-invalid but checksum-coherent primary must NOT replace a good backup.
		put(path + ".bak", original)
		put(path, wrong_core)
		check(world.save_slot("treskal").error_code == "SAVE_EXISTING_INVALID" and FileAccess.get_file_as_bytes(path + ".bak") == original and FileAccess.get_file_as_bytes(path) == wrong_core, "Core inválido con checksum coherente no destruye backup")
		put(path, Save.encode(neutral.call("capture").bytes, installed))
		check(world.save_slot("treskal").error_code == "SAVE_EXISTING_INVALID" and FileAccess.get_file_as_bytes(path + ".bak") == original, "observador inválido no destruye backup")
		put(path, original)
		# Valid overwrite makes backup. Partial temp must never be treated as committed.
		check(world.save_slot("treskal").status == "ok" and FileAccess.get_file_as_bytes(path + ".bak") == original, "sobrescritura segura conserva backup")
		put(path + ".tmp", "partial".to_utf8_buffer())
		check(world.load_slot("treskal").status == "ok", "temporal parcial ignorado con primario válido")
		DirAccess.remove_absolute(path)
		var recovered: Dictionary = world.load_slot("treskal")
		check(recovered.status == "ok" and recovered.recovered_backup and FileAccess.file_exists(path + ".bak") and not FileAccess.file_exists(path), "rename interrumpido recupera backup con aviso sin promoverlo")
		host = world.get("_host")
		session = world.get("_session")
		put(path, corrupt)
		check(world.load_slot("treskal").status == "rejected" and world.get("_session") == session, "primario corrupto no usa backup silenciosamente")
		check(world.save_slot("treskal").error_code == "SAVE_EXISTING_INVALID" and FileAccess.get_file_as_bytes(path + ".bak") == original and FileAccess.get_file_as_bytes(path) == corrupt, "guardar no destruye backup ni primario corrupto")
		scene.get("_resume_button").pressed.emit()
		check(response(scene).contains("no es válido") and scene.get("_backup_button").visible, "UI informa fallo y ofrece recuperación explícita")
		scene.get("_backup_button").pressed.emit()
		check(response(scene).contains("copia de seguridad") and FileAccess.get_file_as_bytes(path) == corrupt, "UI recupera backup explícitamente sin reemplazar corrupción")
		# A path occupied by a directory deterministically fails commit; good backup survives.
		DirAccess.remove_absolute(path)
		DirAccess.make_dir_absolute(path)
		check(world.save_slot("treskal").status != "ok" and FileAccess.get_file_as_bytes(path + ".bak") == original, "fallo I/O conserva última copia buena")
		DirAccess.remove_absolute(path)
		put(path, original)
		check(world.save_slot("treskal").status == "ok", "guardado posterior válido reemplaza temporal parcial")
		for dimensions in [Vector2i(1280, 720), Vector2i(800, 720), Vector2i(640, 800)]:
			tree.root.size = dimensions
			tree.root.content_scale_size = dimensions
			scene.call("_update_layout")
			for frame in range(5):
				await tree.process_frame
			check(scene.get_viewport_rect().encloses(scene.get("_save_button").get_global_rect()) and scene.get_viewport_rect().encloses(scene.get("_resume_button").get_global_rect()) and scene.get("_history_scroll").size.y >= 48, "controles y lectura útiles: " + str(dimensions))
		check(not response(scene).contains("sha256") and not response(scene).contains("user://"), "UI sin metadatos ni rutas internas")
		var current_session: RefCounted = world.get("_session")
		scene.call("_reset_demo")
		check(not scene.get("_save_row").visible, "controles ocultos en demo")
		scene.call("_start_native")
		check(not scene.get("_save_row").visible, "controles ocultos en I1")
		scene.call("_start_v001")
		check(world.get("_session") == current_session and scene.get("_save_row").visible, "volver V001 conserva sesión recuperada")
		scene.queue_free()
		await tree.process_frame
		check(current_session.call("availability").error_code == "SESSION_EXPIRED", "salida cierra nuevas capacidades")
	_finish()

func _finish() -> void:
	print("NIM07_I4_REPORT " + JSON.stringify({"ok": errors.is_empty(), "phase": phase, "pid": OS.get_process_id(), "proof": proof, "checks": checks, "errors": errors, "device_execution": "NOT TESTED"}))
	if errors.is_empty():
		print("NIM-07 I4 SMOKE PASS " + phase)
	tree.quit(0 if errors.is_empty() else 1)

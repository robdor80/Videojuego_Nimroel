extends RefCounted
## I/O privilegiado del Host. Los bytes completos nunca se entregan a sesiones.
## El Core valida/serializa; este archivo solo decide rutas y comprueba I/O.
const DIRECTORY := "user://core_saves"
const MAX_BYTES := 1048576

static func _path(slot: String) -> String:
	return slot_path(slot, DIRECTORY, ".core")

static func slot_path(slot: String, directory: String, extension: String) -> String:
	if slot.is_empty() or slot.length() > 32:
		return ""
	for character in slot:
		if not character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-":
			return ""
	return directory.path_join(slot + extension)

static func _error(code: String, io_error: int = OK) -> Dictionary:
	return {"api_version": 1, "status": "rejected", "error_code": code, "io_error": io_error}

static func save(host: RefCounted, slot: String) -> Dictionary:
	var path := _path(slot)
	if path.is_empty():
		return _error("INVALID_SAVE_SLOT")
	var captured: Dictionary = host.call("capture")
	if captured.get("status") != "ok":
		return captured
	var created := DirAccess.make_dir_recursive_absolute(DIRECTORY)
	if created != OK:
		return _error("SAVE_DIRECTORY_FAILED", created)
	var temporary := path + ".tmp"
	var backup := path + ".bak"
	var file := FileAccess.open(temporary, FileAccess.WRITE)
	if file == null:
		return _error("SAVE_OPEN_FAILED", FileAccess.get_open_error())
	file.store_buffer(captured.bytes)
	file.flush()
	var written := file.get_error()
	file.close()
	if written != OK:
		DirAccess.remove_absolute(temporary)
		return _error("SAVE_WRITE_FAILED", written)
	if FileAccess.file_exists(path):
		if FileAccess.file_exists(backup):
			var removed := DirAccess.remove_absolute(backup)
			if removed != OK:
				DirAccess.remove_absolute(temporary)
				return _error("SAVE_BACKUP_FAILED", removed)
		var moved := DirAccess.rename_absolute(path, backup)
		if moved != OK:
			DirAccess.remove_absolute(temporary)
			return _error("SAVE_BACKUP_FAILED", moved)
	var committed := DirAccess.rename_absolute(temporary, path)
	if committed != OK:
		var rollback := OK
		if FileAccess.file_exists(backup):
			rollback = DirAccess.rename_absolute(backup, path)
		DirAccess.remove_absolute(temporary)
		var failure := _error("SAVE_COMMIT_FAILED", committed)
		failure["rollback_error"] = rollback
		return failure
	return {"api_version": 1, "status": "ok", "error_code": "OK"}

static func load_save(host: RefCounted, slot: String) -> Dictionary:
	var path := _path(slot)
	if path.is_empty():
		return _error("INVALID_SAVE_SLOT")
	var recovered := false
	# Recovery only for an interrupted rename, never silently replace corrupt data.
	if not FileAccess.file_exists(path) and FileAccess.file_exists(path + ".bak"):
		path += ".bak"
		recovered = true
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return _error("LOAD_OPEN_FAILED", FileAccess.get_open_error())
	if file.get_length() > MAX_BYTES:
		file.close()
		return _error("SAVE_LIMIT")
	var size := file.get_length()
	var bytes := file.get_buffer(size)
	var read_error := file.get_error()
	file.close()
	if bytes.size() != size or read_error != OK:
		return _error("LOAD_READ_FAILED", read_error)
	var restored: Dictionary = host.call("restore", bytes)
	restored["recovered_backup"] = recovered
	return restored

# V001 reuses the slot policy and temporal/backup pattern without changing .core.
# validate is a bounded envelope/checksum check, never a Core restore.
static func commit_package(path: String, bytes: PackedByteArray, validate: Callable) -> Dictionary:
	var created := DirAccess.make_dir_recursive_absolute(path.get_base_dir())
	if created != OK:
		return _error("SAVE_DIRECTORY_FAILED", created)
	var temporary := path + ".tmp"
	var backup := path + ".bak"
	# Never rotate an invalid primary over a good backup, or discard a recovery copy.
	for previous in [path, backup] if not FileAccess.file_exists(path) else [path]:
		if FileAccess.file_exists(previous) and validate.call(previous).status != "ok":
			return _error("SAVE_EXISTING_INVALID")
	var file := FileAccess.open(temporary, FileAccess.WRITE)
	if file == null:
		return _error("SAVE_OPEN_FAILED", FileAccess.get_open_error())
	file.store_buffer(bytes)
	file.flush()
	var written := file.get_error()
	file.close()
	if written != OK or validate.call(temporary).status != "ok":
		DirAccess.remove_absolute(temporary)
		return _error("SAVE_WRITE_FAILED", written)
	if FileAccess.file_exists(path):
		if FileAccess.file_exists(backup):
			var removed := DirAccess.remove_absolute(backup)
			if removed != OK:
				return _error("SAVE_BACKUP_FAILED", removed)
		var moved := DirAccess.rename_absolute(path, backup)
		if moved != OK:
			return _error("SAVE_BACKUP_FAILED", moved)
	var committed := DirAccess.rename_absolute(temporary, path)
	if committed != OK:
		# Leave the last good backup intact, including when rollback cannot rename.
		var rollback := OK
		if not FileAccess.file_exists(path) and FileAccess.file_exists(backup):
			rollback = DirAccess.rename_absolute(backup, path)
		var failure := _error("SAVE_COMMIT_FAILED", committed)
		failure["rollback_error"] = rollback
		return failure
	return {"status": "ok", "error_code": "OK"}

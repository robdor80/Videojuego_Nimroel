extends RefCounted
## Trusted transport only. Native Host owns release verification and Core bootstrap.
const ROOT := "res://generated_content/treskal-v001"
const MAX_DOCUMENT := 65536
const MAX_BUNDLE := 131072

static func _collect(path: String, files: Dictionary, budget: Dictionary, depth: int = 0) -> bool:
	if depth > 3:
		return false
	var directory := DirAccess.open(path)
	if directory == null or directory.list_dir_begin() != OK:
		return false
	var name := directory.get_next()
	while not name.is_empty():
		budget.entries += 1
		if budget.entries > 24:
			return false
		var entry := path.path_join(name)
		if directory.current_is_dir():
			if files.size() > 9 or not _collect(entry, files, budget, depth + 1):
				return false
		else:
			if files.size() >= 9:
				return false
			files[entry.trim_prefix(ROOT + "/")] = true
		name = directory.get_next()
	directory.list_dir_end()
	return true

static func read_bundle() -> Dictionary:
	var files := {}
	if not _collect(ROOT, files, {"entries": 0}) or files.size() != 9:
		return {"status": "rejected", "error_code": "CONTENT_FILE_SET"}
	var total := 0
	for name in files:
		var file := FileAccess.open(ROOT.path_join(name), FileAccess.READ)
		if file == null:
			return {"status": "rejected", "error_code": "CONTENT_READ_FAILED"}
		var size := file.get_length()
		total += size
		if size <= 0 or size > MAX_DOCUMENT or total > MAX_BUNDLE:
			return {"status": "rejected", "error_code": "CONTENT_LIMIT"}
		var bytes := file.get_buffer(size)
		if bytes.size() != size or file.get_error() != OK:
			return {"status": "rejected", "error_code": "CONTENT_READ_FAILED"}
		files[name] = bytes
	return {"status": "ok", "files": files}

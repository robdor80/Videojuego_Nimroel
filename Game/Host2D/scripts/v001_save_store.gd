extends RefCounted
## Envelope del Host, independiente del codec Core. Solo uso privilegiado.
const Store = preload("res://scripts/core_save_store.gd")
const DIRECTORY := "user://v001_saves/v1"
const SLOT := "treskal"
const MAGIC := "NIMV001\n"
const MAX_HEADER := 2048
const MAX_CORE := 1048576
const MAX_PACKAGE := 12 + MAX_HEADER + MAX_CORE

static func path_for(slot: String) -> String:
	return Store.slot_path(slot, DIRECTORY, ".nimv001")

static func digest(bytes: PackedByteArray) -> String:
	var hash := HashingContext.new()
	if hash.start(HashingContext.HASH_SHA256) != OK or hash.update(bytes) != OK:
		return ""
	return hash.finish().hex_encode()

static func encode(bytes: PackedByteArray, installed: Dictionary) -> PackedByteArray:
	var metadata := installed.duplicate()
	metadata["core_length"] = str(bytes.size())
	metadata["core_sha256"] = digest(bytes)
	var header := JSON.stringify(metadata, "", true).to_utf8_buffer()
	var package := MAGIC.to_utf8_buffer()
	package.resize(12)
	package.encode_u32(8, header.size())
	package.append_array(header)
	package.append_array(bytes)
	return package

static func decode(package: PackedByteArray, installed: Dictionary) -> Dictionary:
	if package.size() < 12 or package.size() > MAX_PACKAGE:
		return Store._error("SAVE_LIMIT")
	if package.slice(0, 8) != MAGIC.to_utf8_buffer():
		return Store._error("SAVE_FORMAT")
	var length := package.decode_u32(8)
	if length < 2 or length > MAX_HEADER or 12 + length >= package.size():
		return Store._error("SAVE_HEADER")
	var header := package.slice(12, 12 + length)
	var parser := JSON.new()
	if parser.parse(header.get_string_from_utf8()) != OK or not parser.data is Dictionary:
		return Store._error("SAVE_HEADER")
	var metadata: Dictionary = parser.data
	# One canonical encoding rejects duplicate keys, invalid UTF-8 and unknown inventory.
	if JSON.stringify(metadata, "", true).to_utf8_buffer() != header or metadata.size() != installed.size() + 2:
		return Store._error("SAVE_HEADER")
	if metadata.get("save_schema") != installed.get("save_schema"):
		return Store._error("SAVE_SCHEMA_UNSUPPORTED")
	for key in installed:
		if not metadata.get(key) is String or metadata[key] != installed[key]:
			return Store._error("SAVE_CONTENT_INCOMPATIBLE")
	var size = metadata.get("core_length")
	var checksum = metadata.get("core_sha256")
	if not size is String or not size.is_valid_int() or str(int(size)) != size or int(size) < 1 or int(size) > MAX_CORE:
		return Store._error("SAVE_LENGTH")
	if not checksum is String or checksum.length() != 64:
		return Store._error("SAVE_CHECKSUM")
	var bytes := package.slice(12 + length)
	if bytes.size() != int(size):
		return Store._error("SAVE_LENGTH")
	if digest(bytes) != checksum:
		return Store._error("SAVE_CHECKSUM")
	return {"status": "ok", "error_code": "OK", "bytes": bytes}

static func read_package(path: String, installed: Dictionary) -> Dictionary:
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return Store._error("LOAD_OPEN_FAILED", FileAccess.get_open_error())
	var length := file.get_length()
	if length < 12 or length > MAX_PACKAGE:
		file.close()
		return Store._error("SAVE_LIMIT")
	var package := file.get_buffer(length)
	var failure := file.get_error()
	file.close()
	if package.size() != length or failure != OK:
		return Store._error("LOAD_READ_FAILED", failure)
	return decode(package, installed)

static func save(host: RefCounted, slot: String, installed: Dictionary) -> Dictionary:
	var path := path_for(slot)
	if path.is_empty():
		return Store._error("INVALID_SAVE_SLOT")
	var captured: Dictionary = host.call("capture")
	if captured.status != "ok":
		return captured
	if captured.bytes.size() < 1 or captured.bytes.size() > MAX_CORE:
		return Store._error("SAVE_LIMIT")
	var package := encode(captured.bytes, installed)
	if decode(package, installed).status != "ok":
		return Store._error("SAVE_HEADER")
	# A coherent checksum alone does not make an existing backup candidate GOOD.
	# Validate Core and observer in isolation before rotating the previous file.
	var bundle: Dictionary = preload("res://scripts/v001_pack.gd").read_bundle()
	if bundle.status != "ok":
		return bundle
	var verifier: RefCounted = ClassDB.instantiate("CoreRPGHost")
	var prepared: Dictionary = verifier.call("prepare_v001_restore", {"api_version": 1, "files": bundle.files})
	if prepared.status != "ok":
		return prepared
	if prepared.metadata != installed:
		return Store._error("SAVE_CONTENT_INCOMPATIBLE")
	var validate := func(p: String) -> Dictionary:
		var loaded := read_package(p, installed)
		if loaded.status != "ok":
			return loaded
		var checked: Dictionary = verifier.call("restore", loaded.bytes)
		if checked.status != "ok":
			return checked
		return verifier.call("open_session", {"api_version": 1, "observer": prepared.observer, "audience": "player"})
	return Store.commit_package(path, package, validate)

static func load_save(host: RefCounted, slot: String, installed: Dictionary, backup_only: bool = false) -> Dictionary:
	var path := path_for(slot)
	if path.is_empty():
		return Store._error("INVALID_SAVE_SLOT")
	var recovered := backup_only or (not FileAccess.file_exists(path) and FileAccess.file_exists(path + ".bak"))
	if recovered:
		path += ".bak"
	var loaded := read_package(path, installed)
	if loaded.status != "ok":
		return loaded
	# No Core call above this line. Never fall back from a corrupt primary silently.
	var restored: Dictionary = host.call("restore", loaded.bytes)
	restored["recovered_backup"] = recovered
	return restored

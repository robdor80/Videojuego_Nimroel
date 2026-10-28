extends RefCounted
## Host de confianza para la vertical estructural. No conserva un mundo paralelo.
## Toda identidad, mutación, conocimiento y serialización se delega al Core nativo.
const Port = preload("res://scripts/core_port.gd")
const Store = preload("res://scripts/core_save_store.gd")
const V001Store = preload("res://scripts/v001_save_store.gd")
var _metadata: Dictionary = {}
var _host: RefCounted
var _session: RefCounted
var _request_id: int = 0
var _v001: bool = false
var _observer: int = 0 # Identidad de la capacidad; no es un hecho ni ubicación.

func _init(use_v001: bool = false) -> void:
	_v001 = use_v001

func start() -> Dictionary:
	close()
	if not ClassDB.class_exists("CoreRPGHost"):
		return {"status": "unavailable", "error_code": "CORE_NOT_CONNECTED"}
	_host = ClassDB.instantiate("CoreRPGHost")
	if _v001:
		var bundle: Dictionary = preload("res://scripts/v001_pack.gd").read_bundle()
		if bundle.status != "ok":
			return bundle
		var loaded: Dictionary = _host.call("initialize_v001", {"api_version": 1, "files": bundle.files})
		if loaded.status != "ok":
			return loaded
		var opened: Dictionary = _host.call("open_session", {"api_version": 1, "observer": loaded.observer, "audience": "player"})
		if opened.status != "ok":
			return opened
		_session = opened.session
		_metadata = loaded.metadata
		_observer = loaded.observer
		return query()
	var initialized: Dictionary = _host.call("initialize", {"api_version": 1, "seed": "42", "entities": 4})
	if initialized.status != "ok":
		return initialized
	# Configuración neutral del Host: el cuarto ID permanece oculto al jugador.
	var placed: Dictionary = _host.call("step", {"api_version": 1, "actions": [{"operation": "place", "actor": 1, "entity": 1, "target": 2}]})
	if placed.status != "ok" or placed.results[0].outcome != "accepted":
		return {"status": "rejected", "error_code": "BOOTSTRAP_FAILED"}
	for subject in [1, 2, 3]:
		var learned: Dictionary = _host.call("admin", {"api_version": 1, "operation": "learn", "observer": 1, "subject": subject, "kind": 1})
		if learned.status != "ok":
			return learned
	return _bind()

func _bind() -> Dictionary:
	var opened: Dictionary = _host.call("open_session", {"api_version": 1, "observer": 1, "audience": "player", "allow_place": true, "allow_remove": true, "destinations": [2, 3]})
	if opened.status != "ok":
		return opened
	_session = opened.session
	_request_id = 0
	return query()

func query() -> Dictionary:
	if _host == null or _session == null:
		return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
	if _v001:
		return _session.call("context", {"api_version": 1})
	# Política de esta vertical: el jugador observa su propia contención actual.
	# Core conserva y valida el hecho; no se infiere nada desde la presentación.
	var learned: Dictionary = _host.call("admin", {"api_version": 1, "operation": "learn", "observer": 1, "subject": 1, "kind": 3})
	if learned.status != "ok":
		return learned
	return _session.call("context", {"api_version": 1})

func act(operation: String, target: int = 0) -> Dictionary:
	var issued := query()
	if issued.status != "ok":
		return issued
	_request_id += 1
	var proposal := {"api_version": 1, "operation": operation, "context_id": issued.context_id, "request_id": _request_id}
	if target != 0:
		proposal["target"] = target
	return Port.submit(proposal, _session)

func save_slot(slot: String = "native_vertical") -> Dictionary:
	if _v001:
		if _host == null or _session == null:
			return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
		return V001Store.save(_host, slot, _metadata)
	if _host == null:
		return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
	return Store.save(_host, slot)

func load_slot(slot: String = "native_vertical", backup_only: bool = false) -> Dictionary:
	if _v001:
		return _resume_v001(slot, backup_only)
	if _host == null:
		return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
	var loaded := Store.load_save(_host, slot)
	if loaded.status != "ok":
		return loaded
	# Restore invalida todas las capacidades previas. El Host debe autorizar de nuevo.
	_session = null
	return _bind()

func _resume_v001(slot: String, backup_only: bool) -> Dictionary:
	if V001Store.path_for(slot).is_empty():
		return {"status": "rejected", "error_code": "INVALID_SAVE_SLOT"}
	if not ClassDB.class_exists("CoreRPGHost"):
		return {"status": "unavailable", "error_code": "CORE_NOT_CONNECTED"}
	var bundle: Dictionary = preload("res://scripts/v001_pack.gd").read_bundle()
	if bundle.status != "ok":
		return bundle
	var candidate: RefCounted = ClassDB.instantiate("CoreRPGHost")
	var prepared: Dictionary = candidate.call("prepare_v001_restore", {"api_version": 1, "files": bundle.files})
	if prepared.status != "ok":
		return prepared
	var restored := V001Store.load_save(candidate, slot, prepared.metadata, backup_only)
	if restored.status != "ok":
		return restored
	var opened: Dictionary = candidate.call("open_session", {"api_version": 1, "observer": prepared.observer, "audience": "player"})
	if opened.status != "ok":
		return opened
	var context: Dictionary = opened.session.call("context", {"api_version": 1})
	if context.status != "ok":
		return context
	# Commit only after restore, observer/session binding AND first context succeed.
	close()
	_host = candidate
	_session = opened.session
	_observer = prepared.observer
	_metadata = prepared.metadata
	_request_id = 0
	context["recovered_backup"] = restored.recovered_backup
	return context

func close() -> Dictionary:
	_session = null
	_observer = 0
	_metadata = {}
	_request_id = 0
	if _host != null:
		var closed: Dictionary = _host.call("close")
		_host = null
		return closed
	return {"status": "ok", "error_code": "OK"}

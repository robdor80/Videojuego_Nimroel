extends RefCounted
## Host de confianza para la vertical estructural. No conserva un mundo paralelo.
## Toda identidad, mutación, conocimiento y serialización se delega al Core nativo.
const Port = preload("res://scripts/core_port.gd")
const Store = preload("res://scripts/core_save_store.gd")
var _host: RefCounted
var _session: RefCounted
var _request_id: int = 0

func start() -> Dictionary:
	close()
	if not ClassDB.class_exists("CoreRPGHost"):
		return {"status": "unavailable", "error_code": "CORE_NOT_CONNECTED"}
	_host = ClassDB.instantiate("CoreRPGHost")
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
	if _host == null:
		return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
	return Store.save(_host, slot)

func load_slot(slot: String = "native_vertical") -> Dictionary:
	if _host == null:
		return {"status": "unavailable", "error_code": "WORLD_NOT_STARTED"}
	var loaded := Store.load_save(_host, slot)
	if loaded.status != "ok":
		return loaded
	# Restore invalida todas las capacidades previas. El Host debe autorizar de nuevo.
	_session = null
	return _bind()

func close() -> Dictionary:
	_session = null
	if _host != null:
		var closed: Dictionary = _host.call("close")
		_host = null
		return closed
	return {"status": "ok", "error_code": "OK"}

extends RefCounted
## Transporte local. Solo el Host de confianza puede vincular una sesión nativa.
## La interpretación de texto y los servicios IA siguen sin estar integrados.

const STATUS_UNAVAILABLE := "unavailable"
const API_VERSION := 1
static var _session: RefCounted

static func capabilities() -> Dictionary:
	var connected: bool = _session != null and _session.call("availability").get("status") == "ok"
	return {"core_available": connected, "native_available": ClassDB.class_exists("CoreRPGHost"), "api_version": API_VERSION}

static func bind_session(session: RefCounted) -> bool:
	if session != null and session.get_class() != "CoreRPGSession":
		return false
	_session = session
	return true

static func submit(proposal: Dictionary) -> Dictionary:
	if capabilities().core_available:
		return _session.call("submit", proposal)
	return {
		"status": STATUS_UNAVAILABLE,
		"events": [],
		"error_code": "CORE_NOT_CONNECTED",
		"world_mutated": false
	}

extends RefCounted
## Transporte local sin estado global. Cada llamada lleva su capacidad de sesión.
## Los flujos antiguos sin sesión continúan bloqueados de forma explícita.
const STATUS_UNAVAILABLE := "unavailable"
const API_VERSION := 1

static func capabilities(session: RefCounted = null) -> Dictionary:
	var connected: bool = session != null and session.get_class() == "CoreRPGSession" and session.call("availability").get("status") == "ok"
	return {"core_available": connected, "native_available": ClassDB.class_exists("CoreRPGHost"), "api_version": API_VERSION}

static func submit(proposal: Dictionary, session: RefCounted = null) -> Dictionary:
	if capabilities(session).core_available:
		return session.call("submit", proposal)
	return {"status": STATUS_UNAVAILABLE, "events": [], "error_code": "CORE_NOT_CONNECTED", "world_mutated": false}

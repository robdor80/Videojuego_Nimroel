extends RefCounted
## Puerto del Host hacia CoreRPG. Sin GDExtension todavía.
## Toda acción real debe pasar por el Core, nunca por este stub.

const STATUS_UNAVAILABLE := "unavailable"
const API_VERSION := 1

static func capabilities() -> Dictionary:
	return {"core_available": false, "api_version": API_VERSION}

static func submit(_proposal: Dictionary) -> Dictionary:
	return {
		"status": STATUS_UNAVAILABLE,
		"world_revision": -1,
		"events": [],
		"error_code": "CORE_NOT_CONNECTED",
		"world_mutated": false
	}

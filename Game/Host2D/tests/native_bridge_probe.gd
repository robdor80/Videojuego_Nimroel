extends RefCounted
## Integration tests execute CoreRPG through the registered native classes.
## Host-only diagnostics stay here; none are sent to dialogue/providers.
const Store = preload("res://scripts/core_save_store.gd")
const Port = preload("res://scripts/core_port.gd")
static var _errors: Array[String] = []
static var _checks: int = 0

static func check(condition: bool, name: String) -> void:
	_checks += 1
	if not condition:
		_errors.append(name)

static func request(operation: String, fields: Dictionary = {}) -> Dictionary:
	var d := {"api_version": 1, "operation": operation}
	d.merge(fields)
	return d

static func learn(host: RefCounted, observer: int, subject: int, kind: int = 1, extra: Dictionary = {}) -> Dictionary:
	var fields := {"observer": observer, "subject": subject, "kind": kind}
	fields.merge(extra)
	return host.call("admin", request("learn", fields))

static func step(host: RefCounted, actions: Array) -> Dictionary:
	return host.call("step", {"api_version": 1, "actions": actions})

static func context(session: RefCounted, filters: Dictionary = {}) -> Dictionary:
	var d := {"api_version": 1}
	d.merge(filters)
	return session.call("context", d)

static func saved(host: RefCounted) -> PackedByteArray:
	var capture: Dictionary = host.call("capture")
	check(capture.get("status") == "ok", "capture succeeds")
	return capture.get("bytes", PackedByteArray())

static func verify() -> Dictionary:
	_errors = []
	_checks = 0
	if not ClassDB.class_exists("CoreRPGHost") or not ClassDB.class_exists("CoreRPGSession"):
		return {"ok": false, "checks": 0, "errors": ["native classes unavailable"]}
	var host: RefCounted = ClassDB.instantiate("CoreRPGHost")
	check(host.call("capture").error_code == "NOT_INITIALIZED", "uninitialized capture")
	check(host.call("initialize", {"api_version": 9, "seed": "1", "entities": 4}).error_code == "UNSUPPORTED_VERSION", "version mismatch")
	check(host.call("initialize", {"api_version": 1, "seed": "18446744073709551615", "entities": 4}).entities == [1, 2, 3, 4], "Core creates entities and full u64 seed")
	check(host.call("diagnostics").revision == "4", "initial revision")
	var initial := saved(host)
	for bad in [
		{"api_version": 1, "seed": "01", "entities": 4},
		{"api_version": 1, "seed": "18446744073709551616", "entities": 4},
		{"api_version": 1, "seed": "1", "entities": 4.0},
		{"api_version": 1, "seed": "1", "entities": true},
		{"api_version": 1, "seed": "1", "entities": 4, "secret": "x"}]:
		check(host.call("initialize", bad).status == "rejected", "closed initialization schema")
		check(saved(host) == initial, "invalid initialization atomic")
	check(step(host, [{"operation": "place", "actor": 1, "entity": 1, "target": 2}]).results[0].outcome == "accepted", "real placement")
	check(host.call("diagnostics").revision == "5", "placement revision increments")
	check(step(host, [{"operation": "place", "actor": 1, "entity": 1, "target": 2}]).results[0].outcome == "no_change", "Core no-op")
	var before_reject := saved(host)
	for action in [
		{"operation": "place", "actor": 2, "entity": 2, "target": 1},
		{"operation": "place", "actor": 1, "entity": 1, "target": 1},
		{"operation": "place", "actor": 1, "entity": 1, "target": 99},
		{"operation": "roll", "actor": 1, "stream": 7, "minimum": 9, "maximum": 2},
		{"operation": "remove_containment", "actor": 1, "entity": 1, "expected_revision": "0"},
		{"operation": "remove_containment", "actor": 1, "entity": 1, "preconditions": [{"kind": 2, "subject": 1}]}]:
		check(step(host, [action]).results[0].outcome == "rejected", "Core rejects invalid action")
		check(saved(host) == before_reject, "rejection preserves world and RNG")
	check(step(host, [{"operation": "remove_containment", "actor": 1, "entity": 1}, {"operation": "unsupported", "actor": 1}]).error_code == "OPERATION_UNAVAILABLE", "whole batch validates before execution")
	check(saved(host) == before_reject, "bad batch has no prefix mutation")
	# Observer 1 knows only 1,2,3. Entity 4 remains secret. NPC 3 knows only itself.
	for subject in [1, 2, 3]:
		check(learn(host, 1, subject).status == "ok", "remember existence")
	check(learn(host, 1, 1, 3).status == "ok", "remember containment")
	check(learn(host, 3, 3).status == "ok", "separate NPC knowledge")
	var opened: Dictionary = host.call("open_session", {"api_version": 1, "observer": 1, "audience": "player", "allow_place": true, "allow_remove": true, "destinations": [2, 3]})
	check(opened.status == "ok", "authenticated local player session")
	var player: RefCounted = opened.session
	var npc: RefCounted = host.call("open_session", {"api_version": 1, "observer": 3, "audience": "npc"}).session
	var ai: RefCounted = host.call("open_session", {"api_version": 1, "observer": 3, "audience": "ai"}).session
	var bare: RefCounted = ClassDB.instantiate("CoreRPGSession")
	check(context(bare).error_code == "SESSION_EXPIRED", "unbound ClassDB session has no authority")
	check(context(npc).facts.size() == 1 and context(ai).facts.size() == 1, "NPC and AI use bound authorized view")
	check(context(player, {"subject": 4}).facts == context(player, {"subject": 99}).facts, "hidden and missing are indistinguishable")
	check(context(player, {"max_selected": 0}).context_status == "selection_limit", "truncation explicit")
	check(context(player, {"max_content_bytes": 0}).context_status == "content_limit", "content budget explicit")
	check(context(player, {"observer": 4}).error_code == "UNKNOWN_FIELD", "cannot change observer")
	check(context(player, {"grants": []}).error_code == "UNKNOWN_FIELD", "cannot inject visibility grants")
	var issued := context(player)
	check(not issued.has("revision") and not issued.has("entities") and not issued.has("streams"), "no privileged context metadata")
	check(Port.bind_session(player) and Port.capabilities().core_available, "Host2D real port bound")
	var proposal := request("place", {"context_id": issued.context_id, "request_id": 1, "target": 3})
	var forged := proposal.duplicate()
	forged["actor"] = 4
	check(Port.submit(forged).error_code == "UNKNOWN_FIELD", "actor spoofing blocked")
	var denied := proposal.duplicate()
	denied["target"] = 4
	var prior_denied := saved(host)
	check(Port.submit(denied).error_code == "OPERATION_DENIED", "secret/unpermitted target denied")
	check(saved(host) == prior_denied, "denial has no mutation")
	var accepted := Port.submit(proposal)
	check(accepted.outcome == "accepted", "session calls Core action via Host2D port")
	check(not accepted.has("revision") and not accepted.has("consequence") and not accepted.has("rejection"), "safe receipt strips privileged result")
	check(Port.submit(proposal).error_code == "REQUEST_REPLAYED", "request deduplication")
	var remembered := context(player, {"subject": 1, "kind": 3})
	check(remembered.facts[0].reference == 2 and remembered.facts[0].provenance == "remembered", "actions do not silently refresh knowledge")
	check(learn(host, 1, 1, 3).status == "ok", "explicit knowledge refresh")
	check(context(player, {"subject": 1, "kind": 3}).facts[0].reference == 3, "refreshed consequence returns through Core view")
	var stale := context(player)
	check(host.call("admin", request("create_entity")).entity == 5, "trusted entity creation")
	var stale_result: Dictionary = player.call("submit", request("remove_containment", {"context_id": stale.context_id, "request_id": 2}))
	check(stale_result.error_code == "ACTION_REJECTED", "private revision rejects stale proposal")
	var npc_context := context(npc)
	check(npc.call("submit", request("remove_containment", {"context_id": npc_context.context_id, "request_id": 1})).error_code == "OPERATION_DENIED", "NPC cannot directly mutate")
	# Relations and populations are actual Core operations; not game systems.
	var related := step(host, [{"operation": "add_relation", "actor": 1, "entity": 1, "target": 3, "relation_kind": 7}])
	check(related.results[0].outcome == "accepted", "Core relation")
	check(learn(host, 1, 1, 4, {"target": 3, "relation_kind": 7}).status == "ok", "authorized exact relation")
	check(host.call("admin", request("declare_population", {"entity": 2, "total": 12})).status == "ok", "Core population reserve")
	check(host.call("admin", request("materialize", {"entity": 2, "count": 2})).count == 2, "Core materializes identities")
	check(learn(host, 1, 2, 5).status == "ok", "population facts")
	check(context(player, {"subject": 2, "kind": 5}).facts[0].latent == "10", "Core latent count")
	# Persistent world + remembered knowledge + RNG continuation, not replay.
	var roll := {"operation": "roll", "actor": 1, "stream": 7, "minimum": 1, "maximum": 1000000}
	var revision_before_roll: String = host.call("diagnostics").revision
	check(step(host, [roll]).results[0].consumed_random, "real deterministic RNG draw")
	check(host.call("diagnostics").revision == revision_before_roll, "RNG draw does not invent world revision")
	var checkpoint := saved(host)
	check(Store.save(host, "nim06_test").status == "ok", "Host writes physical save")
	check(Store.save(host, "nim06_test").status == "ok", "Host replaces physical save with backup")
	check(Store.save(host, "../escape").error_code == "INVALID_SAVE_SLOT", "Host rejects path traversal")
	check(Store.load_save(host, "missing_slot").error_code == "LOAD_OPEN_FAILED", "Host reports missing file")
	var from_disk := FileAccess.get_file_as_bytes("user://core_saves/nim06_test.core")
	check(from_disk == checkpoint, "Host filesystem roundtrip")
	var continued := step(host, [roll, roll, roll])
	var after_continued := saved(host)
	var restored: Dictionary = Store.load_save(host, "nim06_test")
	check(restored.status == "ok", "Core restores v3")
	check(saved(host) == checkpoint, "canonical bytes identical after restore")
	check(player.call("availability").error_code == "SESSION_EXPIRED", "restore invalidates old session despite same IDs")
	check(step(host, [roll, roll, roll]) == continued, "deterministic result sequence after restore")
	check(saved(host) == after_continued, "deterministic world and streams continuation")
	var corrupt := checkpoint.duplicate()
	corrupt[corrupt.size() - 1] = corrupt[corrupt.size() - 1] ^ 1
	var valid_after_restore: RefCounted = host.call("open_session", {"api_version": 1, "observer": 1, "audience": "player"}).session
	var before_load_error := saved(host)
	check(host.call("restore", corrupt).error_code == "LOAD_REJECTED", "CRC rejects corrupt save")
	check(host.call("restore", checkpoint.slice(0, 20)).error_code == "LOAD_REJECTED", "truncated save rejected")
	check(saved(host) == before_load_error, "failed restore preserves active world and RNG")
	check(valid_after_restore.call("availability").status == "ok", "failed restore preserves active session")
	var other: RefCounted = ClassDB.instantiate("CoreRPGHost")
	check(other.call("initialize", {"api_version": 1, "seed": "3", "entities": 1}).status == "ok", "second independent instance")
	check(host.call("diagnostics").entities == 7 and other.call("diagnostics").entities == 1, "instances isolated")
	var orphan: RefCounted = other.call("open_session", {"api_version": 1, "observer": 1, "audience": "player"}).session
	other = null
	check(orphan.call("availability").error_code == "SESSION_EXPIRED", "host destruction releases world safely")
	var reopened: RefCounted = host.call("open_session", {"api_version": 1, "observer": 1, "audience": "player"}).session
	check(reopened.call("close").status == "ok" and context(reopened).error_code == "SESSION_EXPIRED", "explicit session close")
	check(Port.bind_session(null), "detach port")
	check(host.call("close").status == "ok" and host.call("capture").error_code == "NOT_INITIALIZED", "Host shutdown")
	DirAccess.remove_absolute("user://core_saves/nim06_test.core")
	DirAccess.remove_absolute("user://core_saves/nim06_test.core.bak")
	return {"ok": _errors.is_empty(), "checks": _checks, "errors": _errors, "core_commit": "4f282863737bcd8f5add401202a9e1064c133672", "scope": "native functional vertical; physical device acceptance separate"}

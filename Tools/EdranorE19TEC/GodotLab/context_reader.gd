extends RefCounted
## Consumer E19-TEC para Godot 4.7.2; NO crea entidades ni tiene acceso a Core.
## B2 causal, sin georreferenciación, caminos ni NPC. Fail-closed.

const MAX_CATALOG_BYTES: int = 262144
const EXPECTED_METHOD := "VALRIK_CAUSAL_METHOD_ONLY_NOT_GEOMETRY"
const EXPECTED_STATUS := "NONMETRIC_B2_CATALOG_NO_RUNTIME"

static func validate_catalog(data: Variant) -> Dictionary:
	if not data is Dictionary:
		return {"status": "rejected", "error": "NOT_DICTIONARY"}
	if data.get("schemaVersion") != 1 or data.get("documentId") != "edranor_e19_tec_causal_catalog":
		return {"status": "rejected", "error": "SCHEMA"}
	if data.get("method") != EXPECTED_METHOD or data.get("status") != EXPECTED_STATUS:
		return {"status": "rejected", "error": "AUTHORITY"}
	if data.get("seed") != null or data.get("coordinates") != null or data.get("worldState") != null:
		return {"status": "rejected", "error": "FAKE_WORLD"}
	if data.get("physicalRouteCount") != 0 or data.get("actualSettlementCount") != 0:
		return {"status": "rejected", "error": "FAKE_MATERIALIZATION"}
	if data.get("unknownRegionIds") != ["MF-08"]:
		return {"status": "rejected", "error": "UNKNOWN_NORTH"}
	if not data.get("contexts") is Array or data["contexts"].size() != 7:
		return {"status": "rejected", "error": "REGIONS"}
	var seen := {}
	var safe_regions: Array = []
	for i in range(7):
		var item: Variant = data["contexts"][i]
		if not item is Dictionary:
			return {"status": "rejected", "error": "REGION_TYPE"}
		var id: String = "MF-%02d" % (i + 1)
		if item.get("contextId") != id or seen.has(id) or item.get("status") != "B2_CAUSAL_STUDY_NOT_PLACED":
			return {"status": "rejected", "error": "REGION_ID"}
		seen[id] = true
		if item.get("geometry") != null or item.get("area") != null:
			return {"status": "rejected", "error": "FAKE_GEOMETRY"}
		if item.get("actualPlaces") != [] or item.get("physicalGraphEdges") != []:
			return {"status": "rejected", "error": "FAKE_LOCATIONS"}
		if item.get("eligibleForWorldState") != false or item.get("approvedLandUse") != false:
			return {"status": "rejected", "error": "FAKE_APPROVAL"}
		if not item.get("routeQuestionIds") is Array or not item.get("occupationStudyIds") is Array:
			return {"status": "rejected", "error": "UNTRUSTED_STUDIES"}
		if not item.get("potentialRuleIds") is Dictionary:
			return {"status": "rejected", "error": "MISSING_RULES"}
		for kind in ["soils", "microclimate", "cover", "resources"]:
			if not item["potentialRuleIds"].get(kind) is Array:
				return {"status": "rejected", "error": "MISSING_RULES"}
		safe_regions.append({
			"id": id, "name": item.get("name", ""),
			"basinStudyId": item.get("basinStudyId", ""),
			"status": "UNLOCATED_CONCEPT",
		})
	if not data.get("anchors") is Array or data["anchors"].size() != 5:
		return {"status": "rejected", "error": "ANCHOR_SET"}
	var found_rodas := false
	for anchor in data["anchors"]:
		if not anchor is Dictionary or anchor.get("manual") != true or anchor.get("location") != null:
			return {"status": "rejected", "error": "FAKE_ANCHOR_LOCATION"}
		if anchor.get("id") == "rodas":
			found_rodas = anchor.get("jurisdiction") == "crown_aethros" and anchor.get("kind") == "ALDEA"
	if not found_rodas:
		return {"status": "rejected", "error": "RODAS_CROWN"}
	return {"status": "ok", "kind": "B2_CONCEPTUAL_READ_ONLY",
			"regions": safe_regions, "materialized": false}

static func load_catalog(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {"status": "unavailable", "error": "CATALOG_MISSING"}
	var file: FileAccess = FileAccess.open(path, FileAccess.READ)
	if file == null:
		return {"status": "unavailable", "error": "CATALOG_READ"}
	var size: int = file.get_length()
	if size < 2 or size > MAX_CATALOG_BYTES:
		file.close()
		return {"status": "rejected", "error": "CATALOG_SIZE"}
	var data: PackedByteArray = file.get_buffer(size)
	var err: int = file.get_error()
	file.close()
	if data.size() != size or err != OK:
		return {"status": "unavailable", "error": "CATALOG_IO"}
	var parser := JSON.new()
	if parser.parse(data.get_string_from_utf8()) != OK:
		return {"status": "rejected", "error": "CATALOG_JSON"}
	return validate_catalog(parser.data)

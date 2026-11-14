extends RefCounted
## Importa y dibuja SOLO fixture geométrico de LAB. Nunca Core/partida/canon.
const MAX_INPUT_BYTES: int = 262144
const ALLOWED_TYPES := {
	"boundary_divide": "LineString", "river": "LineString",
	"route_node": "Point", "road": "LineString",
	"settlement": "Point", "forest": "Polygon", "parcel": "Polygon",
}
const LAB_STATUS := "LAB_GEOMETRY_NON_CANON_NOT_RUNTIME"

static func _points(raw: Variant) -> PackedVector2Array:
	if not raw is Array or raw.size() < 2:
		return PackedVector2Array()
	var coords := PackedVector2Array()
	for item in raw:
		if not item is Array or item.size() != 2:
			return PackedVector2Array()
		if not (item[0] is float or item[0] is int) or not (item[1] is float or item[1] is int):
			return PackedVector2Array()
		var pos := Vector2(float(item[0]), float(item[1]))
		if not is_finite(pos.x) or not is_finite(pos.y):
			return PackedVector2Array()
		coords.append(pos)
	return coords

static func inspect(data: Variant) -> Dictionary:
	if not data is Dictionary or data.get("schemaVersion") != 1:
		return {"status": "rejected", "error": "FORMAT"}
	if data.get("profile") != "NIMROEL_GODOT_2D_SPATIAL" or data.get("maturity") != LAB_STATUS:
		return {"status": "rejected", "error": "LAB_ONLY"}
	if data.get("sectorId") != "TEST_SECTOR_ONLY" or data.get("contextIds") != ["MF-01"]:
		return {"status": "rejected", "error": "NOT_SYNTHETIC_TEST"}
	var feats: Variant = data.get("features")
	if not feats is Array or feats.size() != 8:
		return {"status": "rejected", "error": "FEATURE_SET"}
	var seen := {}
	for feature in feats:
		if not feature is Dictionary or not feature.get("id") is String:
			return {"status": "rejected", "error": "FEATURE"}
		var id: String = feature["id"]
		if seen.has(id):
			return {"status": "rejected", "error": "DUPLICATE"}
		seen[id] = true
		if feature.get("status") != "APPROVED_B3" or feature.get("sourceId") != "SURVEY:features":
			return {"status": "rejected", "error": "LAB_EVIDENCE"}
		var shape: Variant = feature.get("geometry")
		if not shape is Dictionary:
			return {"status": "rejected", "error": "MISSING_GEOMETRY"}
		var typ: String = str(shape.get("type", ""))
		var kind: String = str(feature.get("kind", ""))
		if kind == "waterbody":
			if typ not in ["Point", "Polygon"]:
				return {"status": "rejected", "error": "SHAPE_TYPE"}
		elif ALLOWED_TYPES.get(kind) != typ:
			return {"status": "rejected", "error": "SHAPE_TYPE"}
		if typ == "Point":
			var pt: Variant = shape.get("coordinates")
			if not pt is Array or pt.size() != 2:
				return {"status": "rejected", "error": "POINT"}
			if not (pt[0] is int or pt[0] is float) or not (pt[1] is int or pt[1] is float):
				return {"status": "rejected", "error": "POINT"}
		else:
			var coords := _points(shape.get("coordinates"))
			if coords.size() < (4 if typ == "Polygon" else 2):
				return {"status": "rejected", "error": "POLYGON_OR_LINE"}
			if typ == "Polygon" and coords[0] != coords[coords.size() - 1]:
				return {"status": "rejected", "error": "UNCLOSED_POLYGON"}
	return {"status": "ok", "mode": "LAB_GEOMETRY_PREVIEW_ONLY", "featureCount": feats.size(),
			"physicalEntitiesCommitted": 0}

static func load_lab(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {"status": "unavailable", "error": "NOT_FOUND"}
	var file: FileAccess = FileAccess.open(path, FileAccess.READ)
	if file == null:
		return {"status": "unavailable", "error": "OPEN_FAILED"}
	var size: int = file.get_length()
	if size < 2 or size > MAX_INPUT_BYTES:
		file.close()
		return {"status": "rejected", "error": "SIZE"}
	var bytes: PackedByteArray = file.get_buffer(size)
	var err: int = file.get_error()
	file.close()
	if bytes.size() != size or err != OK:
		return {"status": "unavailable", "error": "READ_FAILED"}
	var parser := JSON.new()
	if parser.parse(bytes.get_string_from_utf8()) != OK:
		return {"status": "rejected", "error": "PARSE"}
	var check := inspect(parser.data)
	if check.get("status") != "ok":
		return check
	check["data"] = parser.data
	return check

static func instantiate_lab(data: Dictionary) -> Node2D:
	var valid := inspect(data)
	if valid.get("status") != "ok":
		return null
	var root := Node2D.new()
	root.name = "Edranor_Synthetic_Lab_Not_World"
	for entry in data["features"]:
		var geom: Dictionary = entry["geometry"]
		var kind: String = entry["kind"]
		var shape: String = geom["type"]
		if shape == "Point":
			var node := Marker2D.new()
			node.position = Vector2(float(geom["coordinates"][0]), float(geom["coordinates"][1]))
			node.name = entry["id"]
			root.add_child(node)
		elif shape == "LineString":
			var line := Line2D.new()
			line.points = _points(geom["coordinates"])
			line.name = entry["id"]
			root.add_child(line)
		else:
			var polygon := Polygon2D.new()
			var coords := _points(geom["coordinates"])
			coords.remove_at(coords.size() - 1)
			polygon.polygon = coords
			polygon.name = entry["id"]
			root.add_child(polygon)
	return root

extends SceneTree
const Reader = preload("res://context_reader.gd")

func _initialize() -> void:
	_run.call_deferred()

func _run() -> void:
	var response: Dictionary = Reader.load_catalog("res://catalog_generated.json")
	if response.get("status") != "ok":
		push_error("E19-TEC: no se ha cargado el catálogo: " + str(response))
		quit(1)
		return
	if response["regions"].size() != 7 or response["materialized"] != false:
		push_error("E19-TEC: mapa materializado indebidamente")
		quit(1)
		return
	var file: FileAccess = FileAccess.open("res://catalog_generated.json", FileAccess.READ)
	var parser := JSON.new()
	if file == null or parser.parse(file.get_as_text()) != OK:
		push_error("E19-TEC: lectura secundaria")
		quit(1)
		return
	var original: Dictionary = parser.data
	var invalid: Dictionary = original.duplicate(true)
	invalid["physicalRouteCount"] = 1
	if Reader.validate_catalog(invalid)["status"] != "rejected":
		push_error("E19-TEC: camino inventado aceptado")
		quit(1)
		return
	invalid = original.duplicate(true)
	invalid["contexts"][0]["eligibleForWorldState"] = true
	if Reader.validate_catalog(invalid)["status"] != "rejected":
		push_error("E19-TEC: WorldState inventado aceptado")
		quit(1)
		return
	invalid = original.duplicate(true)
	invalid["unknownRegionIds"] = []
	if Reader.validate_catalog(invalid)["status"] != "rejected":
		push_error("E19-TEC: MF-08 falso aceptado")
		quit(1)
		return
	invalid = original.duplicate(true)
	invalid["anchors"][3]["jurisdiction"] = "casa_edranor"
	if Reader.validate_catalog(invalid)["status"] != "rejected":
		push_error("E19-TEC: Rodas incorrecta aceptada")
		quit(1)
		return
	print("E19-TEC GODOT 4.7.2 PASS: catalogo causal B2, 7 MF; caminos=0, entidades=0")
	quit(0)

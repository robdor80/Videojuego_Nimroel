extends SceneTree
const Reader = preload("res://sector_reader.gd")
func _initialize() -> void:
	_run.call_deferred()

func _run() -> void:
	var result: Dictionary = Reader.load_lab("res://sector_lab_generated.json")
	if result.get("status") != "ok" or result.get("physicalEntitiesCommitted") != 0:
		push_error("E19-TEC: sector TEST_ONLY debe leerse sin WorldState: " + str(result))
		quit(1)
		return
	var nodes: Node2D = Reader.instantiate_lab(result["data"])
	if nodes == null or nodes.get_child_count() != 8:
		push_error("E19-TEC: no se instanciaron ocho formas 2D")
		quit(1)
		return
	var seen := {"Line2D": 0, "Polygon2D": 0, "Marker2D": 0}
	for child in nodes.get_children():
		seen[child.get_class()] += 1
	if seen["Line2D"] != 3 or seen["Polygon2D"] != 1 or seen["Marker2D"] != 4:
		push_error("E19-TEC: tipos 2D no coinciden: " + str(seen))
		nodes.free()
		quit(1)
		return
	var forged: Dictionary = result["data"].duplicate(true)
	forged["maturity"] = "SECTOR_B3_GEOMETRY_ONLY_NOT_RUNTIME_B4"
	if Reader.inspect(forged).get("status") != "rejected":
		push_error("E19-TEC: colada de datos de LAB como B3")
		nodes.free()
		quit(1)
		return
	forged = result["data"].duplicate(true)
	forged["features"][0]["sourceId"] = "CANON_NO_VERIFICADO"
	if Reader.inspect(forged).get("status") != "rejected":
		push_error("E19-TEC: fuente adulterada aceptada")
		nodes.free()
		quit(1)
		return
	print("E19-TEC GODOT PASS: 8 formas 2D LAB, 0 entidades Core; falsos B3 bloqueados")
	nodes.free()
	quit(0)

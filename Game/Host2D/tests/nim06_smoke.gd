extends SceneTree
func _initialize() -> void:
	var report: Dictionary = preload("res://tests/native_bridge_probe.gd").verify()
	print("NIM06_FUNCTIONAL_REPORT " + JSON.stringify(report))
	quit(0 if report.ok else 1)

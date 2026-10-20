extends Control

func _ready() -> void:
	var report: Dictionary = preload("res://tests/native_bridge_probe.gd").verify()
	$Report.text = ("NIM06 FUNCTIONAL PASS" if report.ok else "NIM06 FUNCTIONAL FAIL") + "\n" + JSON.stringify(report, "  ")
	print("NIM06_FUNCTIONAL_REPORT " + JSON.stringify(report))
	# Archivo de diagnóstico del Host; contiene resultados de pruebas, no snapshots.
	var file := FileAccess.open("user://nim06-result.json", FileAccess.WRITE)
	if file != null:
		file.store_string(JSON.stringify(report, "  "))
		file.close()
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		get_tree().quit(0 if report.ok else 1)

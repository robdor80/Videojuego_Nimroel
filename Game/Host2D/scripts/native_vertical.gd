extends Control
const Controller = preload("res://scripts/native_world_controller.gd")
var _controller := Controller.new()

func _ready() -> void:
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		_execute_tests()
		return
	$Report.text = "Vertical estructural real de CoreRPG. Crea un mundo técnico para consultar hechos autorizados, solicitar contención y guardar/restaurar. No es una partida RPG ni un diálogo IA."
	var row := HFlowContainer.new()
	row.position = Vector2(30, 70)
	row.size = Vector2(1200, 100)
	add_child(row)
	for pair in [
		["Crear mundo técnico", func(): _show(_controller.start())],
		["Consultar", func(): _show(_controller.query())],
		["Contener en 2", func(): _show(_controller.act("place", 2))],
		["Contener en 3", func(): _show(_controller.act("place", 3))],
		["Retirar contención", func(): _show(_controller.act("remove_containment"))],
		["Guardar", func(): _show(_controller.save_slot())],
		["Restaurar", func(): _show(_controller.load_slot())],
		["Cerrar mundo", func(): _show(_controller.close())],
		["Ejecutar pruebas", _execute_tests],
		["Volver", func(): get_tree().change_scene_to_file("res://main.tscn")]]:
		var button := Button.new()
		button.text = pair[0]
		button.pressed.connect(pair[1])
		row.add_child(button)

func _show(value: Dictionary) -> void:
	$Report.text = JSON.stringify(value, "  ")

func _execute_tests() -> void:
	_controller.close()
	var report: Dictionary = preload("res://tests/native_bridge_probe.gd").verify()
	$Report.text = ("NIM06 FUNCTIONAL PASS" if report.ok else "NIM06 FUNCTIONAL FAIL") + "\n" + JSON.stringify(report, "  ")
	print("NIM06_FUNCTIONAL_REPORT " + JSON.stringify(report))
	var file := FileAccess.open("user://nim06-result.json", FileAccess.WRITE)
	if file != null:
		file.store_string(JSON.stringify(report, "  "))
		file.close()
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		get_tree().quit(0 if report.ok else 1)

func _exit_tree() -> void:
	_controller.close()

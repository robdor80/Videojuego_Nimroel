extends Control
const Controller = preload("res://scripts/native_world_controller.gd")
var _controller := Controller.new()
var _previous_scale_size: Vector2i
var _launcher: CanvasLayer
@onready var _report: Label = $Margin/Layout/ReportScroll/Report
@onready var _actions: HFlowContainer = $Margin/Layout/ActionsScroll/Actions
@onready var _actions_scroll: ScrollContainer = $Margin/Layout/ActionsScroll

func _ready() -> void:
	_previous_scale_size = get_window().content_scale_size
	_launcher = get_node_or_null("/root/NativeDiagnostics/Launcher")
	if _launcher != null:
		_launcher.hide()
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		_execute_tests()
		return
	_report.text = "Vertical estructural real de CoreRPG. Crea un mundo técnico para consultar hechos autorizados, solicitar contención y guardar/restaurar. No es una partida RPG ni un diálogo IA."
	for pair in [
		["Crear mundo técnico", func(): _show(_controller.start())],
		["Consultar", func(): _show(_controller.query())],
		["Contener en 2", func(): _show(_controller.act("place", 2))],
		["Contener en 3", func(): _show(_controller.act("place", 3))],
		["Retirar contención", func(): _show(_controller.act("remove_containment"))],
		["Guardar", func(): _show(_controller.save_slot())],
		["Restaurar", func(): _show(_controller.load_slot())],
		["Cerrar mundo", func(): _show(_controller.close())],
		["Ejecutar pruebas", _execute_tests]]:
		var button := Button.new()
		button.text = pair[0]
		button.custom_minimum_size = Vector2(200, 48)
		button.pressed.connect(pair[1])
		_actions.add_child(button)
	$Margin/Layout/Back.pressed.connect(func(): get_tree().change_scene_to_file("res://main.tscn"))
	_actions_scroll.get_v_scroll_bar().custom_minimum_size.x = 24
	$Margin/Layout/ReportScroll.get_v_scroll_bar().custom_minimum_size.x = 24
	get_window().size_changed.connect(_update_scale)
	resized.connect(_fit_actions)
	_actions.minimum_size_changed.connect(_fit_actions)
	_update_scale()
	_fit_actions.call_deferred()

static func logical_size(pixels: Vector2i, dpi: int, mobile: bool) -> Vector2i:
	# Densidad independiente del ancho: dividir la pantalla no encoge el texto.
	var density := clampf(float(dpi) / 160.0, 1.0, 3.0) if mobile else 1.0
	return Vector2i(maxi(1, roundi(pixels.x / density)), maxi(1, roundi(pixels.y / density)))

func _update_scale() -> void:
	get_window().content_scale_size = logical_size(get_window().size, DisplayServer.screen_get_dpi(), OS.has_feature("android"))
	_fit_actions.call_deferred()

func _fit_actions() -> void:
	# Los controles tienen su propio scroll en ventanas bajas; resultado y Volver
	# conservan espacio y no se desplazan junto al JSON.
	_actions_scroll.custom_minimum_size.y = minf(_actions.get_combined_minimum_size().y, size.y * 0.4)

func _show(value: Dictionary) -> void:
	_report.text = JSON.stringify(value, "  ")
	$Margin/Layout/ReportScroll.set_deferred("scroll_vertical", 0)

func _execute_tests() -> void:
	_controller.close()
	var report: Dictionary = preload("res://tests/native_bridge_probe.gd").verify()
	_report.text = ("NIM06 FUNCTIONAL PASS" if report.ok else "NIM06 FUNCTIONAL FAIL") + "\n" + JSON.stringify(report, "  ")
	$Margin/Layout/ReportScroll.set_deferred("scroll_vertical", 0)
	print("NIM06_FUNCTIONAL_REPORT " + JSON.stringify(report))
	var file := FileAccess.open("user://nim06-result.json", FileAccess.WRITE)
	if file != null:
		file.store_string(JSON.stringify(report, "  "))
		file.close()
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		get_tree().quit(0 if report.ok else 1)

func _exit_tree() -> void:
	if is_instance_valid(_launcher):
		_launcher.show()
	if get_window().size_changed.is_connected(_update_scale):
		get_window().size_changed.disconnect(_update_scale)
	get_window().content_scale_size = _previous_scale_size
	_controller.close()

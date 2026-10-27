extends Node
## Entrada de diagnóstico independiente de la UI y de las ramas NIM-05/IA.
func _ready() -> void:
	if not ClassDB.class_exists("CoreRPGHost"):
		return
	if OS.get_cmdline_user_args().has("--nim07-i3-self-test"):
		_i3_self_test.call_deferred()
		return
	if OS.get_cmdline_user_args().has("--nim07-i2-self-test"):
		_i2_self_test.call_deferred()
		return
	if OS.get_cmdline_user_args().has("--nim06-self-test"):
		_self_test.call_deferred()
	var layer := CanvasLayer.new()
	layer.name = "Launcher"
	layer.layer = 20
	add_child(layer)
	var button := Button.new()
	button.text = "CoreRPG · prueba nativa"
	button.position = Vector2(12, 12)
	button.pressed.connect(func(): get_tree().change_scene_to_file("res://native_vertical.tscn"))
	layer.add_child(button)

func _self_test() -> void:
	await get_tree().process_frame
	get_tree().change_scene_to_file("res://native_vertical.tscn")

func _i2_self_test() -> void:
	await get_tree().process_frame
	var checks := preload("res://tests/nim07_i2_checks.gd").new()
	await checks.run(get_tree())

func _i3_self_test() -> void:
	await get_tree().process_frame
	var checks := preload("res://tests/nim07_i3_checks.gd").new()
	await checks.run(get_tree())

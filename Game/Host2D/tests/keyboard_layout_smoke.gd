extends SceneTree
## Pruebas geométricas; el teclado Samsung real se valida físicamente.
const KeyboardLayout = preload("res://scripts/keyboard_layout.gd")

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	var view := Vector2(1280, 720)
	var screen := Vector2i(2560, 1600)
	var bluetooth: Dictionary = KeyboardLayout.calculate(view, 0, screen, 720.0, true)
	if bluetooth.get("compact", true) or float(bluetooth.get("usable_height", 0)) != 720.0:
		errors.append("Bluetooth sin IME no conserva la pantalla completa")
	var physical: Dictionary = KeyboardLayout.calculate(view, 720, screen, 720.0, true)
	if not physical.get("compact", false) or absf(float(physical.get("usable_height", 0)) - 360.0) > 0.5:
		errors.append("Altura teclado Samsung no se convierte a coordenadas Godot")
	var resized: Dictionary = KeyboardLayout.calculate(Vector2(1280, 360), 720, screen, 720.0, true)
	if absf(float(resized.get("usable_height", 0)) - 360.0) > 0.5:
		errors.append("Android ha redimensionado: se descuenta el teclado dos veces")
	var desktop: Dictionary = KeyboardLayout.calculate(view, 720, screen, 720.0, false)
	if desktop.get("compact", true):
		errors.append("Regresión: se compacta Windows")
	var closed: Dictionary = KeyboardLayout.calculate(view, 0, screen, 720.0, true)
	if closed.get("compact", true):
		errors.append("No vuelve el diseño normal al cerrar el teclado")
	var tiny: Dictionary = KeyboardLayout.calculate(view, 1700, screen, 720.0, true)
	if not tiny.get("compact", false) or float(tiny.get("usable_height", 0)) < 150.0:
		errors.append("No se conserva altura mínima para entrada")
	if errors.is_empty():
		print("NIM-03 KEYBOARD PASS: virtual compacto, Bluetooth pantalla completa, sin doble descuento.")
		quit(0)
	else:
		for item in errors:
			push_error("NIM-03 KEYBOARD FAIL: " + item)
		quit(1)

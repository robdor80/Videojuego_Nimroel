extends RefCounted
## NIM-03: medidas de UI, sin acceder a WorldState, servicios ni red.
## display_get_height() está en píxeles físicos; el viewport de Godot puede
## emplear coordenadas escaladas y Android puede ya haber reducido su altura.
const SOFT_KEYBOARD_MIN_PX := 48

static func calculate(view: Vector2, keyboard_pixels: int, screen_pixels: Vector2i, normal_height: float, is_mobile: bool) -> Dictionary:
	if not is_mobile or keyboard_pixels <= SOFT_KEYBOARD_MIN_PX or screen_pixels.x <= 0 or view.x <= 0.0:
		return {"compact": false, "usable_height": view.y}
	var pixels_per_ui_unit: float = float(screen_pixels.x) / view.x
	var occluded_height: float = float(keyboard_pixels) / pixels_per_ui_unit
	# Hay sistemas Android que ajustan automáticamente el viewport y otros
	# que dibujan el teclado sobre él. Evitamos descontarlo dos veces.
	var resized_by_android: bool = view.y < normal_height * 0.85
	var usable_height: float = view.y if resized_by_android else view.y - occluded_height
	# Si una distribución extrema deja menos de 150 unidades, mantenemos
	# el cuadro de escritura, pero solo la prueba física acredita visibilidad.
	return {
		"compact": true,
		"usable_height": clampf(usable_height, minf(150.0, view.y), view.y)
	}

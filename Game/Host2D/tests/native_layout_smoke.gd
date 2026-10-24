extends SceneTree
## Geometría y entrada sintética de presentación; no acredita un dispositivo físico.
const Scene = preload("res://native_vertical.tscn")
const Layout = preload("res://scripts/native_vertical.gd")
var _errors: Array[String] = []

func check(ok: bool, message: String) -> void:
	if not ok:
		_errors.append(message)

func _initialize() -> void:
	_run.call_deferred()

func settle() -> void:
	for frame in range(8):
		await process_frame

func _run() -> void:
	var previous_size := root.size
	var previous_scale := root.content_scale_size
	var panel := Scene.instantiate()
	root.add_child(panel)
	var scroll: ScrollContainer = panel.get_node("Margin/Layout/ReportScroll")
	var report: Label = scroll.get_node("Report")
	var actions: ScrollContainer = panel.get_node("Margin/Layout/ActionsScroll")
	var back: Button = panel.get_node("Margin/Layout/Back")
	# Un único resultado pequeño de muchas líneas y un token largo, sin archivos.
	var payload := {"lines": range(80), "long_token": "abcdef".repeat(100), "last": "FIN_RESULTADO"}
	panel._show(payload)
	for dimensions in [Vector2i(1280, 720), Vector2i(640, 800), Vector2i(800, 360), Vector2i(360, 640)]:
		root.size = dimensions
		await settle()
		var visible := Rect2(Vector2.ZERO, Vector2(dimensions))
		check(visible.encloses(back.get_global_rect()), "Volver fuera de ventana %s" % dimensions)
		check(scroll.size.y >= 48, "Resultado sin altura útil %s" % dimensions)
		check(actions.get_global_rect().end.y <= scroll.get_global_rect().position.y, "Controles solapan resultado")
		check(scroll.get_global_rect().end.y <= back.get_global_rect().position.y, "Resultado solapa Volver")
		check(report.size.x <= scroll.size.x, "JSON desborda horizontalmente")
		check(report.text == JSON.stringify(payload, "  "), "Resultado truncado")
		if dimensions.x == 360:
			check(report.get_line_count() >= 100, "Token JSON largo no se envuelve completo")
		var bar := scroll.get_v_scroll_bar()
		check(bar.max_value > bar.page, "No hay rango vertical para JSON largo")
		scroll.scroll_vertical = int(bar.max_value)
		await settle()
		check(report.get_global_rect().end.y <= scroll.get_global_rect().end.y + 1, "No se alcanza final JSON")
		for button in actions.get_node("Actions").get_children():
			check(button.size.y >= 48 and button.get_theme_font_size("font_size") == 18, "Tamaño táctil/texto incorrecto")
		var last: Control = actions.get_node("Actions").get_child(-1)
		actions.ensure_control_visible(last)
		await settle()
		check(last.get_global_rect().end.y <= actions.get_global_rect().end.y + 1, "Último control inaccesible")
	# Entrada sintética de rueda y gesto pan. El arrastre Android queda físico.
	scroll.scroll_vertical = 0
	await settle()
	var point := scroll.get_global_rect().get_center()
	var wheel := InputEventMouseButton.new()
	wheel.position = point
	wheel.global_position = point
	wheel.button_index = MOUSE_BUTTON_WHEEL_DOWN
	wheel.pressed = true
	root.push_input(wheel)
	await settle()
	check(scroll.scroll_vertical > 0, "Rueda no desplaza resultado")
	scroll.scroll_vertical = 0
	var pan := InputEventPanGesture.new()
	pan.position = point
	pan.delta = Vector2(0, 2)
	root.push_input(pan)
	await settle()
	check(scroll.scroll_vertical > 0, "Gesto pan no desplaza resultado")
	check(Layout.logical_size(Vector2i(2800, 1752), 320, true) == Vector2i(1400, 876), "Densidad Android incorrecta")
	check(Layout.logical_size(Vector2i(1400, 1752), 320, true) == Vector2i(700, 876), "Pantalla dividida encoge escala")
	check(Layout.logical_size(Vector2i(1280, 720), 320, false) == Vector2i(1280, 720), "Escala Windows alterada por DPI Android")
	panel._show({"status": "ok"})
	await settle()
	check(scroll.scroll_vertical == 0, "Nuevo resultado no vuelve al inicio")
	panel.queue_free()
	await settle()
	check(root.content_scale_size == previous_scale, "No restaura escala al salir")
	root.size = previous_size
	if _errors.is_empty():
		print("NIM06 LAYOUT PASS: 4 tamaños, JSON íntegro/final accesible, rueda/pan sintéticos, controles y escala Android/Windows.")
	else:
		for message in _errors:
			push_error("NIM06 LAYOUT FAIL: " + message)
	quit(0 if _errors.is_empty() else 1)

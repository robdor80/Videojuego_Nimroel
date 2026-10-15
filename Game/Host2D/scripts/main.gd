extends Control
## Nimroel 2D NIM-01: solo presentación, SIN autoridad de mundo.
## No existe conexión con CoreRPG/Gemini en esta maqueta ejecutable.

const GATEWAY = preload("res://scripts/demo_gateway.gd")
const PIPELINE = preload("res://scripts/interaction_pipeline.gd")
const ART_SCENE = preload("res://art/aldea_fondo_provisional.svg")
const ART_PORTRAIT = preload("res://art/retrato_provisional.svg")

var _backdrop: TextureRect
var _shade: ColorRect
var _masthead: PanelContainer
var _conversation_panel: PanelContainer
var _content_area: Control
var _top_info: VBoxContainer
var _entry_dock: VBoxContainer
var _history_scroll: ScrollContainer
var _history_messages: VBoxContainer
var _input: LineEdit
var _portrait_line: HBoxContainer
var _portrait: TextureRect
var _hint: Label
var _service_state: Label
var _mode_button: Button
var _integration_mode: bool = false
var _turn_sequence: int = 0

func _ready() -> void:
	_build_interface()
	get_viewport().size_changed.connect(_update_layout)
	_update_layout()
	_reset_demo()

func _build_interface() -> void:
	_backdrop = TextureRect.new()
	_backdrop.name = "FondoIlustrado"
	_backdrop.texture = ART_SCENE
	_backdrop.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_backdrop.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	_backdrop.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(_backdrop)
	_backdrop.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)

	_shade = ColorRect.new()
	_shade.name = "VeloAmbiental"
	_shade.color = Color(0.025, 0.048, 0.061, 0.24)
	_shade.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(_shade)
	_shade.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)

	_masthead = PanelContainer.new()
	_masthead.name = "Cabecera"
	_masthead.add_theme_stylebox_override("panel", _panel_style(Color(0.055, 0.088, 0.106, 0.90), 12))
	add_child(_masthead)
	var header_content := VBoxContainer.new()
	header_content.add_theme_constant_override("separation", 1)
	_masthead.add_child(header_content)
	var title := _make_label("NIMROEL  ·  TRESKAL", 24, Color(0.956, 0.891, 0.703))
	header_content.add_child(title)
	var subtitle := _make_label("v0.0.1  |  LABORATORIO 2D CONVERSACIONAL", 12, Color(0.75, 0.84, 0.80))
	header_content.add_child(subtitle)

	_conversation_panel = PanelContainer.new()
	_conversation_panel.name = "PanelConversacion"
	_conversation_panel.add_theme_stylebox_override("panel", _panel_style(Color(0.055, 0.087, 0.107, 0.955), 18))
	add_child(_conversation_panel)
	_content_area = Control.new()
	_content_area.name = "Contenido"
	_conversation_panel.add_child(_content_area)

	_top_info = VBoxContainer.new()
	_top_info.name = "CabeceraRelato"
	_top_info.add_theme_constant_override("separation", 5)
	_content_area.add_child(_top_info)

	_entry_dock = VBoxContainer.new()
	_entry_dock.name = "BarraInferior"
	_entry_dock.add_theme_constant_override("separation", 9)
	_content_area.add_child(_entry_dock)

	var heading := _make_label("TU PARTIDA  /  RELATO", 15, Color(0.953, 0.850, 0.617))
	_top_info.add_child(heading)
	_service_state = _make_label("MODO MAQUETA   ·   MUNDO NO CARGADO   ·   GEMINI Y CORERPG DESCONECTADOS", 11, Color(1.0, 0.72, 0.51))
	_service_state.name = "EstadoServicios"
	_service_state.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_top_info.add_child(_service_state)

	_history_scroll = ScrollContainer.new()
	_history_scroll.name = "Historial"
	_history_scroll.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_history_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	_history_scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	_content_area.add_child(_history_scroll)
	_history_messages = VBoxContainer.new()
	_history_messages.name = "Bocadillos"
	_history_messages.add_theme_constant_override("separation", 11)
	_history_messages.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_history_scroll.add_child(_history_messages)

	_portrait_line = HBoxContainer.new()
	_portrait_line.name = "RetratoEnConversacion"
	_portrait_line.add_theme_constant_override("separation", 12)
	_entry_dock.add_child(_portrait_line)
	_portrait = TextureRect.new()
	_portrait.name = "RetratoProvisional"
	_portrait.texture = ART_PORTRAIT
	_portrait.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_portrait.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	_portrait.custom_minimum_size = Vector2(76, 76)
	_portrait_line.add_child(_portrait)
	var portrait_caption := _make_label("RETRATO PROVISIONAL\nSin NPC real ni identidad generada", 13, Color(0.85, 0.88, 0.77))
	portrait_caption.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	portrait_caption.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_portrait_line.add_child(portrait_caption)

	var entry_row := HBoxContainer.new()
	entry_row.name = "EntradaFila"
	entry_row.add_theme_constant_override("separation", 8)
	_entry_dock.add_child(entry_row)
	_input = LineEdit.new()
	_input.name = "EntradaLibre"
	_input.placeholder_text = "¿Qué veo desde donde estoy?"
	_input.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_input.custom_minimum_size.y = 49
	_input.add_theme_font_size_override("font_size", 16)
	_input.text_submitted.connect(_on_send)
	entry_row.add_child(_input)

	var submit := Button.new()
	submit.name = "Enviar"
	submit.text = "Enviar"
	submit.custom_minimum_size = Vector2(84, 49)
	submit.pressed.connect(_send_from_button)
	entry_row.add_child(submit)

	var footer := HBoxContainer.new()
	footer.name = "Pie"
	footer.add_theme_constant_override("separation", 8)
	_entry_dock.add_child(footer)
	var reset := Button.new()
	reset.name = "ReiniciarMaqueta"
	reset.text = "Reiniciar demo"
	reset.pressed.connect(_reset_demo)
	footer.add_child(reset)
	_mode_button = Button.new()
	_mode_button.name = "ModoIntegracion"
	_mode_button.text = "Modo: demo"
	_mode_button.tooltip_text = "Alterna laboratorio y conexión real (todavía no disponible)"
	_mode_button.pressed.connect(_toggle_mode)
	footer.add_child(_mode_button)
	_hint = _make_label("Solo se ensaya la interfaz", 11, Color(0.73, 0.78, 0.78))
	_hint.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_hint.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	footer.add_child(_hint)

func _update_layout() -> void:
	if not is_instance_valid(_conversation_panel):
		return
	var view: Vector2 = size
	if view.x < 1.0 or view.y < 1.0:
		view = get_viewport_rect().size
	var phone: bool = view.x < 760.0
	var margin: float = 12.0 if phone else 20.0
	_masthead.position = Vector2(margin, margin)
	_masthead.size = Vector2(maxf(250.0, view.x - 2.0 * margin), 72.0)
	if phone:
		var top: float = maxf(102.0, view.y * 0.32)
		_conversation_panel.position = Vector2(margin, top)
		_conversation_panel.size = Vector2(maxf(250.0, view.x - 2.0 * margin), maxf(220.0, view.y - top - margin))
	else:
		var left: float = maxf(340.0, view.x * 0.515)
		_conversation_panel.position = Vector2(left, 109.0)
		_conversation_panel.size = Vector2(maxf(340.0, view.x - left - margin), maxf(260.0, view.y - 109.0 - margin))
	call_deferred("_layout_panel_controls")

func _layout_panel_controls() -> void:
	# Las acciones de entrada NO dependen del tamaño del historial.
	# La barra se coloca abajo de la zona útil; el historial ocupa lo restante.
	if not is_instance_valid(_content_area):
		return
	var inner: Vector2 = _content_area.size
	if inner.x < 1.0 or inner.y < 1.0:
		return
	var head_height: float = _top_info.get_combined_minimum_size().y
	_top_info.position = Vector2.ZERO
	_top_info.size = Vector2(inner.x, head_height)
	var dock_height: float = _entry_dock.get_combined_minimum_size().y
	_entry_dock.position = Vector2(0.0, maxf(0.0, inner.y - dock_height))
	_entry_dock.size = Vector2(inner.x, dock_height)
	var history_top: float = head_height + 12.0
	var history_bottom: float = _entry_dock.position.y - 10.0
	_history_scroll.position = Vector2(0.0, history_top)
	_history_scroll.size = Vector2(inner.x, maxf(1.0, history_bottom - history_top))

func _send_from_button() -> void:
	_on_send(_input.text)

func _on_send(raw_text: String) -> void:
	var mode: String = PIPELINE.MODE_INTEGRATION if _integration_mode else PIPELINE.MODE_DEMO
	var result: Dictionary = submit_turn_for_test(raw_text, mode)
	if str(result.get("status", "")) == "rejected":
		_hint.text = str(result.get("reply", "Entrada no válida"))
		return
	_turn_sequence += 1
	_input.clear()
	_append_bubble("TÚ", raw_text.strip_edges(), true)
	var demo: bool = str(result.get("status", "")) == "demo"
	_append_bubble("SIMULADOR · NO ES UN NPC" if demo else "SISTEMA · CONEXIÓN NO DISPONIBLE", str(result.get("reply", "")), false)
	_portrait_line.visible = demo and bool(result.get("portrait_demo", false))
	_hint.text = "Sin hechos del mundo modificados"
	call_deferred("_layout_panel_controls")

func _toggle_mode() -> void:
	_integration_mode = not _integration_mode
	_mode_button.text = "Modo: integración" if _integration_mode else "Modo: demo"
	_service_state.text = "MODO INTEGRACIÓN   ·   CORERPG / GEMINI / VOZ NO DISPONIBLES" if _integration_mode else "MODO MAQUETA   ·   MUNDO NO CARGADO   ·   GEMINI Y CORERPG DESCONECTADOS"
	_hint.text = "Conexiones reales sin verificar" if _integration_mode else "Solo se ensaya la interfaz"
	call_deferred("_layout_panel_controls")

func _reset_demo() -> void:
	if not is_instance_valid(_history_messages):
		return
	for item in _history_messages.get_children():
		_history_messages.remove_child(item)
		item.queue_free()
	_append_bubble("SISTEMA · PRUEBA", "Bienvenido al laboratorio visual de Nimroel RPG.\n\nEsta es una demostración de interfaz, NO una partida generada. Todavía no están conectados Gemini ni CoreRPG y ninguna acción modifica el mundo.\n\nPrueba: ¿Qué veo desde donde estoy? / Avanzo por la aldea / Hablo con un aldeano.", false)
	_portrait_line.visible = false
	_input.clear()
	_hint.text = "Solo se ensaya la interfaz"
	call_deferred("_layout_panel_controls")

func _append_bubble(author: String, body: String, player: bool) -> void:
	var row := HBoxContainer.new()
	row.name = "MensajeJugador" if player else "MensajeRespuesta"
	row.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_history_messages.add_child(row)
	var spacer := Control.new()
	spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	if player:
		row.add_child(spacer)
	var bubble := PanelContainer.new()
	bubble.custom_minimum_size.x = maxf(195.0, minf(460.0, _conversation_panel.size.x - 94.0))
	bubble.add_theme_stylebox_override("panel", _panel_style(Color(0.17, 0.30, 0.29, 0.98) if player else Color(0.12, 0.17, 0.19, 0.98), 12))
	row.add_child(bubble)
	var content := VBoxContainer.new()
	content.add_theme_constant_override("separation", 5)
	bubble.add_child(content)
	var heading := _make_label(author, 11, Color(0.88, 0.95, 0.75) if player else Color(0.94, 0.82, 0.62))
	content.add_child(heading)
	var text_label := Label.new()
	text_label.text = body
	text_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	text_label.add_theme_font_size_override("font_size", 16)
	text_label.add_theme_color_override("font_color", Color(0.94, 0.95, 0.92))
	content.add_child(text_label)
	if not player:
		row.add_child(spacer)
	call_deferred("_scroll_to_latest")

func _scroll_to_latest() -> void:
	if is_instance_valid(_history_scroll):
		_history_scroll.scroll_vertical = int(_history_scroll.get_v_scroll_bar().max_value)

func submit_intent_for_test(raw_text: String) -> Dictionary:
	## Se conserva el contrato de pruebas NIM-01.
	return GATEWAY.route(raw_text)

func submit_turn_for_test(raw_text: String, mode: String = PIPELINE.MODE_DEMO) -> Dictionary:
	## Contrato NIM-02: no se realizan mutaciones ni peticiones de red.
	return PIPELINE.submit_text(raw_text, mode, _turn_sequence + 1)

func _make_label(value: String, font_px: int, tone: Color) -> Label:
	var output := Label.new()
	output.text = value
	output.add_theme_font_size_override("font_size", font_px)
	output.add_theme_color_override("font_color", tone)
	return output

func _panel_style(tone: Color, rounding: int) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = tone
	style.corner_radius_top_left = rounding
	style.corner_radius_top_right = rounding
	style.corner_radius_bottom_left = rounding
	style.corner_radius_bottom_right = rounding
	style.content_margin_left = 17.0
	style.content_margin_right = 17.0
	style.content_margin_top = 12.0
	style.content_margin_bottom = 12.0
	return style

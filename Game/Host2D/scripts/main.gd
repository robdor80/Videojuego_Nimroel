extends Control
## Nimroel 2D NIM-01: solo presentación, SIN autoridad de mundo.
## No existe conexión con CoreRPG/Gemini en esta maqueta ejecutable.

const GATEWAY = preload("res://scripts/demo_gateway.gd")
const ART_SCENE = preload("res://art/aldea_fondo_provisional.svg")
const ART_PORTRAIT = preload("res://art/retrato_provisional.svg")

var _backdrop: TextureRect
var _shade: ColorRect
var _masthead: PanelContainer
var _conversation_panel: PanelContainer
var _history: RichTextLabel
var _input: LineEdit
var _portrait_line: HBoxContainer
var _portrait: TextureRect
var _hint: Label

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
	var conversation := VBoxContainer.new()
	conversation.name = "Contenido"
	conversation.add_theme_constant_override("separation", 10)
	_conversation_panel.add_child(conversation)

	var heading := _make_label("TU PARTIDA  /  RELATO", 15, Color(0.953, 0.850, 0.617))
	conversation.add_child(heading)
	var state := _make_label("MODO MAQUETA   ·   MUNDO NO CARGADO   ·   GEMINI Y CORERPG DESCONECTADOS", 11, Color(1.0, 0.72, 0.51))
	state.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	conversation.add_child(state)

	_history = RichTextLabel.new()
	_history.name = "Historial"
	_history.bbcode_enabled = false
	_history.scroll_active = true
	_history.scroll_following = true
	_history.selection_enabled = true
	_history.size_flags_vertical = Control.SIZE_EXPAND_FILL
	_history.add_theme_color_override("default_color", Color(0.918, 0.936, 0.920))
	_history.add_theme_font_size_override("normal_font_size", 17)
	conversation.add_child(_history)

	_portrait_line = HBoxContainer.new()
	_portrait_line.name = "RetratoEnConversacion"
	_portrait_line.add_theme_constant_override("separation", 12)
	conversation.add_child(_portrait_line)
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
	entry_row.add_theme_constant_override("separation", 8)
	conversation.add_child(entry_row)
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
	footer.add_theme_constant_override("separation", 8)
	conversation.add_child(footer)
	var reset := Button.new()
	reset.name = "ReiniciarMaqueta"
	reset.text = "Reiniciar demo"
	reset.pressed.connect(_reset_demo)
	footer.add_child(reset)
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

func _send_from_button() -> void:
	_on_send(_input.text)

func _on_send(raw_text: String) -> void:
	var message: String = raw_text.strip_edges()
	if message.is_empty():
		return
	var routed: Dictionary = GATEWAY.route(message)
	_input.clear()
	_history.text += "\n\nTÚ > " + message
	_history.text += "\n\nSIMULADOR [" + str(routed["proposal_type"]) + "] > " + str(routed["demo_response"])
	_portrait_line.visible = bool(routed["portrait_demo"])
	_hint.text = "Sin hechos del mundo modificados"
	_history.call_deferred("scroll_to_line", maxi(0, _history.get_line_count() - 1))

func _reset_demo() -> void:
	if not is_instance_valid(_history):
		return
	_history.text = "Bienvenido al laboratorio visual de Nimroel RPG.\n\nEsta es una demostración de interfaz, NO una partida generada. Todavía no están conectados Gemini ni CoreRPG; ninguna acción modifica el mundo.\n\nPuedes probar estas frases:\n  · ¿Qué veo desde donde estoy?\n  · Avanzo por la aldea y busco a alguien.\n  · Hablo con un aldeano.\n\nEl fondo y el retrato son provisionales y no describen una aldea canónica."
	_portrait_line.visible = false
	_input.clear()
	_hint.text = "Solo se ensaya la interfaz"

func submit_intent_for_test(raw_text: String) -> Dictionary:
	## Puerto de prueba: devuelve estructura de intención SIN efectos secundarios.
	return GATEWAY.route(raw_text)

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

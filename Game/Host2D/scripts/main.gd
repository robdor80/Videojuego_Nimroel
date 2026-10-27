extends Control
## Nimroel 2D NIM-01: solo presentación, SIN autoridad de mundo.
## NIM-07 I1: conversación estructural nativa separada de demo/diagnósticos.

const GATEWAY = preload("res://scripts/demo_gateway.gd")
const PIPELINE = preload("res://scripts/interaction_pipeline.gd")
const GEMINI_DIAGNOSTIC = preload("res://scripts/gemini_diagnostic.gd")
const PROVIDER_DIAGNOSTIC = preload("res://scripts/provider_diagnostic.gd")
const TTS_DIAGNOSTIC = preload("res://scripts/tts_diagnostic.gd")
const KEYBOARD_LAYOUT = preload("res://scripts/keyboard_layout.gd")
const NATIVE_CONVERSATION = preload("res://scripts/native_conversation.gd")
const ART_SCENE = preload("res://art/aldea_fondo_provisional.svg")
const ART_PORTRAIT = preload("res://art/retrato_provisional.svg")

var _backdrop: TextureRect
var _shade: ColorRect
var _masthead: PanelContainer
var _conversation_panel: PanelContainer
var _content_area: Control
var _top_info: VBoxContainer
var _entry_dock: VBoxContainer
var _footer: HBoxContainer
var _history_scroll: ScrollContainer
var _history_messages: VBoxContainer
var _input: LineEdit
var _portrait_line: HBoxContainer
var _portrait: TextureRect
var _hint: Label
var _service_state: Label
var _mode_button: Button
var _native_button: Button
var _v001_button: Button
var _gemini_button: Button
var _title: Label
var _subtitle: Label
var _native_conversation := NATIVE_CONVERSATION.new()
var _native_active: bool = false
var _v001_conversation := NATIVE_CONVERSATION.new(true)
var _active_conversation: RefCounted = _native_conversation
var _gemini_diagnostic
var _provider_diagnostic
var _tts_diagnostic
var _provider_tier: OptionButton
var _provider_row: HBoxContainer
var _integration_mode: bool = false
var _turn_sequence: int = 0
var _keyboard_compact: bool = false
var _portrait_wanted: bool = false
var _keyboard_height_last: int = -1
var _keyboard_poll_time: float = 0.0
var _normal_view_height: float = 720.0

func _ready() -> void:
	_gemini_diagnostic = GEMINI_DIAGNOSTIC.new()
	add_child(_gemini_diagnostic)
	_gemini_diagnostic.probe_finished.connect(_on_gemini_probe_finished)
	_provider_diagnostic = PROVIDER_DIAGNOSTIC.new()
	add_child(_provider_diagnostic)
	_provider_diagnostic.probe_finished.connect(_on_provider_probe_finished)
	# El servicio de voz no existe en Android: sin dependencia del MSI.
	if not OS.has_feature("mobile"):
		_tts_diagnostic = TTS_DIAGNOSTIC.new()
		add_child(_tts_diagnostic)
		_tts_diagnostic.finished.connect(_on_tts_test_finished)
	_build_interface()
	get_viewport().size_changed.connect(_update_layout)
	set_process(OS.has_feature("mobile"))
	_update_layout()
	_reset_demo()

func _process(delta: float) -> void:
	# Android: el cambio de altura del teclado no garantiza un resize de viewport.
	# Un teclado Bluetooth no abre el IME y conserva el layout normal.
	_keyboard_poll_time += delta
	if _keyboard_poll_time < 0.12:
		return
	_keyboard_poll_time = 0.0
	var keyboard_px: int = DisplayServer.virtual_keyboard_get_height()
	if keyboard_px != _keyboard_height_last:
		_keyboard_height_last = keyboard_px
		_update_layout()

func _sync_portrait_visibility() -> void:
	if is_instance_valid(_portrait_line):
		_portrait_line.visible = _portrait_wanted and not _keyboard_compact

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
	_title = _make_label("NIMROEL  ·  TRESKAL", 24, Color(0.956, 0.891, 0.703))
	header_content.add_child(_title)
	_subtitle = _make_label("v0.0.1  |  LABORATORIO 2D CONVERSACIONAL", 12, Color(0.75, 0.84, 0.80))
	_subtitle.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	header_content.add_child(_subtitle)

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

	_native_button = Button.new()
	_native_button.name = "IniciarCoreRPG"
	_native_button.text = "Iniciar experiencia CoreRPG (estructura de prueba)"
	_native_button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_native_button.custom_minimum_size.y = 48
	_native_button.add_theme_font_size_override("font_size", 14)
	_native_button.pressed.connect(_start_native)
	_entry_dock.add_child(_native_button)

	_v001_button = Button.new()
	_v001_button.name = "IniciarV001"
	_v001_button.text = "Iniciar V001 de Treskal (fixture estructural)"
	_v001_button.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_v001_button.custom_minimum_size.y = 48
	_v001_button.add_theme_font_size_override("font_size", 14)
	_v001_button.pressed.connect(_start_v001)
	_entry_dock.add_child(_v001_button)

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
	_mode_button.tooltip_text = "Alterna maqueta e integración antigua bloqueada. CoreRPG tiene su propia entrada."
	_mode_button.pressed.connect(_toggle_mode)
	footer.add_child(_mode_button)
	# Solo Windows: no se activa red en Android ni se añaden controles en la tablet.
	if not OS.has_feature("mobile"):
		var diagnostic_button := Button.new()
		diagnostic_button.name = "DiagnosticoGemini"
		diagnostic_button.text = "Probar Gemini"
		diagnostic_button.tooltip_text = "Envía el texto al proxy local y a Google Gemini. No es gameplay ni respuesta de un NPC."
		diagnostic_button.pressed.connect(_probe_gemini)
		footer.add_child(diagnostic_button)
		_gemini_button = diagnostic_button
	_hint = _make_label("Solo se ensaya la interfaz", 11, Color(0.73, 0.78, 0.78))
	_hint.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_hint.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_hint.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	footer.add_child(_hint)
	_footer = footer
	# NIM-04: fila técnica separada; no se muestra en Android y no altera
	# la barra de envío ni el flujo de partida.
	if not OS.has_feature("mobile"):
		_provider_row = HBoxContainer.new()
		_provider_row.name = "DiagnosticoProveedores"
		_provider_row.add_theme_constant_override("separation", 8)
		_entry_dock.add_child(_provider_row)
		_provider_row.add_child(_make_label("Laboratorio IA (no NPC):", 11, Color(0.78, 0.84, 0.83)))
		_provider_tier = OptionButton.new()
		_provider_tier.name = "NivelDiagnostico"
		_provider_tier.add_item("Sencilla", 0)
		_provider_tier.add_item("Exigente", 1)
		_provider_row.add_child(_provider_tier)
		var provider_button := Button.new()
		provider_button.name = "ProbarProveedores"
		provider_button.text = "Probar proveedores"
		provider_button.tooltip_text = "Envía tu texto al proxy local y al proveedor habilitado. Solo clasificación técnica; no hay NPC ni partida."
		provider_button.pressed.connect(_probe_providers)
		_provider_row.add_child(provider_button)
		var voice_button := Button.new()
		voice_button.name = "PruebaVozLocal"
		voice_button.text = "Escuchar TTS local"
		voice_button.tooltip_text = "Genera una frase en tiempo real con sherpa-onnx local. No es la voz de un NPC ni accede a CoreRPG."
		voice_button.pressed.connect(_probe_tts)
		_provider_row.add_child(voice_button)

func _update_layout() -> void:
	if not is_instance_valid(_conversation_panel):
		return
	var view: Vector2 = size
	if view.x < 1.0 or view.y < 1.0:
		view = get_viewport_rect().size
	var keyboard_px: int = DisplayServer.virtual_keyboard_get_height() if OS.has_feature("mobile") else 0
	var layout: Dictionary = KEYBOARD_LAYOUT.calculate(
		view, keyboard_px, DisplayServer.screen_get_size(), _normal_view_height, OS.has_feature("mobile")
	)
	_keyboard_compact = bool(layout.get("compact", false))
	if not _keyboard_compact:
		_normal_view_height = maxf(_normal_view_height, view.y)
	_masthead.visible = not _keyboard_compact
	_top_info.visible = not _keyboard_compact
	_footer.visible = not _keyboard_compact
	_native_button.visible = not _keyboard_compact
	_v001_button.visible = not _keyboard_compact
	if is_instance_valid(_provider_row):
		_provider_row.visible = not _keyboard_compact and not _native_active
	_sync_portrait_visibility()

	var phone: bool = view.x < 760.0
	var margin: float = 12.0 if phone or _keyboard_compact else 20.0
	_masthead.position = Vector2(margin, margin)
	_masthead.size = Vector2(maxf(250.0, view.x - 2.0 * margin), 72.0)
	if _keyboard_compact:
		# Teclado virtual: conservar historial + texto + Enviar por encima de
		# la zona ocupada. Los elementos decorativos reaparecen al ocultarlo.
		var usable: float = float(layout.get("usable_height", view.y))
		_conversation_panel.position = Vector2(margin, 6.0)
		_conversation_panel.size = Vector2(maxf(250.0, view.x - 2.0 * margin), maxf(150.0, usable - 12.0))
	elif phone:
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
	var head_height: float = _top_info.get_combined_minimum_size().y if _top_info.visible else 0.0
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
	if _native_active:
		var native_result: Dictionary = _active_conversation.submit_text(raw_text)
		if native_result.status == "rejected":
			_hint.text = native_result.reply
			return
		_turn_sequence += 1
		_input.clear()
		_append_bubble("TÚ", raw_text.strip_edges(), true)
		_append_bubble(NATIVE_CONVERSATION.AUTHOR, native_result.reply, false)
		if native_result.status == "unavailable":
			_service_state.text = "CORERPG NO DISPONIBLE · SIN SIMULACIÓN · SIN IA"
		_hint.text = "Consulta local determinista · sin acciones ni IA"
		call_deferred("_layout_panel_controls")
		return
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
	_portrait_wanted = demo and bool(result.get("portrait_demo", false))
	_sync_portrait_visibility()
	_hint.text = "Sin hechos del mundo modificados"
	call_deferred("_layout_panel_controls")

func _probe_gemini() -> void:
	# Interacción deliberada y separada de submit_turn_for_test. No se borra
	# el texto, ni se añade un mensaje de jugador ni se modifica el turno.
	_hint.text = "Diagnóstico externo solicitado (no es una partida)"
	_gemini_diagnostic.probe(_input.text)

func _on_gemini_probe_finished(result: Dictionary) -> void:
	if str(result.get("status", "")) == "ok":
		var kind: String = str(result.get("intent", ""))
		_append_bubble("SISTEMA · DIAGNÓSTICO GEMINI", "Clasificación técnica recibida: " + kind + ". No es una respuesta de NPC; no hay CoreRPG ni mundo conectado.", false)
		_hint.text = "Gemini respondió solo al diagnóstico"
	else:
		var code: String = str(result.get("error_code", "UNKNOWN"))
		_append_bubble("SISTEMA · DIAGNÓSTICO", "No se completó el diagnóstico Gemini (" + code + "). La demo sigue disponible.", false)
		_hint.text = "Diagnóstico sin confirmar"
	call_deferred("_layout_panel_controls")

func _probe_providers() -> void:
	_hint.text = "Diagnóstico multiproveedor solicitado (no es una partida)"
	var tier: String = "complex" if _provider_tier.selected == 1 else "simple"
	_provider_diagnostic.probe(_input.text, tier)

func _on_provider_probe_finished(result: Dictionary) -> void:
	if str(result.get("status", "")) == "ok":
		var provider: String = str(result.get("source", ""))
		var model: String = str(result.get("model", ""))
		var intent: String = str(result.get("intent", ""))
		var latency: String = str(result.get("latency_ms", 0))
		var fallback: String = " · respaldo" if bool(result.get("fallback_used", false)) else ""
		_append_bubble("SISTEMA · PRUEBA IA", provider + " / " + model + fallback + "\nIntención: " + intent + " · " + latency + " ms. No es respuesta NPC ni modifica el mundo.", false)
		_hint.text = "Proveedor verificado solo como clasificación"
	else:
		var code: String = str(result.get("error_code", "UNKNOWN"))
		var reason: String = str(result.get("diagnostic_reason", ""))
		var reason_detail: String = " · Motivo: " + reason if not reason.is_empty() else ""
		_append_bubble("SISTEMA · PRUEBA IA", "Diagnóstico no disponible (" + code + reason_detail + "). La demo sigue operativa y CoreRPG no ha intervenido.", false)
		_hint.text = "Prueba multiproveedor sin confirmar"
	call_deferred("_layout_panel_controls")

func _probe_tts() -> void:
	# Botón explícito: texto visible -> servidor localhost -> inferencia real
	# sherpa-onnx -> WAV -> AudioStreamPlayer. Nunca es un turno de juego.
	_hint.text = "Solicitada síntesis local técnica (sin NPC)"
	_tts_diagnostic.speak_test(_input.text)

func _on_tts_test_finished(result: Dictionary) -> void:
	if result.get("status") == "ok":
		_append_bubble("SISTEMA · PRUEBA DE VOZ", "Audio sintetizado dinámicamente con sherpa-onnx y reproducción iniciada en Godot. Confirma si lo escuchas en el MSI. No es voz de NPC.", false)
		_hint.text = "TTS técnico: reproducción iniciada"
	else:
		_append_bubble("SISTEMA · PRUEBA DE VOZ", "TTS local no disponible (" + str(result.get("error_code", "TTS_UNAVAILABLE")) + "). La demo continúa y no hay voz de NPC.", false)
		_hint.text = "Voz técnica no confirmada"
	call_deferred("_layout_panel_controls")

func _toggle_mode() -> void:
	_native_active = false
	_integration_mode = not _integration_mode
	_show_legacy_header()
	_mode_button.text = "Modo: integración" if _integration_mode else "Modo: demo"
	_service_state.text = "MODO INTEGRACIÓN   ·   CORERPG / GEMINI / VOZ NO DISPONIBLES" if _integration_mode else "MODO MAQUETA   ·   MUNDO NO CARGADO   ·   GEMINI Y CORERPG DESCONECTADOS"
	_hint.text = "Conexiones reales sin verificar" if _integration_mode else "Solo se ensaya la interfaz"
	call_deferred("_layout_panel_controls")

func _reset_demo() -> void:
	if not is_instance_valid(_history_messages):
		return
	_native_active = false
	_integration_mode = false
	_mode_button.text = "Modo: demo"
	_service_state.text = "MODO MAQUETA   ·   MUNDO NO CARGADO   ·   GEMINI Y CORERPG DESCONECTADOS"
	_show_legacy_header()
	for item in _history_messages.get_children():
		_history_messages.remove_child(item)
		item.queue_free()
	_append_bubble("SISTEMA · PRUEBA", "Bienvenido al laboratorio visual de Nimroel RPG.\n\nEsta es una demostración de interfaz, NO una partida generada. Todavía no están conectados Gemini ni CoreRPG y ninguna acción modifica el mundo.\n\nPrueba: ¿Qué veo desde donde estoy? / Avanzo por la aldea / Hablo con un aldeano.", false)
	_portrait_wanted = false
	_sync_portrait_visibility()
	_input.clear()
	_hint.text = "Solo se ensaya la interfaz"
	call_deferred("_layout_panel_controls")

func _show_legacy_header() -> void:
	_title.text = "NIMROEL  ·  TRESKAL"
	_subtitle.text = "v0.0.1  |  LABORATORIO 2D CONVERSACIONAL"
	_backdrop.show()
	_input.placeholder_text = "¿Qué veo desde donde estoy?"
	if is_instance_valid(_gemini_button):
		_gemini_button.show()
	if is_instance_valid(_provider_row):
		_provider_row.visible = not _keyboard_compact

func _start_native() -> void:
	_start_experience(false)

func _start_v001() -> void:
	_start_experience(true)

func _start_experience(v001: bool) -> void:
	var conversation: RefCounted = _v001_conversation if v001 else _native_conversation
	var result: Dictionary = conversation.start()
	if result.status != "ok":
		_append_bubble(NATIVE_CONVERSATION.AUTHOR, result.reply, false)
		_hint.text = "Experiencia nativa no disponible"
		return
	_active_conversation = conversation
	_native_active = true
	_integration_mode = false
	_title.text = "NIMROEL  ·  CORERPG"
	_subtitle.text = "I2  |  V001 — FIXTURE ESTRUCTURAL DE TRESKAL" if v001 else "I1  |  PRUEBA ESTRUCTURAL NEUTRA · SIN TRESKAL NI ALDEA V1"
	_backdrop.hide()
	_mode_button.text = "Modo: nativo"
	if is_instance_valid(_gemini_button):
		_gemini_button.hide()
	if is_instance_valid(_provider_row):
		_provider_row.hide()
	_service_state.text = "CORERPG CONECTADO · CONTEXTO AUTORIZADO · CONSULTAS LOCALES SIN IA"
	_input.placeholder_text = "estado / ¿qué conozco?"
	_portrait_wanted = false
	_sync_portrait_visibility()
	_input.clear()
	if v001:
		_append_bubble(NATIVE_CONVERSATION.AUTHOR, "V001 — fixture estructural. Observador anónimo de prueba; sin aldea jugable ni identidad canónica.\n" + NATIVE_CONVERSATION.HELP, false)
	else:
		_append_bubble(NATIVE_CONVERSATION.AUTHOR, "Experiencia nativa activa: estructura neutra de laboratorio. No es Treskal ni una aldea V1 generada.\n" + NATIVE_CONVERSATION.HELP, false)
	_append_bubble(NATIVE_CONVERSATION.AUTHOR, result.reply, false)
	_hint.text = "Misma instancia durante esta pantalla · guardado V001 pendiente I4" if v001 else "Misma partida durante esta pantalla · sin guardado I1"
	call_deferred("_layout_panel_controls")

func _exit_tree() -> void:
	_native_conversation.close()
	_v001_conversation.close()

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

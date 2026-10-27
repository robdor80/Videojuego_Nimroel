extends RefCounted
## NIM-07: consultas cerradas; conserva capacidades, nunca hechos del mundo.
const World = preload("res://scripts/native_world_controller.gd")
const AUTHOR := "SISTEMA · CORERPG (PRUEBA ESTRUCTURAL)"
const HELP := "Prueba: estado / ¿qué sabe mi personaje? / ¿qué conozco? Solo consultas estructurales locales, sin IA ni acciones."
const V001_HELP := "Puedes preguntar: ¿qué conozco de la aldea?, ¿qué servicios conozco?, ¿qué sé de la herrería?, ¿cuántos habitantes hay?, ¿qué conozco de la herramienta?, ¿dónde está la herramienta? o ¿de dónde procede mi personaje? «estado» resume lo conocido. Solo consultas; V001 es un fixture estructural."
# Repertorio completo tras normalización ortográfica; nunca extraer entidades libres.
const QUERIES := {
	"estado": "summary", "que se": "summary", "que conozco": "summary",
	"que sabe mi personaje": "summary", "que se de la aldea": "village",
	"que conozco de la aldea": "village", "que conozco de esta aldea": "village",
	"que conozco de este lugar": "village", "que servicios conozco": "services",
	"que se de la herreria": "smith", "que conozco de la herreria": "smith",
	"cuantos habitantes hay": "population", "que poblacion conozco": "population",
	"que se de la herramienta": "tool", "que conozco de la herramienta": "tool",
	"donde esta la herramienta": "tool", "de donde procede mi personaje": "origin",
	"cual es el origen de mi personaje": "origin", "que puedo preguntar": "help", "ayuda": "help",
	"que veo": "perception", "que veo desde donde estoy": "perception",
	"donde estoy": "location", "voy a la herreria": "action",
	"hablo con el herrero": "action", "reparo la herramienta": "action", "reparar herramienta": "action",
}
const MAX_MESSAGE_CHARS := 1500
var _world := World.new()
var _started: bool = false
var _v001: bool = false

func _init(use_v001: bool = false) -> void:
	_v001 = use_v001
	_world = World.new(use_v001)

func start() -> Dictionary:
	if _started:
		return _present(_world.query(), _v001)
	var context: Dictionary = _world.start()
	_started = context.get("status") == "ok"
	if not _started:
		_world.close()
		if _v001:
			var code: String = context.get("error_code", "CONTENT_UNAVAILABLE")
			if not code in ["CONTENT_FILE_SET", "CONTENT_READ_FAILED", "CONTENT_LIMIT", "CONTENT_UNTRUSTED_RELEASE", "CONTENT_HASH_MISMATCH", "CORE_NOT_CONNECTED"]:
				code = "CONTENT_UNAVAILABLE"
			return _result("unavailable", "V001 no disponible (" + code + "). No se ha creado ni simulado el fixture.")
	return _present(context, _v001)

func submit_text(raw_text: String) -> Dictionary:
	var text := raw_text.strip_edges()
	if text.is_empty():
		return _result("rejected", "Escribe una consulta antes de enviarla.")
	if text.length() > MAX_MESSAGE_CHARS:
		return _result("rejected", "El mensaje supera el límite de 1500 caracteres.")
	if _v001:
		return _submit_v001(text)
	# Se conserva la ruta neutral I1.
	text = text.to_lower().trim_prefix("¿").trim_suffix("?").strip_edges()
	if text == "qué veo" or text == "que veo":
		return _result("limited", "Todavía no hay percepción visual ni espacial. No puedo describir lo que ves. Usa «estado» para consultar el conocimiento estructural autorizado.")
	if text not in ["estado", "qué sabe mi personaje", "que sabe mi personaje", "qué conozco", "que conozco"]:
		return _result("unsupported", "Consulta no soportada. " + HELP)
	if not _started:
		return _result("unavailable", "CoreRPG no está disponible: inicia la experiencia estructural con una extensión nativa compilada. No se ha simulado una respuesta.")
	return _present(_world.query(), _v001)

static func normalize_query(text: String) -> String:
	text = text.to_lower().strip_edges().trim_prefix("¿").trim_suffix("?").strip_edges()
	for pair in [["á", "a"], ["é", "e"], ["í", "i"], ["ó", "o"], ["ú", "u"], ["ü", "u"]]:
		text = text.replace(pair[0], pair[1])
	return " ".join(text.split(" ", false))

func _submit_v001(text: String) -> Dictionary:
	var intent: String = QUERIES.get(normalize_query(text), "unsupported")
	match intent:
		"help":
			return _result("ok", V001_HELP)
		"perception":
			return _result("limited", "Todavía no hay percepción visual ni espacial. No puedo describir lo que ves. Puedes consultar lo conocido con «estado».")
		"location":
			return _result("limited", "La ubicación actual no está modelada. El origen poblacional conocido no indica posición, vivienda ni procedencia biográfica. Puedes preguntar «¿de dónde procede mi personaje?».")
		"action":
			return _result("unsupported", "Consulta no soportada. Esa acción RPG todavía no está implementada. Solo puedes consultar conocimiento; la contención estructural no permite caminar, conversar, recoger ni reparar.")
		"unsupported":
			return _result("unsupported", "Consulta no soportada. " + V001_HELP)
	if not _started:
		return _result("unavailable", "CoreRPG no está disponible: inicia V001 para consultar el conocimiento autorizado.")
	return format_query(_world.query(), intent, _world.get("_observer"))

func save_game() -> Dictionary:
	if not _v001 or not _started:
		return _result("rejected", "Inicia V001 antes de guardar.")
	var saved: Dictionary = _world.save_slot("treskal")
	return _result("ok", "Partida V001 guardada. Ya puedes cerrar Nimroel y reanudarla al volver.") if saved.status == "ok" else _save_failure(saved)

func resume_game(backup_only: bool = false) -> Dictionary:
	if not _v001:
		return _result("rejected", "La reanudación pertenece a V001.")
	var context: Dictionary = _world.load_slot("treskal", backup_only)
	if context.status != "ok":
		return _save_failure(context)
	_started = true
	var presented := _present(context, true)
	presented["reply"] = ("Partida recuperada desde la copia de seguridad. " if context.get("recovered_backup", false) else "Partida V001 reanudada. ") + presented.reply
	return presented

static func _save_failure(failure: Dictionary) -> Dictionary:
	var code: String = failure.get("error_code", "")
	var explanation := "No se completó el guardado o la recuperación. La partida activa se conserva."
	if code == "LOAD_OPEN_FAILED":
		explanation = "No hay una partida guardada disponible. La partida activa se conserva."
	elif code in ["SAVE_CONTENT_INCOMPATIBLE", "SAVE_SCHEMA_UNSUPPORTED"]:
		explanation = "La partida guardada no es compatible con esta versión de V001. La partida activa se conserva."
	elif code in ["SAVE_LIMIT", "SAVE_FORMAT", "SAVE_HEADER", "SAVE_LENGTH", "SAVE_CHECKSUM", "LOAD_REJECTED", "SAVE_EXISTING_INVALID"]:
		explanation = "El archivo guardado no es válido. Se conserva sin reemplazarlo. Puedes intentar recuperar la copia de seguridad; la partida activa se conserva."
	return _result("rejected", explanation)

func close() -> void:
	_world.close()
	_started = false

static func _result(status: String, reply: String) -> Dictionary:
	# La IU solo recibe texto saneado y estado de presentación, sin el envelope Core.
	return {"status": status, "reply": reply, "world_mutated": false}

func _present(context: Dictionary, v001: bool = false) -> Dictionary:
	if context.get("status") != "ok":
		return _result("unavailable", "CoreRPG no está disponible para esta consulta. Comprueba la compilación nativa e inicia la experiencia. No se ha simulado una respuesta.")
	return format_query(context, "summary", _world.get("_observer")) if v001 else format_context(context)

# La identidad ligada a la capacidad se conserva en el controlador de confianza.
# Todos los hechos y etiquetas siguientes requieren el contexto de esa sesión.
static func format_query(context: Dictionary, intent: String, observer: int = 0) -> Dictionary:
	var validated := format_context(context, true)
	if validated.status != "ok":
		return validated
	if intent not in ["summary", "village", "services", "smith", "population", "tool", "origin"]:
		return _result("unsupported", "Consulta no soportada. " + V001_HELP)
	var facts: Array = context.facts
	var village := _defined_subject(facts, "nimroel.treskal.villages:models/v1")
	var smith := _defined_subject(facts, "nimroel.treskal.villages:capabilities/basic-blacksmithing")
	var tool := _defined_subject(facts, "nimroel.treskal.villages:objects/ordinary-agricultural-tool")
	var lines: Array[String] = []
	if intent in ["summary", "village"]:
		lines.append("Conoces el modelo de aldea V1 agrícola-maderera." if village > 0 else _unknown())
	if intent in ["summary", "village", "services", "smith"]:
		var service := _fact(facts, village, 4, 1, smith)
		if village > 0 and smith > 0 and not service.is_empty():
			lines.append("Conoces una capacidad de herrería básica asociada a la aldea como servicio." if service.present else "Conoces la ausencia de asociación de servicio entre la aldea y la capacidad de herrería básica.")
		elif intent == "smith" and smith > 0:
			lines.append("Conoces la definición de capacidad de herrería básica. Su asociación como servicio no consta entre lo que conoce este observador.")
		else:
			lines.append(_unknown())
		if intent in ["summary", "smith"]:
			var aggregate := _fact(facts, smith, 5)
			if not aggregate.is_empty() and not aggregate.present:
				lines.append("Conoces la ausencia de agregado poblacional en la capacidad de herrería básica. Esto no describe personas ni un edificio físico.")
	if intent in ["summary", "village", "population"]:
		var population := _fact(facts, village, 5)
		if population.is_empty():
			lines.append(_unknown())
		elif population.present:
			lines.append("El agregado de aldea conocido declara " + population.total + " habitantes y " + population.latent + " pendientes de materializar. No es un recuento de personas presentes físicamente.")
		else:
			lines.append("Conoces la ausencia de agregado poblacional en la aldea; eso no significa que tenga cero habitantes.")
	if intent in ["summary", "tool"]:
		if tool == 0:
			lines.append(_unknown())
		else:
			lines.append("Conoces la categoría de herramienta agrícola ordinaria.")
			var containment := _fact(facts, tool, 3)
			if containment.is_empty():
				lines.append("Su contención no consta entre lo que conoce este observador.")
			elif not containment.present:
				lines.append("Conoces la ausencia de contención de la herramienta.")
			elif smith > 0 and containment.reference == smith:
				lines.append("La herramienta está contenida estructuralmente en la capacidad de herrería básica. No indica una ubicación física, propiedad ni posibilidad de recogerla o repararla.")
			else:
				lines.append("Conoces su contención estructural, pero el destino no tiene una etiqueta autorizada en esta respuesta. No indica posición física.")
	if intent in ["summary", "origin"]:
		var origin := _fact(facts, observer, 6) if _knows(facts, observer) else {}
		if origin.is_empty():
			lines.append(_unknown())
		elif not origin.present:
			lines.append("Conoces la ausencia de origen poblacional de tu observador de prueba.")
		elif village > 0 and origin.reference == village:
			lines.append("El origen poblacional conocido de tu observador de prueba es el agregado de aldea V1 agrícola-maderera. No indica ubicación actual, vivienda ni procedencia biográfica.")
		else:
			lines.append("Conoces un origen poblacional, pero el agregado no tiene una etiqueta autorizada en esta respuesta. No indica ubicación actual ni biografía.")
	var heading := "V001 — fixture estructural."
	if context.context_status != "complete":
		heading += " Contexto truncado: pueden faltar hechos; no permite concluir ausencia."
	return _result("ok", heading + "\n" + "\n".join(lines))

static func _unknown() -> String:
	return "Ese dato no consta entre lo que conoce este observador. No demuestra ausencia en el mundo."

static func _knows(facts: Array, subject: int) -> bool:
	return facts.any(func(f): return f.kind == 1 and f.subject == subject and f.present)

static func _defined_subject(facts: Array, definition: String) -> int:
	var subjects: Array[int] = []
	for fact in facts:
		if fact.kind == 2 and fact.present and fact.definition_id == definition and _knows(facts, fact.subject) and fact.subject not in subjects:
			subjects.append(fact.subject)
	return subjects[0] if subjects.size() == 1 else 0

static func _fact(facts: Array, subject: int, kind: int, relation: int = 0, target: int = 0) -> Dictionary:
	if subject < 1:
		return {}
	for fact in facts:
		if fact.subject == subject and fact.kind == kind:
			if kind != 4 or (fact.relation_kind == str(relation) and target > 0 and fact.target == target):
				return fact
	return {}

static func format_context(context: Dictionary, v001: bool = false) -> Dictionary:
	# Lista cerrada de campos interpretables de la vista ligada al jugador.
	# No serializar el contexto, errores nativos ni metadatos privilegiados.
	var limited := _result("limited", "El contexto no se puede interpretar con garantías en esta prueba. No se afirman hechos.")
	if context.get("status") != "ok" or context.get("api_version") != 1 or context.get("context_contract_version") != 1 or context.get("audience") != "player":
		return limited
	var completeness = context.get("context_status")
	if completeness not in ["complete", "examination_limit", "selection_limit", "output_capacity", "content_limit"] or not context.get("facts") is Array:
		return limited
	var facts: Array = context.facts
	if facts.size() > 256:
		return limited
	var known: Array[int] = []
	for fact in facts:
		if not fact is Dictionary or not fact.get("subject") is int or fact.subject < 1 or fact.subject > 4096 or not fact.get("kind") is int or fact.kind not in ([1, 2, 3, 4, 5, 6] if v001 else [1, 3]) or not fact.get("present") is bool or fact.get("provenance") not in ["remembered", "temporary_grant"]:
			return limited
		if fact.kind == 1 and fact.present:
			known.append(fact.subject)
	var lines: Array[String] = []
	for fact in facts:
		var entity := "Entidad estructural técnica #" + str(fact.subject)
		if fact.kind == 1:
			lines.append(entity + (": existencia conocida." if fact.present else ": ausencia conocida."))
		elif fact.subject not in known:
			return limited
		elif fact.kind == 2:
			if not fact.present:
				lines.append(entity + ": ausencia de definición conocida.")
			elif fact.get("definition_id") in V001_DEFINITIONS:
				lines.append(entity + ": definición conocida «" + V001_DEFINITIONS[fact.definition_id] + "».")
			else:
				return limited
		elif fact.kind == 5:
			if not fact.present:
				lines.append(entity + ": ausencia de agregado poblacional conocida.")
			elif _decimal(fact.get("total")) and _decimal(fact.get("latent")) and int(fact.latent) <= int(fact.total):
				lines.append(entity + ": población declarada " + fact.total + "; reserva latente " + fact.latent + ". No indica presencia física.")
			else:
				return limited
		elif fact.kind == 4:
			if fact.get("relation_kind") not in ["1", "2", "3"] or not fact.get("target") is int:
				return limited
			if fact.target in known:
				var relation: String = {"1": "asociación de servicio", "2": "conexión exterior abstracta", "3": "asociación poblacional"}[fact.relation_kind]
				lines.append(entity + ": " + relation + (" conocida con #" if fact.present else " ausente con #") + str(fact.target) + ". Sin significado espacial o profesional implícito.")
			else:
				lines.append(entity + ": relación conocida; extremo sin identidad autorizada.")
		elif fact.kind in [3, 6]:
			if fact.kind == 6:
				if not fact.present:
					lines.append(entity + ": ausencia de origen poblacional conocida.")
				elif fact.get("reference") is int and fact.reference in known:
					lines.append(entity + ": origen poblacional conocido en #" + str(fact.reference) + "; sin ubicación física.")
				else:
					lines.append(entity + ": origen conocido; agregado sin identidad autorizada.")
			elif not fact.present:
				lines.append(entity + ": ausencia de contención conocida.")
			elif not fact.get("reference") is int or fact.reference < 1 or fact.reference > 4096:
				return limited
			elif fact.reference in known:
				lines.append(entity + ": contención conocida en entidad estructural técnica #" + str(fact.reference) + ". No indica desplazamiento ni posición física.")
			else:
				lines.append(entity + ": contención conocida; destino sin identidad autorizada en esta respuesta.")
		else:
			return limited
	var heading := "Contexto estructural completo para esta consulta." if completeness == "complete" else "Contexto estructural truncado: la consulta alcanzó un límite; pueden faltar hechos."
	if lines.is_empty():
		lines.append("No hay hechos autorizados en esta respuesta. Eso no demuestra ausencia en el mundo.")
	return _result("ok", heading + "\n" + "\n".join(lines) + ("\nV001 — fixture estructural. Sin edificios físicos, profesiones, NPC dialogantes ni percepción espacial. Lo no indicado permanece desconocido." if v001 else "\nSon datos de conocimiento autorizado; lo no indicado permanece desconocido. No describen una aldea ni NPC."))

# Traducción documental cerrada de los cuatro IDs de la publicación verificada.
# Solo se consulta cuando Core ha emitido el hecho de definición autorizado.
const V001_DEFINITIONS := {
	"nimroel.treskal.villages:models/v1": "modelo de aldea V1 agrícola-maderera",
	"nimroel.treskal.villages:capabilities/basic-blacksmithing": "capacidad de herrería básica",
	"nimroel.treskal.villages:capabilities/local-tavern": "capacidad de taberna local",
	"nimroel.treskal.villages:objects/ordinary-agricultural-tool": "categoría de herramienta agrícola ordinaria",
}

static func _decimal(value: Variant) -> bool:
	return value is String and value.is_valid_int() and str(int(value)) == value and int(value) >= 0 and int(value) <= 4096

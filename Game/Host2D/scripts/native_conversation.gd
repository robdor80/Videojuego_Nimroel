extends RefCounted
## NIM-07 I1: consultas cerradas; conserva capacidades, nunca hechos del mundo.
const World = preload("res://scripts/native_world_controller.gd")
const AUTHOR := "SISTEMA · CORERPG (PRUEBA ESTRUCTURAL)"
const HELP := "Prueba: estado / ¿qué sabe mi personaje? / ¿qué conozco? Solo consultas estructurales locales, sin IA ni acciones."
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
	# Solo normalizamos mayúsculas, espacios exteriores y signos de pregunta.
	text = text.to_lower().trim_prefix("¿").trim_suffix("?").strip_edges()
	if text == "qué veo" or text == "que veo":
		return _result("limited", "Todavía no hay percepción visual ni espacial. No puedo describir lo que ves. Usa «estado» para consultar el conocimiento estructural autorizado.")
	if text not in ["estado", "qué sabe mi personaje", "que sabe mi personaje", "qué conozco", "que conozco"]:
		return _result("unsupported", "Consulta no soportada. " + HELP)
	if not _started:
		return _result("unavailable", "CoreRPG no está disponible: inicia la experiencia estructural con una extensión nativa compilada. No se ha simulado una respuesta.")
	return _present(_world.query(), _v001)

func close() -> void:
	_world.close()
	_started = false

static func _result(status: String, reply: String) -> Dictionary:
	# La IU solo recibe texto saneado y estado de presentación, sin el envelope Core.
	return {"status": status, "reply": reply, "world_mutated": false}

static func _present(context: Dictionary, v001: bool = false) -> Dictionary:
	if context.get("status") != "ok":
		return _result("unavailable", "CoreRPG no está disponible para esta consulta. Comprueba la compilación nativa e inicia la experiencia. No se ha simulado una respuesta.")
	return format_context(context, v001)

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

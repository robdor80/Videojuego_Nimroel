extends Node
## NIM-05: banco de voz TÉCNICO Windows, nunca un NPC.
## Usa sherpa-onnx en el proceso local opt-in Tools/NIM05/tts_local.py.
signal finished(result: Dictionary)

const ENDPOINT := "http://127.0.0.1:8767/v1/tts-test"
const DEFAULT_TEXT := "Esta es una prueba técnica de voz local en Nimroel."
const MAX_CHARS := 160
const MAX_WAV_BYTES := 2000000

var _http: HTTPRequest
var _player: AudioStreamPlayer
var _busy := false

func _ready() -> void:
	if OS.has_feature("mobile"):
		return
	_http = HTTPRequest.new()
	_http.timeout = 45.0
	_http.body_size_limit = MAX_WAV_BYTES
	add_child(_http)
	_http.request_completed.connect(_completed)
	_player = AudioStreamPlayer.new()
	_player.bus = "Master"
	add_child(_player)

func speak_test(raw_text: String) -> void:
	if OS.has_feature("mobile"):
		finished.emit(_fail("MOBILE_TTS_LAB_DISABLED"))
		return
	if _busy:
		finished.emit(_fail("TTS_TEST_BUSY"))
		return
	var text: String = raw_text.strip_edges()
	if text.is_empty():
		text = DEFAULT_TEXT
	if text.length() > MAX_CHARS:
		finished.emit(_fail("TTS_TEXT_TOO_LONG"))
		return
	var token: String = OS.get_environment("NIMROEL_LOCAL_TOKEN")
	if token.is_empty():
		finished.emit(_fail("LOCAL_AUTH_REQUIRED"))
		return
	_busy = true
	var request_body: String = JSON.stringify({"purpose": "technical_tts_test", "text": text})
	var err: Error = _http.request(ENDPOINT, PackedStringArray([
		"Content-Type: application/json",
		"X-Nimroel-Token: " + token
	]), HTTPClient.METHOD_POST, request_body)
	if err != OK:
		_busy = false
		finished.emit(_fail("TTS_SERVER_NOT_CONNECTED"))

func _completed(result: int, status: int, _headers: PackedStringArray, bytes: PackedByteArray) -> void:
	_busy = false
	if result != HTTPRequest.RESULT_SUCCESS:
		finished.emit(_fail("TTS_SERVER_NOT_CONNECTED"))
		return
	if status != 200:
		finished.emit(_fail(_safe_error(status, bytes)))
		return
	if bytes.size() < 44 or bytes.size() > MAX_WAV_BYTES:
		finished.emit(_fail("INVALID_TTS_AUDIO"))
		return
	var stream: AudioStreamWAV = AudioStreamWAV.load_from_buffer(bytes)
	if stream == null:
		finished.emit(_fail("INVALID_TTS_AUDIO"))
		return
	_player.stop()
	_player.stream = stream
	_player.play()
	finished.emit({
		"status": "ok", "kind": "technical_tts_test",
		"source": "sherpa-onnx-local", "audio_bytes": bytes.size(),
		"world_mutated": false, "npc_voice": false
	})

static func _safe_error(status: int, body: PackedByteArray) -> String:
	if body.size() > 512:
		return "TTS_UNAVAILABLE"
	var document := JSON.new()
	if document.parse(body.get_string_from_utf8()) != OK or not document.data is Dictionary:
		return "TTS_UNAVAILABLE"
	var allowed := [
		"NOT_FOUND", "LOCAL_ONLY", "LOCAL_AUTH_REQUIRED",
		"JSON_REQUIRED", "INVALID_BODY_LENGTH", "INVALID_JSON",
		"INVALID_TTS_TEST", "TTS_ENGINE_UNAVAILABLE", "TTS_GENERATION_FAILED"
	]
	var code: Variant = document.data.get("error_code", "")
	if status in [400, 403, 404, 413, 415, 503] and code is String and allowed.has(code):
		return code
	return "TTS_UNAVAILABLE"

static func _fail(code: String) -> Dictionary:
	return {
		"status": "unavailable", "error_code": code,
		"kind": "technical_tts_test", "world_mutated": false, "npc_voice": false
	}

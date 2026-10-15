extends RefCounted
## Contrato de integración de sherpa-onnx aún SIN backend.
## Cualquier consumidor debe tratar unavailable como falta real de voz.

const STATUS_UNAVAILABLE := "unavailable"
const BACKEND_NAME := "sherpa-onnx"
const API_VERSION := 1

static func capabilities() -> Dictionary:
	return {
		"backend": BACKEND_NAME,
		"version": API_VERSION,
		"asr_available": false,
		"tts_available": false,
		"reason": "No hay biblioteca sherpa-onnx enlazada ni modelos instalados."
	}

static func transcribe(_audio_samples: PackedByteArray, _language: String = "es-ES") -> Dictionary:
	return {
		"status": STATUS_UNAVAILABLE,
		"text": "",
		"error_code": "VOICE_BACKEND_NOT_INSTALLED"
	}

static func synthesize(_speaker_id: String, _text: String) -> Dictionary:
	return {
		"status": STATUS_UNAVAILABLE,
		"audio": PackedByteArray(),
		"error_code": "VOICE_BACKEND_NOT_INSTALLED"
	}

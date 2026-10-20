#!/usr/bin/env python3
"""NIM-05: TTS castellano de laboratorio local para Godot Windows.

Inferencia sherpa-onnx REAL, iniciada tras pulsar botón en Godot.
No llama a proveedores remotos, no se integra con NPC/WorldState,
no descarga modelo y nunca guarda frases o audio salvo --self-test CI.
"""
import argparse
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, HTTPServer
import io
import json
import os
from pathlib import Path
import sys
import wave

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "NIM03"))
from voice_tts_bench import verify_model  # noqa: E402

DEFAULT_TEXT = "Esta es una prueba técnica de voz local en Nimroel."
MAX_TEXT_CHARS = 160
MAX_BODY_BYTES = 1024
MAX_WAV_BYTES = 2_000_000


class LocalTTSEngine:
    def __init__(self, model_dir):
        # El import y el modelo existen solo en el PC que opta por la prueba.
        import sherpa_onnx

        files = verify_model(Path(model_dir))
        config = sherpa_onnx.OfflineTtsConfig(
            model=sherpa_onnx.OfflineTtsModelConfig(
                vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                    model=str(files["onnx"]),
                    data_dir=str(files["espeak"]),
                    tokens=str(files["tokens"]),
                ),
                num_threads=1,
            ),
        )
        if not config.validate():
            raise ValueError("Configuración sherpa-onnx inválida")
        self._tts = sherpa_onnx.OfflineTts(config)

    def speak(self, text):
        import numpy as np

        if not isinstance(text, str) or not 0 < len(text.strip()) <= MAX_TEXT_CHARS:
            raise ValueError("INVALID_TEXT")
        result = self._tts.generate(text=text.strip(), sid=0, speed=1.0)
        sample_rate = int(result.sample_rate)
        samples = np.asarray(result.samples)
        if (not 8000 <= sample_rate <= 48000 or samples.size < 100 or
                samples.ndim != 1 or samples.size > 750_000 or
                not np.all(np.isfinite(samples))):
            raise ValueError("INVALID_AUDIO")
        pcm = (np.clip(samples, -1.0, 1.0) * 32767).astype("<i2").tobytes()
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sample_rate)
            f.writeframes(pcm)
        wave_bytes = buffer.getvalue()
        if not 44 <= len(wave_bytes) <= MAX_WAV_BYTES:
            raise ValueError("INVALID_AUDIO")
        return wave_bytes


class TTSHandler(BaseHTTPRequestHandler):
    engine = None
    protocol_version = "HTTP/1.1"

    def log_message(self, *_args):
        # No registrar frases, headers ni datos de audio.
        pass

    def send_safe(self, status, payload):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != "/v1/tts-test":
            return self.send_safe(404, {"error_code": "NOT_FOUND"})
        if (self.headers.get("Origin") or
                self.headers.get("Host") not in {
                    "127.0.0.1:" + str(self.server.server_port),
                    "localhost:" + str(self.server.server_port),
                }):
            return self.send_safe(403, {"error_code": "LOCAL_ONLY"})
        token = os.environ.get("NIMROEL_LOCAL_TOKEN", "")
        if not token or not hmac.compare_digest(
                token, self.headers.get("X-Nimroel-Token", "")):
            return self.send_safe(403, {"error_code": "LOCAL_AUTH_REQUIRED"})
        if self.headers.get_content_type() != "application/json":
            return self.send_safe(415, {"error_code": "JSON_REQUIRED"})
        try:
            size = int(self.headers.get("Content-Length", "-1"))
        except ValueError:
            size = -1
        if not 0 < size <= MAX_BODY_BYTES:
            return self.send_safe(413, {"error_code": "INVALID_BODY_LENGTH"})
        try:
            data = json.loads(self.rfile.read(size))
        except (ValueError, UnicodeDecodeError):
            return self.send_safe(400, {"error_code": "INVALID_JSON"})
        if (not isinstance(data, dict) or set(data) != {"purpose", "text"} or
                data.get("purpose") != "technical_tts_test" or
                not isinstance(data.get("text"), str) or
                not 0 < len(data["text"].strip()) <= MAX_TEXT_CHARS):
            return self.send_safe(400, {"error_code": "INVALID_TTS_TEST"})
        if self.engine is None:
            return self.send_safe(503, {"error_code": "TTS_ENGINE_UNAVAILABLE"})
        try:
            wav_data = self.engine.speak(data["text"])
            if not isinstance(wav_data, bytes) or not 44 <= len(wav_data) <= MAX_WAV_BYTES:
                raise ValueError("INVALID_AUDIO")
        except Exception:
            return self.send_safe(503, {"error_code": "TTS_GENERATION_FAILED"})
        self.send_response(200)
        self.send_header("Content-Type", "audio/wav")
        self.send_header("Content-Length", str(len(wav_data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(wav_data)


def main():
    parser = argparse.ArgumentParser(description="NIM-05 TTS local Windows; sin NPC")
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--port", type=int, default=8767)
    parser.add_argument("--self-test", type=Path,
                        help="Solo CI: genera un WAV técnico dinámico sin abrir servidor")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("Puerto inválido")
    if sys.platform != "win32" and not args.self_test:
        parser.error("El laboratorio interactivo TTS solo está habilitado en Windows")
    if not args.self_test and not os.environ.get("NIMROEL_LOCAL_TOKEN"):
        parser.error("Falta NIMROEL_LOCAL_TOKEN")
    engine = LocalTTSEngine(args.model_dir)
    if args.self_test:
        wav_data = engine.speak(DEFAULT_TEXT)
        args.self_test.parent.mkdir(parents=True, exist_ok=True)
        args.self_test.write_bytes(wav_data)
        print("NIM-05 TTS CI: PCM WAV generado; bytes=" + str(len(wav_data)) +
              " sha256=" + hashlib.sha256(wav_data).hexdigest())
        return
    class Handler(TTSHandler):
        pass
    Handler.engine = engine
    server = HTTPServer(("127.0.0.1", args.port), Handler)
    print("NIM-05 TTS local en 127.0.0.1:" + str(args.port) + " (no NPC)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

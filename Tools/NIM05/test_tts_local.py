"""Pruebas offline del contrato local TTS, sin modelo ni dispositivos."""
import http.client
import io
import json
import os
import struct
import threading
import unittest
import wave
from unittest.mock import patch

import tts_local as p


def fake_wav():
    out = io.BytesIO()
    with wave.open(out, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(22050)
        wav.writeframes(struct.pack("<" + "h" * 128, *([0] * 128)))
    return out.getvalue()


class TTSOfflineHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = []
        class FakeEngine:
            def speak(self, text):
                cls.texts.append(text)
                return fake_wav()
        class Handler(p.TTSHandler):
            engine = FakeEngine()
        cls.server = p.HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def send(self, body, headers=None):
        request_body = json.dumps(body).encode() if isinstance(body, dict) else body
        conn = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        outgoing = {"Content-Type": "application/json",
                    "X-Nimroel-Token": "fake-local-token"}
        outgoing.update(headers or {})
        conn.request("POST", "/v1/tts-test", request_body, outgoing)
        response = conn.getresponse()
        code, ctype, data = response.status, response.getheader("Content-Type"), response.read()
        conn.close()
        return code, ctype, data

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "fake-local-token"})
    def test_dynamic_local_wav_without_remote_access(self):
        before = len(self.texts)
        code, ctype, raw = self.send({"purpose": "technical_tts_test",
                                      "text": "Frase local inventada distinta"})
        self.assertEqual((code, ctype), (200, "audio/wav"))
        self.assertEqual(raw[:4], b"RIFF")
        self.assertEqual(raw[8:12], b"WAVE")
        self.assertEqual(self.texts[before:], ["Frase local inventada distinta"])

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "fake-local-token"})
    def test_invalid_input_never_synthesizes(self):
        before = len(self.texts)
        for body in [
            {"purpose": "npc_voice", "text": "Hola"},
            {"purpose": "technical_tts_test", "text": ""},
            {"purpose": "technical_tts_test", "text": "x" * 161},
            {"purpose": "technical_tts_test", "text": "Hola", "speaker_id": "npc"},
        ]:
            with self.subTest(body=str(body)[:30]):
                code, _, raw = self.send(body)
                self.assertEqual(code, 400)
                self.assertEqual(json.loads(raw)["error_code"], "INVALID_TTS_TEST")
        self.assertEqual(len(self.texts), before)

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "fake-local-token"})
    def test_origin_and_token_rejected(self):
        before = len(self.texts)
        body = {"purpose": "technical_tts_test", "text": "Hola"}
        for headers in [{"Origin": "https://unknown.example"},
                        {"X-Nimroel-Token": "wrong"},
                        {"Host": "attacker.example"}]:
            with self.subTest(headers=headers):
                code, _, _ = self.send(body, headers=headers)
                self.assertEqual(code, 403)
        self.assertEqual(len(self.texts), before)

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": ""})
    def test_no_local_token_fails_closed(self):
        code, _, raw = self.send({"purpose": "technical_tts_test", "text": "Hola"})
        self.assertEqual(code, 403)
        self.assertEqual(json.loads(raw)["error_code"], "LOCAL_AUTH_REQUIRED")


if __name__ == "__main__":
    unittest.main()

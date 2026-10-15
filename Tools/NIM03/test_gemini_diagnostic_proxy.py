"""Pruebas offline: nunca consumen Gemini ni precisan clave real."""
import http.client
import json
import os
import threading
import unittest
from unittest.mock import patch

from gemini_diagnostic_proxy import Handler, ThreadingHTTPServer, UpstreamUnavailable


class ProxyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class FakeHandler(Handler):
            classifier = staticmethod(lambda _text: "dialogar")
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), FakeHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def send(self, path="/v1/intent-probe", body=None, headers=None, method="POST"):
        if body is None:
            body = {"purpose": "diagnostic_intent", "text": "Hablo con alguien"}
        if isinstance(body, dict):
            body = json.dumps(body).encode("utf-8")
        conn = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
        conn.request(method, path, body=body if method == "POST" else None,
                     headers=headers or {"Content-Type": "application/json"})
        response = conn.getresponse()
        status = response.status
        result = json.loads(response.read())
        conn.close()
        return status, result

    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-for-unit-test"})
    def test_structured_diagnostic_not_world(self):
        status, body = self.send()
        self.assertEqual(status, 200)
        self.assertEqual(body["intent"], "dialogar")
        self.assertEqual(body["kind"], "technical_diagnostic")
        self.assertFalse(body["world_mutated"])
        self.assertNotIn("reply", body)
        self.assertNotIn("speaker_id", body)

    def test_no_key_refuses_upstream(self):
        with patch.dict(os.environ, {"GEMINI_API_KEY": ""}):
            status, body = self.send()
        self.assertEqual(status, 503)
        self.assertEqual(body["error_code"], "GEMINI_KEY_NOT_CONFIGURED")

    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-for-unit-test"})
    def test_origin_rejected(self):
        code, body = self.send(headers={"Content-Type": "application/json",
                                        "Origin": "https://attack.example"})
        self.assertEqual((code, body["error_code"]), (403, "ORIGIN_FORBIDDEN"))

    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-for-unit-test"})
    def test_bad_data(self):
        for malformed in ({"purpose": "execute", "text": "Hola"},
                          {"purpose": "diagnostic_intent", "text": ""},
                          {"purpose": "diagnostic_intent", "text": "a" * 501}):
            with self.subTest(malformed=str(malformed)[:40]):
                code, _ = self.send(body=malformed)
                self.assertEqual(code, 400)
        code, _ = self.send(body=b"{not json")
        self.assertEqual(code, 400)
        code, _ = self.send(headers={"Content-Type": "text/plain"})
        self.assertEqual(code, 415)
        code, _ = self.send(path="/v1/execute")
        self.assertEqual(code, 404)

    def test_health_is_not_integration(self):
        code, body = self.send(path="/health", method="GET")
        self.assertEqual(code, 200)
        self.assertFalse(body["world_mutated"])
        self.assertNotIn("world_revision", body)

    @patch.dict(os.environ, {"GEMINI_API_KEY": "fake-for-unit-test"})
    def test_provider_failure_never_leaks_secrets(self):
        original = self.server.RequestHandlerClass.classifier
        self.server.RequestHandlerClass.classifier = staticmethod(
            lambda _text: (_ for _ in ()).throw(UpstreamUnavailable("secret-test-value")))
        try:
            code, body = self.send()
        finally:
            self.server.RequestHandlerClass.classifier = original
        self.assertEqual(code, 502)
        self.assertNotIn("secret-test-value", json.dumps(body))
        self.assertNotIn("fake-for-unit-test", json.dumps(body))


if __name__ == "__main__":
    unittest.main()

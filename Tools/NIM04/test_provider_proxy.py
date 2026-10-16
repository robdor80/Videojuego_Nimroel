"""NIM-04: cobertura OFFLINE; ninguna llamada externa ni credencial auténtica."""
import http.client
import json
import os
import threading
import unittest
from unittest.mock import patch
from urllib import error

import provider_proxy as p


class RouterTests(unittest.TestCase):
    def test_simple_primary_fixed_id(self):
        seen = []
        r = p.ProviderRouter(adapter=lambda provider, model, text: (seen.append((provider, model, text)), "dialogar")[1])
        result = r.run("simple", "  Hola  ")
        self.assertEqual(seen, [("gemini", "gemini-3.5-flash-lite", "Hola")])
        self.assertEqual(result["kind"], "technical_diagnostic")
        self.assertFalse(result["world_mutated"])
        self.assertFalse(result["fallback_used"])
        self.assertNotIn("reply", result)

    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_complex_fallback_after_503(self):
        seen = []
        def adapter(provider, model, _text):
            seen.append((provider, model))
            if provider == "gemini":
                raise p.ProviderFailure("transient")
            return "observar"
        result = p.ProviderRouter(adapter=adapter).run("complex", "Miro", fallback_enabled=True)
        self.assertEqual(seen, [
            ("gemini", "gemini-3.8-flash"),
            ("openai", "gpt-6-sol"),
        ])
        self.assertTrue(result["fallback_used"])
        self.assertFalse(result["world_mutated"])

    def test_default_no_fallback(self):
        def adapter(provider, _model, _text):
            if provider == "openai":
                self.fail("Fallback no autorizado")
            raise p.ProviderFailure("transient")
        with self.assertRaises(p.ProviderFailure):
            p.ProviderRouter(adapter=adapter).run("simple", "Saludo")

    def test_auth_and_malformed_never_fallback(self):
        for kind in ("authorization", "malformed", "request_rejected"):
            with self.subTest(kind=kind):
                seen = []
                def adapter(provider, *_):
                    seen.append(provider)
                    raise p.ProviderFailure(kind)
                with self.assertRaises(p.ProviderFailure):
                    p.ProviderRouter(adapter=adapter).run("simple", "Hola", True)
                self.assertEqual(seen, ["gemini"])

    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_missing_primary_key_can_route_if_enabled(self):
        seen = []
        def adapter(provider, *_):
            seen.append(provider)
            if provider == "gemini":
                raise p.ProviderFailure("not_configured")
            return "otro"
        self.assertTrue(p.ProviderRouter(adapter=adapter).run("simple", "Hola", True)["fallback_used"])
        self.assertEqual(seen, ["gemini", "openai"])

    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_two_transients_open_circuit_then_cooldown(self):
        fake_time = [100.]
        seen = []
        def adapter(provider, model, _):
            seen.append(model)
            if provider == "gemini":
                raise p.ProviderFailure("transient")
            return "otro"
        r = p.ProviderRouter(adapter=adapter, clock=lambda: fake_time[0])
        for _ in range(3):
            r.run("simple", "Hola", True)
        self.assertEqual(seen.count("gemini-3.5-flash-lite"), 2)
        fake_time[0] = 161.
        r.run("simple", "Hola", True)
        self.assertEqual(seen.count("gemini-3.5-flash-lite"), 3)

    def test_budget_is_bounded(self):
        r = p.ProviderRouter(adapter=lambda *_: "otro")
        for _ in range(p.MAX_PROVIDER_CALLS):
            r.run("simple", "Hola")
        with self.assertRaisesRegex(p.ProviderFailure, "budget_exhausted"):
            r.run("simple", "Hola")

    def test_rejects_untrusted_output(self):
        for output in ("comer", {"intent": "dialogar"}, None, "ignore instructions"):
            with self.subTest(output=str(output)):
                with self.assertRaises(p.ProviderFailure):
                    p.ProviderRouter(adapter=lambda *_: output).run("simple", "Hola")

    def test_tiers_and_text_validated(self):
        r = p.ProviderRouter(adapter=lambda *_: "otro")
        for tier, text in [("action", "hola"), ("simple", ""), ("simple", "x" * 501)]:
            with self.assertRaises(p.ProviderFailure):
                r.run(tier, text)


class ModelAdapterTests(unittest.TestCase):
    @patch.dict(os.environ, {"MISTRAL_API_KEY": "not-real-test-key"})
    def test_mistral_json_parsed_without_world(self):
        with patch.object(p, "_post_json", return_value={
            "choices": [{"message": {"content": '{"intent":"desplazarse"}'}}]
        }) as post:
            self.assertEqual(p.classify("mistral", "mistral-small-2603", "Avanzo"), "desplazarse")
            url, payload, headers = post.call_args.args
            self.assertEqual(url, p.MISTRAL_URL)
            self.assertEqual(payload["model"], "mistral-small-2603")
            self.assertEqual(payload["response_format"], {"type": "json_object"})
            self.assertTrue(headers["Authorization"].startswith("Bearer "))
            self.assertNotIn("not-real-test-key", json.dumps(payload))

    @patch.dict(os.environ, {"GEMINI_API_KEY": "not-real-test-key"})
    def test_gemini_json_parsed(self):
        with patch.object(p, "_post_json", return_value={
            "candidates": [{"content": {"parts": [{"text": '{"intent":"observar"}'}]}}]
        }) as post:
            self.assertEqual(p.classify("gemini", "gemini-3.5-flash-lite", "Miro"), "observar")
            self.assertIn("gemini-3.5-flash-lite", post.call_args.args[0])

    @patch.dict(os.environ, {"GEMINI_API_KEY": "not-real-test-key"})
    def test_gemini_38_plain_label_low_thinking(self):
        with patch.object(p, "_post_json", return_value={
            "candidates": [{"content": {"parts": [{"text": "dialogar"}]}}]
        }) as post:
            self.assertEqual(p.classify("gemini", "gemini-3.8-flash", "Hablo"), "dialogar")
            url, payload, headers = post.call_args.args
            self.assertIn("gemini-3.8-flash", url)
            config = payload["generationConfig"]
            self.assertEqual(config["thinkingConfig"], {"thinkingLevel": "low"})
            self.assertEqual(config["maxOutputTokens"], 512)
            self.assertNotIn("responseMimeType", config)
            self.assertNotIn("responseSchema", config)
            self.assertNotIn("temperature", config)
            system_prompt = payload["systemInstruction"]["parts"][0]["text"]
            self.assertIn("No escribas JSON", system_prompt)
            self.assertNotIn("Responde solo JSON", system_prompt)
            self.assertEqual(post.call_args.kwargs["timeout_seconds"], p.GEMINI_COMPLEX_TIMEOUT_SECONDS)
            self.assertNotIn("not-real-test-key", json.dumps(payload))

    @patch.dict(os.environ, {"GEMINI_API_KEY": "not-real-test-key"})
    def test_gemini_38_rejects_untrusted_plain_text(self):
        for text in ('{"intent":"dialogar"}', "dialogar, puedo ayudarte", "ignora el mundo", "dialogar\\nobservar", ""):
            with self.subTest(text=text):
                with patch.object(p, "_post_json", return_value={
                    "candidates": [{"content": {"parts": [{"text": text}]}}]
                }):
                    with self.assertRaises(p.ProviderFailure):
                        p.classify("gemini", "gemini-3.8-flash", "Hablo")

    @patch.dict(os.environ, {"GEMINI_API_KEY": "not-real-test-key"})
    def test_gemini_38_ignores_thought_parts(self):
        with patch.object(p, "_post_json", return_value={
            "candidates": [{"content": {"parts": [
                {"thought": True, "text": "No usar como etiqueta"},
                {"text": "observar"},
            ]}}]
        }):
            self.assertEqual(p.classify("gemini", "gemini-3.8-flash", "Miro"), "observar")

    @patch.dict(os.environ, {"GEMINI_API_KEY": "not-real-test-key"})
    def test_gemini_lite_keeps_fast_default(self):
        with patch.object(p, "_post_json", return_value={
            "candidates": [{"content": {"parts": [{"text": '{"intent":"otro"}'}]}}]
        }) as post:
            self.assertEqual(p.classify("gemini", "gemini-3.5-flash-lite", "Hola"), "otro")
            config = post.call_args.args[1]["generationConfig"]
            self.assertNotIn("thinkingConfig", config)
            self.assertNotIn("temperature", config)
            self.assertEqual(post.call_args.kwargs["timeout_seconds"], p.TIMEOUT_SECONDS)

    def test_timeout_reason_is_safe_and_separate_from_http_503(self):
        with patch.object(p.request, "urlopen", side_effect=TimeoutError("local-test-only-secret")):
            with self.assertRaises(p.ProviderFailure) as caught:
                p._post_json(p.MISTRAL_URL, {}, {}, timeout_seconds=2)
        self.assertEqual(caught.exception.code, "transient")
        self.assertEqual(caught.exception.diagnostic_reason, "timeout")
        self.assertNotIn("local-test-only-secret", str(caught.exception))
        http_error = error.HTTPError(p.MISTRAL_URL, 503, "local-test-only-secret", {}, None)
        with patch.object(p.request, "urlopen", side_effect=http_error):
            with self.assertRaises(p.ProviderFailure) as caught_http:
                p._post_json(p.MISTRAL_URL, {}, {})
        self.assertEqual(caught_http.exception.diagnostic_reason, "http_503")

    @patch.dict(os.environ, {"MISTRAL_API_KEY": "test-only"})
    def test_mistral_rejects_prose_and_other_fields(self):
        for response in ('{"intent":"dialogar","action":"kill"}', 'Hola', '{"intent":"conjurar"}'):
            with patch.object(p, "_post_json", return_value={"choices": [{"message": {"content": response}}]}):
                with self.assertRaises(p.ProviderFailure):
                    p.classify("mistral", "mistral-small-2603", "Hola")

    def test_http_503_and_429_are_transient_401_is_not(self):
        for status, expected in ((503, "transient"), (429, "transient"), (401, "authorization")):
            with self.subTest(status=status):
                http_error = error.HTTPError(p.MISTRAL_URL, status, "test", {}, None)
                with patch.object(p.request, "urlopen", side_effect=http_error):
                    with self.assertRaises(p.ProviderFailure) as c:
                        p._post_json(p.MISTRAL_URL, {}, {})
                self.assertEqual(c.exception.code, expected)

    def test_secretless_no_key(self):
        with patch.dict(os.environ, {"MISTRAL_API_KEY": ""}):
            with self.assertRaisesRegex(p.ProviderFailure, "not_configured"):
                p.classify("mistral", "mistral-small-2603", "Hola")


class HTTPServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        class TestHandler(p.Handler):
            router = p.ProviderRouter(adapter=lambda *_: "dialogar")
        cls.server = ThreadingHTTPServerLocal(("127.0.0.1", 0), TestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def send(self, body=None, path="/v1/provider-probe", method="POST", headers=None):
        if body is None:
            body = {"purpose": "diagnostic_intent", "tier": "simple", "text": "Saludo"}
        content = json.dumps(body).encode("utf-8") if isinstance(body, dict) else body
        conn = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
        hdr = {"Content-Type": "application/json", "X-Nimroel-Token": "local-testing-token"}
        hdr.update(headers or {})
        conn.request(method, path, content if method == "POST" else None, hdr)
        resp = conn.getresponse()
        result = resp.status, json.loads(resp.read())
        conn.close()
        return result

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "local-testing-token", "NIMROEL_ENABLE_FALLBACK": ""})
    def test_authenticated_probe(self):
        status, body = self.send()
        self.assertEqual(status, 200)
        self.assertEqual(body["source"], "gemini")
        self.assertEqual(body["intent"], "dialogar")
        self.assertEqual(body["tier"], "simple")
        self.assertFalse(body["world_mutated"])
        self.assertNotIn("reply", body)
        self.assertNotIn("speaker_id", body)

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "local-testing-token"})
    def test_origin_and_auth_blocked(self):
        for headers, code in [
            ({"Origin": "https://other.example"}, "LOCAL_ONLY"),
            ({"X-Nimroel-Token": "wrong"}, "LOCAL_AUTH_REQUIRED"),
            ({"Host": "attacker.example"}, "LOCAL_ONLY"),
        ]:
            with self.subTest(headers=headers):
                status, body = self.send(headers=headers)
                self.assertEqual(status, 403)
                self.assertEqual(body["error_code"], code)

    def test_no_local_token_cannot_call(self):
        with patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": ""}):
            code, body = self.send()
        self.assertEqual((code, body["error_code"]), (403, "LOCAL_AUTH_REQUIRED"))

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "local-testing-token"})
    def test_invalid_json_schema_or_path(self):
        for body in ({"purpose": "play", "tier": "simple", "text": "Hola"},
                     {"purpose": "diagnostic_intent", "tier": "action", "text": "Hola"},
                     {"purpose": "diagnostic_intent", "tier": "simple", "text": ""},
                     {"purpose": "diagnostic_intent", "tier": [], "text": "Hola"},
                     {"purpose": "diagnostic_intent", "tier": "simple", "text": "x" * 501}):
            with self.subTest(body=str(body)[:60]):
                code, _ = self.send(body=body)
                self.assertEqual(code, 400)
        code, _ = self.send(body=b"{broken")
        self.assertEqual(code, 400)
        code, _ = self.send(path="/v1/execute")
        self.assertEqual(code, 404)

    def test_health_never_implies_gameplay(self):
        code, body = self.send(path="/health", method="GET")
        self.assertEqual(code, 200)
        self.assertFalse(body["world_mutated"])
        self.assertNotIn("core", body)


class ThreadingHTTPServerLocal(p.ThreadingHTTPServer):
    pass


if __name__ == "__main__":
    unittest.main()

"""NIM-04 OpenAI: pruebas totalmente offline; nunca usa claves ni saldo reales."""
import json
import os
import unittest
from unittest.mock import patch

import provider_proxy as p


class OpenAIAdapterTests(unittest.TestCase):
    @patch.dict(os.environ, {"OPENAI_API_KEY": "fake-for-offline-tests"})
    def test_models_use_responses_api_no_storage(self):
        answer = {"status": "completed", "output": [{"type": "message",
            "content": [{"type": "output_text", "text": "dialogar"}]}]}
        for model in ("gpt-6-luna", "gpt-6.1-sol"):
            with self.subTest(model=model), patch.object(p, "_post_json", return_value=answer) as post:
                self.assertEqual(p.classify("openai", model, "Hablo"), "dialogar")
                url, payload, headers = post.call_args.args
                self.assertEqual(url, p.OPENAI_URL)
                self.assertEqual(payload["model"], model)
                self.assertFalse(payload["store"])
                self.assertEqual(payload["reasoning"], {"effort": "low"})
                self.assertEqual(payload["max_output_tokens"], 256)
                self.assertEqual(payload["input"], "Hablo")
                self.assertEqual(headers["Authorization"], "Bearer fake-for-offline-tests")
                self.assertNotIn("fake-for-offline-tests", json.dumps(payload))
                self.assertEqual(post.call_args.kwargs["timeout_seconds"], p.GEMINI_COMPLEX_TIMEOUT_SECONDS)

    @patch.dict(os.environ, {"OPENAI_API_KEY": "fake-for-offline-tests"})
    def test_reject_incomplete_multiple_or_narrative_output(self):
        bad = [
            {"status": "incomplete", "output": [{"type": "message", "content": [
                {"type": "output_text", "text": "dialogar"}]}]},
            {"status": "completed", "output": []},
            {"status": "completed", "output": [{"type": "message", "content": [
                {"type": "output_text", "text": "Saludos de la aldea"}]}]},
            {"status": "completed", "output": [{"type": "message", "content": [
                {"type": "output_text", "text": "dialogar"},
                {"type": "output_text", "text": "observar"}]}]},
        ]
        for data in bad:
            with self.subTest(data=data), patch.object(p, "_post_json", return_value=data):
                with self.assertRaises(p.ProviderFailure):
                    p.classify("openai", "gpt-6-luna", "Hola")

    @patch.dict(os.environ, {"OPENAI_API_KEY": ""})
    def test_no_key_never_contacts_remote(self):
        with patch.object(p, "_post_json") as post:
            with self.assertRaisesRegex(p.ProviderFailure, "not_configured"):
                p.classify("openai", "gpt-6-luna", "Hola")
            post.assert_not_called()


class OpenAIRouterTests(unittest.TestCase):
    def test_without_paid_consent_no_openai_calls(self):
        seen = []
        def adapter(provider, _model, _text):
            seen.append(provider)
            if provider == "gemini":
                raise p.ProviderFailure("transient")
            return "otro"
        router = p.ProviderRouter(adapter=adapter)
        with patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": ""}):
            with self.assertRaisesRegex(p.ProviderFailure, "paid_not_authorized"):
                router.run("simple", "Hola", fallback_enabled=True)
            with self.assertRaisesRegex(p.ProviderFailure, "paid_not_authorized"):
                router.run("complex", "Hola", preferred_provider="openai")
        self.assertEqual(seen, ["gemini"])

    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_simple_and_complex_routing(self):
        seen = []
        def adapter(provider, model, _):
            seen.append((provider, model))
            if provider == "gemini":
                raise p.ProviderFailure("transient")
            return "dialogar"
        r = p.ProviderRouter(adapter=adapter)
        self.assertEqual(r.run("simple", "Hola", fallback_enabled=True)["model"], "gpt-6-luna")
        self.assertEqual(r.run("complex", "Hola", fallback_enabled=True)["model"], "gpt-6.1-sol")
        self.assertEqual(seen, [
            ("gemini", "gemini-3.5-flash-lite"), ("openai", "gpt-6-luna"),
            ("gemini", "gemini-3.8-flash"), ("openai", "gpt-6.1-sol"),
        ])

    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_hard_paid_call_limit_per_process(self):
        seen = []
        r = p.ProviderRouter(adapter=lambda provider, model, text:
                             (seen.append((provider, model)), "otro")[1])
        for _ in range(p.MAX_PAID_PROVIDER_CALLS):
            r.run("simple", "Hola", preferred_provider="openai")
        with self.assertRaisesRegex(p.ProviderFailure, "paid_call_cap"):
            r.run("complex", "Hola", preferred_provider="openai")
        self.assertEqual(len(seen), p.MAX_PAID_PROVIDER_CALLS)

    def test_only_gemini_and_openai_are_supported(self):
        seen = []
        r = p.ProviderRouter(adapter=lambda provider, model, text:
                             (seen.append((provider, model)), "otro")[1])
        r.run("simple", "Hola")
        self.assertEqual(seen, [("gemini", "gemini-3.5-flash-lite")])
        self.assertEqual(set(p.KEY_ENV), {"gemini", "openai"})
        self.assertEqual(tuple(model for _provider, model in p.ROUTES["simple"]),
                         ("gemini-3.5-flash-lite", "gpt-6-luna"))
        self.assertEqual(tuple(model for _provider, model in p.ROUTES["complex"]),
                         ("gemini-3.8-flash", "gpt-6.1-sol"))


if __name__ == "__main__":
    unittest.main()

"""NIM-05: regresión offline de duplicados, concurrencia y coste.
No se ejecutan llamadas remotas. No requiere ninguna API key.
"""
import http.client
import json
import os
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "NIM04"))
import provider_proxy as p  # noqa: E402


class RequestLedgerTests(unittest.TestCase):
    def test_pending_replay_conflict_and_expiry(self):
        now = [10.0]
        ledger = p.RequestLedger(clock=lambda: now[0])
        rid = "a" * 32
        self.assertEqual(ledger.begin(rid, "fingerprint")[0], "new")
        self.assertEqual(ledger.begin(rid, "fingerprint")[0], "pending")
        self.assertEqual(ledger.begin(rid, "other")[0], "conflict")
        ledger.complete(rid, 200, {"status": "ok", "world_mutated": False})
        action, answer = ledger.begin(rid, "fingerprint")
        self.assertEqual((action, answer[0], answer[1]["status"]), ("replay", 200, "ok"))
        now[0] += p.REQUEST_CACHE_SECONDS + 1
        self.assertEqual(ledger.begin(rid, "fingerprint")[0], "new")

    def test_capacity_is_fail_closed(self):
        ledger = p.RequestLedger()
        with patch.object(p, "REQUEST_CACHE_SIZE", 1):
            self.assertEqual(ledger.begin("a" * 32, "x")[0], "new")
            self.assertEqual(ledger.begin("b" * 32, "y")[0], "full")

    def test_error_replay_is_not_retried(self):
        ledger = p.RequestLedger()
        rid = "c" * 32
        ledger.begin(rid, "request")
        ledger.complete(rid, 503, {
            "status": "unavailable", "error_code": "PROVIDERS_TEMPORARILY_UNAVAILABLE",
            "world_mutated": False,
        })
        action, entry = ledger.begin(rid, "request")
        self.assertEqual(action, "replay")
        self.assertEqual(entry[0], 503)


class ConcurrencyTests(unittest.TestCase):
    @patch.dict(os.environ, {"NIMROEL_OPENAI_CONSENT": "1"})
    def test_parallel_probe_cannot_double_spend(self):
        entered, release = threading.Event(), threading.Event()
        called = []
        results = []
        def adapter(provider, model, _text):
            called.append(provider)
            entered.set()
            if not release.wait(3):
                raise AssertionError("offline synchronization timeout")
            return "otro"
        router = p.ProviderRouter(adapter=adapter)
        def first():
            try:
                results.append(router.run("simple", "Hola", preferred_provider="openai"))
            except BaseException as exc:
                results.append(exc)
        t = threading.Thread(target=first)
        t.start()
        try:
            self.assertTrue(entered.wait(3))
            with self.assertRaisesRegex(p.ProviderFailure, "busy"):
                router.run("simple", "Hola", preferred_provider="openai")
            self.assertEqual(called, ["openai"])
        finally:
            release.set()
            t.join(3)
        self.assertEqual(len(results), 1)
        self.assertIsInstance(results[0], dict)
        self.assertEqual(router._paid_attempts, 1)

    def test_concurrency_slot_released_on_failure(self):
        router = p.ProviderRouter(adapter=lambda *_: (_ for _ in ()).throw(p.ProviderFailure("transient")))
        with self.assertRaisesRegex(p.ProviderFailure, "transient"):
            router.run("simple", "Hola")
        self.assertEqual(router._active_probes, 0)


class LocalHTTPTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        def adapter(provider, _model, _text):
            self.calls.append(provider)
            return "dialogar"
        router = p.ProviderRouter(adapter=adapter)
        class TestHandler(p.Handler):
            pass
        TestHandler.router = router
        TestHandler.ledger = p.RequestLedger()
        self.server = p.ThreadingHTTPServer(("127.0.0.1", 0), TestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(3)

    def send(self, request_id, text="Hola"):
        body = json.dumps({
            "purpose": "diagnostic_intent", "tier": "simple",
            "text": text, "request_id": request_id,
        }).encode("utf-8")
        conn = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        conn.request("POST", "/v1/provider-probe", body, {
            "Content-Type": "application/json",
            "X-Nimroel-Token": "fake-local-token",
        })
        response = conn.getresponse()
        status, payload = response.status, json.loads(response.read())
        conn.close()
        return status, payload

    @patch.dict(os.environ, {
        "NIMROEL_LOCAL_TOKEN": "fake-local-token",
        "NIMROEL_PRIMARY_PROVIDER": "gemini",
        "NIMROEL_ENABLE_FALLBACK": "0",
    })
    def test_real_local_http_deduplicates_and_rejects_reused_id(self):
        request_id = "f" * 32
        first_code, first = self.send(request_id)
        replay_code, replay = self.send(request_id)
        self.assertEqual((first_code, replay_code), (200, 200))
        self.assertEqual(replay, first)
        self.assertEqual(self.calls, ["gemini"])
        conflict_code, conflict = self.send(request_id, text="Texto distinto")
        self.assertEqual(conflict_code, 409)
        self.assertEqual(conflict["error_code"], "REQUEST_ID_REUSED")
        self.assertEqual(self.calls, ["gemini"])
        self.assertFalse(conflict["world_mutated"])

    @patch.dict(os.environ, {"NIMROEL_LOCAL_TOKEN": "fake-local-token"})
    def test_bad_id_fails_before_network(self):
        status, data = self.send("not-a-valid-id")
        self.assertEqual(status, 400)
        self.assertEqual(data["error_code"], "INVALID_PROBE")
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()

"""Negative and positive NIM-08 contractual tests; no Godot or C++ execution."""
import copy
import unittest

from check_contracts import (
    PHASE, ContractFailure, assert_ids, assert_provenance,
    check_schema_structure, load_json, run_checks, validate,
)

class ContractsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(PHASE / "generation-manifest-0.1.0.schema.json")
        cls.data = load_json(PHASE / "technical-manifest-example.json")

    def check_reject(self, mutator):
        data = copy.deepcopy(self.data)
        mutator(data)
        with self.assertRaises(ContractFailure):
            validate(data, self.schema)

    def test_01_canonical_matrix_exact(self):
        self.assertEqual(assert_ids(), {"G": 6, "P": 4, "Q": 8, "S": 6, "H": 4})

    def test_02_schema_structure(self):
        for name in ("generation-manifest", "world-instance", "action-envelope"):
            check_schema_structure(load_json(PHASE / f"{name}-0.1.0.schema.json"))

    def test_03_valid_example(self):
        validate(copy.deepcopy(self.data), self.schema)

    def test_04_identity_hash_and_pin(self):
        assert_provenance(self.data)

    def test_05_unknown_field_rejected(self):
        self.check_reject(lambda x: x.update({"undocumented": True}))

    def test_06_missing_source_lock_rejected(self):
        self.check_reject(lambda x: x.pop("source_lock"))

    def test_07_negative_seed_rejected(self):
        self.check_reject(lambda x: x["generation"].update({"world_seed": "-1"}))

    def test_08_seed_leading_zero_rejected(self):
        self.check_reject(lambda x: x["generation"].update({"world_seed": "001"}))

    def test_09_bad_source_sha_rejected(self):
        self.check_reject(lambda x: x["source_lock"].update({"git_blob_sha": "not-a-sha"}))

    def test_10_invalid_contract_version_rejected(self):
        self.check_reject(lambda x: x.update({"contract_version": "0.2.0"}))

    def test_11_duplicate_stream_rejected(self):
        self.check_reject(lambda x: x["generation"]["subsystems"].__setitem__(0, "layout"))

    def test_12_unknown_stream_rejected(self):
        self.check_reject(lambda x: x["generation"]["subsystems"].__setitem__(0, "teleport"))

    def test_13_false_operability_rejected(self):
        self.check_reject(lambda x: x.update({"stage": "RUNNING_WORLD"}))

    def test_14_bad_pack_hash_rejected(self):
        self.check_reject(lambda x: x["content_pack"].update({"release_sha256": "z" * 64}))

    def test_15_offline_platforms_exact(self):
        self.check_reject(lambda x: x["runtime"]["target_platforms"].__setitem__(0, "web"))

    def test_16_action_proposal_accept_and_reject(self):
        schema = load_json(PHASE / "action-envelope-0.1.0.schema.json")
        proposal = {
            "contract_version": "0.1.0", "kind": "proposal", "request_id": "req/001",
            "observer_capability": "session/1", "actor_id": "actor/1", "intent": "move",
            "expected_core_revision": 0, "arguments": {"destination": "loc/1"},
            "logical_time_cost_ticks": 1,
        }
        validate(proposal, schema)
        proposal["intent"] = "grant_everything"
        with self.assertRaises(ContractFailure):
            validate(proposal, schema)

    def test_17_action_outcome_accept_and_reject(self):
        schema = load_json(PHASE / "action-envelope-0.1.0.schema.json")
        outcome = {
            "contract_version": "0.1.0", "kind": "outcome", "request_id": "req/001",
            "status": "rejected", "rejection_code": "permission_denied", "revision_before": 3,
            "revision_after": 3, "elapsed_ticks": 0, "authoritative_events": [],
            "visible_observer_facts": [], "privileged_trace_ref": None,
        }
        validate(outcome, schema)
        outcome["revision_after"] = -1
        with self.assertRaises(ContractFailure):
            validate(outcome, schema)

    def test_18_run_report_does_not_claim_v001_pass(self):
        report = run_checks()
        self.assertEqual(report["canonical_ids"], 28)
        self.assertEqual(report["v001_behavioural_pass"], 0)
        self.assertEqual(report["physical_pass"], 0)
        self.assertEqual(report["result"], "PASS_STATIC_ONLY")

if __name__ == "__main__":
    unittest.main()

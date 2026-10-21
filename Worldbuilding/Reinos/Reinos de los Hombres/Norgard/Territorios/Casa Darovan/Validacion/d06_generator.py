#!/usr/bin/env python3
"""D06: pure seed-based DESIGN laboratory. Not a CoreRPG or Godot generator."""
from __future__ import annotations

import hashlib
import json
from typing import Any


class IneligibleSite(ValueError):
    """A proposal is not proved eligible by locally verified evidence."""


def digest(*parts: str) -> bytes:
    payload = json.dumps(parts, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).digest()


def stable_id(seed: str, zone: str, slot: str) -> str:
    if not all(isinstance(x, str) and x.strip() for x in (seed, zone, slot)):
        raise IneligibleSite("seed, zone and slot must be nonempty")
    return "d06_test_" + digest("darovan-d06/v0.1", seed, zone, slot).hex()[:16]


def weighted_choice(seed: str, stable: str, version: str, eligible: list[tuple[str, int]]) -> str:
    pairs = sorted(eligible)
    total = sum(w for _, w in pairs)
    if not pairs or total <= 0:
        raise IneligibleSite("no eligible model")
    number = int.from_bytes(digest(seed, stable, "model", version)[:8], "big") % total
    for key, weight in pairs:
        if number < weight:
            return key
        number -= weight
    raise AssertionError("unreachable deterministic roll")


def generate_test_design(rules: dict[str, Any], proposal: dict[str, Any], seed: str) -> dict[str, Any]:
    """Returns an inert synthetic sample; never creates geography or world-state objects."""
    if proposal.get("fixtureKind") != "synthetic_test_only" or proposal.get("canonical") is not False:
        raise IneligibleSite("laboratory proposals only")
    if proposal.get("visibleName") is not None or proposal.get("coordinates") is not None:
        raise IneligibleSite("new names and coordinates forbidden")
    allowed = {"id", "studyZoneId", "slotId", "settlementClass", "evidence",
               "allowedModel", "fixtureKind", "flags", "visibleName",
               "coordinates", "canonical"}
    if set(proposal) - (allowed | set(rules["proposalForbiddenFlags"])):
        raise IneligibleSite("unknown fixture fields cannot assert facts")
    if proposal.get("flags") or proposal.get("claimedCity") or any(
            proposal.get(flag) for flag in rules["proposalForbiddenFlags"]):
        raise IneligibleSite("unapproved world claim")
    zone = proposal.get("studyZoneId")
    slot = proposal.get("slotId")
    klass = proposal.get("settlementClass")
    regions = {z["id"]: z for z in rules["zones"]}
    if zone not in regions or klass not in ("aldea", "pueblo", "villa", "enclave"):
        raise IneligibleSite("unknown study unit or settlement class")
    if zone == "d01_aguja_litoral":
        raise IneligibleSite("Agujas: no permanent settlement (unmapped zone conservative)")
    evidence = proposal.get("evidence")
    if not isinstance(evidence, list) or len(evidence) != len(set(evidence)):
        raise IneligibleSite("invalid site evidence")
    proof = set(evidence)
    if klass == "enclave" and rules["enclavePromotionRequires"] not in proof:
        raise IneligibleSite("worksite is not a settlement without residents")
    if not set(rules["globalRequiredEvidence"]).issubset(proof):
        raise IneligibleSite("missing mandatory site proof")
    stable = stable_id(seed, zone, slot)
    candidates = []
    models = {m["id"]: m for m in rules["models"]}
    for model_id, weight in regions[zone]["modelWeights"].items():
        model = models[model_id]
        if weight > 0 and klass in model["classes"] and set(model["requiredEvidence"]).issubset(proof):
            candidates.append((model_id, weight))
    if not candidates:
        raise IneligibleSite("no eligible economic/site model")
    chosen = weighted_choice(seed, stable, rules["version"], candidates)
    if proposal.get("allowedModel") is not None:
        if proposal["allowedModel"] not in {key for key, _ in candidates}:
            raise IneligibleSite("unproven requested model")
        chosen = proposal["allowedModel"]  # explicit laboratory selector, never canon
    return {
        "id": stable, "studyZoneId": zone, "slotId": slot,
        "settlementClass": klass, "modelId": chosen,
        "designSeed": seed, "generatorVersion": rules["generatorVersion"],
        "rulesVersion": rules["version"], "provenance": "TEST_ONLY",
        "canonical": False, "materialized": False, "visibleName": None,
        "coordinates": None, "population": None, "connectedRoutes": [],
        "serviceInstances": [], "buildingInstances": [], "worldStateId": None,
        "potentialBuildings": models[chosen]["buildingPossibilities"],
        "potentialServices": models[chosen]["servicePossibilities"],
    }

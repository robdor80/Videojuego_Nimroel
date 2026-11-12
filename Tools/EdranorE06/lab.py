"""Edranor E06: seleccion pura y determinista de candidatos SINTETICOS; no crea mundo real."""
from __future__ import annotations
import hashlib
import json

PROTECTED = {"dorth", "lumina", "karsath", "rodas", "hallheim"}
CLASSES = {"aldea", "pueblo", "villa", "enclave"}

def digest(values: list[str]) -> bytes:
    payload = json.dumps(values, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).digest()

def evaluate(rules: dict, case: dict) -> dict:
    """UNKNOWN o ausencia de prueba es NO. Solo acepta entradas TEST_ONLY."""
    reasons: set[str] = set()
    if rules.get("runtimeEnabled") is not False or rules.get("scope", {}).get("syntheticLabOnly") is not True:
        reasons.add("RUNTIME_GUARD")
    if case.get("fixtureKind") != "SYNTHETIC_TEST_ONLY":
        reasons.add("REAL_INPUT_FORBIDDEN")
    if case.get("siteRef") in PROTECTED:
        reasons.add("PROTECTED_ANCHOR")
    elif case.get("siteRef") is not None:
        reasons.add("REAL_SITE_FORBIDDEN")
    if case.get("jurisdictionOwner") != "casa_edranor":
        reasons.add("WRONG_JURISDICTION")
    if case.get("coordinates") is not None or case.get("visibleName") is not None or case.get("population") is not None:
        reasons.add("REAL_OUTPUT_FORBIDDEN")
    if case.get("siteFlags"):
        reasons.add("EXCLUSION_FLAG")
    if not isinstance(case.get("worldSeed"), str) or not case.get("worldSeed"):
        reasons.add("INVALID_SEED")
    if not isinstance(case.get("slotId"), str) or not case.get("slotId", "").startswith("sandbox_"):
        reasons.add("INVALID_SLOT")
    if case.get("settlementClass") not in CLASSES:
        reasons.add("INVALID_CLASS")
    zones = {z["id"]: z for z in rules["zones"]}
    zone = zones.get(case.get("studyZoneId"))
    if zone is None:
        reasons.add("UNKNOWN_ZONE")
    elif zone["id"] in rules["blockedZones"] or zone["eligibility"].startswith("CLOSED_"):
        reasons.add("BLOCKED_ZONE")
    evidence = case.get("evidence")
    if not isinstance(evidence, list) or any(not isinstance(x, str) for x in evidence):
        reasons.add("INVALID_EVIDENCE")
        evidence_set = set()
    else:
        evidence_set = set(evidence)
        if len(evidence_set) != len(evidence):
            reasons.add("DUPLICATE_EVIDENCE")
    if not set(rules["foundationEvidence"]).issubset(evidence_set):
        reasons.add("MISSING_FOUNDATION")
    needed = rules["classEvidence"].get(case.get("settlementClass"), [])
    if not set(needed).issubset(evidence_set):
        reasons.add("MISSING_CLASS_EVIDENCE")
    available = []
    if zone is not None:
        for model in sorted(rules["models"], key=lambda m: m["id"]):
            weight = zone["weights"].get(model["id"], 0)
            if weight > 0 and case.get("settlementClass") in model["classes"] and set(model["extraEvidence"]).issubset(evidence_set):
                available.append((model, weight))
    if not available:
        reasons.add("NO_ELIGIBLE_MODEL")
    if reasons:
        return {"status": "REJECTED", "reasonCodes": sorted(reasons), "stableId": None, "materialized": False}
    seed = case["worldSeed"]
    zone_id = zone["id"]
    stable_id = rules["seedContract"]["idPrefix"] + digest(
        [rules["seedContract"]["namespace"], seed, zone_id, case["slotId"]]
    ).hex()[:rules["seedContract"]["idHexChars"]]
    n = int.from_bytes(digest([seed, stable_id, "model", rules["version"]])[:8], "big")
    pick = n % sum(weight for _, weight in available)
    model = available[-1][0]
    for candidate, weight in available:
        if pick < weight:
            model = candidate
            break
        pick -= weight
    return {
        "status": "LAB_CANDIDATE_ONLY", "reasonCodes": [], "stableId": stable_id,
        "archetypeId": model["id"], "zoneId": zone_id, "settlementClass": case["settlementClass"],
        "provenance": "TEST_ONLY", "canonical": False, "materialized": False,
        "visibleName": None, "coordinates": None, "population": None, "worldStateId": None,
        "households": [], "npcInstances": [], "buildingInstances": [], "serviceInstances": [],
        "connectedRoutes": [], "inventory": [], "potentialBuildings": list(model["potentialBuildings"]),
        "potentialServices": list(model["potentialServices"])
    }

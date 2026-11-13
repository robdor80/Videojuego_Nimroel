#!/usr/bin/env python3
"""Edranor E17: contractual and adversarial verification; NO RUNTIME."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
D = T / "Datos operativos"
SRC = ["edranor_e14_habitability", "edranor_e15_living_economy", "edranor_e16_services_mobility"]
FAMILIES = {"HOUSEHOLD": "H", "WINE": "V", "WOOD": "B", "MOBILITY": "T", "SERVICE": "S", "GOVERNANCE": "A", "INFORMATION": "I", "RECOVERY": "R"}
DOMAINS = ["NEED", "ORDER", "AUTHORITY", "STOCK", "WORK", "PRODUCTION", "RESERVE", "MOBILITY", "RECEIPT", "SERVICE", "MESSAGE", "KNOWLEDGE", "MAINTENANCE", "LEDGER", "MEMORY"]
LIFECYCLE = ["OBSERVE_IF_REAL", "IDENTIFY_NEED", "OPEN_REQUEST", "VERIFY_AUTHORITY", "VERIFY_STOCK_AND_WORK", "VERIFY_ROUTE_AND_AGENT", "RESERVE_IF_REAL", "DISPATCH_IF_REAL", "RECEIVE_ACK", "CONSUME_OR_SERVE_IF_REAL", "MAINTAIN_IF_NEEDED", "RECONCILE_LEDGER", "RECORD_PROVEN_MEMORY_IF_REAL"]
CREATED = ["households", "people", "parcels", "roads", "physicalEdges", "services", "batches", "containers", "deliveries", "messages", "maintenanceJobs", "events", "memories", "taxes", "missions"]
UNKNOWN = ["population", "capacity", "production", "geographicScale", "travelTime", "travelDistance", "economicTurnover", "serviceCoverage", "workforce", "incidentRate"]
POLICIES = {
    "ledgerPolicy": ["availableEqualsOnHandMinusReserved", "noNegativeStock", "oneEventOneMutation", "reservationsNotDelivery", "invoiceNotStock", "lossDeductedOnce", "returnRequiresVerifiedNewEvent", "noCrossUnitConversionWithoutRecipe", "containerIdSurvivesRepair"],
    "knowledgePolicy": ["receiptRequired", "readPermissionRequired", "unknownIsNotTrue", "rumorIsNotFact", "historicalMemoryRequiresActualEvent", "crownOrdersNeedCrownAuthority"],
    "safetyPolicy": ["assetEvidenceRequired", "inspectionRequiredForReopen", "noForestExtractionWithoutRights", "noUnmeasuredAccess", "noAutoEscalationToProviders", "noAutoNPC", "noChildLaborOverride"],
}
DOCS = ["00_BASE_AUTORIDAD_Y_PRECEDENCIA.md", "01_MODELO_DE_CADENAS_Y_MEMORIA.md", "02_HOGARES_OFICIOS_Y_ABASTECIMIENTO.md", "03_VINO_BOSQUES_TONELERIA.md", "04_TRANSPORTES_SERVICIOS_Y_MANTENIMIENTO.md", "05_GOBIERNO_COMUNICACIONES_Y_VERDAD.md", "06_LABORATORIO_32_CONTRAFACTICOS.md", "07_ATLAS_CAUSAL_POR_ANCLA_Y_UNIDAD.md", "08_AUDITORIA_DECISIONES_Y_TRASPASO_E18.md", "README.md"]

class AuditError(ValueError):
    pass

def guard(condition, reason):
    if not condition:
        raise AuditError(reason)

def pairs_unique(pairs):
    result = {}
    for key, value in pairs:
        guard(key not in result, "duplicate JSON key " + key)
        result[key] = value
    return result

def read(name):
    return json.loads((D / name).read_text(encoding="utf-8-sig"), object_pairs_hook=pairs_unique)

def ids(items, key="id"):
    return [item[key] for item in items]

def gate(proofs, needed):
    if any(proofs.get(k) is False for k in needed):
        return "BLOCKED"
    if any(proofs.get(k) is not True for k in needed):
        return "PENDING_EVIDENCE"
    return "ELIGIBLE_SYNTHETIC_ONLY"

def dispatch(proofs, needed):
    value = gate(proofs, needed)
    return "BLOCKED_NO_RUNTIME" if value == "ELIGIBLE_SYNTHETIC_ONLY" else value

def check(c, ss):
    e14, e15, e16 = ss
    guard((c.get("schemaVersion"), c.get("documentId"), c.get("version"), c.get("phase"), c.get("date")) ==
          (1, "edranor_e17_regional_causal_cycles", "0.1", "E17", "2026-11-14"), "identity")
    guard(c["status"] == "DELEGATED_DESIGN_NOT_CANON" and c["authority"] == "ASSISTANT_DELEGATED_DESIGN", "authority")
    for k, v in {"runtimeEnabled": False, "syntheticOnly": True, "georeferenced": False, "physicalGraphValidated": False,
                 "worldStateEventsCreated": 0, "noNextPhaseExecuted": True, "noRealHistory": True,
                 "noRodasTransfer": True, "noInternalCustoms": True}.items():
        guard(type(c.get(k)) is type(v) and c[k] == v, "runtime/canon " + k)
    guard(c["sourceContracts"] == SRC and ids(ss, "documentId") == SRC and
          [x["phase"] for x in ss] == ["E14", "E15", "E16"] and
          all(x["runtimeEnabled"] is False for x in ss), "source locks")
    guard(c["inheritance"] == e16["inheritance"], "inheritance")
    guard(set(c["created"]) == set(CREATED) and all(type(c["created"][k]) is int and c["created"][k] == 0 for k in CREATED), "instances")
    guard(set(c["unknownMetrics"]) == set(UNKNOWN) and all(c["unknownMetrics"][k] is None for k in UNKNOWN), "metrics")
    guard(c["rights"] == e16["rights"] and c["rights"]["rodasJurisdiction"] == "crown_aethros" and
          c["rights"]["hallheimInsideEdranor"] is False and c["rights"]["internalCustoms"] is False, "rights")
    guard(e14["protectedAnchors"][3]["owner"] == "crown_aethros" and
          e15["profiles"][3]["owner"] == "crown_aethros", "Rodas authority sources")
    guard(c["anchors"] == [{k: x[k] for k in ["id", "owner", "role"]} for x in e16["anchors"]] and
          ids(c["anchors"]) == ["dorth", "lumina", "karsath", "rodas", "hallheim"], "anchors")
    guard(c["units"] == [{**{k: x[k] for k in ["unitId", "assessment", "territoryMembershipConfirmed"]},
                          "causalInstanceCreated": False} for x in e16["units"]] and
          c["units"][-1]["assessment"] == "NON_EVALUABLE" and
          c["units"][-1]["territoryMembershipConfirmed"] is False, "U7/units")
    graph = c["graph"]
    guard(set(graph) == {"demandOnly", "studyQuestions", "physicalEdges", "pathfindingEnabled",
                         "routeSurveyState", "causalTemplateDomains"} and
          graph["demandOnly"] is True and graph["physicalEdges"] == [] and
          graph["pathfindingEnabled"] is False and graph["routeSurveyState"] == "UNKNOWN" and
          graph["causalTemplateDomains"] == DOMAINS and
          graph["studyQuestions"] == ids(e16["graph"]["studyQuestions"], "sourceE05") and
          e16["graph"]["physicalEdges"] == [], "fictional physical graph")
    guard(c["lifeCycle"] == LIFECYCLE, "lifecycle")
    for section, keys in POLICIES.items():
        guard(set(c[section]) == set(keys) and all(c[section][k] is True for k in keys), "policy " + section)
    lp = c["loopPolicy"]
    guard(set(lp) == {"eventIdRequired", "uniqueCausalParent", "revisionMonotonic", "idempotencyRequired",
                      "noSyntheticWorldWrite", "maxSyntheticSteps", "onCycle", "onMissingEvidence"} and
          all(lp[k] is True for k in ["eventIdRequired", "uniqueCausalParent", "revisionMonotonic",
                                     "idempotencyRequired", "noSyntheticWorldWrite"]) and
          type(lp["maxSyntheticSteps"]) is int and lp["maxSyntheticSteps"] == 16 and
          lp["onCycle"] == "STOP_AND_AWAIT_NEW_EVIDENCE" and lp["onMissingEvidence"] == "PENDING_EVIDENCE", "loop policy")
    guard(c["gates"] == {"falseResult": "BLOCKED", "unknownResult": "PENDING_EVIDENCE",
                        "allTrueResult": "ELIGIBLE_SYNTHETIC_ONLY", "noRuntimeEffectResult": "BLOCKED_NO_RUNTIME",
                        "values": ["TRUE", "FALSE", "UNKNOWN"]}, "gates")
    cases = c["scenarios"]
    guard(len(cases) == 32 and len(set(ids(cases))) == 32 and
          c["familyCoverage"] == {fam: 4 for fam in FAMILIES}, "coverage")
    keys = {"id", "family", "anchor", "title", "conditionalTrigger", "chain", "requiredProofs",
            "missingProof", "exampleProofValue", "expectedIfMissing", "recoveryCondition",
            "status", "occurred", "worldStateMutation", "entityId", "location", "createdActorCount",
            "createdResourceCount"}
    for fam, prefix in FAMILIES.items():
        subset = [x for x in cases if x["family"] == fam]
        guard(ids(subset) == [f"ED17-{prefix}{i:02d}" for i in range(1, 5)], "case IDs " + fam)
        for x in subset:
            guard(set(x) == keys and x["anchor"] in ids(c["anchors"]), "case keys/anchor")
            guard(isinstance(x["title"], str) and len(x["title"]) >= 18 and
                  isinstance(x["conditionalTrigger"], str) and len(x["conditionalTrigger"]) >= 45 and
                  isinstance(x["recoveryCondition"], str) and len(x["recoveryCondition"]) >= 24, "thin case")
            guard(isinstance(x["chain"], list) and len(x["chain"]) >= 4 and
                  all(k in DOMAINS for k in x["chain"]) and "LEDGER" in x["chain"], "causal chain")
            guard(x["requiredProofs"] == list(dict.fromkeys(["eventEvidence", "authority", x["missingProof"]])), "proofs")
            guard(x["exampleProofValue"] is None or x["exampleProofValue"] is False, "hypothetical proof")
            guard(x["expectedIfMissing"] == ("BLOCKED" if x["exampleProofValue"] is False else "PENDING_EVIDENCE"), "case oracle")
            guard(x["status"] == "HYPOTHETICAL_NOT_OCCURRED" and x["occurred"] is False and
                  x["worldStateMutation"] is False and x["entityId"] is None and
                  x["location"] is None and type(x["createdActorCount"]) is int and
                  x["createdActorCount"] == 0 and type(x["createdResourceCount"]) is int and
                  x["createdResourceCount"] == 0, "scenario promoted to actual event")
    guard(c["debts"] == e16["debts"] and ids(c["debts"]) == [f"EDD-{i:02d}" for i in range(1, 9)] and
          c["debts"][5]["status"] != "OPEN" and
          all(x["status"] == "OPEN" for i, x in enumerate(c["debts"]) if i != 5), "EDD drift")
    dr = c["decisionRegister"]
    guard(ids(dr) == [f"ED17-DEC-{i:02d}" for i in range(1, 11)] and
          all(set(x) == {"id", "decision", "rejectedAlternative", "authority", "canonRatified"} and
              x["authority"] == "ASSISTANT_DELEGATED_DESIGN" and x["canonRatified"] is False and
              len(x["decision"]) > 15 and len(x["rejectedAlternative"]) > 15 for x in dr), "decision register")
    guard(c["carryForwardTo"] == ["E18", "E19", "E20-E24", "E25", "E26", "E27", "E28"], "next phase")
    for name in DOCS:
        f = T / "E17" / name
        guard(f.is_file() and f.stat().st_size > 300, "missing document " + name)
    guard((T / "E17_INDICE.md").is_file(), "missing E17 index")
    laboratory = (T / "E17/06_LABORATORIO_32_CONTRAFACTICOS.md").read_text(encoding="utf-8")
    guard(all(f"| {x['id']} |" in laboratory for x in cases), "scenario table mismatch")

def laboratory(c):
    n = 0
    for x in c["scenarios"]:
        need = x["requiredProofs"]
        full = {k: True for k in need}
        guard(gate(full, need) == "ELIGIBLE_SYNTHETIC_ONLY" and dispatch(full, need) == "BLOCKED_NO_RUNTIME", "no runtime")
        missing = dict(full)
        missing[x["missingProof"]] = x["exampleProofValue"]
        guard(gate(missing, need) == x["expectedIfMissing"], "case " + x["id"])
        absent = dict(full)
        absent.pop(x["missingProof"])
        guard(gate(absent, need) == "PENDING_EVIDENCE", "missing is not false")
        denied = dict(full)
        denied[x["missingProof"]] = False
        guard(gate(denied, need) == "BLOCKED", "explicit veto")
        mixed = dict(full)
        mixed["authority"] = False
        mixed["eventEvidence"] = "UNKNOWN"
        guard(gate(mixed, need) == "BLOCKED", "veto wins against UNKNOWN")
        n += 6
    stock, reserved = 8, 2
    events = {}
    def apply(event_id, ds, dr):
        nonlocal stock, reserved
        guard(type(ds) is int and type(dr) is int, "numeric type")
        pair = (ds, dr)
        if event_id in events:
            guard(events[event_id] == pair, "duplicate event with other mutation")
            return False
        ns, nr = stock + ds, reserved + dr
        guard(ns >= 0 and 0 <= nr <= ns, "negative/double spent stock")
        stock, reserved = ns, nr
        events[event_id] = pair
        return True
    guard(apply("reserve", 0, 3) and not apply("reserve", 0, 3), "idempotent reservation")
    guard(apply("dispatch", -2, -2) and apply("loss", -1, 0) and apply("return", 1, 0), "stock conservation")
    guard((stock, reserved) == (6, 3), "ledger result")
    n += 4
    for event_id, ds, dr in [("reserve", 0, 1), ("negative", -4, 0), ("double", 0, 4), ("float", 1.2, 0)]:
        try: apply(event_id, ds, dr)
        except AuditError: n += 1
        else: raise AuditError("invalid ledger accepted")
    guard((stock, reserved) == (6, 3), "ledger mutated on rejection")
    n += 1
    def memory(observed, source, receipt, permitted):
        return all(x is True for x in (observed, source, receipt, permitted))
    for args, expected in [((True, True, True, True), True), ((True, True, False, True), False),
                           ((True, None, True, True), False), ((False, True, True, True), False)]:
        guard(memory(*args) is expected, "knowledge/memory proof")
        n += 1
    def reopen(asset, work, inspection, rights, runtime):
        return all(x is True for x in (asset, work, inspection, rights, runtime))
    for args, expected in [((True, True, True, True, False), False), ((True, True, False, True, True), False),
                           ((False, True, True, True, True), False), ((True, True, True, True, True), True)]:
        guard(reopen(*args) is expected, "premature reopening")
        n += 1
    def finite(sequence):
        seen = set()
        last_revision = -1
        for i, item in enumerate(sequence):
            if i >= 16 or item in seen or item[1] < last_revision:
                return "STOP_AND_AWAIT_NEW_EVIDENCE"
            seen.add(item)
            last_revision = item[1]
        return "TRACE_FINITE_SYNTHETIC_ONLY"
    guard(finite([("a", 1), ("b", 2)]) == "TRACE_FINITE_SYNTHETIC_ONLY", "finite")
    guard(finite([("a", 1), ("a", 1)]) == "STOP_AND_AWAIT_NEW_EVIDENCE", "repeat")
    guard(finite([("a", 2), ("b", 1)]) == "STOP_AND_AWAIT_NEW_EVIDENCE", "revision")
    guard(finite([(f"event{i}", i) for i in range(17)]) == "STOP_AND_AWAIT_NEW_EVIDENCE", "bound")
    return n + 4

def mutations(c, ss):
    cases = [
        (["phase"], "E18"), (["status"], "CANON"), (["authority"], "AUTHOR"), (["runtimeEnabled"], True),
        (["syntheticOnly"], False), (["georeferenced"], True), (["physicalGraphValidated"], True),
        (["worldStateEventsCreated"], 1), (["noNextPhaseExecuted"], False), (["noRealHistory"], False),
        (["noRodasTransfer"], False), (["noInternalCustoms"], False),
        (["created", "roads"], 1), (["created", "events"], 1), (["created", "people"], 1),
        (["created", "taxes"], 1), (["created", "memories"], 1), (["unknownMetrics", "travelTime"], 4),
        (["unknownMetrics", "population"], 200), (["sourceContracts"], ["edranor_e16_services_mobility"]),
        (["rights", "rodasJurisdiction"], "casa_edranor"), (["rights", "rodasFiscalOwner"], "casa_edranor"),
        (["rights", "internalCustoms"], True), (["rights", "automaticRoadToll"], True),
        (["rights", "forestCuttingWithoutPermit"], True), (["rights", "hallheimInsideEdranor"], True),
        (["rights", "karsathUrbanHarborVerified"], True),
        (["anchors", 3, "owner"], "casa_edranor"), (["anchors", 4, "owner"], "casa_edranor"),
        (["units", 6, "assessment"], "STUDY_ONLY"), (["units", 6, "territoryMembershipConfirmed"], True),
        (["units", 0, "causalInstanceCreated"], True), (["graph", "demandOnly"], False),
        (["graph", "physicalEdges"], ["invented"]), (["graph", "pathfindingEnabled"], True),
        (["graph", "routeSurveyState"], "VERIFIED"), (["graph", "studyQuestions"], []),
        (["lifeCycle"], ["ACT"]), (["ledgerPolicy", "noNegativeStock"], False),
        (["ledgerPolicy", "oneEventOneMutation"], False), (["knowledgePolicy", "receiptRequired"], False),
        (["knowledgePolicy", "rumorIsNotFact"], False), (["safetyPolicy", "noAutoNPC"], False),
        (["safetyPolicy", "inspectionRequiredForReopen"], False),
        (["loopPolicy", "idempotencyRequired"], False), (["loopPolicy", "maxSyntheticSteps"], 10000),
        (["loopPolicy", "onCycle"], "RETRY_FOREVER"), (["gates", "unknownResult"], "ELIGIBLE"),
        (["familyCoverage", "WOOD"], 8),
        (["scenarios", 0, "occurred"], True), (["scenarios", 1, "worldStateMutation"], True),
        (["scenarios", 2, "status"], "HISTORY"), (["scenarios", 3, "entityId"], "npc1"),
        (["scenarios", 4, "location"], [0, 0]), (["scenarios", 5, "createdActorCount"], 1),
        (["scenarios", 6, "createdResourceCount"], 1), (["scenarios", 7, "family"], "WOOD"),
        (["scenarios", 8, "chain"], ["NEED"]), (["scenarios", 9, "missingProof"], "not_required"),
        (["scenarios", 10, "exampleProofValue"], True), (["scenarios", 11, "expectedIfMissing"], "DONE"),
        (["scenarios", 12, "requiredProofs"], ["eventEvidence"]), (["scenarios", 13, "anchor"], "fiction"),
        (["debts", 6, "status"], "RESOLVED"), (["decisionRegister", 0, "canonRatified"], True),
        (["decisionRegister", 1, "authority"], "AUTHOR_EXPRESS"), (["carryForwardTo"], ["E18"]),
    ]
    for path, value in cases:
        mutated = copy.deepcopy(c)
        ref = mutated
        for key in path[:-1]:
            ref = ref[key]
        ref[path[-1]] = value
        try: check(mutated, ss)
        except (AuditError, KeyError, TypeError, IndexError): continue
        raise AuditError("accepted mutation " + repr(path))
    return len(cases)

def main():
    sources = [read(name + "_v0.1.json") for name in SRC]
    c = read("edranor_e17_regional_causal_cycles_v0.1.json")
    check(c, sources)
    n, m = laboratory(c), mutations(c, sources)
    print(f"E17 PASS | 32 scenarios / 8 families | {n} conceptual checks | {m} mutations rejected | NO RUNTIME")

if __name__ == "__main__":
    try: main()
    except (AuditError, ValueError, TypeError, KeyError, IndexError, FileNotFoundError, OSError) as e:
        print("E17 FAIL: " + str(e), file=sys.stderr)
        sys.exit(1)

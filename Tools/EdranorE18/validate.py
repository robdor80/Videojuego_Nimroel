#!/usr/bin/env python3
"""Edranor E18: evidence-gated maturity audit, no map/gameplay claims."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
D = T / "Datos operativos"
BASE = "b4fb1ed9ce114e1532251e28c205eaecf42dbe08"
SOURCES = ["edranor_e13_physical_design", "edranor_e14_habitability",
           "edranor_e15_living_economy", "edranor_e16_services_mobility",
           "edranor_e17_regional_causal_cycles"]
DIM_IDS = ["GEOGRAFIA", "CLIMA", "RECURSOS", "ASENTAMIENTOS", "POBLACION",
           "INSTITUCIONES", "CULTURA", "PERSONAJES", "CONFLICTOS", "IMPLEMENTACION"]
DEBTS = [f"EDD-{n:02d}" for n in range(1, 9)]
DOCS = ["README.md", "00_ALCANCE_AUTORIDAD_METODO.md",
        "01_MATRIZ_DIEZ_DIMENSIONES.md", "02_COHERENCIA_Y_PROHIBICIONES.md",
        "03_HALLAZGOS_DEUDA_Y_PRIORIDAD.md", "04_DICTAMEN_Y_TRASPASO_E19.md"]

class AuditError(ValueError):
    pass

def require(ok, desc):
    if not ok:
        raise AuditError(desc)

def pairs_unique(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "duplicate JSON key: " + k)
        out[k] = v
    return out

def read(name):
    with (D / (name + "_v0.1.json")).open(encoding="utf-8-sig") as fp:
        return json.load(fp, object_pairs_hook=pairs_unique)

def verify(a, src):
    e13, e14, e15, e16, e17 = src
    require((a.get("schemaVersion"), a.get("documentId"), a.get("version"), a.get("phase")) ==
            (1, "edranor_e18_intermediate_maturity_audit", "0.1", "E18"), "identity")
    require(a.get("date") == "2026-11-14" and a.get("sourceMainSha") == BASE, "source SHA/date")
    require(a.get("status") == "AUDIT_DOCUMENTAL_WITH_MATERIAL_GATES" and
            a.get("authority") == "ASSISTANT_DELEGATED_AUDIT", "authority")
    for k, value in dict(mainModified=False, canonSuperiorModified=False,
                         runtimeEnabled=False, worldStateEventsCreated=0,
                         syntheticOnly=True, noNextPhaseExecuted=True).items():
        require(type(a.get(k)) is type(value) and a[k] == value, "false promotion: " + k)
    require(a.get("auditedPhases") == ["E13", "E14", "E15", "E16", "E17"], "phase coverage")
    require([s["phase"] for s in src] == a["auditedPhases"], "wrong sources")
    require(set(a.get("maturityScale", {})) == {"B0", "B1", "B2", "B3", "B4"}, "scale")
    dims = a.get("dimensions", [])
    require([d.get("id") for d in dims] == DIM_IDS, "10 dimensions/order/unique")
    for d in dims:
        require(d.get("level") == "B2" and d.get("documentaryDesign") is True and
                d.get("materialEvidenceValidated") is False and
                d.get("runtimeValidated") is False and
                bool(d.get("sources")) and bool(d.get("handoff")), "unproven maturity")
    debts = a.get("debts", [])
    require([d.get("id") for d in debts] == DEBTS, "debt list")
    for i, d in enumerate(debts):
        expected = "RESOLVED_FOR_DESIGN" if i == 5 else "OPEN"
        require(d.get("status") == expected and bool(d.get("evidenceToClose")) and
                bool(d.get("responsiblePhase")), "debt promotion")
    for source in src:
        require([d["status"] for d in source["debts"]] ==
                [d["status"] for d in debts], "source debt disagreement")
        require(source["runtimeEnabled"] is False, "source runtime falsely enabled")
    anchors = a.get("protectedAnchors", [])
    require(anchors == [{"id": x["id"], "owner": x["owner"]} for x in e17["anchors"]],
            "protected anchors/ownership")
    require([x["id"] for x in anchors] == ["dorth", "lumina", "karsath", "rodas", "hallheim"],
            "anchor identities")
    inv = a.get("invariants", {})
    require(set(inv) == {"rodasVillageRoyal","rodasNoHouseTaxOrMilitary",
        "hallheimOutsideHouse","luminaAnnualMarketOnly","bosqueAltoNoFreeLogging",
        "karsathUrbanHarborUnverified","physicalGraphEdges","units",
        "u7NonEvaluable","communicationReceiptRequired","allE17ScenariosUnoccurred",
        "sourceOfTruthNotPromoted"}, "invariant keys")
    require(all(inv[k] is True for k in inv if k not in ("physicalGraphEdges", "units")) and
            type(inv["physicalGraphEdges"]) is int and inv["physicalGraphEdges"] == 0 and
            type(inv["units"]) is int and inv["units"] == 7, "invariant assertions")
    require(e13["map"]["northBoundaryClosed"] is False and
            e13["map"]["metricGeometryValidated"] is False and
            len(e13["physicalUnits"]) == 7 and
            e13["physicalUnits"][-1]["insideHouseTerritoryConfirmed"] is False, "E13 geography/U7")
    require(len(e14["units"]) == 7 and e14["parcelsCertified"] == 0 and
            all(u["approvedOccupationSites"] == 0 for u in e14["units"]), "E14 occupancy")
    require(all(n == 0 for n in e15["instancesCreated"].values()) and
            len(e15["scenarios"]) == 28, "E15 fabricated resources")
    require(e16["graph"]["physicalEdges"] == [] and
            e16["communication"]["installedChannels"] == [] and
            len(e16["scenarios"]) == 30, "E16 fabricated network")
    require(e17["graph"]["physicalEdges"] == [] and
            len(e17["scenarios"]) == 32 and
            all(s["occurred"] is False and s["worldStateMutation"] is False
                for s in e17["scenarios"]) and
            all(v == 0 for v in e17["created"].values()) and
            e17["units"][-1]["assessment"] == "NON_EVALUABLE", "E17 fake World State")
    ev = a.get("observedEvidence", {})
    require(ev == {"e13Units":7, "e14OccupationOptions":24,
        "e15SyntheticScenarios":28, "e16SyntheticScenarios":30,
        "e17SyntheticScenarios":32, "e16PhysicalGraphEdges":0,
        "e17RealWorldMutations":0, "e11StableDefinitionIds":5}, "observed quantities")
    fs = a.get("findings", [])
    require(len(fs) == 12 and
            [f.get("id") for f in fs] == [f"E18-H{i:02d}" for i in range(1, 13)] and
            all(f.get("dimension") in DIM_IDS and
                (f.get("debtId") is None or f.get("debtId") in DEBTS) and
                f.get("class") in ("BLOCKER_MATERIAL", "BLOCKER_RUNTIME",
                                   "TRACKED_EVIDENCE", "TRACKED_AUTHORITY") and
                f.get("resolution") == "NOT_RESOLVED_IN_E18"
                for f in fs), "findings/claims")
    gates = a.get("gates", {})
    require(set(gates) == {"E19", "E20_E24", "E25", "E26", "E27", "E28"}, "handoff gates")
    require(gates["E19"] == {
        "researchAndSourceCollectionAllowed": True,
        "provisionalNonmetricDesignAllowed": True,
        "metricGeometryReady": False, "physicalRoutingReady": False,
        "requiresEvidence": ["EDD-01", "EDD-02", "EDD-03", "EDD-07"]}, "E19 material gate")
    for name, flag in [("E20_E24", "georeferencedDeploymentReady"),
                       ("E25", "canonicalSuccessionReady"),
                       ("E26", "populationInstantiated"),
                       ("E27", "historyRatified"),
                       ("E28", "actualGameplayCertified")]:
        require(gates[name].get(flag) is False, "premature phase completion: " + name)
    dr = a.get("decisionRegister", [])
    require([x.get("id") for x in dr] == [f"ED18-DEC-{i:02d}" for i in range(1, 6)] and
            all(x.get("authority") == "ASSISTANT_DELEGATED_AUDIT" and
                x.get("canonRatified") is False for x in dr), "decision authority")
    require(a.get("nextPhase") == "E19", "next phase")
    for name in DOCS:
        f = T / "E18" / name
        require(f.is_file() and f.stat().st_size >= 300, "missing/thin E18 doc " + name)
    require((T / "E18_INDICE.md").is_file(), "missing index")
    registry = (T / "E18/03_HALLAZGOS_DEUDA_Y_PRIORIDAD.md").read_text(encoding="utf-8")
    require(all("| " + x["id"] + " |" in registry for x in fs), "registry mismatch")
    require(all("| " + x["id"] + " |" in registry for x in debts), "debt registry mismatch")

def main():
    sources = [read(n) for n in SOURCES]
    audit = read("edranor_e18_maturity_audit")
    verify(audit, sources)
    tests = [
        lambda a: a["dimensions"][0].__setitem__("level", "B3"),
        lambda a: a["dimensions"][9].__setitem__("runtimeValidated", True),
        lambda a: a["debts"][0].__setitem__("status", "RESOLVED"),
        lambda a: a["debts"][5].__setitem__("status", "OPEN"),
        lambda a: a["protectedAnchors"][3].__setitem__("owner", "casa_edranor"),
        lambda a: a["invariants"].__setitem__("physicalGraphEdges", 4),
        lambda a: a["gates"]["E19"].__setitem__("metricGeometryReady", True),
        lambda a: a["gates"]["E28"].__setitem__("actualGameplayCertified", True),
        lambda a: a.__setitem__("runtimeEnabled", True),
        lambda a: a["findings"].pop(),
        lambda a: a.__setitem__("sourceMainSha", "0" * 40),
        lambda a: a["decisionRegister"][0].__setitem__("canonRatified", True)
    ]
    for i, mutate in enumerate(tests, 1):
        changed = copy.deepcopy(audit)
        mutate(changed)
        try:
            verify(changed, sources)
        except AuditError:
            pass
        else:
            raise AuditError(f"adversarial mutation {i} was wrongly accepted")
    print(f"E18 PASS: 10 dimensions B2, 8 EDD, 12 findings, "
          f"{len(tests)} rejected adverse mutations, source E13-E17 checked; NO RUNTIME")

if __name__ == "__main__":
    main()

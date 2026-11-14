#!/usr/bin/env python3
"""E19-R6: auditoría cruzada de contratos B2, sin certificar cartografía ni runtime."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
E = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
V = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik"
P = E / "E19-R6"
EXPECTED_SHAS = [
    "addd767de9bf27ef35e8aef6d68cde00dea79c10",
    "4472e81a88eba7a8e42528043ee426d685c76cef",
    "50a284cf33d59465332623c8a46c5e1d41cdb664",
    "8887445eec5996d18f4c63b849f568ea39c8b0ef",
    "17664ebd54f9553d1a652c79f4a851c169da629c",
    "f38da5e8a0a262e107ba94ec6ea07a5a7f4a7751",
]
STATES = [
    "SOURCE_REVIEW_ONLY_MATERIAL_BLOCKED",
    "REGIONAL_DESIGN_NOT_RUNTIME",
    "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME",
    "REGIONAL_CAUSAL_OCCUPATION_B2_NOT_RUNTIME",
]
DIMS = ["GEOGRAFIA", "CLIMA", "RECURSOS", "ASENTAMIENTOS", "POBLACION",
        "INSTITUCIONES", "CULTURA", "PERSONAJES", "CONFLICTOS", "IMPLEMENTACION"]
SCOPES = ["E19_DIRECT"] * 4 + ["E19_INTERFACE"] * 2 + ["FUTURE_LOCAL"] * 3 + ["E19_INTERFACE"]
DEBTS = ["EDD-01", "EDD-02", "EDD-03", "EDD-04", "EDD-05", "EDD-07", "EDD-08"]
INVARIANTS = {
    "northSketchJoined": False, "politicalNorthClosed": False,
    "farNorthMF08Evaluable": False,
    "valkramWest": "casa_darovan", "valkramEast": "casa_edranor",
    "azuriosWest": "casa_edranor", "azuriosEast": "casa_galdren",
    "lurienWholeSouthernBoundary": False, "rodasType": "ALDEA",
    "rodasJurisdiction": "crown_aethros", "hallheimInEdranor": False,
    "bosqueAltoPermitRequired": True, "bosqueRealOwner": "crown_aethros",
    "karsathUrbanPortConfirmed": False, "caleranAtDorthConfirmed": False,
    "r4CertifiedPhysicalNodes": 0, "r4CertifiedPhysicalEdges": 0,
    "r5CertifiedProviders": 0, "r5ActualSettlements": 0,
    "r5ApprovedParcels": 0, "r5WorldStateEntities": 0,
    "r5OSStudies": 19, "r5AdversarialCases": 30,
    "actualPopulationVerified": False,
}
GATES = [
    "NORTH_AND_LEGAL_BOUNDARIES", "METRIC_SPATIAL_AUTHORITY",
    "HYDROLOGY_RECEPTOR_RIGHTS", "SOIL_CLIMATE_SURVEY",
    "VERIFIED_GP_ROADS_ACCESS", "PARCELS_HOMES_OWNERSHIP",
    "CENSUS_AND_PROVIDERS", "QA_AND_PROVENANCE",
    "GODOT_2D_WORLD_LOAD", "CORERPG_WORLDSTATE_SAVELOAD",
]

class AuditError(ValueError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)

def unique_object(pairs: list) -> dict:
    out = {}
    for k, v in pairs:
        require(k not in out, "duplicate JSON key: " + k)
        out[k] = v
    return out

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)

def zero(value, key: str) -> None:
    require(type(value) is int and value == 0, key + " must remain 0")

def verify(a: dict, r: list[dict], e18: dict) -> None:
    r0, r1, r2, r3, r4, r5 = r
    require((a.get("schemaVersion"), a.get("documentId"), a.get("phase"), a.get("date")) ==
            (7, "edranor_e19_r6_transversal_parity", "E19-R6", "2026-11-14"), "R6 identity")
    require(a.get("status") == "REGIONAL_B2_METHOD_PARITY_WITH_EXPLICIT_GAPS", "R6 status")
    require(a.get("authority") == "INDEPENDENT_ASSISTANT_AUDIT_NO_CANON_PROMOTION", "R6 authority")
    require(a.get("precedence") == "AUTHOR_20261114_R0_SUPERSEDES_E20_P00_METRIC_PREREQUISITE_FOR_B2", "authorial precedence")
    require(a.get("rejectedPR84Reused") is False, "rejected PR84")
    require(a["parent"] == {"phase": "E19-R5", "headSha": EXPECTED_SHAS[5],
             "repo": "robdor80/Videojuego_Nimroel",
             "mainAtAudit": "223f1e49adfbc73be6a80c6ce36e7aab506450c2"}, "parent pin")
    expected_sources = [
        {"phase": f"E19-R{i}", "sha": sha, "status": status}
        for i, (sha, status) in enumerate(zip(EXPECTED_SHAS, STATES))
    ]
    require(a.get("sources") == expected_sources, "R0-R5 source evidence/lineage")
    require([x.get("status") for x in r] == STATES, "source states have changed")
    require(r1["parentHeadSha"] == EXPECTED_SHAS[0], "R1 parent")
    require(r2["base"]["r0HeadSha"] == EXPECTED_SHAS[0] and
            r2["base"]["r1HeadSha"] == EXPECTED_SHAS[1], "R2 parents")
    for i in (3, 4, 5):
        require(r[i]["parent"]["headSha"] == EXPECTED_SHAS[i-1] and
                r[i]["parent"]["rejectedPR84Used"] is False, f"R{i} parent")
    require(r0["rejectedPR84Used"] is False and r1["rejectedPR84Used"] is False and
            r2["base"]["rejectedPR84Used"] is False, "PR84 content")
    v = a.get("verdict", {})
    require(v == {"regionalMethodB2": "PARITY_WITH_RESERVATIONS",
                  "materialB3": "NOT_ACCREDITED", "runtimeB4": "NOT_ACCREDITED",
                  "wholeTerritory": "NOT_ACCREDITED", "e19TecCompleted": False,
                  "e20Completed": False, "mainMerged": False}, "verdict false promotion")
    require(a.get("invariants") == INVARIANTS, "transversal invariants")
    require(a.get("openDebts") == DEBTS and a.get("designOnlyDebt") == "EDD-06", "debt book")
    require(len(e18["dimensions"]) == 10 and
            [x["id"] for x in e18["dimensions"]] == DIMS and
            all(x["level"] == "B2" and x["materialEvidenceValidated"] is False
                and x["runtimeValidated"] is False for x in e18["dimensions"]),
            "E18 maturity was promoted")
    debt_states = {x["id"]: x["status"] for x in e18["debts"]}
    require(all(debt_states[d] == "OPEN" for d in DEBTS)
            and debt_states["EDD-06"] == "RESOLVED_FOR_DESIGN", "E18 debts conflict")
    matrix = a.get("matrix", [])
    require(len(matrix) == 10 and [x["dimension"] for x in matrix] == DIMS, "ten dimensions")
    for row, scope in zip(matrix, SCOPES):
        expected = "B2_METHOD_ONLY" if scope == "E19_DIRECT" else (
            "B2_INTERFACE_ONLY" if scope == "E19_INTERFACE" else "OUTSIDE_E19_AUDIT")
        require(row == {"dimension": row["dimension"], "scope": scope,
                        "e18DocumentedB2": True, "materialValidatedB3": False,
                        "runtimeValidatedB4": False, "regionalVerdict": expected}, "matrix false claim")
    gates = a.get("materialPromotionGates", [])
    require(len(gates) == 10, "missing material gates")
    for i, gate in enumerate(gates):
        ident = ("B3-" if i < 8 else "B4-") + f"{i+1 if i<8 else i-7:02d}"
        require(gate == {"id": ident, "scope": GATES[i], "passed": False}, "gate promoted")
    require(a.get("regression") == {
        "r0ToR5Required": True, "r6CrossChecksRequired": True,
        "linuxWindowsRequired": True, "testsAreSyntheticNotRuntime": True,
        "certifiedFinalHead": None}, "regression must not claim CI before evidence")
    require(a.get("next") == "E19-TEC_AND_E20_E29_WITH_GATE_EVIDENCE", "next phases")
    require(len(a["docs"]) == 6 and len(set(a["docs"])) == 6, "audit documents")
    for name in a["docs"]:
        require(name.endswith(".md") and "/" not in name, "unsafe doc path")
        text = (P / name).read_text(encoding="utf-8")
        require(len(text) > 500 and "E19-R6" in text, "audit document missing: " + name)
    require(all((V / name).is_file() for name in [
        "Geografia_local/README.md",
        "Geografia_local/microrelieve_y_unidades_de_drenaje_v0.1.md",
        "Geografia_local/cuencas_manantiales_red_hidrografica_menor_v0.1.md",
        "Geografia_local/reglas_espaciales_generacion_motor_v0.1.md",
        "Treskal/AUDITORIA_CIERRE_FUNCIONAL_TRESKAL_v0.1.md",
    ]), "Valrik comparator missing")
    # Reglas autorales y separación geográfica/material de R0–R1.
    require(r0["protectedPlaces"]["rodas"] == "crown_aethros" and
            r0["protectedPlaces"]["hallheim"] == "outside_edranor" and
            r0["boundaryModel"]["north"]["redLinesMeet"] is False and
            r0["boundaryModel"]["north"]["artificialClosureAllowed"] is False,
            "R0 crown/north")
    require(r1["boundaries"]["west"]["westernSlope"] == "casa_darovan" and
            r1["boundaries"]["west"]["easternSlope"] == "casa_edranor" and
            r1["boundaries"]["east"]["westernSlope"] == "casa_edranor" and
            r1["boundaries"]["east"]["easternSlope"] == "casa_galdren" and
            r1["boundaries"]["south"]["entireRiverBoundary"] is False and
            r1["boundaries"]["north"]["redSketchLinesJoin"] is False, "R1 slopes/borders")
    require(r1["jurisdiction"]["rodasType"] == "ALDEA" and
            r1["jurisdiction"]["rodas"] == "crown_aethros" and
            r1["jurisdiction"]["bosqueReal"] == "crown_aethros" and
            r1["jurisdiction"]["bosqueAltoHarvest"] == "PERMIT_REQUIRED", "R1 jurisdiction")
    require([x["id"] for x in r1["physicalRegions"]] ==
            [f"MF-{i:02d}" for i in range(1, 9)] and
            r1["physicalRegions"][7]["evaluable"] is False, "MF08 cannot be evaluated")
    require(r1["geometry"] is None and r1["worldStateEntities"] == 0, "R1 materialized")
    # Agua: el grafo conceptual no se asciende a cauces o derechos reales.
    require(r2["majorSystem"]["southBorderOnlyPartialLurien"] is True and
            r2["majorSystem"]["caleranAtDorthConfirmed"] is False and
            r2["majorSystem"]["urbanKarsathShoreConfirmed"] is False, "R2 major system")
    require(r2["divides"]["farNorthMF08"] == "NON_EVALUABLE" and
            r2["divides"]["northArtificialClosure"] is False and
            r2["graphContract"]["minorGraphEdges"] == [] and
            r2["graphContract"]["waterRightsImplied"] is False, "R2 water rights/graph")
    require(len(r2["basinFamilies"]) == 7 and len(r2["minorDrainageScenarios"]) == 14,
            "R2 conditional families")
    for key in ("actualMinorRivers", "actualSprings", "actualWetlands", "actualWaterRights", "worldStateEntities"):
        zero(r2["materialization"][key], "R2." + key)
    require(r2["materialization"]["geometry"] is None, "R2 geometry")
    require(len(r3["contexts"]) == 8 and r3["contexts"][7]["status"] == "NON_EVALUABLE" and
            r3["maturity"]["b3Mapped"] is False and r3["maturity"]["b4Runtime"] is False and
            r3["maturity"]["geometry"] is None, "R3 maturity")
    for key in ("actualParcels", "activeHarvestSites", "worldStateEntities"):
        zero(r3["maturity"][key], "R3." + key)
    require(r3["governance"]["bosqueRealHarvestByEdranor"] is False and
            r3["governance"]["karsathUrbanAntelaShoreConfirmed"] is False, "R3 rights")
    # Gd/Gq no son Gp: ni una arista de transporte certificada.
    require(r4["networks"]["physical"] == "EMPTY_NOT_CERTIFIED" and
            r4["networks"]["pathfindingEnabled"] is False and
            r4["networks"]["acceptedPhysicalGraph"] == {"nodes": [], "edges": []} and
            r4["networks"]["roadGeometry"] == [], "Gp empty")
    for key in ("physicalEdges", "physicalNodes", "actualRoads", "worldStateEntities"):
        zero(r4["maturity"][key], "R4." + key)
    require(r4["maturity"]["b3Mapped"] is False and r4["maturity"]["b4Runtime"] is False, "R4 B2 only")
    # OS son preguntas, Sp no acredita servicios ni habitantes.
    require(len(r5["studies"]) == 19 and len(r5["adversarialCases"]) == 30 and
            all(c["expected"] == "REJECT" for c in r5["adversarialCases"]), "R5 study/adversarial count")
    require([x["id"] for x in r5["contexts"]] == [f"MF-{i:02d}" for i in range(1, 9)] and
            r5["contexts"][7]["nonEvaluable"] is True, "R5 contexts")
    require(r5["coverage"]["verifiedProviderGraph"] == "SP_EMPTY" and
            r5["coverage"]["providerNodeIds"] == [] and
            r5["coverage"]["physicalServiceEdges"] == [], "Sp empty")
    require(r5["population"]["edd04"] == "OPEN" and
            r5["population"]["edranorCensus"] is None and
            r5["population"]["borrowedValrikPopulationRanges"] is False, "population inferred")
    require({x["id"] for x in r5["anchors"]} == {"dorth", "lumina", "karsath", "rodas", "hallheim"} and
            all(x["proceduralSpawn"] is False for x in r5["anchors"]), "manual and crown anchors")
    require(r5["governance"]["rodas"]["jurisdiction"] == "crown_aethros" and
            r5["governance"]["rodas"]["kind"] == "ALDEA" and
            r5["governance"]["bosqueAltoHarvest"] == "PERMIT_REQUIRED" and
            r5["governance"]["bosqueReal"] == "crown_aethros", "R5 sovereignty")
    require(all(v == [] for v in r5["spatialAuthority"].values()), "R5 unauthorized physical assets")
    require(r5["maturity"]["b3Mapped"] is False and r5["maturity"]["b4Runtime"] is False and
            r5["maturity"]["geometry"] is None, "R5 false materialization")
    for key in ("actualSettlements", "approvedParcels", "actualProviders", "worldStateEntities"):
        zero(r5["maturity"][key], "R5." + key)
    require(all((v is False if isinstance(v, bool) else v == 0)
                for v in r5["hardGuards"].values()), "R5 hard guards")
    require(a["invariants"]["r4CertifiedPhysicalNodes"] == r4["maturity"]["physicalNodes"] and
            a["invariants"]["r4CertifiedPhysicalEdges"] == r4["maturity"]["physicalEdges"] and
            a["invariants"]["r5ActualSettlements"] == r5["maturity"]["actualSettlements"] and
            a["invariants"]["r5OSStudies"] == len(r5["studies"]), "R6 is out of sync with sources")

def main() -> None:
    a = load(P / "parity_audit_v0.7.json")
    sources = [load(E / f"E19-R{i}/{name}") for i, name in enumerate([
        "source_manifest_v0.1.json", "natural_features_v0.2.json",
        "hydrology_v0.3.json", "environment_v0.4.json",
        "routes_v0.5.json", "occupation_v0.6.json",
    ])]
    e18 = load(E / "Datos operativos/edranor_e18_maturity_audit_v0.1.json")
    verify(a, sources, e18)
    mutations = [
        ("R6 status", "a", lambda x: x.__setitem__("status", "CERTIFIED_B4")),
        ("R6 parent", "a", lambda x: x["parent"].__setitem__("headSha", "unapproved")),
        ("R6 verdict", "a", lambda x: x["verdict"].__setitem__("wholeTerritory", "CERTIFIED")),
        ("R6 B3", "a", lambda x: x["verdict"].__setitem__("materialB3", "ACCREDITED")),
        ("R6 PR84", "a", lambda x: x.__setitem__("rejectedPR84Reused", True)),
        ("R6 north", "a", lambda x: x["invariants"].__setitem__("northSketchJoined", True)),
        ("R6 slopes", "a", lambda x: x["invariants"].__setitem__("valkramWest", "casa_edranor")),
        ("R6 Rodas", "a", lambda x: x["invariants"].__setitem__("rodasType", "VILLA")),
        ("R6 Gp", "a", lambda x: x["invariants"].__setitem__("r4CertifiedPhysicalEdges", 1)),
        ("R6 provider", "a", lambda x: x["invariants"].__setitem__("r5CertifiedProviders", 1)),
        ("R6 OS", "a", lambda x: x["invariants"].__setitem__("r5OSStudies", 18)),
        ("R6 matrix", "a", lambda x: x["matrix"][0].__setitem__("materialValidatedB3", True)),
        ("R6 gate", "a", lambda x: x["materialPromotionGates"][0].__setitem__("passed", True)),
        ("R6 EDD", "a", lambda x: x["openDebts"].remove("EDD-04")),
        ("R6 doc", "a", lambda x: x["docs"].pop()),
        ("R6 CI", "a", lambda x: x["regression"].__setitem__("certifiedFinalHead", "fake")),
        ("R0 join", 0, lambda x: x["boundaryModel"]["north"].__setitem__("redLinesMeet", True)),
        ("R1 slope", 1, lambda x: x["boundaries"]["east"].__setitem__("westernSlope", "casa_galdren")),
        ("R1 MF08", 1, lambda x: x["physicalRegions"][7].__setitem__("evaluable", True)),
        ("R2 Caleran", 2, lambda x: x["majorSystem"].__setitem__("caleranAtDorthConfirmed", True)),
        ("R2 river", 2, lambda x: x["graphContract"]["minorGraphEdges"].append({"fake": True})),
        ("R3 runtime", 3, lambda x: x["maturity"].__setitem__("b3Mapped", True)),
        ("R4 road", 4, lambda x: x["networks"]["acceptedPhysicalGraph"]["edges"].append({"fake": True})),
        ("R4 pathfinder", 4, lambda x: x["networks"].__setitem__("pathfindingEnabled", True)),
        ("R5 Sp", 5, lambda x: x["coverage"]["providerNodeIds"].append("fictional")),
        ("R5 OS", 5, lambda x: x["studies"].pop()),
        ("R5 home", 5, lambda x: x["maturity"].__setitem__("actualSettlements", 1)),
        ("R5 Crown", 5, lambda x: x["governance"]["rodas"].__setitem__("jurisdiction", "casa_edranor")),
        ("E18 B3", "e18", lambda x: x["dimensions"][0].__setitem__("materialEvidenceValidated", True)),
        ("E18 EDD", "e18", lambda x: x["debts"][0].__setitem__("status", "CLOSED")),
    ]
    for label, target, change in mutations:
        aa, rr, ee = copy.deepcopy(a), copy.deepcopy(sources), copy.deepcopy(e18)
        if target == "a":
            change(aa)
        elif target == "e18":
            change(ee)
        else:
            change(rr[target])
        try:
            verify(aa, rr, ee)
        except (AuditError, KeyError, TypeError, IndexError):
            continue
        raise AuditError("mutation not rejected: " + label)
    print(f"PASS E19-R6: R0-R5 lineage/cross-contract parity, 10 dimensions, "
          f"10 B3/B4 gates, 7 open debts, {len(mutations)} negative mutations; "
          "B2 method only, NO B3/B4/runtime")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""E19-R5: audit B2 occupation. Synthetic checks never certify real sites."""
from __future__ import annotations

import copy
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
VALRIK = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik"
DIR = EDR / "E19-R5"
PIN_R4 = "17664ebd54f9553d1a652c79f4a851c169da629c"

DOCS = ["README.md"] + [
    "01_JERARQUIA_Y_AUTORIDAD.md",
    "02_ESQUELETOS_ASENTAMIENTOS.md",
    "03_ATLAS_OCUPACION_CONTEXTOS.md",
    "04_HABITABILIDAD_Y_CAPACIDAD.md",
    "05_COBERTURA_REGIONAL_SERVICIOS.md",
    "06_ECONOMIA_USOS_Y_PAISAJE.md",
    "07_HOGARES_VIVIENDAS_CENSO.md",
    "08_RIESGOS_ESTACIONES_CAMBIO.md",
    "09_CONTRATO_B3_B4.md",
    "10_PARIDAD_VALRIK_ADVERSARIOS.md",
    "11_ACTA_Y_TRASPASO_R6.md",
]
USE_CLASSES = {
    "PERMANENT_RESIDENCE", "SEASONAL_WORKSTATION",
    "AGRICULTURAL_USE", "FOREST_USE", "TEMPORARY_PASSAGE", "EXCLUDED",
}
EXPECTED_CONTEXT_COUNTS = {
    "MF-01": 2, "MF-02": 3, "MF-03": 3, "MF-04": 4,
    "MF-05": 3, "MF-06": 3, "MF-07": 1, "MF-08": 0,
}
MANDATORY = {
    "jurisdiction_proven", "parcel_geometry_proven", "land_tenure_proven",
    "ground_stability_proven", "hazard_acceptability_proven",
    "potable_water_proven", "sanitation_proven", "food_or_supply_proven",
    "certified_gp_access_proven", "capacity_beds_and_resources_proven",
    "seasonal_safety_proven", "ecological_compatibility_proven",
    "competent_authority_approval_proven",
}
SEQUENCE = [
    "Valkram eastern slope", "Río Lurien", "Lago Antela",
    "Río Lurien", "Hallheim", "Golfo de Norgard",
]
EXPECTED_MATURITY_ZERO = (
    "actualSettlements", "actualVillages", "actualTowns", "actualVillas",
    "approvedParcels", "approvedDwellings", "approvedHouseholds",
    "actualResidents", "actualSeasonalWorkers", "actualProviders",
    "actualRoadAccesses", "worldStateEntities", "actualEmployment",
)
NULL_SPATIAL = ("geometry", "crs", "areaHectares")
FIELDS_STUDY_NULL = (
    "approvedLocationRef", "approvedPlotRef", "approvedPhysicalGpRef",
    "coordinates", "area", "yearRoundWaterRef", "legalTenureRef",
    "worldStateId", "possibleServiceProviderRef",
)
FIELDS_STUDY_ZERO = ("actualResidents", "actualDwellings", "actualEmployees")
EXPECTED_HARD_FALSE = (
    "valrikPopulationNumbersImported", "valrikUniversalVillageServicesImported",
    "edd04PopulationInvented", "edd07RoadInvented", "edd03WaterInvented",
    "northernAreaSettled", "northSketchJoined", "crownRodasTaken",
    "crownForestTaken", "forestHarvestWithoutPermit",
    "karsathUrbanPortInvented", "dorthCaleranInvented",
    "temporaryWorkersAddedToResidentCensus", "worldStateGenerated",
)
EXPECTED_ANCHOR_IDS = ["dorth", "lumina", "karsath", "rodas", "hallheim"]


def require(ok: bool, why: str) -> None:
    if not ok:
        raise AssertionError(why)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_documentation() -> None:
    for name in DOCS:
        f = DIR / name
        require(f.is_file(), f"missing R5 document {name}")
        text = f.read_text(encoding="utf-8")
        require(len(text) > 1700, f"document too short {name}")
        require(text.lstrip().startswith("# "), f"document heading {name}")
    for path in [
        VALRIK / "metodologia_generacion_asentamientos_treskal.md",
        VALRIK / "estructura_asentamientos_treskal.md",
        VALRIK / "Aldeas/00_Base/aldea_tipo_treskal.md",
        VALRIK / "Pueblos/00_Base/pueblo_tipo_treskal.md",
        VALRIK / "Villas/00_Base/villa_tipo_treskal.md",
        EDR / "Asentamientos/E06_ESQUELETO_ELEGIBILIDAD.md",
        EDR / "Poblacion_y_hogares/E08_CENSO_CARGA_ESTACIONAL.md",
        EDR / "E14/01_ATLAS_DE_HABITABILIDAD.md",
        EDR / "E19-R4/10_ACTA_Y_TRASPASO_R5.md",
    ]:
        require(path.is_file(), f"missing source: {path}")


def validate(data: dict, r4: dict) -> None:
    require(data["schemaVersion"] == 6, "R5 version")
    require(data["phase"] == "E19-R5", "R5 phase")
    require(data["documentId"] == "edranor_e19_r5_occupation", "R5 id")
    require(data["status"] == "REGIONAL_CAUSAL_OCCUPATION_B2_NOT_RUNTIME", "R5 status")
    require(data["precedent"] == "CASA_VALRIK_TRESKAL_SETTLEMENT_METHOD_NOT_LOCAL_CANON", "Valrik boundary")
    p = data["parent"]
    require(p == {
        "phase": "E19-R4", "headSha": PIN_R4,
        "documentId": "edranor_e19_r4_routes", "schemaVersion": 5,
        "rejectedPR84Used": False,
    }, "R4 lineage / excluded #84")
    require(data["governance"] == r4["governance"], "R4 jurisdiction or geography changed")
    require(data["governance"]["sourceHydrologySequence"] == SEQUENCE, "Lurien-Antela order")
    m = data["maturity"]
    require(m["b2Documentary"] is True and m["b3Mapped"] is False and m["b4Runtime"] is False,
            "false certification")
    for k in EXPECTED_MATURITY_ZERO:
        require(type(m[k]) is int and m[k] == 0, f"actual materialized {k}")
    for k in NULL_SPATIAL:
        require(m[k] is None, f"geometry/area invented {k}")
    pop = data["population"]
    require(pop["edd04"] == "OPEN", "EDD-04 inappropriately closed")
    for k in ("edranorCensus", "ruralResidents", "urbanResidents",
              "householdSizeMean", "actualDwellingCount",
              "populationDensity", "seasonalWorkerCount"):
        require(pop[k] is None, f"population invented {k}")
    require(pop["borrowedValrikPopulationRanges"] is False and
            pop["borrowedValrikHouseholdMean"] is False, "Valrik figures imported")
    require("UNIQUE_PERSON_ID" in pop["residentCounter"], "resident deduplication")
    require("SUBSET" in pop["seasonalWorkers"], "seasonal workers duplicate census")

    anchors = data["anchors"]
    require([x["id"] for x in anchors] == EXPECTED_ANCHOR_IDS, "canonical anchors")
    require([x["jurisdiction"] for x in anchors] ==
            ["casa_edranor"] * 3 + ["crown_aethros"] * 2, "anchor jurisdiction")
    require(anchors[3]["kind"] == "ALDEA" and anchors[4]["kind"] == "OUTSIDE_SCOPE", "Rodas/Hallheim")
    for a in anchors:
        require(a["proceduralSpawn"] is False and a["population"] is None and
                a["footprint"] is None, f"anchor promoted {a['id']}")
        require(a["design"] in ("MANUAL_E07", "EXTERNAL"), "anchor design")

    contexts = data["contexts"]
    require(len(contexts) == 8, "MF context count")
    require([x["id"] for x in contexts] == list(EXPECTED_CONTEXT_COUNTS), "MF sequence")
    for i, x in enumerate(contexts):
        require(x["hydrology"] == (f"HC-{i+1:02d}" if i < 7 else None),
                f"bad MF/HC pairing {i}")
        require(x["nonEvaluable"] is (i == 7), "MF08 must be non evaluable")
        require(x["status"] == ("NON_EVALUABLE" if i == 7 else "STUDY_ONLY"),
                "context certification")
        require(all(x[k] == 0 for k in ("approvedSites", "realSettlements", "approvedParcels")),
                "MF has real sites")
        require(x["geometry"] is None and x["habitableArea"] is None,
                "MF has assumed extent")
    require(set(x["code"] for x in data["useClasses"]) == USE_CLASSES, "E14 classes")
    for x in data["useClasses"]:
        require(x["actualPlaces"] == 0, "E14 class materialized")
    require(set(data["evidenceContract"]["perUseAdditionalGates"]) == USE_CLASSES,
            "class evidence missing")
    require(set(data["evidenceContract"]["requiredCommonGates"]) == MANDATORY,
            "evidence gates changed")
    require(data["evidenceContract"]["realSitePromotionsAllowedInR5"] is False,
            "R5 falsely promotes sites")
    require(data["evidenceContract"]["requiresCertifiedGpForAccessibleSettlements"] is True,
            "Gq passed as Gp")
    require(data["evidenceContract"]["noAveragingOfEssentialCapacities"] is True,
            "water/bed balance can be bypassed")

    skel = data["settlementSkeletons"]
    require([s["kind"] for s in skel] == ["ALDEA", "PUEBLO", "VILLA"], "skeleton taxonomy")
    for s in skel:
        require(s["status"] == "ABSTRACT_REQUIREMENTS_NOT_GENERATED", "skeleton instantiated")
        require(s["fixedPopulation"] is None and s["realInstances"] == 0,
                "settlement numbers imported")
        require(s["mandatoryNamedBusinesses"] == [], "Valrik services made obligatory")
        require(s["residentCommunityRequired"] is True, "settlement without inhabitants")
    require([x["id"] for x in data["economicProfiles"]] ==
            [f"EP-{i:02d}" for i in range(1,5)], "economic profile taxonomy")
    require(all(x["status"] == "TEMPLATE_NOT_INSTANCED" for x in data["economicProfiles"]),
            "economic profile materialized")

    studies = data["studies"]
    require(len(studies) == 19, "19 studies expected")
    require([x["id"] for x in studies] == [f"OS-{i:02d}" for i in range(1,20)],
            "stable OS ids")
    require(Counter(x["contextId"] for x in studies) ==
            Counter({k:v for k,v in EXPECTED_CONTEXT_COUNTS.items() if v}),
            "OS distribution/MF08 violation")
    for x in studies:
        require(x["useClass"] in USE_CLASSES - {"EXCLUDED"}, "invalid OS use")
        require(x["state"] == "STUDY_ONLY_NOT_A_PLACE" and x["studyOnly"] is True,
                f"OS promoted {x['id']}")
        require(x["actualSettlement"] is False and x["actualParcel"] is False,
                f"OS site invented {x['id']}")
        for k in FIELDS_STUDY_ZERO:
            require(type(x[k]) is int and x[k] == 0, f"OS counts {x['id']} {k}")
        for k in FIELDS_STUDY_NULL:
            require(x[k] is None, f"OS object link {x['id']} {k}")
    cov = data["coverage"]
    require(cov["demandGraph"] == "SD_HYPOTHESIS_ONLY" and
            cov["coverageQuestionGraph"] == "SQ_HYPOTHESIS_ONLY" and
            cov["verifiedProviderGraph"] == "SP_EMPTY", "coverage layers conflated")
    require(cov["providerNodeIds"] == [] and cov["physicalServiceEdges"] == [],
            "real service graph invented")
    require(cov["actualProviderCount"] == 0 and cov["calculatedServiceRadius"] is None
            and cov["travelTime"] is None, "fake coverage metric")
    require(len(cov["issues"]) == 10 and
            all(x["status"] == "NEED_NOT_PROVIDER" for x in cov["issues"]),
            "needs turned into providers")
    require([x["id"] for x in cov["issues"]] ==
            [f"SC-{i:02d}" for i in range(1,11)], "service question ids")
    for section in ("spatialAuthority", "worldState"):
        for k,v in data[section].items():
            if isinstance(v,list):
                require(v == [], f"{section}.{k} materialized")
    require(data["worldState"]["enabled"] is False and
            data["worldState"]["currentSeed"] is None, "runtime enabled")
    require(len(data["promotionGates"]) == 12, "B3/B4 gates")
    neg = data["adversarialCases"]
    require(len(neg) == 30, "negative cases")
    require([x["id"] for x in neg] == [f"NV-{i:02d}" for i in range(1,31)],
            "negative-case ids")
    require(len({x["code"] for x in neg}) == 30 and
            all(x["expected"] == "REJECT" for x in neg), "negative scenarios unguarded")
    for k in EXPECTED_HARD_FALSE:
        require(data["hardGuards"][k] is False, f"hard guard {k}")
    require(data["hardGuards"]["approvedNewSettlementCount"] == 0, "new canonical settlements")
    require([x["id"] for x in data["debts"]] ==
            ["EDD-01","EDD-02","EDD-03","EDD-04","EDD-07"], "EDD debt changed")
    require(all(x["state"] == "OPEN" for x in data["debts"]), "dependency closed")
    require(data["handoff"]["noMainOrParentMutations"] is True, "parent mutation intent")
    require(r4["maturity"]["physicalEdges"] == 0 and
            r4["maturity"]["physicalNodes"] == 0 and
            r4["networks"]["pathfindingEnabled"] is False and
            r4["networks"]["acceptedPhysicalGraph"] == {"nodes": [], "edges": []},
            "R4 changed: physical network unexpectedly present")


def evaluate_synthetic(use_class, context_id="MF-04", location_id=None,
                       jurisdiction="casa_edranor", evidence=None,
                       legal_denial=False, synthetic=True):
    """Pure diagnostic. Never writes a B3 record, plot, NPC or World State."""
    if context_id == "MF-08":
        return "NON_EVALUABLE"
    if location_id == "hallheim":
        return "OUTSIDE_SCOPE"
    if location_id == "rodas" or jurisdiction != "casa_edranor":
        return "OUTSIDE_EDRANOR_JURISDICTION"
    if location_id in ("dorth","lumina","karsath"):
        return "MANUAL_ANCHOR_NOT_PROCEDURAL"
    if legal_denial:
        return "INELIGIBLE"
    if use_class not in USE_CLASSES - {"EXCLUDED"}:
        return "INELIGIBLE"
    required = MANDATORY
    # Test fixtures only: per-use requirements are independent, never averaged.
    if evidence is None:
        evidence = {}
    if any(evidence.get(k) is False for k in required):
        return "INELIGIBLE"
    if any(evidence.get(k) is not True for k in required):
        return "PENDING_EVIDENCE"
    if not synthetic:
        return "PENDING_EVIDENCE"  # R5 has no inspected real parcel
    return "ELIGIBLE_IF_VERIFIED_NOT_MATERIALIZED"


def test_scenarios() -> int:
    count = 0
    full = {k: True for k in MANDATORY}
    for use in USE_CLASSES - {"EXCLUDED"}:
        require(evaluate_synthetic(use, evidence=full) ==
                "ELIGIBLE_IF_VERIFIED_NOT_MATERIALIZED", "all-true synthetic")
        count += 1
        require(evaluate_synthetic(use, evidence=full, synthetic=False) ==
                "PENDING_EVIDENCE", "synthetic result became real")
        count += 1
        for k in MANDATORY:
            for bad, expected in ((None,"PENDING_EVIDENCE"),(False,"INELIGIBLE")):
                modified = dict(full)
                modified[k] = bad
                require(evaluate_synthetic(use, evidence=modified) == expected,
                        f"{use} {k} {bad}")
                count += 1
    for case, kw, expected in [
        ("uncertain north", {"context_id":"MF-08"}, "NON_EVALUABLE"),
        ("Hallheim external", {"location_id":"hallheim"}, "OUTSIDE_SCOPE"),
        ("Rodas Crown", {"location_id":"rodas"}, "OUTSIDE_EDRANOR_JURISDICTION"),
        ("Darovan property", {"jurisdiction":"casa_darovan"}, "OUTSIDE_EDRANOR_JURISDICTION"),
        ("Dorth manual", {"location_id":"dorth"}, "MANUAL_ANCHOR_NOT_PROCEDURAL"),
        ("Lumina manual", {"location_id":"lumina"}, "MANUAL_ANCHOR_NOT_PROCEDURAL"),
        ("Karsath manual", {"location_id":"karsath"}, "MANUAL_ANCHOR_NOT_PROCEDURAL"),
        ("explicit denial", {"legal_denial":True}, "INELIGIBLE"),
    ]:
        require(evaluate_synthetic("PERMANENT_RESIDENCE", evidence=full, **kw) == expected,
                case)
        count += 1
    return count


def test_mutations(data, r4) -> int:
    count = 0
    def bad(mutator, label):
        nonlocal count
        d = copy.deepcopy(data)
        mutator(d)
        try:
            validate(d, r4)
        except (AssertionError, KeyError, TypeError):
            count += 1
            return
        raise AssertionError(f"mutation escaped validator: {label}")

    bad(lambda d: d["parent"].update({"headSha":"0000"}), "wrong parent pin")
    bad(lambda d: d["parent"].update({"rejectedPR84Used":True}), "PR84 restored")
    for k in data["governance"]:
        def mutate_gov(d,k=k):
            current = d["governance"][k]
            d["governance"][k] = (not current if isinstance(current,bool) else
                                  "WRONG" if isinstance(current,str) else [] if isinstance(current,list) else {})
        bad(mutate_gov, f"governance {k}")
    for k in EXPECTED_MATURITY_ZERO:
        bad(lambda d,k=k: d["maturity"].update({k:1}), f"maturity {k}")
    for k in NULL_SPATIAL:
        bad(lambda d,k=k: d["maturity"].update({k:"invented"}), f"spatial {k}")
    bad(lambda d: d["maturity"].update({"b3Mapped":True}), "false B3")
    bad(lambda d: d["maturity"].update({"b4Runtime":True}), "false B4")
    bad(lambda d: d["population"].update({"edranorCensus":123}), "invented census")
    bad(lambda d: d["population"].update({"householdSizeMean":4.8}), "imported household mean")
    bad(lambda d: d["population"].update({"borrowedValrikPopulationRanges":True}), "Valrik range")
    for i in range(5):
        bad(lambda d,i=i: d["anchors"][i].update({"proceduralSpawn":True}), f"anchor {i}")
    bad(lambda d: d["anchors"][3].update({"jurisdiction":"casa_edranor"}), "Rodas stolen")
    bad(lambda d: d["anchors"][3].update({"kind":"VILLA"}), "Rodas villa")
    for i in range(8):
        bad(lambda d,i=i: d["contexts"][i].update({"approvedParcels":1}), f"context {i}")
        bad(lambda d,i=i: d["contexts"][i].update({"geometry":[0,1]}), f"context geom {i}")
        bad(lambda d,i=i: d["contexts"][i].update({"status":"MAPPED"}), f"context status {i}")
    for i in range(19):
        for k,v in [
            ("actualSettlement",True),("actualParcel",True),("actualResidents",1),
            ("state","MATERIALIZED"),("approvedLocationRef","invented"),
            ("approvedPhysicalGpRef","CT-01"),("contextId","MF-08")
        ]:
            bad(lambda d,i=i,k=k,v=v: d["studies"][i].update({k:v}), f"OS {i} {k}")
    for i in range(3):
        bad(lambda d,i=i: d["settlementSkeletons"][i].update({"fixedPopulation":80}),
            f"skeleton population {i}")
        bad(lambda d,i=i: d["settlementSkeletons"][i].update({"mandatoryNamedBusinesses":["tavern"]}),
            f"skeleton services {i}")
    for k in EXPECTED_HARD_FALSE:
        bad(lambda d,k=k: d["hardGuards"].update({k:True}), f"hard guard {k}")
    bad(lambda d: d["hardGuards"].update({"approvedNewSettlementCount":1}), "new settlement")
    bad(lambda d: d["coverage"]["providerNodeIds"].append("fake-provider"), "provider graph")
    bad(lambda d: d["coverage"].update({"travelTime":10}), "travel estimate")
    bad(lambda d: d["coverage"]["issues"][0].update({"status":"ACTIVE_PROVIDER"}), "coverage reified")
    bad(lambda d: d["spatialAuthority"]["approvedDwellings"].append("house1"), "new house")
    bad(lambda d: d["worldState"]["persons"].append("npc1"), "new NPC")
    bad(lambda d: d["worldState"].update({"enabled":True}), "runtime enablement")
    bad(lambda d: d["evidenceContract"].update({"realSitePromotionsAllowedInR5":True}), "promotion")
    bad(lambda d: d["evidenceContract"].update({"requiresCertifiedGpForAccessibleSettlements":False}), "no Gp")
    bad(lambda d: d["adversarialCases"].pop(), "missing negative case")
    bad(lambda d: d["debts"][3].update({"state":"CLOSED"}), "EDD04 closed")
    return count


def main():
    check_documentation()
    data = load(DIR / "occupation_v0.6.json")
    r4 = load(EDR / "E19-R4/routes_v0.5.json")
    validate(data,r4)
    scenarios = test_scenarios()
    mutations = test_mutations(data,r4)
    print(f"E19-R5 PASS: {len(DOCS)} docs, {len(data['contexts'])} MF, "
          f"{len(data['studies'])} OS, {len(data['adversarialCases'])} anticasos; "
          f"{scenarios} synthetic cases + {mutations} rejected mutations; "
          "real sites=0, Sp=empty, B3/B4=false, parent R4 pinned")


if __name__ == "__main__":
    main()

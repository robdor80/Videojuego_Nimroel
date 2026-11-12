#!/usr/bin/env python3
"""D.P24 rural authorship static validation and adversarial mutation tests.
Not a CoreRPG runtime or a proof of physical settlements.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = TERR / "Datos operativos/darovan_dp24_rural_editorial_v0.1.json"
D01 = TERR / "Datos operativos/darovan_d01_relief_profile_v0.1.json"
D06 = TERR / "Datos operativos/darovan_d06_settlement_rules_v0.1.json"
DOC = TERR / "Profundizacion_2026/D.P24"

DOCS = {
    "futureCommunities": ("RUR-S", 9, "01_comunidades_y_paisajes.md"),
    "materialChains": ("RUR-C", 10, "03_oficios_economia_y_abastecimiento.md"),
    "biographyBases": ("RUR-N", 12, "04_personas_y_relaciones.md"),
    "relationshipIdeas": ("RUR-R", 6, "04_personas_y_relaciones.md"),
    "personalMemories": ("RUR-M", 4, "05_memorias_y_conflictos.md"),
    "conditionalArcs": ("RUR-H", 5, "05_memorias_y_conflictos.md"),
    "testOnlyScenes": ("RUR-E", 8, "06_escenas_rurales_multirrol.md"),
    "delegatedDecisions": ("DAR-DP24-", 9, "08_decisiones_editoriales_delegadas.md"),
}

def req(value, message):
    if not value:
        raise AssertionError(message)

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(d, *, check_files=False, d01=None, d06=None):
    req((d["schemaVersion"], d["documentId"], d["version"], d["phase"]) ==
        (1, "darovan_dp24_rural_editorial_v0.1", "0.1.0", "D.P24"),
        "schema/version/scope")
    req(d["status"] == "EDITORIAL_AUTHOR_DELEGATED_SELECTED_NO_PHYSICAL_INSTANCES",
        "unauthorized phase promotion")
    req(d["authority"] == "AUTHORED_EDITORIAL_BASE_NOT_WORLDSTATE" and
        d["delegation"] == "USER_EXPLICIT_CREATIVE_AUTONOMY_2026_11_12",
        "delegation scope")
    dep = d["merger"]
    req(dep == {"authorized": False, "baseBranch": "main",
                "baseCommit": "512434957f248f2513761615a9685ddd6c49c65f",
                "predecessorPhase": "D.P23", "predecessorPr": 46,
                "predecessorDraftWhenStarted": True,
                "dependsOnResolutionBeforeTerritorialClosure": True},
        "no implied permission to merge or skip D.P23")
    canon = d["inheritedCanon"]
    req(canon == {
        "kingdom": "Norgard", "territory": "Darovan",
        "cities": ["treihord","veldora","taramin","syvaris"],
        "excludedCity": "karsath", "arvenOwner": "casa_darovan",
        "arvenMantoVerdeCoverApproxPercent": 90,
        "arvenVillagesKnownGenerically": True,
        "arvenVillagesMostlyInnerCoast": True,
        "arvenNewSeaRouteAllowed": False,
        "agujaInteriorPermanentSettlements": False,
        "pilaresSingleForest": True, "taraminSingleForest": True,
        "belaraShallowIndustryOnly": True,
        "treihordCrisolDuplicatesAllowed": False,
        "royalNavyOfSyvarisAuthority": "CORONA_NORGARD",
        "internalCustomsCreated": False,
        "knownModalLinks": ["d05_road_veldora_treihord",
                            "d05_belara_shallow_haul", "d05_vena_restricted"]},
        "inherited canon changed")
    req(len(d["sourcePaths"]) >= 7 and len(set(d["sourcePaths"])) == len(d["sourcePaths"]),
        "sources missing or duplicated")
    req(set(d["lockedUnknowns"]) == {
        "communityLocations", "communityCoordinates", "totalRuralPopulation",
        "siteWaterSources", "siteRights", "localRouteGeometry",
        "bridgeAndFordLocations", "ruralServiceProviderIds", "actualLivestock",
        "actualCrops", "actualMineralFlows", "realHouseholdMembers",
        "materialChainActualQuantities", "travelTimes", "tradePrices",
        "settlementBuildingIds"} and
        all(x is None for x in d["lockedUnknowns"].values()),
        "unknown is not a fact")
    req(d["runtime"] == {
        "coreRpgIntegrated": False, "godotIntegrated": False,
        "generatedSettlements": 0, "instantiatedNpcs": 0,
        "activeQuests": 0, "worldStateChanged": False},
        "invented runtime effect")
    universe = set()
    for group, (prefix, count, doc) in DOCS.items():
        values = d[group]
        expected = [f"{prefix}{i:02d}" for i in range(1, count+1)]
        req(len(values) == count and [r["id"] for r in values] == expected,
            f"{group}: count, order or duplicate")
        for value in values:
            req(value["id"] not in universe, "cross-group duplicate")
            universe.add(value["id"])
        if check_files:
            target = DOC / doc
            req(target.is_file(), f"missing document: {doc}")
            body = target.read_text(encoding="utf-8")
            for value in values:
                req(value["id"] in body, f"missing textual trace: {value['id']}")
    if d01 is None:
        d01 = read(D01)
    if d06 is None:
        d06 = read(D06)
    zones = {z["id"]: z for z in d06["zones"]}
    models = {m["id"] for m in d06["models"]}
    req(set(zones) == {x["id"] for x in d01["physicalUnits"]} and
        len(zones) == 12 and len(models) == 9,
        "D01/D06 source universe diverged")
    for row in d["futureCommunities"]:
        req(row["studyZoneId"] in zones and row["conditionalD06ModelId"] in models,
            f"invalid D06 model/zone {row['id']}")
        req(zones[row["studyZoneId"]]["modelWeights"][row["conditionalD06ModelId"]] > 0,
            f"forbidden model for zone {row['id']}")
        req(row["studyZoneId"] != "d01_aguja_litoral", "Agujas residence")
        req(row["editorialStatus"] == "AUTHORED_EDITORIAL_BASE" and
            row["futureObjectiveOnly"] is True and row["instantiated"] is False and
            row["gatesPassed"] is False and row["physicalMapApproved"] is False,
            f"materialized community {row['id']}")
        for key in ("siteId", "geometry", "settlementClass",
                    "actualResidentCount", "waterSourceId", "verifiedLocalAccessId",
                    "verifiedRightsId", "worldStateEntityId"):
            req(row[key] is None, f"invented physical fact {row['id']} {key}")
        req(bool(row["name"]) and bool(row["limitation"]), "no rural identity/limit")
    req(d["futureCommunities"][2]["needsModelReassessmentIfEvidenceFails"] is True and
        all(row["needsModelReassessmentIfEvidenceFails"] is False
            for i, row in enumerate(d["futureCommunities"]) if i != 2),
        "Taramin dry-land fishing is conditional")
    for c in d["materialChains"]:
        req(c["status"] == "DESIGN_CONDITIONAL_NOT_ACTIVE" and
            c["realStockIds"] == [] and c["realProviderIds"] == [] and
            c["transactionIds"] == [] and c["realOutputQuantity"] is None and
            c["worldStateChanged"] is False, f"active/infinite supply {c['id']}")
    site_ids = {x["id"] for x in d["futureCommunities"]}
    people_ids = {x["id"] for x in d["biographyBases"]}
    req(len({r["name"] for r in d["biographyBases"]}) == 12, "duplicate biography name")
    for p in d["biographyBases"]:
        req(p["communityRef"] in site_ids and p["editorialStatus"] ==
            "AUTHORED_EDITORIAL_BASE" and p["biographyDoc"] ==
            "04_personas_y_relaciones.md" and p["npcInstantiated"] is False and
            p["knownWorldFacts"] == [], f"invalid biography {p['id']}")
        for k in ("personEntityId", "householdEntityId", "worldStateEntityId"):
            req(p[k] is None, f"unapproved NPC {p['id']}")
    for rel in d["relationshipIdeas"]:
        req(len(rel["personRefs"]) == 2 and len(set(rel["personRefs"])) == 2 and
            set(rel["personRefs"]) <= people_ids and
            rel["status"] == "FUTURE_CONDITIONAL_RELATION" and
            rel["actualRelationshipId"] is None, f"relationship {rel['id']}")
    for mem in d["personalMemories"]:
        req(mem["personRef"] in people_ids and
            mem["status"] == "AUTHORED_EDITORIAL_BASE_PRIVATE_MEMORY" and
            mem["publicHistory"] is False and mem["historicalDate"] is None and
            mem["worldStateMemoryId"] is None, f"fabricated public history {mem['id']}")
    for arc in d["conditionalArcs"]:
        req(set(arc["personRefs"]) <= people_ids and arc["personRefs"] and
            arc["status"] == "FUTURE_CONDITIONAL_ARC" and
            arc["activated"] is False and arc["triggerSatisfied"] is False and
            arc["worldStateQuestId"] is None, f"activated quest {arc['id']}")
    for scene in d["testOnlyScenes"]:
        req(scene["status"] == "TEST_ONLY" and
            scene["personRefs"] and set(scene["personRefs"]) <= people_ids and
            scene["completedInWorld"] is False and scene["worldStateEventId"] is None
            and scene["ledgerMutation"] is False and
            scene["unverifiedTravelAllowed"] is False,
            f"scene mutated world {scene['id']}")
    for dec in d["delegatedDecisions"]:
        req(dec["option"] == "A" and dec["status"] ==
            "EDITORIAL_SELECTED_UNDER_EXPLICIT_CREATIVE_DELEGATION" and
            dec["physicalMaterializationAuthorized"] is False,
            f"delegation exceeded {dec['id']}")
    if check_files:
        for path in d["sourcePaths"]:
            req((ROOT / path).is_file(), f"missing source {path}")
        for doc in ("README.md","02_hogares_tiempo_y_estaciones.md",
                    "07_autoridad_cartografia_y_traspaso.md"):
            req((DOC / doc).is_file(), f"missing D.P24 prose {doc}")
    return True

def negative_tests(d, d01, d06):
    mutants = [
        lambda x: x.update({"status":"IMPLEMENTED"}),
        lambda x: x["merger"].update({"authorized":True}),
        lambda x: x["merger"].update({"predecessorDraftWhenStarted":False}),
        lambda x: x["inheritedCanon"]["cities"].append("karsath"),
        lambda x: x["inheritedCanon"].update({"arvenOwner":"otro"}),
        lambda x: x["inheritedCanon"].update({"agujaInteriorPermanentSettlements":True}),
        lambda x: x["inheritedCanon"].update({"arvenNewSeaRouteAllowed":True}),
        lambda x: x["inheritedCanon"].update({"internalCustomsCreated":True}),
        lambda x: x["lockedUnknowns"].update({"bridgeAndFordLocations":"vado ficticio"}),
        lambda x: x["runtime"].update({"instantiatedNpcs":12}),
        lambda x: x["futureCommunities"][0].update({"siteId":"village_001"}),
        lambda x: x["futureCommunities"][0].update({"geometry":[1,2]}),
        lambda x: x["futureCommunities"][0].update({"gatesPassed":True}),
        lambda x: x["futureCommunities"][0].update({"studyZoneId":"d01_aguja_litoral"}),
        lambda x: x["futureCommunities"][2].update({"conditionalD06ModelId":"forestal_sostenible"}),
        lambda x: x["futureCommunities"][2].update({"needsModelReassessmentIfEvidenceFails":False}),
        lambda x: x["futureCommunities"][1].update({"id":"RUR-S01"}),
        lambda x: x["materialChains"][0]["realStockIds"].append("made_up"),
        lambda x: x["biographyBases"][0].update({"npcInstantiated":True}),
        lambda x: x["biographyBases"][0].update({"communityRef":"RUR-S99"}),
        lambda x: x["relationshipIdeas"][0]["personRefs"].append("RUR-N99"),
        lambda x: x["personalMemories"][0].update({"publicHistory":True}),
        lambda x: x["conditionalArcs"][0].update({"activated":True}),
        lambda x: x["testOnlyScenes"][0].update({"ledgerMutation":True}),
        lambda x: x["testOnlyScenes"][0].update({"unverifiedTravelAllowed":True}),
        lambda x: x["delegatedDecisions"][0].update({"physicalMaterializationAuthorized":True}),
    ]
    for i, mutation in enumerate(mutants, start=1):
        changed = copy.deepcopy(d)
        mutation(changed)
        try:
            validate(changed, d01=d01, d06=d06)
        except (AssertionError, KeyError):
            continue
        raise AssertionError(f"adversarial mutation {i} escaped")
    return len(mutants)

def main():
    d, d01, d06 = read(DATA), read(D01), read(D06)
    validate(d, check_files=True, d01=d01, d06=d06)
    count = negative_tests(d, d01, d06)
    print(f"PASS D.P24: valid documentary contract + {count} rejected adversarial mutations")
    print("No claims of executed rural settlements, CoreRPG or Godot runtime.")

if __name__ == "__main__":
    main()

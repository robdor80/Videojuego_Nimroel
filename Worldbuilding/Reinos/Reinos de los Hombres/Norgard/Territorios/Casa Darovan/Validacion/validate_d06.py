#!/usr/bin/env python3
"""D06 regression: source contracts, noncanonical generator, positive/negative tests."""
from __future__ import annotations

import copy
import json
from pathlib import Path

from d06_generator import IneligibleSite, generate_test_design, stable_id, weighted_choice

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
CITIES = ["treihord", "veldora", "taramin", "syvaris"]
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
MODELS = {
    "agricola", "ganadera", "pesquera", "minera_auxiliar",
    "metalurgica_auxiliar", "forestal_sostenible", "servicio_camino",
    "insular_mixta", "enclave_especializado",
}
EXPECTED_RULES = {
    "insideBosqueAgujasPermanent": False,
    "taraminIndustrialForestry": False,
    "syvarisIntensiveForestry": False,
    "arvenTimberIndustrial": False,
    "arvenNewRouteAutomatic": False,
    "newMinorHarbourAutomatic": False,
    "riverNavigationAutomatic": False,
    "d05SupplyEdgesAreRoads": False,
    "cityGenerationAllowed": False,
    "autoPromoteWorksiteToVillage": False,
    "customsBetweenNorgardGreatHouses": False,
}


def check(test: bool, reason: str) -> None:
    if not test:
        raise AssertionError(reason)


def read(repo: Path, path: str) -> dict:
    return json.loads((repo / path).read_text(encoding="utf-8"))


def validate_rules(r: dict, repo: Path) -> None:
    check(r["schemaVersion"] == 1 and r["documentId"] == "darovan_d06_settlement_design_rules"
          and r["version"] == "0.1" and r["phase"] == "D06"
          and r["generatorVersion"] == "d06-lab-0.1", "D06 schema and version")
    check(r["status"] == "planning_reference_not_runtime"
          and r["canonStatus"] == "no_new_settlements_or_toponyms"
          and r["provenance"] == "PROPOSAL" and r["authorityChain"] == AUTH,
          "non-runtime authority")
    check(r["manualCityIds"] == CITIES and r["excludedCityIds"] == ["karsath"],
          "canonical cities protected")
    check(r["administration"]["arven"] == r["administration"]["syvaris"] == "casa_darovan"
          and r["administration"]["otherStudyUnits"] == "verify_site_jurisdiction_no_polygon",
          "Arven / jurisdiction")
    check(r["hydro"]["namedRivers"] == ["belara","lhera","veldora","fhalion","thalen"]
          and r["hydro"]["systems"] == ["belara_lhera","veldora","fhalion","thalen"]
          and r["hydro"]["fhalionNavigation"] is None
          and r["hydro"]["thalenNavigation"] is None
          and r["hydro"]["belaraDeepDraftAllowed"] is False, "river protection")
    check(r["specialConstraints"] == EXPECTED_RULES, "mandatory prohibition weakened")
    check(set(r["proposalForbiddenFlags"]) >= {
        "insideAgujasInterior", "inCanonicalCityFootprint", "claimsOfficialToponym",
        "claimsNewRoute", "claimsNewHarbour", "claimsRiverNavigation",
        "claimsBelaraDeepDraft", "claimsInternalCustoms", "claimsDarovanNavy",
        "claimsCanonicalSettlement", "containsMapCoordinates", "claimsFixedPopulation",
        "claimsFixedDistance",
    }, "proposal flags incomplete")
    check(set(r["globalRequiredEvidence"]) == {
        "habitable_ground_verified", "potable_water_verified",
        "local_access_verified", "livelihood_viable_verified",
        "local_jurisdiction_verified",
    }, "mandatory evidence missing")
    check(r["versioning"]["stableIdAlgorithm"] == "sha256_utf8_prefix16"
          and r["versioning"]["modelDecisionAlgorithm"] == "sha256_8byte_weighted_sorted"
          and r["versioning"]["visibleNameAffectsId"] is False
          and r["versioning"]["existingSaveAutoReroll"] is False,
          "identity and save stability")
    check(r["runtimeIntegration"] == {
        "status": "not_implemented", "coreRpgPersisted": False, "godotSpawned": False,
        "gisVerified": False, "generatedCanonicalSettlements": 0,
    }, "fictitious runtime completion")
    refs = r["sourceRefs"]
    check(set(refs) == {"d01","d02","d03","d04","d05","coreGeography","norgardFiscal","forests","rivers"}
          and all(str(p).startswith("Worldbuilding/") and (repo / p).is_file()
                  for p in refs.values()), "source references broken")
    d01, d02, d03, d04, d05 = [read(repo, refs["d0" + str(i)]) for i in range(1,6)]
    core, fiscal = read(repo, refs["coreGeography"]), read(repo, refs["norgardFiscal"])
    check(core["status"] == "active_core_contract"
          and core["immutableRules"]["materializedGeometryPersists"], "Core geography contract")
    check(fiscal["fiscalUnity"]["customsBetweenGreatHouseTerritories"] is False,
          "Norgard fiscal contract")
    check([city["id"] for city in d01["cityAnchors"]] == CITIES
          and d01["administration"]["arvenIslandOwner"] == "casa_darovan", "D01 correction")
    check([x["id"] for x in d02["rivers"]] == r["hydro"]["namedRivers"]
          and [x["id"] for x in d02["systems"]] == r["hydro"]["systems"]
          and d02["rivers"][0]["crossesCity"] is False
          and d02["rivers"][1]["branchesFrom"] == "belara"
          and d02["rivers"][4]["terminalArms"] == 2
          and len(d02["conceptualGraph"]["nodes"]) == 15
          and len(d02["conceptualGraph"]["edges"]) == 11, "D02 graph updated")
    check(d03["regionalAnchors"]["permanentSettlementsInsideAgujasAllowed"] is False
          and d03["regionalAnchors"]["arvenOwner"] == "casa_darovan"
          and d03["regionalAnchors"]["syvarisForestsDiscontinuous"] is True, "D03 forest protection")
    check(d04["forestProtection"]["agujasPermanentInteriorSettlementsAllowed"] is False
          and d04["forestProtection"]["taraminIndustrialLoggingAllowed"] is False
          and d04["forestProtection"]["syvarisIntensiveForestryAllowed"] is False
          and d04["geographyProtection"]["arvenOwner"] == "casa_darovan"
          and len(d04["resourceChains"]) == 8, "D04 economy")
    check(len(d05["confirmedTransportLinks"]) == 3
          and len(d05["supplyRelationsNotRoutes"]) == 4
          and d05["movementSemantics"]["arvenHasDarovanRoute"] is False
          and d05["movementSemantics"]["fhalionRiverNavigability"] is None
          and d05["movementSemantics"]["graphContainsOnlyAttestedConnections"] is True,
          "D05 not a travel planner")
    zones = r["zones"]
    ids = [z["id"] for z in zones]
    check(len(ids) == 12 and len(set(ids)) == 12
          and set(ids) == {x["id"] for x in d01["physicalUnits"]}
          == {x["id"] for x in d03["zones"]}
          == {x["id"] for x in d04["studyUnits"]}, "D01–D04 regional references")
    models = r["models"]
    mids = [m["id"] for m in models]
    check(len(mids) == len(MODELS) and set(mids) == MODELS, "model coverage")
    check(r["enclavePromotionRequires"] == "resident_community_justified_verified",
          "installation is not automatically settlement")
    for m in models:
        check(set(m["classes"]) <= {"aldea", "pueblo", "villa", "enclave"}
              and m["classes"] and len(m["classes"]) == len(set(m["classes"]))
              and len(m["requiredEvidence"]) >= 2
              and len(m["requiredEvidence"]) == len(set(m["requiredEvidence"]))
              and m["automaticBuildings"] == [] and m["automaticServices"] == []
              and m["buildingPossibilities"] and m["servicePossibilities"],
              "model prerequisites and non-instantiated optional content")
    for z in zones:
        check(z["class"] == "qualitative_study_unit_not_polygon"
              and z["jurisdictionAtSpecificSite"] == "UNKNOWN_until_validated"
              and z["siteSelectionEnabled"] is False
              and z["weightsMeaning"] == "relative_design_priority_not_frequency_or_population",
              "region is not spatially materialized")
        ws = z["modelWeights"]
        check(set(ws) == MODELS and all(type(v) is int and 0 <= v <= 4 for v in ws.values()),
              "invalid regional design weights")
        if z["id"] == "d01_aguja_litoral":
            check(all(v == 0 for v in ws.values()), "Agujas interior exclusion")
        if z["id"] in {"d01_taramin_norte_centro","d01_taramin_bosque_sur"}:
            check(ws["metalurgica_auxiliar"] == ws["minera_auxiliar"] == 0,
                  "no industrial mining/metal from regional inference")
        if z["id"] in {"d01_arven_contexto","d01_syvaris"}:
            check(ws["metalurgica_auxiliar"] == ws["minera_auxiliar"] == 0,
                  "no island industrial extractions by default")
        if z["id"] == "d01_elyra_paso_peninsular":
            check(ws["minera_auxiliar"] == 0, "Elyra ownership uncertain")
    check((repo / (ROOT + "Asentamientos/01_ESQUELETO_Y_MODELOS_D06_v0.1.md")).is_file()
          and (repo / (ROOT + "Asentamientos/02_PESOS_Y_GENERACION_D06_v0.1.md")).is_file()
          and (repo / (ROOT + "Asentamientos/03_INSTANCIAS_SEMILLAS_D06_v0.1.md")).is_file(),
          "methodology documents absent")


def run() -> None:
    here = Path(__file__).resolve()
    repo = next((p for p in here.parents if (p / "Worldbuilding").is_dir()), None)
    check(repo is not None, "repository checkout missing")
    original = read(repo, ROOT + "Datos operativos/darovan_d06_settlement_rules_v0.1.json")
    fixtures = read(repo, ROOT + "Datos operativos/darovan_d06_test_fixtures_v0.1.json")
    validate_rules(original, repo)
    check(fixtures["schemaVersion"] == 1 and fixtures["status"] == "synthetic_test_only_noncanonical"
          and len(fixtures["scenarios"]) == 6, "fixture provenance")
    generated = []
    for sample in fixtures["scenarios"]:
        a = generate_test_design(original, sample, fixtures["seed"])
        b = generate_test_design(original, copy.deepcopy(sample), fixtures["seed"])
        check(a == b and a["canonical"] is False and a["materialized"] is False
              and a["modelId"] == sample["allowedModel"]
              and a["coordinates"] is None and a["visibleName"] is None
              and a["population"] is None and a["worldStateId"] is None
              and a["connectedRoutes"] == [] and a["serviceInstances"] == []
              and a["buildingInstances"] == [], "noncanonical seeded sample")
        generated.append(a)
    check(len({a["id"] for a in generated}) == 6, "duplicate generated IDs")
    first = fixtures["scenarios"][0]
    check(generate_test_design(original, first, fixtures["seed"] + "-other")["id"] != generated[0]["id"],
          "seed not reflected in identity")
    check(stable_id(fixtures["seed"], first["studyZoneId"], first["slotId"]) == generated[0]["id"],
          "stable derivation")
    choose = weighted_choice(fixtures["seed"], generated[0]["id"], original["version"],
                             [("ganadera",2),("forestal_sostenible",4)])
    check(choose == weighted_choice(fixtures["seed"], generated[0]["id"], original["version"],
                                    [("forestal_sostenible",4),("ganadera",2)]),
          "model tie/weight ordering unstable")
    bad_rules = [
        ("city_deleted",lambda x:x["manualCityIds"].pop()),
        ("arven_unknown",lambda x:x["administration"].update(arven=None)),
        ("fhalion_deleted",lambda x:x["hydro"]["namedRivers"].remove("fhalion")),
        ("hydro_invented",lambda x:x["hydro"]["systems"].append("invented_river")),
        ("agujas_enabled",lambda x:x["zones"][3]["modelWeights"].update(agricola=1)),
        ("site_auto_enabled",lambda x:x["zones"][7].update(siteSelectionEnabled=True)),
        ("weight_illegal",lambda x:x["zones"][7]["modelWeights"].update(agricola=99)),
        ("model_not_stable",lambda x:x["models"][0].update(id="invented_model")),
        ("class_city",lambda x:x["models"][0]["classes"].append("ciudad")),
        ("buildings_spawn",lambda x:x["models"][0]["automaticBuildings"].append("house")),
        ("no_model_proof",lambda x:x["models"][0]["requiredEvidence"].clear()),
        ("road_supply_promoted",lambda x:x["specialConstraints"].update(d05SupplyEdgesAreRoads=True)),
        ("fishing_navigation",lambda x:x["specialConstraints"].update(riverNavigationAutomatic=True)),
        ("taxes",lambda x:x["specialConstraints"].update(customsBetweenNorgardGreatHouses=True)),
        ("taramin_industrial",lambda x:x["specialConstraints"].update(taraminIndustrialForestry=True)),
        ("syvaris_industrial",lambda x:x["specialConstraints"].update(syvarisIntensiveForestry=True)),
        ("fake_runtime",lambda x:x["runtimeIntegration"].update(godotSpawned=True)),
        ("bad_reference",lambda x:x["sourceRefs"].update(d02="Worldbuilding/no_such_file.json")),
        ("territory_new",lambda x:x["zones"].append(copy.deepcopy(x["zones"][0]))),
        ("elyra_mine",lambda x:x["zones"][1]["modelWeights"].update(minera_auxiliar=2)),
    ]
    for name, mutate in bad_rules:
        test = copy.deepcopy(original)
        mutate(test)
        try:
            validate_rules(test, repo)
        except (AssertionError, KeyError, TypeError):
            continue
        raise AssertionError("accepted invalid rules mutation: " + name)
    bad_sites = [
        ("no_water",lambda x:x["evidence"].remove("potable_water_verified")),
        ("no_access",lambda x:x["evidence"].remove("local_access_verified")),
        ("no_jurisdiction",lambda x:x["evidence"].remove("local_jurisdiction_verified")),
        ("no_sustainability",lambda x:x["evidence"].remove("sustainable_harvest_verified")),
        ("no_economy",lambda x:x["evidence"].remove("livelihood_viable_verified")),
        ("no_rights",lambda x:x["evidence"].remove("forest_use_rights_verified")),
        ("agujas",lambda x:x.update(studyZoneId="d01_aguja_litoral")),
        ("city_class",lambda x:x.update(settlementClass="ciudad")),
        ("city_claim",lambda x:x.update(claimedCity="treihord")),
        ("canonical_claim",lambda x:x.update(canonical=True)),
        ("official_name",lambda x:x.update(visibleName="NewTown")),
        ("invented_route",lambda x:x["flags"].append("claimsNewRoute")),
        ("invented_harbour",lambda x:x["flags"].append("claimsNewHarbour")),
        ("internal_customs",lambda x:x["flags"].append("claimsInternalCustoms")),
        ("deep_belara",lambda x:x["flags"].append("claimsBelaraDeepDraft")),
        ("fake_coordinates",lambda x:x.update(coordinates=[1,2])),
        ("non_synthetic",lambda x:x.update(fixtureKind="canonical")),
        ("duplicate_proof",lambda x:x["evidence"].append("habitable_ground_verified")),
        ("unknown_region",lambda x:x.update(studyZoneId="d01_not_found")),
        ("unknown_model",lambda x:x.update(allowedModel="unknown_model")),
        ("unauthorized_geometry_field",lambda x:x.update(routeGeometry=[[1,2],[3,4]])),
    ]
    special = copy.deepcopy(fixtures["scenarios"][2])
    special["evidence"].remove("resident_community_justified_verified")
    try:
        generate_test_design(original,special,fixtures["seed"])
    except IneligibleSite:
        pass
    else:
        raise AssertionError("worksite promoted to resident settlement without proof")
    for name, mutate in bad_sites:
        test = copy.deepcopy(first)
        mutate(test)
        try:
            generate_test_design(original,test,fixtures["seed"])
        except (IneligibleSite, ValueError, TypeError):
            continue
        raise AssertionError("accepted invalid site mutation: " + name)
    print(f"D06 STATIC OK: {len(fixtures['scenarios'])} positive fixtures, "
          f"{len(bad_rules)} negative rules, {len(bad_sites)+1} negative sites, "
          "D01-D05 cross-checks; NO RUNTIME")


if __name__ == "__main__":
    run()

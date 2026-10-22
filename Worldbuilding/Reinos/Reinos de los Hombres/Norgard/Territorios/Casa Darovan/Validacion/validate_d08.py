#!/usr/bin/env python3
"""DAROVAN D08: canonical guardrails and negative regression. STATIC ONLY."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
DATA = ROOT + "Datos operativos/darovan_d08_population_services_v0.1.json"
FIXTURES = ROOT + "Datos operativos/darovan_d08_test_fixtures_v0.1.json"
SCHEMA = ROOT + "Datos operativos/darovan_d08_population_services.schema.json"
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
CITY_IDS = ["treihord", "veldora", "taramin", "syvaris"]
FOCUS = {
    "treihord": ["industria_metalurgica", "ensayo_refinado_crisol_no_ceca",
                 "logistica_mineral_carros_barcas_someras", "servicios_urbanos"],
    "veldora": ["comercio_exterior", "aduana_exterior_corona", "almacenaje",
                "talleres", "sectores_comerciales_organicos"],
    "taramin": ["pesca_maritima_y_fluvial", "productos_marinos", "aceites",
                "zona_pesquera_principal_sin_ubicacion"],
    "syvaris": ["pesca", "productos_marinos_y_aceites", "comercio",
                "actividad_bahia_principal", "presencia_naval_norgard_no_darovan"],
}
CITY_CONCEPT = {"treihord": "CANON_DISENO_BASE_CERRADO",
                "veldora": "APPROVED_CONCEPT_ONLY_B",
                "taramin": "APPROVED_CONCEPT_ONLY_A",
                "syvaris": "APPROVED_CONCEPT_ONLY_A"}
EXPECTED_SERVICES = ["alimentacion", "agua", "higiene_y_residuos",
                     "cuidados", "salud", "aprendizaje", "alojamiento",
                     "transporte", "mantenimiento", "comercio_y_abastecimiento"]
EXPECTED_PROFESSIONS = ["agricultura", "ganaderia", "mineria", "metalurgia", "artesania",
                        "pesca_taramin", "pesca_syvaris", "comercio_veldora",
                        "transporte", "servicios_domesticos", "salud_y_cuidados",
                        "aprendizaje"]
EXPECTED_FIXTURES = ["t01_unrelated_cotenant", "t02_married_separate",
                     "t03_apprentice_13", "t04_youth_worker_16",
                     "t05_care_gap", "t06_no_synthetic_route", "t07_no_inventory_spawn"]
TOP = {"schemaVersion", "documentId", "version", "phase", "preparedAt",
       "status", "canonStatus", "authorityChain", "sourceRefs", "coreRpgAudit",
       "manualCityIds", "excludedCityIds", "cities", "settlementProfiles",
       "householdModel", "occupationFamilies", "serviceNeeds", "causalFlow",
       "planningUnknowns", "authorialApprovalRequiredFor", "runtimeIntegration"}

def check(pred: bool, message: str) -> None:
    if not pred:
        raise AssertionError(message)

def read(repo: Path, path: str) -> dict:
    return json.loads((repo / path).read_text(encoding="utf-8"))

def validate(data: dict, fixtures: dict, repo: Path) -> None:
    check(set(data) == TOP and data["schemaVersion"] == 1
          and data["documentId"] == "darovan_d08_household_population_services"
          and data["phase"] == "D08" and data["version"] == "0.1"
          and data["status"] == "planning_reference_not_runtime"
          and data["canonStatus"] == "approved_veldora_taramin_population_ranges_no_new_entities_or_institutions"
          and data["authorityChain"] == AUTH, "schema, phase, authority")
    schema = read(repo, SCHEMA)
    check(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
          and set(schema["required"]) == TOP
          and set(schema["properties"]) == TOP
          and schema["additionalProperties"] is False, "D08 JSON Schema mismatch")
    source = data["sourceRefs"]
    check(len(source) == 27 and all(isinstance(k, str) and isinstance(v, str)
          and (repo / v).is_file() and v.startswith("Worldbuilding/")
          for k, v in source.items()), "missing/redirected D08 sources")
    for k in ["d04", "d05", "d06", "d07", "treihord", "rural", "family",
              "labor", "property", "health", "fiscal", "currency", "maritime",
              "res", "kin", "care", "chore", "emp", "apr", "need", "wait",
              "txn", "own", "food", "waste", "decisionD0801", "decisionD0801Taramin"]:
        check(k in source, "missing source key: " + k)
    d04, d06, d07 = (read(repo, source[k]) for k in ("d04", "d06", "d07"))
    check(d07["manualCityIds"] == CITY_IDS
          and d06["manualCityIds"] == CITY_IDS, "D06/D07 city registry changed")
    check(data["manualCityIds"] == CITY_IDS and data["excludedCityIds"] == ["karsath"]
          and d07["otherDarovanIsland"] == "arven", "cities or jurisdiction")
    chains = {r["id"] for r in d04["resourceChains"]}
    models = {m["id"]: set(m["classes"]) for m in d06["models"]}
    check(len(models) == 9 and len(chains) == 8, "D04/D06 source drift")
    cities = data["cities"]
    check(len(cities) == 4 and [x["id"] for x in cities] == CITY_IDS,
          "duplicate/extra/city deleted")
    check([x["id"] for x in d07["cities"]] == CITY_IDS,
          "D07 reference unexpectedly changed")
    canonical_treihord = {f["id"]: f["value"] for f in d07["cities"][0]["facts"]}
    check(canonical_treihord["population_approx_approved"] == 32000,
          "D07 Treihord canon drift")
    for city in cities:
        cid = city["id"]
        check(set(city) == {"id", "populationApprox", "populationStatus",
              "populationRange", "economicFocus", "d04Chains", "conceptStatus", "householdCount",
              "occupationCounts", "serviceCapacity", "workforceShare",
              "physicalServicesRegistered", "newBuildingsApproved", "geometry",
              "travelTimes", "sourceRefIds", "provenance", "studyOnly"},
              "city illegal fields or missing protections")
        check(city["economicFocus"] == FOCUS[cid]
              and city["conceptStatus"] == CITY_CONCEPT[cid]
              and set(city["d04Chains"]).issubset(chains)
              and len(city["d04Chains"]) >= 1
              and city["sourceRefIds"] == (["d07", "d04", "decisionD0801"] if cid == "veldora" else
                  ["d07", "d04", "decisionD0801Taramin"] if cid == "taramin" else ["d07", "d04"])
              and city["provenance"] == "DERIVED" and city["studyOnly"] is True,
              "invented city profession or concept change")
        check(city["populationApprox"] == (32000 if cid == "treihord" else None)
              and city["populationStatus"] == (
                "AUTHORED_APPROX" if cid == "treihord" else
                "AUTHORED_RANGE" if cid in ("veldora", "taramin") else "UNKNOWN")
              and all(city[k] is None for k in ["householdCount", "occupationCounts",
                        "serviceCapacity", "workforceShare", "geometry", "travelTimes"])
              and city["physicalServicesRegistered"] == []
              and city["newBuildingsApproved"] is False,
              "false demographic, services, housing or physical capacity")
        expected_range = {
            "minInclusive": 29000, "maxInclusive": 35000, "unit": "habitantes",
            "status": "APPROVED_AUTHOR_RANGE", "decisionId": "DAR-D08-01",
            "option": "B", "provenance": "AUTHORED", "sourceRefId": "decisionD0801",
            "approvalScope": "demographic_reference_range_only_no_exact_count",
        } if cid == "veldora" else {
            "minInclusive": 14000, "maxInclusive": 20000, "unit": "habitantes",
            "status": "APPROVED_AUTHOR_RANGE", "decisionId": "DAR-D08-01",
            "option": "B", "provenance": "AUTHORED",
            "sourceRefId": "decisionD0801Taramin",
            "approvalScope": "demographic_reference_range_only_no_exact_count",
        } if cid == "taramin" else None
        check(city["populationRange"] == expected_range, "D08-01 population interval or city scope")
        if cid == "veldora":
            decision_text = (repo / source["decisionD0801"]).read_text(encoding="utf-8")
            check("DAR-D08-01" in decision_text and "29.000" in decision_text
                  and "35.000" in decision_text and "Opción B" in decision_text,
                  "D08-01 decision provenance missing")
        if cid == "taramin":
            decision_text = (repo / source["decisionD0801Taramin"]).read_text(encoding="utf-8")
            check("DAR-D08-01" in decision_text and "14.000" in decision_text
                  and "20.000" in decision_text and "Opción B" in decision_text,
                  "D08-01 Taramin decision provenance missing")
    check(cities[2]["populationRange"]["maxInclusive"] <
          cities[1]["populationRange"]["minInclusive"], "Taramin must be below Veldora")
    check(cities[2]["populationRange"]["maxInclusive"] < 32000,
          "Taramin must be below approved Treihord approximate population")
    profiles = data["settlementProfiles"]
    check([p["tier"] for p in profiles] == ["aldea", "pueblo", "villa", "enclave"],
          "settlement tiers")
    for p in profiles:
        check(set(p) == {"tier", "modelExamples", "demographicBand",
              "householdsPerSite", "serviceQuota", "actualSettlements",
              "evidenceGate", "provenance", "testModelsOnly"},
              "settlement profile unapproved field")
        check(bool(p["modelExamples"]) and len(p["modelExamples"]) == len(set(p["modelExamples"]))
              and all(x in models and p["tier"] in models[x] for x in p["modelExamples"])
              and p["demographicBand"] is None and p["householdsPerSite"] is None
              and p["serviceQuota"] is None and p["actualSettlements"] == []
              and p["evidenceGate"] == "D06_site_specific_evidence_required"
              and p["provenance"] == "DERIVED" and p["testModelsOnly"] is True,
              "D06 model mismatch or false population")
    household = data["householdModel"]
    check(set(household) == {"provenance", "patterns", "patternsAreNotSocialCasteOrCanonicalHouseholdShares",
          "householdCount", "meanPersonsPerHousehold", "ageShares", "ruralUrbanShares",
          "headOfHouseholdDefault", "sexBasedChoresDefault", "marriageImpliesCoResidence",
          "coResidenceImpliesMarriage", "kinshipImpliesCare", "ownershipImpliesResidence",
          "movingHouseMovesBusiness", "populationMaterializesAutomatically",
          "typesOfRelations", "childAgeBandsFromNorgard", "adultAgeMin",
          "apprenticeshipMinAge", "youthEmploymentMinAge", "provenanceOfAgeBands"},
          "unknown or inserted household social rule")
    check(household["patterns"] == ["one_resident", "related_co_residents",
          "unrelated_co_residents", "temporary_separation"]
          and household["patternsAreNotSocialCasteOrCanonicalHouseholdShares"] is True
          and household["provenance"] == "DERIVED"
          and all(household[k] is None for k in ["householdCount",
                "meanPersonsPerHousehold", "ageShares", "ruralUrbanShares",
                "headOfHouseholdDefault"])
          and all(household[k] is False for k in ["sexBasedChoresDefault",
                "marriageImpliesCoResidence", "coResidenceImpliesMarriage",
                "kinshipImpliesCare", "ownershipImpliesResidence",
                "movingHouseMovesBusiness", "populationMaterializesAutomatically"])
          and household["adultAgeMin"] == 18
          and household["apprenticeshipMinAge"] == 12
          and household["youthEmploymentMinAge"] == 15
          and household["childAgeBandsFromNorgard"] == [[0,7],[8,11],[12,14],[15,17]]
          and household["provenanceOfAgeBands"] == "AUTHORED"
          and household["typesOfRelations"] == ["RES", "MOVE", "KIN", "CARE",
                "CHORE", "EMP", "APR", "OWN", "TXN"], "family, labor or household canon changed")
    jobs = data["occupationFamilies"]
    check([j["family"] for j in jobs] == EXPECTED_PROFESSIONS,
          "missing/extraneous occupation family")
    for j in jobs:
        check(set(j) == {"family", "d04Chain", "gate", "formalGuildCreated",
                        "canonicalJobCount", "contractorCount", "provenance", "personIds"}
              and (j["d04Chain"] is None or j["d04Chain"] in chains)
              and isinstance(j["gate"], str) and len(j["gate"]) > 8
              and j["formalGuildCreated"] is False
              and j["canonicalJobCount"] is None and j["contractorCount"] is None
              and j["provenance"] == "DERIVED" and j["personIds"] == [],
              "fabricated job, guild or person")
    services = data["serviceNeeds"]
    check([s["id"] for s in services] == EXPECTED_SERVICES,
          "missing or invented service type")
    for s in services:
        check(set(s) == {"id", "needType", "evidenceGate", "providerPattern",
                "sourceRefIds", "coverageRule", "actualBuildings", "providerCount",
                "effectiveCapacity", "serviceTravelTime", "provenance", "autoCreateProvider"}
              and isinstance(s["evidenceGate"], str) and s["evidenceGate"]
              and isinstance(s["providerPattern"], str) and s["providerPattern"]
              and bool(s["sourceRefIds"]) and all(k in source for k in s["sourceRefIds"])
              and s["coverageRule"] == "must_evaluate_not_assume_facility"
              and s["actualBuildings"] == []
              and all(s[k] is None for k in ["providerCount","effectiveCapacity","serviceTravelTime"])
              and s["provenance"] == "DERIVED" and s["autoCreateProvider"] is False,
              "new building, provider or service capacity")
    flow = data["causalFlow"]
    check(flow["phases"] == ["need_or_demand", "check_people_skills_availability",
          "check_rights_resources_stock", "check_verified_access_time_capacity",
          "perform_authorized_transaction_or_service", "persist_change_in_world_state"]
          and flow["requireNonnegativeStock"] is True
          and flow["providerNotCreatedByDemand"] is True
          and flow["unservedNeedsCanPersist"] is True
          and flow["absenceDoesNotCreateReplacement"] is True
          and flow["waitingNotAlwaysFIFO"] is True
          and flow["noInstantPlayerPriority"] is True
          and flow["doNotUseD05SupplyDependencyAsRoad"] is True,
          "invalid causal flow or fictional route/inventory")
    audit = data["coreRpgAudit"]
    check(audit["repository"] == "robdor80/CoreRPG"
          and audit["scope"] == "audited_repository_contracts_not_executable_D08_integration"
          and audit["numericRelationKindIds"] is None
          and len(audit["checkedFiles"]) >= 5
          and "household_family_rules" in audit["notImplementedAsNativeCoreMechanics"]
          and "WorldState" in audit["implementedPrimitives"],
          "CoreRPG API or integration claimed beyond evidence")
    runtime = data["runtimeIntegration"]
    check(runtime == {"coreRpgExecuted": False, "godotExecuted": False,
          "populationEntitiesInstantiated": 0, "householdsInstantiated": 0,
          "physicalServicesInstantiated": 0, "kindNumericRegistryApproved": False},
          "runtime integration falsely claimed")
    check("veldora_exact_population" in data["planningUnknowns"]
          and "veldora_population" not in data["planningUnknowns"]
          and "taramin_exact_population" in data["planningUnknowns"]
          and "taramin_population" not in data["planningUnknowns"]
          and "syvaris_population" in data["planningUnknowns"]
          and "total_darovan_population" in data["planningUnknowns"]
          and "all_household_counts" in data["planningUnknowns"]
          and "new_social_categories" in data["authorialApprovalRequiredFor"]
          and "new_canonical_population_bands" in data["authorialApprovalRequiredFor"],
          "unknown and authorial approvals dropped")

    check(set(fixtures) == {"schemaVersion", "documentId", "phase", "status",
            "noNewCanonicalSettlements", "usesOnlySyntheticLocations",
            "allowedLocationPrefix", "createdNpcCountInWorldState", "cases"}
          and fixtures["schemaVersion"] == 1
          and fixtures["documentId"] == "darovan_d08_test_only_cases"
          and fixtures["phase"] == "D08" and fixtures["status"] == "TEST_ONLY_NOT_CANON"
          and fixtures["noNewCanonicalSettlements"] is True
          and fixtures["usesOnlySyntheticLocations"] is True
          and fixtures["allowedLocationPrefix"] == "TEST_ONLY_"
          and fixtures["createdNpcCountInWorldState"] == 0,
          "fixture promoted into canon/runtime")
    cases = fixtures["cases"]
    check([t["id"] for t in cases] == EXPECTED_FIXTURES,
          "fixtures changed or duplicated")
    all_person_ids, all_household_ids = set(), set()
    for t in cases:
        check(set(t) == {"id","site","scenario","persons","households","expected"}
              and t["site"].startswith("TEST_ONLY_")
              and t["site"] not in CITY_IDS
              and isinstance(t["scenario"],str) and bool(t["scenario"])
              and isinstance(t["expected"],str) and bool(t["expected"]),
              "fictional canonical locality / malformed test")
        pids = set()
        for p in t["persons"]:
            check(set(p) == {"id","age"} and p["id"].startswith("TEST_ONLY_")
                  and type(p["age"]) is int and 0 <= p["age"] <= 120
                  and p["id"] not in all_person_ids, "fixture person's IDs/age")
            pids.add(p["id"]); all_person_ids.add(p["id"])
        for h in t["households"]:
            check(set(h) == {"id","members"} and h["id"].startswith("TEST_ONLY_")
                  and h["id"] not in all_household_ids
                  and h["members"] and set(h["members"]).issubset(pids)
                  and len(h["members"]) == len(set(h["members"])),
                  "fixture household ID or invalid member")
            all_household_ids.add(h["id"])
    check(len(all_person_ids) == 8 and len(all_household_ids) == 6,
          "unexpected synthetic person/household counts")
    check(cases[2]["persons"][0]["age"] == 13
          and cases[3]["persons"][0]["age"] == 16,
          "apprentice/youth negative scenario invalid")

def run() -> None:
    repo = next((p for p in Path(__file__).resolve().parents if (p / DATA).is_file()), None)
    check(repo is not None, "cannot locate complete repository checkout")
    data, fixtures = read(repo, DATA), read(repo, FIXTURES)
    validate(data, fixtures, repo)
    mutations = [
        ("false_runtime", "d", lambda x: x["runtimeIntegration"].update(coreRpgExecuted=True)),
        ("invented_pop", "d", lambda x: x["cities"][1].update(populationApprox=42000)),
        ("veldora_range_min_mutated", "d", lambda x: x["cities"][1]["populationRange"].update(minInclusive=28000)),
        ("veldora_range_max_mutated", "d", lambda x: x["cities"][1]["populationRange"].update(maxInclusive=36000)),
        ("veldora_range_revoked", "d", lambda x: x["cities"][1].update(populationRange=None)),
        ("veldora_range_fabricated_on_taramin", "d", lambda x: x["cities"][2].update(populationRange=copy.deepcopy(x["cities"][1]["populationRange"]))),
        ("veldora_range_provenance_lost", "d", lambda x: x["cities"][1]["populationRange"].update(provenance="DERIVED")),
        ("veldora_range_claims_exact_pop", "d", lambda x: x["cities"][1].update(populationApprox=32000)),
        ("veldora_range_status_wrong", "d", lambda x: x["cities"][1].update(populationStatus="UNKNOWN")),
        ("veldora_range_source_unlinked", "d", lambda x: x["cities"][1].update(sourceRefIds=["d07", "d04"])),
        ("veldora_range_source_deleted", "d", lambda x: x["sourceRefs"].pop("decisionD0801")),

        ("taramin_range_min_mutated", "d", lambda x: x["cities"][2]["populationRange"].update(minInclusive=13000)),
        ("taramin_range_max_mutated", "d", lambda x: x["cities"][2]["populationRange"].update(maxInclusive=21000)),
        ("taramin_range_revoked", "d", lambda x: x["cities"][2].update(populationRange=None)),
        ("taramin_range_fabricated_on_syvaris", "d", lambda x: x["cities"][3].update(populationRange=copy.deepcopy(x["cities"][2]["populationRange"]))),
        ("taramin_range_provenance_lost", "d", lambda x: x["cities"][2]["populationRange"].update(provenance="DERIVED")),
        ("taramin_range_claims_exact_pop", "d", lambda x: x["cities"][2].update(populationApprox=17000)),
        ("taramin_range_status_wrong", "d", lambda x: x["cities"][2].update(populationStatus="UNKNOWN")),
        ("taramin_range_source_unlinked", "d", lambda x: x["cities"][2].update(sourceRefIds=["d07", "d04"])),
        ("taramin_range_source_deleted", "d", lambda x: x["sourceRefs"].pop("decisionD0801Taramin")),

        ("treihord_changed", "d", lambda x: x["cities"][0].update(populationApprox=30000)),
        ("made_city", "d", lambda x: x["cities"].append(copy.deepcopy(x["cities"][0]))),
        ("changed_city", "d", lambda x: x["cities"][2].update(id="karsath")),
        ("urban_plan", "d", lambda x: x["cities"][3].update(geometry={"port": "imaginary"})),
        ("new_building", "d", lambda x: x["cities"][1].update(newBuildingsApproved=True)),
        ("invented_service", "d", lambda x: x["cities"][1]["physicalServicesRegistered"].append("hospital")),
        ("invented_households", "d", lambda x: x["cities"][2].update(householdCount=400)),
        ("invented_jobs", "d", lambda x: x["cities"][2].update(occupationCounts={"fishers": 50})),
        ("commute_time", "d", lambda x: x["cities"][1].update(travelTimes=12)),
        ("guild_made", "d", lambda x: x["occupationFamilies"][0].update(formalGuildCreated=True)),
        ("job_count", "d", lambda x: x["occupationFamilies"][3].update(canonicalJobCount=13)),
        ("bad_chain", "d", lambda x: x["occupationFamilies"][7].update(d04Chain="invented")),
        ("created_healer", "d", lambda x: x["serviceNeeds"][4]["actualBuildings"].append("hospital")),
        ("staff_count", "d", lambda x: x["serviceNeeds"][4].update(providerCount=5)),
        ("service_missing", "d", lambda x: x["serviceNeeds"].pop()),
        ("invented_density", "d", lambda x: x["settlementProfiles"][0].update(demographicBand=[10,300])),
        ("new_settlement", "d", lambda x: x["settlementProfiles"][2]["actualSettlements"].append("Invention")),
        ("no_supervision", "d", lambda x: x["householdModel"].update(apprenticeshipMinAge=8)),
        ("adult_age", "d", lambda x: x["householdModel"].update(adultAgeMin=16)),
        ("kinship_magic", "d", lambda x: x["householdModel"].update(coResidenceImpliesMarriage=True)),
        ("household_count", "d", lambda x: x["householdModel"].update(householdCount=500)),
        ("free_stock", "d", lambda x: x["causalFlow"].update(requireNonnegativeStock=False)),
        ("fictitious_road", "d", lambda x: x["causalFlow"].update(doNotUseD05SupplyDependencyAsRoad=False)),
        ("new_provider_by_need", "d", lambda x: x["causalFlow"].update(providerNotCreatedByDemand=False)),
        ("numeric_relation_registry", "d", lambda x: x["coreRpgAudit"].update(numericRelationKindIds={"home": 1})),
        ("source_gone", "d", lambda x: x["sourceRefs"].update(res="Worldbuilding/MISSING.json")),
        ("direct_canon", "d", lambda x: x.update(canonStatus="AUTHORED_NEW_SOCIAL_LAW")),
        ("fake_fixture_site", "f", lambda x: x["cases"][0].update(site="treihord")),
        ("fixture_real_npcs", "f", lambda x: x.update(createdNpcCountInWorldState=8)),
        ("fixture_canonical_claim", "f", lambda x: x.update(status="CANON")),
        ("unprefixed_person", "f", lambda x: x["cases"][0]["persons"][0].update(id="npc_real")),
        ("invalid_member_ref", "f", lambda x: x["cases"][0]["households"][0]["members"].append("TEST_ONLY_absent")),
        ("fixture_age_recast", "f", lambda x: x["cases"][2]["persons"][0].update(age=19)),
    ]
    for name, target, mutate in mutations:
        d, f = copy.deepcopy(data), copy.deepcopy(fixtures)
        mutate(d if target == "d" else f)
        try:
            validate(d, f, repo)
        except (AssertionError, KeyError, TypeError, ValueError):
            continue
        raise AssertionError("D08 NEGATIVE NOT CAUGHT: " + name)
    print(f"D08 STATIC OK: 4 manual cities, 9 D06 model families, "
          f"{len(data['serviceNeeds'])} service needs, "
          f"{len(data['occupationFamilies'])} functional job families, "
          f"{len(fixtures['cases'])} TEST_ONLY cases, {len(mutations)} negative mutations; "
          "NO CORE/GODOT RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print("D08 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)

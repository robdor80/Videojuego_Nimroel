#!/usr/bin/env python3
"""DAROVAN D09 — static documentary consistency, cross-phase and adversarial tests. No runtime."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
INDEX = ROOT + "Datos operativos/darovan_d09_governance_security_v0.1.json"
CASES = ROOT + "Datos operativos/darovan_d09_test_scenarios_v0.1.json"
SCHEMA = ROOT + "Datos operativos/darovan_d09_governance_security.schema.json"
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
CITIES = ["treihord", "veldora", "taramin", "syvaris"]
LINKS = ["d05_road_veldora_treihord", "d05_belara_shallow_haul", "d05_vena_restricted"]
DECISIONS = [
    ("G01", "B"), ("G02", "B"), ("G03", "B"), ("G04", "B"), ("G05", "C"), ("G06", "A"),
    ("F01", "B"), ("F02", "C"), ("F03", "B"), ("F04", "C"),
    ("D01", "A"), ("D02", "C"), ("D03", "C"), ("D04", "A"),
    ("S01", "B"), ("S02", "C"), ("S03", "B"),
]
CASE_IDS = [
    "d09_t01_warehouse_theft", "d09_t02_trade_dispute", "d09_t03_customs_manifest",
    "d09_t04_mine_security", "d09_t05_caravan_attack", "d09_t06_authority_conflict",
    "d09_t07_urban_fire", "d09_t08_syvaris_naval", "d09_t09_vena_access",
    "d09_t10_interhouse_levy", "d09_t11_juvenile_recruit", "d09_t12_capital_sentence",
    "d09_t13_fishing_port", "d09_t14_monetary_paper",
]
EXPECTED_TAGS = [
    "case_requires_proof_no_owner_transfer", "civil_disagreement_not_automatically_crime",
    "no_interior_customs_no_omniscience", "no_new_mine_location",
    "physical_link_existing_not_all_supply_routes", "no_auto_command_takeover",
    "resource_bound_no_instant_rescue", "royal_navy_not_house_navy",
    "joint_custody_no_public_passage", "no_customs_or_new_tax",
    "underage_combat_prohibited", "capital_execution_blocked_without_authority",
    "not_external_import", "no_darovan_coin_or_new_mint",
]
EXPECTED_SITES = [
    "veldora", "veldora", "veldora", "TEST_ONLY_unsited_mine",
    "d05_road_veldora_treihord", "treihord", "taramin", "syvaris",
    "d05_vena_restricted", "TEST_ONLY_house_border", "treihord", "treihord",
    "taramin", "treihord",
]
TOP = {
    "schemaVersion", "documentId", "version", "phase", "preparedAt", "status",
    "canonStatus", "authorityChain", "sourceRefs", "authorDecisions", "government",
    "fiscal", "security", "localities", "unknowns", "runtimeIntegration",
}

def check(ok: bool, why: str) -> None:
    if not ok:
        raise AssertionError(why)

def read(root: Path, path: str) -> dict:
    return json.loads((root / path).read_text(encoding="utf-8"))

def validate(d: dict, f: dict, repo: Path) -> None:
    check(set(d) == TOP and d["schemaVersion"] == 1
          and d["documentId"] == "darovan_d09_governance_fiscal_defense_security"
          and d["version"] == "0.1" and d["phase"] == "D09"
          and d["status"] == "planning_reference_not_runtime"
          and d["canonStatus"] == "author_approved_17_conceptual_choices_no_local_statutes"
          and d["authorityChain"] == AUTH, "D09 root/authority/status")

    s = read(repo, SCHEMA)
    check(s["$schema"] == "https://json-schema.org/draft/2020-12/schema"
          and s["additionalProperties"] is False
          and set(s["required"]) == TOP and set(s["properties"]) == TOP
          and s["properties"]["authorDecisions"]["minItems"] == 17, "D09 schema drift")
    check(len(d["sourceRefs"]) >= 26
          and len(set(d["sourceRefs"].values())) == len(d["sourceRefs"])
          and all(isinstance(v, str) and v.startswith("Worldbuilding/")
                  and (repo / v).is_file() for v in d["sourceRefs"].values()),
          "missing, duplicated or untraceable canon reference")
    for key in ("auditD09", "governmentD09", "fiscalD09", "securityD09",
                "d04", "d05", "d06", "d07", "d08", "kingsJustice", "navy",
                "norgardFiscal", "norgardMilitary", "norgardPenal", "norgardProcedure",
                "coreLegal", "coreTxn", "coreOwn", "coreEmergency"):
        check(key in d["sourceRefs"], "missing mandatory source: " + key)

    choices = d["authorDecisions"]
    check(len(choices) == len(DECISIONS), "decision count")
    for i, (id_, option) in enumerate(DECISIONS):
        v = choices[i]
        check(set(v) == {"id", "option", "scope", "provenance", "approval",
                         "createsNewTax", "createsNamedInstitution", "instantiatesRuntime"}
              and v["id"] == "DAR-D09-" + id_ and v["option"] == option
              and bool(v["scope"]) and v["provenance"] == "AUTHORED_CONCEPT"
              and v["approval"] == "AUTHOR_BATCH_2026-10-22"
              and v["createsNewTax"] is False and v["createsNamedInstitution"] is False
              and v["instantiatesRuntime"] is False, "unauthorized canon choice " + id_)

    g, t, a = d["government"], d["fiscal"], d["security"]
    for key in ("crownSupreme", "karsathExcluded"):
        check(g[key] is True, "governance guardrail " + key)
    for key in ("houseIndependentLegislation", "houseSovereign",
                "newCouncilsCreated", "newJudicialBuildingsCreated"):
        check(g[key] is False, "invented governance power " + key)
    check(g["seat"] == "treihord" and g["delegation"] == "functional_local_subordinate"
          and g["consultation"] == "existing_actors_nonbinding_no_council_created"
          and g["ruralAdministration"] == "subordinate_undelimited"
          and g["arvenAdminHouse"] == "casa_darovan"
          and all(g[x] is None for x in ("namedRuler", "namedHeirs", "minorHouses")), "house governance")
    check(g["royalEnvoyTreihord"] == {"exists": True, "role": "fiscal_oversight",
           "operatesDarovanFacilities": False}, "royal envoy authority")

    j = g["kingsJustice"]
    check(j["onePenalLaw"] is True and j["ordinaryCities"] == CITIES
          and j["smallerLocalities"] == "itinerant_without_claimed_routes_or_buildings"
          and j["penalCodeOwner"] == "norgard_defaults"
          and j["capitalTerritorialConfirmationRequired"] is True
          and j["capitalAuthorityExact"] is None
          and all(j[x] is False for x in ("longPrisonOrdinary",
               "professionalProsecutorCreated", "professionalDefenseCounselCreated",
               "juryCreated", "tortureAsEvidence", "automaticConviction",
               "executionsWithoutConfirmedCompetence")), "king justice/capital oversight")

    check(t["crownSuperior"] is True and t["localRecords"] is True
          and t["treihordReconciliation"] is True and t["crownAccounting"] is True
          and set(t["allowedCategories"]) == {
              "territorial_contribution", "market_real_service", "port_actual_service",
              "external_customs", "recorded_crown_remittance", "royal_authorized_extraordinary_levy"}
          and len(t["allowedCategories"]) == 6
          and all(t[x] is None for x in ("taxRates", "remittancePeriod", "remittanceShare"))
          and t["customsBetweenGreatHouses"] is False
          and t["transactionPerPurchaseTaxAutomatic"] is False
          and t["extraordinaryLevyRequiresRoyalOrder"] is True
          and t["ledgerNeedsEvidence"] is True and t["booksAreNotWorldState"] is True,
          "new tax/customs/remittance invented")
    v = t["veldora"]
    check(v["externalCustoms"] is True and v["customsDecisionAuthority"] == "crown"
          and v["darovanRole"] == "port_logistics_administration_civil_security"
          and v["localFishingIsImport"] is False and v["inspectionRequiresEvidenceOrLawfulSelection"] is True
          and len(v["declarationRequiredWhenApplicable"]) == 7, "Veldora customs authority")
    c = t["crisol"]
    check(c["ownerAndOperator"] == "casa_darovan" and c["canRefineAndAssay"] is True
          and c["canMint"] is False and c["relatedFacility"] == "boveda_del_grifo"
          and c["venaRestricted"] is True and c["recordsReconciledWithCrown"] is True, "Crisol cannot mint")
    cur = t["currency"]
    check(cur == {"accountingUnit": "clavo", "lunaToClavo": 24,
                  "coronaToClavo": 480, "physicalGoodsSurviveValuation": True,
                  "crownMintOnly": True}, "currency/material consistency")

    check(a["royalMilitarySupremacy"] is True and a["royalNavyOnly"] is True
          and a["darovanIndependentNavy"] is False and a["minCombatAge"] == 18
          and a["localGuards"] == "local_scope_territorial_coordination"
          and a["territorialProfessionals"] == "balanced_response_real_threat_resources_required"
          and a["civilGuardsBecomeArmyAutomatically"] is False
          and a["forcedConscriptionMinors"] is False and a["legalProofRequired"] is True
          and a["supplyRelationsDoNotProveRoads"] is True
          and a["confirmedPhysicalLinksOnly"] == LINKS, "military and geospatial limits")
    layer_ids = ["house_guard", "urban_guard", "territorial_professional", "mobilizable_reserve"]
    check([x["id"] for x in a["layers"]] == layer_ids
          and [x["notArmy"] for x in a["layers"]] == [True, True, False, False]
          and all(x["numericStrength"] is None for x in a["layers"]), "fictional troop counts")
    check(a["houseGuardProtected"] == ["boveda_del_grifo", "crisol", "vena",
           "house_family", "institutional_high_value_escort"], "house guard")
    check(a["syvaris"] == {"darovanLandCivilSecurity": True, "royalNavyCommand": "crown",
           "darovanNavy": False, "navalBaseOrQuartersNew": False}, "Syvaris naval sovereignty")
    check(a["patrols"] == {"riskAdaptive": True, "scheduleAndRoutesMaterialized": False,
           "staffAndResourcesGuaranteed": False}, "invented route or patrol")
    check(a["escorts"] == {"mode": "private_or_darovan_according_to_authority_owner_risk",
           "automaticFreeEscort": False}, "infinite escorts")
    check(a["vena"] == {"restricted": True,
           "authorization": "crisol_and_boveda_joint_recorded_coordination",
           "publicAccess": False}, "Vena breached")
    check(len(a["incidentFlow"]) == 7
          and a["incidentFlow"][0] == "verified_signal"
          and a["incidentFlow"][-1] == "persist_only_after_runtime_integration",
          "incident semantics")

    l = d["localities"]
    check([x["id"] for x in l] == CITIES
          and all(x["isCanonicalCity"] is True
                  and x["locationOrBuildingNew"] is False
                  and x["personnelNumbers"] is None for x in l), "invented city/place")
    functions = {x["id"]: set(x["functions"]) for x in l}
    check("royal_external_customs" in functions["veldora"]
          and "crown_permanent_envoy_existing" in functions["treihord"]
          and "crisol_ensay_not_mint" in functions["treihord"]
          and "norgard_royal_navy_presence" in functions["syvaris"]
          and "local_fishing_not_customs_import" in functions["taramin"]
          and all("kings_justice_ordinary" in functions[c] for c in CITIES), "functional city mapping")
    check(len(d["unknowns"]) >= 15 and all(v is None for v in d["unknowns"].values()),
          "unknowns were fabricated")
    check(d["runtimeIntegration"] == {
        "coreRpgExecuted": False, "godotExecuted": False, "gdeExtensionExecuted": False,
        "createdNpcCount": 0, "createdNamedInstitutions": 0,
        "generatedBuildings": 0, "worldStateMaterialized": False,
        "contractsAreNativeCoreAPIs": False}, "false runnable D09 claim")

    d04 = read(repo, d["sourceRefs"]["d04"])
    d05 = read(repo, d["sourceRefs"]["d05"])
    d06 = read(repo, d["sourceRefs"]["d06"])
    d07 = read(repo, d["sourceRefs"]["d07"])
    d08 = read(repo, d["sourceRefs"]["d08"])
    check(len(d04["resourceChains"]) == 8 and len(d06["models"]) == 9,
          "D04/D06 source drift")
    check([x["id"] for x in d05["confirmedTransportLinks"]] == LINKS
          and len(d05["supplyRelationsNotRoutes"]) == 4, "D05 fictitious road")
    check(d07["manualCityIds"] == CITIES
          and [x["id"] for x in d07["cities"]] == CITIES
          and d07["otherDarovanIsland"] == "arven"
          and d07["hydro"]["belaraCrossesTreihord"] is False, "D07 city/canon drift")
    check(d08["territoryPopulation"]["populationRange"]["minInclusive"] == 300000
          and d08["territoryPopulation"]["populationRange"]["maxInclusive"] == 450000
          and d08["territoryPopulation"]["populationApprox"] is None
          and d08["householdModel"]["ageShares"]["bands"][0]["percent"] == 30
          and d08["householdModel"]["ageShares"]["bands"][1]["percent"] == 60
          and d08["householdModel"]["ageShares"]["bands"][2]["percent"] == 10
          and d08["householdModel"]["ruralUrbanShares"]["urbanSharePercentRange"]
              == {"minInclusive": 35, "maxInclusive": 45}
          and d08["householdModel"]["ruralUrbanShares"]["cityListIsCompleteUrbanCoverage"] is False,
          "D08 people or urban coverage drift")
    check(f["schemaVersion"] == 1 and f["documentId"] == "darovan_d09_test_only_incidents"
          and f["phase"] == "D09" and f["status"] == "TEST_ONLY_NOT_CANON"
          and f["authorityChain"] == AUTH
          and f["usesSyntheticEventIdentifiers"] is True
          and f["createsActualNpcCount"] == 0 and f["changesWorldState"] is False, "fixtures have become canon")
    cases = f["cases"]
    check(len(cases) == len(CASE_IDS)
          and [x["id"] for x in cases] == CASE_IDS
          and len({x["site"] for x in cases}) == len(cases), "missing/duplicate fixture")
    for i, case in enumerate(cases):
        check(case["site"] == "TEST_ONLY_" + CASE_IDS[i]
              and case["referenceSite"] == EXPECTED_SITES[i]
              and case["expected"] == EXPECTED_TAGS[i]
              and all(isinstance(case[x], str) and case[x] for x in
                  ("event", "competentActor", "evidence"))
              and case["testOnly"] is True and case["canonicalEvent"] is False
              and case["createsPersons"] == 0 and case["createsFacilities"] == 0
              and case["executesInWorldState"] is False, "fictional event promoted: " + CASE_IDS[i])

def run() -> None:
    repo = Path.cwd()
    data, fixtures = read(repo, INDEX), read(repo, CASES)
    validate(data, fixtures, repo)
    mutations = []
    for i, (_, choice) in enumerate(DECISIONS):
        other = "B" if choice == "A" else "A"
        mutations.append(("option_" + str(i), "d",
                          lambda x, i=i, other=other: x["authorDecisions"][i].update(option=other)))
    mutations.extend([
        ("new_tax", "d", lambda x: x["fiscal"]["allowedCategories"].append("mineral_export_tax")),
        ("customs_inside", "d", lambda x: x["fiscal"].update(customsBetweenGreatHouses=True)),
        ("tax_one_purchase", "d", lambda x: x["fiscal"].update(transactionPerPurchaseTaxAutomatic=True)),
        ("force_remittance", "d", lambda x: x["fiscal"].update(remittancePeriod="monthly")),
        ("crown_quota", "d", lambda x: x["fiscal"].update(remittanceShare=0.25)),
        ("tariff_guess", "d", lambda x: x["fiscal"].update(taxRates={"silver": 10})),
        ("false_mint", "d", lambda x: x["fiscal"]["crisol"].update(canMint=True)),
        ("royal_envoy_controls_mine", "d", lambda x: x["government"]["royalEnvoyTreihord"].update(operatesDarovanFacilities=True)),
        ("capital_execution", "d", lambda x: x["government"]["kingsJustice"].update(executionsWithoutConfirmedCompetence=True)),
        ("named_lord", "d", lambda x: x["government"].update(namedRuler="Caedren Darovan")),
        ("minor_houses_invented", "d", lambda x: x["government"].update(minorHouses=["TEST"])),
        ("jury_modern", "d", lambda x: x["government"]["kingsJustice"].update(juryCreated=True)),
        ("automatic_guilt", "d", lambda x: x["government"]["kingsJustice"].update(automaticConviction=True)),
        ("darovan_war_navy", "d", lambda x: x["security"].update(darovanIndependentNavy=True)),
        ("syvaris_command", "d", lambda x: x["security"]["syvaris"].update(royalNavyCommand="darovan")),
        ("missing_guard", "d", lambda x: x["security"]["layers"].pop()),
        ("guard_count", "d", lambda x: x["security"]["layers"][0].update(numericStrength=70)),
        ("child_soldiers", "d", lambda x: x["security"].update(minCombatAge=16)),
        ("public_vena", "d", lambda x: x["security"]["vena"].update(publicAccess=True)),
        ("invented_road", "d", lambda x: x["security"]["confirmedPhysicalLinksOnly"].append("d05_invented_road")),
        ("auto_patrol_teleport", "d", lambda x: x["security"]["patrols"].update(scheduleAndRoutesMaterialized=True)),
        ("new_city", "d", lambda x: x["localities"].append(dict(x["localities"][0], id="new_city"))),
        ("fabricated_census", "d", lambda x: x["unknowns"].update(householdAndWorkforceExactCounts=80000)),
        ("false_core_runtime", "d", lambda x: x["runtimeIntegration"].update(coreRpgExecuted=True)),
        ("missing_source", "d", lambda x: x["sourceRefs"].update(treihord="Worldbuilding/ABSENT.md")),
        ("fixture_claim_canon", "f", lambda x: x["cases"][0].update(canonicalEvent=True)),
        ("fixture_creates_people", "f", lambda x: x["cases"][1].update(createsPersons=4)),
        ("fixture_site_real", "f", lambda x: x["cases"][2].update(site="veldora")),
        ("fixture_wrong_expected", "f", lambda x: x["cases"][3].update(expected="new_mine_approved")),
        ("fixture_world_state", "f", lambda x: x.update(changesWorldState=True)),
        ("fixture_duplicate", "f", lambda x: x["cases"][4].update(id=x["cases"][0]["id"])),
    ])
    for name, target, mutation in mutations:
        candidate = copy.deepcopy(data)
        tests = copy.deepcopy(fixtures)
        mutation(candidate if target == "d" else tests)
        try:
            validate(candidate, tests, repo)
        except (AssertionError, KeyError, TypeError, ValueError, OSError):
            continue
        raise AssertionError("D09 NEGATIVE NOT CAUGHT: " + name)
    print("D09 STATIC OK: 17 authorial decisions, 4 manual cities, "
          + str(len(fixtures["cases"])) + " synthetic incidents, "
          + str(len(mutations)) + " rejected negative mutations, D04-D08 cross-check; NO CORE/GODOT RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print("D09 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)

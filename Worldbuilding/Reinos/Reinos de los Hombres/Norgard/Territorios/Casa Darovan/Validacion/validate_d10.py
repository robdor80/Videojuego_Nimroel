#!/usr/bin/env python3
"""D10: validación estática, trazabilidad, regresión canónica y pruebas negativas. No runtime."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
INDEX = ROOT + "Datos operativos/darovan_d10_culture_society_v0.1.json"
SCHEMA = ROOT + "Datos operativos/darovan_d10_culture_society.schema.json"
CASES = ROOT + "Datos operativos/darovan_d10_test_scenarios_v0.1.json"
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
CITY = ["treihord", "veldora", "taramin", "syvaris"]
LOCAL = CITY + ["arven", "rural_conditional"]
OPTIONS = ["B"] * 8 + ["C"] + ["B"] * 8
CONTEXT = {
    "treihord": ["institutions", "craft", "metal", "industry", "commerce", "mixed_social_conditions"],
    "veldora": ["external_commerce", "maritime_contact", "craft", "customs_crown"],
    "taramin": ["marine_and_river_fishing", "mixed_livelihood", "thalen_two_terminal_arms"],
    "syvaris": ["island", "protected_bay", "fishing", "royal_navy_presence", "microclimate_diversity"],
    "arven": [],
    "rural_conditional": ["requires_existing_settlement", "requires_local_resources", "requires_context"],
}
EXPECTED_CASES = [
    ("treihord", "poverty_not_criminal_proof"),
    ("treihord", "profession_change_no_pers_reroll"),
    ("veldora", "trade_exists_not_personal_knowledge"),
    ("veldora", "hospitality_requires_willing_actor"),
    ("taramin", "no_mandatory_local_festivity"),
    ("taramin", "no_inferred_bridge_or_navigation"),
    ("syvaris", "island_origin_not_hostility"),
    ("syvaris", "royal_navy_not_darovan_navy"),
    ("arven", "unknown_not_automatic_custom"),
    ("rural_conditional", "network_not_legal_obligation"),
    ("treihord", "three_day_mourning_not_auto_funeral_site"),
    ("treihord", "preexisting_fair_name_and_dates_unknown"),
    ("veldora", "no_unearned_darovan_surname"),
    ("taramin", "food_stock_not_conjured"),
    ("syvaris", "gift_not_automatic_friendship"),
    ("rural_conditional", "d06_model_not_materialized_settlement"),
]
EXPECTED_FALSE = [
    "newLegalCastes", "newLegalPrivileges", "automaticNpcPersonalityFromOccupation",
    "automaticNpcPersonalityFromResidence", "automaticNpcCrimeFromWealth",
    "automaticNpcHostilityFromIsland", "inventedInstitution", "inventedCalendarHoliday",
    "newReligiousRite", "newRecipes", "physicalClocks", "foreignResidentsAutoMaterialized",
    "houseNavy", "newRoutes", "newSettlements", "nameOrSurnameRandomOverride",
    "rerollExistingPersonality",
]
EXPECTED_TRUE = [
    "cultureAffectsLearnedExpressionOnly", "materialTransferRequiresOwn",
    "socialKnowledgeRequiresEvidence", "funeralCremation", "funeralTerritorialReturn",
    "arvenIsDarovan", "fairTreihordAlreadyCanonical", "norgardNavyOnSyvaris",
]
REQUIRED_SOURCE_KEYS = [
    "approvalD10", "matrixD10", "identityD10", "localD10", "everydayD10",
    "relationsD10", "treihord", "greatHouses", "norgardVisual", "d02",
    "d04", "d05", "d06", "d07", "d08", "d09", "norgardFuneral",
    "norgardToponyms", "norgardFamily", "norgardLabor", "norgardProperty",
    "norgardCuisine", "norgardNames", "norgardCalendar", "norgardMaterial",
    "norgardPersonality", "coreKin", "coreFriend", "coreFavor", "coreGift",
    "corePers", "coreName", "coreFood", "coreDialog",
]
def check(value: bool, why: str) -> None:
    if not value:
        raise AssertionError(why)

def read(repo: Path, p: str) -> dict:
    return json.loads((repo / p).read_text(encoding="utf-8"))

def schema_check(value: object, schema: dict, loc: str = "$") -> None:
    """Subconjunto explícito de JSON Schema usado por nuestro esquema; sin librerías extra."""
    if "const" in schema:
        check(value == schema["const"], loc + " const mismatch")
    if "enum" in schema:
        check(value in schema["enum"], loc + " enum mismatch")
    typ = schema.get("type")
    if typ == "object":
        check(isinstance(value, dict), loc + " not object")
        req = schema.get("required", [])
        check(all(k in value for k in req), loc + " missing required")
        if schema.get("additionalProperties") is False:
            check(set(value) == set(schema.get("properties", {})), loc + " extra/missing keys")
        check(len(value) >= schema.get("minProperties", 0), loc + " too few properties")
        for k, v in value.items():
            prop = schema.get("properties", {}).get(k)
            if prop is None and isinstance(schema.get("additionalProperties"), dict):
                prop = schema["additionalProperties"]
            if prop is not None:
                schema_check(v, prop, loc + "." + k)
    elif typ == "array":
        check(isinstance(value, list), loc + " not array")
        check(schema.get("minItems", 0) <= len(value) <= schema.get("maxItems", 10**9), loc + " length")
        if isinstance(schema.get("items"), dict):
            for i, v in enumerate(value):
                schema_check(v, schema["items"], loc + "[" + str(i) + "]")
    elif typ == "string":
        check(isinstance(value, str), loc + " not string")
        check(len(value) >= schema.get("minLength", 0), loc + " short string")
        if "pattern" in schema:
            check(re.search(schema["pattern"], value) is not None, loc + " pattern")
    elif typ == "null":
        check(value is None, loc + " expected null")

def validate(d: dict, f: dict, repo: Path) -> None:
    s = read(repo, SCHEMA)
    check(s["$schema"] == "https://json-schema.org/draft/2020-12/schema"
          and s["additionalProperties"] is False
          and set(s["required"]) == set(s["properties"]) == set(d), "schema top-level drift")
    schema_check(d, s)
    check(d["authorityChain"] == AUTH and d["phase"] == "D10"
          and d["status"] == "planning_reference_not_runtime", "D10 authority/status")
    refs = d["sourceRefs"]
    check(set(refs) == set(REQUIRED_SOURCE_KEYS), "source coverage drift")
    check(len(set(refs.values())) == len(refs), "duplicate source path")
    check(all(v.startswith("Worldbuilding/") and (repo / v).is_file() for v in refs.values()),
          "missing/unauthorized source reference")
    check(all("/Casa Darovan/Datos operativos/darovan_d" + str(i).zfill(2) + "_"
              in refs["d" + str(i).zfill(2)] for i in [2, 4, 5, 6, 7, 8, 9]),
          "wrong phase source")
    decisions = d["authorDecisions"]
    check(len(decisions) == 17, "author decision count")
    for i, v in enumerate(decisions):
        check(v["id"] == "DAR-D10-" + str(i + 1).zfill(2)
              and v["option"] == OPTIONS[i]
              and v["provenance"] == "AUTHORED_CONCEPT"
              and v["approval"] == "AUTHOR_BATCH_2026-10-23"
              and len(v["scope"]) >= 4
              and all(v[x] is False for x in
                      ("createsInstitutions", "createsPersons", "createsEvents", "createsLocalLaw")),
              "unapproved choice or materialization D10-" + str(i + 1))
    loc = d["localProfiles"]
    check([x["id"] for x in loc] == LOCAL, "city/island count or order")
    for i, p in enumerate(loc):
        check(p["decision"] == "DAR-D10-" + str(i + 5).zfill(2)
              and p["contextTags"] == CONTEXT[p["id"]]
              and p["individualVariation"] is True
              and p["createsNewLocations"] is False and p["createsNpc"] is False,
              "local cultural profile drift " + p["id"])
        expected_kind = "canonical_city" if i < 4 else (
            "existing_darovan_island" if i == 4 else "nonmaterialized_planning_category")
        expected_state = "AUTHORED_CONCEPT" if i < 4 else (
            "UNKNOWN" if i == 4 else "DERIVED_NONCANON")
        check(p["kind"] == expected_kind and p["culturalState"] == expected_state,
              "local source authority drift")
    g = d["guardrails"]
    check(all(g[k] is False for k in EXPECTED_FALSE)
          and all(g[k] is True for k in EXPECTED_TRUE)
          and g["funeralCremation"] is True
          and g["mourningFormalDays"] == 3 and g["treihordCanonicalDistrictCount"] == 8
          and g["treihordBelaraCrossesCity"] is False
          and g["fairNewNameOrDateApproved"] is False
          and g["karsathIsDarovan"] is False and g["darovanMintAllowed"] is False
          and g["canonicalCityIds"] == CITY, "guardrail modified")
    check(len(d["unknowns"]) >= 15 and all(v is None for v in d["unknowns"].values()),
          "UNKNOWN promoted to canon")
    runtime = d["runtimeIntegration"]
    check(all(v is False for k, v in runtime.items() if isinstance(v, bool))
          and all(v == 0 for k, v in runtime.items() if type(v) is int)
          and runtime["worldStateMaterialized"] is False, "false runtime claim")
    # Cross-phase reads: source files retained from merged D02/D07/D08/D09.
    d07, d08, d09 = (read(repo, refs[p]) for p in ("d07", "d08", "d09"))
    check(d07["manualCityIds"] == CITY and d07["otherDarovanIsland"] == "arven"
          and d07["hydro"]["belaraCrossesTreihord"] is False
          and [c["id"] for c in d07["cities"]] == CITY, "D07 canonical city regression")
    check(d08["territoryPopulation"]["populationRange"]["minInclusive"] == 300000
          and d08["territoryPopulation"]["populationRange"]["maxInclusive"] == 450000
          and d08["territoryPopulation"]["populationRange"]["status"] == "APPROVED_AUTHOR_RANGE"
          and d08["territoryPopulation"]["populationApprox"] is None
          and d08["householdModel"]["ruralUrbanShares"]["cityListIsCompleteUrbanCoverage"] is False,
          "D08 demographics drift")
    check(d09["government"]["houseIndependentLegislation"] is False
          and d09["security"]["royalNavyOnly"] is True
          and d09["fiscal"]["customsBetweenGreatHouses"] is False,
          "D09 law/navy/customs drift")
    check(f["schemaVersion"] == 1 and f["documentId"] == "darovan_d10_test_only_social_cases"
          and f["phase"] == "D10" and f["status"] == "TEST_ONLY_NOT_CANON"
          and f["authorityChain"] == AUTH and f["createsActualNpcCount"] == 0
          and f["changesWorldState"] is False, "fixtures not isolated")
    check(len(f["cases"]) == len(EXPECTED_CASES), "scenario count")
    for i, v in enumerate(f["cases"]):
        check(v["id"] == "d10_t" + str(i + 1).zfill(2) + "_" + [
            "treihord_poor_neighbor", "treihord_craft_change", "veldora_elf_contact",
            "veldora_outsider", "taramin_fisher", "thalen_crossing",
            "syvaris_islander", "syvaris_navy", "arven", "rural_network",
            "funeral", "fair", "naming", "food", "gift", "rural_no_village",
        ][i], "scenario identifier")
        check(v["site"] == "TEST_ONLY_" + v["id"]
              and v["referenceSite"] == EXPECTED_CASES[i][0]
              and v["expected"] == EXPECTED_CASES[i][1]
              and isinstance(v["event"], str) and bool(v["event"])
              and v["testOnly"] is True and v["canonicalEvent"] is False
              and v["createsNpcCount"] == 0 and v["createsBuildings"] == 0
              and v["changesWorldState"] is False, "scenario escalated to fiction")

def run() -> None:
    repo = Path.cwd()
    d, f = read(repo, INDEX), read(repo, CASES)
    validate(d, f, repo)
    tests = []
    for i, original in enumerate(OPTIONS):
        tests.append(("choice_" + str(i), "d", lambda x, i=i, original=original:
                      x["authorDecisions"][i].update(option="A" if original != "A" else "B")))
    tests.extend([
        ("authority", "d", lambda x: x["authorityChain"].reverse()),
        ("source", "d", lambda x: x["sourceRefs"].update(corePers="Worldbuilding/NO_SUCH_CONTRACT.json")),
        ("dup_source", "d", lambda x: x["sourceRefs"].update(coreGift=x["sourceRefs"]["coreFriend"])),
        ("extra_city", "d", lambda x: x["guardrails"]["canonicalCityIds"].append("karsath")),
        ("fair_name", "d", lambda x: x["unknowns"].update(fairOfficialName="FERIA INVENTADA")),
        ("arven_profile", "d", lambda x: x["localProfiles"][4].update(culturalState="AUTHORED_CONCEPT")),
        ("arven_tags", "d", lambda x: x["localProfiles"][4]["contextTags"].append("fishing")),
        ("city_extra", "d", lambda x: x["localProfiles"].append(copy.deepcopy(x["localProfiles"][0]))),
        ("treihord_extra_district", "d", lambda x: x["guardrails"].update(treihordCanonicalDistrictCount=9)),
        ("funeral_days", "d", lambda x: x["guardrails"].update(mourningFormalDays=5)),
        ("run_npc", "d", lambda x: x["runtimeIntegration"].update(createdNpcCount=1)),
        ("run_flag", "d", lambda x: x["runtimeIntegration"].update(worldStateMaterialized=True)),
        ("case_canon", "f", lambda x: x["cases"][0].update(canonicalEvent=True)),
        ("case_extra", "f", lambda x: x["cases"].append(copy.deepcopy(x["cases"][0]))),
        ("case_missing", "f", lambda x: x["cases"].pop()),
    ])
    for key in EXPECTED_FALSE + EXPECTED_TRUE:
        tests.append(("guard_" + key, "d", lambda x, key=key:
                      x["guardrails"].update({key: not x["guardrails"][key]})))
    for key in d["unknowns"]:
        tests.append(("unknown_" + key, "d", lambda x, key=key:
                      x["unknowns"].update({key: "fabricated"})))
    for i in range(len(EXPECTED_CASES)):
        tests.append(("case_" + str(i), "f", lambda x, i=i:
                      x["cases"][i].update(expected="invalid_expectation")))
    for i in range(len(LOCAL)):
        tests.append(("locale_" + str(i), "d", lambda x, i=i:
                      x["localProfiles"][i].update(individualVariation=False)))
    for name, side, mutate in tests:
        x, y = copy.deepcopy(d), copy.deepcopy(f)
        mutate(x if side == "d" else y)
        try:
            validate(x, y, repo)
        except (AssertionError, TypeError, KeyError, ValueError):
            continue
        raise AssertionError("Negative mutation NOT REJECTED: " + name)
    print("D10 STATIC OK | 17 author decisions | 6 locality profiles | "
          + str(len(EXPECTED_CASES)) + " TEST_ONLY cases | "
          + str(len(tests)) + " negative mutations rejected | sources and D07-D09 checked")

if __name__ == "__main__":
    run()

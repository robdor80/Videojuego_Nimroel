#!/usr/bin/env python3
"""Darovan D07: traceable city facts, authorial gates and cross-phase static regression. NO RUNTIME."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
FILE = ROOT + "Datos operativos/darovan_d07_canonical_cities_v0.1.json"
CITIES = ["treihord", "veldora", "taramin", "syvaris"]
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
RIVERS = ["belara", "lhera", "veldora", "fhalion", "thalen"]
SYSTEMS = ["belara_lhera", "veldora", "fhalion", "thalen"]
LINKS = ["d05_road_veldora_treihord", "d05_belara_shallow_haul", "d05_vena_restricted"]
EXPECTED_FACTS = {
    "treihord": ["capital_of_darovan", "population_approx_approved", "belara_adjacent_not_crossing",
                 "port_industrial_shallow_draft_only", "crisol_not_mint", "coal_source_montes_azurios",
                 "vena_restricted_gallery", "boveda_del_grifo_existing", "eight_approved_districts",
                 "four_approved_squares", "four_approved_gates"],
    "veldora": ["primary_commercial_port", "west_coast_golfo_veldora", "river_veldora_independent",
                "river_behind_city_visual_anchor", "external_customs_and_royal_presence",
                "merchant_storage_workshops_guilds", "organic_growth_not_perfect_grid",
                "stone_wood_tile_two_floors_some_three", "affluent_areas_away_from_docks",
                "offshore_forested_island"],
    "taramin": ["fishing_port_and_fluvial_fishing", "between_two_thalen_terminal_arms",
                "thalen_terminal_arms_two_not_two_rivers", "maritime_and_fluvial_fishing",
                "marine_products_and_whale_oil_visual", "medium_scale_below_veldora_treihord",
                "functional_non_monumental_character", "semiarid_peninsular_transition",
                "taramin_forest_no_industrial_logging"],
    "syvaris": ["island_is_norgard_and_darovan", "city_at_main_bay_with_minor_coves",
                "safe_island_port", "norgard_naval_presence_not_darovan_navy",
                "smaller_than_taramin", "fishing_trade_marine_products_oils",
                "south_greener_center_north_drier", "discontinuous_small_forests_nonintensive",
                "low_stone_wood_some_whitewash_not_all", "not_desert"],
}
EXPECTED_LAYERS = {
    "treihord": [],
    "veldora": ["study_port_cargo_customs_interface", "study_commercial_mixed_fabric",
                 "study_affluent_transition"],
    "taramin": ["study_fishing_interface", "study_supply_water_resilience",
                 "study_interfluvial_access"],
    "syvaris": ["study_main_bay_interfaces", "study_microclimate_fabric",
                 "study_coves_without_routes"],
}
DISTRICTS = ["El Recinto", "Los Altos", "El Peso", "Las Lonjas",
             "Los Oficios", "La Calzada", "La Ribera", "La Costra"]
SQUARES = ["Plaza Vieja", "Plaza de las Balanzas", "Plaza de las Lonjas", "Plaza del Camino"]
GATES = ["Puerta Alta", "Puerta del Río", "Puerta del Camino", "Puerta Sur"]
TOP_KEYS = {"schemaVersion", "documentId", "version", "phase", "preparedAt", "status",
            "canonStatus", "authorityChain", "sourceRefs", "manualCityIds", "excludedCityIds",
            "otherDarovanIsland", "hydro", "fiscal", "prohibitions", "measurementPolicy",
            "confirmedPhysicalLinkIds", "cities", "authorialPendingIds", "authorialDecisions", "runtimeIntegration"}

def check(ok: bool, why: str) -> None:
    if not ok:
        raise AssertionError(why)

def read(repo: Path, path: str) -> dict:
    return json.loads((repo / path).read_text(encoding="utf-8"))

def validate(data: dict, repo: Path) -> None:
    check(set(data) == TOP_KEYS and data["schemaVersion"] == 1
          and data["documentId"] == "darovan_d07_canonical_city_operational_index"
          and data["version"] == "0.1" and data["phase"] == "D07", "D07 schema")
    check(data["status"] == "planning_reference_not_runtime"
          and data["canonStatus"] == "index_of_authored_facts_and_unapproved_technical_options"
          and data["authorityChain"] == AUTH, "authority / status")
    check(data["manualCityIds"] == CITIES and data["excludedCityIds"] == ["karsath"]
          and data["otherDarovanIsland"] == "arven", "manual cities and jurisdiction")
    hydro = data["hydro"]
    check(hydro == {
        "namedRivers": RIVERS, "systems": SYSTEMS, "belaraCrossesTreihord": False,
        "belaraNavigation": "industrial_shallow_draft_only", "veldoraIndependent": True,
        "thalenTerminalArms": 2, "thalenArmsNavigation": None, "fhalionNavigation": None,
    }, "hydro / navigability protected")
    check(data["fiscal"] == {"internalCustomsBetweenGreatHouses": False,
                             "veldoraExternalCustoms": True}, "Norgard fiscal")
    check(set(data["prohibitions"]) == {
        "generateCanonicalCities", "createCanonicalDistrictsWithoutAuthor",
        "createPhysicalRoutesWithoutEvidence", "createBridgesWithoutEvidence",
        "createHarboursWithoutEvidence", "assumeRiverNavigation",
        "permanentAgujasInteriorSettlements", "industrialTaraminForestry",
        "intensiveSyvarisForestry", "darovanIndependentNavy", "createD08Demographics"
    } and all(v is False for v in data["prohibitions"].values()), "new canon quietly enabled")
    check(set(data["measurementPolicy"]) == {"coordinates", "distances", "travelTimes",
          "portCapacities", "streetMaps", "hydrologicDischarge"}
          and all(v is None for v in data["measurementPolicy"].values()), "false measurements")
    check(data["confirmedPhysicalLinkIds"] == LINKS, "added invented physical link")
    check(data["runtimeIntegration"] == {
        "status": "not_implemented", "coreRpgValidated": False,
        "godotValidated": False, "gisValidated": False,
        "persistedCityEntities": 0, "materializedRoutes": 0, "generatedCities": 0,
    }, "pretend runtime / generated city")
    check(data["authorialPendingIds"] == ["DAR-P02", "DAR-P04", "DAR-P05",
          "DAR-P08", "DAR-P09", "DAR-P10", "DAR-P11",
          ], "authorial pending removed")
    # Three AUTHOR-approved conceptual choices closed; no physical design approved.
    approvals = data["authorialDecisions"]
    check(type(approvals) is list and len(approvals) == 3, "approved decisions count")
    approval = approvals[0]
    check(set(approval) == {
        "id", "cityId", "choice", "status", "approvingAuthority",
        "approvedConcept", "description", "affectsUrbanLayout",
        "createsCanonicalDistrictNames", "createsPhysicalRoutes",
        "createsNewFacilities", "changesPopulation", "pendingDetails"
    } and approval["id"] == "DAR-D07-01" and approval["cityId"] == "veldora"
          and approval["choice"] == "B" and approval["status"] == "APPROVED_CONCEPT_ONLY"
          and approval["approvingAuthority"] == "autor"
          and approval["approvedConcept"] == "multiple_organic_commercial_sectors"
          and isinstance(approval["description"], str)
          and len(approval["description"]) > 30
          and all(approval[k] is False for k in [
              "affectsUrbanLayout", "createsCanonicalDistrictNames",
              "createsPhysicalRoutes", "createsNewFacilities", "changesPopulation"
          ])
          and approval["pendingDetails"] == [
              "district_names", "district_boundaries", "street_plan",
              "placement_of_facilities", "new_buildings_and_accesses"
          ], "Veldora B authorial decision or scope tampered")
    taramin_approval = approvals[1]
    check(set(taramin_approval) == set(approval)
          and taramin_approval["id"] == "DAR-D07-02"
          and taramin_approval["cityId"] == "taramin"
          and taramin_approval["choice"] == "A"
          and taramin_approval["status"] == "APPROVED_CONCEPT_ONLY"
          and taramin_approval["approvingAuthority"] == "autor"
          and taramin_approval["approvedConcept"] == "one_principal_fishing_activity_sector"
          and isinstance(taramin_approval["description"], str)
          and "Thalen" in taramin_approval["description"]
          and all(taramin_approval[k] is False for k in [
              "affectsUrbanLayout", "createsCanonicalDistrictNames",
              "createsPhysicalRoutes", "createsNewFacilities", "changesPopulation"
          ])
          and taramin_approval["pendingDetails"] == [
              "fishing_sector_location", "thalen_arm_navigability",
              "land_access_and_bridges", "dock_placement", "fish_handling_facilities"
          ], "Taramin A authorial decision or scope tampered")
    syvaris_approval = approvals[2]
    check(set(syvaris_approval) == set(approval)
          and syvaris_approval["id"] == "DAR-D07-03"
          and syvaris_approval["cityId"] == "syvaris"
          and syvaris_approval["choice"] == "A"
          and syvaris_approval["status"] == "APPROVED_CONCEPT_ONLY"
          and syvaris_approval["approvingAuthority"] == "autor"
          and syvaris_approval["approvedConcept"] == "principal_urban_activity_concentrated_around_sheltered_main_bay"
          and isinstance(syvaris_approval["description"], str)
          and "bahía" in syvaris_approval["description"]
          and all(syvaris_approval[k] is False for k in [
              "affectsUrbanLayout", "createsCanonicalDistrictNames",
              "createsPhysicalRoutes", "createsNewFacilities", "changesPopulation"
          ])
          and syvaris_approval["pendingDetails"] == [
              "main_bay_precise_urban_layout", "district_names_and_boundaries",
              "port_and_naval_facility_positions", "minor_coves_without_new_ports",
              "island_land_access_and_maritime_routes"
          ], "Syvaris A authorial decision or scope tampered")
    sources = data["sourceRefs"]
    check(set(sources) == {"treihord", "visual", "visualData", "houses", "rivers", "coasts",
          "forests", "regions", "climate", "fiscal", "navigation", "d00", "d01", "d02",
          "d03", "d04", "d05", "d06", "decisions"}, "source keys changed")
    check(all(isinstance(p, str) and p.startswith("Worldbuilding/") and
              (repo / p).is_file() for p in sources.values()), "missing source")
    check(sources["treihord"].endswith("/Norgard/Ciudades/Casa Darovan/Treihord.md")
          and sources["visualData"].endswith("/norgard_settlements_v0.2.json"),
          "identity authority redirected")
    treihord_source = (repo / sources["treihord"]).read_text(encoding="utf-8")
    visual_source = (repo / sources["visual"]).read_text(encoding="utf-8")
    check("CANON — DISEÑO BASE CERRADO" in treihord_source
          and "32.000 habitantes" in treihord_source
          and "Río Belara" in treihord_source
          and "La Vena" in treihord_source
          and all(s in treihord_source for s in DISTRICTS + SQUARES + GATES),
          "Treihord canonical document missing required anchors")
    check(all(s in visual_source for s in ["## 16. Veldora", "## 18. Taramin",
           "## 19. Syvaris", "aduanas", "aceite de ballena"]),
          "Norgard approved visual profile missing")
    visual = read(repo, sources["visualData"])
    check({x["id"] for x in visual["settlements"]} >= set(CITIES),
          "approved Norgard settlement profiles missing")
    d01, d02, d03, d04, d05, d06, fiscal = (read(repo, sources[k]) for k in
           ["d01", "d02", "d03", "d04", "d05", "d06", "fiscal"])
    check(d01["administration"]["darovanCities"] == CITIES
          and d01["administration"]["arvenIslandOwner"] == "casa_darovan",
          "D01 authority")
    check([r["id"] for r in d02["rivers"]] == RIVERS
          and [s["id"] for s in d02["systems"]] == SYSTEMS
          and d02["rivers"][0]["crossesCity"] is False
          and d02["rivers"][1]["branchesFrom"] == "belara"
          and d02["rivers"][4]["terminalArms"] == 2, "D02 hydro")
    check(d03["regionalAnchors"]["syvarisForestsDiscontinuous"] is True
          and d03["regionalAnchors"]["permanentSettlementsInsideAgujasAllowed"] is False,
          "D03 ecology")
    check(d04["forestProtection"]["taraminIndustrialLoggingAllowed"] is False
          and d04["forestProtection"]["syvarisIntensiveForestryAllowed"] is False
          and d04["resourceSourceProtection"]["treihordCoalSource"] == "montes_azurios",
          "D04 resources")
    check([e["id"] for e in d05["confirmedTransportLinks"]] == LINKS
          and len(d05["supplyRelationsNotRoutes"]) == 4
          and d05["movementSemantics"]["graphContainsOnlyAttestedConnections"] is True,
          "D05 links / supply")
    check(d06["manualCityIds"] == CITIES and
          d06["specialConstraints"]["cityGenerationAllowed"] is False, "D06 city exclusion")
    check(fiscal["fiscalUnity"]["customsBetweenGreatHouseTerritories"] is False,
          "Norgard no internal customs")
    cities = data["cities"]
    check(len(cities) == 4 and [c["id"] for c in cities] == CITIES
          and [c["name"] for c in cities] == ["Treihord", "Veldora", "Taramin", "Syvaris"],
          "city inventory order/name")
    city_keys = {"id", "name", "administrativeOwner", "manualOnly",
                 "proceduralGenerationAllowed", "sourceOfIdentity", "designStatus",
                 "facts", "unknowns", "conceptualLayers", "cityGeometry",
                 "routeGeometry", "portGeometry", "worldStateEntityId", "generatedByD06",
                 "authorApprovedNewLayout"}
    for c in cities:
        cid = c["id"]
        check(set(c) == city_keys and c["administrativeOwner"] == "casa_darovan"
              and c["manualOnly"] is True and c["proceduralGenerationAllowed"] is False
              and c["generatedByD06"] is False and c["authorApprovedNewLayout"] is False,
              "manual identity / authorial gate: " + cid)
        check(all(c[k] is None for k in
                  ["cityGeometry", "routeGeometry", "portGeometry", "worldStateEntityId"]),
              "invented city geometry or world state: " + cid)
        check(c["sourceOfIdentity"] == ("treihord" if cid == "treihord" else "visual"),
              "canonical identity source: " + cid)
        check(c["designStatus"] == ("CANON_DISENO_BASE_CERRADO" if cid == "treihord"
              else "VISUAL_APROBADO_TRAZADO_URBANO_PENDIENTE"), "design status: " + cid)
        facts = c["facts"]
        check([f["id"] for f in facts] == EXPECTED_FACTS[cid], "missing/added fact: " + cid)
        check(all(set(f) == {"id", "value", "provenance", "sourceRefIds"}
              and f["provenance"] == "AUTHORED" and f["sourceRefIds"]
              and all(r in sources for r in f["sourceRefIds"]) for f in facts),
              "untraceable fact: " + cid)
        for f in facts:
            fid, val = f["id"], f["value"]
            if fid == "population_approx_approved":
                check(type(val) is int and val == 32000, "Treihord population")
            elif fid == "eight_approved_districts":
                check(val == DISTRICTS, "Treihord original districts")
            elif fid == "four_approved_squares":
                check(val == SQUARES, "Treihord squares")
            elif fid == "four_approved_gates":
                check(val == GATES, "Treihord gates")
            else:
                check(val is True, "authorial fact flipped: " + fid)
        u = c["unknowns"]
        check(len(u) >= 3 and len({x["id"] for x in u}) == len(u)
              and all(set(x) == {"id", "value", "status", "resolution"}
              and x["value"] is None and x["status"] == "UNKNOWN"
              and x["resolution"] in {"pending_autor", "future_technical_verification"}
              for x in u), "unknown replaced by invention: " + cid)
        layers = c["conceptualLayers"]
        check([x["id"] for x in layers] == EXPECTED_LAYERS[cid],
              "city proposals become urban design: " + cid)
        check(all(set(x) == {"id", "goal", "status", "isCanonical",
                             "spatiallyLocated", "createsNewDistrict",
                             "createsNewFacility", "materializedInWorld"}
                  and isinstance(x["goal"], str) and len(x["goal"]) >= 20
                  and x["status"] == "PROPOSAL_PENDING_AUTHOR"
                  and all(x[f] is False for f in ["isCanonical", "spatiallyLocated",
                     "createsNewDistrict", "createsNewFacility", "materializedInWorld"])
                  for x in layers), "proposal promoted silently: " + cid)
    check((repo / (ROOT + "Ciudades/Treihord/D07_COMPATIBILIDAD_OPERATIVA_v0.1.md")).is_file(),
          "Treihord control missing")
    for cid in CITIES[1:]:
        check((repo / (ROOT + "Ciudades/" + cid.capitalize() +
              "/D07_PERFIL_URBANO_OPERATIVO_v0.1.md")).is_file(),
              "city operational sheet missing: " + cid)

def run() -> None:
    repo = Path(__file__).resolve().parents[7]
    # Resolve root robustly from the script location instead of assuming current directory.
    repo = next((p for p in Path(__file__).resolve().parents
                 if (p / FILE).is_file()), None)
    check(repo is not None, "repository checkout root missing")
    data = read(repo, FILE)
    validate(data, repo)
    mutations = [
        ("city_fifth", lambda x: x["manualCityIds"].append("arven")),
        ("karsath_darovan", lambda x: x.update(excludedCityIds=[])),
        ("arven_wrong_owner", lambda x: x.update(otherDarovanIsland="other")),
        ("fhalion_removed", lambda x: x["hydro"].update(namedRivers=RIVERS[:3]+["thalen"])),
        ("extra_system", lambda x: x["hydro"]["systems"].append("lhera")),
        ("belara_city_crossing", lambda x: x["hydro"].update(belaraCrossesTreihord=True)),
        ("belara_deep", lambda x: x["hydro"].update(belaraNavigation="deep_port")),
        ("veldora_river_merged", lambda x: x["hydro"].update(veldoraIndependent=False)),
        ("thalen_one_branch", lambda x: x["hydro"].update(thalenTerminalArms=1)),
        ("thalen_navigable", lambda x: x["hydro"].update(thalenArmsNavigation=True)),
        ("fhalion_navigable", lambda x: x["hydro"].update(fhalionNavigation=True)),
        ("internal_customs", lambda x: x["fiscal"].update(internalCustomsBetweenGreatHouses=True)),
        ("invented_bridge", lambda x: x["prohibitions"].update(createBridgesWithoutEvidence=True)),
        ("invented_harbour", lambda x: x["prohibitions"].update(createHarboursWithoutEvidence=True)),
        ("invented_road", lambda x: x["prohibitions"].update(createPhysicalRoutesWithoutEvidence=True)),
        ("agujas_permanent", lambda x: x["prohibitions"].update(permanentAgujasInteriorSettlements=True)),
        ("taramin_logging", lambda x: x["prohibitions"].update(industrialTaraminForestry=True)),
        ("syvaris_logging", lambda x: x["prohibitions"].update(intensiveSyvarisForestry=True)),
        ("darovan_navy", lambda x: x["prohibitions"].update(darovanIndependentNavy=True)),
        ("new_D08_populations", lambda x: x["prohibitions"].update(createD08Demographics=True)),
        ("fake_coordinates", lambda x: x["measurementPolicy"].update(coordinates=[40,-7])),
        ("new_link", lambda x: x["confirmedPhysicalLinkIds"].append("syvaris_taramin")),
        ("injection_unknown_field", lambda x: x.update(canonicalCityCount=5)),
        ("treihord_rewritten", lambda x: x["cities"][0].update(authorApprovedNewLayout=True)),
        ("treihord_new_district", lambda x: x["cities"][0]["facts"][8]["value"].append("Distrito Inventado")),
        ("treihord_population", lambda x: x["cities"][0]["facts"][1].update(value=45000)),
        ("treihord_mint", lambda x: x["cities"][0]["facts"][4].update(value=False)),
        ("veldora_procedural", lambda x: x["cities"][1].update(proceduralGenerationAllowed=True)),
        ("veldora_fake_port", lambda x: x["cities"][1].update(portGeometry={"newMooring":1})),
        ("veldora_tax_invention", lambda x: x["cities"][1]["facts"][4].update(value=False)),
        ("taramin_new_city", lambda x: x["cities"][2].update(name="Taramin II")),
        ("taramin_fact_unattributed", lambda x: x["cities"][2]["facts"][1].update(sourceRefIds=[])),
        ("syvaris_desert", lambda x: x["cities"][3]["facts"][-1].update(value=False)),
        ("syvaris_naval_claim", lambda x: x["cities"][3]["facts"][3].update(value=False)),
        ("syvaris_district_approved", lambda x: x["cities"][3]["conceptualLayers"][0].update(isCanonical=True)),
        ("proposal_spatialized", lambda x: x["cities"][1]["conceptualLayers"][0].update(spatiallyLocated=True)),
        ("proposal_builds_infrastructure", lambda x: x["cities"][2]["conceptualLayers"][0].update(createsNewFacility=True)),
        ("unknown_filled_without_author", lambda x: x["cities"][1]["unknowns"][0].update(value="Distrito Inventado")),
        ("runtime_claim", lambda x: x["runtimeIntegration"].update(godotValidated=True)),
        ("world_state_claim", lambda x: x["cities"][3].update(worldStateEntityId="instantiated")),
        ("missing_source", lambda x: x["sourceRefs"].update(treihord="Worldbuilding/borrado.md")),
        ("missing_approval_gate", lambda x: x["authorialPendingIds"].remove("DAR-P09")),
        ("choice_flip", lambda x: x["authorialDecisions"][0].update(choice="A")),
        ("approve_building", lambda x: x["authorialDecisions"][0].update(createsNewFacilities=True)),
        ("approve_streets", lambda x: x["authorialDecisions"][0].update(affectsUrbanLayout=True)),
        ("decision_dropped", lambda x: x.update(authorialDecisions=[])),
        ("taramin_choice_flip", lambda x: x["authorialDecisions"][1].update(choice="B")),
        ("taramin_fake_navigation", lambda x: x["hydro"].update(thalenArmsNavigation=True)),
        ("taramin_approval_spatialized", lambda x: x["authorialDecisions"][1].update(affectsUrbanLayout=True)),
        ("taramin_approval_builds_port", lambda x: x["authorialDecisions"][1].update(createsNewFacilities=True)),
        ("syvaris_choice_flip", lambda x: x["authorialDecisions"][2].update(choice="B")),
        ("syvaris_fake_new_port", lambda x: x["authorialDecisions"][2].update(createsNewFacilities=True)),
        ("syvaris_spatialized", lambda x: x["authorialDecisions"][2].update(affectsUrbanLayout=True)),
        ("syvaris_new_districts", lambda x: x["authorialDecisions"][2].update(createsCanonicalDistrictNames=True)),
        ("syvaris_world_route", lambda x: x["authorialDecisions"][2].update(createsPhysicalRoutes=True)),
        ("duplicate_city", lambda x: x["cities"][3].update(id="veldora")),
    ]
    for name, mutate in mutations:
        candidate = copy.deepcopy(data)
        mutate(candidate)
        try:
            validate(candidate, repo)
        except (AssertionError, KeyError, TypeError, ValueError):
            continue
        raise AssertionError("D07 NEGATIVE NOT CAUGHT: " + name)
    print(f"D07 STATIC OK: 4 manual cities, {sum(len(c['facts']) for c in data['cities'])} traced facts, "
          f"{sum(len(c['unknowns']) for c in data['cities'])} UNKNOWN entries, "
          f"{sum(len(c['conceptualLayers']) for c in data['cities'])} noncanonical conceptual layers, "
          f"{len(mutations)} negative mutations, D01-D06 cross-check; NO RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print("D07 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)

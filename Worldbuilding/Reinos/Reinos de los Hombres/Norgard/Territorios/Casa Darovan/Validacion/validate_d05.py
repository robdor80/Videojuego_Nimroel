#!/usr/bin/env python3
"""D05 Darovan — auditoría estática modal, logística y MSG; NO ruta ejecutable."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
AUTH = ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"]
CITIES = ["treihord", "veldora", "taramin", "syvaris"]
PHYSICAL = {
    "d05_road_veldora_treihord": ("d05_city_veldora", "d05_city_treihord", "land_road", "not_specified"),
    "d05_belara_shallow_haul": ("d05_belara_loading_unlocated", "d05_port_treihord", "river_shallow_draft_barge", "industrial_heavy_cargo"),
    "d05_vena_restricted": ("d05_crisol", "d05_boveda", "fortified_underground_gallery", "restricted_guarded"),
}
SUPPLY = {
    "d05_ore_cart_stage", "d05_ore_port_handling",
    "d05_coal_azurios_supply", "d05_pilares_wood_supply",
}
RISK = {
    "d05_risk_shallow_belara", "d05_risk_road_weather", "d05_risk_coal_dependency",
    "d05_risk_coastal_weather", "d05_risk_thalen",
}
PENDING = {"DAR-P04", "DAR-P08", "DAR-P09", "DAR-P10", "DAR-P11"}

def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def read(repo: Path, path: str) -> dict:
    return json.loads((repo / path).read_text(encoding="utf-8"))

def validate(d: dict, repo: Path) -> None:
    check(d["schemaVersion"] == 1 and d["documentId"] == "darovan_d05_qualitative_mobility_communications"
          and d["phase"] == "D05" and d["status"] == "planning_reference_not_runtime"
          and d["canonStatus"] == "source_traced_no_new_canon", "D05 plan / no canon")
    check(d["authorityChain"] == AUTH and d["evidenceLabels"] ==
          ["AUTHORED", "DERIVED", "PROPOSAL", "UNKNOWN"], "authority / source labels")
    policy = d["geometryPolicy"]
    check(set(policy) == {
        "containsCoordinates", "containsGeometry", "containsNewNamedRoutes",
        "containsNewBridges", "containsNewFords", "containsNewHarbours",
        "containsDistances", "containsTravelTimes", "containsInventedCapacity",
        "containsNavigationSchedules", "containsRuntimeAssets", "graphIsTravelPlanner"
    } and all(value is False for value in policy.values()), "false cartographic/operational claim")
    refs = d["sourceRefs"]
    check(len(refs) == 23 and all(path.startswith("Worldbuilding/") and (repo / path).is_file()
                                  for path in refs.values()), "source paths missing")
    for key, attr in [("d01","referenceD01Relief"),("d02","referenceD02Hydro"),
                      ("d03","referenceD03Climate"),("d04","referenceD04Economy")]:
        check(d[attr] == refs[key], "cross-phase references " + key)
    relief, hydro, climate, economy, vessels, maritime, fiscal = (
        read(repo, refs[k]) for k in
        ("d01", "d02", "d03", "d04", "coreVessels", "norgardNavigation", "norgardFiscal"))
    check(relief["administration"]["darovanCities"] == CITIES, "D01 cities")
    check({x["id"] for x in relief["physicalUnits"]} == {x["id"] for x in climate["zones"]},
          "D01/D03 study units")
    check([x["id"] for x in hydro["rivers"]] == ["belara", "lhera", "veldora", "fhalion", "thalen"]
          and hydro["rivers"][0]["crossesCity"] is False
          and hydro["rivers"][1]["branchesFrom"] == "belara"
          and hydro["rivers"][4]["terminalArms"] == 2, "D02 hydro")
    check(economy["resourceSourceProtection"]["treihordCoalSource"] == "montes_azurios"
          and economy["resourceSourceProtection"]["pilaresTimberSuppliesValkramMines"] is True
          and economy["geographyProtection"]["arvenOwner"] == "casa_darovan"
          and len(economy["resourceChains"]) == 8, "D04 dependencies")
    check(vessels["status"] == "active_core_contract"
          and vessels["immutableRules"]["movementRequiresNavigableConnection"]
          and vessels["immutableRules"]["movementRespectsDraftAndWaterConstraints"],
          "Core navigation constraints")
    check(maritime["status"] == "active_realm_default"
          and maritime["civilNavigation"]["riverNavigationRequiresNavigability"]
          and fiscal["fiscalUnity"]["customsBetweenGreatHouseTerritories"] is False,
          "Norgard maritime/fiscal")
    msg_content = (repo / refs["coreMessage"]).read_text(encoding="utf-8")
    check("MSG01" in msg_content and "entregar no equivale a leer" in msg_content
          and "comunicación física no es instantánea" in msg_content, "Core MSG")

    nodes, edges, supply = d["nodes"], d["confirmedTransportLinks"], d["supplyRelationsNotRoutes"]
    node_map = {n["id"]: n for n in nodes}
    all_ids = [n["id"] for n in nodes] + [e["id"] for e in edges] + [s["id"] for s in supply]
    all_ids += [m["id"] for m in d["communicationEvidence"]] + [r["id"] for r in d["riskCandidates"]]
    all_ids += [u["id"] for u in d["unknowns"]]
    check(len(nodes) == len(node_map) == 17 and len(all_ids) == len(set(all_ids)), "unique technical IDs")
    check({n["id"] for n in nodes if n["type"] == "canonical_city"} ==
          {"d05_city_" + name for name in CITIES}, "only canonical cities")
    for n in nodes:
        check(n["provenance"] == "AUTHORED" and n["sourceRefIds"] and
              all(k in refs for k in n["sourceRefIds"]) and
              n["geometry"] is None and n["coordinates"] is None, "invented node geometry")
    check(all(node_map["d05_city_" + city]["administrativeOwner"] == "casa_darovan"
              for city in CITIES), "city authority")
    check(node_map["d05_arven_context"]["administrativeOwner"] == "casa_darovan"
          and node_map["d05_linde_context"]["type"] == "landmark_not_waypoint",
          "Arven / Linde must remain contextual")
    check(len(edges) == len(PHYSICAL) and {e["id"] for e in edges} == set(PHYSICAL),
          "injected / missing route")
    for e in edges:
        expected = PHYSICAL[e["id"]]
        check((e["from"], e["to"], e["mode"], e["access"]) == expected, "altered authored link")
        check(e["from"] in node_map and e["to"] in node_map and e["provenance"] == "AUTHORED"
              and e["relationKind"] == "attested_modal_connection_without_cartographic_path"
              and e["physicalRouteConfirmed"] is True and e["sourceRefIds"]
              and all(k in refs for k in e["sourceRefIds"])
              and e["waypoints"] == [] and e["routeGeometry"] is None
              and e["distanceKm"] is None and e["travelTime"] is None
              and e["capacity"] is None, "invented road / water path")
        check(bool(e["evidence"]) and bool(e["operationalRestriction"]), "evidence / limits missing")
    check("Linde" in next(e for e in edges if e["id"] == "d05_road_veldora_treihord")["evidence"], "Linde qualified")
    check("poco calado" in next(e for e in edges if e["id"] == "d05_belara_shallow_haul")["operationalRestriction"], "Belara draft")
    check("no tránsito público" in next(e for e in edges if e["id"] == "d05_vena_restricted")["operationalRestriction"], "Vena public route")

    check(len(supply) == len(SUPPLY) and {s["id"] for s in supply} == SUPPLY,
          "invented supply flow")
    for s in supply:
        check(s["from"] in node_map and s["to"] in node_map and s["provenance"] == "AUTHORED"
              and s["relationKind"] == "supply_or_handling_relation_not_proof_of_mapped_route"
              and s["physicalRouteConfirmed"] is False
              and s["routeGeometry"] is None and s["waypoints"] == []
              and s["distanceKm"] is None and s["travelTime"] is None and s["capacity"] is None
              and s["sourceRefIds"] and all(k in refs for k in s["sourceRefIds"]), "supply promoted to physical road")
    supplies = {s["id"]: s for s in supply}
    check(supplies["d05_coal_azurios_supply"]["transportMode"] is None
          and supplies["d05_pilares_wood_supply"]["transportMode"] is None
          and supplies["d05_coal_azurios_supply"]["from"] == "d05_azurios_coal_source"
          and supplies["d05_pilares_wood_supply"]["from"] == "d05_pilares_forest",
          "coal path / timber path invented")

    ports = {f["city"]: f for f in d["facilitiesByCity"]}
    check(len(ports) == 4 and list(ports) == CITIES, "ports and city identity")
    check({p["facilityId"] for p in ports.values()} ==
          {"d05_port_" + c for c in CITIES}, "port IDs")
    check(all(p["provenance"] == "AUTHORED" and p["linkedMaritimeRoute"] is None
              and p["sourceRefIds"] and all(k in refs for k in p["sourceRefIds"]) for p in ports.values()),
          "fabricated sea connection")
    check(ports["treihord"]["navigationLimits"] == "industrial_shallow_draft_only"
          and "commercial" in ports["veldora"]["function"]
          and ports["taramin"]["thalenArmNavigability"] is None
          and "safe_island_bay" in ports["syvaris"]["function"], "port canon")

    movement = d["movementSemantics"]
    check(movement["admissibleForActualRoutingOnly"] == list(PHYSICAL)
          and movement["graphContainsOnlyAttestedConnections"] is True
          and movement["separatedWaters"] == ["belara_lhera","veldora","fhalion","thalen"]
          and movement["thalenUniqueRiver"] is True and movement["thalenTerminalArms"] == 2
          and movement["taraminBetweenThalenArms"] is True
          and movement["lheraBranchesFrom"] == "belara"
          and movement["veldoraIndependentFromBelaraLhera"] is True
          and movement["belaraAdjacentToTreihord"] is True
          and movement["belaraCrossesTreihord"] is False
          and movement["arvenJurisdiction"] == "casa_darovan"
          and movement["fhalionNamedMinorRiver"] is True
          and movement["fhalionRiverNavigability"] is None
          and movement["fhalionCoastalOutletExact"] is None
          and movement["arvenHasDarovanRoute"] is False
          and movement["crossGreatHouseCustomsOnlyBecauseBoundary"] is False
          and movement["navigableFromKnownPortToOtherNamedPort"] is None
          and movement["genericRoadNetworkAvailability"] is None
          and movement["unknownWaypointsAllowedAsCanon"] is False
          and movement["syvarisRequiresWaterTravelToLeaveIsland"] ==
              "DERIVED_not_specific_route", "water / fiscal / Arven protection")
    check(movement["riverNetworkReference"] ==
          "d02_topology_is_hydrology_not_passenger_or_trade_navigation", "D02 nav false claim")

    messages = {m["id"]: m for m in d["communicationEvidence"]}
    check(set(messages) == {"d05_msg_treihord_caminos", "d05_msg_treihord_avisos",
                            "d05_msg_delivery_policy"}, "messages must not create postal links")
    check(messages["d05_msg_treihord_caminos"]["provenance"] == "AUTHORED"
          and messages["d05_msg_treihord_avisos"]["provenance"] == "AUTHORED"
          and "plaza_del_camino" in messages["d05_msg_treihord_caminos"]["activity"]
          and "plaza_vieja" in messages["d05_msg_treihord_avisos"]["activity"]
          and messages["d05_msg_delivery_policy"]["provenance"] == "PROPOSAL", "MSG provenance")
    check(all(m["scopeNode"] is None or m["scopeNode"] in node_map
              for m in messages.values()), "MSG orphan")
    check(all(m["networkService"] is None and m["dispatchSchedule"] is None
              for m in messages.values()), "invented postal service")

    risks = d["riskCandidates"]
    check(len(risks) == 5 and {r["id"] for r in risks} == RISK, "risk catalog")
    check(all(r["provenance"] == "DERIVED" and r["requires"]
              and r["currentClosure"] is False and r["measuredSeverity"] is None
              and r["sourceRefIds"] and all(k in refs for k in r["sourceRefIds"]) for r in risks),
          "hypothetical risk asserted as event")

    unknowns = d["unknowns"]
    check({x["id"] for x in unknowns} == PENDING and len(unknowns) == len(PENDING)
          and all(x["provenance"] == "UNKNOWN" and x["materialized"] is False for x in unknowns),
          "unapproved canon gap")
    check(d["authorship"] == {"authorApprovalRequiredForNewNamedRoutes":True,
                             "newCanonApproved":False, "pendingAuthor": sorted(PENDING)},
          "author approvals changed")
    check(d["runtimeIntegration"] == {"status":"not_implemented","validatedWithCoreRPG":False,
                                      "validatedInGodot":False, "routeFinderPresent":False,
                                      "messageDeliverySimulated":False, "cargoMoved":False,
                                      "boatsSpawned":0, "coordinatesMaterialized":0}, "runtime invented")
    check((repo / (ROOT + "Rutas_y_comunicaciones/01_red_modal_y_corredores_v0.1.md")).is_file()
          and (repo / (ROOT + "Rutas_y_comunicaciones/02_logistica_puertos_y_dependencias_v0.1.md")).is_file()
          and (repo / (ROOT + "Rutas_y_comunicaciones/03_mensajeria_riesgos_y_limites_v0.1.md")).is_file(),
          "D05 docs missing")

def run() -> None:
    here = Path(__file__).resolve()
    repo = next((p for p in here.parents if (p / "Worldbuilding").is_dir()), None)
    check(repo is not None, "repository root missing")
    original = json.loads((here.parents[1] / "Datos operativos/darovan_d05_mobility_communications_v0.1.json").read_text(encoding="utf-8"))
    validate(original, repo)
    mutations = [
        ("new_road", lambda x: x["confirmedTransportLinks"].append({**x["confirmedTransportLinks"][0], "id":"invented_new_road"})),
        ("road_endpoint", lambda x: x["confirmedTransportLinks"][0].update(to="d05_city_taramin")),
        ("road_wood", lambda x: x["confirmedTransportLinks"][0].update(waypoints=["d05_linde_context"])),
        ("distance", lambda x: x["confirmedTransportLinks"][0].update(distanceKm=20)),
        ("travel_time", lambda x: x["confirmedTransportLinks"][0].update(travelTime=2)),
        ("barge_deep", lambda x: x["confirmedTransportLinks"][1].update(mode="deep_sea_merchant")),
        ("barge_restriction", lambda x: x["confirmedTransportLinks"][1].update(operationalRestriction="all ships")),
        ("vena_public", lambda x: x["confirmedTransportLinks"][2].update(access="public")),
        ("mines_geometry", lambda x: x["nodes"][8].update(coordinates=[0,0])),
        ("bridge", lambda x: x["geometryPolicy"].update(containsNewBridges=True)),
        ("arven_owner_erased", lambda x: x["movementSemantics"].update(arvenJurisdiction=None)),
        ("arven_node_owner_erased", lambda x: x["nodes"][15].update(administrativeOwner=None)),
        ("arven_sea_link", lambda x: x["movementSemantics"].update(arvenHasDarovanRoute=True)),
        ("fhalion_navigation_invented", lambda x: x["movementSemantics"].update(fhalionRiverNavigability=True)),
        ("fhalion_missing", lambda x: x["movementSemantics"].update(separatedWaters=["belara_lhera","veldora","thalen"])),
        ("thalen_single_arm", lambda x: x["movementSemantics"].update(thalenTerminalArms=1)),
        ("veldora_join", lambda x: x["movementSemantics"].update(veldoraIndependentFromBelaraLhera=False)),
        ("belara_city", lambda x: x["movementSemantics"].update(belaraCrossesTreihord=True)),
        ("coal_belara_mode", lambda x: x["supplyRelationsNotRoutes"][2].update(transportMode="belara_barge")),
        ("coal_route_promoted", lambda x: x["supplyRelationsNotRoutes"][2].update(physicalRouteConfirmed=True)),
        ("wood_as_road", lambda x: x["supplyRelationsNotRoutes"][3].update(routeGeometry={"path":["pilares","valkram"]})),
        ("sea_route_invented", lambda x: x["facilitiesByCity"][3].update(linkedMaritimeRoute="veldora")),
        ("thalen_navigable", lambda x: x["facilitiesByCity"][2].update(thalenArmNavigability=True)),
        ("msg_route", lambda x: x["communicationEvidence"][0].update(networkService="official_post")),
        ("msg_instant", lambda x: x["communicationEvidence"][1].update(dispatchSchedule="instant")),
        ("risk_event", lambda x: x["riskCandidates"][0].update(currentClosure=True)),
        ("risk_intensity", lambda x: x["riskCandidates"][2].update(measuredSeverity=5)),
        ("pending_removed", lambda x: x["authorship"].update(pendingAuthor=["DAR-P01"])),
        ("fake_runtime", lambda x: x["runtimeIntegration"].update(validatedWithCoreRPG=True)),
        ("source_deleted", lambda x: x["sourceRefs"].update(treihord="Worldbuilding/no-such-file.md")),
        ("duplicate_id", lambda x: x["nodes"][0].update(id="d05_city_veldora")),
        ("port_identity", lambda x: x["facilitiesByCity"][1].update(function="primary_fishing_only")),
    ]
    for name, mutation in mutations:
        candidate = copy.deepcopy(original)
        mutation(candidate)
        try:
            validate(candidate, repo)
        except (AssertionError, KeyError, TypeError, ValueError):
            continue
        raise AssertionError("NEGATIVE NOT CAUGHT: " + name)
    print(f"D05 STATIC OK: {len(original['nodes'])} nodes, "
          f"{len(original['confirmedTransportLinks'])} attested modal links, "
          f"{len(original['supplyRelationsNotRoutes'])} non-route supply relations, "
          f"{len(original['sourceRefs'])} source paths, "
          f"{len(mutations)} negative mutations; NOT RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print("D05 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)

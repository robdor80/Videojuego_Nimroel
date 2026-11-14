#!/usr/bin/env python3
"""E19-R4 — Validator B2: mobility hypotheses never become roads by assertion."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DIR = EDR / "E19-R4"
PIN_R3 = "8887445eec5996d18f4c63b849f568ea39c8b0ef"
DOCS = ["README.md"] + [
    "01_JERARQUIA_Y_GRAFOS.md", "02_ATLAS_DE_CORREDORES.md",
    "03_PASOS_CRUCES_Y_TRANSICIONES.md", "04_CARGAS_VIAJEROS_Y_HITOS.md",
    "05_JURISDICCION_Y_PROTECCION.md", "06_ESTACIONALIDAD_Y_DETERIORO.md",
    "07_VIAJE_CONOCIMIENTO_Y_MEMORIA.md", "08_CONTRATO_DE_CARTOGRAFIA_2D.md",
    "09_PARIDAD_VALRIK_Y_ADVERSARIOS.md", "10_ACTA_Y_TRASPASO_R5.md",
]
SEQUENCE = [
    "Valkram eastern slope", "Río Lurien", "Lago Antela",
    "Río Lurien", "Hallheim", "Golfo de Norgard"
]
NAMES = [
    "Dorth–Lumina", "Lumina–Karsath", "Dorth–Karsath", "Dorth–Rodas",
    "Valkram oriental", "Piedemonte–Karsath", "Campiña central",
    "Lumina–Bosque Alto", "Dorth–Azurios occidental",
    "Karsath–Antela/Lurien", "Red mayor de Norgard",
    "Norte sin delimitar"
]
CONTEXTS = [
    ["MF-06","MF-04","MF-05"], ["MF-05","MF-04","MF-03"],
    ["MF-06","MF-04","MF-03"], ["MF-06","MF-04","MF-07"],
    ["MF-01","MF-02"], ["MF-02","MF-03"], ["MF-04"], ["MF-05"],
    ["MF-06"], ["MF-03"], ["MF-04"], ["MF-08"]
]
E05_SOURCES = [
    "edr_e05_question_dorth_lumina", "edr_e05_question_lumina_karsath",
    "edr_e05_question_dorth_karsath", "edr_e05_question_dorth_rodas",
    "edr_e05_question_valkram", None, None, None, None, None,
    "edr_e05_external_edranor_realm", None
]
REASONS = [
    "WINE_AND_MARKET", "WINE_AND_SUPPLIES",
    "E04_TRADE_ONLY_NO_E01_CORRIDOR", "CROWN_PERMISSION_REQUIRED",
    "MOUNTAIN_PASS_UNCONFIRMED", "FOOTHILL_TRANSITION_ONLY",
    "LOCAL_RURAL_ACCESS_UNPROVEN", "FOREST_PERMIT_AND_ACCESS",
    "AZURIOS_WEST_ONLY", "LAKE_RIVER_INTERFACE_UNPROVEN",
    "EXTERNAL_NETWORK_UNPROVEN", "NORTH_NOT_EVALUABLE"
]
TYPES = [
    "TERRITORIAL_SUPPLY", "VINTAGE_RURAL", "CONTROLLED_FOREST",
    "LOCAL_FOOTPATH", "MOUNTAIN_PASS", "WATER_CROSSING",
    "INSTITUTIONAL_ACCESS", "SERVICE_AND_EMERGENCY"
]
FREIGHT = [
    "DORTH_RED_WINE", "LUMINA_WHITE_FAIR", "KARSATH_SELECTED_WINE",
    "LICENSED_BOSQUE_ALTO_WOOD", "HOUSEHOLD_SUPPLIES",
    "REAL_MESSENGER", "VERIFIED_PATROL_EMERGENCY"
]
HAZARDS = [
    "SATURATED_SOIL_MUD", "THAW_SLOPE_INSTABILITY", "LOCAL_FREEZE_ICE",
    "VERIFIED_WATER_CROSSING_FLOOD", "DUST_WEAR",
    "AUTHORIZED_HEAVY_FOREST_TRAFFIC", "DOCUMENTED_TREEFALL",
    "DOCUMENTED_ROCKFALL", "ACTUAL_FAIR_HARVEST_CONGESTION",
    "INSPECTED_MAINTENANCE_DEFICIT"
]
GATES = [
    "MAPPED_GEOMETRY_AND_CONTINUITY", "VALID_PARENT_CONTEXT_AND_JURISDICTION",
    "REAL_GRADIENT_AND_STABILITY", "SOIL_AND_SEASON_SUPPORT",
    "LOCAL_HYDROLOGY_RECEIVER", "ALL_CROSSINGS_SURVEYED",
    "LAND_TITLE_AND_SERVITUDE", "FOREST_AND_CROWN_PERMISSIONS",
    "MODE_AND_CAPACITY_SURVEYED", "MAINTENANCE_AND_RISK",
    "FIELD_REVIEW_AND_PROVENANCE", "B3_EDITORIAL_APPROVAL"
]
ZERO = [
    "physicalEdges", "physicalNodes", "actualRoads", "bridges", "fords",
    "tunnels", "ferries", "roadStations", "signposts", "installedMessengers",
    "activeConvoys", "playerRoutes", "worldStateEntities"
]
GUARDS = {
    "NO_PR84_REUSE", "NO_NORTH_MF08_ROUTE", "NO_QUESTION_GRAPH_AS_PHYSICAL",
    "NO_UNVERIFIED_MOUNTAIN_PASS", "NO_WATER_CROSSING_FROM_HS_TEMPLATES",
    "NO_BRIDGE_FORD_FERRY_WITHOUT_SURVEY", "NO_KARSATH_PORT",
    "NO_DORTH_CALERAN", "NO_RODAS_EDRANOR_TAXES",
    "NO_CROWN_FOREST_APPROPRIATION", "NO_BOSQUE_ALTO_UNLICENSED_ACCESS",
    "NO_INTERNAL_CUSTOMS", "NO_TRESKAL_GEOMETRY_COPY",
    "NO_INVENTED_METRICS", "NO_INSTANT_SHIPPING_OR_MESSAGING",
    "NO_AUTO_WINTER_CLOSURE", "NO_B3_B4_UPGRADE",
    "NO_UNKNOWN_TO_APPROVED"
}
UNKNOWN = {
    "GEOMETRY_CRS_NORTH", "LOCAL_MOUNTAIN_PASSES", "REAL_ROADS",
    "SOILS_AND_SLOPES_OF_SECTIONS", "REAL_WATER_CROSSINGS",
    "SERVITUDES_OWNERSHIP", "ROAD_CAPACITY_AND_MAINTENANCE",
    "RODAS_CROWN_ACCESS", "LOCAL_WEATHER_OBSERVATIONS",
    "REAL_NORGARD_EXTERNAL_NETWORK"
}

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def problems(c: dict, p: dict, h: dict, g: dict, e05: dict) -> list[str]:
    errors: list[str] = []
    def ck(condition: bool, label: str) -> None:
        if not condition:
            errors.append(label)
    try:
        ck(c.get("schemaVersion") == 5 and c.get("documentId") == "edranor_e19_r4_routes"
           and c.get("phase") == "E19-R4", "schema/version")
        ck(c.get("status") == "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME"
           and c.get("authority") == "ASSISTANT_DELEGATED_DESIGN"
           and c.get("precedent") == "VALRIK_GEOGRAFIA_LOCAL_TRESKAL_ROADS_AND_TRAVEL",
           "authority and precedent")
        ck(c.get("parent") == {
            "phase":"E19-R3", "headSha":PIN_R3,
            "documentId":"edranor_e19_r3_land_ecology",
            "schemaVersion":4, "rejectedPR84Used":False
        }, "R3 lineage and PR84 ban")
        ck(p.get("documentId") == "edranor_e19_r3_land_ecology"
           and p.get("schemaVersion") == 4
           and h.get("documentId") == "edranor_e19_r2_hydrology"
           and g.get("schemaVersion") == 2
           and e05.get("documentId") == "edranor_e05_roads_communications",
           "source contracts")
        ck(e05.get("scope", {}).get("physicalEdges") == []
           and e05.get("scope", {}).get("roadPolylines") == []
           and e05.get("scope", {}).get("pathfindingEnabled") is False, "E05 question graph not physical")
        gov = c["governance"]
        pg = p["governance"]
        ck(all(gov.get(k) == pg.get(k) for k in (
            "west","east","south","northArtificialClosure","northSketchJoined",
            "hallheim","bosqueAltoHarvest","bosqueReal","caleranThroughDorthConfirmed",
            "karsathUrbanAntelaShoreConfirmed","sourceHydrologySequence"
        )) and gov.get("sourceHydrologySequence") == h["majorSystem"]["sequence"] == SEQUENCE,
           "borders/river canon")
        ck(gov.get("rodas") == {
            "kind":"ALDEA","jurisdiction":"crown_aethros",
            "edranorTaxes":False,"edranorCommand":False
        } and gov.get("noInternalCustoms") is True, "Crown and customs")
        ck(g["boundaries"]["west"]["easternSlope"] == "casa_edranor"
           and g["boundaries"]["east"]["westernSlope"] == "casa_edranor"
           and g["jurisdiction"]["rodas"] == "crown_aethros", "R1 authority")
        m=c["maturity"]
        ck(m.get("b2Documentary") is True and m.get("b3Mapped") is False
           and m.get("b4Runtime") is False, "maturity B2")
        ck(all(m.get(k) is None for k in (
            "geometry","crs","measuredDistances","measuredSpeeds",
            "measuredRoadWidths","measuredTravelTimes")), "no invented metrics")
        ck(all(m.get(k) == 0 for k in ZERO), "zero physical instances")
        n=c["networks"]
        ck(n.get("demand") == "REQUIREMENTS_ONLY"
           and n.get("questions") == "NON_TRAVERSABLE"
           and n.get("physical") == "EMPTY_NOT_CERTIFIED"
           and n.get("pathfindingEnabled") is False
           and n.get("routeDispatchEnabled") is False
           and n.get("candidateQuestionsCount") == 11, "separate graphs")
        ck(n.get("acceptedPhysicalGraph") == {"nodes":[],"edges":[]}
           and n.get("roadGeometry") == [] and n.get("crossingAssets") == [],
           "no Gp/crossings")
        t=c["roadTypes"]
        ck(len(t) == 8 and [i.get("id") for i in t] ==
           [f"TC-{j:02d}" for j in range(1,9)]
           and [i.get("name") for i in t] == TYPES, "road class catalogue")
        ck(all(i.get("status") == "TEMPLATE_NOT_ASSIGNED"
               and i.get("actualSegments") == 0
               and i.get("approvedWidth") is None
               and i.get("approvedCapacity") is None for i in t), "road class not instantiated")
        ctx=c["corridorQuestions"]
        ck(len(ctx) == 12 and [q.get("id") for q in ctx] ==
           [f"CT-{j:02d}" for j in range(1,13)]
           and [q.get("name") for q in ctx] == NAMES, "CT catalogue")
        ck([q.get("contextIds") for q in ctx] == CONTEXTS
           and [q.get("sourceQuestionId") for q in ctx] == E05_SOURCES
           and [q.get("studyReason") for q in ctx] == REASONS, "CT contexts and provenance")
        valid_sources = {x["id"] for x in e05["candidateRoadQuestions"]}
        valid_sources.add(e05["passQuestion"]["id"])
        valid_sources.update(x["id"] for x in e05["externalInterfaces"])
        ck(all(x is None or x in valid_sources for x in E05_SOURCES), "E05 links")
        ck([q.get("status") for q in ctx] ==
           ["STUDY_ONLY_NOT_A_ROUTE"]*11+["DENIED_UNASSESSED"],
           "CT12 north blocked")
        ck(all(q.get("actualRoute") is False and q.get("geometry") is None
               and q.get("length") is None and q.get("travelTime") is None
               and q.get("waterCrossings") is None and q.get("slopeEvidence") is None
               and q.get("soilEvidence") is None and q.get("rights") == "UNKNOWN"
               and q.get("capacity") is None and q.get("surface") == "UNKNOWN"
               and q.get("seasonality") == "UNKNOWN" and q.get("physicalEdgeIds") == []
               and q.get("approvedNodes") == [] and q.get("gqOnly") is True
               and q.get("worldStateId") is None for q in ctx), "CT nonmaterialized")
        ck(all("MF-08" not in q["contextIds"] for q in ctx[:11])
           and ctx[-1]["contextIds"] == ["MF-08"]
           and p["contexts"][-1]["status"] == "NON_EVALUABLE", "MF08 ban")
        freight=c["freightStudies"]
        ck(len(freight) == 7
           and [x.get("id") for x in freight] ==
           [f"FS-{j:02d}" for j in range(1,8)]
           and [x.get("name") for x in freight] == FREIGHT, "freight catalogue")
        ck(all(x.get("status") == "FLOW_CONDITIONAL_NOT_DISPATCHED"
               and x.get("realShipments") == 0
               and x.get("approvedItinerary") is None
               and x.get("agent") is None and x.get("cargo") is None
               for x in freight), "freight not performed")
        hz=c["seasonalHazards"]
        ck(len(hz) == 10 and [x.get("id") for x in hz] ==
           [f"HZ-{j:02d}" for j in range(1,11)]
           and [x.get("name") for x in hz] == HAZARDS, "hazard catalogue")
        ck(all(x.get("status") == "SCENARIO_ONLY"
               and x.get("observedEvent") is False
               and x.get("routeInstance") is None
               and x.get("closure") is None and x.get("measurement") is None
               and x.get("triggerEvidence") == "REQUIRES_OBSERVATION"
               and x.get("persistentIfMaterialized") is True for x in hz),
           "hazards conditional")
        ck(c.get("promotionGates") == GATES
           and c.get("requiredToTravel") == [
            "CERTIFIED_PHYSICAL_EDGE_CHAIN", "LEGAL_ACCESS_PER_ACTOR",
            "MODE_CAPACITY", "CURRENT_ROUTE_STATE", "REAL_AGENT_AND_CARGO_IF_ANY"
           ], "promotion and travel gates")
        ck(set(c.get("unknown",[])) == UNKNOWN, "unknowns preserved")
        ck(set(c.get("hardGuards",[])) == GUARDS, "hard guards")
        ck(c.get("handoff") == {
            "R5":"SETTLEMENT_ACCESS_REQUIRES_CERTIFIED_PHYSICAL_GRAPH",
            "R6":"VALRIK_PARITY_AUDIT_PENDING",
            "TEC":"GODOT_2D_AND_WORLD_STATE_AFTER_B3"
           }, "handoff")
        ck(c.get("evidencePriority") == [
            "CANON_AUTOR","CANON_REPO","FIELD_SURVEY",
            "ASSISTANT_DELEGATED_DESIGN","UNKNOWN"
           ], "provenance")
    except (KeyError, TypeError, ValueError, IndexError, AttributeError) as ex:
        errors.append("malformed: "+str(ex))
    return errors

def synthetic_gate(f: dict) -> bool:
    """Logical test of FUTURE approval, never actual certification."""
    for gate in GATES:
        if f.get(gate) is not True:
            return False
    if f.get("jurisdiction") not in {"casa_edranor","crown_aethros"}:
        return False
    if f.get("context") == "MF-08" or f.get("pr84") or f.get("internal_customs"):
        return False
    if f.get("question_only") or f.get("unresolved_gap") or f.get("invented_metric"):
        return False
    if f.get("context") not in {f"MF-{i:02d}" for i in range(1,8)}:
        return False
    if f.get("jurisdiction") == "crown_aethros" and f.get("royal_agreement") is not True:
        return False
    if f.get("crosses_water") and f.get("real_crossing_permission") is not True:
        return False
    if f.get("forest_area") == "bosque_alto" and f.get("forest_rights") is not True:
        return False
    if f.get("forest_area") == "bosque_real" and f.get("royal_agreement") is not True:
        return False
    if f.get("crosses_divide") and f.get("both_sides_permission") is not True:
        return False
    if f.get("current_block") is True:
        return False
    return True

def mutation_suite(c: dict, p: dict, h: dict, g: dict, e: dict) -> int:
    changes: list[tuple[str,object]] = [
        ("version",lambda a:a.__setitem__("schemaVersion",6)),
        ("phase",lambda a:a.__setitem__("phase","E19-R5")),
        ("authority",lambda a:a.__setitem__("authority","CANON_REPO")),
        ("precedent",lambda a:a.__setitem__("precedent","VALRIK_GEOMETRY")),
        ("parent",lambda a:a["parent"].__setitem__("headSha","wrong")),
        ("pr84",lambda a:a["parent"].__setitem__("rejectedPR84Used",True)),
        ("west",lambda a:a["governance"].__setitem__("west","DAROVAN_EAST")),
        ("east",lambda a:a["governance"].__setitem__("east","EDRANOR_EAST")),
        ("south",lambda a:a["governance"].__setitem__("south","LURIEN_FULL_BORDER")),
        ("north",lambda a:a["governance"].__setitem__("northArtificialClosure",True)),
        ("join",lambda a:a["governance"].__setitem__("northSketchJoined",True)),
        ("rodas",lambda a:a["governance"]["rodas"].__setitem__("jurisdiction","casa_edranor")),
        ("rodas_kind",lambda a:a["governance"]["rodas"].__setitem__("kind","CIUDAD")),
        ("rodas_tax",lambda a:a["governance"]["rodas"].__setitem__("edranorTaxes",True)),
        ("rodas_command",lambda a:a["governance"]["rodas"].__setitem__("edranorCommand",True)),
        ("hallheim",lambda a:a["governance"].__setitem__("hallheim","INSIDE_EDRANOR")),
        ("alto",lambda a:a["governance"].__setitem__("bosqueAltoHarvest","OPEN")),
        ("real",lambda a:a["governance"].__setitem__("bosqueReal","casa_edranor")),
        ("caleran",lambda a:a["governance"].__setitem__("caleranThroughDorthConfirmed",True)),
        ("antela",lambda a:a["governance"].__setitem__("karsathUrbanAntelaShoreConfirmed",True)),
        ("river",lambda a:a["governance"]["sourceHydrologySequence"].reverse()),
        ("customs",lambda a:a["governance"].__setitem__("noInternalCustoms",False)),
        ("b3",lambda a:a["maturity"].__setitem__("b3Mapped",True)),
        ("b4",lambda a:a["maturity"].__setitem__("b4Runtime",True)),
        ("geometry",lambda a:a["maturity"].__setitem__("geometry",{})),
        ("metric",lambda a:a["maturity"].__setitem__("measuredTravelTimes",5)),
        ("graph",lambda a:a["networks"]["acceptedPhysicalGraph"]["edges"].append({"id":"fake"})),
        ("pathfinding",lambda a:a["networks"].__setitem__("pathfindingEnabled",True)),
        ("dispatch",lambda a:a["networks"].__setitem__("routeDispatchEnabled",True)),
        ("question_count",lambda a:a["networks"].__setitem__("candidateQuestionsCount",12)),
        ("road_geometry",lambda a:a["networks"]["roadGeometry"].append([1,2])),
        ("crossing",lambda a:a["networks"]["crossingAssets"].append({"bridge":"fake"})),
        ("types_count",lambda a:a["roadTypes"].pop()),
        ("type_status",lambda a:a["roadTypes"][0].__setitem__("status","OPEN")),
        ("type_width",lambda a:a["roadTypes"][0].__setitem__("approvedWidth",6.2)),
        ("ct_count",lambda a:a["corridorQuestions"].pop()),
        ("ct_wrong_source",lambda a:a["corridorQuestions"][2].__setitem__("sourceQuestionId","false")),
        ("ct_wrong_context",lambda a:a["corridorQuestions"][0].__setitem__("contextIds",["MF-08"])),
        ("ct12",lambda a:a["corridorQuestions"][-1].__setitem__("status","OPEN")),
        ("freight_count",lambda a:a["freightStudies"].pop()),
        ("hazards_count",lambda a:a["seasonalHazards"].pop()),
        ("gate",lambda a:a["promotionGates"].pop()),
        ("travel_gate",lambda a:a["requiredToTravel"].pop()),
        ("hard_guard",lambda a:a["hardGuards"].remove("NO_PR84_REUSE")),
        ("unknown",lambda a:a["unknown"].remove("REAL_ROADS")),
        ("handoff",lambda a:a["handoff"].__setitem__("TEC","COMPLETE")),
        ("priority",lambda a:a["evidencePriority"].reverse()),
    ]
    for key in ZERO:
        changes.append((key,lambda a,k=key:a["maturity"].__setitem__(k,1)))
    for i in range(12):
        changes.append((f"CT-{i+1:02d} promoted",
                        lambda a,j=i:a["corridorQuestions"][j].__setitem__("actualRoute",True)))
        changes.append((f"CT-{i+1:02d} geometry",
                        lambda a,j=i:a["corridorQuestions"][j].__setitem__("geometry",[[1,2]])))
    for i in range(7):
        changes.append((f"FS-{i+1:02d} dispatch",
                        lambda a,j=i:a["freightStudies"][j].__setitem__("realShipments",1)))
    for i in range(10):
        changes.append((f"HZ-{i+1:02d} event",
                        lambda a,j=i:a["seasonalHazards"][j].__setitem__("observedEvent",True)))
    for label,mutate in changes:
        x=copy.deepcopy(c)
        mutate(x)
        assert problems(x,p,h,g,e), "Mutation escaped: "+label
    return len(changes)

def synthetic_suite() -> int:
    base={**{k:True for k in GATES},
          "jurisdiction":"casa_edranor", "context":"MF-04"}
    assert synthetic_gate(base)
    count=1
    for gate in GATES:
        t=dict(base);t[gate]=False
        assert not synthetic_gate(t), gate
        count+=1
    for flag in ("pr84","internal_customs","question_only",
                 "unresolved_gap","invented_metric","current_block"):
        t=dict(base);t[flag]=True
        assert not synthetic_gate(t), flag
        count+=1
    for ctx in ("MF-08","MF-00","UNKNOWN"):
        t=dict(base);t["context"]=ctx
        assert not synthetic_gate(t)
        count+=1
    for jurisdiction in ("casa_darovan","casa_galdren","UNKNOWN","crown_aethros"):
        t=dict(base);t["jurisdiction"]=jurisdiction
        assert not synthetic_gate(t)
        count+=1
    cases=[
        ("crown allowed",{"jurisdiction":"crown_aethros","royal_agreement":True},True),
        ("water unverified",{"crosses_water":True},False),
        ("water authorized",{"crosses_water":True,"real_crossing_permission":True},True),
        ("forest unlicensed",{"forest_area":"bosque_alto"},False),
        ("forest authorized",{"forest_area":"bosque_alto","forest_rights":True},True),
        ("royal forest unlicensed",{"forest_area":"bosque_real"},False),
        ("royal forest authorized",{"forest_area":"bosque_real","royal_agreement":True},True),
        ("divide no consent",{"crosses_divide":True},False),
        ("divide consent",{"crosses_divide":True,"both_sides_permission":True},True)
    ]
    for label,patch,expected in cases:
        assert synthetic_gate({**base,**patch}) is expected, label
        count+=1
    return count

def main() -> None:
    c=load(DIR/"routes_v0.5.json")
    p=load(EDR/"E19-R3"/"environment_v0.4.json")
    h=load(EDR/"E19-R2"/"hydrology_v0.3.json")
    g=load(EDR/"E19-R1"/"natural_features_v0.2.json")
    e=load(EDR/"Datos operativos"/"edranor_e05_roads_communications_v0.1.json")
    errors=problems(c,p,h,g,e)
    assert not errors, "R4 contract failed: "+", ".join(errors)
    for name in DOCS:
        doc=(DIR/name).read_text(encoding="utf-8")
        assert len(doc) >= 1100, "Missing/thin document: "+name
    assert "Rodas" in (DIR/"05_JURISDICCION_Y_PROTECCION.md").read_text(encoding="utf-8")
    assert "Valrik" in (DIR/"09_PARIDAD_VALRIK_Y_ADVERSARIOS.md").read_text(encoding="utf-8")
    assert "MF-08" in (DIR/"02_ATLAS_DE_CORREDORES.md").read_text(encoding="utf-8")
    muts=mutation_suite(c,p,h,g,e)
    syn=synthetic_suite()
    print(f"E19-R4 B2 PASS: {len(DOCS)} documents, 12 corridor questions, 8 types, "
          f"7 freight models, 10 hazards, {muts} negative mutations, "
          f"{syn} synthetic gate scenarios; Gp=0; B3/B4 NOT CERTIFIED")

if __name__ == "__main__":
    main()

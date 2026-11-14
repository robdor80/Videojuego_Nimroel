#!/usr/bin/env python3
"""E19-R2: contrato de cuencas y dinámica no métrica + mutaciones adversariales."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
R0, R1, R2 = EDR / "E19-R0", EDR / "E19-R1", EDR / "E19-R2"
DOCS = [
    "README.md", "01_CUENCAS_Y_DIVISORIAS.md",
    "02_RED_MENOR_Y_CONECTIVIDAD.md",
    "03_MANANTIALES_RECARGA_Y_HUMEDALES.md",
    "04_BALANCE_ESTACIONAL_RIESGOS.md",
    "05_AGUA_SUELO_BOSQUE_VINO_Y_ASENTAMIENTOS.md",
    "06_CONTRATO_CAUSAL_GENERACION_Y_PERSISTENCIA.md",
    "07_AUDITORIA_PARIDAD_Y_TRASPASO_R3.md"
]
SEQUENCE = ["Valkram eastern slope", "Río Lurien", "Lago Antela",
            "Río Lurien", "Hallheim", "Golfo de Norgard"]
GUARDS = {
    "NO_FAKE_NORTH_JOIN", "NO_REJECTED_PR84", "NO_RIVER_WITHOUT_RECEIVER",
    "NO_CYCLE", "NO_UPHILL_FLOW", "NO_KARSATH_URBAN_PORT",
    "NO_DORTH_MAJOR_RIVER", "NO_CALERAN_DORTH_TRANSFER",
    "NO_BELARA_EAST_TRANSFER", "NO_RODAS_CROWN_TRANSFER",
    "NO_ROYAL_FOREST_HARVEST", "NO_FREE_IRRIGATION", "NO_B3_B4_CLAIM",
}
SPRING_CAUSES = {"CONTACT_LAYER", "FRACTURE_AQUIFER", "COLLUVIAL_TOE",
                 "VALLEY_FLOOR_WATERTABLE", "FOREST_SHADED_SEEP"}
WETLAND_CAUSES = {"CLOSED_OR_SLOW_DRAIN_DEPRESSION", "FLOODPLAIN_BACKWATER",
                  "FOREST_SEEP_SATURATION"}


def failures(data: dict, r1: dict, r0: dict) -> list[str]:
    bad: list[str] = []
    def require(condition: bool, message: str) -> None:
        if not condition:
            bad.append(message)
    try:
        require(data.get("schemaVersion") == 3 and
                data.get("documentId") == "edranor_e19_r2_hydrology" and
                data.get("phase") == "E19-R2", "schema")
        require(data.get("status") == "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME" and
                data.get("authority") == "ASSISTANT_DELEGATED_DESIGN" and
                data.get("precedent") == "VALRIK_GEOGRAFIA_LOCAL", "authority")
        base = data["base"]
        require(base == {"r0HeadSha": "addd767de9bf27ef35e8aef6d68cde00dea79c10",
                         "r1HeadSha": "4472e81a88eba7a8e42528043ee426d685c76cef",
                         "parentPhase": "E19-R1", "rejectedPR84Used": False}, "lineage")
        require(r1.get("parentHeadSha") == base["r0HeadSha"] and
                r1.get("schemaVersion") == 2 and
                r0.get("schemaVersion") is not None, "source parents")
        mat = data["materialization"]
        require(mat.get("implementedInGodot") is False and all(
                    mat.get(k) == 0 for k in (
                        "worldStateEntities", "actualMinorRivers", "actualSprings",
                        "actualWetlands", "actualRoads", "actualWaterRights")), "no runtime")
        require(all(mat.get(k) is None for k in (
            "geometry", "projection", "measuredDischarge", "measuredAltitude",
            "measuredArea")), "no fake metric")
        major = data["majorSystem"]
        require(major.get("sequence") == SEQUENCE and
                major.get("sourceSlope") == "VALKRAM_EAST" and
                major.get("antelaRelativeToKarsath") == "SOUTH", "major river chain")
        require(all(major.get(k) is False for k in (
            "urbanKarsathShoreConfirmed", "majorDorthRiverConfirmed",
            "caleranAtDorthConfirmed")), "unproven river/shore")
        require(major.get("caleranNorgardSource") ==
                "AZURIOS_WEST_GENERAL_CANON_LOCAL_PATH_UNKNOWN" and
                major.get("lurienNavigationFrom") == "Hallheim", "Caleran/navigation")
        require(major.get("southBorderOnlyPartialLurien") is True and
                major.get("southBorderSegment") is None, "south border")
        div = data["divides"]
        require(div["valkram"] == {"westernSlope": "casa_darovan",
                                   "easternSlope": "casa_edranor"}, "Valkram")
        require(div["azurios"] == {"westernSlope": "casa_edranor",
                                   "easternSlope": "casa_galdren"}, "Azurios")
        require(div.get("northArtificialClosure") is False and
                div.get("northRedSketchLinesJoin") is False and
                div.get("farNorthMF08") == "NON_EVALUABLE", "north not closed")
        j = data["jurisdiction"]
        require(j.get("rodas") == "crown_aethros" and
                j.get("rodasType") == "ALDEA" and
                j.get("hallheim") == "OUTSIDE_EDRANOR" and
                j.get("bosqueAltoHarvest") == "PERMIT_REQUIRED" and
                j.get("bosqueReal") == "crown_aethros", "jurisdictions")
        contexts = [f"MF-{i:02d}" for i in range(1, 9)]
        require(data.get("contextIds") == contexts and
                [x.get("id") for x in r1["physicalRegions"]] == contexts and
                r1["physicalRegions"][-1].get("evaluable") is False, "R1 contexts")
        basins = data["basinFamilies"]
        require(len(basins) == 7 and
                [b.get("id") for b in basins] == [f"HC-{i:02d}" for i in range(1, 8)] and
                [b.get("contextId") for b in basins] == contexts[:7], "seven basins")
        require(all(b.get("status") == "DESIGN_FAMILY_UNLOCATED" and
                    b.get("evaluable") is True and b.get("receiver") == "UNKNOWN" and
                    b.get("geometry") is None and b.get("flowMeasurements") is None and
                    b.get("jurisdictionChange") is False and
                    len(b.get("receiverCandidates", [])) == 5 and
                    b.get("guard") and b.get("densityClass") and b.get("name")
                    for b in basins), "basins not materialized")
        require(len({b["name"] for b in basins}) == 7 and
                not any(b.get("contextId") == "MF-08" for b in basins), "no U7 basin")
        scenarios = data["minorDrainageScenarios"]
        require(len(scenarios) == 14 and
                [s.get("id") for s in scenarios] ==
                [f"HS-{i:02d}" for i in range(1, 15)], "14 scenarios")
        require(all(s.get("basinId") == f"HC-{(i // 2)+1:02d}" and
                    s.get("status") == "SCENARIO_UNLOCATED" and
                    s.get("sourceEvidence") == "NOT_VERIFIED" and
                    s.get("receiver") == "UNKNOWN" and
                    s.get("regime") == "UNKNOWN" and
                    s.get("geometry") is None and
                    s.get("materialized") is False and
                    s.get("worldStateId") is None and s.get("riverName") is None and
                    bool(s.get("sourceCause")) and bool(s.get("name"))
                    for i, s in enumerate(scenarios)), "scenario not river")
        require(len({s["name"] for s in scenarios}) == 14, "scenario name duplicate")
        springs = data["springTypes"]
        require(len(springs) == 5 and
                [s.get("id") for s in springs] == [f"SP-{i:02d}" for i in range(1, 6)] and
                {s.get("cause") for s in springs} == SPRING_CAUSES, "five spring mechanisms")
        require(all(s.get("status") == "TYPE_ONLY" and s.get("confirmed") is False
                    and s.get("geometry") is None and s.get("flow") is None and
                    s.get("waterRights") is None and len(s.get("requires", [])) == 4 and
                    bool(s.get("basinIds")) and
                    set(s.get("basinIds", [])) <= {b["id"] for b in basins}
                    for s in springs), "spring status/recharge")
        wetlands = data["wetlandTypes"]
        require(len(wetlands) == 3 and
                [w.get("id") for w in wetlands] == ["WH-01", "WH-02", "WH-03"] and
                {w.get("cause") for w in wetlands} == WETLAND_CAUSES, "wetland types")
        require(all(w.get("status") == "TYPE_ONLY" and
                    w.get("confirmed") is False and w.get("area") is None and
                    w.get("receiver") == "UNKNOWN" and
                    len(w.get("requires", [])) == 3 for w in wetlands), "wetland status")
        require(data.get("regimes") == ["PERMANENT_IF_EVIDENCED",
                                        "SEASONAL_IF_EVIDENCED",
                                        "EPHEMERAL_IF_EVIDENCED", "UNKNOWN"], "regime")
        require(len(data.get("seasonalProcesses", [])) == 6 and
                "SNOW_ACCUMULATION_IF_VERIFIED" in data["seasonalProcesses"], "seasons")
        graph = data["graphContract"]
        require(graph.get("directedAcyclic") is True and
                graph.get("receiverRequiredBeforeMaterialization") is True and
                graph.get("uphillFlowForbidden") is True and
                graph.get("closedSinkRequiresBalance") is True and
                graph.get("minorGraphEdges") == [] and
                graph.get("waterRightsImplied") is False, "graph contract")
        required_unknowns = {"ALL_MINOR_RECEIVERS", "GROUNDWATER_CONNECTIONS",
                             "LURIEN_BORDER_SEGMENT", "WATER_USE_RIGHTS"}
        require(required_unknowns <= set(data.get("reservedUnknowns", [])), "unknowns")
        require(set(data.get("prohibitions", [])) == GUARDS, "prohibitions")
        phases = data.get("futurePhases", {})
        require(phases.get("R3") == "SOILS_MICROCLIMATES_PENDING" and
                phases.get("R4") == "ROUTES_PENDING" and
                phases.get("R5") == "OCCUPATION_PENDING" and
                phases.get("R6") == "AUDIT_PENDING" and
                phases.get("TEC") == "GODOT_COORDINATES_DEFERRED", "future gates")
    except (KeyError, TypeError, ValueError, AttributeError) as exc:
        bad.append(f"malformed contract: {exc}")
    return bad


def check_graph(nodes: list[dict]) -> list[str]:
    """Puerta semántica sintética para futuros cursos, no crea cauces reales."""
    errors: list[str] = []
    ids = [n.get("id") for n in nodes]
    if len(ids) != len(set(ids)):
        return ["duplicate IDs"]
    by_id = {n["id"]: n for n in nodes if n.get("id")}
    for n in nodes:
        target = n.get("receiver")
        if not target or target not in by_id:
            errors.append("dangling receiver")
        elif n.get("height") is not None and by_id[target].get("height") is not None:
            if n["height"] < by_id[target]["height"]:
                errors.append("uphill")
        if n.get("kind") == "SINK" and not n.get("balanced", False):
            errors.append("unbalanced sink")
        if n.get("rightsImplied", False):
            errors.append("water rights inferred")
    for start in by_id:
        visited: set[str] = set()
        node = start
        while node in by_id and node not in visited:
            visited.add(node)
            target = by_id[node].get("receiver")
            if target == node:
                # El sumidero terminal puede autoseñalarse únicamente si está balanceado.
                if by_id[node].get("kind") != "SINK" or not by_id[node].get("balanced"):
                    errors.append("self loop")
                break
            node = target
        if node in visited and by_id.get(node, {}).get("kind") != "SINK":
            errors.append("cycle")
    return sorted(set(errors))


def check_docs() -> None:
    for name in DOCS:
        content = (R2 / name).read_text(encoding="utf-8")
        assert len(content) >= 1600, f"short/missing: {name}"
        assert "E19-R2" in content, name
    txt = "\n".join((R2 / name).read_text(encoding="utf-8") for name in DOCS)
    for word in ("Lurien", "Antela", "Valkram", "Azurios", "Karsath",
                 "Dorth", "Lumina", "Rodas", "Hallheim", "Caleran", "Bosque Alto"):
        assert word in txt, word


def negative_mutations(data: dict, r1: dict, r0: dict) -> int:
    scenarios = [
        ("falsify schema", lambda a: a.update(schemaVersion=4)),
        ("rejected PR reused", lambda a: a["base"].update(rejectedPR84Used=True)),
        ("wrong lineage", lambda a: a["base"].update(r1HeadSha="fake")),
        ("fake runtime", lambda a: a["materialization"].update(implementedInGodot=True)),
        ("invented river", lambda a: a["materialization"].update(actualMinorRivers=1)),
        ("invented spring", lambda a: a["materialization"].update(actualSprings=1)),
        ("invented wetland", lambda a: a["materialization"].update(actualWetlands=1)),
        ("fake water right", lambda a: a["materialization"].update(actualWaterRights=1)),
        ("measured flow", lambda a: a["materialization"].update(measuredDischarge=20)),
        ("fake projection", lambda a: a["materialization"].update(projection="EPSG:4326")),
        ("incorrect river order", lambda a: a["majorSystem"]["sequence"].reverse()),
        ("Antela north", lambda a: a["majorSystem"].update(antelaRelativeToKarsath="NORTH")),
        ("Karsath port", lambda a: a["majorSystem"].update(urbanKarsathShoreConfirmed=True)),
        ("Dorth major river", lambda a: a["majorSystem"].update(majorDorthRiverConfirmed=True)),
        ("Caleran in Dorth", lambda a: a["majorSystem"].update(caleranAtDorthConfirmed=True)),
        ("Caleran transfer", lambda a: a["majorSystem"].update(caleranNorgardSource="DORTH")),
        ("navigation upriver", lambda a: a["majorSystem"].update(lurienNavigationFrom="Karsath")),
        ("whole southern border river", lambda a: a["majorSystem"].update(southBorderOnlyPartialLurien=False)),
        ("invented southern segment", lambda a: a["majorSystem"].update(southBorderSegment="invented")),
        ("Valkram slope inverted", lambda a: a["divides"]["valkram"].update(easternSlope="casa_darovan")),
        ("Azurios slope inverted", lambda a: a["divides"]["azurios"].update(westernSlope="casa_galdren")),
        ("north joined", lambda a: a["divides"].update(northRedSketchLinesJoin=True)),
        ("north closed", lambda a: a["divides"].update(northArtificialClosure=True)),
        ("U7 activated", lambda a: a["divides"].update(farNorthMF08="EVALUABLE")),
        ("Rodas transferred", lambda a: a["jurisdiction"].update(rodas="casa_edranor")),
        ("Rodas city", lambda a: a["jurisdiction"].update(rodasType="CITY")),
        ("Hallheim annexed", lambda a: a["jurisdiction"].update(hallheim="CASA_EDRANOR")),
        ("forest harvesting free", lambda a: a["jurisdiction"].update(bosqueAltoHarvest="FREE")),
        ("royal forest transferred", lambda a: a["jurisdiction"].update(bosqueReal="casa_edranor")),
        ("invent basin", lambda a: a["basinFamilies"].append(copy.deepcopy(a["basinFamilies"][0]))),
        ("north basin", lambda a: a["basinFamilies"][6].update(contextId="MF-08")),
        ("fabricated basin receiver", lambda a: a["basinFamilies"][0].update(receiver="Lurien")),
        ("basin geometry", lambda a: a["basinFamilies"][1].update(geometry={"type":"Polygon"})),
        ("invent scenario", lambda a: a["minorDrainageScenarios"].append(copy.deepcopy(a["minorDrainageScenarios"][0]))),
        ("scenario canon", lambda a: a["minorDrainageScenarios"][0].update(status="CANON")),
        ("scenario named river", lambda a: a["minorDrainageScenarios"][1].update(riverName="Río falso")),
        ("scenario connected without proof", lambda a: a["minorDrainageScenarios"][2].update(receiver="Lurien")),
        ("scenario made permanent", lambda a: a["minorDrainageScenarios"][3].update(regime="PERMANENT")),
        ("scenario material", lambda a: a["minorDrainageScenarios"][4].update(materialized=True)),
        ("scenario wrong basin", lambda a: a["minorDrainageScenarios"][5].update(basinId="HC-07")),
        ("spring exists", lambda a: a["springTypes"][0].update(confirmed=True)),
        ("spring lacks recharge", lambda a: a["springTypes"][0].update(requires=[])),
        ("spring flow invented", lambda a: a["springTypes"][1].update(flow=10)),
        ("wetland invented", lambda a: a["wetlandTypes"][0].update(confirmed=True)),
        ("wetland without budget", lambda a: a["wetlandTypes"][1].update(requires=[])),
        ("wetland receiver invented", lambda a: a["wetlandTypes"][2].update(receiver="Antela")),
        ("permanence default", lambda a: a["regimes"].remove("UNKNOWN")),
        ("snow assumed", lambda a: a["seasonalProcesses"].remove("SNOW_ACCUMULATION_IF_VERIFIED")),
        ("cycle allowed", lambda a: a["graphContract"].update(directedAcyclic=False)),
        ("receiver optional", lambda a: a["graphContract"].update(receiverRequiredBeforeMaterialization=False)),
        ("uphill allowed", lambda a: a["graphContract"].update(uphillFlowForbidden=False)),
        ("new graph edge", lambda a: a["graphContract"]["minorGraphEdges"].append({"from":"HS-01","to":"Lurien"})),
        ("water rights implied", lambda a: a["graphContract"].update(waterRightsImplied=True)),
        ("unknowns erased", lambda a: a["reservedUnknowns"].remove("ALL_MINOR_RECEIVERS")),
        ("removed guard", lambda a: a["prohibitions"].remove("NO_B3_B4_CLAIM")),
        ("R3 claimed", lambda a: a["futurePhases"].update(R3="COMPLETE"))
    ]
    for title, mutate in scenarios:
        changed = copy.deepcopy(data)
        mutate(changed)
        assert failures(changed, r1, r0), f"mutation accepted: {title}"
    return len(scenarios)


def test_graph() -> int:
    valid = [
        {"id": "a", "height": 3, "receiver": "b", "kind": "SEGMENT"},
        {"id": "b", "height": 2, "receiver": "terminal", "kind": "SEGMENT"},
        {"id": "terminal", "height": 1, "receiver": "terminal",
         "kind": "SINK", "balanced": True},
    ]
    assert not check_graph(valid), check_graph(valid)
    cases = [
        ("cycle", [{"id": "a", "height": 3, "receiver": "b"},
                   {"id": "b", "height": 3, "receiver": "a"}]),
        ("uphill", [{**valid[0], "height": 0}, valid[1], valid[2]]),
        ("missing receiver", [{**valid[0], "receiver": "unknown"}, valid[1], valid[2]]),
        ("unbalanced sink", [valid[0], valid[1], {**valid[2], "balanced": False}]),
        ("rights invented", [{**valid[0], "rightsImplied": True}, valid[1], valid[2]]),
        ("duplicate ID", [valid[0], valid[0], valid[2]]),
    ]
    for title, graph in cases:
        assert check_graph(graph), f"graph accepted: {title}"
    return len(cases)


def main() -> None:
    r0 = json.loads((R0 / "natural_regions_v0.1.json").read_text(encoding="utf-8"))
    r1 = json.loads((R1 / "natural_features_v0.2.json").read_text(encoding="utf-8"))
    data = json.loads((R2 / "hydrology_v0.3.json").read_text(encoding="utf-8"))
    errors = failures(data, r1, r0)
    assert not errors, errors
    check_docs()
    mutations = negative_mutations(data, r1, r0)
    graph_tests = test_graph()
    print(f"PASS E19-R2: 7 HC, 14 HS, 5 SP, 3 WH; {mutations} contract "
          f"mutations, {graph_tests} graph mutants; B2 ONLY, NO METRIC, NO RUNTIME")


if __name__ == "__main__":
    main()

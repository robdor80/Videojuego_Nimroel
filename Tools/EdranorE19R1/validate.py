#!/usr/bin/env python3
"""E19-R1: valida el atlas no métrico y ejecuta mutaciones adversariales."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
R1 = EDR / "E19-R1"
R0 = EDR / "E19-R0"
EXPECTED_NAMES = {
    "EDR-G01": "Los Rellanos de Karsath",
    "EDR-G02": "Las Gradas de Lumina",
    "EDR-G03": "La Umbría del Alto",
    "EDR-G04": "Los Resaltes de Dorth",
    "EDR-G05": "Los Claros del Norte",
    "EDR-G06": "La Nava de Rodas",
}
DOCS = (
    "README.md",
    "01_ATLAS_MORFOESTRUCTURAL.md",
    "02_VERTIENTES_CRESTAS_Y_PIEDEMONTES.md",
    "03_VALLES_CUBETAS_Y_RELIEVE_INTERIOR.md",
    "04_GACETERO_DE_TOPONIMIA.md",
    "05_PERFILES_Y_TRANSICIONES_CAUSALES.md",
    "06_PARIDAD_VALRIK_AUDITORIA_Y_TRASPASO.md",
)
REQUIRED_RESTRICTIONS = {
    "NO_FAKE_NORTH_JOIN", "NO_REJECTED_PR84",
    "NO_ROADS_OR_PASSES_FROM_LORE", "NO_MINOR_RIVERS_WITHOUT_BASIN",
    "NO_CROWN_TRANSFER", "NO_ROYAL_FOREST_HARVEST",
    "NO_KARSATH_URBAN_PORT", "NO_VARETH_IN_EDRANOR",
    "NO_VIUDA_APPROPRIATION", "NO_B3_B4_CLAIM",
}


def failures(d: dict, r0: dict) -> list[str]:
    e = []
    def require(cond: bool, key: str) -> None:
        if not cond:
            e.append(key)

    require(d.get("schemaVersion") == 2 and d.get("documentId") == "edranor_e19_r1_physical_geography_toponymy", "schema")
    require(d.get("status") == "REGIONAL_DESIGN_NOT_RUNTIME" and d.get("precedent") == "VALRIK_GEOGRAFIA_LOCAL", "scope")
    require(d.get("parentPhase") == "E19-R0" and d.get("parentHeadSha") == "addd767de9bf27ef35e8aef6d68cde00dea79c10", "provenance")
    require(d.get("rejectedPR84Used") is False, "discarded PR")
    require(d.get("implementedInGodot") is False, "Godot")
    require(all(d.get(k) == 0 for k in ("worldStateEntities", "actualRoadEdges", "actualMinorRivers", "actualSettlements")), "invented entities")
    require(all(d.get(k) is None for k in ("geometry", "projection", "measuredArea", "measuredAltitude")), "false metric")

    b = d.get("boundaries", {})
    require(b.get("west", {}).get("mountain") == "Montes Valkram"
            and b.get("west", {}).get("westernSlope") == "casa_darovan"
            and b.get("west", {}).get("easternSlope") == "casa_edranor"
            and b.get("west", {}).get("divide") == "MOUNTAIN_WATERSHED", "Valkram")
    require(b.get("east", {}).get("mountain") == "Montes Azurios"
            and b.get("east", {}).get("westernSlope") == "casa_edranor"
            and b.get("east", {}).get("easternSlope") == "casa_galdren"
            and b.get("east", {}).get("divide") == "MOUNTAIN_WATERSHED", "Azurios")
    require(b.get("south", {}).get("nonRiverPart") == "ADMINISTRATIVE"
            and b.get("south", {}).get("river") == "Río Lurien"
            and b.get("south", {}).get("neighbor") == "casa_aethros"
            and b.get("south", {}).get("riverSegment") is None
            and b.get("south", {}).get("entireRiverBoundary") is False, "south border")
    require(b.get("north", {}).get("redSketchLinesJoin") is False
            and b.get("north", {}).get("artificialClosure") is False
            and b.get("north", {}).get("geometry") is None, "north false closure")

    j = d.get("jurisdiction", {})
    require(j.get("rodas") == "crown_aethros" and j.get("rodasType") == "ALDEA"
            and j.get("hallheim") == "OUTSIDE_EDRANOR"
            and j.get("bosqueReal") == "crown_aethros"
            and j.get("bosqueAltoHarvest") == "PERMIT_REQUIRED", "jurisdiction")
    h = d.get("regionalHydrology", {})
    require(h.get("sequence") == ["Valkram eastern slope","Río Lurien","Lago Antela","Río Lurien","Hallheim","Golfo de Norgard"], "river order")
    require(h.get("antelaRelativeToKarsath") == "SOUTH"
            and h.get("karsathUrbanShoreConfirmed") is False
            and h.get("dorthMajorRiverConfirmed") is False
            and h.get("lurienNavigationFrom") == "Hallheim"
            and h.get("minorReceiverMap") is None, "river guard")

    regions = d.get("physicalRegions", [])
    require(len(regions) == 8 and [x.get("id") for x in regions] == [f"MF-{i:02d}" for i in range(1,9)], "context count/order")
    require(all(x.get("physicalGeometry") is None and x.get("administrativeRegion") is False for x in regions), "context geometry")
    require(all(x.get("evaluable") is True for x in regions[:7]) and regions[-1].get("evaluable") is False
            and regions[-1].get("originalUnit") == "far_north_unclosed", "U7 not evaluable")

    canon = d.get("canonicalFeatures", [])
    require(len(canon) == 8 and [x.get("id") for x in canon] == [f"A{i:02d}" for i in range(1,9)], "canon coverage")
    require([x.get("name") for x in canon] == ["Montes Valkram","Montes Azurios","Río Lurien","Lago Antela",
                                            "Bosque Alto","Bosque de los Azurios","Bosque Real","Paso de Vareth"], "canon names")
    require(all(x.get("geometry") is None and x.get("localFeatureConfirmed") is False and x.get("authority") in {"author_canon","repo_canon"} for x in canon), "canon scope")
    require(canon[-1].get("guard") == "NOT_ASSIGNED_TO_EDRANOR", "Vareth guard")
    require(canon[6].get("guard") == "CROWN_NO_EDRANOR_RIGHTS", "royal forest")
    selected = d.get("selectedDesignNames", [])
    require(len(selected) == 6 and {x.get("id"): x.get("name") for x in selected} == EXPECTED_NAMES, "six R0 names")
    r0_selected = {x.get("id"): x.get("name") for x in r0.get("naturalRegions", [])}
    require(r0_selected == EXPECTED_NAMES, "R0 lineage")
    require(all(x.get("status") == "SELECTED_DESIGN_NOT_MAPPED"
                and x.get("authority") == "assistant_delegated_design"
                and x.get("origin") == "E13_AND_R0"
                and x.get("geometry") is None
                and x.get("materialized") is False and x.get("worldStateId") is None
                and bool(x.get("proofRequired")) for x in selected), "selected not material")
    require(next((x for x in selected if x.get("id") == "EDR-G06"), {}).get("proofRequired") == "WITHDRAW_IF_NO_NAVA", "Nava conditional")
    proposed = d.get("proposedNames", [])
    require(len(proposed) == 12 and {x.get("id") for x in proposed} == {f"EDR-P{i:02d}" for i in range(1,13)}, "proposal count")
    require(all(x.get("status") == "PROPOSAL_NO_LOCAL_FEATURE"
                and x.get("authority") == "assistant_delegated_proposal"
                and x.get("geometry") is None and x.get("materialized") is False
                and x.get("worldStateId") is None and bool(x.get("proofRequired")) for x in proposed), "proposals cannot be canon")
    reserved = d.get("reservedNames", [])
    require(len(reserved) == 2 and {x.get("id"): x.get("name") for x in reserved} == {
        "ED13-T03": "Los Bancales Viejos", "ED13-T04": "La Loma del Lagar"}, "reserved identity")
    require(all(x.get("status") == "RESERVED_UNASSIGNED" and bool(x.get("reason")) for x in reserved), "reserved activation")
    all_items = canon + selected + proposed + reserved
    require(len({x.get("id") for x in all_items}) == len(all_items), "ID collision")
    require(len({x.get("name").casefold() for x in all_items}) == len(all_items), "toponym collision")
    require(all(x.get("name") and x.get("form") and x.get("source") for x in canon), "canon metadata")
    require(all(x.get("form") and x.get("anchor") for x in selected + proposed), "local metadata")
    for key in ("selectedDesignNames","proposedNames"):
        require(not any(x.get("id", "").startswith("A") for x in d.get(key,[])), "authority ID separation")

    transitions = d.get("naturalTransitions", [])
    region_ids = {r["id"] for r in regions}
    require(len(transitions) == 6 and len({(x.get("from"),x.get("to")) for x in transitions}) == 6, "transitions count")
    require(all(x.get("from") in region_ids and x.get("to") in region_ids and x.get("from") != x.get("to")
                and x.get("isRoad") is False for x in transitions), "roads inferred")
    require(not any(x.get("from") == "MF-08" or x.get("to") == "MF-08" for x in transitions), "unknown north mapped")
    require(set(d.get("prohibitions",[])) == REQUIRED_RESTRICTIONS, "restrictions")
    require(d.get("futurePhases", {}).get("R2") == "HYDROLOGY_UNDELIMITED"
            and d.get("futurePhases",{}).get("R4") == "ROUTES_NOT_MATERIALIZED"
            and d.get("futurePhases",{}).get("TEC") == "GODOT_COORDINATES_DEFERRED", "do not close future phases")
    require(len(d.get("sourceFiles",[])) >= 7, "sources")
    return e


def assert_docs() -> None:
    for name in DOCS:
        path = R1/name
        assert path.is_file(), name
        body = path.read_text(encoding="utf-8")
        assert len(body) > 1200, name
        assert "E19-R1" in body, name
    gazetteer = (R1/"04_GACETERO_DE_TOPONIMIA.md").read_text(encoding="utf-8")
    for name in EXPECTED_NAMES.values():
        assert name in gazetteer, name
    profile = (R1/"05_PERFILES_Y_TRANSICIONES_CAUSALES.md").read_text(encoding="utf-8")
    for word in ("Valkram","Azurios","Karsath","Lumina","Dorth","Rodas"):
        assert word in profile, word


def mutations(data: dict, r0: dict) -> int:
    cases = [
        ("north joined", lambda x: x["boundaries"]["north"].update(redSketchLinesJoin=True)),
        ("north artificial", lambda x: x["boundaries"]["north"].update(artificialClosure=True)),
        ("north geometry", lambda x: x["boundaries"]["north"].update(geometry=[1,2])),
        ("west inverted", lambda x: x["boundaries"]["west"].update(easternSlope="casa_darovan")),
        ("east inverted", lambda x: x["boundaries"]["east"].update(westernSlope="casa_galdren")),
        ("wrong west mountain", lambda x: x["boundaries"]["west"].update(mountain="Montes Azurios")),
        ("wrong east mountain", lambda x: x["boundaries"]["east"].update(mountain="Montes Valkram")),
        ("south entire river", lambda x: x["boundaries"]["south"].update(entireRiverBoundary=True)),
        ("south invented segment", lambda x: x["boundaries"]["south"].update(riverSegment="invented")),
        ("south all natural", lambda x: x["boundaries"]["south"].update(nonRiverPart="NATURAL")),
        ("Rodas transfer", lambda x: x["jurisdiction"].update(rodas="casa_edranor")),
        ("Rodas city", lambda x: x["jurisdiction"].update(rodasType="CITY")),
        ("Hallheim annexed", lambda x: x["jurisdiction"].update(hallheim="CASA_EDRANOR")),
        ("royal forest owned", lambda x: x["jurisdiction"].update(bosqueReal="casa_edranor")),
        ("forest free cutting", lambda x: x["jurisdiction"].update(bosqueAltoHarvest="FREE_HARVEST")),
        ("Antela north", lambda x: x["regionalHydrology"].update(antelaRelativeToKarsath="NORTH")),
        ("fake urban shore", lambda x: x["regionalHydrology"].update(karsathUrbanShoreConfirmed=True)),
        ("Dorth new river", lambda x: x["regionalHydrology"].update(dorthMajorRiverConfirmed=True)),
        ("wrong river order", lambda x: x["regionalHydrology"]["sequence"].reverse()),
        ("fake minor receiver", lambda x: x["regionalHydrology"].update(minorReceiverMap={"r":"antela"})),
        ("false upstream navigation", lambda x: x["regionalHydrology"].update(lurienNavigationFrom="Karsath")),
        ("false coords", lambda x: x.update(projection="EPSG:4326")),
        ("false geometry", lambda x: x.update(geometry={"type":"Polygon"})),
        ("false altitude", lambda x: x.update(measuredAltitude=450)),
        ("Godot claimed", lambda x: x.update(implementedInGodot=True)),
        ("WorldState created", lambda x: x.update(worldStateEntities=1)),
        ("invented road", lambda x: x.update(actualRoadEdges=1)),
        ("invented river", lambda x: x.update(actualMinorRivers=1)),
        ("prior rejected PR", lambda x: x.update(rejectedPR84Used=True)),
        ("minor proposal canonized", lambda x: x["proposedNames"][0].update(status="CANON")),
        ("proposal materialized", lambda x: x["proposedNames"][2].update(materialized=True)),
        ("selected materialized", lambda x: x["selectedDesignNames"][0].update(worldStateId="edr_1")),
        ("Nava assumed", lambda x: x["selectedDesignNames"][-1].update(proofRequired="NO_PROOF")),
        ("Vareth assigned", lambda x: x["canonicalFeatures"][-1].update(guard="EDRANOR_PASS")),
        ("royal forest released", lambda x: x["canonicalFeatures"][6].update(guard="EDRANOR_FREE")),
        ("duplicate name", lambda x: x["proposedNames"][0].update(name="Los Rellanos de Karsath")),
        ("duplicate ID", lambda x: x["proposedNames"][0].update(id="EDR-G01")),
        ("U7 evaluable", lambda x: x["physicalRegions"][-1].update(evaluable=True)),
        ("U7 transition", lambda x: x["naturalTransitions"].append({"from":"MF-08","to":"MF-07","relation":"NORTH","isRoad":False})),
        ("invented transit road", lambda x: x["naturalTransitions"][0].update(isRoad=True)),
        ("R2 falsely closed", lambda x: x["futurePhases"].update(R2="COMPLETE")),
        ("prohibition removed", lambda x: x["prohibitions"].remove("NO_CROWN_TRANSFER")),
        ("missing authority", lambda x: x["selectedDesignNames"][1].update(authority="author_canon")),
    ]
    for title, patch in cases:
        altered = copy.deepcopy(data)
        patch(altered)
        assert failures(altered, r0), f"mutation accepted: {title}"
    return len(cases)


def main() -> None:
    d = json.loads((R1/"natural_features_v0.2.json").read_text(encoding="utf-8"))
    r0 = json.loads((R0/"natural_regions_v0.1.json").read_text(encoding="utf-8"))
    bad = failures(d, r0)
    assert not bad, bad
    assert_docs()
    n = mutations(d, r0)
    print(f"PASS E19-R1: 8 contexts, 8 canon anchors, 6 selected names, 12 candidates, 2 reserved, {n} negative mutations; NO METRIC/NO RUNTIME")


if __name__ == "__main__":
    main()

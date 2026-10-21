#!/usr/bin/env python3
"""D02 Darovan: comprobación de grafo, fuentes y anti-regresiones, no runtime."""
from __future__ import annotations
import copy
import json
import sys
from collections import defaultdict
from pathlib import Path

EXPECTED_EDGES = {
    ("d02_belara_source", "d02_belara_lhera_split"),
    ("d02_belara_lhera_split", "d02_belara_mouth"),
    ("d02_belara_lhera_split", "d02_lhera_agujas"),
    ("d02_lhera_agujas", "d02_lhera_mouth"),
    ("d02_veldora_upstream_unknown", "d02_veldora_mouth"),
    ("d02_fhalion_upstream_unknown", "d02_fhalion_west_coast_mouth_unlocated"),
    ("d02_thalen_upstream_unknown", "d02_thalen_terminal_split"),
    ("d02_thalen_terminal_split", "d02_thalen_arm_a"),
    ("d02_thalen_terminal_split", "d02_thalen_arm_b"),
    ("d02_thalen_arm_a", "d02_thalen_mouth_a"),
    ("d02_thalen_arm_b", "d02_thalen_mouth_b"),
}

def check(condition: bool, why: str) -> None:
    if not condition:
        raise AssertionError(why)

def reachable(src: str, dst: str, graph: dict[str, list[str]]) -> bool:
    stack, seen = [src], set()
    while stack:
        node = stack.pop()
        if node == dst:
            return True
        if node in seen:
            continue
        seen.add(node)
        stack.extend(graph[node])
    return False

def validate(d: dict, repo: Path) -> None:
    check(d["schemaVersion"] == 1 and d["status"] == "planning_reference_not_runtime", "contrato no-runtime")
    check(d["authorityChain"] == ["nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"], "jerarquía")
    check(d["sourceHierarchy"] == ["AUTHORED", "DERIVED", "GENERATED", "DYNAMIC", "UNKNOWN"], "clasificación Core")
    for flag in ("containsCoordinates", "containsMeasuredSlopes", "containsBasinPolygons",
                 "containsDischargeValues", "containsTributaryInstances", "containsRuntimeAssets"):
        check(d[flag] is False, "dato no autorizado: " + flag)
    rivers = {r["id"]: r for r in d["rivers"]}
    check(len(d["rivers"]) == 5 and len(rivers) == 5
          and set(rivers) == {"belara", "lhera", "veldora", "fhalion", "thalen"}, "ríos")
    b, l, v, t = (rivers[k] for k in ("belara", "lhera", "veldora", "thalen"))
    check(b["source"] == "west_flank_northern_valkram" and b["sourceKnown"] is True, "nacimiento Belara")
    check(b["mainCourseMouth"] == "golfo_de_norgard" and b["passesByCity"] == "treihord"
          and b["crossesCity"] is False and b["navigationNearCity"] == "industrial_shallow_draft_only"
          and b["branchGivesRiseTo"] == "lhera", "Belara Treihord y boca")
    check(l["branchesFrom"] == "belara" and l["mainCourseMouth"] == "golfo_de_veldora"
          and l["adjacentTo"] == "bosque_de_las_agujas", "Lhera")
    check(v["source"] is None and v["sourceKnown"] is False
          and v["mainCourseMouth"] == "golfo_de_veldora"
          and set(v["independentOf"]) == {"belara", "lhera"}
          and v["visualRiverBehindCityIdentification"] == "veldora", "Veldora independiente")
    f = rivers["fhalion"]
    check(f["source"] is None and f["sourceKnown"] is False and f["mainCourseMouth"] is None
          and f["coastalSector"] == "costa_occidental_al_sur_de_veldora"
          and set(f["independentOf"]) == {"belara","lhera","veldora","thalen"}, "Fhalion")
    check(t["source"] is None and t["sourceKnown"] is False
          and t["mainCourseMouth"] == "golfo_de_norgard"
          and t["terminalArms"] == 2 and t["cityBetweenTerminalArms"] == "taramin", "Thalen")
    systems = {s["id"]: s for s in d["systems"]}
    check(len(systems) == 4 and len(d["systems"]) == 4 and
          set(systems) == {"belara_lhera", "veldora", "fhalion", "thalen"}, "sistemas")
    check(systems["belara_lhera"]["riverIds"] == ["belara", "lhera"] and
          set(systems["belara_lhera"]["mouths"]) == {"golfo_de_norgard", "golfo_de_veldora"} and
          systems["belara_lhera"]["hydraulicSplitFraction"] is None, "red divergente")
    check(systems["veldora"]["riverIds"] == ["veldora"] and
          systems["veldora"]["mouths"] == ["golfo_de_veldora"], "red Veldora")
    check(systems["fhalion"]["riverIds"] == ["fhalion"] and systems["fhalion"]["mouths"] == [] and systems["fhalion"]["mouthSpecificName"] is None, "Fhalion boca desconocida")
    check(systems["thalen"]["riverIds"] == ["thalen"] and
          systems["thalen"]["mouths"] == ["golfo_de_norgard"], "red Thalen")
    check(all(s["catchmentPolygon"] is None for s in systems.values()), "polígonos falsos")
    ng = d["conceptualGraph"]["nodes"]
    nodes = {n["id"]: n for n in ng}
    check(len(nodes) == len(ng) == 15, "IDs nodos")
    check(all(n["coordinate"] is None and n["geom"] is None for n in ng), "nodo cartográfico prohibido")
    edges = d["conceptualGraph"]["edges"]
    actual = {(e["from"], e["to"]) for e in edges}
    check(len(edges) == len(actual) == len({e["id"] for e in edges}) == 11
          and actual == EXPECTED_EDGES, "aristas topológicas")
    graph = defaultdict(list)
    for fr, to in actual:
        check(fr in nodes and to in nodes and nodes[fr]["systemId"] == nodes[to]["systemId"], "enlace entre sistemas")
        graph[fr].append(to)
    check(reachable("d02_belara_source", "d02_belara_mouth", graph)
          and reachable("d02_belara_source", "d02_lhera_mouth", graph), "Belara a dos golfos")
    check(not reachable("d02_belara_source", "d02_veldora_mouth", graph), "Veldora ajeno al Belara")
    check(reachable("d02_thalen_terminal_split", "d02_thalen_mouth_a", graph)
          and reachable("d02_thalen_terminal_split", "d02_thalen_mouth_b", graph), "brazos Thalen")
    # La topología obligatoria es acíclica: no confundir separación con reconexión.
    def visit(n: str, seen: set, active: set) -> None:
        check(n not in active, "ciclo fluvial")
        if n in seen:
            return
        active.add(n)
        for child in graph[n]:
            visit(child, seen, active)
        active.remove(n)
        seen.add(n)
    seen: set[str] = set()
    for n in nodes:
        visit(n, seen, set())
    rel = d["conceptualGraph"]["adjacencies"]
    check(next(x for x in rel if x["river"] == "belara")["orderRelativeToSplit"] is None,
          "orden Treihord/divergencia inventado")
    c = d["catchmentPlanning"]
    check(c["basinDivides"] is None
          and not c["minorTributaries"] and not c["springInstances"]
          and not c["wetlandInstances"] and not c["floodplainInstances"], "microhidrografía inventada")
    check(all(not x["instances"] for x in c["knownMinorCourseType"]), "cauces estacionales específicos inventados")
    city = d["cityProtection"]
    check(set(city["manualCities"]) == {"treihord", "veldora", "taramin", "syvaris"}
          and city["excludedCity"] == "karsath"
          and city["arvenIslandOwner"] == "casa_darovan"
          and city["syvarisIslandOwner"] == "casa_darovan"
          and city["permanentSettlementsInsideAgujasAllowed"] is False
          and city["redMapMarkupIsLegalBorder"] is False, "ciudades, Arven, Agujas")
    runtime = d["runtimeIntegration"]
    check(runtime["validatedInGame"] is False and runtime["generatedWatercourseEntities"] == 0
          and runtime["persistedGeometry"] is False, "runtime falso")
    refs = set(d["sourcePaths"]) | {d["referenceCoreContract"], d["referenceD01Relief"]}
    for obj in d["rivers"] + d["systems"] + rel + c["knownMinorCourseType"]:
        refs.update(obj["sourcePaths"])
    check(len(refs) >= 9, "trazabilidad insuficiente")
    for path in refs:
        check(path.startswith("Worldbuilding/") and (repo / path).is_file(), "fuente ausente: " + path)
    check((repo / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"
           "Hidrografia/01_red_hidrografica_y_grafo_v0.1.md").is_file(), "documentación grafo ausente")

def run() -> None:
    here = Path(__file__).resolve()
    repo = next((p for p in here.parents if (p / "Worldbuilding").is_dir()), None)
    check(repo is not None, "no se encuentra raíz Git")
    base = here.parents[1]
    d = json.loads((base / "Datos operativos/darovan_d02_hydro_network_v0.1.json").read_text(encoding="utf-8"))
    validate(d, repo)
    invalid_cases = [
        ("belara_desembocadura", lambda x: x["rivers"][0].update(mainCourseMouth="golfo_de_veldora")),
        ("lhera_sin_bifurcacion", lambda x: x["rivers"][1].update(branchesFrom=None)),
        ("veldora_conectada", lambda x: x["rivers"][2].update(independentOf=[])),
        ("thalen_un_brazo", lambda x: x["rivers"][4].update(terminalArms=1)),
        ("belara_cruza_treihord", lambda x: x["rivers"][0].update(crossesCity=True)),
        ("arven_owner_erased", lambda x: x["cityProtection"].update(arvenIslandOwner=None)),
        ("fhalion_mouth_invented", lambda x: x["rivers"][3].update(mainCourseMouth="golfo_de_norgard")),
        ("fhalion_join", lambda x: x["conceptualGraph"]["edges"][10].update(to="d02_thalen_mouth_a")),
        ("arroyo_inventado", lambda x: x["catchmentPlanning"]["minorTributaries"].append({"id":"inventado"})),
        ("arista_conectando_redes", lambda x: x["conceptualGraph"]["edges"][0].update(to="d02_veldora_mouth")),
    ]
    for name, mutation in invalid_cases:
        altered = copy.deepcopy(d)
        mutation(altered)
        try:
            validate(altered, repo)
        except AssertionError:
            continue
        raise AssertionError("regresión no detectada: " + name)
    print(f"D02 STATIC OK: {len(d['rivers'])} ríos, {len(d['systems'])} redes, "
          f"{len(d['conceptualGraph']['nodes'])} nodos, "
          f"{len(d['conceptualGraph']['edges'])} aristas, {len(invalid_cases)} pruebas negativas; NO runtime")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print("D02 STATIC FAIL: " + str(exc), file=sys.stderr)
        sys.exit(1)

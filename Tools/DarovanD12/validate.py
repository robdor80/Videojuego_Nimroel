#!/usr/bin/env python3
"""D12: auditoría cruzada estática del territorio Darovan (no simulación del juego).

Ninguna de estas pruebas crea personajes, rutas, eventos, emplazamientos o WorldState.
No sustituye validadores D01–D11 ni la compilación CoreRPG incluida en la CI.
"""
import copy
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = TERR / "Datos operativos"
PACK = ROOT / "ContentPacks/darovan-territory"
CITIES = ["treihord", "veldora", "taramin", "syvaris"]
RIVERS = ["belara", "lhera", "veldora", "fhalion", "thalen"]
SYSTEMS = ["belara_lhera", "veldora", "fhalion", "thalen"]
PHYSICAL = ["d05_road_veldora_treihord", "d05_belara_shallow_haul", "d05_vena_restricted"]
SUPPLY = ["d05_ore_cart_stage", "d05_ore_port_handling",
          "d05_coal_azurios_supply", "d05_pilares_wood_supply"]
FILES = {f"D{i:02d}": DATA / f"darovan_d{i:02d}_{suffix}_v0.1.json"
         for i, suffix in enumerate([
             "canonical_anchors", "relief_profile", "hydro_network",
             "climate_ecosystems", "resources_production",
             "mobility_communications", "settlement_rules",
             "canonical_cities", "population_services",
             "governance_security", "culture_society"
         ])}

class D12Error(AssertionError):
    pass

def require(expr, message):
    if not expr:
        raise D12Error(message)

def object_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise D12Error("Clave JSON duplicada: " + key)
        obj[key] = value
    return obj

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=object_pairs)

def ids(seq):
    return [item["id"] for item in seq]

def range_is(obj, lo, hi):
    return (isinstance(obj, dict) and type(obj.get("minInclusive")) is int
            and type(obj.get("maxInclusive")) is int
            and obj["minInclusive"] == lo and obj["maxInclusive"] == hi)

def pointer(document, json_pointer):
    if json_pointer == "":
        return document
    require(json_pointer.startswith("/"), "Puntero JSON no absoluto")
    out = document
    for item in json_pointer[1:].split("/"):
        token = item.replace("~1", "/").replace("~0", "~")
        try:
            out = out[int(token)] if isinstance(out, list) else out[token]
        except (IndexError, ValueError, KeyError, TypeError) as exc:
            raise D12Error("Puntero JSON roto: " + json_pointer) from exc
    return out

def check(d, projection, manifest, resources, fixtures):
    # D00–D10: invariantes que se comparan ENTRE fases, no simplemente por archivo.
    a, geo, hydro, climate, econ, move, gen, cities, pop, admin, culture = (
        d[f"D{i:02d}"] for i in range(11))
    require(ids(a["cities"]) == CITIES and a["excludedCity"] == "karsath", "D00 canon urbano")
    require(ids(geo["cityAnchors"]) == CITIES, "D01 canon urbano")
    require(geo["administration"]["arvenIslandOwner"] == "casa_darovan", "D01 Arven actual")
    # D00 conserva un registro historico de Arven anterior a la decision autoral;
    # no se reescribe el blob porque lo protege el lock D11.
    require(a["arvenAdministrativeOwner"] is None, "D00 archivo historico alterado")
    for current in (geo, hydro, gen, cities, pop):
        key = "manualCityIds" if "manualCityIds" in current else "darovanCities"
        if key == "manualCityIds":
            require(current[key] == CITIES, "Desviacion de ciudades manuales")
    require(geo["administration"]["excludedCity"] == "karsath"
            and hydro["cityProtection"]["excludedCity"] == "karsath", "Karsath")
    require(geo["lockedHydroAnchors"]["belara"]["crossesCity"] is False
            and hydro["rivers"][0]["crossesCity"] is False
            and climate["hydroProtection"]["belaraCrossesCity"] is False
            and cities["hydro"]["belaraCrossesTreihord"] is False
            and culture["guardrails"]["treihordBelaraCrossesCity"] is False,
            "El Belara no debe atravesar Treihord")
    require(len(a["treihord"]["districts"]) == 8
            and len(set(a["treihord"]["districts"])) == 8
            and culture["guardrails"]["treihordCanonicalDistrictCount"] == 8,
            "Treihord debe conservar ocho barrios")
    require(ids(hydro["rivers"]) == RIVERS and ids(hydro["systems"]) == SYSTEMS,
            "D02: cinco rios y cuatro sistemas")
    require(climate["hydroProtection"]["namedRivers"] == RIVERS
            and gen["hydro"]["namedRivers"] == RIVERS
            and cities["hydro"]["namedRivers"] == RIVERS, "Rios transversales")
    require(gen["hydro"]["systems"] == SYSTEMS and cities["hydro"]["systems"] == SYSTEMS,
            "Sistemas hidrograficos transversales")
    graph = hydro["conceptualGraph"]
    require(len(graph["nodes"]) == 15 and len(graph["edges"]) == 11,
            "Grafo D02 topologico esperado")
    graph_nodes = ids(graph["nodes"])
    require(len(graph_nodes) == len(set(graph_nodes)), "D02: nodos duplicados")
    require(len(set(ids(graph["edges"]))) == len(graph["edges"]), "D02 aristas duplicadas")
    require(all(e["from"] in graph_nodes and e["to"] in graph_nodes
                and e["kind"] == "topological_relation_not_cartographic_line"
                for e in graph["edges"]), "D02: extremo inexistente o geometria inventada")
    unit_ids = ids(geo["physicalUnits"])
    require(len(unit_ids) == 12 and len(set(unit_ids)) == 12, "D01 unidades cualitativas")
    for other, key in ((climate, "zones"), (econ, "studyUnits"), (gen, "zones")):
        require(ids(other[key]) == unit_ids, "Unidades D01-D03-D04-D06 desalineadas")
    require(gen["manualCityIds"] == CITIES and gen["excludedCityIds"] == ["karsath"],
            "D06 excluye ciudades canonicas y Karsath")
    require(len(gen["models"]) == 9 and len(set(ids(gen["models"]))) == 9,
            "D06: modelos")
    require(gen["runtimeIntegration"]["generatedCanonicalSettlements"] == 0
            and all(c["proceduralGenerationAllowed"] is False and c["manualOnly"] is True
                    and c["worldStateEntityId"] is None for c in cities["cities"]),
            "D06/D07: ciudades instanciadas indebidamente")
    require(ids(cities["cities"]) == CITIES and ids(pop["cities"]) == CITIES
            and ids(admin["localities"]) == CITIES, "D07-D09 identidad urbana")
    require([x["id"] for x in culture["localProfiles"][:4]] == CITIES,
            "D10 identidades locales")
    require([(x["cityId"], x["choice"], x["status"]) for x in
             cities["authorialDecisions"]] == [
                 ("veldora", "B", "APPROVED_CONCEPT_ONLY"),
                 ("taramin", "A", "APPROVED_CONCEPT_ONLY"),
                 ("syvaris", "A", "APPROVED_CONCEPT_ONLY")
             ], "D07: las tres aprobaciones son SOLO conceptuales")
    require(all(x["createsPhysicalRoutes"] is False and x["changesPopulation"] is False
                for x in cities["authorialDecisions"]), "D07: promocion de propuesta")

    # D04→D05→D08 y D09: suministro NO es trayecto geofisico.
    chains = set(ids(econ["resourceChains"]))
    require(len(chains) == len(econ["resourceChains"]), "D04 cadenas duplicadas")
    assert_ids = set(ids(move["nodes"]))
    require(len(assert_ids) == len(move["nodes"]), "D05 nodos duplicados")
    actual = move["confirmedTransportLinks"]
    supplies = move["supplyRelationsNotRoutes"]
    require(ids(actual) == PHYSICAL and ids(supplies) == SUPPLY, "D05 enlaces")
    require(set(ids(actual)).isdisjoint(ids(supplies)), "D05 ruta y suministro solapados")
    for relation in actual + supplies:
        require(relation["from"] in assert_ids and relation["to"] in assert_ids,
                "D05: extremo de enlace sin nodo")
        require(relation["routeGeometry"] is None and relation["distanceKm"] is None
                and relation["travelTime"] is None and relation["capacity"] is None,
                "D05: distancias/recorridos/capacidades inventados")
    require(all(x["physicalRouteConfirmed"] is True for x in actual)
            and all(x["physicalRouteConfirmed"] is False for x in supplies),
            "D05: suministro promovido a ruta")
    require(cities["confirmedPhysicalLinkIds"] == PHYSICAL
            and admin["security"]["confirmedPhysicalLinksOnly"] == PHYSICAL
            and admin["security"]["supplyRelationsDoNotProveRoads"] is True,
            "D07/D09 no pueden inventar nuevas conexiones")
    require(all(x.get("d04Chain") is None or x["d04Chain"] in chains
                for x in pop["occupationFamilies"]), "D08 ocupacion sin recurso D04")
    require(all(all(c in chains for c in x["d04Chains"]) for x in pop["cities"]),
            "D08 ciudad referencia cadenas D04 inexistentes")
    require(econ["containsNewMiningSites"] is False
            and econ["containsNewRoutes"] is False
            and econ["containsNewQuantities"] is False, "D04 promueve recursos a instancias")

    # D08: aprobado significa intervalo/porcentaje, NUNCA personas concretas.
    require(pop["manualCityIds"] == CITIES and pop["excludedCityIds"] == ["karsath"],
            "D08 lista de ciudades")
    require(pop["cities"][0]["populationApprox"] == 32000, "Treihord ~32.000")
    require([(x["populationRange"]["minInclusive"], x["populationRange"]["maxInclusive"])
             for x in pop["cities"][1:]] == [(29000, 35000), (14000, 20000),
                                           (7000, 10000)], "D08 rangos urbanos")
    require(all(x["populationApprox"] is None for x in pop["cities"][1:]),
            "D08 rangos no son habitantes instanciados")
    territory = pop["territoryPopulation"]
    require(range_is(territory["populationRange"], 300000, 450000)
            and territory["populationApprox"] is None
            and territory["runtimeInstantiated"] is False, "D08 total Darovan")
    household = pop["householdModel"]
    require(range_is(household["urbanMeanPersonsPerHouseholdRange"], 3, 5)
            and range_is(household["ruralMeanPersonsPerHouseholdRange"], 4, 6),
            "D08 rangos de media por hogar")
    require(household["urbanMeanPersonsPerHouseholdRange"]["notAnIndividualHouseholdLimit"] is True
            and household["ruralMeanPersonsPerHouseholdRange"]["notAnIndividualHouseholdLimit"] is True,
            "D08 medias no son limites individuales")
    ages = household["ageShares"]["bands"]
    require([x["percent"] for x in ages] == [30, 60, 10]
            and sum(x["percent"] for x in ages) == 100,
            "D08 edades")
    shares = household["ruralUrbanShares"]
    require(range_is(shares["urbanSharePercentRange"], 35, 45)
            and range_is(shares["ruralSharePercentRange"], 55, 65)
            and shares["cityListIsCompleteUrbanCoverage"] is False, "D08 reparto")
    require(household["urbanRuralAgeBreakdown"]["urbanAgeShares"] is None
            and household["urbanRuralAgeBreakdown"]["ruralAgeShares"] is None,
            "D08 no aprobo edades urbanas/rurales separadas")

    # D09: autoridad regia; D10: perfiles culturales, nunca personalidad impuesta.
    require(admin["government"]["crownSupreme"] is True
            and admin["government"]["houseIndependentLegislation"] is False
            and admin["security"]["royalNavyOnly"] is True
            and admin["security"]["darovanIndependentNavy"] is False,
            "D09 competencias soberanas")
    require(len(admin["authorDecisions"]) == 17
            and len(set(ids(admin["authorDecisions"]))) == 17,
            "D09 decisiones del autor")
    require([(x["id"], x["option"]) for x in culture["authorDecisions"]] ==
            [(f"DAR-D10-{i:02d}", "C" if i == 9 else "B")
             for i in range(1, 18)], "D10 decisiones del autor")
    require(culture["unknowns"]["arvenCulturalIdentity"] is None
            and next(x for x in culture["localProfiles"] if x["id"] == "arven")
                ["culturalState"] == "UNKNOWN", "Cultura de Arven UNKNOWN")
    for flag in ("automaticNpcPersonalityFromOccupation",
                 "automaticNpcPersonalityFromResidence",
                 "automaticNpcCrimeFromWealth", "automaticNpcHostilityFromIsland",
                 "inventedInstitution", "inventedCalendarHoliday",
                 "newReligiousRite", "newRoutes", "newSettlements", "houseNavy"):
        require(culture["guardrails"][flag] is False, "D10 barrera: " + flag)
    require(all(x["individualVariation"] is True and x["createsNpc"] is False
                for x in culture["localProfiles"]), "D10 libertad individual NPC")

    # D11: proyeccion, esquema de identificadores, fuentes y trazabilidad reales.
    require(projection["sourceLocks"] and len(projection["sourceLocks"]) == 11,
            "D11 once fuentes")
    require([l["phase"] for l in projection["sourceLocks"]] ==
            [f"D{i:02d}" for i in range(11)], "D11 orden fuentes")
    for lock in projection["sourceLocks"]:
        require(lock["path"] == FILES[lock["phase"]].relative_to(ROOT).as_posix(),
                "D11 ruta fuente")
    require(projection["canonicalCityIds"] == CITIES
            and projection["excludedCityIds"] == ["karsath"]
            and projection["namedRiverIds"] == RIVERS
            and projection["hydroSystemIds"] == SYSTEMS
            and projection["belaraCrossesTreihord"] is False, "D11 canon")
    require(projection["physicalTransportLinkIds"] == PHYSICAL
            and projection["supplyRelationsNotRoutes"] == SUPPLY, "D11 grafo modal")
    require(projection["arvenCulturalIdentity"] is None
            and projection["islandAdministrativeOwner"]["arven"] == "casa_darovan",
            "D11 Arven")
    require(projection["status"] == "planning_reference_not_runtime"
            and projection["worldStateEntitiesCreated"] == 0
            and all(value is False for value in projection["executionCapabilities"].values()),
            "D11 no acredita subsistemas simulados")
    require(pointer(pop, projection["sourceDemographyPointer"]) == territory,
            "D11 puntero D08")
    require(pointer(culture, projection["sourceCultureDecisionPointer"]) ==
            culture["authorDecisions"], "D11 puntero D10")
    for definition in projection["definitions"]:
        require(definition["sourcePhase"] in d, "D11 origen de definicion")
        pointer(d[definition["sourcePhase"]], definition["sourcePointer"])
    require(len(projection["definitions"]) == 5
            and len(set(x["id"] for x in projection["definitions"])) == 5,
            "D11 cinco definiciones estables")
    ids_pack = {x["id"] for x in projection["definitions"]}
    require({x["id"] for x in resources.values()} == ids_pack,
            "D11 pack/sidecar no alineados")
    require(len(manifest["resources"]) == 5 and len(resources) == 5
            and manifest["dependencies"] == [], "D11 manifiesto")
    require(fixtures["status"] == "TEST_ONLY"
            and len(fixtures["scenarios"]) == 8
            and [x["id"] for x in fixtures["scenarios"]] ==
                [f"T{i:02d}" for i in range(1, 9)]
            and all(x["classification"] == "TEST_ONLY"
                    and x["kind"] == "SPECIFICATION_NOT_EXECUTED"
                    and x["executedInCoreRPG"] is False
                    for x in fixtures["scenarios"]), "D11 no ejecuta T01-T08")

def load_all():
    d = {name: read(path) for name, path in FILES.items()}
    projection = read(PACK / "authoring/projection-v0.1.json")
    manifest = read(PACK / "pack/manifest.json")
    resources = {p: read(PACK / "pack" / p) for p in manifest["resources"]}
    fixtures = read(PACK / "fixtures/d11-scenarios-v0.1.json")
    return d, projection, manifest, resources, fixtures

def scan_paths():
    """Inventario total: lectura UTF-8 de markdown/JSON, claves JSON, rutas de fuente.

    Se detectan referencias de autoría a rutas completas de proyecto.
    No se invalidan URLs externas ni notas historicas con referencias textuales
    a estados antiguos de PR.
    """
    all_files = sorted(p for p in TERR.rglob("*") if p.is_file())
    require(len(all_files) >= 100, "Inventario Darovan incompleto")
    markdown = 0
    json_count = 0
    refs = 0
    missing = []
    for p in all_files:
        if p.suffix.lower() == ".json":
            doc = read(p)
            json_count += 1
            def walk(v, key):
                nonlocal refs
                if isinstance(v, dict):
                    for k, val in v.items():
                        walk(val, k)
                elif isinstance(v, list):
                    for val in v:
                        walk(val, key)
                elif isinstance(v, str) and v.startswith("Worldbuilding/") and (
                        v.endswith(".md") or v.endswith(".json")):
                    refs += 1
                    if not (ROOT / v).is_file():
                        missing.append((p.relative_to(ROOT).as_posix(), key, v))
            walk(doc, "")
        elif p.suffix.lower() == ".md":
            p.read_text(encoding="utf-8-sig")
            markdown += 1
    require(not missing, "Referencias de fuentes inexistentes: " +
            repr(missing[:12]))
    require((TERR / "00_Control_del_proyecto/TRASPASO_D12_PREPARATORIO.md").is_file(),
            "Falta el traspaso D12 previo")
    return len(all_files), markdown, json_count, refs

def negatives(original):
    """Mutaciones negativas sobre copias; no se toca ni reescribe ninguna fuente."""
    d, p, m, res, f = original
    trials = [
        ("D00", lambda x: x["cities"].append({"id": "karsath"})),
        ("D01", lambda x: x["administration"].update(arvenIslandOwner="UNKNOWN")),
        ("D02", lambda x: x["rivers"].append({"id": "inventado"})),
        ("D02", lambda x: x["conceptualGraph"]["edges"][0].update(to="inexistente")),
        ("D03", lambda x: x["hydroProtection"].update(belaraCrossesCity=True)),
        ("D04", lambda x: x.update(containsNewMiningSites=True)),
        ("D05", lambda x: x["supplyRelationsNotRoutes"][2].update(physicalRouteConfirmed=True)),
        ("D05", lambda x: x["confirmedTransportLinks"][0].update(distanceKm=15)),
        ("D06", lambda x: x["manualCityIds"].append("karsath")),
        ("D07", lambda x: x["authorialDecisions"][0].update(changesPopulation=True)),
        ("D08", lambda x: x["cities"][1]["populationRange"].update(minInclusive=12000)),
        ("D08", lambda x: x["householdModel"]["ageShares"]["bands"][0].update(percent=40)),
        ("D08", lambda x: x["territoryPopulation"].update(populationApprox=350000)),
        ("D09", lambda x: x["security"].update(darovanIndependentNavy=True)),
        ("D10", lambda x: x["unknowns"].update(arvenCulturalIdentity="maritima")),
        ("D10", lambda x: x["guardrails"].update(automaticNpcPersonalityFromOccupation=True)),
    ]
    for phase, mutation in trials:
        cloned = copy.deepcopy(d)
        mutation(cloned[phase])
        try:
            check(cloned, p, m, res, f)
        except D12Error:
            continue
        raise D12Error("Mutacion invalida no rechazada en " + phase)
    # Caso transversal fuera de las fases: falsificar ejecucion del sidecar.
    bad = copy.deepcopy(p)
    bad["executionCapabilities"]["routing"] = True
    try:
        check(d, bad, m, res, f)
    except D12Error:
        pass
    else:
        raise D12Error("La proyeccion acepta runtime inventado")
    return len(trials) + 1

def main():
    inventory = scan_paths()
    data = load_all()
    check(*data)
    mutations = negatives(data)
    print(f"D12 STATIC PASS: {inventory[0]} archivos Darovan; "
          f"{inventory[1]} Markdown, {inventory[2]} JSON; "
          f"{inventory[3]} referencias a fuentes existentes; "
          f"11 fases + pack D11; {mutations} negativas rechazadas.")
    print("NO es simulacion economica, clima dinamico, IA NPC, "
          "Godot ni ejecucion de reglas territoriales CoreRPG.")

if __name__ == "__main__":
    try:
        main()
    except (D12Error, KeyError, ValueError, OSError, TypeError) as exc:
        print("D12 FAIL:", str(exc), file=sys.stderr)
        sys.exit(1)

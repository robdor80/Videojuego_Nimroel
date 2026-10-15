#!/usr/bin/env python3
"""D03 Darovan: perfil climático/ecológico cualitativo, NO RUNTIME."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ZONE_IDS = {
    "d01_valkram_oeste", "d01_elyra_paso_peninsular", "d01_norte_transicion",
    "d01_aguja_litoral", "d01_belara_treihord", "d01_veldora_litoral",
    "d01_linde_caminos", "d01_pilares_sur", "d01_taramin_norte_centro",
    "d01_taramin_bosque_sur", "d01_syvaris", "d01_arven_contexto",
}
NULL_FIELDS = (
    "temperatureC", "precipitationMm", "elevationM", "seasonDates",
    "dominantWind", "soilClass", "groundwaterAvailability",
    "watercoursePermanence",
)

def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def validate(d: dict, repo: Path) -> None:
    check(d["schemaVersion"] == 1 and d["documentId"] == "darovan_d03_climate_ecosystems"
          and d["status"] == "planning_reference_not_runtime", "no runtime/version")
    check(d["authorityChain"] == [
        "nimroel_core", "norgard_defaults", "casa_darovan", "locality", "world_state"
    ], "authority chain")
    check(d["sourceHierarchy"] == [
        "AUTHORED", "DERIVED", "GENERATED", "DYNAMIC", "UNKNOWN"
    ], "source hierarchy")
    check(all(v is False for k, v in d.items() if k.startswith("contains")),
          "unapproved data flag")
    zones = d["zones"]
    check(len(zones) == len(ZONE_IDS) == len({z["id"] for z in zones})
          and {z["id"] for z in zones} == ZONE_IDS, "D01 study units")
    for z in zones:
        check(z["classification"] == "qualitative_study_unit_not_polygon",
              "fictional zone polygon")
        check(all(z[f] is None for f in NULL_FIELDS), "invented climate/soil values")
        check(bool(z["sourceRefIds"]), "unattributed study unit")
        check(all(k in d["sourceRefs"] for k in z["sourceRefIds"]),
              "unresolved source key")
    refs = d["sourceRefs"]
    check(len(refs) >= 13, "insufficient primary references")
    check(all(p.startswith("Worldbuilding/") and (repo / p).is_file()
              for p in refs.values()), "missing source file")
    check(d["referenceD01Relief"] == refs["d01"] and
          d["referenceD02Hydro"] == refs["d02"] and
          d["referenceCoreContract"] == refs["core"], "broken source links")

    relief = json.loads((repo / refs["d01"]).read_text(encoding="utf-8"))
    hydro = json.loads((repo / refs["d02"]).read_text(encoding="utf-8"))
    core = json.loads((repo / refs["core"]).read_text(encoding="utf-8"))
    # Compatibility is about identifiers and invariant values; not runtime code.
    check(core["status"] == "active_core_contract", "Core inactive")
    check(len(relief["physicalUnits"]) == 12 and
          {u["id"] for u in relief["physicalUnits"]} == ZONE_IDS, "D01 incompatibility")
    check([r["id"] for r in hydro["rivers"]] == ["belara", "lhera", "veldora", "thalen"],
          "D02 river set")

    a = d["regionalAnchors"]
    check(a["westernCoast"] == "mild_oceanic"
          and a["northernTransition"] == "polar_to_cold_to_continental_gradual"
          and a["taraminNorthCentral"] == "semiarid_not_desert"
          and a["taraminSouth"] == "increasing_moisture_and_humid_subtropical_forest_at_far_south"
          and a["syvaris"] == "warm_partly_dry_with_green_sheltered_areas_not_desert_or_uniform_jungle",
          "canonical regional gradients")
    check(a["arvenOwner"] is None and a["syvarisOwner"] == "casa_darovan"
          and a["excludedCity"] == "karsath"
          and a["manualCities"] == ["treihord", "veldora", "taramin", "syvaris"],
          "administration/cities")
    check(a["permanentSettlementsInsideAgujasAllowed"] is False
          and a["pilaresOneForest"] is True and a["taraminOneForest"] is True
          and a["syvarisForestsDiscontinuous"] is True, "forests/Agujas")
    by_id = {z["id"]: z for z in zones}
    check(by_id["d01_arven_contexto"]["administrativeOwner"] is None
          and by_id["d01_syvaris"]["administrativeOwner"] == "casa_darovan",
          "island owners")

    h = d["hydroProtection"]
    check(h["namedRivers"] == ["belara", "lhera", "veldora", "thalen"]
          and h["belaraMouth"] == "golfo_de_norgard"
          and h["belaraAdjacentCity"] == "treihord"
          and h["belaraCrossesCity"] is False, "Belara")
    check(h["lheraFrom"] == "belara"
          and h["lheraMouth"] == "golfo_de_veldora"
          and h["veldoraIndependentFrom"] == ["belara", "lhera"]
          and h["veldoraMouth"] == "golfo_de_veldora", "Lhera/Veldora")
    check(h["thalenTerminalArms"] == 2
          and h["thalenCityBetween"] == "taramin"
          and h["thalenMouth"] == "golfo_de_norgard", "Thalen")
    check(h["namedRiverPermanence"] == "UNKNOWN"
          and all(not h[k] for k in ("newTributaries", "newSprings", "newWetlands", "newBasins"))
          and h["channelGeometry"] is None, "inferred fake water")
    check(hydro["rivers"][0]["crossesCity"] is False
          and hydro["rivers"][1]["branchesFrom"] == "belara"
          and set(hydro["rivers"][2]["independentOf"]) == {"belara", "lhera"}
          and hydro["rivers"][3]["terminalArms"] == 2, "D02 regression")
    run = d["runtimeIntegration"]
    check(run["status"] == "not_implemented" and run["validatedInGame"] is False
          and run["generatedClimateCells"] == 0
          and run["generatedSpecies"] == 0
          and run["persistedClimateState"] is False, "false runtime claim")
    check(d["approvals"]["newCanonApproved"] is False
          and set(d["approvals"]["pendingAuthor"]) ==
          {"DAR-P01", "DAR-P04", "DAR-P07", "DAR-P08"}, "canon approvals")

def run() -> None:
    here = Path(__file__).resolve()
    repo = next((p for p in here.parents if (p / "Worldbuilding").is_dir()), None)
    check(repo is not None, "repository root missing")
    base = here.parents[1]
    file_path = base / "Datos operativos/darovan_d03_climate_ecosystems_v0.1.json"
    data = json.loads(file_path.read_text(encoding="utf-8"))
    validate(data, repo)
    negative = [
        ("arven_claim", lambda d: d["regionalAnchors"].update(arvenOwner="casa_darovan")),
        ("belara_cross", lambda d: d["hydroProtection"].update(belaraCrossesCity=True)),
        ("lhera_source", lambda d: d["hydroProtection"].update(lheraFrom="veldora")),
        ("veldora_join", lambda d: d["hydroProtection"].update(veldoraIndependentFrom=[])),
        ("thalen_arm", lambda d: d["hydroProtection"].update(thalenTerminalArms=1)),
        ("numeric_climate", lambda d: d["zones"][0].update(temperatureC=10)),
        ("new_species", lambda d: d.update(containsNewSpecies=True)),
        ("missing_reference", lambda d: d["zones"][0].update(sourceRefIds=["fake_source"])),
        ("agujas_village", lambda d: d["regionalAnchors"].update(permanentSettlementsInsideAgujasAllowed=True)),
        ("perennial_assertion", lambda d: d["hydroProtection"].update(namedRiverPermanence="perennial")),
    ]
    for name, mutate in negative:
        broken = copy.deepcopy(data)
        mutate(broken)
        try:
            validate(broken, repo)
        except (AssertionError, KeyError, TypeError):
            continue
        raise AssertionError("undetected mutation: " + name)
    print(f"D03 STATIC OK: {len(data['zones'])} qualitative units, "
          f"{len(data['sourceRefs'])} references, {len(negative)} negative tests; NOT RUNTIME")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as e:
        print("D03 STATIC FAIL: " + str(e), file=sys.stderr)
        sys.exit(1)

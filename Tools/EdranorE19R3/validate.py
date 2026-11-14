#!/usr/bin/env python3
"""E19-R3: contrato ambiental B2 y negativos; no crea mundo ni superficie medida."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DIR = EDR / "E19-R3"
DOCS = ["README.md", "01_PERFILES_SUELO_DRENAJE.md",
        "02_MICROCLIMAS_Y_GRADIENTES.md", "03_VEGETACION_Y_MOSAICOS.md",
        "04_APROVECHAMIENTO_Y_DERECHOS.md", "05_ESTACIONALIDAD_Y_MEMORIA.md",
        "06_ATLAS_POR_CONTEXTOS.md", "07_CONTRATO_GENERACION_2D.md",
        "08_PARIDAD_VALRIK_Y_PRUEBAS.md", "09_ACTA_R3_Y_TRASPASO.md"]
PARENT = "50a284cf33d59465332623c8a46c5e1d41cdb664"
SEQUENCE = ["Valkram eastern slope", "Río Lurien", "Lago Antela",
            "Río Lurien", "Hallheim", "Golfo de Norgard"]
COUNTS = (12, 11, 10, 10, 8)
GUARDS = {"NO_FAKE_NORTH_CLOSURE", "NO_REJECTED_PR84", "NO_B3_B4_UPGRADE",
          "NO_BELARA_TO_EDRANOR", "NO_CALERAN_DORTH", "NO_DORTH_MAJOR_RIVER",
          "NO_KARSATH_LAKE_PORT", "NO_WATER_USE_BY_PRESENCE",
          "NO_FOREST_RIGHTS_BY_COVER", "NO_RODAS_TAXATION",
          "NO_BOSQUE_REAL_EDRANOR", "NO_BOREAL_VINES",
          "NO_POLAR_MF08_ASSIGNMENT", "NO_UNVERIFIED_SOIL_VALUES",
          "NO_IMPOSSIBLE_VEGETATION", "NO_INSTANT_ECOLOGICAL_RESET",
          "NO_HARVEST_WITHOUT_STOCK", "NO_NEW_ROAD_OR_PARCEL"}
CTX = [f"MF-{i:02d}" for i in range(1, 9)]
HC = [f"HC-{i:02d}" for i in range(1, 8)]
PERMITTED_EVIDENCE = {
    "JURISDICTION", "GEOMETRY", "MATERIAL", "TEXTURE", "DEPTH", "DRAINAGE",
    "WATER_AND_SLOPE", "PLACED_RELIEF", "EXPOSURE", "REGIONAL_WEATHER",
    "RECENT_WEATHER_MEMORY", "SOIL_AND_WATER", "CLIMATE_AND_EXPOSURE",
    "FOREST_RIGHTS", "HABITAT_TRANSITION", "MATERIALIZED_STOCK",
    "RIGHTS_PERMISSION", "QUOTA_AND_REGENERATION",
    "ACCESS_AND_DOWNSTREAM_EFFECT",
}


def failures(a: dict, hyd: dict, geo: dict) -> list[str]:
    bad: list[str] = []
    def ck(condition: bool, label: str) -> None:
        if not condition:
            bad.append(label)
    try:
        ck(a.get("schemaVersion") == 4 and
           a.get("documentId") == "edranor_e19_r3_land_ecology" and
           a.get("phase") == "E19-R3", "schema")
        ck(a.get("status") == "REGIONAL_CAUSAL_DESIGN_B2_NOT_RUNTIME" and
           a.get("authority") == "ASSISTANT_DELEGATED_DESIGN" and
           a.get("precedent") == "VALRIK_GEOGRAFIA_LOCAL_CLIMA_LOCAL", "authority")
        ck(a.get("parent") == {
            "phase": "E19-R2", "headSha": PARENT,
            "documentId": "edranor_e19_r2_hydrology", "schemaVersion": 3,
            "rejectedPR84Used": False}, "lineage")
        ck(hyd.get("schemaVersion") == 3 and
           hyd.get("documentId") == a["parent"]["documentId"] and
           geo.get("schemaVersion") == 2 and
           len(hyd.get("basinFamilies", [])) == 7, "parent contracts")
        g = a["governance"]
        ck(g.get("west") == "VALKRAM_WEST_DAROVAN_EAST_EDRANOR" and
           g.get("east") == "AZURIOS_WEST_EDRANOR_EAST_GALDREN" and
           g.get("south") == "AETHROS_ADMIN_EXCEPT_UNLOCATED_LURIEN_SECTION" and
           g.get("northArtificialClosure") is False and
           g.get("northSketchJoined") is False, "natural borders")
        ck(g.get("rodas") == {"kind": "ALDEA", "jurisdiction": "crown_aethros"} and
           g.get("hallheim") == "OUTSIDE_EDRANOR" and
           g.get("bosqueAltoHarvest") == "PERMIT_REQUIRED" and
           g.get("bosqueReal") == "crown_aethros" and
           g.get("bosqueRealHarvestByEdranor") is False, "jurisdiction/forests")
        ck(g.get("caleranThroughDorthConfirmed") is False and
           g.get("karsathUrbanAntelaShoreConfirmed") is False and
           g.get("sourceHydrologySequence") == SEQUENCE and
           hyd["majorSystem"]["sequence"] == SEQUENCE, "river chain")
        ck(geo["boundaries"]["west"]["easternSlope"] == "casa_edranor" and
           geo["boundaries"]["east"]["westernSlope"] == "casa_edranor" and
           geo["jurisdiction"]["rodas"] == "crown_aethros", "R1 guards")
        m = a["maturity"]
        ck(m.get("b2Documentary") is True and
           m.get("b3Mapped") is False and m.get("b4Runtime") is False and
           m.get("geometry") is None and m.get("crs") is None, "B2 only")
        ck(all(m.get(k) == 0 for k in (
            "terrainCells","realSoilSamples","materializedSoilPatches",
            "materializedVegetation","materializedWeatherEvents",
            "actualParcels","activeHarvestSites","worldStateEntities",
            "actualEconomicYields")), "no materialized content")
        cx = a["contexts"]
        ck(len(cx) == 8 and [x.get("id") for x in cx] == CTX, "context IDs")
        ck(all(x.get("basinId") == HC[i] and
               x.get("status") == "CONTEXT_ONLY_NOT_MAPPED" and
               x.get("surfaceArea") is None and x.get("geometry") is None and
               x.get("quantifiedClimate") is None and
               x.get("approvedParcels") == 0 and
               x.get("actualLandCoverEntities") == 0
               for i,x in enumerate(cx[:7])), "context non materialized")
        ck(cx[7].get("basinId") is None and
           cx[7].get("status") == "NON_EVALUABLE" and
           cx[7].get("approvedParcels") == 0 and
           cx[7].get("geometry") is None and
           cx[7].get("surfaceArea") is None, "MF08 excluded")
        ck([x.get("id") for x in geo["physicalRegions"]] == CTX and
           [x.get("id") for x in hyd["basinFamilies"]] == HC and
           all(hyd["basinFamilies"][i]["contextId"] == cx[i]["id"]
               for i in range(7)), "R1/R2 map")
        soil = a["soilPrototypes"]; mic = a["microclimateRules"]
        cov = a["coverMosaics"]; res = a["resourceChains"]
        sea = a["seasonalRules"]
        ck(tuple(map(len,(soil,mic,cov,res,sea))) == COUNTS, "counts")
        for label,items,prefix in (
            ("soil",soil,"SO"),("micro",mic,"MU"),("cover",cov,"CV"),
            ("resource",res,"RN"),("season",sea,"ES")):
            ck([x.get("id") for x in items] ==
               [f"{prefix}-{i:02d}" for i in range(1,len(items)+1)], label+" IDs")
            ck(len({x.get("name") for x in items}) == len(items) and
               all(x.get("name") and x.get("status") for x in items),
               label+" names/status")
        ck(all(s.get("status") == "TEMPLATE_NOT_SURVEYED" and
               s.get("actualParcels") == 0 and
               all(s.get(k) is None for k in (
                   "actualGeometry","measuredPh","measuredDepth",
                   "measuredInfiltration","approvedUse")) and
               len(s.get("evidenceRequired",[])) == 3 and
               s.get("inference") and s.get("mechanism") and s.get("limitation") and
               s.get("contextIds") and
               set(s.get("contextIds",[])) <= set(CTX[:7])
               for s in soil), "soil safeguards")
        ck(all(s.get("status") == "RULE_CONDITIONAL_NOT_LOCATED" and
               s.get("appliedPlaces") == 0 and
               s.get("deltaTemperature") is None and
               s.get("probabilityFog") is None and s.get("daysSnow") is None and
               len(s.get("evidenceRequired", [])) == 3 and
               s.get("trigger") and s.get("potential") and s.get("guard") and
               s.get("contextIds") and set(s.get("contextIds", [])) <= set(CTX[:7])
               for s in mic), "micro safeguards")
        ck(all(s.get("status") == "COVER_TYPE_NOT_MAPPED" and
               s.get("materializedPatches") == 0 and
               s.get("individualTrees") == 0 and
               s.get("geometry") is None and s.get("area") is None and
               s.get("contextIds") and set(s.get("contextIds",[])) <= set(CTX[:7])
               and s.get("description") and s.get("guard") and
               s.get("authority") in ("CANON_REGIONAL","DESIGN_MOSAIC",
                                      "SCENARIO","REGIONAL_GRADIENT")
               for s in cov), "cover safeguards")
        ck(cov[0].get("name") == "Bosque Alto mixto" and
           cov[1].get("name") == "Bosque occidental de los Azurios" and
           cov[7].get("authority") == "REGIONAL_GRADIENT", "protected mosaics")
        ck(all(s.get("status") == "CHAIN_CONDITIONAL_NOT_ACTIVE" and
               s.get("rightsStatus") == "UNKNOWN" and
               s.get("actualProduction") == 0 and s.get("activeSites") == 0 and
               s.get("verifiedStock") is None and
               s.get("verifiedCapacity") is None and
               s.get("contextId") in CTX[:7] and
               s.get("kind") and s.get("requires") and s.get("guard")
               for s in res), "resource safeguards")
        ck(res[4].get("kind") == "FOREST_HARVEST" and
           res[4].get("contextId") == "MF-05" and
           res[9].get("kind") == "WATER_USE", "forestry/water")
        ck(all(s.get("status") == "CAUSAL_RULE_ONLY" and
               s.get("observedEvent") is False and
               s.get("date") is None and s.get("spatialInstance") is None and
               s.get("driver") and s.get("memory") for s in sea), "seasonal safeguards")
        infer = a["inferenceContract"]
        ck(set(infer.get("requiredBeforeSoilAssignment", [])) ==
           {"JURISDICTION","GEOMETRY","MATERIAL","TEXTURE","DEPTH",
            "DRAINAGE","WATER_AND_SLOPE"} and
           set(infer.get("requiredBeforeMicroclimate", [])) ==
           {"PLACED_RELIEF","EXPOSURE","REGIONAL_WEATHER","RECENT_WEATHER_MEMORY"}
           and set(infer.get("requiredBeforeCoverPlacement", [])) ==
           {"SOIL_AND_WATER","CLIMATE_AND_EXPOSURE","FOREST_RIGHTS",
            "HABITAT_TRANSITION"} and
           set(infer.get("requiredBeforeHarvest", [])) ==
           {"MATERIALIZED_STOCK","RIGHTS_PERMISSION","QUOTA_AND_REGENERATION",
            "ACCESS_AND_DOWNSTREAM_EFFECT"}, "evidence gates")
        ck(set(sum((infer[k] for k in (
            "requiredBeforeSoilAssignment","requiredBeforeMicroclimate",
            "requiredBeforeCoverPlacement","requiredBeforeHarvest")), []))
           == PERMITTED_EVIDENCE, "evidence enum")
        ck(set(infer.get("memoryRequired", [])) ==
           {"SOIL_WETNESS","SNOW_OR_FROST_IF_VERIFIED","COMPACTION",
            "COVER_DISTURBANCE","REGENERATION","HARVEST_STOCK"}, "memory")
        ck(all(infer.get(k) is True for k in (
            "noUniformBiomeByContext","noWeatherByForestLabel",
            "noFreeWaterRights","noHarvestWithoutPermission",
            "noRiversFromCover","allUnknownsMustRemainExplicit")) and
           infer.get("landUseClass") == "UNASSESSED" and
           infer.get("runtimeProvenanceStates") ==
           ["AUTHORED","DERIVED","GENERATED"] and
           infer.get("approvedRuntimeImplementations") == 0, "inference semantics")
        ck(set(a.get("hardGuards", [])) == GUARDS, "guard list")
        ck(set(a.get("reservedUnknowns", [])) >= {
            "SOIL_MATERIAL","LOCAL_TEMPERATURE_PRECIPITATION",
            "FOREST_PERIMETERS","LAND_TENURE","LOCAL_WATER_RIGHTS",
            "ACTUAL_VINEYARD_PARCELS","FAR_NORTH_MEMBERSHIP",
            "GEOMETRY_AND_CRS"}, "unknowns preserved")
        ck(a.get("handoff") == {
            "R4":"CORRIDORS_ONLY_AFTER_NATURAL_CONSTRAINTS_AND_REAL_WATER_CROSSINGS",
            "R5":"LAND_USE_ONLY_WITH_SOIL_CLIMATE_TENURE_WATER_AND_ACCESS",
            "R6":"VALRIK_PARITY_AUDIT_PENDING",
            "TEC":"GODOT_2D_WORLD_STATE_AFTER_B3"}, "handoff")
    except (KeyError, TypeError, ValueError, AttributeError) as exc:
        bad.append(f"malformed: {exc}")
    return bad


def allow_synthetic(stage: str, facts: dict) -> bool:
    """Pure gate for adversarial fabricated scenarios, never an authorization."""
    if facts.get("jurisdiction") != "casa_edranor" or
       facts.get("context") == "MF-08":
        return False
    stages = {
        "SOIL": {"geometry","material","texture","depth","drainage"},
        "MICRO": {"placed_relief","exposure","regional_weather",
                  "recent_weather_memory"},
        "COVER": {"soil_water","climate_exposure","habitat_transition",
                  "forest_rights"},
        "HARVEST": {"materialized_stock","rights_permission","quota",
                    "regeneration","access"},
        "WATER": {"real_source","quality","rights_permission",
                   "downstream_balance"},
        "VINE": {"real_parcel","soil","climate","water_rights_or_dry_farming",
                 "labour","legitimate_title"}
    }
    return bool(stage in stages and
                all(facts.get(k) is True for k in stages[stage]))


def mutation_suite(a: dict, hyd: dict, geo: dict) -> int:
    """Each independent drift must be rejected by the positive predicate."""
    checks = [
        ("phase", lambda x: x.__setitem__("phase","E19-R4")),
        ("schema", lambda x: x.__setitem__("schemaVersion",3)),
        ("authority", lambda x: x.__setitem__("authority","CANON")),
        ("precedent", lambda x: x.__setitem__("precedent","TRE SKAL")),
        ("parent", lambda x: x["parent"].__setitem__("headSha","fake")),
        ("pr84", lambda x: x["parent"].__setitem__("rejectedPR84Used",True)),
        ("west", lambda x: x["governance"].__setitem__("west","DAROVAN")),
        ("east", lambda x: x["governance"].__setitem__("east","GALDREN")),
        ("south", lambda x: x["governance"].__setitem__("south","ENTIRE_LURIEN")),
        ("north", lambda x: x["governance"].__setitem__("northArtificialClosure",True)),
        ("red_join", lambda x: x["governance"].__setitem__("northSketchJoined",True)),
        ("rodas", lambda x: x["governance"]["rodas"].__setitem__("jurisdiction","casa_edranor")),
        ("rodas_kind", lambda x: x["governance"]["rodas"].__setitem__("kind","CIUDAD")),
        ("hallheim", lambda x: x["governance"].__setitem__("hallheim","casa_edranor")),
        ("alto", lambda x: x["governance"].__setitem__("bosqueAltoHarvest","FREE")),
        ("royal", lambda x: x["governance"].__setitem__("bosqueRealHarvestByEdranor",True)),
        ("caleran", lambda x: x["governance"].__setitem__("caleranThroughDorthConfirmed",True)),
        ("antela", lambda x: x["governance"].__setitem__("karsathUrbanAntelaShoreConfirmed",True)),
        ("waterseq", lambda x: x["governance"]["sourceHydrologySequence"].reverse()),
        ("b3", lambda x: x["maturity"].__setitem__("b3Mapped",True)),
        ("b4", lambda x: x["maturity"].__setitem__("b4Runtime",True)),
        ("crs", lambda x: x["maturity"].__setitem__("crs","EPSG:4326")),
        ("soilcount", lambda x: x["maturity"].__setitem__("realSoilSamples",1)),
        ("worldstate", lambda x: x["maturity"].__setitem__("worldStateEntities",1)),
        ("contexts", lambda x: x["contexts"][0].__setitem__("basinId","HC-07")),
        ("mf08", lambda x: x["contexts"][7].__setitem__("status","EVALUABLE")),
        ("mf08geom", lambda x: x["contexts"][7].__setitem__("geometry",{})),
        ("soil_len", lambda x: x["soilPrototypes"].pop()),
        ("soil_id", lambda x: x["soilPrototypes"][0].__setitem__("id","SO-09")),
        ("soil_mf08", lambda x: x["soilPrototypes"][0]["contextIds"].append("MF-08")),
        ("soil_geom", lambda x: x["soilPrototypes"][0].__setitem__("actualGeometry",{})),
        ("soil_ph", lambda x: x["soilPrototypes"][0].__setitem__("measuredPh",7)),
        ("soil_use", lambda x: x["soilPrototypes"][0].__setitem__("approvedUse","APTO")),
        ("soil_count", lambda x: x["soilPrototypes"][0].__setitem__("actualParcels",1)),
        ("soil_why", lambda x: x["soilPrototypes"][0].__setitem__("limitation","")),
        ("micro_len", lambda x: x["microclimateRules"].pop()),
        ("micro_id", lambda x: x["microclimateRules"][0].__setitem__("id","MU-99")),
        ("micro_deg", lambda x: x["microclimateRules"][0].__setitem__("deltaTemperature",2)),
        ("micro_nieve", lambda x: x["microclimateRules"][0].__setitem__("daysSnow",30)),
        ("micro_mf08", lambda x: x["microclimateRules"][0]["contextIds"].append("MF-08")),
        ("cover_len", lambda x: x["coverMosaics"].pop()),
        ("cover_can", lambda x: x["coverMosaics"][0].__setitem__("name","Bosque infinito")),
        ("cover_royal", lambda x: x["coverMosaics"][0].__setitem__("authority","CROWN_EDRANOR")),
        ("cover_patch", lambda x: x["coverMosaics"][0].__setitem__("materializedPatches",4)),
        ("cover_area", lambda x: x["coverMosaics"][0].__setitem__("area",1000)),
        ("cover_mf08", lambda x: x["coverMosaics"][0]["contextIds"].append("MF-08")),
        ("resources_len", lambda x: x["resourceChains"].pop()),
        ("resources_wood", lambda x: x["resourceChains"][4].__setitem__("kind","FREE_HARVEST")),
        ("resources_rights", lambda x: x["resourceChains"][4].__setitem__("rightsStatus","GRANTED")),
        ("resources_stock", lambda x: x["resourceChains"][4].__setitem__("verifiedStock",1000)),
        ("resources_active", lambda x: x["resourceChains"][4].__setitem__("activeSites",1)),
        ("resources_mf08", lambda x: x["resourceChains"][0].__setitem__("contextId","MF-08")),
        ("season_len", lambda x: x["seasonalRules"].pop()),
        ("season_date", lambda x: x["seasonalRules"][0].__setitem__("date","2026-11-14")),
        ("season_event", lambda x: x["seasonalRules"][0].__setitem__("observedEvent",True)),
        ("gate_soil", lambda x: x["inferenceContract"]["requiredBeforeSoilAssignment"].remove("MATERIAL")),
        ("gate_micro", lambda x: x["inferenceContract"].__setitem__("requiredBeforeMicroclimate",[])),
        ("gate_cover", lambda x: x["inferenceContract"].__setitem__("requiredBeforeCoverPlacement",[])),
        ("gate_harvest", lambda x: x["inferenceContract"].__setitem__("requiredBeforeHarvest",[])),
        ("gate_memory", lambda x: x["inferenceContract"].__setitem__("memoryRequired",[])),
        ("gate_biome", lambda x: x["inferenceContract"].__setitem__("noUniformBiomeByContext",False)),
        ("gate_weather", lambda x: x["inferenceContract"].__setitem__("noWeatherByForestLabel",False)),
        ("gate_water", lambda x: x["inferenceContract"].__setitem__("noFreeWaterRights",False)),
        ("gate_rights", lambda x: x["inferenceContract"].__setitem__("noHarvestWithoutPermission",False)),
        ("gate_rivers", lambda x: x["inferenceContract"].__setitem__("noRiversFromCover",False)),
        ("gate_unknown", lambda x: x["inferenceContract"].__setitem__("allUnknownsMustRemainExplicit",False)),
        ("gate_APTO", lambda x: x["inferenceContract"].__setitem__("landUseClass","APTO")),
        ("gate_runtime", lambda x: x["inferenceContract"].__setitem__("approvedRuntimeImplementations",1)),
        ("guards", lambda x: x["hardGuards"].remove("NO_RODAS_TAXATION")),
        ("unknown", lambda x: x["reservedUnknowns"].remove("LAND_TENURE")),
        ("handoff", lambda x: x["handoff"].__setitem__("TEC","IMPLEMENTED")),
    ]
    for name, mutate in checks:
        x = copy.deepcopy(a)
        mutate(x)
        assert failures(x,hyd,geo), "mutation escaped: " + name
    return len(checks)


def synthetic_suite() -> int:
    base={"jurisdiction":"casa_edranor","context":"MF-04"}
    complete={
        "SOIL":["geometry","material","texture","depth","drainage"],
        "MICRO":["placed_relief","exposure","regional_weather","recent_weather_memory"],
        "COVER":["soil_water","climate_exposure","habitat_transition","forest_rights"],
        "HARVEST":["materialized_stock","rights_permission","quota","regeneration","access"],
        "WATER":["real_source","quality","rights_permission","downstream_balance"],
        "VINE":["real_parcel","soil","climate","water_rights_or_dry_farming",
                "labour","legitimate_title"]}
    count = 0
    for stage,keys in complete.items():
        valid={**base,**{k:True for k in keys}}
        assert allow_synthetic(stage,valid)
        count+=1
        for missing in keys:
            case=dict(valid); case[missing]=False
            assert not allow_synthetic(stage,case), (stage,missing)
            count+=1
        for where in ("crown_aethros","casa_darovan","casa_galdren"):
            case={**valid,"jurisdiction":where}
            assert not allow_synthetic(stage,case)
            count+=1
        case={**valid,"context":"MF-08"}
        assert not allow_synthetic(stage,case)
        count+=1
    assert not allow_synthetic("VINE",{**base})
    count+=1
    return count


def main() -> None:
    a=json.loads((DIR/"environment_v0.4.json").read_text(encoding="utf-8"))
    h=json.loads((EDR/"E19-R2"/"hydrology_v0.3.json").read_text(encoding="utf-8"))
    g=json.loads((EDR/"E19-R1"/"natural_features_v0.2.json").read_text(encoding="utf-8"))
    wrong=failures(a,h,g)
    assert not wrong, "contract errors: "+", ".join(wrong)
    for d in DOCS:
        doc=(DIR/d).read_text(encoding="utf-8")
        assert len(doc)>700, "document missing or thin: "+d
    for proof in ("Valrik","E19-R2","Rodas","Bosque Alto","B2"):
        assert proof in (DIR/"README.md").read_text(encoding="utf-8")
    num=mutation_suite(a,h,g)
    scenarios=synthetic_suite()
    print(f"PASS E19-R3: 1 valid contract, {len(DOCS)} docs, "
          f"{num} negative mutations, {scenarios} synthetic gates; "
          "R1/R2 links and Valrik B2 safeguards")


if __name__ == "__main__":
    main()

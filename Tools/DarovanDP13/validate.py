#!/usr/bin/env python3
"""D.P13 Darovan: cobertura física, canon protegido, consistencia y mutaciones negativas.
No ejecuta motor, no inventa geometría ni corrige documentos históricos.
"""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = TERR / "Datos operativos"
RIVERS = ["belara","lhera","veldora","fhalion","thalen"]
SYSTEMS = ["belara_lhera","veldora","fhalion","thalen"]
ZONES = ["d01_valkram_oeste","d01_elyra_paso_peninsular","d01_norte_transicion","d01_aguja_litoral",
         "d01_belara_treihord","d01_veldora_litoral","d01_linde_caminos","d01_pilares_sur",
         "d01_taramin_norte_centro","d01_taramin_bosque_sur","d01_syvaris","d01_arven_contexto"]
TOPICS = ["canon","landform","topology","hydro","temp","precip","snow","wind","fog",
          "soil","vegetation","season","risk","settlement"]
EXPECTED_DOCS = ["00_comparacion_fuentes_y_metodo.md","01_regiones_y_subzonas.md",
                 "02_relieve_y_microrelieve.md","03_cuencas_y_agua_menor.md",
                 "04_temperatura_y_estaciones.md","05_lluvia_nieve_y_deshielo.md",
                 "06_viento_humedad_niebla.md","07_suelos_drenaje_erosion.md",
                 "08_bosques_vegetacion_ecosistemas.md","09_inferencia_causal_y_persistencia.md",
                 "10_contratos_y_validacion.md","11_auditoria_suficiencia.md","README.md"]
def demand(ok, reason):
    if not ok:
        raise AssertionError(reason)

def load(p):
    return json.loads(p.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate)

def no_duplicate(pairs):
    out = {}
    for k,v in pairs:
        demand(k not in out, "duplicate JSON key "+k)
        out[k]=v
    return out

def validate(profiles, hydro, causal, d01, d02, d03, *, check_fs=True):
    demand(profiles["schemaVersion"] == hydro["schemaVersion"] == causal["schemaVersion"] == 1,"schema")
    demand(profiles["status"] == hydro["status"] == "derived_design_not_runtime","planning")
    demand(causal["status"] == "documented_not_executed","not executed")
    demand(not profiles["canonMutation"] and not hydro["canonMutation"],"new canon flag")
    for flag in ("containsCoordinates","containsElevations","containsMeasuredClimate",
                 "containsNamedMinorChannels","containsSettlementInstances"):
        demand(profiles[flag] is False, "invented feature "+flag)
    for flag in ("containsGeometry","containsNamedMinorRivers","containsNavigabilityClaims"):
        demand(hydro[flag] is False,"invention "+flag)
    demand(profiles["unitType"] == "qualitative_study_unit_not_polygon","fake polygons")
    demand(profiles["authorityChain"] == causal["authorityChain"] ==
           ["nimroel_core","norgard_defaults","casa_darovan","locality","world_state"],"authority")
    demand(profiles["sourceHierarchy"] == ["AUTHORED","DERIVED_CONDITIONAL",
           "PROPOSAL_PENDING_AUTHOR","GENERATED_TEST_ONLY","UNKNOWN"],"provenance")
    old_ids = [x["id"] for x in d01["physicalUnits"]]
    demand(old_ids == ZONES and [z["id"] for z in profiles["zones"]] == ZONES,"D01 units")
    demand([z["id"] for z in d03["zones"]] == ZONES,"D03 ids")
    demand(len(set(old_ids))==12,"duplicates")
    protection=profiles["existingCanons"]
    demand(protection["cities"] == ["treihord","veldora","taramin","syvaris"],"cities")
    demand(protection["excludedCity"] == "karsath" and protection["arvenOwner"] == "casa_darovan","admin")
    demand(protection["majorRivers"] == RIVERS and protection["systems"] == SYSTEMS,"rivers")
    demand(protection["agujaPermanentSettlements"] is False
           and protection["pilaresSingleForest"] is True and protection["taraminSingleForest"] is True
           and protection["syvarisDiscontinuousForest"] is True,"forests")
    demand(hydro["canonicalRivers"] == RIVERS
           and [s["id"] for s in hydro["systems"]] == SYSTEMS,"hydrology schema")
    demand([r["id"] for r in d02["rivers"]] == RIVERS
           and [s["id"] for s in d02["systems"]] == SYSTEMS,"D02 source")
    h={s["id"]:s for s in hydro["systems"]}
    demand(h["belara_lhera"]["riverIds"] == ["belara","lhera"] and
           h["belara_lhera"]["canonicalOutlets"] == ["golfo_de_norgard","golfo_de_veldora"] and
           h["belara_lhera"]["authorizedSplit"]=="belara_to_lhera","Belara-Lhera")
    demand(h["veldora"]["riverIds"]==["veldora"] and h["veldora"]["canonicalOutlets"]==["golfo_de_veldora"]
           and h["veldora"]["authorizedSplit"] is None,"Veldora independence")
    demand(h["fhalion"]["riverIds"]==["fhalion"] and h["fhalion"]["canonicalOutlets"]==[],"Fhalion unknown mouth")
    demand(h["thalen"]["riverIds"]==["thalen"] and h["thalen"]["canonicalOutlets"]==["golfo_de_norgard"]
           and h["thalen"]["authorizedSplit"]=="two_terminal_arms_around_taramin","Thalen two arms")
    guard=hydro["topologyGuards"]
    demand(guard["belaraAdjacentTreihord"] is True and guard["belaraCrossesTreihord"] is False
           and guard["lheraBranchesFrom"]=="belara","Treihord")
    demand(guard["veldoraConnectedToBelaraLhera"] is False and guard["fhalionMouth"]=="UNKNOWN"
           and guard["thalenTerminalArms"]==2 and guard["taraminBetweenArms"] is True,"river topology")
    demand(guard["namedMinorRiverCount"]==0 and guard["bridgesOrFordsCreated"]==0,"new river/bridge")
    demand(len(hydro["candidateProfiles"])==12 and
           [c["studyUnitId"] for c in hydro["candidateProfiles"]]==ZONES,"hydro zones")
    demand(all(c["assignedBasin"] is None and c["geometry"] is None and
               c["featureInstances"]==[] and c["status"]=="DERIVED_CONDITIONAL"
               for c in hydro["candidateProfiles"]),"hydro candidate != existing river")
    demand(set(hydro["minorFeatureTypes"]) == {"minor_perennial_channel_candidate",
           "seasonal_channel_candidate","ephemeral_channel_candidate","spring_candidate",
           "wetland_candidate"},"hydro candidates")
    demand(len(hydro["mandatoryInputs"])>=5 and "valid_downstream_receiver" in hydro["mandatoryInputs"],"hydro causal")
    for z in profiles["zones"]:
        demand(z["designStatus"]=="DERIVED_CONDITIONAL" and all(z[k] is None for k in (
               "altitudeMeters","temperatureC","precipitationMm","dominantWindAzimuth",
               "soilTaxon","geometry","administrativeBoundary")),"zone measurements")
        demand(all(isinstance(z[k],str) and len(z[k])>=35 for k in TOPICS),"shallow zone profile")
        demand(bool(z["sourcePaths"]) and len(set(z["sourcePaths"]))==len(z["sourcePaths"]),"source paths")
        if check_fs:
            for p in z["sourcePaths"]:
                demand(p.startswith("Worldbuilding/") and (ROOT/p).is_file(),"missing source "+p)
    demand(profiles["runtime"]=={"implementedInCoreRPG":False,"implementedInGodot":False,
                                 "persistentObjectsCreated":0},"fake runtime")
    demand(hydro["runtime"]=={"implemented":False,"generatedSegments":0,
                                "persistedWorldState":False},"fake river implementation")
    demand(all(x is False for x in causal["noClaims"].values()),"fake environmental implementation")
    demand(len(causal["rules"])==10 and len({r["id"] for r in causal["rules"]})==10,"causality rules")
    demand(all(r["cause"] and r["effect"] and r["requires"] and r["unknownFallback"]
               for r in causal["rules"]),"causal rule missing dependency")
    demand(len(causal["negativeCases"])==8 and
           len({x["id"] for x in causal["negativeCases"]})==8,"negative fixtures")
    demand(causal["futureEntityContract"]["writeAuthority"]=="corerpg_only_when_implemented"
           and causal["futureEntityContract"]["generatorVersionRequired"] is True
           and causal["futureEntityContract"]["seedRequired"] is True,"persistence versioning")
    demand(len(set(causal["persistedFieldsProposed"]))>=7,"state fields")
    if check_fs:
        demand(all((TERR/"D.P13"/p).is_file() for p in EXPECTED_DOCS),"docs missing")
        for p in profiles["sources"].values():
            demand(p.startswith("Worldbuilding/") and (ROOT/p).is_file(),"bad primary source "+p)
        for p in hydro["sources"]:
            demand((ROOT/p).is_file(),"hydro source absent")

def run():
    profiles=load(DATA/"darovan_dp13_physical_profiles_v0.1.json")
    hydro=load(DATA/"darovan_dp13_hydro_overlay_v0.1.json")
    causal=load(DATA/"darovan_dp13_environment_causal_v0.1.json")
    d01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    d02=load(DATA/"darovan_d02_hydro_network_v0.1.json")
    d03=load(DATA/"darovan_d03_climate_ecosystems_v0.1.json")
    validate(profiles,hydro,causal,d01,d02,d03)
    mutations=[
      ("extra_city",lambda p,h,c:p["existingCanons"]["cities"].append("karsath")),
      ("arven_revoked",lambda p,h,c:p["existingCanons"].__setitem__("arvenOwner","UNKNOWN")),
      ("fhalion_mouth",lambda p,h,c:h["systems"][2]["canonicalOutlets"].append("golfo_de_norgard")),
      ("belara_through_city",lambda p,h,c:h["topologyGuards"].__setitem__("belaraCrossesTreihord",True)),
      ("split_thalen_removed",lambda p,h,c:h["topologyGuards"].__setitem__("thalenTerminalArms",1)),
      ("lhera_veldora_connected",lambda p,h,c:h["topologyGuards"].__setitem__("veldoraConnectedToBelaraLhera",True)),
      ("arven_island_city",lambda p,h,c:p["existingCanons"]["cities"].append("arven")),
      ("new_named_river",lambda p,h,c:h["topologyGuards"].__setitem__("namedMinorRiverCount",1)),
      ("invented_bridge",lambda p,h,c:h["topologyGuards"].__setitem__("bridgesOrFordsCreated",1)),
      ("numeric_temperature",lambda p,h,c:p["zones"][0].__setitem__("temperatureC",14)),
      ("invented_elevation",lambda p,h,c:p["zones"][1].__setitem__("altitudeMeters",500)),
      ("runtime_claim",lambda p,h,c:p["runtime"].__setitem__("implementedInCoreRPG",True)),
      ("river_runtime_claim",lambda p,h,c:h["runtime"].__setitem__("generatedSegments",12)),
      ("fictitious_basin",lambda p,h,c:h["candidateProfiles"][0].__setitem__("assignedBasin","thalen")),
      ("missing_catchment",lambda p,h,c:h["mandatoryInputs"].remove("valid_downstream_receiver")),
      ("zone_omitted",lambda p,h,c:p["zones"].pop()),
      ("zone_without_source",lambda p,h,c:p["zones"][0].__setitem__("sourcePaths",[])),
      ("bogus_soil",lambda p,h,c:p["zones"][0].__setitem__("soilTaxon","CHERNOZEM")),
      ("fog_rule_nocause",lambda p,h,c:c["rules"][3].__setitem__("requires",[])),
      ("bogus_persisted_authority",lambda p,h,c:c["futureEntityContract"].__setitem__("writeAuthority","gemini")),
      ("single_taramin_forest_false",lambda p,h,c:p["existingCanons"].__setitem__("taraminSingleForest",False)),
      ("aguja_settlement_true",lambda p,h,c:p["existingCanons"].__setitem__("agujaPermanentSettlements",True)),
      ("status_live",lambda p,h,c:p.__setitem__("status","implemented")),
      ("missing_negative_case",lambda p,h,c:c["negativeCases"].pop()),
    ]
    for label,change in mutations:
        p,h,c=(copy.deepcopy(x) for x in (profiles,hydro,causal))
        change(p,h,c)
        try:
            validate(p,h,c,d01,d02,d03,check_fs=False)
        except AssertionError:
            continue
        raise AssertionError("Negative test did not reject "+label)
    print(f"D.P13 STATIC OK: {len(profiles['zones'])} zones, "
          f"{len(hydro['systems'])} systems, {len(causal['rules'])} causal rules, "
          f"{len(mutations)} negative tests; NO RUNTIME")

if __name__=="__main__":
    run()

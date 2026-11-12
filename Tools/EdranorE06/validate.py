"""Validacion documental E06, contratos, laboratorio y mutaciones negativas. Python 3.12."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lab import evaluate, digest

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

rules = load(BASE/"Datos operativos/edranor_e06_settlement_rules_v0.1.json")
fixtures = load(BASE/"Datos operativos/edranor_e06_synthetic_fixtures_v0.1.json")
e00 = load(BASE/"Datos operativos/edranor_e00_manifest_v0.1.json")
e01 = load(BASE/"Datos operativos/edranor_e01_relief_v0.1.json")
e02 = load(BASE/"Datos operativos/edranor_e02_hydrology_v0.1.json")
e03 = load(BASE/"Datos operativos/edranor_e03_climate_soils_ecosystems_v0.1.json")
e04 = load(BASE/"Datos operativos/edranor_e04_economy_viticulture_v0.1.json")
e05 = load(BASE/"Datos operativos/edranor_e05_roads_communications_v0.1.json")

MODELS = {
    "agricultura_mixta": ({"aldea","pueblo"}, {"agriculturalSoilValidated","seasonalWaterSupplyVerified","cultivationRightsVerified"}),
    "viticultura_condicional": ({"aldea","pueblo"}, {"wineParcelValidated","microclimateAndSoilsVerified","vineCultivationRightsVerified","vineyardSupplyVerified"}),
    "toneleria_auxiliar": ({"aldea","pueblo","enclave"}, {"licensedWorkshopSiteVerified","legitimateWoodSupplyVerified","cooperageDemandVerified","actualInputAccessVerified"}),
    "forestal_controlado": ({"aldea","enclave"}, {"managedForestPlotVerified","forestRightsVerified","regenerationPlanVerified","forestProtectionClearanceVerified"}),
    "ganaderia_transicion": ({"aldea"}, {"pastureSiteValidated","grazingRightsVerified","winterFeedVerified"}),
    "servicios_camino": ({"aldea","pueblo","enclave"}, {"physicalRoadAtSiteVerified","realTravelDemandVerified","serviceRightsVerified"}),
    "artesania_intercambio": ({"aldea","pueblo"}, {"localDemandVerified","legitimateInputsVerified","workshopRightsVerified"}),
    "bodega_auxiliar": ({"aldea","pueblo","enclave"}, {"legalWineSourceVerified","approvedStorageSiteVerified","verifiedStorageDemand","authorizedSupplyAccessVerified"})
}
FOUND = {"habitableGroundVerified","potableWaterVerified","localAccessVerified","livelihoodViableVerified","localJurisdictionVerified","landUseRightsVerified","ecologicalClearanceVerified","canonicalClearanceVerified"}
BLOCK = {"edr_e01_west_valkram_interface","edr_e01_north_cold_transition","edr_e01_far_north_unclosed"}
FLAGS = {"royal_forest","protected_habitat","unresolved_northern_border","canonical_footprint","unverified_forest_rights","unverified_local_route","unverified_water_source","archaeological_protection"}
GUARDS = {"noRuntimeMaterialization","noLocationWithoutSurvey","noPopulationOrHouseholds","noNPCsOrInventories","noTransportFromE05Questions","noViticultureFromRegionLabel","noForestCutWithoutRights","noRoyalForestClaim","noRodasEdranorAuthority","noCustomsWithinNorgard","preserveGeneratedIdentityAcrossPresentationChanges","revalidateRealSitesAfterWorldStateChanges"}
ANCHORS = {"dorth","lumina","karsath","rodas","hallheim"}

def indexed(items):
    assert isinstance(items, list) and all(isinstance(x,dict) and isinstance(x.get("id"),str) for x in items)
    assert len(items)==len({x["id"] for x in items}), "duplicated IDs"
    return {x["id"]:x for x in items}

def check(x):
    assert x["schemaVersion"]==1 and x["documentId"]=="edranor_e06_settlement_rules"
    assert x["version"]=="0.1" and x["date"]=="2026-11-12" and x["phase"]=="E06"
    assert x["status"]=="SYNTHETIC_DESIGN_ONLY" and x["runtimeEnabled"] is False
    assert x["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor","localidad","world_state"]
    assert set(x["sourceAuthorities"])=={"CANON_REPO","AUTOR_2026_11_12","OBSERVACION_MAPA","PROPUESTA","UNKNOWN"}
    assert len(x["sourceAuthorities"])==5
    s=x["scope"]
    assert s["territory"]=="casa_edranor"
    for k in ("northBoundaryClosed","georeferenced","localHydrographyValidated","localSoilsMapped","physicalRoadGraphValidated","realSitePlacementAllowed"):
        assert s[k] is False,k
    assert s["syntheticLabOnly"] is True and s["proceduralSettlementsInstantiated"]==0
    assert s["realSettlementInstances"]==[] and s["coordinates"]==s["population"]==s["territorialQuota"]=="UNKNOWN"
    anchors=indexed(x["protectedAnchors"]); assert set(anchors)==ANCHORS
    for key,a in anchors.items():
        assert a["procedural"] is False
        assert a["jurisdictionOwner"]==("crown_aethros" if key in {"rodas","hallheim"} else "casa_edranor")
        assert a["insideTerritorialContext"] is (key!="hallheim")
        if key=="rodas":
            assert a["fiscalOwner"]==a["militaryOwner"]=="crown_aethros"
    assert set(x["blockedZones"])==BLOCK and len(x["blockedZones"])==len(BLOCK)
    assert set(x["exclusionFlags"])==FLAGS and len(x["exclusionFlags"])==len(FLAGS)
    assert set(x["foundationEvidence"])==FOUND and len(x["foundationEvidence"])==len(FOUND)
    classes=x["classEvidence"]
    assert set(classes)=={"aldea","pueblo","villa","enclave"} and classes["aldea"]==[]
    assert set(classes["pueblo"])=={"localServiceDemandVerified","sharedCommunityFunctionsVerified"}
    assert set(classes["villa"])==set(classes["pueblo"])|{"urbanScaleApprovedVerified"}
    assert set(classes["enclave"])=={"residentCommunityJustifiedVerified","specializedPurposeAuthorizedVerified"}
    model_map=indexed(x["models"])
    assert set(model_map)=={"edr_e06_model_"+z for z in MODELS}
    for key,(allowed,required) in MODELS.items():
        m=model_map["edr_e06_model_"+key]
        assert set(m["classes"])==allowed and len(m["classes"])==len(allowed)
        assert set(m["extraEvidence"])==required and len(m["extraEvidence"])==len(required)
        assert m["installationConfirmed"] is False and m["unconditionalSpawn"] is False
        assert m["evidence"]=="PROPUESTA"
        assert m["potentialBuildings"] and m["potentialServices"]
        assert all(isinstance(z,str) and z for z in m["potentialBuildings"]+m["potentialServices"])
    zone_map=indexed(x["zones"])
    relief_ids={z["id"] for z in e01["reliefUnits"]}
    assert set(zone_map)==relief_ids and len(zone_map)==7
    for key,z in zone_map.items():
        assert set(z["weights"])==set(model_map)
        assert all(type(v) is int and 0<=v<=4 for v in z["weights"].values())
        assert z["terrainMapped"] is False and z["settlementSitesConfirmed"]==0 and z["evidence"]=="PROPUESTA"
        if key in BLOCK:
            assert z["eligibility"].startswith("CLOSED_") and all(v==0 for v in z["weights"].values())
        else:
            assert z["eligibility"].startswith("STUDY_ONLY") and any(v>0 for v in z["weights"].values())
    # Bosque de los Azurios no se habilita como explotación automática.
    assert zone_map["edr_e01_dorth_azurios_west"]["weights"]["edr_e06_model_forestal_controlado"]==0
    assert zone_map["edr_e01_central_wine_context"]["weights"]["edr_e06_model_viticultura_condicional"]>0
    seed=x["seedContract"]
    assert seed=={"namespace":"edranor-e06/v0.1","encoding":"json-array-utf8-compact","hash":"sha256","idHexChars":16,"idPrefix":"edr_e06_test_","selectionHashBytes":8,"modelSort":"lexicographic_id","weightedChoice":"unsigned_big_endian_modulo_weight_sum","globalRngUsed":False}
    for k in GUARDS: assert x["worldStateConstraints"][k] is True,k
    assert len(x["unknown"])==len(set(x["unknown"]))>=10
    assert {"EDD-01_NORTH_BOUNDARY_CLOSURE","EDD-02_GEOREFERENCING_AND_SCALE","EDD-03_LOCAL_WATER","EDD-07_ACCESS_AND_PATHS","E11_RUNTIME_AND_PERSISTENCE"}.issubset(set(x["unknown"]))
    assert len(x["forbiddenClaims"])==len(set(x["forbiddenClaims"]))>=12
    assert {"RODAS_PROCEDURAL","HALLHEIM_INSIDE_EDRANOR","INTERNAL_CUSTOMS","CORERPG_SETTLEMENTS_ACTIVE"}.issubset(set(x["forbiddenClaims"]))

# Herencia real y regresión cruzada, sin promover preguntas a pruebas.
assert e00["protectedIds"]==["dorth","lumina","karsath","rodas","hallheim"]
assert e00["government"]["houseControlsRodas"] is False
assert e01["cartography"]["georeferenced"] is False
assert e02["scope"]["localHydrographyValidated"] is False
assert e03["scope"]["localSoilsMapped"] is False
assert e04["scope"]["parcelMapValidated"] is False
assert e05["scope"]["physicalGraphValidated"] is False and e05["scope"]["physicalEdges"]==[]
assert {z["id"] for z in e01["reliefUnits"]}=={z["id"] for z in rules["zones"]}
required_docs = [
    "E06_INDICE.md",
    "Asentamientos/E06_ESQUELETO_ELEGIBILIDAD.md",
    "Asentamientos/E06_ARQUETIPOS_Y_ECONOMIA.md",
    "Asentamientos/E06_PESOS_REGIONALES.md",
    "Asentamientos/E06_SEMILLAS_Y_PERSISTENCIA.md",
    "Asentamientos/E06_ESCENARIOS_SINTETICOS.md",
    "Auditorias/E06_FUENTES_Y_DECISIONES.md",
    "Auditorias/E06_ACTA.md",
    "00_Control_del_proyecto/TRASPASO_E07.md",
]
for name in required_docs:
    p=BASE/name
    assert p.is_file() and p.stat().st_size>160, name
assert (ROOT/".github/workflows/edranor-e06.yml").exists()
check(rules)
assert fixtures["documentId"]=="edranor_e06_synthetic_fixtures" and fixtures["fixtureOnly"] is True
assert fixtures["canonical"] is False and fixtures["version"]=="0.1"
assert len(fixtures["scenarios"])==15
assert len({s["id"] for s in fixtures["scenarios"]})==15
passed=0; rejected=0
for case in fixtures["scenarios"]:
    assert case["worldSeed"]==fixtures["worldSeed"]
    actual=evaluate(rules, case)
    assert actual["status"]==case["expectedOutcome"],(case["id"],actual)
    assert actual==evaluate(rules,copy.deepcopy(case))
    if case["expectedOutcome"]=="LAB_CANDIDATE_ONLY":
        passed+=1
        assert actual["archetypeId"]==case["expectedModel"]
        assert actual["provenance"]=="TEST_ONLY" and actual["canonical"] is False and actual["materialized"] is False
        for k in ("visibleName","coordinates","population","worldStateId"): assert actual[k] is None
        for k in ("households","npcInstances","buildingInstances","serviceInstances","connectedRoutes","inventory"):assert actual[k]==[]
        assert actual["stableId"].startswith("edr_e06_test_")
        rotated=copy.deepcopy(case);rotated["worldSeed"]="new_world_seed"
        assert evaluate(rules,rotated)["stableId"]!=actual["stableId"]
        moved=copy.deepcopy(case);moved["slotId"]=case["slotId"]+"_different"
        assert evaluate(rules,moved)["stableId"]!=actual["stableId"]
        reordered=copy.deepcopy(rules);reordered["models"].reverse()
        assert evaluate(reordered,case)==actual
        less=copy.deepcopy(case);less["evidence"].remove("potableWaterVerified")
        assert evaluate(rules,less)["status"]=="REJECTED"
        # Raw world input must never materialize even with synthetic evidence.
        real=copy.deepcopy(case);real["fixtureKind"]="REAL"
        assert "REAL_INPUT_FORBIDDEN" in evaluate(rules,real)["reasonCodes"]
    else:
        rejected+=1
        assert case["expectedReason"] in actual["reasonCodes"],(case["id"],actual)

# Mutaciones adversarias de integridad de contrato.
mutations=[]
def add(path,value):
    mutations.append((path,value))
for key,val in [("runtimeEnabled",True),("phase","E07"),("status","ACTIVE"),("version","1.0"),("documentId","fake"),("inheritance",[]),("sourceAuthorities",[]),("foundationEvidence",[]) ,("blockedZones",[]),("exclusionFlags",[]),("unknown",[]),("forbiddenClaims",[])]:
    add([key],val)
for key in ("northBoundaryClosed","georeferenced","localHydrographyValidated","localSoilsMapped","physicalRoadGraphValidated","realSitePlacementAllowed"):
    add(["scope",key],True)
add(["scope","syntheticLabOnly"],False)
add(["scope","proceduralSettlementsInstantiated"],1)
add(["scope","realSettlementInstances"],["invented"])
for key in ("coordinates","population","territorialQuota"):
    add(["scope",key],33)
for i,a in enumerate(rules["protectedAnchors"]):
    add(["protectedAnchors",i,"procedural"],True)
    add(["protectedAnchors",i,"jurisdictionOwner"],"another_owner")
    add(["protectedAnchors",i,"insideTerritorialContext"],not a["insideTerritorialContext"])
for key in ("fiscalOwner","militaryOwner"):
    add(["protectedAnchors",3,key],"casa_edranor")
for i,zone in enumerate(rules["zones"]):
    add(["zones",i,"id"],"false_zone")
    add(["zones",i,"terrainMapped"],True)
    add(["zones",i,"settlementSitesConfirmed"],1)
    model=next(iter(zone["weights"]))
    add(["zones",i,"weights",model],5)
    add(["zones",i,"weights",model],-1)
    if zone["id"] in BLOCK:
        add(["zones",i,"weights",model],1)
for i,model in enumerate(rules["models"]):
    add(["models",i,"id"],"unknown")
    add(["models",i,"installationConfirmed"],True)
    add(["models",i,"unconditionalSpawn"],True)
    add(["models",i,"extraEvidence"],[])
for key in GUARDS:
    add(["worldStateConstraints",key],False)
for key in rules["seedContract"]:
    add(["seedContract",key],"BROKEN")
for key in rules["classEvidence"]:
    add(["classEvidence",key],["BROKEN"])
add(["models"],rules["models"]+[copy.deepcopy(rules["models"][0])])
add(["zones"],rules["zones"]+[copy.deepcopy(rules["zones"][0])])
add(["protectedAnchors"],rules["protectedAnchors"]+[copy.deepcopy(rules["protectedAnchors"][0])])
for i,(path,value) in enumerate(mutations,1):
    d=copy.deepcopy(rules);p=d
    for key in path[:-1]: p=p[key]
    p[path[-1]]=value
    try:
        check(d)
    except (AssertionError,KeyError,TypeError,ValueError): pass
    else: raise AssertionError(f"Mutacion no detectada #{i} {path}")
# Protección extra de identidad: separadores JSON y UTF-8 estables.
assert digest(["edranor-e06/v0.1","área","slot"]).hex()==digest(["edranor-e06/v0.1","área","slot"]).hex()
assert digest(["a,b","c"])!=digest(["a","b,c"])
print(f"E06 OK | {passed} casos sintéticos elegibles, {rejected} rechazos | {len(mutations)} mutaciones negativas detectadas | runtime=OFF")

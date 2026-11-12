"""Edranor E07 structural audit and mutation tests; no CoreRPG/Godot runtime."""
from __future__ import annotations
import copy
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
VIS=ROOT/"Worldbuilding/Direccion artistica/Biblia visual/Culturas/Norgard/Datos operativos"
def load(p):return json.loads(p.read_text(encoding="utf-8"))
doc=load(BASE/"Datos operativos/edranor_e07_canonical_nuclei_v0.1.json")
e00=load(BASE/"Datos operativos/edranor_e00_manifest_v0.1.json")
e02=load(BASE/"Datos operativos/edranor_e02_hydrology_v0.1.json")
e04=load(BASE/"Datos operativos/edranor_e04_economy_viticulture_v0.1.json")
e05=load(BASE/"Datos operativos/edranor_e05_roads_communications_v0.1.json")
e06=load(BASE/"Datos operativos/edranor_e06_settlement_rules_v0.1.json")
nv=load(VIS/"norgard_settlements_v0.2.json")
lu=load(VIS/"lumina_local_profile_v0.1.json")
ro=load(VIS/"rodas_local_profile_v0.1.json")
NAMES=["dorth","lumina","karsath","rodas"]
TYPES=["city","small_compact_settlement","small_lakeside_visual_settlement","village"]
PRODS=["red_wine","white_wine","exclusive_small_batch_wine","rural_and_berserker_tradition"]
ROOFS=["tile","red_tile","tile","slate"]
AREAS=[6,5,5,4]
FORBIDDEN={"lumina":{"no_walls","no_fortifications","no_major_river","no_canal","no_lake","no_harbor"},
"rodas":{"no_walls","no_fences","no_palisades","no_castle","no_fortress","no_church","no_temple","no_transformed_berserkers_wandering","no_edranor_taxation","no_edranor_military_command"},
"karsath":{"no_assumed_urban_shore","no_harbor"}}
DOCS=["E07_INDICE.md","Ciudades/Dorth/E07_DORTH.md","Ciudades/Lumina/E07_LUMINA.md",
"Ciudades/Karsath/E07_KARSATH.md","Ciudades/Rodas/E07_RODAS.md","Ciudades/E07_MATRIZ_2D.md",
"Ciudades/E07_EDIFICIOS_Y_SERVICIOS.md","Ciudades/E07_GANCHOS_JUGABLES.md",
"Auditorias/E07_FUENTES_Y_DECISIONES.md","Auditorias/E07_ACTA.md",
"00_Control_del_proyecto/TRASPASO_E08.md"]
def check(d):
    assert d["schemaVersion"]==1 and d["documentId"]=="edranor_e07_canonical_nuclei"
    assert d["phase"]=="E07" and d["version"]=="0.1" and d["date"]=="2026-11-12"
    assert d["status"]=="DOCUMENTAL_DESIGN_ONLY" and d["runtimeEnabled"] is False
    assert d["protectedIds"]==NAMES+["hallheim"]
    assert d["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"]
    assert set(d["sourceAuthorities"])=={"CANON_REPO","VISUAL_APROBADO","AUTOR_2026_11_12","OBSERVACION_MAPA","PROPUESTA","UNKNOWN"}
    s=d["scope"]
    assert s["territory"]=="casa_edranor" and s["designedCanonicalNuclei"]==4
    for key in ("georeferenced","physicalRoadGraphValidated","localWaterMapped","localSoilsMapped"):
        assert s[key] is False,key
    for key in ("instantiatedCanonicalNuclei","householdsInstantiated","buildingsInstantiated","npcInstantiated","inventoryInstantiated"):
        assert type(s[key]) is int and s[key]==0,key
    assert len(d["settlements"])==4
    for i,n in enumerate(d["settlements"]):
        id=NAMES[i]
        assert n["id"]==id and n["name"].lower()==id
        assert n["geographicContextHouse"]=="casa_edranor"
        assert n["jurisdictionOwner"]==("crown_aethros" if id=="rodas" else "casa_edranor")
        assert n["fiscalOwner"]==n["jurisdictionOwner"]
        assert n["militaryOwner"]==("crown_aethros" if id=="rodas" else "crown_supreme_house_subordinate")
        assert n["berserkerCommandOwner"]==("crown_aethros" if id=="rodas" else None)
        assert n["type"]==TYPES[i] and n["production"]==PRODS[i] and n["roof"]==ROOFS[i]
        assert n["protected"] is True and n["procedural"] is False and n["designOnly"] is True
        assert n["instantiated"] is False and n["coordinates"] is None and n["population"] is None
        assert n["physicalRoads"]==n["buildings"]==n["npcInstances"]==n["inventories"]==n["households"]==[]
        assert len(n["areas"])==AREAS[i] and len(set(n["areas"]))==AREAS[i]
        assert len(n["landmarks"])>=2 and len(set(n["landmarks"]))==len(n["landmarks"])
        assert FORBIDDEN.get(id,set()).issubset(set(n["forbidden"])) and len(n["forbidden"])>=3
        assert n["dependencies"]==["E08","E09","E10","E11"]
    out=d["outsideScope"]
    assert out=={"id":"hallheim","jurisdictionOwner":"crown_aethros","insideEdranor":False,"designed":False}
    assert set(d["rights"])=={"rodasTaxedByEdranor","rodasCommandedByEdranor","rodasBerserkersOwnedByEdranor",
       "customsBetweenGreatHouses","roadsInventedFromE05","forestExploitedWithoutRights",
       "buildingInstancesGenerated","peopleGenerated","stocksGenerated"}
    assert all(v is False for v in d["rights"].values())
    ed=d["editorial"]
    assert ed["rodasScale"]=="ALDEA" and ed["rodasDivergentNarrativeTerm"]=="CIUDAD_IN_DRAFT_SOURCES"
    assert ed["rodasTextEdited"] is False and ed["edd06TerritorialDesignResolved"] is True
    assert ed["rodasAuthorMapOverridesOldMapFlag"] is True and ed["rodasGeoreferenced"] is False
    assert ed["luminaLegalStatus"]==ed["karsathUrbanShore"]=="UNKNOWN"
    assert len(d["hooks"])==12 and len(set(d["hooks"]))==12
    assert all(h.startswith("edr_e07_hook_") for h in d["hooks"])
    assert len(d["unknown"])>=12 and len(set(d["unknown"]))==len(d["unknown"])
    assert d["runtimeClaims"]==[]
# Cross-document assertions
assert e00["protectedIds"]==NAMES+["hallheim"] and e00["government"]["houseControlsRodas"] is False
assert e02["scope"]["localHydrographyValidated"] is False
assert e04["scope"]["parcelMapValidated"] is False
assert e05["scope"]["physicalGraphValidated"] is False and e05["scope"]["physicalEdges"]==[]
assert e06["scope"]["syntheticLabOnly"] is True and e06["scope"]["proceduralSettlementsInstantiated"]==0
assert [i["id"] for i in nv["settlements"] if i["id"] in NAMES[:3]]==NAMES[:3]
assert lu["geography"]["water_rules"]["harbor"] is False
assert lu["urban_core"]["central_square"]["shape"]=="elongated"
assert ro["type"]=="village" and ro["settlement"]["fortifications"]["walls"] is False
assert ro["architecture"]["landmarkBuilding"]["religious"] is False
for rel in DOCS:
    p=BASE/rel
    assert p.is_file() and p.stat().st_size>350,rel
assert (ROOT/".github/workflows/edranor-e07.yml").exists()
check(doc)
# Mutation test: any unauthorized promotion or structural drift must fail.
mut=[]
def m(path,val):mut.append((path,val))
for key,val in [("documentId","FAKE"),("schemaVersion",5),("phase","E08"),("version","9"),
                ("date","2025"),("runtimeEnabled",True),("protectedIds",[]),("sourceAuthorities",[]),
                ("inheritance",[]),("status","ACTIVE"),("settlements",[]),("hooks",[]),("unknown",[]),
                ("runtimeClaims",["ready"])]:
    m([key],val)
for key in ("georeferenced","physicalRoadGraphValidated","localWaterMapped","localSoilsMapped"):m(["scope",key],True)
for key in ("instantiatedCanonicalNuclei","householdsInstantiated","buildingsInstantiated","npcInstantiated","inventoryInstantiated"):m(["scope",key],1)
m(["scope","designedCanonicalNuclei"],5)
for key in doc["rights"]:m(["rights",key],True)
for i,n in enumerate(doc["settlements"]):
    for key,val in [("id","fake"),("name","fake"),("jurisdictionOwner","other"),("fiscalOwner","other"),
       ("militaryOwner","other"),("berserkerCommandOwner","other"),("type","wrong"),("roof","wrong"),
       ("production","wrong"),("protected",False),("procedural",True),("designOnly",False),("instantiated",True),
       ("coordinates",[3,4]),("population",300),("physicalRoads",["road"]),("buildings",["built"]),
       ("npcInstances",["npc"]),("inventories",["stock"]),("households",["home"]),
       ("areas",[]),("landmarks",[]),("dependencies",[])]:
        m(["settlements",i,key],val)
    m(["settlements",i,"forbidden"],[])
for key,val in [("rodasScale","CITY"),("rodasDivergentNarrativeTerm","NONE"),
                ("rodasTextEdited",True),("edd06TerritorialDesignResolved",False),
                ("rodasAuthorMapOverridesOldMapFlag",False),("rodasGeoreferenced",True),
                ("luminaLegalStatus","CITY"),("karsathUrbanShore","VERIFIED")]:
    m(["editorial",key],val)
for key,val in [("id","fake"),("jurisdictionOwner","casa_edranor"),("insideEdranor",True),("designed",True)]:
    m(["outsideScope",key],val)
for index,(path,value) in enumerate(mut,1):
    copy_data=copy.deepcopy(doc);target=copy_data
    for p in path[:-1]:target=target[p]
    target[path[-1]]=value
    try:check(copy_data)
    except (AssertionError,KeyError,TypeError,ValueError):pass
    else:raise AssertionError(f"E07 NEGATIVE MUTATION ESCAPED #{index}: {path}")
print(f"E07 OK | 4 manual localities, Hallheim outside, {len(DOCS)} docs, {len(mut)} negative mutations, no runtime")

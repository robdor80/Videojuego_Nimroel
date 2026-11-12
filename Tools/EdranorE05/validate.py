"""Edranor E05: validador documental, sin motor ni mapa navegable."""
from __future__ import annotations
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
B = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
load = lambda p: json.loads(p.read_text(encoding="utf-8"))
d = load(B / "Datos operativos/edranor_e05_roads_communications_v0.1.json")
e00 = load(B / "Datos operativos/edranor_e00_manifest_v0.1.json")
e01 = load(B / "Datos operativos/edranor_e01_relief_v0.1.json")
e02 = load(B / "Datos operativos/edranor_e02_hydrology_v0.1.json")
e03 = load(B / "Datos operativos/edranor_e03_climate_soils_ecosystems_v0.1.json")
e04 = load(B / "Datos operativos/edranor_e04_economy_viticulture_v0.1.json")
U = "UNKNOWN"
ANCHORS = {"dorth","lumina","karsath","rodas","hallheim"}
ROADS = {
 "dorth_lumina": ("dorth","lumina","edr_e01_corridor_lumina_dorth","edr_e04_trade_question_dorth_lumina"),
 "lumina_karsath": ("lumina","karsath","edr_e01_corridor_karsath_lumina","edr_e04_trade_question_lumina_karsath"),
 "dorth_karsath": ("dorth","karsath","NONE","edr_e04_trade_question_dorth_karsath"),
 "dorth_rodas": ("dorth","rodas","edr_e01_corridor_rodas","NONE"),
}
EXT = {"edranor_rodas":("casa_edranor","rodas"),"edranor_realm":("casa_edranor","norgard_commercial_network")}
CHANNELS = {"foot_messenger","mounted_courier","merchant_dispatch","local_notice","emergency_signal"}
GATES = {"boundary","georeference","hydrology","seasonality","rights","royal_access","world_state"}
DEPENDENCIES = {"boundary":"EDD-01","georeference":"EDD-02","hydrology":"EDD-03","seasonality":"E03","rights":"EDD-07","royal_access":"RODAS_CROWN","world_state":"E11_WORLD_STATE"}
FALSE_SCOPE = ("northBoundaryClosed","georeferenced","metricGeometryValidated","physicalGraphValidated","hydrologicalCrossingsValidated","pathfindingEnabled","communicationsEnabled")
EMPTY_SCOPE = ("roadPolylines","physicalEdges","bridges","fords","courierStations","signalTowers")
BOOL_BASIS_TRUE = ("dorthSeat","luminaKarsathEdranor","rodasRoyal","hallheimOutside","realmWineTrade","antelaSouthOfKarsath","lurienNavigableHallheimToSea")
BOOL_BASIS_FALSE = ("localLurienTransportConfirmed","localRoadsConfirmed")
BOOL_RIGHT_TRUE = ("rodasBerserkersUnderCrown","noInternalHouseCustoms","servicesNeedActualAuthorization","propertyRightsPreserved")
BOOL_RIGHT_FALSE = ("edranorControlsRodas","hallheimInEdranor","foreignCustomsAtRodas","automaticTransitToll","forestHarvestWithoutRights")
GUARD_TRUE = ("roadRequiresConfirmedGeometry","deliveryRequiresRealAgentAndGoods","eventualClosureRequiresRealRouteAndEvent","noTransitTimeFromMapSymbols","noRoadGenerationFromQuestions","noAutomaticWineShippingOnLurien","noUnverifiedWinterClosure")
EXPECTED_UNKNOWN = {"EDD-01_NORTH_BOUNDARY_CLOSURE","EDD-02_GEOREFERENCING_AND_SCALE","EDD-03_LOCAL_WATER_AND_GROUNDWATER","EDD-07_ACCESS_AND_PATHS","ROUTE_RIGHTS_AND_OWNERSHIP","BRIDGES_AND_FORDS","DISTANCES_AND_TRAVEL_TIMES","LOCAL_PASSABILITY","RODAS_REAL_ACCESS_PROTOCOL","POSTAL_NETWORK","FOREST_ACCESS_RIGHTS","MAINTENANCE_AND_SECURITY"}
EXPECTED_FORBIDDEN = {"PHYSICAL_DORTH_LUMINA_ROAD_EXISTS","PHYSICAL_LUMINA_KARSATH_ROAD_EXISTS","PHYSICAL_DORTH_KARSATH_ROAD_EXISTS","PHYSICAL_DORTH_RODAS_ROAD_EXISTS","RODAS_EDRANOR_TAXES","RODAS_EDRANOR_BERSERKERS","HALLHEIM_INSIDE_EDRANOR","LOCAL_LURIEN_WINE_BOATS_CONFIRMED","VALKRAM_PASS_CONFIRMED","BRIDGE_WITHOUT_SURVEY","UNVERIFIED_TRAVEL_TIME","CUSTOMS_WITHIN_NORGARD","INSTALLED_POST_STATIONS","PATHFINDING_ON_STUDY_GRAPH","E05_RUNTIME_CERTIFIED"}
def by_id(seq):
    assert isinstance(seq,list)
    assert len(seq)==len({x["id"] for x in seq}),"IDs duplicados"
    return {x["id"]:x for x in seq}
def check(x):
    assert x["schemaVersion"]==1 and x["documentId"]=="edranor_e05_roads_communications"
    assert x["version"]=="0.1" and x["date"]=="2026-11-12"
    assert x["phase"]=="E05" and x["status"]=="DOCUMENTARY_PLANNING_ONLY"
    assert x["runtimeEnabled"] is False
    assert x["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor","localidad","world_state"]
    assert set(x["sourceAuthorities"])=={"CANON_REPO","AUTOR_2026_11_12","OBSERVACION_MAPA","PROPUESTA","UNKNOWN"}
    assert len(x["sourceAuthorities"])==5
    s=x["scope"]
    assert s["territory"]=="casa_edranor"
    for k in FALSE_SCOPE: assert s[k] is False,k
    for k in EMPTY_SCOPE: assert s[k]==[],k
    for k in ("coordinates","scale"): assert s[k]==U,k
    b=x["canonicalBasis"]
    for k in BOOL_BASIS_TRUE: assert b[k] is True,k
    for k in BOOL_BASIS_FALSE: assert b[k] is False,k
    a=by_id(x["anchors"]); assert set(a)==ANCHORS
    for id in ANCHORS:
        z=a[id]
        assert z["owner"]==("crown_aethros" if id in ("rodas","hallheim") else "casa_edranor")
        assert z["inside"] is (id!="hallheim")
        assert z["roadAccess"]==U
        assert z["evidence"]==("AUTOR_2026_11_12" if id=="rodas" else "CANON_REPO")
    q=by_id(x["candidateRoadQuestions"]);assert len(q)==4
    assert set(q)=={"edr_e05_question_"+suffix for suffix in ROADS}
    for suffix,(src,dst,corr,trade) in ROADS.items():
        z=q["edr_e05_question_"+suffix]
        assert (z["from"],z["to"],z["sourceE01"],z["sourceE04"])==(src,dst,corr,trade)
        assert z["status"]=="QUESTION_ONLY" and z["roadConfirmed"] is False and z["traversable"] is False
        for k in ("geometry","length","travelTime","roadClass","waterCrossings","rights","maintenance","seasonality"): assert z[k]==U,k
        assert z["evidence"]=="PROPUESTA"
    ee=by_id(x["externalInterfaces"]);assert len(ee)==2
    assert set(ee)=={"edr_e05_external_"+suffix for suffix in EXT}
    for suffix,(src,dst) in EXT.items():
        z=ee["edr_e05_external_"+suffix]
        assert (z["from"],z["to"],z["sourceE04"])==(src,dst,"edr_e04_trade_question_"+suffix)
        assert z["status"]=="QUESTION_ONLY" and z["roadConfirmed"] is False
        assert z["itinerary"]==z["authorityToAgree"]==U and z["foreignCustomsBorder"] is False
        assert z["evidence"]=="PROPUESTA"
    p=x["passQuestion"]
    assert p["id"]=="edr_e05_question_valkram" and p["sourceE01"]=="edr_e01_corridor_valkram"
    assert p["namedPassConfirmed"] is False and p["physicalConnectionConfirmed"] is False
    for k in ("geometry","legalAccess","winterCondition"): assert p[k]==U,k
    assert p["evidence"]=="PROPUESTA"
    cc=by_id(x["communicationStudies"]);assert set(cc)=={"edr_e05_channel_"+c for c in CHANNELS}
    for z in cc.values():
        assert z["optionOnly"] is True and z["networkInstalled"] is False
        assert z["stations"]==[] and z["operators"]==z["coverage"]==z["deliveryTime"]==U
        assert z["guaranteedDelivery"] is False and z["evidence"]=="PROPUESTA"
    gg=by_id(x["validationGates"]);assert set(gg)=={"edr_e05_gate_"+g for g in GATES}
    for suffix,dep in DEPENDENCIES.items():
        z=gg["edr_e05_gate_"+suffix]
        assert z["dependsOn"]==dep and z["passed"] is False and z["proof"]==U
    f=x["rightsAndFiscality"]
    assert f["rodasFiscalOwner"]==f["rodasMilitaryOwner"]=="crown_aethros"
    for k in BOOL_RIGHT_TRUE: assert f[k] is True,k
    for k in BOOL_RIGHT_FALSE: assert f[k] is False,k
    assert f["roadOwner"]==f["serviceTariff"]==U
    for k in GUARD_TRUE: assert x["worldStateConstraints"][k] is True,k
    assert set(x["unknown"])==EXPECTED_UNKNOWN and len(x["unknown"])==len(EXPECTED_UNKNOWN)
    assert set(x["forbiddenClaims"])==EXPECTED_FORBIDDEN and len(x["forbiddenClaims"])==len(EXPECTED_FORBIDDEN)

# Regresiones directas de los artefactos anteriores; no solo manifest E05.
assert e00["house"]["seatId"]=="dorth" and set(e00["protectedIds"])==ANCHORS
assert {c["id"] for c in e01["corridorQuestions"]}>={"edr_e01_corridor_lumina_dorth","edr_e01_corridor_karsath_lumina","edr_e01_corridor_rodas","edr_e01_corridor_valkram"}
assert e02["scope"]["localHydrographyValidated"] is False
assert e03["scope"]["localSoilsMapped"] is False
assert e04["scope"]["transportGraphValidated"] is False
assert {x["id"] for x in e04["tradeStudy"]}=={"edr_e04_trade_question_dorth_lumina","edr_e04_trade_question_lumina_karsath","edr_e04_trade_question_dorth_karsath","edr_e04_trade_question_edranor_rodas","edr_e04_trade_question_edranor_realm"}
assert "navegable desde Hallheim hasta el mar" in (N/"Geografía/rios_y_lagos.md").read_text(encoding="utf-8")
required = [
 B/"E05_INDICE.md",B/"Comunicaciones/E05_GRAFO_Y_CORREDORES.md",
 B/"Comunicaciones/E05_VIABILIDAD_Y_RIESGOS.md",B/"Comunicaciones/E05_TRANSPORTE_Y_LOGISTICA.md",
 B/"Comunicaciones/E05_MENSAJERIA_Y_AVISOS.md",B/"Comunicaciones/E05_JURISDICCION_Y_MANTENIMIENTO.md",
 B/"Auditorias/E05_FUENTES_Y_DECISIONES.md",B/"Auditorias/E05_ACTA.md",
 B/"00_Control_del_proyecto/TRASPASO_E06.md",
 ROOT/".github/workflows/edranor-e05.yml",ROOT/"Tools/EdranorE05/validate.py"
]
for path in required: assert path.is_file() and path.stat().st_size>70,path
check(d)

# Mutaciones negativas: toda promoción ficticia o usurpación debe fallar.
mut=[]
def add(path,v):mut.append((path,v))
for k,v in [("schemaVersion",2),("phase","E06"),("runtimeEnabled",True),("status","ACTIVE"),
 ("documentId","other"),("version","0.2"),("date","2001-01-01"),("inheritance",[]),
 ("sourceAuthorities",["CANON_REPO"]),("unknown",[]),("forbiddenClaims",[])]:add([k],v)
for k in FALSE_SCOPE:add(["scope",k],True)
for k in EMPTY_SCOPE:add(["scope",k],[{"fake":"road"}])
for k in ("territory","coordinates","scale"):add(["scope",k],"FABRICATED")
for k in BOOL_BASIS_TRUE:add(["canonicalBasis",k],False)
for k in BOOL_BASIS_FALSE:add(["canonicalBasis",k],True)
for i,z in enumerate(d["anchors"]):
 for k,v in [("id","false"),("owner","usurper"),("inside",not z["inside"]),("roadAccess","ROAD"),("evidence","PROPUESTA")]:add(["anchors",i,k],v)
for i,z in enumerate(d["candidateRoadQuestions"]):
 for k,v in [("from","false"),("to","false"),("sourceE01","FABRICATED"),("sourceE04","FABRICATED"),("status","OPEN_ROAD"),("roadConfirmed",True),("traversable",True),("geometry","ROAD"),("length",12),("travelTime",35),("roadClass","PAVED"),("waterCrossings","BRIDGE"),("rights","CROWN"),("maintenance","CROWN"),("seasonality","ALL_YEAR"),("evidence","CANON_REPO")]:add(["candidateRoadQuestions",i,k],v)
for i,z in enumerate(d["externalInterfaces"]):
 for k,v in [("from","hallheim"),("to","fake"),("sourceE04","fake"),("status","ACTIVE"),("roadConfirmed",True),("itinerary","ROAD"),("authorityToAgree","EDRANOR"),("foreignCustomsBorder",True),("evidence","CANON_REPO")]:add(["externalInterfaces",i,k],v)
for k,v in [("namedPassConfirmed",True),("physicalConnectionConfirmed",True),("geometry","ROAD"),("legalAccess","OPEN"),("winterCondition","ALWAYS_CLOSED"),("sourceE01","NONE"),("evidence","CANON_REPO")]:add(["passQuestion",k],v)
for i,z in enumerate(d["communicationStudies"]):
 for k,v in [("optionOnly",False),("networkInstalled",True),("stations",["posta"]),("operators","CONFIRMED"),("coverage","FULL"),("deliveryTime",30),("guaranteedDelivery",True),("evidence","CANON_REPO")]:add(["communicationStudies",i,k],v)
for i,z in enumerate(d["validationGates"]):
 for k,v in [("dependsOn","DONE"),("passed",True),("proof","YES")]:add(["validationGates",i,k],v)
for k in BOOL_RIGHT_TRUE:add(["rightsAndFiscality",k],False)
for k in BOOL_RIGHT_FALSE:add(["rightsAndFiscality",k],True)
for k in ("rodasFiscalOwner","rodasMilitaryOwner"):add(["rightsAndFiscality",k],"casa_edranor")
for k in ("roadOwner","serviceTariff"):add(["rightsAndFiscality",k],100)
for k in GUARD_TRUE:add(["worldStateConstraints",k],False)
for k in ("anchors","candidateRoadQuestions","externalInterfaces","communicationStudies","validationGates"):
 add([k],d[k]+[copy.deepcopy(d[k][0])])
for n,(path,val) in enumerate(mut,1):
 z=copy.deepcopy(d);t=z
 for key in path[:-1]:t=t[key]
 t[path[-1]]=val
 try:check(z)
 except (AssertionError,KeyError,ValueError,TypeError):pass
 else:raise AssertionError(f"mutación no detectada #{n}: {path}")
print(f"E05 OK | {len(mut)} mutaciones negativas rechazadas | sin rutas físicas, sin runtime")

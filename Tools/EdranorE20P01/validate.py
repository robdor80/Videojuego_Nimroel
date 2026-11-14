#!/usr/bin/env python3
"""Valida los vetos de la monografía funcional E20-P01, no el videojuego."""
import copy
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/E20/P01/dorth_program_v0.1.json"
EXPECTED_IDS={f"DOR-F{i:02d}" for i in range(1,13)}
def check(d):
    e=[]
    if d.get("status")!="DEEP_FUNCTIONAL_DESIGN_ONLY" or d.get("runtimeEnabled") is not False:
        e.append("state")
    if d.get("georeferenced") is not False or d.get("metricGeometryValidated") is not False:
        e.append("false metrics")
    loc=d.get("location",{})
    if loc.get("id")!="dorth" or loc.get("authorityOwner")!="casa_edranor" or loc.get("sovereign")!="crown_aethros":
        e.append("location/authority")
    if loc.get("coordinates") is not None or loc.get("population") is not None:
        e.append("false location/population")
    a=d.get("functionalAreas",[])
    if len(a)!=12 or {x.get("id") for x in a}!=EXPECTED_IDS:e.append("functional IDs")
    for x in a:
        if x.get("status")!="DESIGN_NOT_MATERIALIZED" or x.get("coordinates") is not None or x.get("geometry") is not None:
            e.append("area promoted")
        if any(x.get(k)!=[] for k in ("buildingInstanceIds","personInstanceIds","parcels")):
            e.append("instances promoted")
    for k in ("physicalRoads","actualPeople","actualBuildings","actualLots","actualHouseholds","realWorldEvents"):
        if d.get(k)!=[]:e.append(k)
    p=d.get("protected",{})
    for k in ("royalSeatRequired","royalApartmentsRequired"):
        if p.get(k) is not True:e.append(k)
    for k in ("hallheimInsideEdranor","edranorOwnLaw","edranorIndependentArmy","azuriosRoyalForestAccessGranted","karsathUrbanHarborInvented","luminaMonthlyFairInvented"):
        if p.get(k) is not False:e.append(k)
    if p.get("rodasAuthority")!="crown_aethros":e.append("Rodas")
    if d.get("processDependencyKind")!="FUNCTIONAL_ONLY_NOT_ROADS":e.append("roads disguised")
    links=d.get("requiredProcessDependencies",[])
    if any(len(x)!=2 or x[0] not in EXPECTED_IDS or x[1] not in EXPECTED_IDS for x in links):e.append("broken graph")
    s=d.get("scenarioDesigns",[])
    if len(s)!=3 or {x.get("id") for x in s}!={"DOR-SC01","DOR-SC02","DOR-SC03"}:e.append("scenes")
    if any(x.get("status")!="UNTRIGGERED_PROPOSAL" or x.get("eventsCreated")!=0 or not x.get("requirements") for x in s):e.append("events faked")
    if d.get("maturity")!={"B2":"DESIGN_STRENGTHENED","B3":"NOT_ACCREDITED","B4":"NOT_ACCREDITED"}:
        e.append("maturity")
    if d.get("validatorsDoNotCertifyRuntime") is not True:e.append("runtime claim")
    if "E19_PR84_MAP" not in d.get("forbiddenFeatureInheritance",[]):e.append("forbidden E19")
    return e

def main():
    d=json.loads(P.read_text(encoding="utf-8"))
    assert not check(d),check(d)
    tests=[]
    for k,v in [("status","COMPLETE"),("runtimeEnabled",True),("georeferenced",True),
                ("metricGeometryValidated",True),("physicalRoads",[{"edge":"fake"}]),
                ("actualPeople",["npc"]),("actualBuildings",["b"]),("actualLots",["wine"]),
                ("actualHouseholds",["home"]),("realWorldEvents",["event"]),
                ("processDependencyKind","PHYSICAL_ROADS"),("validatorsDoNotCertifyRuntime",False)]:
        evil=copy.deepcopy(d);evil[k]=v;tests.append((k,evil))
    for k,v in [("rodasAuthority","casa_edranor"),("royalSeatRequired",False),
                ("royalApartmentsRequired",False),("edranorOwnLaw",True),
                ("azuriosRoyalForestAccessGranted",True),("karsathUrbanHarborInvented",True)]:
        evil=copy.deepcopy(d);evil["protected"][k]=v;tests.append((k,evil))
    evil=copy.deepcopy(d);evil["location"]["population"]=12000;tests.append(("fictional census",evil))
    evil=copy.deepcopy(d);evil["location"]["coordinates"]=[10,10];tests.append(("fictional map",evil))
    evil=copy.deepcopy(d);evil["functionalAreas"][0]["geometry"]={"type":"Polygon"};tests.append(("fictional district",evil))
    evil=copy.deepcopy(d);evil["functionalAreas"][0]["buildingInstanceIds"]=["b001"];tests.append(("fictional building",evil))
    evil=copy.deepcopy(d);evil["scenarioDesigns"][0]["eventsCreated"]=1;tests.append(("fictional historical event",evil))
    evil=copy.deepcopy(d);evil["maturity"]["B3"]="ACCREDITED";tests.append(("false B3",evil))
    evil=copy.deepcopy(d);evil["forbiddenFeatureInheritance"]=[];tests.append(("rejected map",evil))
    for k,v in tests:
        assert check(v),f"mutated item unexpectedly passed: {k}"
    print(f"E20-P01 PASS baseline + {len(tests)} negative mutations; no B3/B4 claims")
if __name__=="__main__":main()

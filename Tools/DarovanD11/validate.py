#!/usr/bin/env python3
"""D11: validación estática y adversarial. No ejecuta reglas de dominio."""
import argparse
import copy
import json
import re
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT=Path(__file__).resolve().parents[2]
D11=ROOT/"ContentPacks/darovan-territory"
OPER="Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/Datos operativos/"
PACK="nimroel.darovan.territory"
CITIES=["treihord","veldora","taramin","syvaris"]
RIVERS=["belara","lhera","veldora","fhalion","thalen"]
SYSTEMS=["belara_lhera","veldora","fhalion","thalen"]
PHYSICAL=["d05_road_veldora_treihord","d05_belara_shallow_haul","d05_vena_restricted"]
SUPPLY=["d05_ore_cart_stage","d05_ore_port_handling","d05_coal_azurios_supply","d05_pilares_wood_supply"]
FILES=["darovan_d00_canonical_anchors_v0.1.json","darovan_d01_relief_profile_v0.1.json",
"darovan_d02_hydro_network_v0.1.json","darovan_d03_climate_ecosystems_v0.1.json",
"darovan_d04_resources_production_v0.1.json","darovan_d05_mobility_communications_v0.1.json",
"darovan_d06_settlement_rules_v0.1.json","darovan_d07_canonical_cities_v0.1.json",
"darovan_d08_population_services_v0.1.json","darovan_d09_governance_security_v0.1.json",
"darovan_d10_culture_society_v0.1.json"]

class D11Error(Exception):
    pass

def pairs_no_dup(items):
    result={}
    for k,v in items:
        if k in result: raise D11Error("JSON duplicate key "+k)
        result[k]=v
    return result

def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),object_pairs_hook=pairs_no_dup)

def ok(value, what):
    if not value: raise D11Error(what)

def blob_sha(path):
    name=path.relative_to(ROOT).as_posix()
    return subprocess.run(["git","hash-object","--path="+name,name],cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()

def check(p,m,defs,tests,real_sources=True):
    ok(p["schemaVersion"]==1 and p["projectionVersion"]=="0.1.0" and p["contentContract"]=="0.1.0","D11 version")
    ok(p["packId"]==PACK and p["status"]=="planning_reference_not_runtime","D11 boundary")
    ok(type(p["worldStateEntitiesCreated"]) is int and p["worldStateEntitiesCreated"]==0,"WorldState fiction")
    ok(p["dataClassification"]=="AUTHORING_PROJECTION_ONLY","classification")
    ok(p["authorityLayers"]==["nimroel_core","norgard_defaults","casa_darovan","localidad","world_state"],"authority order")
    ok(p["canonicalCityIds"]==CITIES and p["excludedCityIds"]==["karsath"],"canonical cities")
    ok(p["islandAdministrativeOwner"]=={"arven":"casa_darovan","syvaris":"casa_darovan"},"islands")
    ok(p["arvenCulturalIdentity"] is None,"Arven culture UNKNOWN")
    ok(p["namedRiverIds"]==RIVERS and p["hydroSystemIds"]==SYSTEMS and p["belaraCrossesTreihord"] is False,"hydrology")
    ok(p["unmeasuredRouteDistances"] is True,"distances unknown")
    ok(p["physicalTransportLinkIds"]==PHYSICAL and p["supplyRelationsNotRoutes"]==SUPPLY,"actual routes vs supply")
    ok(p["sourceDemographyPointer"]=="/territoryPopulation" and p["sourceCultureDecisionPointer"]=="/authorDecisions","source JSON pointers")
    cap=p["executionCapabilities"]
    ok(set(cap)=={"territoryLogic","resourceConversion","routing","householdMigration","culturalPersonality","fiscalAuthority","hostIntegration"} and all(v is False for v in cap.values()),"unproven runtime")
    locks=p["sourceLocks"]
    ok(len(locks)==11 and [l["phase"] for l in locks]==["D%02d"%i for i in range(11)],"phase locks")
    for i,l in enumerate(locks):
        ok(set(l)=={"phase","path","gitBlobSha"} and l["path"]==OPER+FILES[i],"traceability")
        ok(bool(re.fullmatch(r"[0-9a-f]{40}",l["gitBlobSha"])),"source git sha")
        if real_sources: ok(blob_sha(ROOT/l["path"])==l["gitBlobSha"],"source altered "+l["phase"])
    if real_sources:
        d={i:read(ROOT/OPER/FILES[i]) for i in (2,5,7,8,9,10)}
        ok([r["id"] for r in d[2]["rivers"]]==RIVERS and [x["id"] for x in d[2]["systems"]]==SYSTEMS,"D02")
        ok(d[7]["manualCityIds"]==CITIES and [c["id"] for c in d[7]["cities"]]==CITIES,"D07")
        ok(d[8]["manualCityIds"]==CITIES,"D08")
        ok(d[9]["government"]["crownSupreme"] is True and d[9]["security"]["darovanIndependentNavy"] is False,"D09")
        ok([x["option"] for x in d[10]["authorDecisions"]]==["C" if i==9 else "B" for i in range(1,18)],"D10")
        ok(d[10]["unknowns"]["arvenCulturalIdentity"] is None,"D10 Arven")
        ok([x["id"] for x in d[5]["confirmedTransportLinks"]]==PHYSICAL and all(x["physicalRouteConfirmed"] is True for x in d[5]["confirmedTransportLinks"]),"D05 routes")
        ok([x["id"] for x in d[5]["supplyRelationsNotRoutes"]]==SUPPLY and all(x["physicalRouteConfirmed"] is False for x in d[5]["supplyRelationsNotRoutes"]),"D05 supply")
    ok(m["pack_id"]==PACK and m["pack_version"]=="0.1.0" and m["content_contract_version"]=="0.1.0" and m["minimum_core_version"]=="0.1.0","Core manifest")
    ok(m["dependencies"]==[] and m["resources"]==sorted(defs) and len(defs)==5 and len(set(m["resources"]))==5,"Core physical pack")
    ids=[PACK+":territory/darovan"]+[PACK+":cities/"+c for c in CITIES]
    ok([x["id"] for x in p["definitions"]]==ids and len({x["id"] for x in p["definitions"]})==5,"D11 ids")
    ok(all(x["sourcePhase"]=="D07" and x["sourcePointer"] in ["/manualCityIds"]+["/cities/"+str(i) for i in range(4)] for x in p["definitions"]),"source pointers")
    ok({x["id"] for x in defs.values()}==set(ids),"Core definition IDs")
    for item in defs.values():
        ok(set(item)=={"$schema","id","kind","references"},"Content Contract 0.1.0 payload prohibited")
        for link in item["references"]:
            ok(set(link)=={"expected_kind","target"},"reference fields")
            target=next((x for x in defs.values() if x["id"]==link["target"]),None)
            ok(target is not None and target["kind"]==link["expected_kind"],"missing/wrong reference")
    territory=defs["resources/territory/darovan.json"]
    ok(territory["kind"]=="territory_reference" and territory["id"]==ids[0] and len(territory["references"])==4,"territory envelope")
    for city in CITIES:
        item=defs["resources/cities/"+city+".json"]
        ok(item["kind"]=="canonical_city_reference" and item["id"]==PACK+":cities/"+city and item["references"]==[],"city definition")
    ok(tests["version"]=="0.1.0" and tests["status"]=="TEST_ONLY" and type(tests["worldStateEvents"]) is int and tests["worldStateEvents"]==0,"technical fixtures")
    ok([x["id"] for x in tests["scenarios"]]==["T%02d"%i for i in range(1,9)],"T01-T08")
    for s in tests["scenarios"]:
        ok(s["classification"]=="TEST_ONLY" and s["kind"]=="SPECIFICATION_NOT_EXECUTED" and s["executedInCoreRPG"] is False,"false executable claim")
        ok(s["requires"] in cap and cap[s["requires"]] is False and all(z in ["D%02d"%i for i in range(11)] for z in s["sourcePhases"]),"test dependencies")

def official_core_schema(core,m,defs):
    directory=core/"schemas/content/0.1.0"
    schemas=[read(directory/x) for x in ("types.schema.json","content-pack-manifest.schema.json","resource-definition.schema.json")]
    reg=Registry()
    for s in schemas: reg=reg.with_resource(s["$id"],Resource.from_contents(s))
    Draft202012Validator(schemas[1],registry=reg).validate(m)
    for item in defs.values(): Draft202012Validator(schemas[2],registry=reg).validate(item)

def negatives(p,m,d,t):
    edits=[]
    def change(which,name,fn):
        original=[p,m,d,t][which]; x=copy.deepcopy(original);fn(x);edits.append((which,name,x))
    change(0,"foreign city",lambda x:x["canonicalCityIds"].append("karsath"))
    change(0,"Arven owner",lambda x:x["islandAdministrativeOwner"].update(arven="other"))
    change(0,"Arven culture",lambda x:x.update(arvenCulturalIdentity="mercantile"))
    change(0,"Belara",lambda x:x.update(belaraCrossesTreihord=True))
    change(0,"new river",lambda x:x["namedRiverIds"].append("unknown-river"))
    change(0,"new road",lambda x:x["physicalTransportLinkIds"].append("d05_coal_azurios_supply"))
    change(0,"coal route",lambda x:x["supplyRelationsNotRoutes"].remove("d05_coal_azurios_supply"))
    change(0,"world state",lambda x:x.update(worldStateEntitiesCreated=1))
    change(0,"runtime",lambda x:x["executionCapabilities"].update(routing=True))
    change(0,"drift",lambda x:x["sourceLocks"][0].update(gitBlobSha="0"*40))
    change(0,"fake provenance",lambda x:x["sourceLocks"][1].update(path="other"))
    change(0,"inverted authority",lambda x:x["authorityLayers"].reverse())
    change(0,"unstable ids",lambda x:x["definitions"][1].update(id=PACK+":cities/other"))
    change(1,"fabricated dependency",lambda x:x["dependencies"].append({"pack_id":"nimroel.core","version_requirement":{"minimum_inclusive":"1.0.0"}}))
    change(1,"duplicate resource",lambda x:x["resources"].append(x["resources"][0]))
    change(1,"pack replacement",lambda x:x.update(pack_id="fake.pack"))
    change(2,"unauthorized payload",lambda x:x["resources/cities/treihord.json"].update(population=32000))
    change(2,"resource unknown ID",lambda x:x["resources/cities/treihord.json"].update(id=PACK+":cities/other"))
    change(2,"broken link",lambda x:x["resources/territory/darovan.json"]["references"][0].update(target=PACK+":cities/other"))
    change(3,"world event",lambda x:x.update(worldStateEvents=1))
    change(3,"executed flag",lambda x:x["scenarios"][0].update(executedInCoreRPG=True))
    change(3,"canonical event",lambda x:x["scenarios"][0].update(classification="CANON"))
    change(3,"missing T08",lambda x:x["scenarios"].pop())
    for which,name,obj in edits:
        all_items=[p,m,d,t]; all_items[which]=obj
        try: check(*all_items,real_sources=False)
        except D11Error: pass
        else: raise D11Error("Negative mutation accepted: "+name)
    return len(edits)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--core-root",type=Path)
    args=parser.parse_args()
    p=read(D11/"authoring/projection-v0.1.json")
    m=read(D11/"pack/manifest.json")
    d={name:read(D11/"pack"/name) for name in m["resources"]}
    t=read(D11/"fixtures/d11-scenarios-v0.1.json")
    Draft202012Validator(read(D11/"schemas/projection.schema.json")).validate(p)
    check(p,m,d,t)
    if args.core_root:
        official_core_schema(args.core_root,m,d)
        print("CoreRPG 0.1.0 original schema: PASS")
    else: print("CoreRPG original schema: NOT EXECUTED; supply --core-root")
    count=negatives(p,m,d,t)
    print("D11 STATIC PASS: 11 locked sources, 5 definitions, 8 TEST_ONLY specs, %d rejected mutations"%count)
    print("No domain economy, fiscal, cultural, routing or Godot runtime execution claimed.")

if __name__=="__main__":
    main()

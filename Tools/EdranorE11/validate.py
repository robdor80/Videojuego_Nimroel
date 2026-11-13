#!/usr/bin/env python3
"""Edranor E11: document/source contract, CoreRPG schema and adversarial checks. Not gameplay."""
import argparse
import copy
import json
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
OPER = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/Datos operativos/"
PACKDIR = ROOT / "ContentPacks/edranor-territory"
PACK = "nimroel.edranor.territory"
NAMES = ["dorth","lumina","karsath","rodas"]
OWNERS = ["casa_edranor","casa_edranor","casa_edranor","crown_aethros"]
KINDS = ["canonical_city_reference","canonical_settlement_reference",
         "canonical_settlement_reference","crown_village_reference"]
CATS = ["city","small_compact_settlement","small_lakeside_visual_settlement","village"]
PROTECTED = NAMES + ["hallheim"]
UNKNOWNS = ["EDD-01","EDD-02","EDD-03","EDD-04",
            "EDD-05_LEGAL_RECORDS","EDD-07","EDD-08_DATED_ACTS"]
CAPS = ["gameplay","governance","routing","households","trade","quests",
        "npcSpawning","kin","worldStateEvents","godotScene"]
SOURCES = [
 ("E00","edranor_e00_manifest_v0.1.json","a5d003f183d8a2c2a754c39b5ee5c154f19a95c9"),
 ("E01","edranor_e01_relief_v0.1.json","7e22fa9d2e6214a8402bc9fa24140ada7332839d"),
 ("E02","edranor_e02_hydrology_v0.1.json","b0764d13a4c899d72db4dffdb3e49626a365a6aa"),
 ("E03","edranor_e03_climate_soils_ecosystems_v0.1.json","a715ee0d5b641e886f394e69e5081135397deaa9"),
 ("E04","edranor_e04_economy_viticulture_v0.1.json","a0ca6880375c5d4ac3d88a2c79d71ea406c7dab5"),
 ("E05","edranor_e05_roads_communications_v0.1.json","47bdf1fdf560029bc8328292c398b2ed5dd46a28"),
 ("E06","edranor_e06_settlement_rules_v0.1.json","401938170890e189a8d052e69ddf96055a7bd6f0"),
 ("E07","edranor_e07_canonical_nuclei_v0.1.json","1ee1d2bf6757443366702095707c913d50aa8de1"),
 ("E08","edranor_e08_population_services_v0.1.json","b8acd87045e0e75580691869d0bc0cb37b0ae6b9"),
 ("E09","edranor_e09_governance_v0.1.json","6ded136a9971a40c36fdf03e09b2fe50f81a4748"),
 ("E10","edranor_e10_lore_v0.1.json","6ad5a879a574cf7dea0f64868d37ae0200f082e9")
]
MANIFEST_SCHEMA = "https://robdor80.github.io/CoreRPG/schemas/content/0.1.0/content-pack-manifest.schema.json"
RESOURCE_SCHEMA = "https://robdor80.github.io/CoreRPG/schemas/content/0.1.0/resource-definition.schema.json"

class Rejected(ValueError): pass
def must(ok, message):
    if not ok: raise Rejected(message)
def no_duplicate_keys(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise Rejected("Duplicate JSON key "+k)
        d[k]=v
    return d
def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),object_pairs_hook=no_duplicate_keys)
def blob_hash(relative_path):
    return subprocess.run(["git","hash-object","--path="+relative_path,relative_path],
            cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()
def sources_check():
    src={phase:read(ROOT/OPER/name) for phase,name,_ in SOURCES}
    a,b,c,d,e,f,g=[src[x] for x in ("E00","E05","E06","E07","E08","E09","E10")]
    must(a["house"]["id"]=="casa_edranor" and a["house"]["seatId"]=="dorth","E00 house")
    must(a["protectedIds"]==PROTECTED and [x["id"] for x in a["locations"]]==PROTECTED,"E00 anchors")
    must([x["jurisdictionOwner"] for x in a["locations"][:4]]==OWNERS
         and a["locations"][4]["insideEdranorPerimeter"] is False,"E00 owners")
    must([x["id"] for x in b["anchors"]]==PROTECTED
         and all(x["roadAccess"]=="UNKNOWN" for x in b["anchors"]),"E05 roads UNKNOWN")
    must(b["rightsAndFiscality"]["edranorControlsRodas"] is False
         and b["rightsAndFiscality"]["noInternalHouseCustoms"] is True,"E05 sovereignty")
    must([x["id"] for x in c["protectedAnchors"]]==PROTECTED
         and all(x["procedural"] is False for x in c["protectedAnchors"]),"E06 protected")
    must([x["id"] for x in d["settlements"]]==NAMES,"E07 place IDs")
    must([x["type"] for x in d["settlements"]]==CATS
         and [x["jurisdictionOwner"] for x in d["settlements"]]==OWNERS,"E07 types and owners")
    for x in d["settlements"]:
        must(x["protected"] is True and x["procedural"] is False and
             x["instantiated"] is False and x["coordinates"] is None and
             x["population"] is None and x["physicalRoads"]==[] and
             x["npcInstances"]==[] and x["households"]==[],"E07 no actual instances")
    must([x["id"] for x in e["localityModels"]]==NAMES
         and [x["jurisdictionOwner"] for x in e["localityModels"]]==OWNERS,"E08 owners")
    for x in e["localityModels"]:
        must(x["population"] is None and x["householdCount"] is None
             and x["actualResidents"]==[] and x["actualProviders"]==[]
             and x["physicalRoads"]==[],"E08 not populated")
    must([x["id"] for x in f["localityModels"]]==NAMES,"E09 localities")
    for i,x in enumerate(f["localityModels"]):
        must(all(x[k]==OWNERS[i] for k in ("jurisdictionOwner","fiscalOwner",
              "justiceOwner","securityOwner")),"E09 institutional rights")
        must(x["courtCaseIds"]==[] and x["instantiatedOfficerIds"]==[]
             and x["issuedTaxObligationIds"]==[],"E09 no actual offices")
    must(g["protectedIds"]==PROTECTED
         and [x["id"] for x in g["territorialPlaces"]]==NAMES,"E10 localities")
    must(g["governance"]["druidicHouseIsTemple"] is False
         and g["governance"]["hallheimWithinEdranor"] is False
         and g["governance"]["rodasBerserkerCommander"]=="crown_aethros","E10 royal Rodas")
    for i,x in enumerate(g["territorialPlaces"]):
        must(all(x[k]==OWNERS[i] for k in ("authorityOwner","justiceOwner",
             "taxOwner","securityOwner")) and x["physicalRouteConfirmed"] is False
             and x["instantiatedNpcIds"]==[],"E10 no authority reassignment")
    must(len(g["characters"])==11 and len(g["conflicts"])==8 and len(g["scenes"])==8,
         "E10 design counts")
    must(all(x["npcId"] is None and x["legalKinRecordId"] is None
             and x["provenance"]=="PROPUESTA_E10" for x in g["characters"]),"E10 unratified")
    must(all(x["runtimeEnabled"] is False for x in g["conflicts"]+g["scenes"])
         and g["instantiatedQuestIds"]==[] and g["instantiatedNpcIds"]==[],
         "E10 not executable")

def check(p,m,d,t,check_real_sources=True):
    must(p["schemaVersion"]==1 and p["packId"]==PACK and
         p["projectionVersion"]=="0.1.0" and p["contentContract"]=="0.1.0","projection version")
    must(p["classification"]=="STRUCTURAL_CATALOG_NOT_GAMEPLAY" and
         p["runtimeEnabled"] is False and type(p["worldStateEntitiesCreated"]) is int and
         p["worldStateEntitiesCreated"]==0,"no materialized world")
    must(p["authorityLayers"]==["nimroel_core","norgard_defaults",
         "casa_edranor_or_crown_aethros","localidad","world_state"],"inheritance order")
    must(p["protectedIds"]==PROTECTED and p["territorialContextPlaceIds"]==NAMES
         and p["excludedPlaceIds"]==["hallheim"],"perimeter")
    must(p["unknowns"]==UNKNOWNS,"pending author decisions")
    must(list(p["executionCapabilities"])==CAPS and
         all(p["executionCapabilities"][x] is False for x in CAPS),"runtime capabilities fiction")
    must(p["unpromotedDesign"]=={"sourcePhase":"E10","provenance":"PROPUESTA_E10",
         "characters":11,"conflicts":8,"scenes":8,"legalKinRecords":0,
         "npcInstances":0,"questInstances":0,"worldStateEvents":0},"E10 promotion")
    must(p["governance"]=={"crown":"crown_aethros","singleLaw":True,
         "internalCustoms":False,"independentHouseArmy":False,"independentHouseMint":False,
         "rodasDruidicHouseIsTemple":False,"rodasMilitaryCommand":"crown_aethros",
         "hallheimInsideEdranor":False},"governance")
    must(len(p["sourceLocks"])==11,"source lock count")
    for i,(phase,name,sha) in enumerate(SOURCES):
        lock={"phase":phase,"path":OPER+name,"gitBlobSha":sha}
        must(p["sourceLocks"][i]==lock,"source lock "+phase)
        if check_real_sources: must(blob_hash(lock["path"])==sha,"source content changed "+phase)
    if check_real_sources: sources_check()
    ids=[PACK+":territory/edranor"]+[PACK+":places/"+n for n in NAMES]
    must(p["definitions"]==[{"id":ids[0],"kind":"territory_reference",
         "sourcePhase":"E00","sourcePointer":"/house/id"}]+[
         {"id":ids[i+1],"kind":KINDS[i],"sourcePhase":"E07",
          "sourcePointer":"/settlements/"+str(i)+"/id"} for i in range(4)],"stable ids/provenance")
    must(len(p["places"])==4,"four canonical places")
    for i,x in enumerate(p["places"]):
        must(x=={"id":NAMES[i],"definitionId":ids[i+1],"resourceKind":KINDS[i],
           "legalCategory":CATS[i],"geographicContextHouse":"casa_edranor",
           "jurisdictionOwner":OWNERS[i],"fiscalOwner":OWNERS[i],
           "justiceOwner":OWNERS[i],"securityOwner":OWNERS[i],
           "berserkerCommander":"crown_aethros" if i==3 else None,
           "protectedCanonicalAnchor":True,"proceduralSpawnAllowed":False,
           "physicalRouteConfirmed":False,"coordinates":None,"population":None,
           "instantiatedNpcIds":[],"activeQuestIds":[],"courtCaseIds":[]},"place "+NAMES[i])
    must(m["$schema"]==MANIFEST_SCHEMA and m["pack_id"]==PACK
         and m["pack_version"]=="0.1.0" and m["content_contract_version"]=="0.1.0"
         and m["minimum_core_version"]=="0.1.0" and m["dependencies"]==[],"manifest")
    must(len(d)==5 and m["resources"]==sorted(d),"resource list")
    for res in d.values():
        must(set(res)=={"$schema","id","kind","references"}
             and res["$schema"]==RESOURCE_SCHEMA,"unapproved Core content payload")
        for link in res["references"]:
            must(set(link)=={"target","expected_kind"},"typed link")
            target=next((v for v in d.values() if v["id"]==link["target"]),None)
            must(target is not None and target["kind"]==link["expected_kind"],"broken link/kind")
    territory=d["resources/territory/edranor.json"]
    must(territory["kind"]=="territory_reference" and territory["id"]==ids[0] and
         territory["references"]==[{"target":ids[i+1],"expected_kind":KINDS[i]}
                                   for i in range(4)],"territory refs")
    for i,n in enumerate(NAMES):
        resource=d["resources/places/"+n+".json"]
        must(resource["id"]==ids[i+1] and resource["kind"]==KINDS[i] and
             resource["references"]==[],"place resource "+n)
    must(t["schemaVersion"]==1 and t["version"]=="0.1.0"
         and t["phase"]=="E11" and t["status"]=="TEST_ONLY"
         and type(t["worldStateEvents"]) is int and t["worldStateEvents"]==0,"test fixtures")
    must([s["id"] for s in t["scenarios"]]==["T%02d"%x for x in range(1,13)],"test cases")
    must(all(s["classification"]=="TEST_ONLY" and
         s["executedInCoreRPG"] is False and s["implementedAsGameplay"] is False
         and s["goal"] for s in t["scenarios"]),"scenario is not world state")

def core_schema(root,m,d):
    schemas=[read(root/"schemas/content/0.1.0"/name) for name in (
        "types.schema.json","content-pack-manifest.schema.json","resource-definition.schema.json")]
    reg=Registry()
    for sch in schemas: reg=reg.with_resource(sch["$id"],Resource.from_contents(sch))
    Draft202012Validator(schemas[1],registry=reg).validate(m)
    for res in d.values(): Draft202012Validator(schemas[2],registry=reg).validate(res)

def adversarial(p,m,d,t):
    cases=[]
    def bad(index,label,fn):
        arr=copy.deepcopy([p,m,d,t]);fn(arr[index]);cases.append((label,arr))
    bad(0,"Rodas house authority",lambda x:x["places"][3].update(jurisdictionOwner="casa_edranor"))
    bad(0,"Rodas tax",lambda x:x["places"][3].update(fiscalOwner="casa_edranor"))
    bad(0,"Rodas justice",lambda x:x["places"][3].update(justiceOwner="casa_edranor"))
    bad(0,"Rodas berserkers",lambda x:x["places"][3].update(berserkerCommander="casa_edranor"))
    bad(0,"phantom road",lambda x:x["places"][1].update(physicalRouteConfirmed=True))
    bad(0,"procedural protected",lambda x:x["places"][0].update(proceduralSpawnAllowed=True))
    bad(0,"new NPC",lambda x:x["places"][2]["instantiatedNpcIds"].append("npc"))
    bad(0,"new quest",lambda x:x["places"][3]["activeQuestIds"].append("quest"))
    bad(0,"fictional census",lambda x:x["places"][0].update(population=1500))
    bad(0,"false coordinates",lambda x:x["places"][2].update(coordinates=[100,200]))
    bad(0,"Hallheim inclusion",lambda x:x["excludedPlaceIds"].clear())
    bad(0,"unprotect Rodas",lambda x:x["protectedIds"].remove("rodas"))
    bad(0,"customs",lambda x:x["governance"].update(internalCustoms=True))
    bad(0,"independent army",lambda x:x["governance"].update(independentHouseArmy=True))
    bad(0,"temple Rodas",lambda x:x["governance"].update(rodasDruidicHouseIsTemple=True))
    bad(0,"WorldState mutation",lambda x:x.update(worldStateEntitiesCreated=1))
    bad(0,"unratified NPC",lambda x:x["unpromotedDesign"].update(npcInstances=1))
    bad(0,"unratified conflict",lambda x:x["unpromotedDesign"].update(worldStateEvents=1))
    bad(0,"fictitious game",lambda x:x["executionCapabilities"].update(gameplay=True))
    bad(0,"source drift",lambda x:x["sourceLocks"][0].update(gitBlobSha="0"*40))
    bad(0,"source reassignment",lambda x:x["sourceLocks"][2].update(path="false.json"))
    bad(0,"inheritance reversal",lambda x:x["authorityLayers"].reverse())
    bad(0,"unstable DefinitionId",lambda x:x["definitions"][1].update(id=PACK+":places/altered"))
    bad(0,"unproven source",lambda x:x["definitions"][0].update(sourcePointer="/fiction"))
    bad(1,"unapproved dependency",lambda x:x["dependencies"].append({"pack_id":"nimroel.fake","version_requirement":{"minimum_inclusive":"0.1.0"}}))
    bad(1,"duplicate resource",lambda x:x["resources"].append(x["resources"][0]))
    bad(1,"pack impersonation",lambda x:x.update(pack_id="nimroel.fake"))
    bad(1,"wrong contract version",lambda x:x.update(content_contract_version="3.0.0"))
    bad(2,"illegal Core payload",lambda x:x["resources/places/dorth.json"].update(population=10))
    bad(2,"broken resource target",lambda x:x["resources/territory/edranor.json"]["references"][0].update(target=PACK+":places/other"))
    bad(2,"wrong target kind",lambda x:x["resources/territory/edranor.json"]["references"][3].update(expected_kind="canonical_city_reference"))
    bad(2,"Rodas made city",lambda x:x["resources/places/rodas.json"].update(kind="canonical_city_reference"))
    bad(3,"fixture events",lambda x:x.update(worldStateEvents=1))
    bad(3,"fictional executed in Core",lambda x:x["scenarios"][0].update(executedInCoreRPG=True))
    bad(3,"scene gameplay",lambda x:x["scenarios"][5].update(implementedAsGameplay=True))
    bad(3,"fake canonical scenario",lambda x:x["scenarios"][4].update(classification="CANON"))
    bad(3,"missing scenario",lambda x:x["scenarios"].pop())
    for label,arr in cases:
        try: check(*arr,check_real_sources=False)
        except (Rejected,KeyError,TypeError,IndexError,ValueError): pass
        else: raise Rejected("negative mutation accepted: "+label)
    return len(cases)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--core-root",type=Path)
    args=ap.parse_args()
    p=read(PACKDIR/"authoring/projection-v0.1.json")
    manifest=read(PACKDIR/"pack/manifest.json")
    definitions={path:read(PACKDIR/"pack"/path) for path in manifest["resources"]}
    fixtures=read(PACKDIR/"fixtures/e11-scenarios-v0.1.json")
    schema=read(PACKDIR/"schemas/projection.schema.json")
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(p)
    check(p,manifest,definitions,fixtures)
    if args.core_root:
        core_schema(args.core_root,manifest,definitions)
        print("EDRANOR E11: official CoreRPG 0.1.0 schemas PASS")
    else: print("EDRANOR E11: official Core schemas NOT EXECUTED (provide --core-root)")
    n=adversarial(p,manifest,definitions,fixtures)
    for path in ("E11_INDICE.md","Auditorias/E11_ACTA.md",
                 "Auditorias/E11_FUENTES_Y_DEUDA.md","00_Control_del_proyecto/TRASPASO_E12.md"):
        must((BASE/path).is_file(),"missing "+path)
    print("EDRANOR E11 STATIC PASS: 11 Git blob locks; 4 protected places; "
          "5 Core resources; 12 TEST_ONLY specifications; %d negatives rejected"%n)
    print("No Godot, gameplay or territorial simulations claimed.")

if __name__=="__main__": main()

#!/usr/bin/env python3
import copy
import json
from pathlib import Path
P=Path(__file__).resolve().parents[2]/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/E19-R0/source_manifest_v0.1.json"
def errors(d):
    e=[]
    if d.get("status")!="SOURCE_REVIEW_ONLY_MATERIAL_BLOCKED" or d.get("notRuntime") is not True: e.append("scope")
    for k in ("authorCropBytesVerified","generalMapHasHouseBorder","northBoundaryClosed","metricTransformValidated","mappedHydrology","physicalRoadGraphValidated","rejectedPR84Used"):
        if d.get(k) is not False:e.append(k)
    if d.get("worldStateEntitiesCreated")!=0:e.append("worldstate")
    if d.get("geometry")!=[] or d.get("roads")!=[] or d.get("properties")!=[]:e.append("geometry")
    if d.get("protectedPlaces",{}).get("rodas")!="crown_aethros" or d.get("protectedPlaces",{}).get("hallheim")!="outside_edranor":e.append("crown")
    if d.get("debt",{}).get("EDD_01")!="OPEN_VECTOR_TRACING_NORTH_NONJOIN_RESOLVED" or any(d.get("debt",{}).get(k)!="OPEN" for k in ("EDD_02","EDD_03","EDD_07")):e.append("debt")
    c=d.get("authorDirective20261114",{})
    if c.get("redLinesMeetInNorth") is not False or c.get("politicalNorthClosureRequired") is not False or c.get("technicalClipEquivalentToPoliticalBoundary") is not False:e.append("north union forbidden")
    if c.get("blueX")!="RODAS_CROWN_AETHROS" or c.get("authorConfirmed") is not True:e.append("author correction")
    if d.get("debt",{}).get("EDD_06")!="DESIGN_ONLY":e.append("Rodas")
    if d.get("forbiddenSource")!="E19_PR_84":e.append("rejected map")
    return e
def main():
    d=json.loads(P.read_text(encoding="utf-8"))
    assert not errors(d),errors(d)
    trials={"authorCropBytesVerified":True,"generalMapHasHouseBorder":True,"northBoundaryClosed":True,"metricTransformValidated":True,"mappedHydrology":True,"physicalRoadGraphValidated":True,"rejectedPR84Used":True,"worldStateEntitiesCreated":1,"geometry":[{"type":"Polygon"}],"roads":[{"a":"b"}],"properties":[{"id":"x"}]}
    for k,v in trials.items():
        altered=copy.deepcopy(d);altered[k]=v;assert errors(altered),k
    for k,v in (("rodas","casa_edranor"),("hallheim","casa_edranor")):
        altered=copy.deepcopy(d);altered["protectedPlaces"][k]=v;assert errors(altered),k
    altered=copy.deepcopy(d);altered["debt"]["EDD_01"]="CLOSED";assert errors(altered)
    for key in ("redLinesMeetInNorth","politicalNorthClosureRequired","technicalClipEquivalentToPoliticalBoundary"):
        altered=copy.deepcopy(d);altered["authorDirective20261114"][key]=True;assert errors(altered),key
    print("PASS E19-R0: 1 baseline + 14 negative tests; no fabricated cartography")
if __name__=="__main__":main()

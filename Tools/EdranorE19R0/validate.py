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
    if d.get("debt",{}).get("EDD_01")!="REGIONAL_BOUNDARY_RULES_RESOLVED_GEOGRAPHIC_DETAILS_IN_DEVELOPMENT" or (d.get("debt",{}).get("EDD_02")!="DEFERRED_TECHNICAL_GODOT_ONLY" or d.get("debt",{}).get("EDD_03")!="HYDROLOGIC_CAUSAL_MODEL_PENDING" or d.get("debt",{}).get("EDD_07")!="REGIONAL_ROAD_LOGIC_PENDING"):e.append("debt")
    c=d.get("authorDirective20261114",{})
    if c.get("redLinesMeetInNorth") is not False or c.get("politicalNorthClosureRequired") is not False or c.get("technicalClipEquivalentToPoliticalBoundary") is not False:e.append("north union forbidden")
    if c.get("blueX")!="RODAS_CROWN_AETHROS" or c.get("authorConfirmed") is not True:e.append("author correction")
    b=d.get("boundaryModel",{})
    if b.get("redSketchMode")!="APPROXIMATE_GUIDE_NOT_BORDER" or b.get("legalGeometryValidated") is not False or b.get("vertices")!=[]:e.append("no red trace")
    if b.get("west",{}).get("neighbor")!="casa_darovan" or b.get("west",{}).get("mountain")!="montes_valkram":e.append("Valkram west Darovan")
    if b.get("east",{}).get("neighbor")!="casa_galdren" or b.get("east",{}).get("mountain")!="montes_azurios":e.append("Azurios east Galdren")
    if (b.get("west",{}).get("westernSlopeOwner"),b.get("west",{}).get("easternSlopeOwner"))!=("casa_darovan","casa_edranor") or b.get("west",{}).get("ownershipResolvedByAuthor") is not True:e.append("Valkram slope ownership")
    if (b.get("east",{}).get("westernSlopeOwner"),b.get("east",{}).get("easternSlopeOwner"))!=("casa_edranor","casa_galdren") or b.get("east",{}).get("ownershipResolvedByAuthor") is not True:e.append("Azurios slope ownership")
    if d.get("authorDirective20261114",{}).get("slopeOwnershipRule")!="EACH_SLOPE_BELONGS_TO_HOUSE_ON_SAME_SIDE_OF_MOUNTAIN_DIVIDE":e.append("author slope rule")
    if b.get("south",{}).get("neighbor")!="casa_aethros" or b.get("south",{}).get("rule")!="CONVENTIONAL_EXCEPT_RIVER_SEGMENT" or b.get("south",{}).get("river")!="rio_lurien" or b.get("south",{}).get("riverSegment")!="UNKNOWN":e.append("Lurien segment not all south")
    if b.get("north",{}).get("redLinesMeet") is not False or b.get("north",{}).get("artificialClosureAllowed") is not False:e.append("no north join")
    if c.get("redLineTraceIsLegalGeometry") is not False or c.get("geometryMustFollowNaturalFeatures") is not True:e.append("geography first")
    g=d.get("geographicWorkflow",{})
    if g.get("precedent")!="CASA_VALRIK_GEOGRAFIA_LOCAL" or g.get("metricCoordinatesPrerequisiteForRegionalGeography") is not False or g.get("mapPixelsPrerequisiteForRegionalGeography") is not False or g.get("regionalNamedFeaturesCanBeDefinedWithoutCoordinates") is not True:
        e.append("Valrik geography method")
    if d.get("authorDirective20261114",{}).get("territorialMethod")!="VALRIK_CAUSAL_GEOGRAPHY_FIRST_NO_COORDINATE_PREREQUISITE":e.append("author method")
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
    negatives=[
      ("west wrong",lambda x:x["boundaryModel"]["west"].update(neighbor="casa_galdren")),
      ("west mountains wrong",lambda x:x["boundaryModel"]["west"].update(mountain="montes_azurios")),
      ("east wrong",lambda x:x["boundaryModel"]["east"].update(neighbor="casa_darovan")),
      ("east mountains wrong",lambda x:x["boundaryModel"]["east"].update(mountain="montes_valkram")),
      ("south all river",lambda x:x["boundaryModel"]["south"].update(rule="ALL_RIVER")),
      ("south wrong river",lambda x:x["boundaryModel"]["south"].update(river="unnamed")),
      ("south invented segment",lambda x:x["boundaryModel"]["south"].update(riverSegment="invented")),
      ("north joins",lambda x:x["boundaryModel"]["north"].update(redLinesMeet=True)),
      ("red legal",lambda x:x["authorDirective20261114"].update(redLineTraceIsLegalGeometry=True)),
      ("not geographic",lambda x:x["authorDirective20261114"].update(geometryMustFollowNaturalFeatures=False)),
      ("invented vertices",lambda x:x["boundaryModel"].update(vertices=[[1,2]]))
    ]
    for name,change in negatives:
        altered=copy.deepcopy(d);change(altered);assert errors(altered),name
    for side,field,bad in [("west","westernSlopeOwner","casa_edranor"),("west","easternSlopeOwner","casa_darovan"),("east","westernSlopeOwner","casa_galdren"),("east","easternSlopeOwner","casa_edranor")]:
        altered=copy.deepcopy(d);altered["boundaryModel"][side][field]=bad
        assert errors(altered),(side,field)
    for side in ("west","east"):
        altered=copy.deepcopy(d);altered["boundaryModel"][side]["ownershipResolvedByAuthor"]=False
        assert errors(altered),side
    for key in ("metricCoordinatesPrerequisiteForRegionalGeography","mapPixelsPrerequisiteForRegionalGeography"):
        altered=copy.deepcopy(d);altered["geographicWorkflow"][key]=True
        assert errors(altered),key
    print("PASS E19-R0: source/provenance guards + physical border & coordinate-free regional atlas guards")
if __name__=="__main__":main()

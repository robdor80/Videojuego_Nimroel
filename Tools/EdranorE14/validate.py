#!/usr/bin/env python3
"""E14: auditoría contractual y evaluación sintética. NO runtime."""
import copy
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
T=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
D=T/"Datos operativos"
SOURCES=["edranor_e01_relief_v0.1.json","edranor_e06_settlement_rules_v0.1.json","edranor_e07_canonical_nuclei_v0.1.json","edranor_e08_population_services_v0.1.json","edranor_e13_physical_design_v0.1.json"]
REQ={
"PERMANENT_RESIDENCE":["legalTenure","stableSlope","potableYearRoundWater","sanitation","yearRoundAccess","hazardClearance","dwellingCapacity","livelihoodCapacity","seasonalClimateVerified"],
"SEASONAL_WORKSTATION":["legalTenure","stableSlope","seasonalPotableWater","sanitation","seasonalAccess","hazardClearance","safeWorkShelter","seasonalClimateVerified"],
"AGRICULTURAL_USE":["legalTenure","stableSlope","productiveSoil","waterForUse","seasonalClimateVerified","hazardClearance","agriculturalRights"],
"FOREST_USE":["legalTenure","stableSlope","forestRights","protectionClearance","regenerationPlan","hazardClearance","accessAssessment"],
"TEMPORARY_PASSAGE":["passageRights","stableSlope","seasonalAccess","hazardClearance","routeSurvey"],
"EXCLUDED":[]}
USES=list(REQ)
OWNERS=["casa_edranor"]*3+["crown_aethros"]*2
ANCHORS=["dorth","lumina","karsath","rodas","hallheim"]
DOCS=["00_AUTORIDAD_Y_ALCANCE.md","01_ATLAS_DE_HABITABILIDAD.md","02_MODELO_CAUSAL_Y_USOS.md","03_ANCLAS_Y_DERECHOS.md","04_RIESGOS_Y_ESCENARIOS.md","05_CAPACIDAD_DEUDA_Y_TRASPASOS.md","06_AUDITORIA_Y_ACTA.md","07_TRASPASO_E15.md","README.md"]
BLOCKERS={"SLOPE_UNSTABLE","WATER_UNVERIFIED","ACCESS_UNVERIFIED","LAKE_SHORE_UNVERIFIED","FOREST_RIGHTS_MISSING","PROTECTED_HABITAT","CLIMATE_UNVERIFIED","CROWN_LAND"}
class Error(ValueError):pass
def ok(p,m):
    if not p:raise Error(m)
def unique_pairs(pairs):
    d={}
    for k,v in pairs:
        ok(k not in d,"duplicate JSON key "+k)
        d[k]=v
    return d
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"),object_pairs_hook=unique_pairs)
def vals(xs,k="id"):return [x[k] for x in xs]
def check(c,ss):
    e01,e06,e07,e08,e13=ss
    ok(c.get("schemaVersion")==1 and c.get("phase")=="E14"
       and c.get("documentId")=="edranor_e14_habitability"
       and c.get("status")=="DELEGATED_DESIGN_CONDITIONAL_NOT_CANON"
       and c.get("authority")=="ASSISTANT_DELEGATED_DESIGN"
       and c.get("runtimeEnabled") is False and c.get("syntheticOnly") is True
       and c.get("georeferenced") is False,"scope/authority")
    for key in ("worldStateEntitiesCreated","settlementsCreated","parcelsCertified","buildingsCreated","residentsCreated"):
        ok(c.get(key)==0,"instances "+key)
    ok(c.get("sourceContracts")==["edranor_e01_relief","edranor_e06_settlement_rules","edranor_e07_canonical_nuclei","edranor_e08_population_services","edranor_e13_physical_design"],"source chain")
    ok(c.get("inheritance")==["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"],"precedence")
    ok([s["phase"] for s in ss]==["E01","E06","E07","E08","E13"] and all(s.get("runtimeEnabled") is False for s in ss),"source phase/runtime")
    m=c["perimeter"]
    ok(m.get("northClosed") is False and m.get("metricGeometry") is False and m.get("crs") is None,"unverified geometry")
    for name in ("sitePolygons","coordinates","roads","rivers","realPermits"):ok(m.get(name)==[],"false layer "+name)
    ok(e13["map"]["northBoundaryClosed"] is False and e01["cartography"]["georeferenced"] is False,"E13/E01 map drift")
    ok(c.get("occupationTypes")==USES and c.get("requirements")==REQ,"proof matrix changed")
    pp=c["protectedAnchors"]
    ok(vals(pp)==ANCHORS and vals(pp,"owner")==OWNERS,"anchor owner")
    ok(vals(e07["settlements"])==ANCHORS[:4] and vals(e07["settlements"],"jurisdictionOwner")==OWNERS[:4],"E07 authority")
    ok(vals(e06["protectedAnchors"])==ANCHORS and vals(e08["localityModels"])==ANCHORS[:4],"E06/E08 anchors")
    ok(e07["settlements"][3]["berserkerCommandOwner"]=="crown_aethros" and e08["hardConstraints"]["rodasCrownFiscal"] is True,"Rodas legal")
    for i,p in enumerate(pp):
        ok(p.get("proceduralSpawnAllowed") is False and p.get("occupationCapacityVerified") is False
           and p.get("extraPopulationCreated")==0 and p.get("siteGeometry") is None
           and p.get("excludedFromEdranorClaim") is (i==4),"protected anchor materialized")
    ids=vals(e13["physicalUnits"],"unitId")
    units=c["units"]
    ok(len(units)==7 and vals(units)==ids==vals(e01["reliefUnits"])==vals(e06["zones"]),"7 E01/E06/E13 units")
    ok(vals(units,"studyId")==["U1","U2","U3","U4","U5","U6","U7"],"unit labels")
    scenario=[]
    for i,u in enumerate(units):
        ok(u.get("territorialGeometryVerified") is False and u.get("soilStatus")=="UNASSESSED"
           and u.get("waterStatus")=="UNKNOWN" and u.get("legalPlotOwnership")=="UNKNOWN"
           and u.get("approvedOccupationSites")==0 and len(u.get("focus",""))>20,"unit verified accidentally")
        p=u["archetypes"];n=u["counterexamples"]
        if i==6:
            ok(u.get("habitatAssessment")=="NON_EVALUABLE" and p==[] and n==[]
               and e13["physicalUnits"][6]["insideHouseTerritoryConfirmed"] is False,"unclosed north")
        else:
            ok(len(p)==4 and len(n)==3,"4 alternatives + 3 negative for each U1-U6")
            for j,a in enumerate(p):
                scenario.append(a["id"])
                ok(a.get("id")==f"ED14-U{i+1}-P{j+1}" and a.get("use") in USES[:5]
                   and a.get("requiredProofs")==REQ[a["use"]]
                   and a.get("status")=="STUDY_ONLY" and a.get("siteId") is None
                   and a.get("georeferenced") is False and a.get("instantiated") is False
                   and len(a.get("design",""))>30,"positive model became real")
            for j,a in enumerate(n):
                scenario.append(a["id"])
                ok(a.get("id")==f"ED14-U{i+1}-N{j+1}"
                   and a.get("blocker") in BLOCKERS and a.get("observed") is False
                   and a.get("siteId") is None and a.get("status")=="CONDITIONAL_NEGATIVE"
                   and len(a.get("causalReason",""))>20,"negative becomes actual event")
    ok(len(scenario)==len(set(scenario))==42,"42 scenarios unique")
    ok(vals(c["hazards"])==e13["hazardScenarioIds"] and len(c["hazards"])==10,"E13 hazards")
    for h in c["hazards"]:
        ok(all(h.get(x) is True for x in ("susceptibilityRequired","exposureRequired","vulnerabilityRequired"))
           and h.get("probability")=="UNKNOWN" and h.get("severity")=="UNKNOWN"
           and h.get("observedLocalIncident") is False and h.get("autoDisaster") is False,"hazard as fact")
    ok(c.get("debts")==e13["debts"] and vals(c["debts"])==[f"EDD-{i:02d}" for i in range(1,9)],"EDD list")
    ok([x["status"] for x in c["debts"]]==["OPEN"]*5+["RESOLVED_FOR_DESIGN"]+["OPEN"]*2,"EDD falsely resolved")
    ok(c.get("carryForwardTo")==["E15","E16","E19","E26","E28"],"handoff")
    lim=c["limits"]
    ok(set(lim)=={"populationTotal","areaHectares","densityPersonsPerKm2","agriculturalYields","carryingCapacity","realVacantHousing","forestHarvestQuota"} and all(v is None for v in lim.values()),"fictional population/area")
    for k in ("roadsCreatedFromEligibility","riversCreatedFromEligibility","forestsCutWithoutRights"):ok(c.get(k) is False,k)
    for k in ("noBorealViticultureAssumed","noRodasTaxOrMilitaryClaim","noRealCensus","noRuntimeClaims"):ok(c.get(k) is True,k)
    ok(vals(c["decisionRegister"])==[f"ED14-DEC-{i:02d}" for i in range(1,6)]
       and all(x["authority"]=="ASSISTANT_DELEGATED_DESIGN" for x in c["decisionRegister"]),"decisions")
    for name in DOCS:ok((T/"E14"/name).is_file() and (T/"E14"/name).stat().st_size>200,"missing "+name)
    ok((T/"E14_INDICE.md").is_file(),"index missing")
def evaluate(site,use,c):
    """Conservative pure evaluator: nothing is written to game or world state."""
    if use not in USES or use=="EXCLUDED":return "INELIGIBLE"
    if site.get("unitId") not in vals(c["units"]):return "OUTSIDE_SCOPE"
    if site["unitId"]==c["units"][6]["id"]:return "NON_EVALUABLE"
    if site.get("anchorId")=="hallheim" or site.get("insideScope") is False:return "OUTSIDE_SCOPE"
    if site.get("anchorId") in ANCHORS and site.get("proceduralSpawn"):return "INELIGIBLE"
    owner=site.get("jurisdictionOwner")
    if site.get("anchorId")=="rodas" and owner!="crown_aethros":return "INELIGIBLE"
    if owner not in ("casa_edranor","crown_aethros"):return "PENDING_EVIDENCE" if owner in (None,"UNKNOWN") else "INELIGIBLE"
    if site.get("crownLand") and owner!="crown_aethros":return "INELIGIBLE"
    if site.get("activeUnmitigatedHazard") or site.get("slopeUnstable") or site.get("borealAutoVineyard"):return "INELIGIBLE"
    if site.get("protectedHabitat"):
        if use in ("PERMANENT_RESIDENCE","AGRICULTURAL_USE"):return "INELIGIBLE"
        if use=="FOREST_USE" and not (site.get("forestRights") is True and site.get("protectionClearance") is True):return "INELIGIBLE"
    proofs=site.get("proofs")
    if not isinstance(proofs,dict):return "PENDING_EVIDENCE"
    need=c["requirements"][use]
    if any(proofs.get(p) is False for p in need):return "INELIGIBLE"
    if any(proofs.get(p) is not True for p in need):return "PENDING_EVIDENCE"
    if site.get("evidenceSource")=="SYNTHETIC_TEST":return "ELIGIBLE_IF_VERIFIED"
    if site.get("evidenceSource")=="VERIFIED_SITE_RECORD" and all(isinstance(site.get(k),str) and len(site[k])>6 for k in ("siteId","surveyId","rightsRecordId","authorityApprovalId","sourceHash")):return "ELIGIBLE_IF_VERIFIED"
    return "PENDING_EVIDENCE"
def site(c,use):
    return {"unitId":c["units"][3]["id"],"jurisdictionOwner":"casa_edranor","insideScope":True,
       "anchorId":None,"proceduralSpawn":False,"crownLand":False,"protectedHabitat":False,
       "activeUnmitigatedHazard":False,"slopeUnstable":False,"borealAutoVineyard":False,
       "evidenceSource":"SYNTHETIC_TEST","proofs":{k:True for k in REQ[use]}}
def lab(c):
    n=0
    for use in USES[:5]:
        s=site(c,use);ok(evaluate(s,use,c)=="ELIGIBLE_IF_VERIFIED","all proofs synthetic");n+=1
        for key in REQ[use]:
            for v,expected in ((False,"INELIGIBLE"),(None,"PENDING_EVIDENCE"),("UNKNOWN","PENDING_EVIDENCE")):
                q=copy.deepcopy(s);q["proofs"][key]=v
                ok(evaluate(q,use,c)==expected,f"wrong gate {use}:{key}={v}");n+=1
        for k in ("activeUnmitigatedHazard","slopeUnstable","borealAutoVineyard"):
            q=copy.deepcopy(s);q[k]=True;ok(evaluate(q,use,c)=="INELIGIBLE",k);n+=1
        for k in ("jurisdictionOwner","evidenceSource"):
            q=copy.deepcopy(s);q[k]=None;ok(evaluate(q,use,c)=="PENDING_EVIDENCE",k);n+=1
        for k,expected in (("hallheim","OUTSIDE_SCOPE"),("rodas","INELIGIBLE")):
            q=copy.deepcopy(s);q["anchorId"]=k;ok(evaluate(q,use,c)==expected,k);n+=1
        q=copy.deepcopy(s);q["anchorId"]="rodas";q["jurisdictionOwner"]="crown_aethros"
        ok(evaluate(q,use,c)=="ELIGIBLE_IF_VERIFIED","Rodas crown allowed in synthetic");n+=1
        q["proceduralSpawn"]=True;ok(evaluate(q,use,c)=="INELIGIBLE","Rodas procedural");n+=1
        q=copy.deepcopy(s);q["unitId"]=c["units"][6]["id"];ok(evaluate(q,use,c)=="NON_EVALUABLE","U7");n+=1
        q=copy.deepcopy(s);q["crownLand"]=True;ok(evaluate(q,use,c)=="INELIGIBLE","Crown rights");n+=1
        q=copy.deepcopy(s);q["evidenceSource"]="UNSUPPORTED";ok(evaluate(q,use,c)=="PENDING_EVIDENCE","unproven source");n+=1
        if use in ("PERMANENT_RESIDENCE","AGRICULTURAL_USE","FOREST_USE"):
            q=copy.deepcopy(s);q["protectedHabitat"]=True
            ok(evaluate(q,use,c)=="INELIGIBLE","protected without clearance");n+=1
        if use=="FOREST_USE":
            q["forestRights"]=True;q["protectionClearance"]=True
            ok(evaluate(q,use,c)=="ELIGIBLE_IF_VERIFIED","protected managed with both rights");n+=1
    return n
def mutation_tests(c,ss):
    targets=[
      (["runtimeEnabled"],True),(["worldStateEntitiesCreated"],1),(["settlementsCreated"],1),
      (["parcelsCertified"],1),(["buildingsCreated"],1),(["residentsCreated"],1),
      (["georeferenced"],True),(["syntheticOnly"],False),(["phase"],"E15"),
      (["authority"],"AUTHOR_EXPRESS"),(["status"],"CANON_REPO"),
      (["perimeter","northClosed"],True),(["perimeter","crs"],"EPSG:4326"),
      (["perimeter","roads"],["fake"]),(["perimeter","rivers"],["fake"]),
      (["perimeter","sitePolygons"],[[[0,0],[1,0],[1,1]]]),(["perimeter","realPermits"],["fake"]),
      (["protectedAnchors",3,"owner"],"casa_edranor"),(["protectedAnchors",4,"excludedFromEdranorClaim"],False),
      (["protectedAnchors",0,"proceduralSpawnAllowed"],True),(["protectedAnchors",1,"extraPopulationCreated"],1),
      (["protectedAnchors",2,"siteGeometry"],[1,2]),(["units",0,"soilStatus"],"APTO"),
      (["units",1,"legalPlotOwnership"],"PUBLIC"),(["units",2,"approvedOccupationSites"],1),
      (["units",3,"territorialGeometryVerified"],True),(["units",4,"waterStatus"],"VERIFIED"),
      (["units",5,"archetypes",0,"instantiated"],True),(["units",5,"archetypes",0,"status"],"BUILT"),
      (["units",2,"archetypes",1,"siteId"],"fake-site"),(["units",2,"archetypes",1,"requiredProofs"],[]),
      (["units",3,"archetypes",0,"georeferenced"],True),(["units",0,"counterexamples",0,"observed"],True),
      (["units",1,"counterexamples",0,"blocker"],"SAFE"),(["units",4,"counterexamples",1,"siteId"],"fake-road"),
      (["units",6,"habitatAssessment"],"HABITABLE"),(["units",6,"archetypes"],[c["units"][0]["archetypes"][0]]),
      (["hazards",0,"observedLocalIncident"],True),(["hazards",1,"probability"],0.75),
      (["hazards",2,"autoDisaster"],True),(["hazards",3,"exposureRequired"],False),
      (["debts",0,"status"],"RESOLVED"),(["debts",5,"status"],"OPEN"),
      (["limits","populationTotal"],4000),(["limits","areaHectares"],200),
      (["roadsCreatedFromEligibility"],True),(["riversCreatedFromEligibility"],True),
      (["forestsCutWithoutRights"],True),(["noBorealViticultureAssumed"],False),
      (["noRodasTaxOrMilitaryClaim"],False),(["noRealCensus"],False),(["noRuntimeClaims"],False),
      (["requirements","AGRICULTURAL_USE"],["productiveSoil"]),(["occupationTypes",0],"EXCLUDED"),
      (["carryForwardTo",0],"E20"),(["decisionRegister",0,"authority"],"AUTHOR_EXPRESS"),
      (["sourceContracts",4],"fiction"),
    ]
    for path,value in targets:
        v=copy.deepcopy(c);z=v
        for k in path[:-1]:z=z[k]
        z[path[-1]]=value
        try:check(v,ss)
        except Error:continue
        raise Error("mutation not rejected: "+str(path))
    return len(targets)
def main():
    ss=[read(D/x) for x in SOURCES];c=read(D/"edranor_e14_habitability_v0.1.json")
    check(c,ss);n=lab(c);m=mutation_tests(c,ss)
    print(f"E14 PASS | U1-U6 24 designs / 18 negative | U7 NON_EVALUABLE | 5 anchors | 10 hazards | {n} proof cases | {m} mutations rejected")
if __name__=="__main__":
    try:main()
    except (Error,ValueError,TypeError,KeyError,IndexError,FileNotFoundError) as ex:
        print("E14 FAIL: "+str(ex),file=sys.stderr);sys.exit(1)

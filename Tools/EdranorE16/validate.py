#!/usr/bin/env python3
"""E16 Edranor: audit contract and synthetic negative tests, no runtime."""
from __future__ import annotations
import copy, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
T=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
D=T/"Datos operativos"
FILES=[
"edranor_e05_roads_communications_v0.1.json",
"edranor_e07_canonical_nuclei_v0.1.json",
"edranor_e08_population_services_v0.1.json",
"edranor_e13_physical_design_v0.1.json",
"edranor_e14_habitability_v0.1.json",
"edranor_e15_living_economy_v0.1.json"]
SRC=[x.removesuffix("_v0.1.json") for x in FILES]
NAMES=["dorth","lumina","karsath","rodas","hallheim"]
OWNERS=["casa_edranor"]*3+["crown_aethros"]*2
UNITS=["edr_e01_west_valkram_interface","edr_e01_karsath_central_west","edr_e01_lumina_bosque_alto",
"edr_e01_central_wine_context","edr_e01_dorth_azurios_west","edr_e01_north_cold_transition","edr_e01_far_north_unclosed"]
QUESTIONS=["edr_e05_question_dorth_lumina","edr_e05_question_lumina_karsath","edr_e05_question_dorth_karsath","edr_e05_question_dorth_rodas"]
LOADS=["WINE_GRAPE","COOPERAGE_WOOD","FOOD_GRAIN_FLOUR","FOOD_PERISHABLE","FUEL","TOOLS_REPAIRS","PEOPLE","MESSAGES"]
SERVICES=["DRINKING_WATER","SANITATION","FOOD","FUEL_HEAT","SHELTER","CARE","BAKING","MILLING","BLACKSMITH_REPAIR","LODGING","MARKET_ANNUAL","WINERY_COOPERAGE","COURIER_TRANSPORT"]
STAGES=["HOUSEHOLD","NEIGHBOR","SPECIALIST","NEARBY_VILLAGE","MARKET","LARGER_CENTER"]
CHANNELS=["FOOT_MESSENGER","MOUNTED_COURIER","MERCHANT_DISPATCH","LOCAL_NOTICE","EMERGENCY_SIGNAL"]
ASSETS=["ROAD_SEGMENT","BRIDGE_OR_FORD","WATER_SYSTEM","SANITATION","PUBLIC_SERVICE_SPACE","BUILDING_FURNACE","WAREHOUSE","MESSAGE_CHANNEL"]
TF=["originId","destinationId","loadRef","owner","rights","routeSurvey","carrier","capacity","seasonWindow","receiverAck"]
CF=["messageId","sender","recipient","readAuthority","deliveryChannel","agent","realRouteOrLocalContact","eventEvidence","receiverAck"]
SF=["need","authority","provider","realLocation","availability","supply","access","safeOperation","recipient"]
MF=["assetId","realGeometry","title","operator","defectEvidence","hazardReview","workRights","partsAndLabor","funding","inspectionAck"]
REQUIRED={
"requiredTransportProof":["rights","loadRef","routeSurvey","carrier","capacity","seasonWindow","receiverAck"],
"requiredMessageProof":["sender","recipient","readAuthority","deliveryChannel","agent","realRouteOrLocalContact","receiverAck"],
"requiredServiceProof":["authority","provider","realLocation","availability","supply","access","safeOperation"],
"requiredMaintenanceProof":["assetId","realGeometry","title","operator","defectEvidence","workRights","partsAndLabor","inspectionAck"]}
GROUPS={"MOBILITY":("T",10),"COMMUNICATION":("C",6),"SERVICE":("S",8),"MAINTENANCE":("M",6)}
DOCS=["00_BASE_AUTORIDAD.md","01_GRAFO_NECESIDADES_Y_ACCESIBILIDAD.md","02_TRANSPORTE_LOGISTICA_Y_RECEPCION.md",
"03_MENSAJERIA_AVISOS_Y_CONOCIMIENTO.md","04_SERVICIOS_Y_ESCALADO_COMUNITARIO.md",
"05_MANTENIMIENTO_AVERIAS_Y_RECUPERACION.md","06_ATLAS_DE_LOCALIDADES_Y_UNIDADES.md",
"07_LABORATORIO_CAUSAL_Y_CONTRAEJEMPLOS.md","08_AUDITORIA_DECISIONES_TRASPASO_E17.md","README.md"]
class AuditError(ValueError): pass
def guard(ok,msg):
    if not ok: raise AuditError(msg)
def strict_pairs(xs):
    out={}
    for k,v in xs:
        guard(k not in out,"duplicate JSON key "+k)
        out[k]=v
    return out
def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"),object_pairs_hook=strict_pairs)
def ids(xs,key="id"): return [x[key] for x in xs]
def check(c,ss):
    e05,e07,e08,e13,e14,e15=ss
    guard((c.get("schemaVersion"),c.get("documentId"),c.get("version"),c.get("phase"))==
          (1,"edranor_e16_services_mobility","0.1","E16"),"identity")
    guard(c["status"]=="DELEGATED_DESIGN_NOT_CANON" and c["authority"]=="ASSISTANT_DELEGATED_DESIGN","authority")
    for k,v in {"runtimeEnabled":False,"syntheticOnly":True,"georeferenced":False,
                "physicalGraphValidated":False,"noNextPhaseExecuted":True}.items():
        guard(c.get(k) is v,"no runtime "+k)
    guard(c["sourceContracts"]==SRC and ids(ss,"documentId")==SRC
          and [x["phase"] for x in ss]==["E05","E07","E08","E13","E14","E15"]
          and all(x["runtimeEnabled"] is False for x in ss),"source identity")
    guard(c["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"],"inheritance")
    created=c["created"]
    guard(set(created)=={"physicalRoads","bridges","fords","ports","carriers","postalStations","signalTowers","serviceBuildings","workOrders","deliveries","messagesSent","people","levies"}
          and all(type(v) is int and v==0 for v in created.values()),"created instances")
    metrics=c["unknownMetrics"]
    guard(set(metrics)=={"routeDistance","travelHours","freightTonnage","networkCapacity","serviceCoverage","repairBudget","workforce","forecastCalendar"}
          and all(v is None for v in metrics.values()),"invented metrics")
    guard(c["rights"]=={"rodasJurisdiction":"crown_aethros","rodasFiscalOwner":"crown_aethros",
          "rodasMilitaryOwner":"crown_aethros","hallheimInsideEdranor":False,"edranorTaxOnRodas":False,
          "internalCustoms":False,"automaticRoadToll":False,"forestCuttingWithoutPermit":False,
          "karsathUrbanHarborVerified":False,"borealWineTransportNetworkAssumed":False},"rights")
    guard(e05["scope"]["physicalEdges"]==[] and e05["scope"]["pathfindingEnabled"] is False
          and e05["scope"]["georeferenced"] is False
          and e07["settlements"][3]["type"]=="village"
          and e07["settlements"][3]["jurisdictionOwner"]=="crown_aethros"
          and e14["protectedAnchors"][3]["owner"]=="crown_aethros"
          and e13["map"]["northBoundaryClosed"] is False,"source authority")
    a=c["anchors"]
    guard(ids(a)==NAMES and ids(a,"owner")==OWNERS and ids(e15["profiles"])==NAMES
          and ids(e15["profiles"],"owner")==OWNERS,"anchors")
    guard(ids(a,"role")==["HOUSE_SEAT_RED_WINE","WHITE_WINE_ANNUAL_MARKET",
          "SELECT_SMALL_BATCH_INTERIOR_LAKES","CROWN_VILLAGE_CONTACT","EXTERNAL_CROWN_CAPITAL"],"local identities")
    for i,x in enumerate(a):
        guard(x["serviceInstancesConfirmed"]==0 and x["carriersConfirmed"]==0
            and x["physicalRoadAccess"]=="UNKNOWN"
            and x["jurisdictionForServices"]==("HOUSE_UNDER_CROWN" if i<3 else "CROWN_DIRECT" if i==3 else "OUT_OF_SCOPE"),"anchor service")
    u=c["units"]
    guard(ids(u,"unitId")==UNITS==ids(e13["physicalUnits"],"unitId")
          and ids(u,"unitId")==ids(e15["units"]),"unit ids")
    for i,x in enumerate(u):
        guard(x["assessment"]==("NON_EVALUABLE" if i==6 else "STUDY_ONLY")
              and x["geometryValidated"] is False and x["accessCertified"] is False
              and x["servicesInstalled"]==0 and x["maintenanceJobsCreated"]==0
              and x["territoryMembershipConfirmed"] is (False if i==6 else None),"unit overclaim")
    graph=c["graph"]; qs=graph["studyQuestions"]
    guard(ids(qs,"sourceE05")==QUESTIONS==ids(e05["candidateRoadQuestions"])
          and [(x["from"],x["to"]) for x in qs]==[(x["from"],x["to"]) for x in e05["candidateRoadQuestions"]],"E05 source grafo")
    guard(graph["physicalEdges"]==[] and graph["pathfindingEnabled"] is False
          and graph["routeSurveyState"]=="UNKNOWN"
          and graph["externalInterfaces"]==["edr_e05_external_edranor_rodas","edr_e05_external_edranor_realm"]
          and graph["passQuestion"]=="edr_e05_question_valkram","graph not physical")
    for x in qs:
        guard(x["status"]=="QUESTION_ONLY" and x["physicalEdgeCreated"] is False
            and x["routeSurvey"]=="UNKNOWN" and x["permissionVerified"] is False
            and all(x[k] is None for k in ("travelTime","capacity","geometry")),"fake route")
    t=c["transport"]
    guard(t["loadClasses"]==LOADS and t["requiredFields"]==TF
          and t["lifeCycle"]==["REQUEST","PROVE_RIGHTS","VERIFY_STOCK","VERIFY_ROUTE",
            "VERIFY_CARRIER_AND_CAPACITY","RESERVE","DISPATCH_IF_REAL_RUNTIME","RECEIVE_ACK","CLOSE_BOOKS"]
          and t["dispatchAllowedInE16"] is False and t["freightBalancesFromE15"] is True
          and t["invoiceIsNotDelivery"] is True and t["activeTransportModes"]==[]
          and t["transportModeOptions"]==["ON_FOOT","PACK_ANIMAL","WAGON_IF_AUTHORIZED","MOUNTED_COURIER","BOAT_IF_VERIFIED"],"transport")
    msg=c["communication"]
    guard(msg["candidateChannels"]==CHANNELS and msg["installedChannels"]==[]
          and msg["requiredFields"]==CF
          and all(msg[k] is True for k in ("knowledgeRequiresReceipt","emergencyRequiresObservedEvent",
              "crownRecipientForRodas","noMagicalRelayAssumed","confidentialityRequired")),"messages")
    s=c["services"]
    guard(ids(s["catalogue"])==SERVICES and all(x["status"]=="NEED_MODEL_ONLY" and x["installedProviders"]==0 for x in s["catalogue"])
          and s["escalation"]==STAGES and s["requiredFields"]==SF
          and all(s[k] is True for k in ("availabilityMustBeObserved","specialistNotGuaranteed","safetyBeforeAdmission"))
          and s["luminaMarketFrequency"]=="ANNUAL" and s["rodasServiceAuthority"]=="CROWN_DIRECT","service")
    m=c["maintenance"]
    guard(m["potentialAssetClasses"]==ASSETS and m["requiredFields"]==MF
          and m["lifeCycle"]==["REPORT","IDENTIFY_REAL_ASSET","VERIFY_OWNER_AND_RIGHTS",
            "ASSESS_RISK","ALLOCATE_REAL_RESOURCES","WORK_IF_AUTHORIZED","INSPECT","REOPEN_OR_RESTRICT"]
          and m["createdJobs"]==[] and all(m[k] is True for k in ("reopenRequiresInspection",
                "closureNeedsRealAssetAndEvent","forestOrWaterWorkNeedsPermit","noInstantRepair")),"maintenance")
    gp=c["gatePolicy"]
    guard(gp["unknownResult"]=="PENDING_EVIDENCE" and gp["falseResult"]=="BLOCKED"
          and gp["allTrueResult"]=="ELIGIBLE_SYNTHETIC_ONLY" and gp["runtimeDispatchBlocked"] is True
          and all(gp[k]==v for k,v in REQUIRED.items()),"gate policy")
    sc=c["scenarios"]
    guard(len(sc)==30 and len(set(ids(sc)))==30,"scenario count")
    for fam,(prefix,count) in GROUPS.items():
        subset=[x for x in sc if x["family"]==fam]
        guard(ids(subset)==[f"ED16-{prefix}{i:02d}" for i in range(1,count+1)],"case IDs")
        for case in subset:
            guard(isinstance(case["question"],str) and len(case["question"])>=19
                  and case["missingProof"] in set(sum(REQUIRED.values(),[])).union(
                       {"authority","portEvidence","calendar","territory"})
                  and case["expectedIfMissing"] in ("BLOCKED","PENDING_EVIDENCE")
                  and case["status"]=="HYPOTHETICAL_NOT_OCCURRED"
                  and case["occurred"] is False and case["worldStateMutation"] is False
                  and case["assetId"] is None and case["carrierId"] is None,"case became fact")
    guard([(x["id"],x["status"]) for x in c["debts"]]==
          [(x["id"],x["status"]) for x in e15["debts"]]
          and ids(c["debts"])==[f"EDD-{i:02d}" for i in range(1,9)],"EDD drift")
    guard(ids(c["decisionRegister"])==[f"ED16-DEC-{i:02d}" for i in range(1,9)]
          and all(x["authority"]=="ASSISTANT_DELEGATED_DESIGN" and x["canonRatified"] is False
                  for x in c["decisionRegister"]),"design approval")
    guard(c["carryForwardTo"]==["E17","E18","E19","E20-E24","E26","E28"],"handoff")
    for doc in DOCS:
        f=T/"E16"/doc
        guard(f.is_file() and f.stat().st_size>180,"missing E16 doc "+doc)
    guard((T/"E16_INDICE.md").is_file(),"missing index")
def gate(proofs,need):
    if any(proofs.get(k) is False for k in need): return "BLOCKED"
    if any(proofs.get(k) is not True for k in need): return "PENDING_EVIDENCE"
    return "ELIGIBLE_SYNTHETIC_ONLY"
def dispatch(proofs,need,runtime=False):
    g=gate(proofs,need)
    if g!="ELIGIBLE_SYNTHETIC_ONLY": return g
    return "BLOCKED_NO_RUNTIME" if not runtime else "RUNTIME_REQUIRES_EXTERNAL_WORLD_STATE"
def reopen(asset,repair,inspection,rights,runtime):
    return all(x is True for x in (asset,repair,inspection,rights,runtime))
def laboratory():
    n=0
    for key,need in REQUIRED.items():
        complete={k:True for k in need}
        guard(gate(complete,need)=="ELIGIBLE_SYNTHETIC_ONLY","all true")
        guard(dispatch(complete,need)=="BLOCKED_NO_RUNTIME","no runtime dispatch")
        n+=2
        for k in need:
            for val,answer in [(None,"PENDING_EVIDENCE"),("UNKNOWN","PENDING_EVIDENCE"),(False,"BLOCKED")]:
                d=dict(complete);d[k]=val
                guard(gate(d,need)==answer,"proof "+key+":"+k);n+=1
        d=dict(complete);d[need[0]]=False;d[need[1]]="UNKNOWN"
        guard(gate(d,need)=="BLOCKED","veto dominates pending");n+=1
    for vals,exp in [
        ((True,True,True,True,False),False),((False,True,True,True,True),False),
        ((True,True,False,True,True),False),((True,True,True,False,True),False),
        ((True,True,True,True,True),True)]:
        guard(reopen(*vals) is exp,"maintenance reopen");n+=1
    return n
def mutations(c,ss):
    changes=[
      (["runtimeEnabled"],True),(["syntheticOnly"],False),(["phase"],"E17"),
      (["status"],"CANON_REPO"),(["authority"],"AUTHOR_EXPRESS"),
      (["georeferenced"],True),(["physicalGraphValidated"],True),(["noNextPhaseExecuted"],False),
      (["created","physicalRoads"],1),(["created","postalStations"],1),
      (["created","serviceBuildings"],1),(["created","workOrders"],1),
      (["unknownMetrics","travelHours"],4),(["unknownMetrics","repairBudget"],50),
      (["rights","rodasJurisdiction"],"casa_edranor"),(["rights","edranorTaxOnRodas"],True),
      (["rights","internalCustoms"],True),(["rights","automaticRoadToll"],True),
      (["rights","forestCuttingWithoutPermit"],True),(["rights","karsathUrbanHarborVerified"],True),
      (["rights","hallheimInsideEdranor"],True),
      (["anchors",3,"owner"],"casa_edranor"),(["anchors",4,"jurisdictionForServices"],"HOUSE_UNDER_CROWN"),
      (["anchors",0,"serviceInstancesConfirmed"],1),(["units",6,"assessment"],"STUDY_ONLY"),
      (["units",0,"geometryValidated"],True),(["graph","pathfindingEnabled"],True),
      (["graph","studyQuestions",0,"physicalEdgeCreated"],True),
      (["graph","studyQuestions",2,"routeSurvey"],"CONFIRMED"),
      (["graph","studyQuestions",1,"travelTime"],5),(["graph","physicalEdges"],["invented"]),
      (["transport","dispatchAllowedInE16"],True),
      (["transport","activeTransportModes"],["WAGON_IF_AUTHORIZED"]),
      (["transport","invoiceIsNotDelivery"],False),
      (["communication","installedChannels"],["EMERGENCY_SIGNAL"]),
      (["communication","knowledgeRequiresReceipt"],False),
      (["communication","emergencyRequiresObservedEvent"],False),
      (["services","catalogue",0,"installedProviders"],1),(["services","luminaMarketFrequency"],"DAILY"),
      (["services","specialistNotGuaranteed"],False),
      (["services","rodasServiceAuthority"],"HOUSE_UNDER_CROWN"),
      (["maintenance","createdJobs"],["bridge_123"]),
      (["maintenance","reopenRequiresInspection"],False),
      (["maintenance","forestOrWaterWorkNeedsPermit"],False),
      (["gatePolicy","runtimeDispatchBlocked"],False),
      (["gatePolicy","allTrueResult"],"DISPATCH_OK"),
      (["scenarios",0,"occurred"],True),(["scenarios",1,"worldStateMutation"],True),
      (["scenarios",2,"carrierId"],"fiction"),(["scenarios",3,"status"],"HISTORICAL_FACT"),
      (["debts",6,"status"],"RESOLVED"),(["decisionRegister",0,"canonRatified"],True),
      (["carryForwardTo"],["E17"])]
    for keys,val in changes:
        obj=copy.deepcopy(c); ref=obj
        for k in keys[:-1]: ref=ref[k]
        ref[keys[-1]]=val
        try: check(obj,ss)
        except AuditError: continue
        raise AuditError("mutation accepted "+repr(keys))
    return len(changes)
def main():
    sources=[read(D/x) for x in FILES]
    c=read(D/"edranor_e16_services_mobility_v0.1.json")
    check(c,sources)
    n=laboratory();m=mutations(c,sources)
    print(f"E16 PASS | 5 anchors | 7 units | 4 E05 questions | 13 services | 30 synthetic scenarios | {n} checks | {m} mutations rejected | NO RUNTIME")
if __name__=="__main__":
    try: main()
    except (AuditError,ValueError,TypeError,KeyError,IndexError,FileNotFoundError) as e:
        print("E16 FAIL: "+str(e),file=sys.stderr)
        sys.exit(1)

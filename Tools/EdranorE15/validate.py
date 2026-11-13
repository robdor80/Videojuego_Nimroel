#!/usr/bin/env python3
"""E15 economy: contractual audit + synthetic material/rights tests. NO RUNTIME."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
T=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
D=T/"Datos operativos"
FILES=[
 "edranor_e04_economy_viticulture_v0.1.json",
 "edranor_e07_canonical_nuclei_v0.1.json",
 "edranor_e08_population_services_v0.1.json",
 "edranor_e13_physical_design_v0.1.json",
 "edranor_e14_habitability_v0.1.json",
]
SRC=["edranor_e04_economy_viticulture","edranor_e07_canonical_nuclei","edranor_e08_population_services","edranor_e13_physical_design","edranor_e14_habitability"]
NAMES=["dorth","lumina","karsath","rodas","hallheim"]
OWNERS=["casa_edranor"]*3+["crown_aethros"]*2
STYLES=["RED_TINTO","WHITE_BLANCO","SELECT_SMALL_BATCH","NOT_ASSIGNED","OUTSIDE_SCOPE"]
U=[
 "edr_e01_west_valkram_interface","edr_e01_karsath_central_west",
 "edr_e01_lumina_bosque_alto","edr_e01_central_wine_context",
 "edr_e01_dorth_azurios_west","edr_e01_north_cold_transition",
 "edr_e01_far_north_unclosed",
]
STAGES={
 "wine":["PARCEL_RIGHTS","CULTIVATION","VINTAGE_MATURITY","HARVEST","RECEPTION","PROCESSING","STORAGE","SALE_DELIVERY"],
 "wood":["FOREST_TITLE","HARVEST_PERMIT","CUTTING","SEASONING","STAVES","HOOPS_ASSEMBLY_TEST","DELIVERY_REPAIR"],
 "food":["AGRICULTURAL_RIGHTS","SOW_CARE","HARVEST","DRY_STORE","MILL_IF_VERIFIED","COOK_OR_PRESERVE"],
 "household":["HOUSEHOLD_NEEDS","JOB_CONTRACT","SCHEDULE_AND_CARE","LEGAL_SUPPLIES","CONSUME_AND_RECORD"],
 "trade":["STOCK_PROVENANCE","OWNER_OFFER","CONTRACT","ROUTE_AND_CARRIER","RECEIPT","PAYMENT_AND_LEGAL_TAX"],
}
NEEDS={"wine":["rights","climate","labor","provenance","water","container","stock","delivery"],"wood":["forestPermit","regeneration","jurisdiction","conditioning","components","container"],"food":["rights","water","provider","fuel","stock"],"household":["schedule","minorSafety","lodging","potableWater","delivery"],"trade":["routeSurvey","jurisdiction","portEvidence","internalCustoms"]}
GROUPS={"WINE":8,"WOOD":6,"FOOD":5,"HOUSEHOLD":5,"TRADE":4}
GROUP_PREFIX={"WINE":"W","WOOD":"M","FOOD":"F","HOUSEHOLD":"H","TRADE":"T"}
RESULTS={"PENDING_EVIDENCE","BLOCKED","HOLD","INSUFFICIENT_STOCK"}
DOCS=[
 "00_BASE_Y_AUTORIDAD.md","01_UVA_Y_VINOS.md","02_TONELERIA_Y_BOSQUES.md",
 "03_CULTIVOS_Y_ALIMENTACION.md","04_HOGARES_Y_OFICIOS.md",
 "05_ALMACENES_BALANCES_Y_MERCADOS.md","06_ATLAS_ECONOMICO_POR_LOCALIDAD.md",
 "07_ESCENARIOS_Y_PRUEBAS_CAUSALES.md",
 "08_AUDITORIA_DECISIONES_Y_TRASPASO_E16.md","README.md",
]
class AuditError(ValueError): pass
def guard(cond,msg):
    if not cond: raise AuditError(msg)
def strict_pairs(ps):
    d={}
    for k,v in ps:
        guard(k not in d,"duplicate JSON key: "+k)
        d[k]=v
    return d
def read(p):
    return json.loads(p.read_text(encoding="utf-8-sig"),object_pairs_hook=strict_pairs)
def ids(xs,key="id"):
    return [x[key] for x in xs]
def check(c,ss):
    e04,e07,e08,e13,e14=ss
    guard(c.get("schemaVersion")==1 and c.get("documentId")=="edranor_e15_living_economy"
          and c.get("phase")=="E15" and c.get("version")=="0.1"
          and c.get("status")=="DELEGATED_DESIGN_NOT_CANON"
          and c.get("authority")=="ASSISTANT_DELEGATED_DESIGN","scope authority")
    for k,v in {"runtimeEnabled":False,"syntheticOnly":True,"georeferenced":False,"noNextPhaseExecuted":True}.items():
        guard(c.get(k) is v,"non runtime / later phase "+k)
    guard(c.get("sourceContracts")==SRC and ids(ss,"documentId")==SRC
          and [x["phase"] for x in ss]==["E04","E07","E08","E13","E14"]
          and all(x["runtimeEnabled"] is False for x in ss),"source contracts")
    guard(c.get("inheritance")==["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"],"hierarchy")
    expected_instances={"parcels","producers","wineries","cooperages","grainMills","stores","households","npcs","routes","batches","containers","taxes"}
    guard(set(c.get("instancesCreated",{}))==expected_instances and
          all(type(x) is int and x==0 for x in c["instancesCreated"].values()),"instances are real")
    keys={"vineyardHectares","grapeTonnes","redWineLitres","whiteWineLitres","selectWineLitres","forestHarvestQuota","barrelCapacity","localPopulation","annualTradeVolume","unitPricesClavos","calendarHarvestMonth","validRoutes"}
    guard(set(c.get("limits",{}))==keys and all(v is None for v in c["limits"].values()),"fake amounts")
    rights=c["rights"]
    guard(rights=={"rodasTaxOwner":"crown_aethros","rodasCommandOwner":"crown_aethros",
          "forestHarvestRequiresPermit":True,"realForestPermitsIssued":0,"internalCustomsAllowed":False,
          "borealViticultureAssumed":False,"karsathUrbanShoreVerified":False,
          "hallheimInsideEdranor":False},"forest/crown/hydro rights")
    guard(e07["settlements"][3]["jurisdictionOwner"]=="crown_aethros"
          and e07["settlements"][3]["type"]=="village"
          and e14["protectedAnchors"][3]["owner"]=="crown_aethros"
          and e14["protectedAnchors"][4]["excludedFromEdranorClaim"] is True
          and e13["map"]["northBoundaryClosed"] is False,"source authority drift")
    p=c["profiles"]
    guard(len(p)==5 and ids(p)==NAMES and ids(p,"owner")==OWNERS
          and ids(e07["settlements"])==NAMES[:4]
          and ids(e07["settlements"],"jurisdictionOwner")==OWNERS[:4]
          and ids(p,"wineStyle")==STYLES,"profiles")
    for i,x in enumerate(p):
        guard(x["marketAnnual"] is (i==1)
             and x["operationalStockConfirmed"] is False
             and x["newInfrastructureConfirmed"] is False and x["realBuildingsCreated"]==0
             and x["economicAuthority"]==("CROWN_AETHROS" if i==3 else "OUTSIDE_SCOPE" if i==4 else "CASA_EDRANOR_SUBORDINATE_CROWN"),"profile false claim")
    un=c["units"]
    guard(len(un)==7 and ids(un)==U==ids(e13["physicalUnits"],"unitId")
          and ids(un)==ids(e14["units"]), "units source misaligned")
    for i,x in enumerate(un):
        guard(x["assessment"]==("NON_EVALUABLE" if i==6 else "STUDY_ONLY")
              and x["insideHouseTerritoryConfirmed"] is (False if i==6 else None)
              and x["georeferenced"] is False and x["certifiedAgriculturalPlots"]==0
              and x["certifiedForestPlots"]==0 and x["productiveSoilVerified"] is False
              and x["waterSourceVerified"] is False and x["routeVerified"] is False,"unit overclaim")
    guard(c["chainStages"]==STAGES and c["chainPrerequisites"]==NEEDS,"supply chain stages")
    lp=c["lotPolicy"]
    guard(set(lp)=={"parentBatchRequired","ownerRequired","custodianRequired","quantityUnitRequired",
          "capacityMustBeVerified","lossMustBeRecorded","spendAvailableNotOnHand",
          "noNegativeStock","conversionFactorUnknown","recipeRequiredForDifferentUnits",
          "invoiceDoesNotCreateStock","containerIdPersistentAcrossRepairs"}
          and all(v is True for v in lp.values()),"lot/material rules")
    cp=c["commercialPolicy"]
    guard(cp=={"currency":"CLAVO","clavosPerLuna":24,"clavosPerCorona":480,
         "priceSchedule":None,"taxRates":None,"internalCustoms":False,
         "luminaAnnualMarketOnly":True,"rodasEdranorFiscalClaim":False,
         "deliveryRequiresSurveyedRoute":True,"contractsDoNotTeleportGoods":True},"money/customs")
    pp=c["peoplePolicy"]
    guard(pp=={"ageOfMajority":18,"children0to7EmploymentAllowed":False,
          "children8to11FullEmploymentAllowed":False,
          "children12to14UnsupervisedApprenticeshipAllowed":False,
          "minor15to17UnrestrictedDangerousWorkAllowed":False,
          "doubleBookedWorkersAllowed":False,"censusCreated":False},"people/care")
    guard(c["seasonalWindows"]==["DORMANCY_OR_PREP","GROWTH_AND_CARE",
          "MATURITY_AND_HARVEST_IF_VERIFIED","PROCESSING_AND_CLEANING",
          "STORAGE_AND_DISPATCH"] and c["calendarMonthsAssigned"]==[],"harvest not calendared")
    sc=c["scenarios"]
    guard(len(sc)==28 and len(set(ids(sc)))==28,"scenario count/unique")
    for family,count in GROUPS.items():
        group=[x for x in sc if x.get("family")==family]
        guard(len(group)==count,"scenario family "+family)
        guard(ids(group)==[f"ED15-{GROUP_PREFIX[family]}{i:02d}" for i in range(1,count+1)],"id stable")
        for case in group:
            guard(isinstance(case["question"],str) and len(case["question"])>14
                and case["missingProof"] in set(sum(NEEDS.values(),[]))
                and case["expectedIfMissing"] in RESULTS
                and case["status"]=="HYPOTHETICAL_NOT_OCCURRED"
                and case["observed"] is False and case["worldStateMutation"] is False
                and case["siteId"] is None and case["producerId"] is None,"case became fact")
    guard(c["debts"]==e14["debts"] and ids(c["debts"])==[f"EDD-{i:02d}" for i in range(1,9)],"EDD drift")
    guard(ids(c["decisionRegister"])==[f"ED15-DEC-{i:02d}" for i in range(1,8)]
          and all(x["authority"]=="ASSISTANT_DELEGATED_DESIGN" and x["canonRatified"] is False for x in c["decisionRegister"]),"delegation promoted")
    guard(c["carryForwardTo"]==["E16","E17","E19","E20-E24","E26","E28"],"handoff")
    for name in DOCS:
        path=T/"E15"/name
        guard(path.is_file() and path.stat().st_size>180,"missing doc "+name)
    guard((T/"E15_INDICE.md").is_file(),"missing index")

def reserve(on_hand,reserved,requested):
    """No side effects; fixed integer test units, not crop-volume rules."""
    if any(type(v) is not int or v<0 for v in (on_hand,reserved,requested)):
        return "INVALID_QUANTITY"
    if reserved>on_hand: return "INVALID_QUANTITY"
    if requested>on_hand-reserved: return "INSUFFICIENT_STOCK"
    return on_hand-reserved-requested

def balance(input_qty,useful,loss,remainder):
    if any(type(v) is not int or v<0 for v in (input_qty,useful,loss,remainder)):
        return False
    return input_qty==useful+loss+remainder

def gate(proofs,need):
    for key in need:
        if proofs.get(key) is False: return "BLOCKED"
    if any(proofs.get(key) is not True for key in need):return "PENDING_EVIDENCE"
    return "ELIGIBLE_SYNTHETIC_ONLY"

def laboratory(c):
    n=0
    for family,prerequisites in c["chainPrerequisites"].items():
        full={name:True for name in prerequisites}
        guard(gate(full,prerequisites)=="ELIGIBLE_SYNTHETIC_ONLY","all conditions synthetic");n+=1
        for key in prerequisites:
            for value,expected in ((None,"PENDING_EVIDENCE"),("UNKNOWN","PENDING_EVIDENCE"),(False,"BLOCKED")):
                q=dict(full);q[key]=value
                guard(gate(q,prerequisites)==expected,"gate "+family+key);n+=1
    for t,expected in [((12,2,6),4),((12,8,5),"INSUFFICIENT_STOCK"),
         ((4,5,1),"INVALID_QUANTITY"),((12,0,0),12),((-1,0,1),"INVALID_QUANTITY")]:
        guard(reserve(*t)==expected,"reserve");n+=1
    for t,expected in [((20,10,2,8),True),((20,20,2,1),False),
         ((20,0,0,20),True),((20,10,-1,11),False),((0,0,0,0),True)]:
        guard(balance(*t) is expected,"material conservation");n+=1
    return n

def mutations(c,ss):
    changes=[
      (["runtimeEnabled"],True),(["syntheticOnly"],False),(["georeferenced"],True),
      (["phase"],"E16"),(["status"],"CANON_REPO"),(["authority"],"AUTHOR_EXPRESS"),
      (["noNextPhaseExecuted"],False),(["instancesCreated","batches"],1),
      (["instancesCreated","taxes"],1),(["instancesCreated","wineries"],1),
      (["limits","grapeTonnes"],100),(["limits","unitPricesClavos"],80),
      (["rights","rodasTaxOwner"],"casa_edranor"),(["rights","forestHarvestRequiresPermit"],False),
      (["rights","realForestPermitsIssued"],1),(["rights","internalCustomsAllowed"],True),
      (["rights","borealViticultureAssumed"],True),(["rights","karsathUrbanShoreVerified"],True),
      (["rights","hallheimInsideEdranor"],True),
      (["profiles",3,"owner"],"casa_edranor"),(["profiles",1,"marketAnnual"],False),
      (["profiles",0,"operationalStockConfirmed"],True),(["profiles",2,"newInfrastructureConfirmed"],True),
      (["units",6,"assessment"],"STUDY_ONLY"),(["units",0,"georeferenced"],True),
      (["units",4,"certifiedAgriculturalPlots"],2),
      (["chainStages","wine"],["VINTAGE_MATURITY"]),
      (["chainPrerequisites","wood"],["components"]),(["lotPolicy","noNegativeStock"],False),
      (["lotPolicy","invoiceDoesNotCreateStock"],False),
      (["commercialPolicy","internalCustoms"],True),
      (["commercialPolicy","rodasEdranorFiscalClaim"],True),
      (["commercialPolicy","clavosPerLuna"],20),
      (["commercialPolicy","luminaAnnualMarketOnly"],False),
      (["peoplePolicy","children12to14UnsupervisedApprenticeshipAllowed"],True),
      (["peoplePolicy","doubleBookedWorkersAllowed"],True),
      (["calendarMonthsAssigned"],["october"]),
      (["scenarios",0,"observed"],True),
      (["scenarios",1,"worldStateMutation"],True),
      (["scenarios",2,"producerId"],"producer invented"),
      (["scenarios",3,"status"],"CANON"),
      (["debts",0,"status"],"RESOLVED"),
      (["decisionRegister",0,"canonRatified"],True),
      (["carryForwardTo"],["E17"]),
    ]
    for keys,value in changes:
        copy_c=copy.deepcopy(c)
        p=copy_c
        for key in keys[:-1]:p=p[key]
        p[keys[-1]]=value
        try:check(copy_c,ss)
        except AuditError:continue
        raise AuditError("mutation not rejected: "+repr(keys))
    return len(changes)

def main():
    ss=[read(D/x) for x in FILES]
    c=read(D/"edranor_e15_living_economy_v0.1.json")
    check(c,ss)
    n=laboratory(c)
    m=mutations(c,ss)
    print(f"E15 PASS | 5 process chains | 5 anchors | 7 units (U7 NON_EVALUABLE) | 28 hypothetical cases | {n} synthetic checks | {m} mutations rejected")
if __name__=="__main__":
    try:main()
    except (AuditError,ValueError,TypeError,KeyError,IndexError,FileNotFoundError) as ex:
        print("E15 FAIL: "+str(ex),file=sys.stderr)
        sys.exit(1)

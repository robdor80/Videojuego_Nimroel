#!/usr/bin/env python3
"""D.P23 Treihord: auditoría estática documental, no simulación ni runtime."""
import copy, json, re, subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DOC = BASE / "Profundizacion_2026/D.P23"
DATA = BASE / "Datos operativos/darovan_dp23_treihord_editorial_v0.1.json"
SPEC = {
    "neighborhoods": ("TRH-B",8,"01_ocho_barrios_y_ritmos_urbanos.md"),
    "futureEstablishments": ("TRH-L",12,"02_doce_lugares_y_oficios.md"),
    "biographyBases": ("TRH-N",10,"04_diez_vidas_y_relaciones.md"),
    "privateMemories": ("TRH-M",4,"05_memorias_y_arcos_condicionales.md"),
    "futureConditionalArcs": ("TRH-H",4,"05_memorias_y_arcos_condicionales.md"),
    "testOnlyScenes": ("TRH-E",8,"06_ocho_escenas_multirrol.md"),
    "decisions": ("TRH-DP23-",8,"08_resoluciones_editoriales.md")
}
NEIGHBORHOODS = ["El Recinto","Los Altos","El Peso","Las Lonjas","Los Oficios",
                 "La Calzada","La Ribera","La Costra"]
GATES = ["Puerta Alta","Puerta del Río","Puerta del Camino","Puerta Sur"]
SQUARES = ["Plaza Vieja","Plaza de las Balanzas","Plaza de las Lonjas","Plaza del Camino"]
PRIOR = "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/"
ORIGINAL = PRIOR + "Ciudades/Casa Darovan/Treihord.md"
ORIGINAL_SHA = "cfc1d664ac87e1f1521a79b6299cdf1a71b45de5"
BOOL_FALSE = ["mergeAuthorized","createsPhysicalMap","createsBuildings",
              "createsWorldStateEntities","coreRpgIntegrated","godotIntegrated"]
CANON = {
    "originalPath":ORIGINAL,"originalBlobSha":ORIGINAL_SHA,"originalLines":2374,
    "populationApprox":32000,"territorialHouse":"Darovan","capital":True,
    "river":"Belara","riverCrossesCity":False,"riverIndustrialShallowBarges":True,
    "oreFrom":"Valkram","coalFrom":"Azurios","hasMint":False,
    "kingdomMint":"Hallheim","crownAuditsHouseProduction":True,
    "crownOperatesHouseProduction":False,"laVenaPublicAccess":False,
    "secondContinuousWall":False,"royalJusticeAppliesInLaCostra":True,
    "neighborhoodCount":8,"mainSquares":SQUARES,"mainGates":GATES}
APPROVAL={"source":"USER_D.P23_2026_11_12_AUTONOMOUS_DECISIONS_AS_THEIRS",
          "scope":"EDITORIAL_ONLY","creativeApprovedByDelegation":True,
          "explicitMergeAuthorization":False}

def req(ok, msg):
    if not ok: raise AssertionError(msg)

def invariant(d, check_files=False):
    req([d[k] for k in ("schemaVersion","documentId","version","phase","date","cityId")] ==
        [1,"darovan_dp23_treihord_editorial_v0.1","0.1.0","D.P23","2026-11-12","treihord"],
        "version/scope")
    req(d["status"]=="EDITORIAL_APPROVED_BY_EXPLICIT_DELEGATION_CI_REQUIRED","status")
    req(d["approval"]==APPROVAL and d["addsEditorialCanon"] is True,"approval")
    req(all(d[k] is False for k in BOOL_FALSE),"unauthorized runtime/merge")
    req(d["predecessor"]=={"phase":"D.P22","pr":45,"merged":True,
        "mainBaseSha":"512434957f248f2513761615a9685ddd6c49c65f"},"predecessor")
    req(d["canon"]==CANON,"Treihord canon")
    req(len(d["lockedUnknowns"])>=30 and
        all(v is None for v in d["lockedUnknowns"].values()),"UNKNOWN invented")
    ids={}
    for key,(prefix,count,source) in SPEC.items():
        rows=d[key]
        req(len(rows)==count,"count "+key)
        expected=[prefix+f"{i:02d}" for i in range(1,count+1)]
        req([x["id"] for x in rows]==expected,"IDs "+key)
        ids[key]=set(expected)
    req([x["name"] for x in d["neighborhoods"]]==NEIGHBORHOODS,"eight barrios")
    for x in d["neighborhoods"]:
        req(x["status"]=="AUTHORED_EXISTING" and x["newDistrict"] is False
            and x["geometry"] is None,"new barrio/geometry")
    for x in d["futureEstablishments"]:
        req(x["neighborhoodRef"] in ids["neighborhoods"] and
            x["status"]=="AUTHORED_FUTURE_OBJECTIVE" and x["created"] is False and
            x["buildingId"] is None and x["ownerId"] is None and
            x["coordinates"] is None and x["inventoryIds"]==[] and
            x["capacity"] is None and bool(x["name"]),"invented place")
    for x in d["biographyBases"]:
        req(x["neighborhoodRef"] in ids["neighborhoods"] and
            x["status"]=="AUTHORED_BIOGRAPHY_BASE" and x["created"] is False and
            x["entityId"] is None and x["householdId"] is None and
            x["age"] is None and x["officialRank"] is None and
            x["activeRelations"]==[] and x["privilegedKnowledge"]==[],
            "invented NPC")
    for x in d["privateMemories"]:
        req(x["personRef"] in ids["biographyBases"] and
            x["status"]=="AUTHORED_PERSONAL_MEMORY" and
            x["publicHistoricalFact"] is False and x["eventId"] is None and
            x["eventDate"] is None,"public memory invented")
    for x in d["futureConditionalArcs"]:
        req(set(x["personRefs"])<=ids["biographyBases"] and
            x["status"]=="AUTHORED_FUTURE_CONDITIONAL_ARC" and
            x["implemented"] is False and x["triggered"] is False and
            x["eventId"] is None,"future arc activated")
    for x in d["testOnlyScenes"]:
        req(set(x["personRefs"])<=ids["biographyBases"] and
            x["status"]=="TEST_ONLY" and x["createsEvent"] is False and
            x["eventId"] is None,"TEST_ONLY promoted")
    scopes=["EIGHT_EXISTING_BARRIOS_ONLY","CULTURAL_CHARACTER_EDITORIAL",
            "TWELVE_FUTURE_PLACES","TEN_BIOGRAPHY_BASES","FOUR_PRIVATE_MEMORIES",
            "FOUR_FUTURE_ARCS_TEST_SCENES","CARTOGRAPHY_CONDITIONAL_METHOD",
            "EDITORIAL_CLOSURE_CI_REQUIRED_NO_MERGE"]
    for i,x in enumerate(d["decisions"]):
        req(x=={"id":f"TRH-DP23-{i+1:02d}","option":"A",
                "approved":"DELEGATED_AUTHORIAL_DECISION","scope":scopes[i]},
            "decision authority")
    req(d["sources"]==[ORIGINAL, BASE.relative_to(ROOT).as_posix()+
        "/Ciudades/Treihord/ANCLAS_CANONICAS_TREIHORD_v0.1.md",
        BASE.relative_to(ROOT).as_posix()+
        "/Profundizacion_2026/D.P16/ciudad_treihord_plan_funcional_condicionado.md"],
        "source list")
    if check_files:
        docs=["README.md","01_ocho_barrios_y_ritmos_urbanos.md",
              "02_doce_lugares_y_oficios.md","03_ocho_cadenas_materiales_y_servicios.md",
              "04_diez_vidas_y_relaciones.md","05_memorias_y_arcos_condicionales.md",
              "06_ocho_escenas_multirrol.md","07_cartografia_autoridad_y_traspaso.md",
              "08_resoluciones_editoriales.md"]
        for f in docs: req((DOC/f).is_file(),"missing "+f)
        for link in re.findall(r"\]\(([^)]+)\)",(DOC/"README.md").read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#"):
                req((DOC/unquote(link.split("#")[0])).resolve().is_file(),"broken link "+link)
        for key,(_,_,f) in SPEC.items():
            txt=(DOC/f).read_text(encoding="utf-8")
            for row in d[key]:
                req((row["name"] if key=="neighborhoods" else row["id"]) in txt,
                    "missing in prose: "+row["id"])
                if key!="decisions": req(row.get("name",row.get("title")) in txt,
                                        "name not in prose: "+row["id"])
        for src in d["sources"]: req((ROOT/src).is_file(),"missing source "+src)
        sha=subprocess.run(["git","rev-parse","HEAD:"+ORIGINAL],cwd=ROOT,
                           text=True,capture_output=True,check=True).stdout.strip()
        req(sha==ORIGINAL_SHA,"original Treihord.md modified")

def negatives(d):
    mutations=[]
    def add(path,value): mutations.append((path,value))
    for k,v in [("schemaVersion",2),("phase","D.P24"),("cityId","syvaris"),
        ("version","2.0"),("date","2026-09-01"),("status","WORLD_READY"),
        ("addsEditorialCanon",False),("mergeAuthorized",True),
        ("createsPhysicalMap",True),("createsBuildings",True),
        ("createsWorldStateEntities",True),("coreRpgIntegrated",True),
        ("godotIntegrated",True)]: add((k,),v)
    for k,v in [("scope","RUNTIME"),("creativeApprovedByDelegation",False),
                ("explicitMergeAuthorization",True)]: add(("approval",k),v)
    add(("predecessor","pr"),44)
    add(("predecessor","merged"),False)
    for k,v in [("river","Eshneva"),("riverCrossesCity",True),
        ("populationApprox",50000),("coalFrom","Valkram"),("oreFrom","Azurios"),
        ("hasMint",True),("kingdomMint","Treihord"),
        ("laVenaPublicAccess",True),("secondContinuousWall",True),
        ("royalJusticeAppliesInLaCostra",False),
        ("crownAuditsHouseProduction",False),("crownOperatesHouseProduction",True),
        ("neighborhoodCount",9),("originalBlobSha","0"*40)]:
        add(("canon",k),v)
    add(("canon","mainGates",0),"Puerta del Tesoro")
    add(("canon","mainSquares",0),"Plaza Nueva")
    for k,v in [("coalRoute","nueva ruta"),("namedCurrentDarovanHead","Un Lord"),
                ("streetGeometry",[0,0]),("exactPopulation",32119)]:
        add(("lockedUnknowns",k),v)
    for path,val in [
        (("neighborhoods",0,"name"),"Nuevo Barrio"),
        (("neighborhoods",1,"newDistrict"),True),
        (("neighborhoods",2,"geometry"),[1,2]),
        (("futureEstablishments",0,"created"),True),
        (("futureEstablishments",1,"buildingId"),"build1"),
        (("futureEstablishments",2,"inventoryIds"),["ore"]),
        (("futureEstablishments",3,"coordinates"),[2,3]),
        (("futureEstablishments",4,"capacity"),500),
        (("futureEstablishments",5,"neighborhoodRef"),"TRH-B09"),
        (("biographyBases",0,"created"),True),
        (("biographyBases",1,"entityId"),"npc"),
        (("biographyBases",2,"officialRank"),"Lord"),
        (("biographyBases",3,"privilegedKnowledge"),["SECRET"]),
        (("biographyBases",4,"householdId"),"house"),
        (("biographyBases",5,"activeRelations"),["married"]),
        (("privateMemories",0,"eventId"),"event"),
        (("privateMemories",1,"publicHistoricalFact"),True),
        (("privateMemories",2,"eventDate"),"15375"),
        (("privateMemories",3,"personRef"),"TRH-N99"),
        (("futureConditionalArcs",0,"implemented"),True),
        (("futureConditionalArcs",1,"triggered"),True),
        (("futureConditionalArcs",2,"personRefs",0),"TRH-N99"),
        (("testOnlyScenes",0,"createsEvent"),True),
        (("testOnlyScenes",1,"eventId"),"event"),
        (("testOnlyScenes",2,"status"),"ACTIVE"),
        (("decisions",0,"option"),"B"),
        (("decisions",7,"scope"),"MERGE_ALLOWED"),
        (("biographyBases",9,"id"),"TRH-N01"),
        (("futureEstablishments",11,"id"),"TRH-L01"),
        (("sources",0),"missing.md")]:
        add(path,val)
    for path,val in mutations:
        changed=copy.deepcopy(d)
        target=changed
        for key in path[:-1]: target=target[key]
        target[path[-1]]=val
        try: invariant(changed)
        except (AssertionError,KeyError,TypeError,IndexError): pass
        else: raise AssertionError("invalid mutation accepted: "+str(path))
    return len(mutations)

if __name__=="__main__":
    d=json.loads(DATA.read_text(encoding="utf-8"))
    invariant(d,check_files=True)
    n=negatives(d)
    print("D.P23 TREIHORD STATIC PASS: 8 barrios, 12 lugares futuros, "
          "10 biografías, 4 memorias, 4 arcos, 8 TEST_ONLY y 8 decisiones")
    print(f"{n} mutaciones negativas rechazadas; {len(d['lockedUnknowns'])} UNKNOWN bloqueados")
    print("Canon original verificado por SHA; ni edificios ni runtime.")

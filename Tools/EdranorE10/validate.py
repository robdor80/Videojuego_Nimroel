"""Edranor E10 static contract and adversarial validation. NOT an engine/runtime test."""
from __future__ import annotations
from copy import deepcopy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DATA = BASE / "Datos operativos"
def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

doc = load("edranor_e10_lore_v0.1.json")
lab = load("edranor_e10_adversarial_cases_v0.1.json")
e09 = load("edranor_e09_governance_v0.1.json")
e07 = load("edranor_e07_canonical_nuclei_v0.1.json")
paths = [
 "E10_INDICE.md","Historia/E10_ORIGEN_Y_CRONOLOGIA.md",
 "Historia/E10_RODAS_CRONOLOGIA_DIPLOMACIA.md",
 "Personajes/E10_CASA_FAMILIA_Y_SUCESION.md",
 "Personajes/E10_PERSONAJES_Y_RELACIONES.md",
 "Cultura/E10_COSTUMBRES_CIVILES_Y_OFICIOS.md",
 "Cultura/E10_RODAS_IDENTIDAD_Y_CUSTODIA.md",
 "Conflictos/E10_DILEMAS_Y_ARBITRAJE.md",
 "Conflictos/E10_SEMILLAS_NARRATIVAS.md",
 "Auditorias/E10_FUENTES_Y_DEUDA.md","Auditorias/E10_ACTA.md",
 "00_Control_del_proyecto/TRASPASO_E11.md",
]
OWNERS={"dorth":"casa_edranor","lumina":"casa_edranor","karsath":"casa_edranor","rodas":"crown_aethros"}
TYPES=["city","small_compact_settlement","small_lakeside_visual_settlement","village"]
def validate(d):
    assert d["schemaVersion"]==1 and type(d["schemaVersion"]) is int
    assert (d["phase"],d["date"],d["version"],d["documentId"],d["status"],d["runtimeEnabled"])==(
      "E10","2026-11-13","0.1","edranor_e10_lore","DOCUMENTAL_DESIGN_ONLY",False)
    assert d["sourceAuthorities"]==["CANON_REPO","VISUAL_APROBADO","AUTOR_2026_11_12","OBSERVACION_MAPA","PROPUESTA_E10","UNKNOWN"]
    assert d["inheritance"]==["nimroel_core","norgard_defaults","casa_edranor_or_crown_aethros","localidad","world_state"]
    assert d["protectedIds"]==["dorth","lumina","karsath","rodas","hallheim"]
    assert d["norgardCalendar"]=={"referenceYear":15375,"months":12,"daysPerYear":365}
    g=d["governance"]
    assert g["singleCrown"]=="crown_aethros" and g["singleLaw"] is True
    for k in ["internalCustoms","houseHasIndependentArmy","houseHasMint","druidicHouseIsTemple","hallheimWithinEdranor"]:
        assert g[k] is False,k
    assert g["rodasBerserkerCommander"]=="crown_aethros"
    p=d["territorialPlaces"]
    assert len(p)==4 and [x["id"] for x in p]==list(OWNERS)
    for i,x in enumerate(p):
        assert x["legalCategory"]==TYPES[i]
        assert x["protectedAnchor"] is True and x["physicalRouteConfirmed"] is False
        assert x["instantiatedNpcIds"]==[]
        for k in ["authorityOwner","justiceOwner","taxOwner","securityOwner"]:
            assert x[k]==OWNERS[x["id"]],(x["id"],k)
    dy=d["dynasty"]
    assert dy["status"]=="PROPUESTA_E10_NOT_LEGAL_KIN"
    assert dy["headDesignId"]=="edr_e10_char_elira"
    assert dy["presumptiveHeirDesignId"]=="edr_e10_char_maelis"
    assert dy["siblingsOrChildren"]==["edr_e10_char_maelis","edr_e10_char_caelen","edr_e10_char_vesra"]
    assert dy["legalSuccessionEstablished"] is False
    assert dy["houseInheritancePrinciple"]=="hereditary_with_crown_confirmation"
    assert dy["coronationOrElectionRequired"] is False
    ch=d["characters"]
    assert len(ch)==11 and len({c["designId"] for c in ch})==11
    assert [c["designId"] for c in ch]==["edr_e10_char_"+s for s in (
        "elira","maelis","caelen","vesra","orlan","ysna","tovan","lira","heran","saer","bren")]
    assert [c["type"] for c in ch]==["dynasty"]*4+["civilian"]*7
    for c in ch:
        assert c["provenance"]=="PROPUESTA_E10"
        assert c["placeId"] in OWNERS and c["authorityOwner"]==OWNERS[c["placeId"]]
        for k in ["npcId","appointedOfficeId","birthDate","legalKinRecordId"]: assert c[k] is None,(c["designId"],k)
        assert bool(c["name"]) and len(c["name"])>5
        if c["type"]!="dynasty":
            assert not c["name"].endswith((" Edranor"," Aethros"," Darovan"," Galdren"," Valrik"))
    assert all(any(c["designId"]==ref for c in ch) for ref in [dy["headDesignId"],dy["presumptiveHeirDesignId"]]+dy["siblingsOrChildren"])
    h=d["relativeHistory"]
    assert [x["id"] for x in h]==["edr_e10_hist_h0"+str(i) for i in range(1,6)]
    for x in h:
        assert x["relativeOnly"] is True and x["absoluteYear"] is None and x["evidence"]=="PROPUESTA_E10"
    cf=d["conflicts"]
    assert [x["id"] for x in cf]==["edr_e10_conflict_c0"+str(i) for i in range(1,9)]
    assert all(x["status"]=="SEED_NOT_TRIGGERED" and x["outcome"] is None and x["runtimeEnabled"] is False for x in cf)
    sc=d["scenes"]
    assert [x["id"] for x in sc]==["edr_e10_scene_s0"+str(i) for i in range(1,9)]
    for i,x in enumerate(sc):
        assert x["conflictId"]==cf[i]["id"] and x["status"]=="DESIGN_ONLY"
        assert x["runtimeEnabled"] is False and x["worldStateEventId"] is None
    cu=d["culturalPractices"]
    assert len(cu)==6 and len({x["id"] for x in cu})==6
    for c in cu:
        assert c["provenance"]=="PROPUESTA_E10" and c["mandatoryLaw"] is False and c["publicHolidayDate"] is None
    assert d["unknowns"]==["EDD-01","EDD-02","EDD-03","EDD-04","EDD-05_LEGAL_RECORDS","EDD-07","EDD-08_DATED_ACTS"]
    for k in ["instantiatedNpcIds","instantiatedQuestIds","issuedOrders","resolvedWars",
              "historicalTreatyIds","physicalRoadIds","newTaxIds","newCourtIds"]:
        assert d[k]==[],k

def set_mutation(d,path,value):
    bits=re.findall(r"[^.\[\]]+|\[\d+\]",path)
    ref=d
    for key in bits[:-1]:
        ref=ref[int(key[1:-1])] if key.startswith("[") else ref[key]
    k=bits[-1]
    if k.startswith("["):
        ref[int(k[1:-1])]=value
    else:
        ref[k]=value

validate(doc)
assert lab["schemaVersion"]==1 and lab["phase"]=="E10"
assert lab["runtimeEnabled"] is False and lab["fixturesAreCanonical"] is False
assert len(lab["cases"])==24
assert len({x["id"] for x in lab["cases"]})==len(lab["cases"])
for case in lab["cases"]:
    assert case["expected"]=="REJECT"
    changed=deepcopy(doc)
    set_mutation(changed,case["mutationPath"],case["mutationValue"])
    try:
        validate(changed)
    except (AssertionError,KeyError,TypeError,ValueError):
        pass
    else:
        raise AssertionError("Adversarial mutation survived: "+case["id"])
for p in paths:
    full=BASE/p
    assert full.is_file(),p
    t=full.read_text(encoding="utf-8")
    assert "E10" in t and len(t)>400,p
for must in ["Rodas","Corona","EDD-08"]:
    assert must in (BASE/"Historia/E10_RODAS_CRONOLOGIA_DIPLOMACIA.md").read_text(encoding="utf-8")
assert [x["id"] for x in e09["localityModels"]]==list(OWNERS)
for x in e09["localityModels"]:
    assert x["jurisdictionOwner"]==OWNERS[x["id"]]
assert len(e07["settlements"])==4
print("EDRANOR E10 PASS: 11 proposed characters; 8 conflicts/scenes; 24 negative mutations; E07/E09 compatibility; docs and canon guards. NO RUNTIME.")

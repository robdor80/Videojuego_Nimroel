#!/usr/bin/env python3
"""Syvaris D.P22: static documentary guardrails; not a CoreRPG runtime test."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = BASE / "Datos operativos/darovan_dp22_syvaris_proposals_v0.1.json"
DOC = BASE / "Profundizacion_2026/D.P22"
GROUPS = {
  "proposedUrbanAreas": ("SYV-U", 6, "01_syvaris_ciudad_de_abrigo_y_ambitos.md"),
  "proposedEstablishments": ("SYV-L", 12, "02_syvaris_lugares_y_trabajos.md"),
  "proposedPeople": ("SYV-N", 10, "04_syvaris_diez_biografias.md"),
  "proposedPrivateMemories": ("SYV-M", 4, "05_syvaris_memorias_y_conflictos.md"),
  "proposedConditionalArcs": ("SYV-H", 4, "05_syvaris_memorias_y_conflictos.md"),
  "testOnlyScenes": ("SYV-E", 6, "06_syvaris_escenas_y_decisiones.md"),
}
DOCS = ["README.md", "03_syvaris_vida_cotidiana_y_cadenas.md",
        "07_syvaris_cartografia_autoridad_y_traspaso.md",
        "08_syvaris_decisiones_editoriales.md"]

def req(ok, message):
    if not ok:
        raise AssertionError(message)

def invariant(d, check_files=False):
    req((d["schemaVersion"],d["documentId"],d["version"],d["phase"],d["cityId"]) ==
        (1,"darovan_dp22_syvaris_city_authorship_proposals_v0.1","0.1.0","D.P22","syvaris"),
        "wrong version/scope")
    req(d["status"] == "AUTHORSHIP_PROPOSAL_PR_DRAFT_NO_CANON_PROMOTION", "unapproved editorial closure")
    req(d["creativeDelegation"] ==
        "GENERAL_EDITORIAL_RECOMMENDATIONS_2026_11_11_NOT_INDIVIDUAL_CANON_RATIFICATION",
        "delegation does not equal individual author ratification")
    for key in ("authorRatifiedNewContent","addsCanon","createsWorldStateEntities","createsBuildings",
                "createsPhysicalMap","coreRpgIntegrated","godotIntegrated","mergeAuthorized"):
        req(d[key] is False, "unauthorized mutation: "+key)
    dep = d["dependency"]
    req(dep == {"predecessorPhase":"D.P21","predecessorPr":44,
                "predecessorBranch":"feat/darovan-dp21-taramin-ciudad-vivida-20261111",
                "predecessorMergedWhenStarted":False,"baseOfWork":"PREDECESSOR_BRANCH",
                "requiresPredecessorMergeBeforeMainMerge":True}, "stacked predecessor dependency")
    canon = d["canonClaims"]
    for k,v in {
        "kingdom":"Norgard","territorialHouse":"Darovan","cityOnIsland":True,
        "islandIndependentKingdom":False,"citySmallerThanTaramin":True,
        "totalIslandPopulation":None,"d07ConceptDecision":"DAR-D07-03_A",
        "urbanActivityConcentratedAroundProtectedBay":True,"protectedBayExists":True,
        "smallerCovesExist":True,"smallerCovesHaveAuthorizedPorts":False,
        "royalNavyPresenceAuthority":"CORONA_NORGARD","darovanPrivateNavyExists":False,
        "royalNavyGovernsAllCivilians":False,"automaticMainlandSeaRoute":False,
        "automaticNewWaterSource":False,"externalCustomsPortOfVeldoraTransferred":False,
        "islandClimate":"WARM_DRY_EXPOSED_CENTRE_NORTH_GREENER_SOUTH_SHELTERED",
        "woodlands":"LIGHT_DISPERSED_DISCONTINUOUS",
        "architecture":"LOWER_VOLUMES_STONE_WOOD_PALE_TONES_PARTIAL_WHITEWASH",
        "fishingCommerceOilsAndMarineProducts":True}.items():
        req(canon[k] == v, "canon anchor: "+k)
    req(canon["cityPopulationRange"] == {"minInclusive":7000,"maxInclusive":10000,"exact":None},
        "population is city-only")
    req(len(d["lockedUnknowns"]) >= 29 and all(v is None for v in d["lockedUnknowns"].values()),
        "invented UNKNOWN")
    ids = {}
    for key,(prefix,count,source) in GROUPS.items():
        rows = d[key]
        req(len(rows) == count, "count "+key)
        req([r["id"] for r in rows] == [f"{prefix}{i:02}" for i in range(1,count+1)],
            "duplicate/missing IDs "+key)
        ids[key] = {r["id"] for r in rows}
        for r in rows:
            req(r["status"] == ("TEST_ONLY" if key=="testOnlyScenes" else "PROPOSAL_PENDING_AUTHOR"),
                "promoted proposal: "+r["id"])
            req(bool(r.get("name",r.get("title"))), "unnamed "+r["id"])
    for r in d["proposedUrbanAreas"]:
        req(r["popularNameApproved"] is False and r["isOfficialDistrict"] is False and
            r["geometry"] is None and r["worldStateEntityId"] is None, "district/geometry")
    for r in d["proposedEstablishments"]:
        req(r["areaId"] in ids["proposedUrbanAreas"], "missing area")
        req(r["futureEditorialObjectiveOnly"] is True and r["buildingMaterialized"] is False and
            r["propertyEntityId"] is None and r["actualLocationId"] is None and
            r["inventoryEntityIds"] == [] and r["capacity"] is None and
            r["worldStateEntityId"] is None, "invented building/stock")
    for r in d["proposedPeople"]:
        req(r["associatedEstablishmentId"] is None or
            r["associatedEstablishmentId"] in ids["proposedEstablishments"], "invalid person place")
        req(r["biographySource"] == GROUPS["proposedPeople"][2], "biography path")
        req(r["npcMaterialized"] is False and r["personEntityId"] is None and
            r["householdEntityId"] is None and r["knownWorldFacts"] == [] and
            r["royalNavalRank"] is None and r["worldStateEntityId"] is None, "invented person/rank")
    for r in d["proposedPrivateMemories"]:
        req(r["personRef"] in ids["proposedPeople"] and r["isPublicHistoricalFact"] is False
            and r["datedEvent"] is None and r["worldStateEventId"] is None, "fabricated history")
    for r in d["proposedConditionalArcs"]:
        req(set(r["personRefs"]) <= ids["proposedPeople"] and r["conditional"] is True and
            r["implementationStatus"]=="NOT_IMPLEMENTED" and r["triggered"] is False and
            r["worldStateEventId"] is None, "triggered arc")
    for r in d["testOnlyScenes"]:
        req(set(r["personRefs"]) <= ids["proposedPeople"] and
            r["createsEvent"] is False and r["worldStateEventId"] is None, "TEST_ONLY became event")
    req(len(d["editorialDecisionRecommendations"])==8, "eight editorial decisions")
    for i,r in enumerate(d["editorialDecisionRecommendations"],1):
        req(r == {"id":f"SYV-DP22-{i:02}","selectedRecommendedOption":"A",
                  "selectionStatus":"SELECTED_CREATIVE_PROPOSAL",
                  "authorRatified":False,"canonPromotion":False}, "invented author approval")
    req(d["scopes"]["merge"] == "EXPLICIT_AUTHOR_AUTHORIZATION_REQUIRED" and
        d["scopes"]["cartography"] == "AUTHOR_AUTHORIZED_MAP_REQUIRED", "unsafe scope")
    if check_files:
        for filename in DOCS:
            req((DOC/filename).is_file(), "missing document "+filename)
        for key,(prefix,count,source) in GROUPS.items():
            prose=(DOC/source).read_text(encoding="utf-8")
            for r in d[key]:
                req(r["id"] in prose and r.get("name",r.get("title")) in prose,
                    "documentation differs from inventory: "+r["id"])
        decisions=(DOC/DOCS[-1]).read_text(encoding="utf-8")
        for r in d["editorialDecisionRecommendations"]:
            req(r["id"] in decisions,"decision absent from prose")
        paths=d["canonicalSourcePaths"]
        req(len(paths)==4 and len(set(paths))==4,"source count")
        for source in paths:
            req(source.startswith("Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan/"),
                "unexpected source root")
            p=ROOT/source
            req(p.is_file() and "Syvaris" in p.read_text(encoding="utf-8"),
                "missing canon source: "+source)

def negative_cases(d):
    mutations=[
      (("status",),"CANON_APPROVED"), (("authorRatifiedNewContent",),True),
      (("addsCanon",),True), (("mergeAuthorized",),True),
      (("createsWorldStateEntities",),True), (("createsBuildings",),True),
      (("createsPhysicalMap",),True), (("coreRpgIntegrated",),True),
      (("godotIntegrated",),True), (("cityId",),"taramin"),
      (("dependency","predecessorPr"),43),
      (("canonClaims","royalNavyPresenceAuthority"),"DAROVAN"),
      (("canonClaims","d07ConceptDecision"),"DAR-D07-03_B"),
      (("canonClaims","totalIslandPopulation"),9000),
      (("canonClaims","smallerCovesHaveAuthorizedPorts"),True),
      (("canonClaims","automaticMainlandSeaRoute"),True),
      (("canonClaims","cityPopulationRange","maxInclusive"),20000),
      (("proposedUrbanAreas",0,"isOfficialDistrict"),True),
      (("proposedEstablishments",0,"buildingMaterialized"),True),
      (("proposedPeople",6,"royalNavalRank"),"almirante"),
      (("proposedPrivateMemories",0,"isPublicHistoricalFact"),True),
      (("proposedConditionalArcs",0,"triggered"),True),
      (("testOnlyScenes",0,"createsEvent"),True),
      (("editorialDecisionRecommendations",0,"authorRatified"),True)
    ]
    mutations += [(("lockedUnknowns",name),"fabricated") for name in d["lockedUnknowns"]]
    for key in GROUPS:
        mutations += [((key,0,"id"),"SYV-INVALID"),((key,0,"status"),"AUTHORED")]
    rejected=0
    for route,value in mutations:
        m=copy.deepcopy(d)
        node=m
        for part in route[:-1]:
            node=node[part]
        node[route[-1]]=value
        try:
            invariant(m)
        except AssertionError:
            rejected+=1
        else:
            raise AssertionError("negative test accepted: "+repr(route))
    return rejected

def main():
    d=json.loads(DATA.read_text(encoding="utf-8"))
    invariant(d,check_files=True)
    n=negative_cases(d)
    print(f"D.P22 SYVARIS STATIC OK; {n} negative mutations rejected; no canon promotion or runtime.")

if __name__=="__main__":
    main()

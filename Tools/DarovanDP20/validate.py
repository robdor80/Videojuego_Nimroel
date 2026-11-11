#!/usr/bin/env python3
"""D.P20 Veldora: guardas documentales de canon, no pruebas del motor."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = BASE / "Datos operativos/darovan_dp20_veldora_proposals_v0.1.json"

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def req(ok, text):
    if not ok:
        raise AssertionError(text)

def invariant(d, check_files=True):
    req(d["schemaVersion"] == 1 and d["version"] == "0.1.0", "schema version")
    req(d["documentId"] == "darovan_dp20_veldora_city_authorship_proposals_v0.1", "document id")
    req(d["phase"] == "D.P20" and d["cityId"] == "veldora" and d["cityKind"] == "canonical_city_manual_reference", "scope")
    req(d["status"] == "MIXED_AUTHORED_DP20_01_02_AND_PENDING_PROPOSALS" and d["authorApprovalRecorded"] is True and d["addsCanon"] is True, "approval limited to popular names")
    req(d["createsWorldStateEntities"] is False and d["externalCustomsFacilityCreated"] is False and d["privateRoyalArmyCreated"] is False, "no instances")
    c=d["canonClaims"]
    req(c["principalCommercialPortOfNorgard"] is True and c["gulf"] == "Golfo de Veldora", "canonical commercial role")
    req(c["commercialLayout"] == "distributed_organic_B" and c["d07AuthorDecision"] == "DAR-D07-01_B", "D07 layout")
    req(c["approvedCityCharacter"]=="PREDOMINANTLY_TRADITIONAL_AND_GUILD_ORIENTED" and c["approvedCityCharacterOption"]=="DAR-DP20-02_B", "approved B city character")
    req(c["cityCharacterDoesNotDisplaceExternalPort"] is True and c["cityCharacterCreatesNewGuildInstitutions"] is False, "character may not invent institutions")
    approved_names=["Borde de las Marcas","Patios de la Cuenta","Calles del Trato","Patios del Oficio","Tejas Serenas","Vuelta del Camino"]
    req(c["approvedPopularAreaNames"]==approved_names and c["approvedPopularAreaNamesDoNotDefineDistricts"] is True,"approved popular names without official districts")
    req(c["populationRange"] == {"minInclusive":29000,"maxInclusive":35000,"exact":None}, "D08 population")
    req(c["urbanReferenceAltitudeMetersApprox"] == {"min":0,"max":60}, "D.P13 altitude")
    req(c["riverVeldoraIndependentFromBelaraLhera"] is True, "hydro")
    req(c["externalCustomsAuthority"] == "CORONA" and c["internalCustomsBetweenHouses"] is False, "customs")
    req(c["roadVeldoraTreihordExistsAsQualitativeLink"] is True, "attested road only")
    req(len(d["lockedUnknowns"]) >= 20 and all(v is None for v in d["lockedUnknowns"].values()), "unknowns must remain null")
    refs={}
    for key,num,prefix in (("proposedUrbanAreas",6,"VEL-U"),("proposedEstablishments",12,"VEL-L"),("proposedPeople",10,"VEL-N"),("proposedConflicts",4,"VEL-H")):
        records=d[key]
        req(len(records)==num and len({x["id"] for x in records})==num, "count or duplicate: "+key)
        refs[key]={x["id"] for x in records}
        for i,x in enumerate(records,1):
            req(x["id"]==prefix+str(i).zfill(2), "ordered ids: "+key)
            req(x["status"]=="PROPOSAL_PENDING_AUTHOR" and x["authorApproved"] is False and x["isCanonical"] is False, "not canon: "+key)
            req(x["worldStateEntityId"] is None and x["coordinates"] is None, "no geometry/WorldState: "+key)
            req(bool(x.get("name",x.get("theme"))), "not empty: "+key)
    for i,x in enumerate(d["proposedUrbanAreas"]):
        req(x["name"]==approved_names[i] and x["popularNameApproval"]=="AUTHORED_DAR_DP20_01_A" and x["popularNameAuthorApproved"] is True, "popular names canonical only")
        req(x["spatialBoundary"] is None and x["isOfficialDistrict"] is False, "no approved district")
    for x in d["proposedEstablishments"]:
        req(x["areaId"] in refs["proposedUrbanAreas"] and x["actualLocationId"] is None, "places not located")
        req(x["capacity"] is None and x["ownerEntityId"] is None and x["inventoryEntityIds"] == [], "no stock or owner")
    for x in d["proposedPeople"]:
        req(x["associatedEstablishmentId"] is None or x["associatedEstablishmentId"] in refs["proposedEstablishments"], "person place reference")
        req(x["personEntityId"] is None and x["householdEntityId"] is None and x["isNamedNpcInWorld"] is False and x["knownCurrentFacts"]==[], "NPC not instantiated")
    for x in d["proposedConflicts"]:
        req(x["scenarioState"]=="CONDITIONAL_NOT_TRIGGERED" and set(x["personRefs"]) <= refs["proposedPeople"], "hypothetical conflicts")
    req(len(d["testOnlyScenes"])==6, "scene count")
    for i,x in enumerate(d["testOnlyScenes"],1):
        req(x["id"]=="VEL-E"+str(i).zfill(2) and x["status"]=="TEST_ONLY" and x["createsEvent"] is False and x["worldStateEntityId"] is None, "scene not event")
        req(set(x["personRefs"])<=refs["proposedPeople"], "scene people refs")
    req(len(d["authorDecisions"])==8, "eight authorial choices")
    for i,x in enumerate(d["authorDecisions"],1):
        if i==1:
            req(x=={"id":"DAR-DP20-01","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"SIX_POPULAR_NAMES_NO_ADMIN_DISTRICTS_NO_GEOMETRY"}, "exact approval scope")
        elif i==2:
            req(x=={"id":"DAR-DP20-02","status":"APPROVED","selectedOption":"B","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"PREDOMINANTLY_TRADITIONAL_AND_GUILD_ORIENTED_CULTURAL_CHARACTER_NO_NEW_INSTITUTIONS"}, "exact character approval scope")
        else:
            req(x=={"id":"DAR-DP20-"+str(i).zfill(2),"status":"PENDING_AUTHOR","selectedOption":None,"approvedDate":None,"canonPromotion":False}, "unauthorized other decision")
    req(all(v is False for v in d["runtime"].values()) and d["nextPhase"]=="D.P21_TARAMIN_NOT_STARTED", "scope isolation")
    if check_files:
        req(len(d["sourcePaths"])==7 and len(d["documentPaths"])==9, "document inventory")
        for ref in d["sourcePaths"]+d["documentPaths"]:
            req((ROOT/ref).is_file(), "missing path: "+ref)
        for ref in d["documentPaths"]:
            s=(ROOT/ref).read_text(encoding="utf-8")
            req(len(s)>350 and ("PROPOSAL" in s or "PROPUESTA" in s), "shallow/unmarked chapter: "+ref)
        d07=read(BASE/"Datos operativos/darovan_d07_canonical_cities_v0.1.json")
        city=next(x for x in d07["cities"] if x["id"]=="veldora")
        req(city["designStatus"]=="VISUAL_APROBADO_TRAZADO_URBANO_PENDIENTE" and city["authorApprovedNewLayout"] is False, "D07 layout protected")
        req(d07["fiscal"]["internalCustomsBetweenGreatHouses"] is False and d07["fiscal"]["veldoraExternalCustoms"] is True, "D07 fiscal")
        d08=read(BASE/"Datos operativos/darovan_d08_population_services_v0.1.json")
        pop=next(x for x in d08["cities"] if x["id"]=="veldora")
        req(pop["populationApprox"] is None and pop["populationRange"]["minInclusive"]==29000 and pop["populationRange"]["maxInclusive"]==35000,"D08 protected")
        alt=read(BASE/"Datos operativos/darovan_dp13_veldora_elevation_authorial_v0.1.json")
        req(alt["urbanAltitudeReferenceBandMetersApprox"]=={"min":0,"max":60}, "D.P13 protected")
        d05=read(BASE/"Datos operativos/darovan_d05_mobility_communications_v0.1.json")
        links={x["id"]:x for x in d05["confirmedTransportLinks"]}
        req(set(links)=={"d05_road_veldora_treihord","d05_belara_shallow_haul","d05_vena_restricted"}, "D05 three links")
        req(links["d05_road_veldora_treihord"]["routeGeometry"] is None, "D05 remains unmapped")

def mutation_tests(d):
    cases=[
        ("canon declared",lambda x:x.update(status="AUTHORED")),
        ("author approval erased",lambda x:x.update(authorApprovalRecorded=False)),
        ("world created",lambda x:x.update(createsWorldStateEntities=True)),
        ("population invented",lambda x:x["canonClaims"]["populationRange"].update(exact=32000)),
        ("altitude invented",lambda x:x["canonClaims"]["urbanReferenceAltitudeMetersApprox"].update(max=200)),
        ("internal customs invented",lambda x:x["canonClaims"].update(internalCustomsBetweenHouses=True)),
        ("royal authority usurped",lambda x:x["canonClaims"].update(externalCustomsAuthority="DAROVAN")),
        ("street invented",lambda x:x["lockedUnknowns"].update(streetLayout="grid")),
        ("island identified",lambda x:x["lockedUnknowns"].update(islandIdentification="arven")),
        ("district canonized",lambda x:x["proposedUrbanAreas"][0].update(isOfficialDistrict=True)),
        ("area approved",lambda x:x["proposedUrbanAreas"][0].update(authorApproved=True)),
        ("local generated",lambda x:x["proposedEstablishments"][0].update(worldStateEntityId="invented")),
        ("inventory invented",lambda x:x["proposedEstablishments"][0].update(inventoryEntityIds=["x"])),
        ("npc generated",lambda x:x["proposedPeople"][0].update(isNamedNpcInWorld=True)),
        ("npc bad ref",lambda x:x["proposedPeople"][0].update(associatedEstablishmentId="unknown")),
        ("event claimed",lambda x:x["proposedConflicts"][0].update(scenarioState="OCCURRED")),
        ("scene event",lambda x:x["testOnlyScenes"][0].update(createsEvent=True)),
        ("approved decision changed",lambda x:x["authorDecisions"][0].update(selectedOption="B")),
        ("character decision altered",lambda x:x["authorDecisions"][1].update(selectedOption="A")),
        ("other decision prematurely selected",lambda x:x["authorDecisions"][2].update(selectedOption="A")),
        ("character altered",lambda x:x["canonClaims"].update(approvedCityCharacter="COSMOPOLITAN")),
        ("character invents guilds",lambda x:x["canonClaims"].update(cityCharacterCreatesNewGuildInstitutions=True)),
        ("popular name changed",lambda x:x["proposedUrbanAreas"][0].update(name="Otro nombre")),
        ("popular name approval removed",lambda x:x["proposedUrbanAreas"][0].update(popularNameAuthorApproved=False)),
        ("approved popular name omitted",lambda x:x["canonClaims"]["approvedPopularAreaNames"].pop()),
        ("runtime claimed",lambda x:x["runtime"].update(coreRpgIntegration=True)),
        ("D.P21 silently started",lambda x:x.update(nextPhase="D.P21_STARTED")),
    ]
    for label,edit in cases:
        mutated=copy.deepcopy(d); edit(mutated)
        try: invariant(mutated,check_files=False)
        except AssertionError: continue
        raise AssertionError("mutation escaped invariant: "+label)
    return len(cases)

if __name__=="__main__":
    d=read(DATA); invariant(d)
    n=mutation_tests(d)
    print(f"PASS D.P20: integral contract and {n} adverse mutations; source files and chapters verified.")
    print("DOCUMENTARY ONLY: six popular names and traditional-guild city character approved; no official districts, new guild institutions, runtime, NPCs or map instantiated.")

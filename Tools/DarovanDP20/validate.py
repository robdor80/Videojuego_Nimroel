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
    req(d["status"] == "EDITORIAL_CLOSURE_APPROVED_CI_REQUIRED_PR_DRAFT" and d["authorApprovalRecorded"] is True and d["addsCanon"] is True, "approval limited to popular names")
    req(d["createsWorldStateEntities"] is False and d["externalCustomsFacilityCreated"] is False and d["privateRoyalArmyCreated"] is False, "no instances")
    req(d["editorialClosure"]=={"decisionId":"DAR-DP20-08","selectedOption":"A","approvedDate":"2026-11-11","approvalStatus":"APPROVED_CONDITIONAL_CI","closureScope":"EDITORIAL_AUTHORSHIP_ONLY","requiredWorkflowFamilies":["Darovan D.P20 Veldora authoring validation","Darovan static regression D01-D12","Darovan DP13 physical territory checks","Darovan D.P14–D.P18 documentation contracts"],"ciCondition":"ALL_FOUR_WORKFLOW_FAMILIES_GREEN_ON_FINAL_HEAD","ciCertifiedInRepositoryData":False,"requiredCiPlatforms":["windows-2022","ubuntu-24.04"],"prNumber":43,"prMustRemainDraft":True,"mergeAuthorized":False,"requiresNewExplicitAuthorPermissionToMerge":True,"physicalCityCompleted":False,"coreRpgIntegrated":False,"godotIntegrated":False,"materializedWorldState":False,"nextPhase":"D.P21_TARAMIN_NOT_STARTED"}, "editorial closure conditional CI, no merger or runtime")
    req(d["approvedCartographyProcess"]=={"decisionId":"DAR-DP20-07","selectedOption":"A","approvalDate":"2026-11-11","processStatus":"APPROVED_NOT_EXECUTED","sourcePolicy":"AUTHOR_AUTHORIZED_MAP_ONLY","preserveExistingEditorialCanon":True,"requireSeparateAuthorDecisionForUnknownGeometry":True,"inventGeometry":False,"createsPhysicalMap":False,"createsStreets":False,"createsDocks":False,"createsBridges":False,"createsRiverPort":False,"createsBuildings":False,"createsTravelRouteMetrics":False,"altitudinalUrbanReferenceMetersApprox":{"min":0,"max":60}}, "cartography process approved, no made-up geometry")
    c=d["canonClaims"]
    req(c["principalCommercialPortOfNorgard"] is True and c["gulf"] == "Golfo de Veldora", "canonical commercial role")
    req(c["commercialLayout"] == "distributed_organic_B" and c["d07AuthorDecision"] == "DAR-D07-01_B", "D07 layout")
    req(c["approvedCityCharacter"]=="PREDOMINANTLY_TRADITIONAL_AND_GUILD_ORIENTED" and c["approvedCityCharacterOption"]=="DAR-DP20-02_B", "approved B city character")
    req(c["cityCharacterDoesNotDisplaceExternalPort"] is True and c["cityCharacterCreatesNewGuildInstitutions"] is False, "character may not invent institutions")
    approved_future_names=["Depósito de la Cuerda Ceniza","Mesa de los Tres Renglones","Taller de la Cuña Fina","Fragua del Arco Corto","Casa de las Dos Tejas","Patio del Encordado","La Medida Prestada","Horno de los Postigos","Casa de los Pliegos","Banco de las Hebillas","Archivo de las Copias","Patio de los Carros"]
    approved_future_purposes=["custodia_privada","escribania_privada","carpinteria_reparacion","herreria_menor","hospedaje","trabajo_cooperativo","pesaje_privado","panaderia","hogar_mercantil","taller_tienda","deposito_documental_privado","servicio_urbano"]
    req(c["approvedFutureEstablishments"]==[{"id":"VEL-L"+str(i).zfill(2),"name":approved_future_names[i-1],"purpose":approved_future_purposes[i-1]} for i in range(1,13)] and c["futureEstablishmentsArePhysicalEntities"] is False, "exact 12 future editorial objectives, not runtime")
    approved_biography_names=["Liria Menor","Sered Alvar","Naia Corven","Oren Talen","Vesa Orrin","Bram Iven","Mira Sern","Edris Fen","Adel Renvar","Fenra Doril"]
    approved_biography_roles=["comerciante","custodio","artesana","escribiente_aduanas_de_corona","trabajadora_adulta","transportista","posadera","copista","comerciante_acomodada","panadera"]
    req(c["approvedCharacterBiographyBases"]==[{"id":"VEL-N"+str(i).zfill(2),"name":approved_biography_names[i-1],"role":approved_biography_roles[i-1],"biographySource":"04_personajes_hogares_y_relaciones.md"} for i in range(1,11)] and c["approvedCharacterBiographiesCreatePeople"] is False, "exact ten approved biographies, no NPCs")
    approved_personal_memories=[("VEL-M01","La promesa incompleta","VEL-N01","Liria Menor"),("VEL-M02","El error de una copia","VEL-N08","Edris Fen"),("VEL-M03","La reparación hecha deprisa","VEL-N03","Naia Corven"),("VEL-M04","La ración prestada","VEL-N10","Fenra Doril")]
    req(c["approvedPersonalMemories"]==[{"id":mid,"title":title,"characterId":person_id,"characterName":person_name,"approval":"AUTHORED_PERSONAL_MEMORY_DAR_DP20_05_A","publicEvent":False,"eventDate":None,"worldStateEventId":None} for mid,title,person_id,person_name in approved_personal_memories], "only four approved personal memories without dates or events")
    req(c["personalMemoriesCreateHistoricalPublicEvents"] is False and c["personalMemoriesCreateWorldStateEvents"] is False, "no public history or worldstate from memories")
    approved_arc_titles=["El bulto que nadie quiere abrir","La herramienta que sostiene dos hogares","El rumor de una vela extranjera","Pan, paga y crédito"]
    approved_arc_themes=["bulto_que_nadie_quiere_abrir","herramienta_dos_hogares","rumor_vela_extranjera","pan_paga_y_credito"]
    expected_arcs=[{"id":a["id"],"title":approved_arc_titles[i],"theme":approved_arc_themes[i],"personRefs":a["personRefs"],"approval":"AUTHORED_FUTURE_CONDITIONAL_ARC_DAR_DP20_06_A","conditional":True,"implementationStatus":"NOT_IMPLEMENTED","triggered":False,"worldStateEventId":None} for i,a in enumerate(d["proposedConflicts"])]
    req(c["approvedFutureConditionalArcs"]==expected_arcs,"four authored conditional future arcs, none implemented")
    req(c["conditionalArcsMayStartWithoutCoreRpgPreconditions"] is False and c["conditionalArcsCreateExistingWorldStateEvents"] is False,"no CoreRPG bypass")
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
    for i,x in enumerate(d["proposedEstablishments"]):
        req(x["name"]==approved_future_names[i] and x["purpose"]==approved_future_purposes[i], "approved future establishment identity")
        req(x["canonicalFutureObjective"] is True and x["futureNameAndPurposeApproved"] is True and x["futureObjectiveApproval"]=="AUTHORED_FUTURE_OBJECTIVE_DAR_DP20_03_B" and x["materialized"] is False, "future objective distinct from physical instance")
        req(x["areaId"] in refs["proposedUrbanAreas"] and x["actualLocationId"] is None, "places not located")
        req(x["capacity"] is None and x["ownerEntityId"] is None and x["inventoryEntityIds"] == [], "no stock or owner")
    for i,x in enumerate(d["proposedPeople"]):
        req(x["name"]==approved_biography_names[i] and x["role"]==approved_biography_roles[i], "approved name and role")
        req(x["biographyApproval"]=="AUTHORED_BIOGRAPHY_BASE_DAR_DP20_04_A" and x["nameRoleBiographyApproved"] is True and x["npcMaterialized"] is False, "approved biography is not instantiated NPC")
        req(x["associatedEstablishmentId"] is None or x["associatedEstablishmentId"] in refs["proposedEstablishments"], "person place reference")
        req(x["personEntityId"] is None and x["householdEntityId"] is None and x["isNamedNpcInWorld"] is False and x["knownCurrentFacts"]==[], "NPC not instantiated")
    for x in d["proposedConflicts"]:
        req(x["scenarioState"]=="CONDITIONAL_NOT_TRIGGERED" and set(x["personRefs"]) <= refs["proposedPeople"], "hypothetical conflicts")
        req(x["designApproved"] is True and x["futureNarrativeArcApproval"]=="AUTHORED_FUTURE_CONDITIONAL_ARC_DAR_DP20_06_A" and x["arcImplemented"] is False and x["arcTriggered"] is False, "no activation of approved designs")
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
        elif i==3:
            req(x=={"id":"DAR-DP20-03","status":"APPROVED","selectedOption":"B","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"TWELVE_NAMED_ESTABLISHMENT_FUTURE_OBJECTIVES_ONLY_NO_PHYSICAL_MATERIALIZATION"}, "exact twelve future objectives approval")
        elif i==4:
            req(x=={"id":"DAR-DP20-04","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"TEN_CHARACTER_NAME_ROLE_BIOGRAPHY_BASES_ONLY_NO_NPC_MATERIALIZATION"}, "exact biography approval scope")
        elif i==5:
            req(x=={"id":"DAR-DP20-05","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"FOUR_PRIVATE_BIOGRAPHICAL_MEMORIES_ONLY_NO_DATE_NO_PUBLIC_EVENTS_NO_WORLDSTATE"}, "private memories only approval")
        elif i==6:
            req(x=={"id":"DAR-DP20-06","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":True,"approvalScope":"FOUR_FUTURE_CONDITIONAL_NARRATIVE_ARCS_ONLY_NOT_IMPLEMENTED_NOT_TRIGGERED"}, "exact future narrative approval")
        elif i==7:
            req(x=={"id":"DAR-DP20-07","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":False,"approvalScope":"AUTHOR_MAP_BASED_FUTURE_CARTOGRAPHY_NO_GEOMETRY_CREATED"}, "future cartography decision must not create a map")
        elif i==8:
            req(x=={"id":"DAR-DP20-08","status":"APPROVED","selectedOption":"A","approvedDate":"2026-11-11","canonPromotion":False,"approvalScope":"EDITORIAL_CLOSURE_CONDITIONAL_ALL_CI_GREEN_NO_MERGE_PR43_DRAFT"}, "final closure authorized conditional CI only")
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
        ("establishment decision altered",lambda x:x["authorDecisions"][2].update(selectedOption="A")),
        ("biography approval changed",lambda x:x["authorDecisions"][3].update(selectedOption="B")),
        ("memory approval changed",lambda x:x["authorDecisions"][4].update(selectedOption="B")),
        ("approved arc option changed",lambda x:x["authorDecisions"][5].update(selectedOption="B")),
        ("approved cartography changed",lambda x:x["authorDecisions"][6].update(selectedOption="B")),
        ("editorial closure option altered",lambda x:x["authorDecisions"][7].update(selectedOption="B")),
        ("closure marked certified without external CI",lambda x:x["editorialClosure"].update(ciCertifiedInRepositoryData=True)),
        ("merge permission fabricated",lambda x:x["editorialClosure"].update(mergeAuthorized=True)),
        ("draft lost",lambda x:x["editorialClosure"].update(prMustRemainDraft=False)),
        ("CI requirement bypassed",lambda x:x["editorialClosure"].update(ciCondition="IGNORED")),
        ("physical city falsely completed",lambda x:x["editorialClosure"].update(physicalCityCompleted=True)),
        ("coreRpg falsely integrated",lambda x:x["editorialClosure"].update(coreRpgIntegrated=True)),
        ("closure workflow omitted",lambda x:x["editorialClosure"]["requiredWorkflowFamilies"].pop()),
        ("cartography invented",lambda x:x["approvedCartographyProcess"].update(inventGeometry=True)),
        ("cartography creates streets",lambda x:x["approvedCartographyProcess"].update(createsStreets=True)),
        ("cartography creates new docks",lambda x:x["approvedCartographyProcess"].update(createsDocks=True)),
        ("cartography creates bridge",lambda x:x["approvedCartographyProcess"].update(createsBridges=True)),
        ("cartography creates river port",lambda x:x["approvedCartographyProcess"].update(createsRiverPort=True)),
        ("cartography creates buildings",lambda x:x["approvedCartographyProcess"].update(createsBuildings=True)),
        ("cartography source replaced",lambda x:x["approvedCartographyProcess"].update(sourcePolicy="AI_GENERATED_MAP")),
        ("cartography unapproved coordinates",lambda x:x["approvedCartographyProcess"].update(requireSeparateAuthorDecisionForUnknownGeometry=False)),
        ("approved arc title changed",lambda x:x["canonClaims"]["approvedFutureConditionalArcs"][0].update(title="Otro")),
        ("approved arc missing",lambda x:x["canonClaims"]["approvedFutureConditionalArcs"].pop()),
        ("arc implemented silently",lambda x:x["proposedConflicts"][0].update(arcImplemented=True)),
        ("arc triggered silently",lambda x:x["proposedConflicts"][0].update(arcTriggered=True)),
        ("arc event invented",lambda x:x["canonClaims"]["approvedFutureConditionalArcs"][0].update(worldStateEventId="false")),
        ("core precondition bypass",lambda x:x["canonClaims"].update(conditionalArcsMayStartWithoutCoreRpgPreconditions=True)),
        ("approved memory title mutated",lambda x:x["canonClaims"]["approvedPersonalMemories"][0].update(title="Otra historia")),
        ("approved memory owner mutated",lambda x:x["canonClaims"]["approvedPersonalMemories"][0].update(characterId="VEL-N02")),
        ("approved memory invented date",lambda x:x["canonClaims"]["approvedPersonalMemories"][0].update(eventDate="1234-01-01")),
        ("approved memory turned public",lambda x:x["canonClaims"]["approvedPersonalMemories"][0].update(publicEvent=True)),
        ("approved memory created event",lambda x:x["canonClaims"]["approvedPersonalMemories"][0].update(worldStateEventId="fake")),
        ("public history forged",lambda x:x["canonClaims"].update(personalMemoriesCreateHistoricalPublicEvents=True)),
        ("memory created worldstate",lambda x:x["canonClaims"].update(personalMemoriesCreateWorldStateEvents=True)),
        ("approved memory omitted",lambda x:x["canonClaims"]["approvedPersonalMemories"].pop()),
        ("approved character name changed",lambda x:x["proposedPeople"][0].update(name="Nombre cambiado")),
        ("approved character role changed",lambda x:x["proposedPeople"][0].update(role="superintendente")),
        ("approved biography scope stripped",lambda x:x["proposedPeople"][0].update(nameRoleBiographyApproved=False)),
        ("NPC materialized from biography",lambda x:x["proposedPeople"][0].update(npcMaterialized=True)),
        ("biography implicitly creates people",lambda x:x["canonClaims"].update(approvedCharacterBiographiesCreatePeople=True)),
        ("biography list mutated",lambda x:x["canonClaims"]["approvedCharacterBiographyBases"].pop()),
        ("establishment future name altered",lambda x:x["proposedEstablishments"][0].update(name="Otro depósito")),
        ("establishment future function altered",lambda x:x["proposedEstablishments"][0].update(purpose="aduana_corona")),
        ("establishment future approval erased",lambda x:x["proposedEstablishments"][0].update(futureNameAndPurposeApproved=False)),
        ("establishment materialized silently",lambda x:x["proposedEstablishments"][0].update(materialized=True)),
        ("future objective made physical",lambda x:x["canonClaims"].update(futureEstablishmentsArePhysicalEntities=True)),
        ("future objective list corrupted",lambda x:x["canonClaims"]["approvedFutureEstablishments"].pop()),
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
    print("DOCUMENTARY ONLY: all eight decisions approved; editorial closure conditional to external green CI, PR #43 Draft and not merged; no physical map, NPC, missions or WorldState.")

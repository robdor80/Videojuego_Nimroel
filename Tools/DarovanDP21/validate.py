#!/usr/bin/env python3
"""Taramin D.P21: contract verification, sources and adversarial mutations. NOT runtime."""
import copy
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA=BASE/"Datos operativos/darovan_dp21_taramin_proposals_v0.1.json"

def read(p): return json.loads(p.read_text(encoding="utf-8"))
def req(cond,msg):
    if not cond: raise AssertionError(msg)

def validate(d, files=True):
    req((d["phase"],d["cityId"],d["status"]) == ("D.P21","taramin","PARTIAL_AUTHOR_APPROVAL_NAMES_CHARACTER_ESTABLISHMENTS_BIOGRAPHIES"),"wrong phase/state")
    req(d["authorApprovalRecorded"] is True and d["addsCanon"] is True and d["createsWorldStateEntities"] is False,"limited author approval")
    c=d["canonClaims"]
    exact={
      "cityOwner":"CASA_DAROVAN","cityManualOnly":True,"thalenSingleNamedRiver":True,
      "thalenTerminalArms":2,"cityBetweenThalenTerminalArms":True,
      "receivingGulf":"GOLFO_DE_NORGARD","fishingPortCanonical":True,
      "principalFishingWorkAreaConceptualOnly":True,"principalFishingZonePosition":None,
      "maritimeAndFluvialFishing":True,"marineProductsAndOils":True,
      "populationRange":{"minInclusive":14000,"maxInclusive":20000,"exact":None},
      "urbanReferenceAltitudeMetersApprox":{"min":0,"max":40},
      "northCentralPeninsularHillsReferenceMetersApprox":{"min":300,"max":600},
      "northernCentralSemiaridTransition":True,"southernTaraminForestOne":True,
      "industrialTaraminLoggingAllowed":False,"kingsJusticeAuthority":True,
      "darovanOwnNavy":False,"externalCustomsAuthorityTransferredFromVeldora":False,
      "riverNavigabilityConfirmed":False,"bridgeKnown":False,
      "approvedPopularAreaNames":["Voces de la Marea","El Patio de los Remiendos","Sombras de la Cal","Las Cuentas Secas","La Voz del Thalen","Los Oficios de Tierra"],
      "approvedPopularAreaNamesDoNotDefineDistricts":True,
      "approvedCityCharacter":"PRAGMATICA_MARINERA_PLURAL",
      "approvedCityCharacterOption":"A",
      "cityCharacterDoesNotReduceResidentsToFishing":True,
      "cityCharacterCreatesNewLegalOrGuildInstitutions":False,
      "approvedFutureEstablishments":[
        {"id":f"TAR-L{i:02d}","name":name,"purpose":purpose,"status":"AUTHORED_FUTURE_OBJECTIVE","materialized":False}
        for i,(name,purpose) in enumerate([
          ("Casa del Cabo Zurcido","reparacion_cabos"),
          ("El Peso de la Sal","verificacion_calidad"),
          ("Despensa de las Dos Vasijas","preparacion_alimentos"),
          ("Taller del Aro Partido","reparacion_recipientes"),
          ("Patio de las Tinajas Quietas","almacenaje_agua_condicionado"),
          ("Mesa del Cordel Corto","acuerdos_pequena_escala"),
          ("La Hoja y el Anzuelo","herramientas_manuales"),
          ("Fogón de Bruma","comida_y_reunion"),
          ("Escribanía del Trato Llano","copia_de_acuerdos_privados"),
          ("El Nudo de Regreso","noticias_no_verificadas"),
          ("Cestas de la Tierra Ocre","intercambio_interior"),
          ("El Telar de las Horas","textiles")],1)],
      "futureEstablishmentsArePhysicalEntities":False,
      "futureEstablishmentApprovalCreatesNewPortOrWaterInfrastructure":False,
      "approvedFuturePeople":[
        {"id":f"TAR-N{i:02d}","name":name,"role":role,"biography":bio,
         "status":"AUTHORED_EDITORIAL_BIOGRAPHY","npcMaterialized":False}
        for i,(name,role,bio) in enumerate([
          ("Mareva Senn","negociadora_partidas","Se niega a certificar calidad sin comprobar"),
          ("Eiron Valc","reparador_utiles","Exige probar reparaciones y teme reconocer errores"),
          ("Telia Arvenn","cuidadora_cocinera","Cuida a otros pero anhela tiempo propio"),
          ("Corven Dail","reparador_recipientes","Reconoce la dureza con clientes sin recursos"),
          ("Orea Niv","aprendiz_escribania","Quiere un oficio ajeno a la pesca"),
          ("Daric Fen","proveedor_encargos","Prefiere pequeños compromisos verificables"),
          ("Inara Vel","trabajadora_textil","Defiende que el trabajo doméstico tiene valor"),
          ("Sarel Tern","transmisor_noticias","Distingue testimonio de conocimiento aunque falle"),
          ("Yalena Mors","cuidadora_vecinal","Necesita apoyo además de ofrecer cuidados"),
          ("Breon Cal","auxiliar_seguridad_civil","No confunde su función civil con sentencia o mando naval")],1)],
      "approvedBiographiesDoNotCreateNPCs":True,
      "approvedBiographiesDoNotEstablishRelationships":True,
      "approvedBiographiesDoNotEstablishPrivateMemories":True}
    req(c==exact,"protected canon altered")
    req(len(d["lockedUnknowns"])>=30 and all(v is None for v in d["lockedUnknowns"].values()),"invented unknown")
    ids={}
    for key,n,prefix in [("proposedUrbanAreas",6,"TAR-U"),("proposedEstablishments",12,"TAR-L"),("proposedPeople",10,"TAR-N")]:
        items=d[key]
        req([e["id"] for e in items]==[f"{prefix}{i:02d}" for i in range(1,n+1)],"IDs/count: "+key)
        ids[key]={e["id"] for e in items}
        for e in items:
            req(e["status"]=="PROPOSAL_PENDING_AUTHOR" and e["authorApproved"] is False and e["isCanonical"] is False,"new lore promoted: "+key)
            req(e["worldStateEntityId"] is None and e["coordinates"] is None and bool(e["name"]),"materialized or unnamed: "+key)
    for i,e in enumerate(d["proposedUrbanAreas"]):
        req(e["isOfficialDistrict"] is False and e["spatialBoundary"] is None,"district invented")
        req(e["name"]==exact["approvedPopularAreaNames"][i]
            and e["popularNameApproval"]=="AUTHORED_TAR_DP21_01_A"
            and e["popularNameAuthorApproved"] is True,"approved popular names changed")
    for i,e in enumerate(d["proposedEstablishments"]):
        target=exact["approvedFutureEstablishments"][i]
        req(e["name"]==target["name"] and e["purpose"]==target["purpose"]
            and e["canonicalFutureObjective"] is True
            and e["futureObjectiveApproval"]=="AUTHORED_FUTURE_OBJECTIVE_TAR_DP21_03_A"
            and e["futureNameAndPurposeApproved"] is True,"approved future establishment changed")
        req(e["areaId"] in ids["proposedUrbanAreas"] and e["actualLocationId"] is None and e["materialized"] is False
            and e["ownerEntityId"] is None and e["inventoryEntityIds"]==[] and e["capacity"] is None,"shop invented")
    for i,e in enumerate(d["proposedPeople"]):
        target=exact["approvedFuturePeople"][i]
        req(e["name"]==target["name"] and e["role"]==target["role"] and e["biography"]==target["biography"]
            and e["canonicalEditorialBase"] is True
            and e["editorialBiographyApproval"]=="AUTHORED_EDITORIAL_BIOGRAPHY_TAR_DP21_04_A"
            and e["futureNameRoleBiographyApproved"] is True,"approved editorial character altered")
        req(e["personEntityId"] is None and e["householdEntityId"] is None and e["npcMaterialized"] is False
            and e["relationsMaterialized"] is False and e["knownCurrentFacts"]==[] and bool(e["role"]) and bool(e["biography"]),"NPC invented")
    req([e["id"] for e in d["proposedPersonalMemories"]]==[f"TAR-M{i:02d}" for i in range(1,5)],"memory IDs")
    for e in d["proposedPersonalMemories"]:
        req(e["status"]=="PROPOSAL_PENDING_AUTHOR" and e["authorApproved"] is False and e["private"] is True
            and e["characterId"] in ids["proposedPeople"] and e["eventDate"] is None
            and e["publicHistoricalEvent"] is False and e["worldStateEventId"] is None and bool(e["title"]),"memory invented")
    req([e["id"] for e in d["proposedConditionalArcs"]]==[f"TAR-H{i:02d}" for i in range(1,5)],"arc IDs")
    for e in d["proposedConditionalArcs"]:
        req(e["status"]=="PROPOSAL_PENDING_AUTHOR" and e["authorApproved"] is False
            and e["conditional"] is True and e["implemented"] is False and e["triggered"] is False
            and e["worldStateEventId"] is None and len(e["personRefs"])>=2
            and set(e["personRefs"])<=ids["proposedPeople"],"arc activated")
    req([e["id"] for e in d["testOnlyScenes"]]==[f"TAR-E{i:02d}" for i in range(1,7)],"scene IDs")
    for e in d["testOnlyScenes"]:
        req(e["status"]=="TEST_ONLY" and e["createsEvent"] is False and e["worldStateEntityId"] is None
            and len(e["personRefs"])>=2 and set(e["personRefs"])<=ids["proposedPeople"],"scene made real")
    req(d["authorDecisions"]==[{"id":"TAR-DP21-01","status":"APPROVED","selectedOption":"A",
         "approvedDate":"2026-11-11","canonPromotion":True,
         "approvalScope":"SIX_POPULAR_NAMES_NO_OFFICIAL_DISTRICTS_NO_GEOMETRY"},
         {"id":"TAR-DP21-02","status":"APPROVED","selectedOption":"A",
          "approvedDate":"2026-11-11","canonPromotion":True,
          "approvalScope":"PRAGMATIC_MARITIME_PLURAL_CITY_CHARACTER_NO_NEW_LAWS_OR_INSTITUTIONS"},
         {"id":"TAR-DP21-03","status":"APPROVED","selectedOption":"A",
          "approvedDate":"2026-11-11","canonPromotion":True,
          "approvalScope":"TWELVE_NAMED_ESTABLISHMENT_FUTURE_OBJECTIVES_ONLY_NO_PHYSICAL_MATERIALIZATION"},
         {"id":"TAR-DP21-04","status":"APPROVED","selectedOption":"A",
          "approvedDate":"2026-11-11","canonPromotion":True,
          "approvalScope":"TEN_NAMED_ROLE_BIOGRAPHY_EDITORIAL_BASES_ONLY_NO_NPC_HOUSEHOLD_OR_RELATION_INSTANTIATION"}]
         + [{"id":f"TAR-DP21-{i:02d}","status":"PENDING_AUTHOR","selectedOption":None,
             "approvedDate":None,"canonPromotion":False} for i in range(5,9)],"approvals forged")
    req(all(v is False for v in d["runtime"].values()) and d["nextPhase"]=="D.P22_SYVARIS_NOT_STARTED","runtime created")
    req(d["editorialClosure"]=={"authorDecisionId":"TAR-DP21-08","closureApproved":False,
          "ciCertifiedInData":False,"mergeAuthorized":False,"prMustRemainDraft":True,
          "physicalCityCompleted":False,"requiredCiPlatforms":["ubuntu-24.04","windows-2022"]},"merge/closure forged")
    if not files: return
    req(len(d["sourcePaths"])==7 and len(d["documentPaths"])==9,"inventory missing")
    for p in d["sourcePaths"]+d["documentPaths"]:
        req((ROOT/p).is_file(),"missing file "+p)
    for p in d["documentPaths"]:
        s=(ROOT/p).read_text(encoding="utf-8")
        req(len(s)>900 and any(x in s for x in ("PROPUESTA","PROPOSAL","PENDIENTE")),"unmarked chapter "+p)
    d07=read(BASE/"Datos operativos/darovan_d07_canonical_cities_v0.1.json")
    city=next(e for e in d07["cities"] if e["id"]=="taramin")
    facts={e["id"]:e["value"] for e in city["facts"]}
    req(city["manualOnly"] and city["authorApprovedNewLayout"] is False
        and facts["between_two_thalen_terminal_arms"] is True
        and facts["thalen_terminal_arms_two_not_two_rivers"] is True
        and facts["fishing_port_and_fluvial_fishing"] is True
        and d07["hydro"]["thalenTerminalArms"]==2
        and d07["hydro"]["thalenArmsNavigation"] is None,"D07 source")
    d08=read(BASE/"Datos operativos/darovan_d08_population_services_v0.1.json")
    pop=next(e for e in d08["cities"] if e["id"]=="taramin")
    req(pop["populationApprox"] is None and pop["populationRange"]["minInclusive"]==14000
        and pop["populationRange"]["maxInclusive"]==20000,"D08 source")
    alt=read(BASE/"Datos operativos/darovan_dp13_taramin_elevation_authorial_v0.1.json")
    hills=read(BASE/"Datos operativos/darovan_dp13_taramin_north_central_hills_authorial_v0.1.json")
    req(alt["urbanAltitudeReferenceBandMetersApprox"]=={"min":0,"max":40}
        and alt["bridgeCount"] is None
        and hills["characteristicHillElevationBandMetersApprox"]=={"min":300,"max":600},"D.P13 source")
    d09=read(BASE/"Datos operativos/darovan_d09_governance_security_v0.1.json")
    loc=next(e for e in d09["localities"] if e["id"]=="taramin")
    req("kings_justice_ordinary" in loc["functions"] and loc["locationOrBuildingNew"] is False,"D09 source")
    d10=read(BASE/"Datos operativos/darovan_d10_culture_society_v0.1.json")
    prof=next(e for e in d10["localProfiles"] if e["id"]=="taramin")
    req(prof["individualVariation"] is True and prof["createsNpc"] is False,"D10 source")

def mutation_test(d):
    edits=[
      ("canon",lambda x:x.update(addsCanon=False)),("approval",lambda x:x.update(authorApprovalRecorded=False)),
      ("state",lambda x:x.update(createsWorldStateEntities=True)),
      ("river",lambda x:x["canonClaims"].update(thalenTerminalArms=3)),
      ("rivers",lambda x:x["canonClaims"].update(thalenSingleNamedRiver=False)),
      ("site",lambda x:x["canonClaims"].update(cityBetweenThalenTerminalArms=False)),
      ("port",lambda x:x["canonClaims"].update(fishingPortCanonical=False)),
      ("newport",lambda x:x["canonClaims"].update(principalFishingZonePosition="north_arm")),
      ("pop",lambda x:x["canonClaims"]["populationRange"].update(exact=17000)),
      ("alt",lambda x:x["canonClaims"]["urbanReferenceAltitudeMetersApprox"].update(max=100)),
      ("hills",lambda x:x["canonClaims"]["northCentralPeninsularHillsReferenceMetersApprox"].update(max=900)),
      ("wood",lambda x:x["canonClaims"].update(industrialTaraminLoggingAllowed=True)),
      ("navy",lambda x:x["canonClaims"].update(darovanOwnNavy=True)),
      ("tax",lambda x:x["canonClaims"].update(externalCustomsAuthorityTransferredFromVeldora=True)),
      ("navigability",lambda x:x["canonClaims"].update(riverNavigabilityConfirmed=True)),
      ("bridge",lambda x:x["canonClaims"].update(bridgeKnown=True)),
      ("unknown",lambda x:x["lockedUnknowns"].update(bridgeCount=1)),
      ("dock",lambda x:x["lockedUnknowns"].update(newDocks=["dock"])),
      ("route",lambda x:x["lockedUnknowns"].update(routeGeometry="line")),
      ("district",lambda x:x["proposedUrbanAreas"][0].update(isOfficialDistrict=True)),
      ("boundary",lambda x:x["proposedUrbanAreas"][0].update(spatialBoundary="poly")),
      ("areaapproved",lambda x:x["proposedUrbanAreas"][0].update(authorApproved=True)),
      ("popular_name_modified",lambda x:x["proposedUrbanAreas"][0].update(name="Otro nombre")),
      ("popular_name_approval_lost",lambda x:x["proposedUrbanAreas"][0].update(popularNameAuthorApproved=False)),
      ("popular_name_canon_lost",lambda x:x["canonClaims"]["approvedPopularAreaNames"].pop()),
      ("popular_district_forged",lambda x:x["canonClaims"].update(approvedPopularAreaNamesDoNotDefineDistricts=False)),
      ("areaentity",lambda x:x["proposedUrbanAreas"][0].update(worldStateEntityId="id")),
      ("owner",lambda x:x["proposedEstablishments"][0].update(ownerEntityId="id")),
      ("stock",lambda x:x["proposedEstablishments"][0].update(inventoryEntityIds=["fish"])),
      ("location",lambda x:x["proposedEstablishments"][0].update(actualLocationId="plot")),
      ("business",lambda x:x["proposedEstablishments"][0].update(materialized=True)),
      ("badref",lambda x:x["proposedEstablishments"][0].update(areaId="TAR-U99")),
      ("npc",lambda x:x["proposedPeople"][0].update(npcMaterialized=True)),
      ("house",lambda x:x["proposedPeople"][0].update(householdEntityId="home")),
      ("knowledge",lambda x:x["proposedPeople"][0].update(knownCurrentFacts=["omniscient"])),
      ("relationship",lambda x:x["proposedPeople"][0].update(relationsMaterialized=True)),
      ("memorydate",lambda x:x["proposedPersonalMemories"][0].update(eventDate="1234")),
      ("memorypublic",lambda x:x["proposedPersonalMemories"][0].update(publicHistoricalEvent=True)),
      ("memoryevent",lambda x:x["proposedPersonalMemories"][0].update(worldStateEventId="event")),
      ("memoryperson",lambda x:x["proposedPersonalMemories"][0].update(characterId="TAR-N99")),
      ("arcstart",lambda x:x["proposedConditionalArcs"][0].update(triggered=True)),
      ("arcimplemented",lambda x:x["proposedConditionalArcs"][0].update(implemented=True)),
      ("arcevent",lambda x:x["proposedConditionalArcs"][0].update(worldStateEventId="event")),
      ("arcperson",lambda x:x["proposedConditionalArcs"][0].update(personRefs=["TAR-N99"])),
      ("scene",lambda x:x["testOnlyScenes"][0].update(createsEvent=True)),
      ("sceneperson",lambda x:x["testOnlyScenes"][0].update(personRefs=["TAR-N99"])),
      ("decision",lambda x:x["authorDecisions"][0].update(selectedOption="B")),
      ("decisionstatus",lambda x:x["authorDecisions"][0].update(status="PENDING_AUTHOR")),
      ("decision_scope",lambda x:x["authorDecisions"][0].update(approvalScope="SIX_OFFICIAL_DISTRICTS")),
      ("second_decision_option",lambda x:x["authorDecisions"][1].update(selectedOption="B")),
      ("second_decision_status",lambda x:x["authorDecisions"][1].update(status="PENDING_AUTHOR")),
      ("second_decision_scope",lambda x:x["authorDecisions"][1].update(approvalScope="CREATES_NEW_GUILD")),
      ("city_character_changed",lambda x:x["canonClaims"].update(approvedCityCharacter="GREMIAL")), 
      ("city_character_option_changed",lambda x:x["canonClaims"].update(approvedCityCharacterOption="B")),
      ("all_fishers",lambda x:x["canonClaims"].update(cityCharacterDoesNotReduceResidentsToFishing=False)),
      ("invented_institutions",lambda x:x["canonClaims"].update(cityCharacterCreatesNewLegalOrGuildInstitutions=True)),
      ("third_decision_option",lambda x:x["authorDecisions"][2].update(selectedOption="B")),
      ("third_decision_status",lambda x:x["authorDecisions"][2].update(status="PENDING_AUTHOR")),
      ("third_decision_scope",lambda x:x["authorDecisions"][2].update(approvalScope="TWELVE_EXISTING_SHOPS")),
      ("future_establishment_name",lambda x:x["proposedEstablishments"][0].update(name="Otro negocio")),
      ("future_establishment_purpose",lambda x:x["proposedEstablishments"][0].update(purpose="aduana_real")),
      ("future_establishment_approval_lost",lambda x:x["proposedEstablishments"][0].update(futureNameAndPurposeApproved=False)),
      ("future_establishment_flag_lost",lambda x:x["proposedEstablishments"][0].update(canonicalFutureObjective=False)),
      ("future_establishment_scope_changed",lambda x:x["proposedEstablishments"][0].update(futureObjectiveApproval="AUTHORED_PHYSICAL")),
      ("future_establishment_canon_mutated",lambda x:x["canonClaims"]["approvedFutureEstablishments"].pop()),
      ("future_establishment_physically_forged",lambda x:x["canonClaims"].update(futureEstablishmentsArePhysicalEntities=True)),
      ("new_water_infrastructure_forged",lambda x:x["canonClaims"].update(futureEstablishmentApprovalCreatesNewPortOrWaterInfrastructure=True)),
      ("fourth_decision_option",lambda x:x["authorDecisions"][3].update(selectedOption="B")),
      ("fourth_decision_status",lambda x:x["authorDecisions"][3].update(status="PENDING_AUTHOR")),
      ("fourth_decision_scope",lambda x:x["authorDecisions"][3].update(approvalScope="TEN_NPCS_MATERIALIZED")),
      ("future_character_name",lambda x:x["proposedPeople"][0].update(name="Otra persona")),
      ("future_character_role",lambda x:x["proposedPeople"][0].update(role="juez_rey")),
      ("future_character_bio",lambda x:x["proposedPeople"][0].update(biography="Otro pasado")),
      ("future_character_approval_lost",lambda x:x["proposedPeople"][0].update(futureNameRoleBiographyApproved=False)),
      ("future_character_flag_lost",lambda x:x["proposedPeople"][0].update(canonicalEditorialBase=False)),
      ("future_character_scope_changed",lambda x:x["proposedPeople"][0].update(editorialBiographyApproval="NPC_AUTHORED_PHYSICAL")),
      ("future_character_canon_mutated",lambda x:x["canonClaims"]["approvedFuturePeople"].pop()),
      ("future_character_instantiation_forged",lambda x:x["canonClaims"].update(approvedBiographiesDoNotCreateNPCs=False)),
      ("future_character_relationship_forged",lambda x:x["canonClaims"].update(approvedBiographiesDoNotEstablishRelationships=False)),
      ("future_character_memory_forged",lambda x:x["canonClaims"].update(approvedBiographiesDoNotEstablishPrivateMemories=False)),
      ("another_decision",lambda x:x["authorDecisions"][4].update(status="APPROVED")),
      ("ci",lambda x:x["editorialClosure"].update(ciCertifiedInData=True)),
      ("merge",lambda x:x["editorialClosure"].update(mergeAuthorized=True)),
      ("draft",lambda x:x["editorialClosure"].update(prMustRemainDraft=False)),
      ("runtime",lambda x:x["runtime"].update(coreRpgIntegration=True)),
      ("next",lambda x:x.update(nextPhase="D.P22_STARTED"))]
    for name,change in edits:
        x=copy.deepcopy(d);change(x)
        try: validate(x,files=False)
        except AssertionError: continue
        raise AssertionError("adversarial mutation escaped: "+name)
    return len(edits)

if __name__=="__main__":
    d=read(DATA);validate(d)
    print("D.P21 Taramin CONTRACT PASS; negative mutations rejected:",mutation_test(d))
    print("PARTIAL AUTHOR APPROVAL: six popular names, city character, twelve future establishments and ten editorial biographies; no NPC, relationships, memories, buildings, geometry, runtime or merge.")

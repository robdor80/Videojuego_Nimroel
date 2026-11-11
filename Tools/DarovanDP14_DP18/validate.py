#!/usr/bin/env python3
"""Darovan D.P14-D.P18: documental cross-source guardrails. No production runtime."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
VALRIK = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Valrik"
DATA = TERR / "Datos operativos"
FILES = [
    "darovan_dp14_habitability_planning_v0.1.json",
    "darovan_dp15_settlement_service_network_v0.1.json",
    "darovan_dp16_city_functional_planning_v0.1.json",
    "darovan_dp17_conceptual_integration_v0.1.json",
    "darovan_dp18_territorial_closure_audit_v0.1.json",
]

def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def check(condition, message: str):
    if not condition:
        raise AssertionError(message)

def invariant(documents, sources, check_fs=True):
    a,b,c,d,e=documents
    d01,d05,d06,d07,d08,d09 = sources
    check([x["phase"] for x in documents] == ["D.P14","D.P15","D.P16","D.P17","D.P18"],
          "phase identity")
    check(all(x["schemaVersion"]==1 and x["version"]=="0.1.0" for x in documents),
          "document schema identity")
    check(all(x["status"] and "RUNTIME_READY" not in x["status"] for x in documents),
          "documents cannot assert running engine")
    zone_ids=[x["id"] for x in d01["physicalUnits"]]
    check(len(zone_ids)==12 and len(set(zone_ids))==12,"D01 source")
    check(len(a["orderedGates"])==10 and len(set(g["id"] for g in a["orderedGates"]))==10,
          "D.P14 ten ordered gates")
    check([x["id"] for x in a["orderedGates"]] ==
          ["authored_anchor","topography","water_supply","drainage_risk",
           "legal_land_use","accessibility","food_and_sustenance",
           "network_coverage","community","persistence"],"D.P14 gate sequence")
    check([x["studyUnitId"] for x in a["studyUnits"]]==zone_ids,"D.P14 zone universe")
    d6_zones={x["id"]:x for x in d06["zones"]}
    for z in a["studyUnits"]:
        key=z["studyUnitId"]
        check(z["d06ModelPriorities"]==d6_zones[key]["modelWeights"],
              "D.P14 weight unmodified: "+key)
        check(z["eligibleModelsAfterSiteProof"]==
              [m for m,v in d6_zones[key]["modelWeights"].items() if v>0],
              "D.P14 positive models must match D06: "+key)
        check(z["siteCoordinates"] is None and not z["eligiblePhysicalSlots"]
              and not z["actualSettlementIds"] and z["authorApprovedNewSite"] is False,
              "D.P14 cannot create site: "+key)
        check(all(z[k] is None for k in
             ("availableDrinkingWater","realLocalAccess","measuredSlope",
              "measuredFloodProbability")), "D.P14 no invented measurements "+key)
        check(z["planningResult"]=="UNDETERMINED_UNTIL_REAL_SITE_PROOF",
              "site cannot be asserted habitable "+key)
        if key=="d01_aguja_litoral":
            check(z["ifInsideAgujasPermanentResidenceAllowed"] is False
                  and z["eligibleModelsAfterSiteProof"]==[],
                  "Agujas interior non-residence")
    check(a["globalInvariants"]["fourManualCities"]==d06["manualCityIds"]
          and a["globalInvariants"]["forbiddenCityIds"]==["karsath"]
          and a["globalInvariants"]["forestAgujasNoPermanentResidents"] is True
          and a["globalInvariants"]["d06WeightsAreNotPercentages"] is True
          and a["globalInvariants"]["siteCanBeAuthorizedWithoutCoordinates"] is False
          and a["globalInvariants"]["physicalRouteCannotBeInferredFromSupply"] is True,
          "D.P14 legal and city protection")
    check(a["runtime"]=={"implemented":False,"worldStateModified":False,
                          "siteGeometryCreated":False},"D.P14 no runtime")
    for src in a["sourcePaths"]:
        if check_fs: check((ROOT/src).is_file(), "D.P14 missing source "+src)

    check(b["generationLayers"]==
          ["esqueleto_minimo","posibilidades","filtros_fisicos_ley_y_compatibilidad",
           "coherencia_regional","pesos_de_d06","seleccion_de_modelo",
           "instancia_y_persistencia"],"Valrik sequence preserved")
    check(len(b["availableModels"])==9 and
          [x["modelId"] for x in b["availableModels"]]==[x["id"] for x in d06["models"]],
          "D.P15 exact D06 model catalogue")
    for x,source in zip(b["availableModels"],d06["models"]):
        check(x["classes"]==source["classes"]
              and x["requiredEvidence"]==source["requiredEvidence"]
              and x["possibleBuildings"]==source["buildingPossibilities"]
              and x["possibleServices"]==source["servicePossibilities"]
              and x["actualInstanceCount"] is None
              and x["actualProviderIds"]==[]
              and not x["automaticBuildingCreation"] and not x["automaticServiceCreation"],
              "D.P15 no fabricated service/model "+x["modelId"])
    check(len(b["serviceNeeds"])==10
          and [x["needId"] for x in b["serviceNeeds"]]==[x["id"] for x in d08["serviceNeeds"]],
          "D.P15 D08 needs coverage")
    for x in b["serviceNeeds"]:
        check(x["actualProviderIds"]==[] and x["actualCapacity"] is None
              and x["unmetNeedPermitted"] is True,"D.P15 no magical provider")
    check(b["confirmedTransportLinkIds"]==[x["id"] for x in d05["confirmedTransportLinks"]],
          "D.P15 must not add physically proven links")
    check(b["cityManualIds"]==d06["manualCityIds"] and
          b["actualVillageIds"]==[] and b["newCanonicalTownNames"]==[]
          and b["linksMayNotBeEquatedToUniversalCivilRoads"] is True
          and b["populationRangesNotExactCensuses"] is True
          and b["travelTimesMinutes"] is None and
          b["realServiceNetworkGeometry"] is None and
          b["fullProviderCoverageAsserted"] is False,
          "D.P15 no fabricated network or demographics")
    check(b["runtime"]=={"implemented":False,"generatedSites":0,
                          "worldStateChanged":False},"D.P15 no runtime")
    if check_fs:
        check((ROOT/b["referenceValrikMethod"]).is_file(),"Valrik methodology path")
        for src in b["sourcePaths"]: check((ROOT/src).is_file(),"D.P15 source "+src)

    check(c["cityIds"]==d07["manualCityIds"]==["treihord","veldora","taramin","syvaris"],
          "D.P16 canonical city IDs")
    check(len(c["cities"])==4 and len(c["functionalGates"])==12,
          "D.P16 cities and functional gates")
    check(c["valrikFunctionalReference"]["cataloguedIndexedFolders"]==100
          and len(c["valrikFunctionalReference"]["catalog"])==100,
          "Treskal numbered catalogue known to include double 34")
    catalog=c["valrikFunctionalReference"]["catalog"]
    check(len(set(x["sourceFolder"] for x in catalog))==100
          and set(x["number"] for x in catalog)==set(range(1,100))
          and sum(x["number"]==34 for x in catalog)==2,
          "Valrik 99 indices and duplicated 34")
    check(all(x["localRulesCopied"] is False and
              x["darovanUrbanInstanceCreated"] is False for x in catalog),
          "Valrik cannot be cloned as Darovan")
    for city in c["cities"]:
        cid=city["cityId"]
        source=next(x for x in d07["cities"] if x["id"]==cid)
        demo=next(x for x in d08["cities"] if x["id"]==cid)
        gov=next(x for x in d09["localities"] if x["id"]==cid)
        check(city["cityManualOnly"] is True and
              city["sourceDesignStatus"]==source["designStatus"] and
              city["approvedCoreFacts"]==[x["id"] for x in source["facts"]],
              "D.P16 provenance cannot overwrite D07 "+cid)
        check(city["administrativeFunctionsAlreadyInD09"]==gov["functions"],
              "D.P16 administrative ownership "+cid)
        check(len(city["checksForFutureUrbanPlanning"])==12 and
              all(g["proof"]=="PENDING_SITE_AND_INSTITUTION_DATA"
                  for g in city["checksForFutureUrbanPlanning"]),
              "D.P16 does not fake completed functions")
        check(city["concreteCityPlanGeometry"] is None
              and city["citySectorPolygons"]==[]
              and city["newDistrictNames"]==[] and city["newBuildingIds"]==[]
              and city["cityStreetNetwork"] is None and
              city["marketServiceCapacities"] is None,
              "D.P16 no new buildings, districts or streets "+cid)
        if cid=="treihord":
            districts=next(f["value"] for f in source["facts"]
                           if f["id"]=="eight_approved_districts")
            check(city["canonicalDistrictNames"]==districts
                  and city["demographicReference"]=={"approx":32000},
                  "Treihord canon and population")
        else:
            check(city["canonicalDistrictNames"]==[]
                  and city["demographicReference"]==demo["populationRange"],
                  "D.P16 only exact author-approved range "+cid)
    check(all(c["neverInvented"][k]==[] for k in
           ("newCityIds","newDistricts","newQuays","newNavalFacilities",
            "newCrossings","newNamedStreets")),
          "No new urban identities by inheritance")
    check(all(v is False for v in c["runtime"].values()),"D.P16 no runtime")

    check(d["authorityOrder"]==
          ["nimroel_core","norgard_defaults","casa_darovan",
           "manual_city_or_settlement_instance","world_state"],
          "D.P17 authority")
    check(d["requiresCurrentContractVerification"] is True and
          d["reuseNamespaceCatalogue"] and len(d["reuseNamespaceCatalogue"])==57,
          "D.P17 Core reuse references")
    check(len(set(x["namespace"] for x in d["reuseNamespaceCatalogue"]))==57
          and all(x["darovanUniqueOverride"] is None
                  and x["currentlySimulatedByThisPhase"] is False
                  for x in d["reuseNamespaceCatalogue"]),
          "D.P17 never claim implemented namespaces")
    check([x["id"] for x in d["testOnlyScenarios"]]==
          ["DP17-T"+str(i).zfill(2) for i in range(1,25)],"D.P17 24 scenarios")
    check(all(x["status"]=="TEST_ONLY" and
              x["directWorldStateMutation"] is False
              and x["narrativeMayNotMutateState"] is True and
              x["output"]=="REQUIRE_EVIDENCE_OR_REJECT"
              and x["precondition"] and x["forbidden"]
              for x in d["testOnlyScenarios"]), "D.P17 scenario semantics")
    check(d["simulationClaims"]=={"implementedByThisPR":False,
          "compiledRuntimeAdapter":False,"realNpcSpawn":False,
          "realWorldStateWrites":False,"aiHasStateAuthority":False},
          "D.P17 no executed systems")
    check("no_private_darovan_navy" in d["authorialCanonProtections"] and
          "thalen_one_river_two_arms" in d["authorialCanonProtections"]
          and "fhalion_mouth_unknown" in d["authorialCanonProtections"]
          and "no_mint_in_treihord" in d["authorialCanonProtections"],
          "D.P17 protect canon")
    if check_fs: check((ROOT/d["valrikCoreExtractionMap"]).is_file(),
                        "Missing Valrik system extraction source")

    check(e["date"]=="2026-11-11" and len(e["deliverableMetrics"])==8,
          "D.P18 actual metrics")
    metrics={x["id"]:x["value"] for x in e["deliverableMetrics"]}
    check(metrics=={"twelveStudyUnits":12,"eligibilityGates":10,
          "settlementModels":9,"serviceNeeds":10,"manualCityPlans":4,
          "treskalIndexedFolders":100,"globalNamespaceCandidates":57,
          "testOnlyScenarios":24}, "D.P18 metrics grounded in files")
    check(len(e["unresolved"])==12 and
          [x["id"] for x in e["unresolved"]]==["P18-G"+str(i).zfill(2)
                                            for i in range(1,13)]
          and all(x["closed"] is False for x in e["unresolved"]),
          "D.P18 must expose twelve gaps")
    check(len(e["phaseStatuses"])==5 and
          all(x["runtime"] is False for x in e["phaseStatuses"]),
          "D.P18 phase not implemented")
    guard=e["projectGuard"]
    check(guard["authorDecisionsNotFabricated"] is True
          and guard["notEquivalentToValrik99LocalDetail"] is True
          and guard["treihordCanonicalDesignUntouched"] is True
          and guard["mayMergePr"] is False and
          guard["nextHouseNotStarted"] is True
          and guard["worldStateMutations"]==0
          and all(guard[k]==[] for k in
               ("newCanonicalCities","newCanonicalDistricts","newRoads","newRivers")),
          "D.P18 no false complete/fusion/new canon")
    check(e["technicalValidation"]["githubActionsFinalResult"] is None and
          e["technicalValidation"]["executedEngineValidation"] is False,
          "D.P18 cannot pre-certify CI or runtime")
    if check_fs:
        for path in [
            "Profundizacion_2026/PLAN_DP14_DP18_2026-11-11.md",
            "Profundizacion_2026/D.P14/01_habitabilidad_y_diez_puertas.md",
            "Profundizacion_2026/D.P15/01_coherencia_regional_servicios_y_asentamientos.md",
            "Profundizacion_2026/D.P15/02_cobertura_causal_y_limitaciones.md",
            "Profundizacion_2026/D.P16/01_auditoria_funcional_99_capas_treskal_y_cuatro_ciudades.md",
            "Profundizacion_2026/D.P17/01_interfaces_causalidad_persistencia_y_24_escenarios.md",
            "Profundizacion_2026/D.P18/01_auditoria_comparada_y_deuda_real.md",
            "Profundizacion_2026/D.P18/02_precondiciones_cartograficas.md",
            "Profundizacion_2026/README.md"]:
            check((TERR/path).is_file(),"Missing report "+path)
        for city in ["treihord","veldora","taramin","syvaris"]:
            check((TERR/f"Profundizacion_2026/D.P16/ciudad_{city}_plan_funcional_condicionado.md").is_file(),
                  "City report missing "+city)

def negative_checks(data,source):
    edits = []
    def add(label,idx,fn):
        edits.append((label,idx,fn))
    add("dp14_remove_zone",0,lambda d:d["studyUnits"].pop())
    add("dp14_wrong_zone",0,lambda d:d["studyUnits"][0].__setitem__("studyUnitId","wrong"))
    add("dp14_wrong_weight",0,lambda d:d["studyUnits"][0]["d06ModelPriorities"].__setitem__("minera_auxiliar",0))
    add("dp14_fabricated_site",0,lambda d:d["studyUnits"][0]["eligiblePhysicalSlots"].append("invented"))
    add("dp14_fabricated_coordinates",0,lambda d:d["studyUnits"][0].__setitem__("siteCoordinates",[1,2]))
    add("dp14_fabricated_population",0,lambda d:d["studyUnits"][0]["actualSettlementIds"].append("village-new"))
    add("dp14_auto_permission",0,lambda d:d["studyUnits"][0].__setitem__("authorApprovedNewSite",True))
    add("dp14_fabricated_water",0,lambda d:d["studyUnits"][0].__setitem__("availableDrinkingWater",True))
    add("dp14_fabricated_slope",0,lambda d:d["studyUnits"][0].__setitem__("measuredSlope",1))
    add("dp14_fabricated_flood",0,lambda d:d["studyUnits"][0].__setitem__("measuredFloodProbability",.1))
    add("dp14_aguja_residents",0,lambda d:d["studyUnits"][3].__setitem__("ifInsideAgujasPermanentResidenceAllowed",True))
    add("dp14_aguja_model",0,lambda d:d["studyUnits"][3]["eligibleModelsAfterSiteProof"].append("agricola"))
    add("dp14_wrong_city_list",0,lambda d:d["globalInvariants"]["fourManualCities"].append("new_city"))
    add("dp14_weight_percent",0,lambda d:d["globalInvariants"].__setitem__("d06WeightsAreNotPercentages",False))
    add("dp14_false_runtime",0,lambda d:d["runtime"].__setitem__("implemented",True))
    add("dp15_model_count",1,lambda d:d["availableModels"].pop())
    add("dp15_model_right",1,lambda d:d["availableModels"][0]["requiredEvidence"].clear())
    add("dp15_auto_shop",1,lambda d:d["availableModels"][0].__setitem__("automaticBuildingCreation",True))
    add("dp15_fabricated_village",1,lambda d:d["actualVillageIds"].append("impossible"))
    add("dp15_fabricated_town",1,lambda d:d["newCanonicalTownNames"].append("Pueblo de la Prueba"))
    add("dp15_provider",1,lambda d:d["serviceNeeds"][0]["actualProviderIds"].append("made-up"))
    add("dp15_service_capacity",1,lambda d:d["serviceNeeds"][0].__setitem__("actualCapacity",40))
    add("dp15_unmet_need_not_allowed",1,lambda d:d["serviceNeeds"][0].__setitem__("unmetNeedPermitted",False))
    add("dp15_new_road",1,lambda d:d["confirmedTransportLinkIds"].append("invented_road"))
    add("dp15_all_to_all_roads",1,lambda d:d.__setitem__("linksMayNotBeEquatedToUniversalCivilRoads",False))
    add("dp15_fabricated_travel",1,lambda d:d.__setitem__("travelTimesMinutes",20))
    add("dp15_fake_full_coverage",1,lambda d:d.__setitem__("fullProviderCoverageAsserted",True))
    add("dp15_false_runtime",1,lambda d:d["runtime"].__setitem__("generatedSites",10))
    add("dp16_extra_city",2,lambda d:d["cityIds"].append("extra_city"))
    add("dp16_city_missing",2,lambda d:d["cities"].pop())
    add("dp16_new_district",2,lambda d:d["cities"][1]["newDistrictNames"].append("Nuevo"))
    add("dp16_new_street",2,lambda d:d["neverInvented"]["newNamedStreets"].append("Inventada"))
    add("dp16_new_military",2,lambda d:d["neverInvented"]["newNavalFacilities"].append("Base"))
    add("dp16_city_geometry",2,lambda d:d["cities"][2].__setitem__("concreteCityPlanGeometry",{}))
    add("dp16_wrong_treihord",2,lambda d:d["cities"][0]["canonicalDistrictNames"].pop())
    add("dp16_wrong_veldora_population",2,lambda d:d["cities"][1]["demographicReference"].__setitem__("maxInclusive",50000))
    add("dp16_valrik_clone",2,lambda d:d["valrikFunctionalReference"]["catalog"][0].__setitem__("localRulesCopied",True))
    add("dp16_catalog_missing",2,lambda d:d["valrikFunctionalReference"]["catalog"].pop())
    add("dp16_live_worldstate",2,lambda d:d["runtime"].__setitem__("coreCityEntityInstantiated",True))
    add("dp17_no_authority",3,lambda d:d["authorityOrder"].reverse())
    add("dp17_namespace_missing",3,lambda d:d["reuseNamespaceCatalogue"].pop())
    add("dp17_local_duplicate",3,lambda d:d["reuseNamespaceCatalogue"][0].__setitem__("darovanUniqueOverride","wrong"))
    add("dp17_scenario_deleted",3,lambda d:d["testOnlyScenarios"].pop())
    add("dp17_scenario_not_test",3,lambda d:d["testOnlyScenarios"][0].__setitem__("status","AUTHORED"))
    add("dp17_ai_mutates",3,lambda d:d["testOnlyScenarios"][0].__setitem__("narrativeMayNotMutateState",False))
    add("dp17_false_ship",3,lambda d:d["authorialCanonProtections"].remove("no_private_darovan_navy"))
    add("dp17_simulation_claim",3,lambda d:d["simulationClaims"].__setitem__("implementedByThisPR",True))
    add("dp17_ai_authority",3,lambda d:d["simulationClaims"].__setitem__("aiHasStateAuthority",True))
    add("dp18_gap_closed",4,lambda d:d["unresolved"][0].__setitem__("closed",True))
    add("dp18_gap_removed",4,lambda d:d["unresolved"].pop())
    add("dp18_overclaim_valrik",4,lambda d:d["projectGuard"].__setitem__("notEquivalentToValrik99LocalDetail",False))
    add("dp18_unapproved_merge",4,lambda d:d["projectGuard"].__setitem__("mayMergePr",True))
    add("dp18_fake_new_road",4,lambda d:d["projectGuard"]["newRoads"].append("road"))
    add("dp18_fake_ci",4,lambda d:d["technicalValidation"].__setitem__("githubActionsFinalResult","SUCCESS"))
    add("dp18_fake_runtime",4,lambda d:d["technicalValidation"].__setitem__("executedEngineValidation",True))
    add("dp18_incorrect_metric",4,lambda d:d["deliverableMetrics"][0].__setitem__("value",99))
    for label,index,mut in edits:
        changed=copy.deepcopy(data)
        mut(changed[index])
        try:
            invariant(changed,source,check_fs=False)
        except AssertionError:
            continue
        raise AssertionError("Negative mutation was accepted: "+label)
    return len(edits)

def validate_valrik_triage():
    r=read(DATA/"darovan_dp16_valrik_functional_coverage_v0.1.json")
    check(r["schemaVersion"] == 1 and r["phase"] == "D.P16"
          and r["documentId"] == "darovan_dp16_valrik_functional_coverage_triage_v0.1"
          and r["authority"] == "ASSISTANT_DESIGN_TRIAGE_NOT_CANON",
          "Valrik 99-layer triage authority")
    entries=r["referenceLayers"]
    check(r["folderCount"]==len(entries)==100
          and r["distinctNumericIndices"]==99
          and r["duplicatedNumericIndex"]==34,
          "Triage source counts")
    check(len(set(x["sourceFolder"] for x in entries))==100
          and set(x["number"] for x in entries)==set(range(1,100))
          and sum(x["number"]==34 for x in entries)==2,
          "Valrik numbering sanity")
    check(sum(r["categoryCounts"].values())==100
          and {k:sum(x["triage"]==k for x in entries)
               for k in r["categoryCounts"]}==r["categoryCounts"],
          "Every folder classified")
    check(all(not x["canonicalDarovanFactCreated"]
              and x["requiresManualCityReview"]
              and not x["localRulesCopied"]
              and not x["darovanUrbanInstanceCreated"]
              for x in entries), "No Treskal local canon copied")
    flows=r["cityFunctionalFlows"]
    check(len(flows)==13 and len(set(f["id"] for f in flows))==13,
          "Thirteen functional chains")
    check({x["place"] for x in flows}=={"Treihord","Veldora","Taramin","Syvaris","Arven"},
          "Coverage of 4 cities and Arven")
    check(all(x["status"]=="FUNCTIONAL_CONCEPT_ONLY"
              and not x["createsSpatialRoute"]
              and not x["createsCanonicalInfrastructure"]
              and len(x["requiredProof"])>20
              and len(x["forbidden"])>10 for x in flows),
          "No physical network or building inferred")
    check(r["cityIds"]==["treihord","veldora","taramin","syvaris"]
          and r["noNewRoads"]==[] and r["noNewNeighborhoods"]==[]
          and r["noNewBuildings"]==[] and r["noWorldStateRuntime"] is True,
          "City boundary and no-runtime triage")
    check((ROOT/r["sourcePath"]).is_dir(), "Valrik reference root")
    for entry in entries:
        check((ROOT/r["sourcePath"]/entry["sourceFolder"]).is_dir(),
              "Unverified Treskal folder "+entry["sourceFolder"])
    check((TERR/"Profundizacion_2026/D.P16/02_99_capas_triado_y_13_cadenas_darovan.md").is_file(),
          "Triage report absent")
    edits=[
      ("invented_city",lambda d:d["cityIds"].append("new_city")),
      ("invented_road",lambda d:d["noNewRoads"].append("road")),
      ("invented_neighborhood",lambda d:d["noNewNeighborhoods"].append("new")),
      ("invented_building",lambda d:d["noNewBuildings"].append("new")),
      ("fake_worldstate",lambda d:d.__setitem__("noWorldStateRuntime",False)),
      ("missing_treskal_layer",lambda d:d["referenceLayers"].pop()),
      ("duplicate_layer",lambda d:d["referenceLayers"][0].__setitem__("sourceFolder","fake")),
      ("cloned_local_canon",lambda d:d["referenceLayers"][0].__setitem__("localRulesCopied",True)),
      ("made_up_local_fact",lambda d:d["referenceLayers"][0].__setitem__("canonicalDarovanFactCreated",True)),
      ("made_up_category_count",lambda d:d["categoryCounts"].__setitem__("LOCAL_SPACE_AND_SITE_PROOF",999)),
      ("removed_function",lambda d:d["cityFunctionalFlows"].pop()),
      ("materialized_road",lambda d:d["cityFunctionalFlows"][0].__setitem__("createsSpatialRoute",True)),
      ("materialized_installation",lambda d:d["cityFunctionalFlows"][0].__setitem__("createsCanonicalInfrastructure",True)),
      ("pretend_authored",lambda d:d.__setitem__("authority","AUTHORED"))
    ]
    for label,change in edits:
        changed=copy.deepcopy(r)
        change(changed)
        try:
            # The same structural rules, without evaluating file system on mutation.
            rows=changed["referenceLayers"]
            check(changed["schemaVersion"]==1 and
                  changed["authority"]=="ASSISTANT_DESIGN_TRIAGE_NOT_CANON",
                  "mutated triage authority")
            check(changed["cityIds"]==["treihord","veldora","taramin","syvaris"]
                  and not changed["noNewRoads"] and not changed["noNewNeighborhoods"]
                  and not changed["noNewBuildings"]
                  and changed["noWorldStateRuntime"] is True,
                  "mutated forbidden addition")
            check(len(rows)==100 and len(set(x["sourceFolder"] for x in rows))==100
                  and all((ROOT/changed["sourcePath"]/x["sourceFolder"]).is_dir()
                          for x in rows), "mutated reference integrity")
            check(all(not x["localRulesCopied"] and not x["canonicalDarovanFactCreated"]
                      and not x["darovanUrbanInstanceCreated"] for x in rows),
                  "mutated canon")
            check(sum(changed["categoryCounts"].values())==100 and
                  {k:sum(x["triage"]==k for x in rows)
                   for k in changed["categoryCounts"]}==changed["categoryCounts"],
                  "mutated classification")
            fs=changed["cityFunctionalFlows"]
            check(len(fs)==13 and
                  all(not f["createsSpatialRoute"] and
                      not f["createsCanonicalInfrastructure"] for f in fs),
                  "mutated flow")
        except AssertionError:
            continue
        raise AssertionError("Triage negative mutation accepted "+label)
    return len(edits)

def main():
    documents=[read(DATA/f) for f in FILES]
    source=[read(DATA/f) for f in (
        "darovan_d01_relief_profile_v0.1.json",
        "darovan_d05_mobility_communications_v0.1.json",
        "darovan_d06_settlement_rules_v0.1.json",
        "darovan_d07_canonical_cities_v0.1.json",
        "darovan_d08_population_services_v0.1.json",
        "darovan_d09_governance_security_v0.1.json")]
    invariant(documents,source,check_fs=True)
    count=negative_checks(documents,source)
    triage_count=validate_valrik_triage()
    print("DAROVAN D.P14-D.P18 STATIC OK: 12 study units, 10 gates, "
          "9 D06 models, 10 needs, 4 manual cities, 100 Treskal 01-99 folders, "
          "57 source namespaces, 24 TEST_ONLY scenarios, "
          f"12 explicit gaps, {count+triage_count} negative mutations; NO RUNTIME")

if __name__=="__main__":
    main()

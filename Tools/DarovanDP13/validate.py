#!/usr/bin/env python3
"""D.P13 Darovan: cobertura física, canon protegido, consistencia y mutaciones negativas.
No ejecuta motor, no inventa geometría ni corrige documentos históricos.
"""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan"
DATA = TERR / "Datos operativos"
RIVERS = ["belara","lhera","veldora","fhalion","thalen"]
SYSTEMS = ["belara_lhera","veldora","fhalion","thalen"]
ZONES = ["d01_valkram_oeste","d01_elyra_paso_peninsular","d01_norte_transicion","d01_aguja_litoral",
         "d01_belara_treihord","d01_veldora_litoral","d01_linde_caminos","d01_pilares_sur",
         "d01_taramin_norte_centro","d01_taramin_bosque_sur","d01_syvaris","d01_arven_contexto"]
TOPICS = ["canon","landform","topology","hydro","temp","precip","snow","wind","fog",
          "soil","vegetation","season","risk","settlement"]
EXPECTED_DOCS = ["00_comparacion_fuentes_y_metodo.md","01_regiones_y_subzonas.md",
                 "02_relieve_y_microrelieve.md","03_cuencas_y_agua_menor.md",
                 "04_temperatura_y_estaciones.md","05_lluvia_nieve_y_deshielo.md",
                 "06_viento_humedad_niebla.md","07_suelos_drenaje_erosion.md",
                 "08_bosques_vegetacion_ecosistemas.md","09_inferencia_causal_y_persistencia.md",
                 "10_contratos_y_validacion.md","11_auditoria_suficiencia.md","README.md"]
def demand(ok, reason):
    if not ok:
        raise AssertionError(reason)

def load(p):
    return json.loads(p.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate)

def no_duplicate(pairs):
    out = {}
    for k,v in pairs:
        demand(k not in out, "duplicate JSON key "+k)
        out[k]=v
    return out

def validate(profiles, hydro, causal, d01, d02, d03, *, check_fs=True):
    demand(profiles["schemaVersion"] == hydro["schemaVersion"] == causal["schemaVersion"] == 1,"schema")
    demand(profiles["status"] == hydro["status"] == "derived_design_not_runtime","planning")
    demand(causal["status"] == "documented_not_executed","not executed")
    demand(not profiles["canonMutation"] and not hydro["canonMutation"],"new canon flag")
    for flag in ("containsCoordinates","containsElevations","containsMeasuredClimate",
                 "containsNamedMinorChannels","containsSettlementInstances"):
        demand(profiles[flag] is False, "invented feature "+flag)
    for flag in ("containsGeometry","containsNamedMinorRivers","containsNavigabilityClaims"):
        demand(hydro[flag] is False,"invention "+flag)
    demand(profiles["unitType"] == "qualitative_study_unit_not_polygon","fake polygons")
    demand(profiles["authorityChain"] == causal["authorityChain"] ==
           ["nimroel_core","norgard_defaults","casa_darovan","locality","world_state"],"authority")
    demand(profiles["sourceHierarchy"] == ["AUTHORED","DERIVED_CONDITIONAL",
           "PROPOSAL_PENDING_AUTHOR","GENERATED_TEST_ONLY","UNKNOWN"],"provenance")
    old_ids = [x["id"] for x in d01["physicalUnits"]]
    demand(old_ids == ZONES and [z["id"] for z in profiles["zones"]] == ZONES,"D01 units")
    demand([z["id"] for z in d03["zones"]] == ZONES,"D03 ids")
    demand(len(set(old_ids))==12,"duplicates")
    protection=profiles["existingCanons"]
    demand(protection["cities"] == ["treihord","veldora","taramin","syvaris"],"cities")
    demand(protection["excludedCity"] == "karsath" and protection["arvenOwner"] == "casa_darovan","admin")
    demand(protection["majorRivers"] == RIVERS and protection["systems"] == SYSTEMS,"rivers")
    demand(protection["agujaPermanentSettlements"] is False
           and protection["pilaresSingleForest"] is True and protection["taraminSingleForest"] is True
           and protection["syvarisDiscontinuousForest"] is True,"forests")
    demand(hydro["canonicalRivers"] == RIVERS
           and [s["id"] for s in hydro["systems"]] == SYSTEMS,"hydrology schema")
    demand([r["id"] for r in d02["rivers"]] == RIVERS
           and [s["id"] for s in d02["systems"]] == SYSTEMS,"D02 source")
    h={s["id"]:s for s in hydro["systems"]}
    demand(h["belara_lhera"]["riverIds"] == ["belara","lhera"] and
           h["belara_lhera"]["canonicalOutlets"] == ["golfo_de_norgard","golfo_de_veldora"] and
           h["belara_lhera"]["authorizedSplit"]=="belara_to_lhera","Belara-Lhera")
    demand(h["veldora"]["riverIds"]==["veldora"] and h["veldora"]["canonicalOutlets"]==["golfo_de_veldora"]
           and h["veldora"]["authorizedSplit"] is None,"Veldora independence")
    demand(h["fhalion"]["riverIds"]==["fhalion"] and h["fhalion"]["canonicalOutlets"]==[],"Fhalion unknown mouth")
    demand(h["thalen"]["riverIds"]==["thalen"] and h["thalen"]["canonicalOutlets"]==["golfo_de_norgard"]
           and h["thalen"]["authorizedSplit"]=="two_terminal_arms_around_taramin","Thalen two arms")
    guard=hydro["topologyGuards"]
    demand(guard["belaraAdjacentTreihord"] is True and guard["belaraCrossesTreihord"] is False
           and guard["lheraBranchesFrom"]=="belara","Treihord")
    demand(guard["veldoraConnectedToBelaraLhera"] is False and guard["fhalionMouth"]=="UNKNOWN"
           and guard["thalenTerminalArms"]==2 and guard["taraminBetweenArms"] is True,"river topology")
    demand(guard["namedMinorRiverCount"]==0 and guard["bridgesOrFordsCreated"]==0,"new river/bridge")
    demand(len(hydro["candidateProfiles"])==12 and
           [c["studyUnitId"] for c in hydro["candidateProfiles"]]==ZONES,"hydro zones")
    demand(all(c["assignedBasin"] is None and c["geometry"] is None and
               c["featureInstances"]==[] and c["status"]=="DERIVED_CONDITIONAL"
               for c in hydro["candidateProfiles"]),"hydro candidate != existing river")
    demand(set(hydro["minorFeatureTypes"]) == {"minor_perennial_channel_candidate",
           "seasonal_channel_candidate","ephemeral_channel_candidate","spring_candidate",
           "wetland_candidate"},"hydro candidates")
    demand(len(hydro["mandatoryInputs"])>=5 and "valid_downstream_receiver" in hydro["mandatoryInputs"],"hydro causal")
    for z in profiles["zones"]:
        demand(z["designStatus"]=="DERIVED_CONDITIONAL" and all(z[k] is None for k in (
               "altitudeMeters","temperatureC","precipitationMm","dominantWindAzimuth",
               "soilTaxon","geometry","administrativeBoundary")),"zone measurements")
        demand(all(isinstance(z[k],str) and len(z[k])>=35 for k in TOPICS),"shallow zone profile")
        demand(bool(z["sourcePaths"]) and len(set(z["sourcePaths"]))==len(z["sourcePaths"]),"source paths")
        if check_fs:
            for p in z["sourcePaths"]:
                demand(p.startswith("Worldbuilding/") and (ROOT/p).is_file(),"missing source "+p)
    demand(profiles["runtime"]=={"implementedInCoreRPG":False,"implementedInGodot":False,
                                 "persistentObjectsCreated":0},"fake runtime")
    demand(hydro["runtime"]=={"implemented":False,"generatedSegments":0,
                                "persistedWorldState":False},"fake river implementation")
    demand(all(x is False for x in causal["noClaims"].values()),"fake environmental implementation")
    demand(len(causal["rules"])==10 and len({r["id"] for r in causal["rules"]})==10,"causality rules")
    demand(all(r["cause"] and r["effect"] and r["requires"] and r["unknownFallback"]
               for r in causal["rules"]),"causal rule missing dependency")
    demand(len(causal["negativeCases"])==8 and
           len({x["id"] for x in causal["negativeCases"]})==8,"negative fixtures")
    demand(causal["futureEntityContract"]["writeAuthority"]=="corerpg_only_when_implemented"
           and causal["futureEntityContract"]["generatorVersionRequired"] is True
           and causal["futureEntityContract"]["seedRequired"] is True,"persistence versioning")
    demand(len(set(causal["persistedFieldsProposed"]))>=7,"state fields")
    if check_fs:
        demand(all((TERR/"D.P13"/p).is_file() for p in EXPECTED_DOCS),"docs missing")
        for p in profiles["sources"].values():
            demand(p.startswith("Worldbuilding/") and (ROOT/p).is_file(),"bad primary source "+p)
        for p in hydro["sources"]:
            demand((ROOT/p).is_file(),"hydro source absent")

def validate_authorial_altitudes(record):
    demand(record["schemaVersion"] == 1 and record["authority"] == "AUTHORED_AUTHOR_DECISION","alt authority")
    demand(record["decisionIds"] == ["DAR-DP13-ALT-01","DAR-DP13-ALT-02","DAR-DP13-ALT-03","DAR-DP13-SNOW-01","DAR-DP13-PASS-01"],"author decisions")
    rg=record["rangeDefinition"]
    demand(rg["mountainRange"] == "Montes Valkram" and rg["option"] == "B","mountain range choice")
    demand(rg["representativeMajorSummitBandMetersApprox"] == {"min":3600,"max":4200},"peak band")
    p=record["worldHighestSummit"]
    demand(p["mountainRange"] == "Montes Valkram" and p["sector"] == "northern","summit sector")
    demand(p["altitudeMetersApprox"] == 4200 and p["approximation"] is True and p["highestInNorgard"] is True,"absolute high point")
    demand("entre las letras N y O" in p["mapLocator"],"visual map anchor")
    demand(p["officialToponym"] == "la Viuda" and p["toponymAuthority"] == "AUTHORED_AUTHOR_DECISION" and p["toponymApprovedDate"] == "2026-10-25","official authorial summit name")
    demand(p["coordinates"] is None and p["administrativeOwnership"] is None and p["etymology"] is None,"no fabricated location or origin")
    demand(all(p[k] is None for k in ("exactElevationMeasurement","climateConditions","glacierPresence")),"unknown mountain conditions")
    demand(p["snowPersistence"] == "localized_perennial_snow_patches","approved snow persistence")
    snow=p["snowPersistenceDetail"]
    demand(snow["authorChoice"] == "B" and snow["authorDecisionDate"] == "2026-10-25"
           and snow["authority"] == "AUTHORED_AUTHOR_DECISION","snow author decision")
    demand(snow["appliesTo"] == "la Viuda only; upper and sheltered sections"
           and snow["survivesSummer"] is True and snow["continuousBlanketOverEntireSummit"] is False,
           "localized summer snow")
    demand(all(snow[k] is None for k in ("fixedSnowlineMeters","fixedSnowpatchGeometry",
                                         "coveragePercentage","snowmeltAmountOrTiming")),"no fabricated snow measurements")
    demand(snow["glacierExistenceDetermined"] is False and
           snow["glacierAuthorizationInThisDecision"] is False and p["glacierPresence"] is None,
           "no glacier conclusion")
    demand(record["limits"]["permanentSnow"] == "localized_perennial_snow_patches_confirmed_only_on_la_Viuda",
           "snow restriction scope")
    pas=record["principalNaturalPasses"]
    demand(pas["authorDecisionId"] == "DAR-DP13-PASS-01" and pas["authorChoice"] == "B"
           and pas["authority"] == "AUTHORED_AUTHOR_DECISION"
           and pas["authorDecisionDate"] == "2026-10-25","pass author decision")
    demand(pas["mountainRange"] == "Montes Valkram" and
           pas["approximateElevationBandMeters"] == {"min":1400,"max":2200}
           and pas["bandAppliesTo"] == "principal_natural_passes_as_typological_reference","pass elevations")
    demand(pas["namesApproved"] == [] and pas["geographicPassLocations"] == []
           and pas["exactPassElevations"] == [] and pas["exactNumberOfPasses"] is None
           and pas["establishedRoadsOrBridges"] == [] and pas["seasonalClosureDates"] is None,
           "no named passes, fixed positions, closures or infrastructure")
    demand(pas["guaranteesYearRoundTransit"] is False and
           pas["createsPassInstances"] is False and pas["measuredGeoreferencedTerrain"] is False,
           "passes not materialized")
    demand(record["limits"]["passElevations"] ==
           "general_principal_natural_pass_band_1400_to_2200_m_authorized_individual_pass_elevations_unknown",
           "pass authority scope")
    demand(record["limits"]["cartographicReferenceIsGeoreferenced"] is False
           and record["limits"]["topographicRuntimeMaterialized"] is False,"not GIS/runtime")
    demand(record["crossCanon"]["harmonizationPendingAtNorgardScope"] is True
           and record["crossCanon"]["superiorCanonFileModified"] is False,"superior document guard")
    demand(record["generatedFeatures"] == [] and record["runtime"] == {"implemented":False,"geometryGenerated":False},"altitude runtime")

def validate_elyra_authorial(record):
    demand(record["schemaVersion"] == 1 and record["documentId"] == "darovan_dp13_elyra_altitude_authorial","elyra schema")
    demand(record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["decisionId"] == "DAR-DP13-ALT-04","elyra author approval")
    demand(record["mountainRange"] == "Montañas Elyra" and record["selectedOption"] == "A","elyra option")
    demand(record["majorSummitsApproximateUpperElevationMeters"] == 2600
           and record["approvedNumberIsMeasuredSurvey"] is False,"elyra peak ceiling")
    demand(all(record[x] is None for x in
           ["exactPeakElevationMeters","officialHighestPeakName","georeferencedPeakPosition",
            "specificPassElevations","exactValleyElevations","glacierPresence",
            "permanentSnow","georeferencedMountainGeometry"]),"elyra uncertainty")
    demand(record["relativeCanon"] == {"valkramHighestSummitName":"la Viuda",
           "valkramHighestSummitApproxMeters":4200,"elyraLowerThanValkram":True},"relative canon")
    demand(record["runtime"] == {"implemented":False,"terrainGeometryCreated":False},"elyra runtime")

def validate_treihord_authorial(record):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_treihord_elevation_authorial",
           "treihord schema")
    demand(record["authorDecisionId"] == "DAR-DP13-CITY-ALT-01"
           and record["authorDecisionDate"] == "2026-10-25"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["status"] == "AUTHORED_AUTHOR_DECISION_NOT_GEOMETRY",
           "treihord author decision")
    demand(record["settlementId"] == "treihord" and
           record["type"] == "canonical_city" and
           record["role"] == "darovan_capital" and
           record["selectedOption"] == "A",
           "treihord identity and option")
    demand(record["urbanAltitudeReferenceBandMetersApprox"] == {"min":150,"max":350}
           and record["referenceType"] == "approximate_general_urban_site_not_every_district",
           "treihord elevation band")
    demand(all(record[k] is None for k in
           ("urbanAltitudeSingleValueMeters","cityCenterCoordinates",
            "elevationOfBelaraAtPortMeters","dockLevelMeters",
            "embankmentSlopePercent","cadastralOrStreetTopography","terrainElevationRaster"))
           and record["neighborhoodElevations"] == [],"no invented city measurements")
    demand("sin ser atravesada por el río" in record["autoralAnchorNotes"][0]
           and "poco calado" in record["autoralAnchorNotes"][1],
           "Belara and shallow-draft port canon")
    demand(record["worldStateRuntimeImplemented"] is False
           and record["mapGeoreferenced"] is False
           and record["createsNewInfrastructure"] is False
           and record["legacyPhaseFilesModified"] is False,
           "no infrastructure/runtime/legacy rewrite")
    demand(len(record["sourcePaths"]) >= 3,"treihord provenance")

def validate_veldora_authorial(record, d01, d07):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_veldora_elevation_authorial",
           "Veldora schema")
    demand(record["authorDecisionId"] == "DAR-DP13-CITY-ALT-02" and
           record["authorDecisionDate"] == "2026-10-25" and
           record["authority"] == "AUTHORED_AUTHOR_DECISION" and
           record["status"] == "AUTHORED_AUTHOR_DECISION_NOT_GEOMETRY",
           "Veldora author decision")
    demand(record["settlementId"] == "veldora" and
           record["type"] == "canonical_city" and
           record["role"] == "darovan_primary_commercial_seaport" and
           record["selectedOption"] == "B","Veldora identity and option")
    demand(record["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":150}
           and record["referenceType"] == "approximate_general_coastal_urban_site_not_every_street",
           "Veldora urban elevation range")
    demand(all(record[k] is None for k in
           ("urbanAltitudeSingleValueMeters","cityCenterCoordinates","portDockElevationsMeters",
            "coastlineCoordinates","quayPositions","tidalRangeMeters","shorelineSlopePercent",
            "riverBehindCityIdentity","riverMouthToCityGeometry","terrainElevationRaster",
            "cadastralOrStreetTopography")) and record["neighborhoodElevations"] == [],
           "Veldora invented measurement, district or river identity")
    demand("principal puerto comercial marítimo" in record["autoralAnchorNotes"][0] and
           "no queda identificado" in record["autoralAnchorNotes"][3] and
           "dos ríos canónicos distintos" in record["autoralAnchorNotes"][4],
           "Veldora coastal and river guards")
    demand(record["worldStateRuntimeImplemented"] is False and
           record["mapGeoreferenced"] is False and
           record["createsNewInfrastructure"] is False and
           record["changesCanonicalRivers"] is False and
           record["createsNewDistricts"] is False and
           record["legacyPhaseFilesModified"] is False,"Veldora no new terrain")
    demand([c["id"] for c in d01["cityAnchors"] if c["id"] == "veldora"] == ["veldora"],
           "D01 Veldora identity")
    demand(d07["manualCityIds"] == ["treihord","veldora","taramin","syvaris"] and
           d07["excludedCityIds"] == ["karsath"],"D07 canonical cities")
    for p in record["sourcePaths"]:
        demand((ROOT/p).is_file(),"Veldora source missing "+p)
    demand((TERR/"D.P13"/"15_altitud_veldora_autorizada.md").is_file(),
           "Veldora decision document missing")

def run():
    veldora=load(DATA/"darovan_dp13_veldora_elevation_authorial_v0.1.json")
    vd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    vd07=load(DATA/"darovan_d07_canonical_cities_v0.1.json")
    validate_veldora_authorial(veldora,vd01,vd07)
    veldora_mutations=[
      ("veldora_wrong_city",lambda d:d.__setitem__("settlementId","treihord")),
      ("veldora_wrong_option",lambda d:d.__setitem__("selectedOption","A")),
      ("veldora_wrong_min",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("min",30)),
      ("veldora_wrong_max",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",250)),
      ("veldora_invented_port_height",lambda d:d.__setitem__("portDockElevationsMeters",2)),
      ("veldora_fake_city_height",lambda d:d.__setitem__("urbanAltitudeSingleValueMeters",50)),
      ("veldora_named_back_river",lambda d:d.__setitem__("riverBehindCityIdentity","lhera")),
      ("veldora_fake_tide",lambda d:d.__setitem__("tidalRangeMeters",1.8)),
      ("veldora_new_breakwater",lambda d:d.__setitem__("createsNewInfrastructure",True)),
      ("veldora_connect_rivers",lambda d:d.__setitem__("changesCanonicalRivers",True)),
      ("veldora_new_districts",lambda d:d.__setitem__("createsNewDistricts",True)),
      ("veldora_false_georeference",lambda d:d.__setitem__("mapGeoreferenced",True)),
      ("veldora_fake_runtime",lambda d:d.__setitem__("worldStateRuntimeImplemented",True)),
      ("veldora_made_up_street",lambda d:d["neighborhoodElevations"].append({"name":"Barrio inventado","height":120})),
    ]
    for label,change in veldora_mutations:
        tmp=copy.deepcopy(veldora)
        change(tmp)
        try:
            validate_veldora_authorial(tmp,vd01,vd07)
        except AssertionError:
            continue
        raise AssertionError("Veldora negative mutation accepted "+label)
    treihord=load(DATA/"darovan_dp13_treihord_elevation_authorial_v0.1.json")
    validate_treihord_authorial(treihord)
    treihord_mutations=[
      ("wrong_city",lambda d:d.__setitem__("settlementId","veldora")),
      ("wrong_altitude_min",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("min",350)),
      ("wrong_altitude_max",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",600)),
      ("assigned_center_height",lambda d:d.__setitem__("urbanAltitudeSingleValueMeters",250)),
      ("invented_district_height",lambda d:d["neighborhoodElevations"].append({"district":"Los Altos","elevation":320})),
      ("invented_river_level",lambda d:d.__setitem__("elevationOfBelaraAtPortMeters",180)),
      ("invented_belara_cross_city",lambda d:d["autoralAnchorNotes"].__setitem__(0,"El Belara cruza la ciudad")),
      ("invented_bridge",lambda d:d.__setitem__("createsNewInfrastructure",True)),
      ("fake_runtime",lambda d:d.__setitem__("worldStateRuntimeImplemented",True)),
      ("fake_gis",lambda d:d.__setitem__("mapGeoreferenced",True))
    ]
    for label,change in treihord_mutations:
        test=copy.deepcopy(treihord)
        change(test)
        try:
            validate_treihord_authorial(test)
        except AssertionError:
            continue
        raise AssertionError("Treihord negative test failed to reject "+label)
    demand((TERR/"D.P13"/"14_altitud_treihord_autorizada.md").is_file(),
           "missing Treihord altitude document")
    elyra=load(DATA/"darovan_dp13_elyra_altitude_authorial_v0.1.json")
    validate_elyra_authorial(elyra)
    elyra_mutations=[
      ("elyra_wrong_option",lambda d:d.__setitem__("selectedOption","B")),
      ("elyra_wrong_height",lambda d:d.__setitem__("majorSummitsApproximateUpperElevationMeters",3200)),
      ("elyra_invented_peak",lambda d:d.__setitem__("officialHighestPeakName","Pico de las Lomas")),
      ("elyra_invented_terrain",lambda d:d.__setitem__("georeferencedMountainGeometry",{"lat":10})),
      ("elyra_misrepresented_survey",lambda d:d.__setitem__("approvedNumberIsMeasuredSurvey",True)),
      ("elyra_wrong_relative_canon",lambda d:d["relativeCanon"].__setitem__("valkramHighestSummitName","otro"))
    ]
    for label,change in elyra_mutations:
        test=copy.deepcopy(elyra)
        change(test)
        try:
            validate_elyra_authorial(test)
        except AssertionError:
            continue
        raise AssertionError("Elyra negative mutation not rejected "+label)
    demand((TERR/"D.P13"/"13_altitud_elyra_autorizada.md").is_file(),"missing Elyra document")
    peak=load(DATA/"darovan_dp13_valkram_altitude_authorial_v0.1.json")
    validate_authorial_altitudes(peak)
    alt_mutations=[
      ("apex_height",lambda d:d["worldHighestSummit"].__setitem__("altitudeMetersApprox",4800)),
      ("apex_location",lambda d:d["worldHighestSummit"].__setitem__("sector","southern")),
      ("apex_owner",lambda d:d["worldHighestSummit"].__setitem__("administrativeOwnership","casa_darovan")),
      ("apex_toponym",lambda d:d["worldHighestSummit"].__setitem__("officialToponym","Pico Nuevo")),
      ("apex_toponym_case",lambda d:d["worldHighestSummit"].__setitem__("officialToponym","La Viuda")),
      ("apex_invented_etymology",lambda d:d["worldHighestSummit"].__setitem__("etymology","leyenda inventada")),
      ("snow_patches_removed",lambda d:d["worldHighestSummit"].__setitem__("snowPersistence",None)),
      ("snow_does_not_survive_summer",lambda d:d["worldHighestSummit"]["snowPersistenceDetail"].__setitem__("survivesSummer",False)),
      ("snow_spans_entire_peak",lambda d:d["worldHighestSummit"]["snowPersistenceDetail"].__setitem__("continuousBlanketOverEntireSummit",True)),
      ("snowline_fabricated",lambda d:d["worldHighestSummit"]["snowPersistenceDetail"].__setitem__("fixedSnowlineMeters",2700)),
      ("glaciers_implicitly_approved",lambda d:d["worldHighestSummit"]["snowPersistenceDetail"].__setitem__("glacierAuthorizationInThisDecision",True)),
      ("glacier_existence_fabricated",lambda d:d["worldHighestSummit"].__setitem__("glacierPresence",True)),
      ("snow_generalized_to_all_valkram",lambda d:d["limits"].__setitem__("permanentSnow","confirmed_everywhere")),
      ("pass_wrong_min",lambda d:d["principalNaturalPasses"]["approximateElevationBandMeters"].__setitem__("min",900)),
      ("pass_wrong_max",lambda d:d["principalNaturalPasses"]["approximateElevationBandMeters"].__setitem__("max",2800)),
      ("pass_invented_name",lambda d:d["principalNaturalPasses"]["namesApproved"].append("Paso del Sol")),
      ("pass_invented_road",lambda d:d["principalNaturalPasses"]["establishedRoadsOrBridges"].append("camino nuevo")),
      ("pass_invented_location",lambda d:d["principalNaturalPasses"]["geographicPassLocations"].append("UTM test")),
      ("pass_materialized",lambda d:d["principalNaturalPasses"].__setitem__("createsPassInstances",True)),
      ("pass_pretend_year_round",lambda d:d["principalNaturalPasses"].__setitem__("guaranteesYearRoundTransit",True)),
      ("pass_wrong_scope",lambda d:d["limits"].__setitem__("passElevations","all_passes_exact")),
      ("glacier_approved",lambda d:d["worldHighestSummit"].__setitem__("glacierPresence",True)),
      ("azor_superior_overwritten",lambda d:d["crossCanon"].__setitem__("superiorCanonFileModified",True))
    ]
    for label,change in alt_mutations:
        test=copy.deepcopy(peak)
        change(test)
        try:
            validate_authorial_altitudes(test)
        except AssertionError:
            continue
        raise AssertionError("Authorial peak negative test not rejected "+label)
    demand((TERR/"D.P13"/"12_altitud_valkram_autorizada.md").is_file(),"missing altitude decision document")
    profiles=load(DATA/"darovan_dp13_physical_profiles_v0.1.json")
    hydro=load(DATA/"darovan_dp13_hydro_overlay_v0.1.json")
    causal=load(DATA/"darovan_dp13_environment_causal_v0.1.json")
    d01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    d02=load(DATA/"darovan_d02_hydro_network_v0.1.json")
    d03=load(DATA/"darovan_d03_climate_ecosystems_v0.1.json")
    validate(profiles,hydro,causal,d01,d02,d03)
    mutations=[
      ("extra_city",lambda p,h,c:p["existingCanons"]["cities"].append("karsath")),
      ("arven_revoked",lambda p,h,c:p["existingCanons"].__setitem__("arvenOwner","UNKNOWN")),
      ("fhalion_mouth",lambda p,h,c:h["systems"][2]["canonicalOutlets"].append("golfo_de_norgard")),
      ("belara_through_city",lambda p,h,c:h["topologyGuards"].__setitem__("belaraCrossesTreihord",True)),
      ("split_thalen_removed",lambda p,h,c:h["topologyGuards"].__setitem__("thalenTerminalArms",1)),
      ("lhera_veldora_connected",lambda p,h,c:h["topologyGuards"].__setitem__("veldoraConnectedToBelaraLhera",True)),
      ("arven_island_city",lambda p,h,c:p["existingCanons"]["cities"].append("arven")),
      ("new_named_river",lambda p,h,c:h["topologyGuards"].__setitem__("namedMinorRiverCount",1)),
      ("invented_bridge",lambda p,h,c:h["topologyGuards"].__setitem__("bridgesOrFordsCreated",1)),
      ("numeric_temperature",lambda p,h,c:p["zones"][0].__setitem__("temperatureC",14)),
      ("invented_elevation",lambda p,h,c:p["zones"][1].__setitem__("altitudeMeters",500)),
      ("runtime_claim",lambda p,h,c:p["runtime"].__setitem__("implementedInCoreRPG",True)),
      ("river_runtime_claim",lambda p,h,c:h["runtime"].__setitem__("generatedSegments",12)),
      ("fictitious_basin",lambda p,h,c:h["candidateProfiles"][0].__setitem__("assignedBasin","thalen")),
      ("missing_catchment",lambda p,h,c:h["mandatoryInputs"].remove("valid_downstream_receiver")),
      ("zone_omitted",lambda p,h,c:p["zones"].pop()),
      ("zone_without_source",lambda p,h,c:p["zones"][0].__setitem__("sourcePaths",[])),
      ("bogus_soil",lambda p,h,c:p["zones"][0].__setitem__("soilTaxon","CHERNOZEM")),
      ("fog_rule_nocause",lambda p,h,c:c["rules"][3].__setitem__("requires",[])),
      ("bogus_persisted_authority",lambda p,h,c:c["futureEntityContract"].__setitem__("writeAuthority","gemini")),
      ("single_taramin_forest_false",lambda p,h,c:p["existingCanons"].__setitem__("taraminSingleForest",False)),
      ("aguja_settlement_true",lambda p,h,c:p["existingCanons"].__setitem__("agujaPermanentSettlements",True)),
      ("status_live",lambda p,h,c:p.__setitem__("status","implemented")),
      ("missing_negative_case",lambda p,h,c:c["negativeCases"].pop()),
    ]
    for label,change in mutations:
        p,h,c=(copy.deepcopy(x) for x in (profiles,hydro,causal))
        change(p,h,c)
        try:
            validate(p,h,c,d01,d02,d03,check_fs=False)
        except AssertionError:
            continue
        raise AssertionError("Negative test did not reject "+label)
    print(f"D.P13 STATIC OK: {len(profiles['zones'])} zones, "
          f"{len(hydro['systems'])} systems, {len(causal['rules'])} causal rules, "
          f"{len(mutations)+len(alt_mutations)+len(elyra_mutations)+len(treihord_mutations)+len(veldora_mutations)} negative tests; NO RUNTIME")

if __name__=="__main__":
    run()

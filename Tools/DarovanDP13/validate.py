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
           record["selectedOption"] == "A","Veldora identity and option")
    demand(record["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":60}
           and record["referenceType"] == "approximate_general_coastal_urban_site_not_every_street",
           "Veldora urban elevation range")
    demand(all(record[k] is None for k in
           ("urbanAltitudeSingleValueMeters","cityCenterCoordinates","portDockElevationsMeters",
            "coastlineCoordinates","quayPositions","tidalRangeMeters","shorelineSlopePercent",
            "riverBehindCityIdentity","riverMouthToCityGeometry","terrainElevationRaster",
            "cadastralOrStreetTopography")) and record["neighborhoodElevations"] == [],
           "Veldora invented measurement, district or river identity")
    demand("puerto comercial marítimo" in record["autoralAnchorNotes"][0] and
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

def validate_taramin_authorial(record, d01, d07):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_taramin_elevation_authorial"
           and record["status"] == "AUTHORED_AUTHOR_DECISION_NOT_GEOMETRY",
           "Taramin schema and status")
    demand(record["authorDecisionId"] == "DAR-DP13-CITY-ALT-03"
           and record["authorDecisionDate"] == "2026-10-25"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION","Taramin author decision")
    demand(record["settlementId"] == "taramin" and record["type"] == "canonical_city"
           and record["role"] == "darovan_fishing_port" and record["selectedOption"] == "A",
           "Taramin identity and option")
    demand(record["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":40}
           and record["referenceType"] == "approximate_main_urban_core_not_every_street_or_dock",
           "Taramin reference elevations")
    demand(all(record[x] is None for x in ("singleUrbanAltitudeMeters","cityCenterCoordinates",
           "portDockElevationMeters","tidalRangeMeters","tidalOrSurgeFloodRiskMeasured",
           "thalenArmSurfaceHeightsMeters","thalenArmNavigability",
           "thalenExactRiverChannelCoordinates","bridgeCount","shorelineTopographicSlope",
           "urbanTerrainRaster","georeferencedCityPlan")),"No invented Taramin measurements")
    demand(record["neighborhoodElevations"] == [] and record["bridgeLocations"] == []
           and record["newCanals"] == [] and record["newIslands"] == [],"No invented Taramin objects")
    demand(record["canonicalGuards"] == {
           "cityBetweenThalenTerminalArms":True,
           "thalenOneNamedRiverTwoTerminalArms":True,
           "armCrossingsOrBridgesUnconfirmed":True,
           "maritimeAndFluvialFishingAuthored":True,
           "fishingPortExisting":True,
           "semiaridPeninsularTransition":True,
           "noInventedHydroConnections":True}, "Taramin canonical guards")
    demand(record["implementation"] == {
           "worldStateRuntime":False,"georeferencedMap":False,
           "createsInfrastructure":False,"modifiesPriorPhases":False},"Taramin implementation")
    demand([c["id"] for c in d01["cityAnchors"] if c["id"]=="taramin"] == ["taramin"]
           and d07["manualCityIds"] == ["treihord","veldora","taramin","syvaris"],
           "Taramin prior index")
    for source in record["sourcePaths"]:
        demand((ROOT/source).is_file(),"Missing Taramin source "+source)
    demand((TERR/"D.P13"/"16_altitud_taramin_autorizada.md").is_file(),
           "Missing Taramin decision doc")

def validate_syvaris_authorial(record, d01, d07):
    demand(record["schemaVersion"] == 1
           and record["documentId"] == "darovan_dp13_syvaris_elevation_authorial"
           and record["status"] == "AUTHORED_AUTHOR_DECISION_NOT_GEOMETRY",
           "Syvaris schema/status")
    demand(record["authorDecisionId"] == "DAR-DP13-CITY-ALT-04"
           and record["authorDecisionDate"] == "2026-10-25"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION",
           "Syvaris author decision")
    demand(record["settlementId"] == "syvaris"
           and record["type"] == "canonical_city"
           and record["role"] == "darovan_insular_main_bay_settlement"
           and record["selectedOption"] == "A","Syvaris city identity and option")
    demand(record["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":40}
           and record["referenceType"] == "approximate_main_urban_core_near_bay_not_whole_island",
           "Syvaris urban elevation band")
    demand(all(record[x] is None for x in
           ("oneExactUrbanElevationMeters","mainBayGeometry","cityCenterCoordinates",
            "harborOrQuayElevationsMeters","islandMaximumElevationMeters",
            "islandAverageElevationMeters","bayTidalRangeMeters","coastalFloodReturnPeriod",
            "cliffHeightsMeters","shorelineSlopePercent","urbanTerrainRaster","officialStreetPlan")),
           "Syvaris speculative measurements forbidden")
    demand(all(record[x] == [] for x in
           ("neighborhoodElevations","coveCoordinates","waterSupplySites",
            "navalFacilityPositions")),"Syvaris fictional specific features")
    demand(record["canonicalGuards"] == {
           "islandIsNorgardAndAdministeredByDarovan":True,
           "cityAtMainBay":True,
           "minorCovesExistingAsQualitativeFeatures":True,
           "safePortAlreadyAuthored":True,
           "norgardNavalPresenceIsRoyalNotPrivateDarovanFleet":True,
           "southGreenerCenterNorthDrier":True,
           "scatteredForestNotUniformJungle":True,
           "noNewPortsOrCoves":True,
           "noNewNavalFacility":True},"Syvaris source-anchored guards")
    demand(record["implementation"] ==
           {"worldStateRuntime":False,"georeferencedMap":False,
            "newInfrastructure":False,"modifiedPriorPhases":False},
           "Syvaris is non-runtime")
    demand([c["id"] for c in d01["cityAnchors"] if c["id"] == "syvaris"] == ["syvaris"]
           and d07["manualCityIds"] == ["treihord","veldora","taramin","syvaris"],
           "Syvaris D01/D07 identity")
    for p in record["sourcePaths"]:
        demand((ROOT/p).is_file(),"Syvaris source missing "+p)
    demand((TERR/"D.P13"/"17_altitud_syvaris_autorizada.md").is_file(),
           "Syvaris decision documentation missing")

def validate_syvaris_island_maximum(record, urban_record, d01, d07):
    demand(record["schemaVersion"] == 1
           and record["documentId"] == "darovan_dp13_syvaris_island_maximum_elevation_authorial"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["authorDecisionId"] == "DAR-DP13-ISLAND-ALT-01"
           and record["authorDecisionDate"] == "2026-10-25",
           "Syvaris island decision")
    demand(record["geographyId"] == "syvaris_island"
           and record["geographyName"] == "isla de Syvaris"
           and record["adminOwner"] == "casa_darovan"
           and record["selectedOption"] == "A",
           "Syvaris island identity")
    demand(record["approximateHighestNaturalElevationBandMeters"] == {"min":200,"max":400}
           and record["semantics"] ==
           "the_islands_maximum_height_lies_approximately_within_this_band_not_a_uniform_elevation_of_hills",
           "Syvaris island maximum band")
    demand(all(record[k] is None for k in
           ("exactMaximumElevationMeters","highestSummitOfficialName",
            "highestSummitCoordinates","elevatedAreasPolygon","terrainHeightmap",
            "generalizedSnowClimateInference","permanentSnow")),
           "No fabricated summit coordinates or snow")
    demand(record["specificHillsAndCliffElevations"] == []
           and record["officialMountainPeakInstances"] == [],
           "No specific summits or terrain measurements")
    demand(record["separateCityAltitude"] == {
           "cityId":"syvaris","urbanCoreBandMetersApprox":{"min":0,"max":40},
           "cityDecisionId":"DAR-DP13-CITY-ALT-04"},
           "Distinguish city and island maximum")
    demand(urban_record["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":40}
           and urban_record["islandMaximumElevationMeters"] is None,
           "Preserve the exact UNKNOWN and urban core")
    demand(record["protectedPreexistingCanon"] == {
           "cityAtMainBay":True,"drierNorthCentralSectors":True,
           "greenerSouth":True,"discontinuousSmallForests":True,"notDesert":True,
           "islandIsNorgard":True,"administeredByDarovan":True},
           "Syvaris source canon")
    demand(record["implementation"] == {
           "georeferencedMap":False,"terrainCreated":False,
           "worldStateRuntime":False,"changedPriorPhases":False},
           "Syvaris island non-runtime")
    demand([c["id"] for c in d01["cityAnchors"] if c["id"]=="syvaris"] == ["syvaris"]
           and d07["manualCityIds"] == ["treihord","veldora","taramin","syvaris"],
           "Syvaris D01/D07 continuity")
    for source in record["sourcePaths"]:
        demand((ROOT/source).is_file(),"Syvaris island source missing "+source)
    demand((TERR/"D.P13"/"18_altitud_maxima_isla_syvaris_autorizada.md").is_file(),
           "Syvaris island documentation missing")

def validate_arven_island_maximum(record, d01):
    demand(record["schemaVersion"] == 1
           and record["documentId"] == "darovan_dp13_arven_island_maximum_elevation_authorial"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["authorDecisionId"] == "DAR-DP13-ISLAND-ALT-02"
           and record["authorDecisionDate"] == "2026-10-25",
           "Arven author decision")
    demand(record["geographyId"] == "arven_island"
           and record["geographyName"] == "isla de Arven"
           and record["adminOwner"] == "casa_darovan"
           and record["selectedOption"] == "B","Arven island identity")
    demand(record["approximateHighestNaturalElevationBandMeters"] == {"min":250,"max":500}
           and record["semantics"] == "island_natural_maximum_lies_approximately_within_band_not_all_hills_or_villages",
           "Arven maximum elevation constraint")
    demand(all(record[k] is None for k in
           ("exactMaximumElevationMeters","highestSummitOfficialName","highestSummitCoordinates",
            "elevatedAreasPolygon","terrainHeightmap","villageAltitudeMeters",
            "coastLevelMetrics","rainfallOrTemperatureMeasured","permanentSnow")),
           "No fabricated Arven elevations or climatic measurements")
    demand(all(record[k] == [] for k in
           ("specificHillOrCliffElevations","officialPeakInstances","villageCoordinates",
            "watercoursesOrSpringsCreated")),
           "No invented Arven peaks, villages or watercourses")
    demand(record["protectedPreexistingCanon"] == {
           "islandFacesGolfoDeVeldora":True,
           "islandPartOfNorgard":True,
           "administeredByDarovan":True,
           "mainForestName":"Bosque del Manto Verde",
           "forestCoverApproxPercent":90,
           "forestContinuous":True,
           "forestDominantlyConifers":True,
           "villagesExist":True,
           "villagesConcentratedOnInnerCoastFacingGulf":True,
           "forestHuntingImportant":True,
           "loggingLimited":True}, "Arven forest and settlement canon")
    demand(record["implementation"] == {
           "georeferencedMap":False,"terrainCreated":False,
           "worldStateRuntime":False,"changedPriorPhases":False},
           "Arven not materialized in engine or old phases")
    demand(any(z["id"] == "d01_arven_contexto"
               and z["administrativeOwner"] == "casa_darovan"
               for z in d01["physicalUnits"]), "Arven D01 work-unit anchor")
    for source in record["sourcePaths"]:
        demand((ROOT/source).is_file(),"Arven source path unavailable "+source)
    demand((TERR/"D.P13"/"19_altitud_maxima_isla_arven_autorizada.md").is_file(),
           "Arven decision documentation missing")

def validate_taramin_hills_authorial(record, d01, elyra, taramin_city):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_taramin_north_central_hills_authorial"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["authorDecisionId"] == "DAR-DP13-HILLS-01"
           and record["authorDecisionDate"] == "2026-10-25",
           "Taramin hills author decision")
    demand(record["geographyId"] == "taramin_peninsula_north_central_hills"
           and record["sourceStudyUnitId"] == "d01_taramin_norte_centro"
           and record["excludesStudyUnitId"] == "d01_elyra_paso_peninsular"
           and record["selectedOption"] == "B","Taramin hills geographic scope")
    demand(record["characteristicHillElevationBandMetersApprox"] == {"min":300,"max":600}
           and record["semantics"] ==
           "characteristic_elevations_of_north_central_peninsular_hills_not_all_terrain_nor_peninsula_maximum",
           "Taramin hills reference heights")
    demand(record["physicalProfile"] == {
           "landformCategory":"hills",
           "canonicalTraits":["ochre_hills","rocky_exposures","semiarid_transition"],
           "seasonalGulliesPossibleByTopologyNotInstantiated":True},
           "Taramin hills qualitative source profile")
    demand(all(record[k] is None for k in
           ("specificHillHeightMeters","exactHillMaximumMeters",
            "peninsulaOverallMaximumMeters","heightmap","polygon","coordinates",
            "measuredRainfallMm","measuredTemperatureC")),
           "No fabricated hill geometry/measurement")
    demand(all(record[k] == [] for k in
           ("roadOrPassLocations","namedNewFeatures","permanentWatercoursesAdded",
            "exactSeasonalGullies","namedSettlementsAdded","specificForestsModified")),
           "No invented Taramin features")
    demand(record["referenceConstraints"] == {
           "elyraSeparateMountainRange":True,
           "elyraUpperSummitsMetersApprox":2600,
           "taraminMainUrbanCoreMetersApprox":{"min":0,"max":40},
           "northCentralSemiaridNotUniformDesert":True,
           "thalenOneRiverWithTwoTerminalArms":True,
           "southTaraminForestSeparate":True},
           "Taramin source and other authorial decisions")
    demand(elyra["majorSummitsApproximateUpperElevationMeters"] == 2600
           and taramin_city["urbanAltitudeReferenceBandMetersApprox"] == {"min":0,"max":40},
           "Crosscheck Elyra and city records")
    demand(any(z["id"] == "d01_taramin_norte_centro" for z in d01["physicalUnits"])
           and any(z["id"] == "d01_elyra_paso_peninsular" for z in d01["physicalUnits"]),
           "Preserve D01 unit identities")
    demand(record["implementation"] == {
           "worldStateRuntime":False,"georeferencedMap":False,
           "terrainCreated":False,"olderPhasesModified":False},
           "Taramin hills not materialized")
    for source in record["sourcePaths"]:
        demand((ROOT/source).is_file(),"Missing source for Taramin hills "+source)
    demand((TERR/"D.P13"/"20_colinas_norte_centro_taramin_autorizadas.md").is_file(),
           "Missing Taramin hills authored document")

def validate_valkram_west_foothills_authorial(record, d01, valkram, treihord):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_valkram_west_foothills_authorial"
           and record["authority"] == "AUTHORED_AUTHOR_DECISION"
           and record["authorDecisionId"] == "DAR-DP13-FOOTHILLS-01"
           and record["authorDecisionDate"] == "2026-10-25",
           "Valkram foothills authored contract")
    demand(record["landformId"] == "valkram_west_foothills"
           and record["mountainRange"] == "Montes Valkram"
           and record["direction"] == "western"
           and record["sourceStudyUnitId"] == "d01_valkram_oeste"
           and record["option"] == "B",
           "Valkram western foothills identity")
    demand(record["characteristicFoothillElevationBandMetersApprox"] == {"min":400,"max":900}
           and record["semantics"] ==
           "characteristic_western_foothill_elevations_not_every_slope_valley_or_valkram_summit",
           "Valkram foothills reference band and proper scope")
    demand(all(record[k] is None for k in
           ("zonePolygon","heightmap","uniformHeightMeters",
            "exactFoothillPeakHeightMeters","individualSlopePercent",
            "exactRiverElevationsMeters","climateMeasurements",
            "forestCoverByAltitude","observedSnowlineMeters")),
           "Valkram foothills no invented geometry or measurements")
    demand(all(record[k] == [] for k in
           ("valleyFloorHeightsMeters","roadOrPassLocations","newValleyNames",
            "newWatercourseNames","newBridgesOrSettlements")),
           "Valkram foothills no invented features")
    demand(record["sourceCanonProtection"] == {
           "valkramMajorSummitsBandMetersApprox":{"min":3600,"max":4200},
           "valkramHighestPeakName":"la Viuda",
           "valkramHighestPeakApproxMeters":4200,
           "valkramPrincipalPassesBandMetersApprox":{"min":1400,"max":2200},
           "treihordUrbanCoreBandMetersApprox":{"min":150,"max":350},
           "belaraAdjacentToTreihordNotCrossing":True,
           "noNewBelaraRiverBranch":True,
           "noAutomaticPoliticalBoundaryFromRidge":True,
           "naturalWestwardDescentOnlyConditional":True},
           "Valkram foothills cross-canon protection")
    demand(valkram["rangeDefinition"]["representativeMajorSummitBandMetersApprox"] ==
           {"min":3600,"max":4200}
           and valkram["worldHighestSummit"]["officialToponym"] == "la Viuda"
           and valkram["worldHighestSummit"]["altitudeMetersApprox"] == 4200
           and valkram["principalNaturalPasses"]["approximateElevationBandMeters"] ==
           {"min":1400,"max":2200}
           and treihord["urbanAltitudeReferenceBandMetersApprox"] == {"min":150,"max":350},
           "Foothills preserve other authored altitude contracts")
    demand(any(z["id"] == "d01_valkram_oeste"
               for z in d01["physicalUnits"]),"Foothills D01 unit")
    demand(record["implementation"] == {
           "worldStateRuntime":False,"georeferencedMap":False,
           "terrainCreated":False,"olderPhasesModified":False},
           "Foothills not runtime")
    for source in record["sourcePaths"]:
        demand((ROOT/source).is_file(),"Missing foothills source "+source)
    demand((TERR/"D.P13"/"21_piedemonte_occidental_valkram_autorizado.md").is_file(),
           "Foothills authorial document missing")

def validate_author_delegated_choices(record):
    demand(record["schemaVersion"] == 1 and
           record["documentId"] == "darovan_dp13_delegated_decisions_authorized_2026_10_25"
           and record["phase"] == "D.P13", "Delegated closure schema")
    delegation=record["delegation"]
    demand(delegation["authorizedBy"] == "author"
           and delegation["authorizedDate"] == "2026-10-25"
           and delegation["method"] == "assistant_chooses_recommended_options_without_additional_questions",
           "Explicit author delegation recorded")
    demand("not personally selected individually" in delegation["attribution"]
           and "no merge" in delegation["limits"], "Do not misattribute decision or PR authority")
    demand(record["status"] == "DESIGN_DECISIONS_CLOSED_WITH_MATERIALIZATION_RESERVES",
           "Do not claim fully mapped/runtime world")
    expected=[
      ("valkram_valleys",700,1300),
      ("elyra_main_passes",900,1500),
      ("elyra_valleys",400,900),
      ("taramin_south_hills",150,500),
      ("northern_cold",None,None),
      ("west_coast",None,None),
      ("snow",None,None),
      ("wind",None,None),
      ("rain",None,None),
      ("fog",None,None),
      ("soil",None,None),
      ("streams",None,None),
      ("flood",None,None),
      ("pass_weather",None,None),
      ("forest",None,None),
      ("mapping",None,None)
    ]
    demand(len(record["decisions"]) == len(expected), "Q13-Q28 coverage")
    for i,(scope,lower,upper) in enumerate(expected):
        decision=record["decisions"][i]
        demand(decision["id"] == "DAR-DP13-DELEGATED-Q"+str(i+13)
               and decision["question"] == i+13 and decision["selectedOption"] == "B"
               and decision["authority"] == "ASSISTANT_UNDER_AUTHOR_BLANKET_DELEGATION"
               and decision["scopeId"] == scope, "Delegated choice Q"+str(i+13))
        band=None if lower is None else {"min":lower,"max":upper}
        demand(decision["characteristicElevationMetersApprox"] == band,
               "Delegated characteristic band Q"+str(i+13))
        demand(len(decision["subject"]) > 6 and len(decision["scopeRule"]) > 18,
               "Decision must explain scope Q"+str(i+13))
        demand(decision["authorPersonallyChoseThisOption"] is False
               and decision["createsGeoreferencedGeometry"] is False
               and decision["claimsMeasuredValues"] is False,
               "Delegation cannot imply personal response, GIS or observation")
    anchors=record["directAuthorCanon"]
    demand(anchors["valkramHighSummitName"] == "la Viuda"
           and anchors["valkramHighSummitApproxMeters"] == 4200
           and anchors["valkramMainPassesMeters"] == {"min":1400,"max":2200}
           and anchors["valkramWestFoothillsMeters"] == {"min":400,"max":900}
           and anchors["elyraTopApproxMeters"] == 2600
           and anchors["treihordUrbanMeters"] == {"min":150,"max":350}
           and anchors["veldoraUrbanMeters"] == {"min":0,"max":60}
           and anchors["taraminUrbanMeters"] == {"min":0,"max":40}
           and anchors["syvarisUrbanMeters"] == {"min":0,"max":40}
           and anchors["syvarisIslandMaximumMeters"] == {"min":200,"max":400}
           and anchors["arvenIslandMaximumMeters"] == {"min":250,"max":500}
           and anchors["taraminNorthCenterHillsMeters"] == {"min":300,"max":600}
           and anchors["laViudaSnowPatchesSurviveSummer"] is True,
           "Do not override directly approved facts")
    demand(record["hydrologyGuards"] == {
           "rivers":["belara","lhera","veldora","fhalion","thalen"],
           "systemCount":4,"belaraCrossesTreihord":False,
           "thalenTerminalArms":2,"fhalionMouthUnconfirmed":True},
           "Protect five rivers and four systems")
    unknown=record["unresolvedRequiringPhysicalData"]
    demand(len(unknown)==9 and len(set(unknown))==9
           and "georeferenced_elevation_grid" in unknown
           and "executable_CoreRPG_environmental_simulation" in unknown
           and "prevailing_wind_statistics" in unknown,
           "Metric and runtime reservations persist")
    policy=record["prohibitions"]
    demand(all(policy[k]==[] for k in (
           "newGeographicNames","newRivers","newRoads","newSettlements",
           "newBridges","newCanals")), "No newly invented physical features")
    demand(all(policy[k] is False for k in (
           "exactCoordinatesAuthorized","meteorologicalMeasurementsApproved",
           "heightmapCreated","glaciersConfirmed","engineSimulationExecuted",
           "mainModified","nextPhaseStarted","mayMergePr")),
           "No invented metrics, simulation, phase or PR merge")
    demand((TERR/"D.P13"/"22_cierre_delegado_preguntas_y_opciones.md").is_file(),
           "Delegated decision report required")

def run():
    delegated=load(DATA/"darovan_dp13_delegated_decisions_authorized_v0.1.json")
    validate_author_delegated_choices(delegated)
    delegated_mutations=[]
    for idx in range(16):
        delegated_mutations.append(
            ("delegate_wrong_choice_"+str(idx),
             lambda d,i=idx:d["decisions"][i].__setitem__("selectedOption","A")))
    for idx in range(4):
        delegated_mutations.extend([
            ("delegate_wrong_min_"+str(idx),
             lambda d,i=idx:d["decisions"][i]["characteristicElevationMetersApprox"].__setitem__("min",5)),
            ("delegate_wrong_max_"+str(idx),
             lambda d,i=idx:d["decisions"][i]["characteristicElevationMetersApprox"].__setitem__("max",9999))
        ])
    delegated_mutations.extend([
      ("wrong_source",lambda d:d["delegation"].__setitem__("authorizedBy","assistant")),
      ("pretend_direct_author",lambda d:d["decisions"][0].__setitem__("authorPersonallyChoseThisOption",True)),
      ("invented_alt_geometry",lambda d:d["decisions"][0].__setitem__("createsGeoreferencedGeometry",True)),
      ("invented_weather_reading",lambda d:d["decisions"][9].__setitem__("claimsMeasuredValues",True)),
      ("renamed_la_viuda",lambda d:d["directAuthorCanon"].__setitem__("valkramHighSummitName","otra")),
      ("raised_veldora",lambda d:d["directAuthorCanon"]["veldoraUrbanMeters"].__setitem__("max",150)),
      ("changed_belara",lambda d:d["hydrologyGuards"].__setitem__("belaraCrossesTreihord",True)),
      ("changed_thalen",lambda d:d["hydrologyGuards"].__setitem__("thalenTerminalArms",3)),
      ("invented_fhalion_mouth",lambda d:d["hydrologyGuards"].__setitem__("fhalionMouthUnconfirmed",False)),
      ("invented_new_river",lambda d:d["prohibitions"]["newRivers"].append("false_river")),
      ("invented_new_road",lambda d:d["prohibitions"]["newRoads"].append("false_road")),
      ("invented_new_city",lambda d:d["prohibitions"]["newSettlements"].append("false_city")),
      ("faked_heightmap",lambda d:d["prohibitions"].__setitem__("heightmapCreated",True)),
      ("invented_glacier",lambda d:d["prohibitions"].__setitem__("glaciersConfirmed",True)),
      ("faked_rainfall",lambda d:d["prohibitions"].__setitem__("meteorologicalMeasurementsApproved",True)),
      ("merges_without_permission",lambda d:d["prohibitions"].__setitem__("mayMergePr",True)),
      ("changes_main",lambda d:d["prohibitions"].__setitem__("mainModified",True)),
      ("fakes_engine_simulation",lambda d:d["prohibitions"].__setitem__("engineSimulationExecuted",True)),
      ("claims_no_reservations",lambda d:d.__setitem__("unresolvedRequiringPhysicalData",[])),
      ("not_a_delegated_status",lambda d:d.__setitem__("status","PHYSICAL_RUNTIME_READY"))
    ])
    for label,change in delegated_mutations:
        altered=copy.deepcopy(delegated)
        change(altered)
        try:
            validate_author_delegated_choices(altered)
        except AssertionError:
            continue
        raise AssertionError("Delegated option negative mutation accepted "+label)
    foothills=load(DATA/"darovan_dp13_valkram_west_foothills_authorial_v0.1.json")
    fd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    fv=load(DATA/"darovan_dp13_valkram_altitude_authorial_v0.1.json")
    ft=load(DATA/"darovan_dp13_treihord_elevation_authorial_v0.1.json")
    validate_valkram_west_foothills_authorial(foothills,fd01,fv,ft)
    foothills_mutations=[
      ("wrong_range",lambda d:d.__setitem__("mountainRange","Montañas Elyra")),
      ("wrong_direction",lambda d:d.__setitem__("direction","eastern")),
      ("wrong_study_unit",lambda d:d.__setitem__("sourceStudyUnitId","d01_taramin_norte_centro")),
      ("wrong_option",lambda d:d.__setitem__("option","A")),
      ("wrong_min_elevation",lambda d:d["characteristicFoothillElevationBandMetersApprox"].__setitem__("min",250)),
      ("wrong_max_elevation",lambda d:d["characteristicFoothillElevationBandMetersApprox"].__setitem__("max",1200)),
      ("uniform_altitude_misread",lambda d:d.__setitem__("semantics","each_valley_is_at_400_to_900")),
      ("fabricated_terrain",lambda d:d.__setitem__("heightmap",[[400,900]])),
      ("fabricated_polygon",lambda d:d.__setitem__("zonePolygon",{"type":"Polygon"})),
      ("invented_valley_height",lambda d:d["valleyFloorHeightsMeters"].append(500)),
      ("invented_pass",lambda d:d["roadOrPassLocations"].append("Paso ficticio")),
      ("invented_belara_branch",lambda d:d["newWatercourseNames"].append("Afluente nuevo")),
      ("belara_crosses_treihord",lambda d:d["sourceCanonProtection"].__setitem__("belaraAdjacentToTreihordNotCrossing",False)),
      ("wrong_peak",lambda d:d["sourceCanonProtection"].__setitem__("valkramHighestPeakName","otro")),
      ("wrong_pass_band",lambda d:d["sourceCanonProtection"]["valkramPrincipalPassesBandMetersApprox"].__setitem__("max",3000)),
      ("wrong_city_band",lambda d:d["sourceCanonProtection"]["treihordUrbanCoreBandMetersApprox"].__setitem__("min",450)),
      ("invented_snowline",lambda d:d.__setitem__("observedSnowlineMeters",2500)),
      ("invented_slope",lambda d:d.__setitem__("individualSlopePercent",30)),
      ("false_political_border",lambda d:d["sourceCanonProtection"].__setitem__("noAutomaticPoliticalBoundaryFromRidge",False)),
      ("false_runtime",lambda d:d["implementation"].__setitem__("terrainCreated",True))
    ]
    for label,change in foothills_mutations:
        altered=copy.deepcopy(foothills)
        change(altered)
        try:
            validate_valkram_west_foothills_authorial(altered,fd01,fv,ft)
        except AssertionError:
            continue
        raise AssertionError("Foothills negative mutation accepted "+label)
    taramin_hills=load(DATA/"darovan_dp13_taramin_north_central_hills_authorial_v0.1.json")
    hd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    helyra=load(DATA/"darovan_dp13_elyra_altitude_authorial_v0.1.json")
    hcity=load(DATA/"darovan_dp13_taramin_elevation_authorial_v0.1.json")
    validate_taramin_hills_authorial(taramin_hills,hd01,helyra,hcity)
    taramin_hill_mutations=[
      ("wrong_option",lambda d:d.__setitem__("selectedOption","A")),
      ("wrong_lower_band",lambda d:d["characteristicHillElevationBandMetersApprox"].__setitem__("min",100)),
      ("wrong_upper_band",lambda d:d["characteristicHillElevationBandMetersApprox"].__setitem__("max",900)),
      ("wrong_study_area",lambda d:d.__setitem__("sourceStudyUnitId","d01_taramin_bosque_sur")),
      ("wrong_elyra_exclusion",lambda d:d.__setitem__("excludesStudyUnitId","d01_valkram_oeste")),
      ("uniform_height_misread",lambda d:d.__setitem__("semantics","all_land_has_this_elevation")),
      ("wrong_elyra_height",lambda d:d["referenceConstraints"].__setitem__("elyraUpperSummitsMetersApprox",600)),
      ("wrong_city_height",lambda d:d["referenceConstraints"]["taraminMainUrbanCoreMetersApprox"].__setitem__("max",600)),
      ("fixed_peninsula_max",lambda d:d.__setitem__("peninsulaOverallMaximumMeters",600)),
      ("invented_exact_hill",lambda d:d.__setitem__("specificHillHeightMeters",450)),
      ("invented_new_road",lambda d:d["roadOrPassLocations"].append("road")),
      ("invented_new_watercourse",lambda d:d["permanentWatercoursesAdded"].append("river")),
      ("invented_gully_location",lambda d:d["exactSeasonalGullies"].append([2,5])),
      ("made_up_measurement",lambda d:d.__setitem__("measuredRainfallMm",450)),
      ("turns_into_uniform_desert",lambda d:d["referenceConstraints"].__setitem__("northCentralSemiaridNotUniformDesert",False)),
      ("changes_thalen",lambda d:d["referenceConstraints"].__setitem__("thalenOneRiverWithTwoTerminalArms",False)),
      ("claims_heightmap",lambda d:d.__setitem__("heightmap",[[300,600]])),
      ("claims_runtime",lambda d:d["implementation"].__setitem__("worldStateRuntime",True))
    ]
    for label,change in taramin_hill_mutations:
        altered=copy.deepcopy(taramin_hills)
        change(altered)
        try:
            validate_taramin_hills_authorial(altered,hd01,helyra,hcity)
        except AssertionError:
            continue
        raise AssertionError("Taramin hills negative mutation accepted "+label)
    arven=load(DATA/"darovan_dp13_arven_island_relief_authorial_v0.1.json")
    ad01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    validate_arven_island_maximum(arven,ad01)
    arven_mutations=[
      ("wrong_island",lambda d:d.__setitem__("geographyId","syvaris_island")),
      ("wrong_option",lambda d:d.__setitem__("selectedOption","A")),
      ("lower_bound_wrong",lambda d:d["approximateHighestNaturalElevationBandMeters"].__setitem__("min",100)),
      ("upper_bound_wrong",lambda d:d["approximateHighestNaturalElevationBandMeters"].__setitem__("max",800)),
      ("invented_exact_peak",lambda d:d.__setitem__("exactMaximumElevationMeters",375)),
      ("invented_peak_name",lambda d:d.__setitem__("highestSummitOfficialName","Pico Manto Verde")),
      ("invented_peak_location",lambda d:d.__setitem__("highestSummitCoordinates",[1,2])),
      ("all_villages_at_height",lambda d:d.__setitem__("villageAltitudeMeters",300)),
      ("false_forest_reduction",lambda d:d["protectedPreexistingCanon"].__setitem__("forestCoverApproxPercent",40)),
      ("false_forest_split",lambda d:d["protectedPreexistingCanon"].__setitem__("forestContinuous",False)),
      ("wrong_admin_owner",lambda d:d.__setitem__("adminOwner","casa_galdren")),
      ("wrong_village_coast",lambda d:d["protectedPreexistingCanon"].__setitem__("villagesConcentratedOnInnerCoastFacingGulf",False)),
      ("invented_village",lambda d:d["villageCoordinates"].append([1,2])),
      ("invented_river",lambda d:d["watercoursesOrSpringsCreated"].append("new river")),
      ("fake_heightmap",lambda d:d.__setitem__("terrainHeightmap",[[250,500]])),
      ("fabricated_snow",lambda d:d.__setitem__("permanentSnow",True)),
      ("wrong_landform_semantics",lambda d:d.__setitem__("semantics","average_height")),
      ("invented_runtime",lambda d:d["implementation"].__setitem__("worldStateRuntime",True))
    ]
    for label,change in arven_mutations:
        altered=copy.deepcopy(arven)
        change(altered)
        try:
            validate_arven_island_maximum(altered,ad01)
        except AssertionError:
            continue
        raise AssertionError("Arven negative mutation accepted "+label)
    syvaris_island=load(DATA/"darovan_dp13_syvaris_island_relief_authorial_v0.1.json")
    syvaris_urban=load(DATA/"darovan_dp13_syvaris_elevation_authorial_v0.1.json")
    sd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    sd07=load(DATA/"darovan_d07_canonical_cities_v0.1.json")
    validate_syvaris_island_maximum(syvaris_island,syvaris_urban,sd01,sd07)
    syvaris_island_mutations=[
      ("wrong_island",lambda d:d.__setitem__("geographyId","arven")),
      ("wrong_option",lambda d:d.__setitem__("selectedOption","B")),
      ("maximum_below_approved_band",lambda d:d["approximateHighestNaturalElevationBandMeters"].__setitem__("min",100)),
      ("maximum_above_approved_band",lambda d:d["approximateHighestNaturalElevationBandMeters"].__setitem__("max",700)),
      ("exact_height_invented",lambda d:d.__setitem__("exactMaximumElevationMeters",300)),
      ("invented_peak_name",lambda d:d.__setitem__("highestSummitOfficialName","Pico de la Isla")),
      ("invented_peak_position",lambda d:d.__setitem__("highestSummitCoordinates",[1,2])),
      ("whole_island_urban_band",lambda d:d["separateCityAltitude"]["urbanCoreBandMetersApprox"].__setitem__("max",400)),
      ("invented_landform",lambda d:d["officialMountainPeakInstances"].append("new")),
      ("fabricated_heightmap",lambda d:d.__setitem__("terrainHeightmap",[[200,300]])),
      ("fabricated_snow",lambda d:d.__setitem__("permanentSnow",True)),
      ("wrong_south_green",lambda d:d["protectedPreexistingCanon"].__setitem__("greenerSouth",False)),
      ("invented_runtime",lambda d:d["implementation"].__setitem__("terrainCreated",True)),
      ("misrepresented_mean",lambda d:d.__setitem__("semantics","average_elevation_of_island"))
    ]
    for label,change in syvaris_island_mutations:
        altered=copy.deepcopy(syvaris_island)
        change(altered)
        try:
            validate_syvaris_island_maximum(altered,syvaris_urban,sd01,sd07)
        except AssertionError:
            continue
        raise AssertionError("Syvaris island maximum mutation accepted "+label)
    syvaris=load(DATA/"darovan_dp13_syvaris_elevation_authorial_v0.1.json")
    sd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    sd07=load(DATA/"darovan_d07_canonical_cities_v0.1.json")
    validate_syvaris_authorial(syvaris,sd01,sd07)
    syvaris_mutations=[
      ("wrong_city",lambda d:d.__setitem__("settlementId","arven")),
      ("wrong_option",lambda d:d.__setitem__("selectedOption","B")),
      ("wrong_minimum",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("min",40)),
      ("wrong_maximum",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",100)),
      ("whole_island_false_ceiling",lambda d:d.__setitem__("islandMaximumElevationMeters",40)),
      ("invented_bay_polygon",lambda d:d.__setitem__("mainBayGeometry",{"point":[0,0]})),
      ("invented_quay_height",lambda d:d.__setitem__("harborOrQuayElevationsMeters",2)),
      ("invented_street_height",lambda d:d["neighborhoodElevations"].append({"name":"Nuevo","height":20})),
      ("invented_cove",lambda d:d["coveCoordinates"].append([5,5])),
      ("invented_water_supply",lambda d:d["waterSupplySites"].append("manantial")),
      ("private_navy",lambda d:d["canonicalGuards"].__setitem__("norgardNavalPresenceIsRoyalNotPrivateDarovanFleet",False)),
      ("uniform_jungle",lambda d:d["canonicalGuards"].__setitem__("scatteredForestNotUniformJungle",False)),
      ("new_naval_facility",lambda d:d["navalFacilityPositions"].append("artificial")),
      ("invented_tide",lambda d:d.__setitem__("bayTidalRangeMeters",2.5)),
      ("new_port",lambda d:d["implementation"].__setitem__("newInfrastructure",True)),
      ("fake_runtime",lambda d:d["implementation"].__setitem__("worldStateRuntime",True))
    ]
    for label,change in syvaris_mutations:
        altered=copy.deepcopy(syvaris)
        change(altered)
        try:
            validate_syvaris_authorial(altered,sd01,sd07)
        except AssertionError:
            continue
        raise AssertionError("Syvaris negative mutation accepted "+label)
    taramin=load(DATA/"darovan_dp13_taramin_elevation_authorial_v0.1.json")
    td01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    td07=load(DATA/"darovan_d07_canonical_cities_v0.1.json")
    validate_taramin_authorial(taramin,td01,td07)
    taramin_mutations=[
      ("wrong_city",lambda d:d.__setitem__("settlementId","syvaris")),
      ("wrong_option",lambda d:d.__setitem__("selectedOption","B")),
      ("wrong_max",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",100)),
      ("wrong_min",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("min",40)),
      ("false_dock_height",lambda d:d.__setitem__("portDockElevationMeters",1)),
      ("false_river_level",lambda d:d.__setitem__("thalenArmSurfaceHeightsMeters",[1,2])),
      ("false_tide",lambda d:d.__setitem__("tidalRangeMeters",1.2)),
      ("third_thalen_arm",lambda d:d["canonicalGuards"].__setitem__("thalenOneNamedRiverTwoTerminalArms",False)),
      ("invented_bridge",lambda d:d["bridgeLocations"].append("fictional_bridge")),
      ("invented_island",lambda d:d["newIslands"].append("fictional_island")),
      ("false_flood_risk",lambda d:d.__setitem__("tidalOrSurgeFloodRiskMeasured",True)),
      ("false_runtime",lambda d:d["implementation"].__setitem__("worldStateRuntime",True))
    ]
    for label,change in taramin_mutations:
        altered=copy.deepcopy(taramin)
        change(altered)
        try:
            validate_taramin_authorial(altered,td01,td07)
        except AssertionError:
            continue
        raise AssertionError("Taramin negative mutation accepted "+label)
    veldora=load(DATA/"darovan_dp13_veldora_elevation_authorial_v0.1.json")
    vd01=load(DATA/"darovan_d01_relief_profile_v0.1.json")
    vd07=load(DATA/"darovan_d07_canonical_cities_v0.1.json")
    validate_veldora_authorial(veldora,vd01,vd07)
    veldora_mutations=[
      ("veldora_wrong_city",lambda d:d.__setitem__("settlementId","treihord")),
      ("veldora_wrong_option",lambda d:d.__setitem__("selectedOption","B")),
      ("veldora_wrong_min",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("min",30)),
      ("veldora_wrong_max",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",250)),
      ("veldora_previous_B_band",lambda d:d["urbanAltitudeReferenceBandMetersApprox"].__setitem__("max",150)),
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
          f"{len(mutations)+len(alt_mutations)+len(elyra_mutations)+len(treihord_mutations)+len(veldora_mutations)+len(taramin_mutations)+len(syvaris_mutations)+len(syvaris_island_mutations)+len(arven_mutations)+len(taramin_hill_mutations)+len(foothills_mutations)+len(delegated_mutations)} negative tests; NO RUNTIME")

if __name__=="__main__":
    run()

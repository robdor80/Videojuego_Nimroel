"""GALDREN G04: canon alimentario y económico, 12 unidades y ataques negativos.
Solamente pruebas de consistencia documental. NO hay producción ni economía runtime.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
H = N / "Territorios/Casa Galdren"
D = H / "Datos operativos"
load = lambda p: json.loads(p.read_text(encoding="utf-8"))
g0 = load(D / "galdren_g00_manifest_v0.1.json")
g1 = load(D / "galdren_g01_geography_v0.1.json")
g2 = load(D / "galdren_g02_hydrology_v0.1.json")
g3 = load(D / "galdren_g03_climate_soils_ecosystems_v0.1.json")
g4 = load(D / "galdren_g04_agriculture_livestock_food_v0.1.json")

def ids(seq,prefix,n):
    assert isinstance(seq,list)
    assert [e["id"] for e in seq] == [f"{prefix}{i:02d}" for i in range(1,n+1)]
def no(row,fields):
    for field in fields:
        assert row[field] is False, f"Falso certificado: {field}"
def yes(row,fields):
    for field in fields:
        assert row[field] is True, f"Canon no preservado: {field}"
def unknown(row,fields):
    for field in fields:
        assert row[field] == "UNKNOWN", f"Dato local indebidamente rellenado: {field}"
def empty(row,fields):
    for field in fields:
        assert row[field] == [], f"Inventario ficticio: {field}"
def null(row,fields):
    for field in fields:
        assert row[field] is None, f"Magnitud numérica inventada: {field}"

KINDS = ["MOUNTAIN","INVERNOS_SHARED","ZANTHIR_INDUSTRIAL","BAY_ICE",
         "BOREAL_REGIONAL","ARLEON_FERTILE","CALERAN_LOWER","HORSE_BREEDING",
         "CAMINO_REAL_FOREST","RIBERAS_AGRARIAN","VALRIK_REFERENCE","VELARIS_EXTERNAL"]
JURIS = ["UNKNOWN","UNKNOWN","casa_galdren_context_only","UNKNOWN","UNKNOWN",
         "casa_galdren_context_only","UNKNOWN","UNKNOWN","UNKNOWN","UNKNOWN",
         "casa_valrik","UNKNOWN"]
CHAINS = ["CEREAL_BREAD","LEGUMES_GARDEN","DAIRY_EGGS","MEAT_PRESERVATION",
          "EQUINE_BREEDING","BEEKEEPING"]
CHAIN_INPUTS = [
    ["trigo","cebada","avena","centeno"],
    ["guisantes","habas","lentejas","cebolla","puerro","col","nabo","zanahoria","remolacha"],
    ["leche","aves_corral"],["vacuno","ovino","porcino"],
    ["pastos","forraje","agua","caballos"],["apicultura"]
]
CHAIN_OUTPUTS = [
    ["grano","harina","pan","gachas"],["guisos","conservas"],
    ["queso_fresco","queso_curado","mantequilla","huevos"],["carne","carne_conservada"],
    ["cria","trabajo","monturas"],["miel","cera","hidromiel"]
]
FLOW_PAIRS = [("arleon","entorno_caleran"),("bosque_quebrado","arleon"),
              ("bosque_riberas","mercado_oriental_no_identificado"),
              ("arleon","zanthir"),("arleon","hallheim"),("casa_galdren","casa_darovan")]
FLOW_KINDS = ["RURAL_PRODUCTION_STUDY","EQUINE_STUDY","RIPARIAN_STUDY",
              "FOOD_SUPPLY_STUDY","ROYAL_SUPPLY_STUDY","ECONOMIC_RIVALRY_STUDY"]
SERVICES = ["WATER_SOURCE_RURAL_REQUIREMENT","COMMUNAL_OVEN_COMMON",
            "MILL_OPTIONAL","TAVERN_SOCIAL_BASE","INN_OPTIONAL",
            "BEEKEEPING_NOT_UNIVERSAL","GRANARY_STUDY","FORMAL_MARKET_STUDY",
            "EQUINE_STABLE_STUDY"]
RISK_KINDS = ["VORNARSK_WINTER_FREEZE","KELDARSK_WINTER_FREEZE",
              "ZANTHIR_BAY_ICE","INVERNOS_SNOWMELT",
              "CALERAN_FLOOD_CROP_DAMAGE","BOSQUE_QUEBRADO_PASTURE_DROUGHT",
              "ARLEON_FROST_DAMAGE","ARLEON_ZANTHIR_SUPPLY_INTERRUPTION",
              "FOOD_STOCK_SPOILAGE","FORAGE_DEFICIT"]
CROP_GROUPS = {
    "cereals":["trigo","cebada","avena","centeno"],
    "legumes":["guisantes","habas","lentejas"],
    "vegetables":["cebolla","puerro","col","nabo","zanahoria","remolacha"],
    "fruit":["manzana","pera","ciruela","uva","frutos_bosque_categoria"],
    "animals":["vacuno","ovino","porcino","aves_corral"],
    "animalFoods":["huevos","leche","mantequilla","queso_fresco","queso_curado"],
    "other":["miel","sal","vinagre","hierbas_culinarias_categoria"],
}
UNKNOWN = [
    "GALDREN_LOCAL_CROPS","SOIL_AND_FIELD_PARCELS","CROP_YIELDS",
    "LOCAL_PLANTING_AND_HARVEST","HERD_COUNTS_AND_BREEDS","PASTURE_CARRYING_CAPACITY",
    "GRAIN_STORAGE_AND_MILLS","WATER_RIGHTS_AND_IRRIGATION","FOREST_OWNERSHIP",
    "TRADE_ROUTES_AND_CONTRACTS","FOOD_RESERVES_AND_SPOILAGE",
    "FISCAL_RATES_AND_REAL_REMITTANCES","CALERAN_WEST_EAST_TOPOLOGY",
    "ZANTHIR_NORTHERN_RIVER_OUTLETS","GDD-01","GDD-02","GDD-03","GDD-07"
]
SOURCES = [(N.relative_to(ROOT) / p).as_posix() for p in [
    "Grandes Casas/grandes_casas.md","Geografía/bosques.md",
    "Geografía/rios_y_lagos.md","Geografía/montanas.md",
    "Clima/clima_general.md","Sociedad/calendario_fechas_estaciones_norgard_v0.1.md",
    "Sociedad/gastronomia_alimentacion_norgard_v0.1.md",
    "Sociedad/aldeas_servicios_y_economia_local.md",
    "Gobierno y leyes/sistema_fiscal_y_aduanero_v0.1.md",
    "Gobierno y leyes/moneda_y_acunacion.md"
]] + [(H.relative_to(ROOT) / p).as_posix() for p in [
    "Datos operativos/galdren_g01_geography_v0.1.json",
    "Datos operativos/galdren_g02_hydrology_v0.1.json",
    "Datos operativos/galdren_g03_climate_soils_ecosystems_v0.1.json",
    "00_Control_del_proyecto/TRASPASO_G04.md","Suelos/G03_ATLAS_EDAFOLOGICO.md",
    "Ecosistemas/G03_ATLAS_ECOLOGICO.md"
]]

def validate(x):
    assert x["schemaVersion"] == 1 and x["documentId"] == "galdren_g04_agriculture_livestock_food"
    assert x["phase"] == "G04" and x["version"] == "0.1.0" and x["date"] == "2026-11-13"
    assert x["baselineMainSha"] == "0cec00d7b05a28972a9e6969279446aa0a6d119a"
    assert x["baseDocumentId"] == g3["documentId"] == "galdren_g03_climate_soils_ecosystems"
    assert x["status"] == "DOCUMENTARY_PLANNING_ONLY" and x["runtimeEnabled"] is False
    assert x["authorApproval"] == "G04_WORK_APPROVED_LOCAL_DETAILS_NOT_RATIFIED"
    assert x["inheritance"] == g0["inheritance"] == g1["inheritance"] == g2["inheritance"] == g3["inheritance"]
    assert len(g1["reliefUnits"]) == len(g3["reliefProfiles"]) == len(g3["soilStudies"]) == 12
    assert all(s["parcelSuitability"] == "UNASSESSED" for s in g3["soilStudies"])
    assert g2["caleran"]["westToEastLink"] == "TOPOGRAPHIC_ROUTE_UNRESOLVED"
    assert len(g2["rivers"]) == 5 and g3["ecologyGuard"]["mainHorseBreedingRegion"] == "bosque_quebrado"

    s=x["scope"]
    assert s["territory"]=="casa_galdren"
    no(s,["geoReferenced","parcelMapValidated","productionSimulated",
          "economyRuntimeEnabled","actualInventoriesVerified","localServicesMapped",
          "newTerritorialJurisdiction"])
    empty(s,["plotPolygons","roadPolylines","serviceCoordinates"])
    g=x["guardrails"]
    yes(g,["galdrenGranary","galdrenMostProductiveAgricultureLivestock","arleonGaldren",
           "zanthirGaldrenIndustrial","bosqueQuebradoMainHorseRegion","caleranOneRiver",
           "caleranWestBirth","vornarskKeldarskWinterFreeze","zanthirBayIce",
           "invernosShared","noHouseBorderCustoms","royalMintExclusive"])
    no(g,["caleranWestEastTopologyResolved","galdrenCoinExists"])
    for field in ["newRiversAdded","newCropsAdded","newHorseBreedsAdded","newSettlementsAdded"]:
        assert g[field]==0, "Alta de canon no autorizada: " + field
    assert g["metalEstelarOnly"]=="montes_azurios"
    assert g["treskalOwner"]=="casa_valrik" and g["dorthOwner"]=="casa_edranor"
    assert g["hallheimOwner"]=="crown_aethros"
    assert g["forjaOwner"]=="UNKNOWN" and g["forjaPeacetimeAdmin"]=="casa_galdren"
    assert g["forjaWartimeCommand"]=="crown_aethros_hallheim"

    civil=x["civilCalendar"]
    assert civil["authority"]=="NORGARD_CIVIL_POINT_12"
    assert civil["months"]==12 and civil["days"]==365 and civil["daysPerWeek"]==7
    assert civil["leapYear"] is False
    assert civil["seasonMonths"]==[
        {"season":"PRIMAVERA","months":[3,4,5]},
        {"season":"VERANO","months":[6,7,8]},
        {"season":"OTONO","months":[9,10,11]},
        {"season":"INVIERNO","months":[12,1,2]}]
    no(civil,["localAgronomicScheduleVerified","treskalLocalRoutineImported",
              "seasonChangeAutomaticallyCreatesHarvest"])
    unknown(civil,["localSowing","localHarvest"])

    catalog=x["cropAndFoodCatalog"]
    assert catalog["sourceScope"]=="NORGARD_COMMON_NOT_GALDREN_PARCELS"
    for key, items in CROP_GROUPS.items():
        assert catalog[key]==items and len(items)==len(set(items))
    no(catalog,["localPresenceOfEveryProduct","allCultivarsAssigned","allPlotsSuitable",
                "potatoCanon","wineSpecializationTakenFromEdranor"])
    null(catalog,["localHarvestStatistics"])

    eq=x["equine"]
    assert eq["region"]=="bosque_quebrado" and eq["status"]=="CANON_REPO"
    assert eq["uses"]==["reproduccion","trabajo_agricola","montura_aristocratica","guerra"]
    empty(eq,["breedsApproved","breedingFarmsKnown"])
    null(eq,["herdPopulation","pastureCapacity"])
    unknown(eq,["pastureOwnership"])
    no(eq,["horseMeatFoodAssumed"])

    econ=x["economy"]
    yes(econ,["galdrenKingdomGranary","confirmedRegionalAgriculture",
              "confirmedRegionalLivestock","confirmedGaldrenCrisisCanAffectKingdom"])
    no(econ,["crisisActuallyOccurred","everySettlementProducesAllFood",
             "localSpecificCropsVerified","localStorageFacilitiesConfirmed",
             "treskalLivestockDistributionImported","treskalAgrarianCalendarImported"])
    null(econ,["localProductionTonnes"])

    units=x["unitStudies"]
    ids(units,"G04-U",12)
    for i,u in enumerate(units):
        assert u["reliefUnitId"]==g1["reliefUnits"][i]["id"]
        assert u["g03ProfileId"]==g3["reliefProfiles"][i]["id"]
        assert u["studyKind"]==KINDS[i] and u["jurisdiction"]==JURIS[i]
        assert u["outsideHouseContext"] is (i>=10)
        assert u["regionalFoodProductivityReference"] is (i in [5,7,9])
        no(u,["politicalSubdivision","localPlotConfirmed","localCropConfirmed",
              "localHerdConfirmed","irrigationVerified","marketVerified","localRouteVerified"])
        assert u["localSoilSuitability"]=="UNASSESSED"
        null(u,["localYield","localAreaHa","localHerdCount"])

    chains=x["productionChains"]
    ids(chains,"G04-L",6)
    for i,c in enumerate(chains):
        assert c["kind"]==CHAINS[i] and c["inputs"]==CHAIN_INPUTS[i]
        assert c["outputs"]==CHAIN_OUTPUTS[i] and c["status"]=="MODEL_ONLY"
        no(c,["localIndustryConfirmed","localBuildingConfirmed","productionRecorded",
              "stockCreated","materialBalanceValidated","staffAssigned"])
        null(c,["quantities"])

    flows=x["tradeFlowStudies"]
    ids(flows,"G04-F",6)
    for i,f in enumerate(flows):
        assert (f["from"],f["to"])==FLOW_PAIRS[i]
        assert f["kind"]==FLOW_KINDS[i] and f["status"]=="STUDY_ONLY"
        no(f,["roadVerified","riverNavigableVerified","tradeContractConfirmed",
              "shipmentRecorded","internalCustoms"])
        assert f["routeGeometry"]==[]
        null(f,["distanceKm","tradeVolume"])

    services=x["ruralServiceStudies"]
    ids(services,"G04-I",9)
    for i,item in enumerate(services):
        assert item["kind"]==SERVICES[i] and item["scope"]=="NORGARD_MODEL_OR_STUDY"
        no(item,["galdrenInstanceValidated","automaticallyCreated","treskalOverrideImported"])
        unknown(item,["location","owner"])
        null(item,["capacity"])

    preserv=x["foodPreservation"]
    assert preserv["scope"]=="NORGARD_GENERAL"
    assert preserv["methods"]==["secado","salazon","salmuera","ahumado",
                               "encurtido","fermentacion","almacenamiento_fresco_condicional"]
    null(preserv,["shelfLifeDays"])
    no(preserv,["localFacilitiesConfirmed","stockRuntime"])

    tax=x["fiscal"]
    assert tax["coinUnit"]=="clavo" and tax["lunaClavos"]==24 and tax["coronaClavos"]==480
    yes(tax,["crownMintOnly","kindPaymentRequiresAuthorization"])
    no(tax,["norgardInternalCustoms","houseRemittancesRegistered",
            "routineSaleTaxByDefault","royalEmergencyLevyDeclared"])
    null(tax,["universalTaxRate"])
    risks=x["riskStudies"]
    ids(risks,"G04-R",10)
    for i,r in enumerate(risks):
        assert r["kind"]==RISK_KINDS[i]
        assert r["evidence"] == ("CANON_QUALITATIVE" if i<3 else
                                 "REGIONAL_DRAFT_QUALITATIVE" if i==3 else "STUDY_ONLY")
        assert r["baseFactConfirmed"] is (i<3)
        no(r,["localEconomicLossConfirmed","actualEventRecorded","runtimeEnabled"])
        unknown(r,["frequency"])
        assert r["affectedAreasVerified"]==[]
        null(r,["probability","loss"])

    assert x["unknown"]==UNKNOWN
    assert x["sourceRegistry"]==SOURCES and len(set(SOURCES))==16
    for source in SOURCES:
        assert (ROOT / source).is_file(),"Fuente no encontrada: "+source

validate(g4)
# Evidencia contra las fuentes, no solo autorreferencia del contrato.
cal=(N/"Sociedad/calendario_fechas_estaciones_norgard_v0.1.md").read_text(encoding="utf-8")
food=(N/"Sociedad/gastronomia_alimentacion_norgard_v0.1.md").read_text(encoding="utf-8")
rural=(N/"Sociedad/aldeas_servicios_y_economia_local.md").read_text(encoding="utf-8")
houses=(N/"Grandes Casas/grandes_casas.md").read_text(encoding="utf-8")
forest=(N/"Geografía/bosques.md").read_text(encoding="utf-8")
for mark in ["CALENDAR_POINT_12_CLOSED_NORGARD_CIVIL_CALENDAR",
             "365 días","marzo","septiembre"]:
    assert mark in cal,"Canon civil incompleto: "+mark
for mark in ["trigo","cebada","avena","centeno","guisantes","habas","lentejas",
             "cebolla","nabo","remolacha","No se canoniza patata",
             "## 31. Territorio Galdren"]:
    assert mark in food,"Alimento no respaldado en FOOD: "+mark
for mark in ["Norgard/Treskal/village","norgard.rural.mill",
             "norgard.rural.communal_oven","apicultura"]:
    assert mark in rural,"Modelo rural no encontrado: "+mark
for mark in ["granero de Norgard","Zanthir","rivalidad"]:
    assert mark in houses,"Marco Galdren no encontrado: "+mark
assert "principal región caballar de Norgard" in forest
mandatory=[
"G04_INDICE.md","Economia/G04_ATLAS_PRODUCTIVO.md",
"Agricultura/G04_CULTIVOS_Y_CICLOS.md","Ganaderia/G04_GANADERIA_Y_CABALLOS.md",
"Economia/G04_CADENAS_Y_CONSERVACION.md",
"Economia/G04_ABASTECIMIENTO_COMERCIO_FISCALIDAD.md",
"Riesgos/G04_ESTACIONALIDAD_Y_RIESGOS.md",
"Auditorias/G04_FUENTES_Y_DEUDA.md","Auditorias/G04_ACTA.md",
"00_Control_del_proyecto/TRASPASO_G05.md",
"Datos operativos/galdren_g04_agriculture_livestock_food_v0.1.json"]
for relative in mandatory:
    assert (H/relative).is_file(),"Entrega no encontrada: "+relative
assert (ROOT/".github/workflows/galdren-g04.yml").is_file()
assert "G04_INDICE.md" in (H/"README.md").read_text(encoding="utf-8")

def alter(path,value):
    def fn(d):
        z=d
        for k in path[:-1]: z=z[k]
        z[path[-1]]=value
    return fn
cases=[
(["schemaVersion"],2),(["documentId"],"otro"),(["phase"],"G05"),
(["version"],"1.0"),(["date"],"2027-01-01"),(["baselineMainSha"],"deadbeef"),
(["baseDocumentId"],"galdren_g02"),(["runtimeEnabled"],True),
(["status"],"RUNTIME_READY"),(["authorApproval"],"ALL_RATIFIED"),
(["inheritance",0],"casa_galdren"),
(["scope","territory"],"casa_valrik"),(["scope","geoReferenced"],True),
(["scope","parcelMapValidated"],True),(["scope","productionSimulated"],True),
(["scope","economyRuntimeEnabled"],True),(["scope","actualInventoriesVerified"],True),
(["scope","localServicesMapped"],True),(["scope","newTerritorialJurisdiction"],True),
(["scope","plotPolygons"],[[2,3]]),(["scope","roadPolylines"],[[2,3]]),
(["scope","serviceCoordinates"],[[5,6]]),
(["guardrails","galdrenGranary"],False),(["guardrails","caleranOneRiver"],False),
(["guardrails","caleranWestBirth"],False),
(["guardrails","caleranWestEastTopologyResolved"],True),
(["guardrails","zanthirBayIce"],False),(["guardrails","invernosShared"],False),
(["guardrails","newRiversAdded"],1),(["guardrails","newCropsAdded"],1),
(["guardrails","newHorseBreedsAdded"],1),(["guardrails","newSettlementsAdded"],1),
(["guardrails","metalEstelarOnly"],"zanthir"),
(["guardrails","treskalOwner"],"casa_galdren"),
(["guardrails","dorthOwner"],"casa_galdren"),
(["guardrails","hallheimOwner"],"casa_galdren"),
(["guardrails","forjaOwner"],"casa_galdren"),
(["guardrails","forjaWartimeCommand"],"casa_galdren"),
(["guardrails","noHouseBorderCustoms"],False),
(["guardrails","galdrenCoinExists"],True),
(["civilCalendar","months"],13),(["civilCalendar","days"],366),
(["civilCalendar","leapYear"],True),
(["civilCalendar","seasonMonths",0,"months"],[2,3,4]),
(["civilCalendar","seasonMonths",3,"months"],[11,12,1]),
(["civilCalendar","localAgronomicScheduleVerified"],True),
(["civilCalendar","localSowing"],"2026-03-01"),
(["civilCalendar","treskalLocalRoutineImported"],True),
(["civilCalendar","seasonChangeAutomaticallyCreatesHarvest"],True),
(["cropAndFoodCatalog","sourceScope"],"GALDREN_UNIVERSAL"),
(["cropAndFoodCatalog","cereals"],["trigo","patata"]),
(["cropAndFoodCatalog","vegetables"],["patata"]),
(["cropAndFoodCatalog","animals"],["unicornio"]),
(["cropAndFoodCatalog","localPresenceOfEveryProduct"],True),
(["cropAndFoodCatalog","potatoCanon"],True),
(["cropAndFoodCatalog","wineSpecializationTakenFromEdranor"],True),
(["cropAndFoodCatalog","localHarvestStatistics"],12000),
(["equine","region"],"zanthir"),(["equine","breedsApproved"],["raza_inventada"]),
(["equine","herdPopulation"],10000),(["equine","breedingFarmsKnown"],["granja_inventada"]),
(["equine","horseMeatFoodAssumed"],True),
(["economy","crisisActuallyOccurred"],True),
(["economy","everySettlementProducesAllFood"],True),
(["economy","localSpecificCropsVerified"],True),
(["economy","treskalLivestockDistributionImported"],True),
(["unitStudies",0,"reliefUnitId"],"G01-U12"),
(["unitStudies",5,"localSoilSuitability"],"APTO"),
(["unitStudies",7,"localHerdCount"],1500),
(["unitStudies",7,"jurisdiction"],"casa_galdren"),
(["unitStudies",10,"outsideHouseContext"],False),
(["unitStudies",6,"localRouteVerified"],True),
(["productionChains",0,"kind"],"GOLD_FARMING"),
(["productionChains",1,"status"],"OPERATING"),
(["productionChains",2,"productionRecorded"],True),
(["productionChains",3,"stockCreated"],True),
(["productionChains",4,"quantities"],1000),
(["productionChains",5,"localBuildingConfirmed"],True),
(["tradeFlowStudies",0,"roadVerified"],True),
(["tradeFlowStudies",1,"shipmentRecorded"],True),
(["tradeFlowStudies",2,"tradeVolume"],1000),
(["tradeFlowStudies",3,"routeGeometry"],[[1,2]]),
(["tradeFlowStudies",4,"tradeContractConfirmed"],True),
(["tradeFlowStudies",5,"internalCustoms"],True),
(["ruralServiceStudies",0,"galdrenInstanceValidated"],True),
(["ruralServiceStudies",1,"location"],"Arleon 1"),
(["ruralServiceStudies",2,"automaticallyCreated"],True),
(["ruralServiceStudies",3,"treskalOverrideImported"],True),
(["ruralServiceStudies",8,"capacity"],5),
(["foodPreservation","shelfLifeDays"],999),
(["foodPreservation","stockRuntime"],True),
(["fiscal","norgardInternalCustoms"],True),
(["fiscal","universalTaxRate"],0.15),
(["fiscal","coinUnit"],"moneda_galdren"),
(["fiscal","coronaClavos"],500),
(["fiscal","royalEmergencyLevyDeclared"],True),
(["riskStudies",0,"evidence"],"STUDY_ONLY"),
(["riskStudies",3,"evidence"],"CANON_QUALITATIVE"),
(["riskStudies",4,"evidence"],"CANON_QUALITATIVE"),
(["riskStudies",5,"localEconomicLossConfirmed"],True),
(["riskStudies",6,"loss"],42),
(["riskStudies",7,"actualEventRecorded"],True),
(["riskStudies",8,"frequency"],"ANUAL"),
(["riskStudies",9,"runtimeEnabled"],True),
(["unknown",0],"VERIFIED"),
(["sourceRegistry",0],"falsa.md"),
]
attacks=[alter(path,value) for path,value in cases]
attacks.extend([
    lambda x:x["unitStudies"].append(copy.deepcopy(x["unitStudies"][0])),
    lambda x:x["productionChains"].append(copy.deepcopy(x["productionChains"][0])),
    lambda x:x["tradeFlowStudies"].append(copy.deepcopy(x["tradeFlowStudies"][0])),
    lambda x:x["ruralServiceStudies"].append(copy.deepcopy(x["ruralServiceStudies"][0])),
    lambda x:x["riskStudies"].append(copy.deepcopy(x["riskStudies"][0])),
    lambda x:x["sourceRegistry"].pop(),
    lambda x:x["unknown"].pop(),
])
for i,change in enumerate(attacks,1):
    y=copy.deepcopy(g4)
    change(y)
    try: validate(y)
    except (AssertionError,KeyError,IndexError,TypeError): continue
    raise AssertionError(f"Ataque negativo aceptado: {i}")
print("GALDREN G04 STATIC PASS | 12 unidades | 6 cadenas | 6 flujos | 9 servicios | 10 riesgos | %d mutaciones negativas | documental" % len(attacks))

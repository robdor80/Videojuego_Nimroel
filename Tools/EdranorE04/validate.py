"""E04 Edranor: contrato documental; NO verifica simulación ni motor."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
B = N / "Territorios/Casa Edranor"
load = lambda p: json.loads(p.read_text(encoding="utf-8"))
e00 = load(B / "Datos operativos/edranor_e00_manifest_v0.1.json")
e01 = load(B / "Datos operativos/edranor_e01_relief_v0.1.json")
e02 = load(B / "Datos operativos/edranor_e02_hydrology_v0.1.json")
e03 = load(B / "Datos operativos/edranor_e03_climate_soils_ecosystems_v0.1.json")
data = load(B / "Datos operativos/edranor_e04_economy_viticulture_v0.1.json")
LAYERS = ["nimroel_core","norgard_defaults","casa_edranor","localidad","world_state"]
AUTHORITIES = {"CANON_REPO","AUTOR_2026_11_12","OBSERVACION_MAPA","PROPUESTA","UNKNOWN"}
UNITS = {x["id"] for x in e01["reliefUnits"]}
ANCHORS = {"dorth","lumina","karsath","rodas","hallheim"}
STAGES = [
 ("vine_preflight","VINE","PRECONDITION",["parcel_title","soil_climate_evidence","water_rights_if_needed"],["eligible_parcel_if_approved"]),
 ("cultivate","VINE","OPTIONAL_PROCESS",["eligible_parcel_if_approved","plant_material","labor","tools"],["grape_crop_if_world_state"]),
 ("harvest","VINE","OPTIONAL_PROCESS",["grape_crop_if_world_state","labor","containers"],["grape_lot"]),
 ("sort_crush","CELLAR","OPTIONAL_PROCESS",["grape_lot","pressing_tools"],["must_lot","pomace_lot"]),
 ("ferment","CELLAR","OPTIONAL_PROCESS",["must_lot","suitable_vessel","labor"],["young_wine_lot","lees_lot"]),
 ("care_age","CELLAR","OPTIONAL_PROCESS",["young_wine_lot","storage_capacity"],["finished_wine_lot"]),
 ("pack_store","CELLAR","OPTIONAL_PROCESS",["finished_wine_lot","clean_vessels","legitimate_storage"],["market_wine_lot"]),
 ("distribute","TRADE","OPTIONAL_PROCESS",["market_wine_lot","owner_consent","commercial_contract","transport_capacity"],["delivered_wine_lot"]),
 ("sell","TRADE","OPTIONAL_PROCESS",["delivered_wine_lot","buyer","lawful_transaction"],["transfer_record"]),
 ("legal_harvest_wood","WOOD","PRECONDITION",["verified_title_or_harvest_permission","forest_stewardship","labor"],["authorized_wood_lot"]),
 ("season_shape_wood","WOOD","OPTIONAL_PROCESS",["authorized_wood_lot","craft_tools","workshop_capacity"],["prepared_staves_or_timber"]),
 ("cooper_build","WOOD","OPTIONAL_PROCESS",["prepared_staves_or_timber","hoops_and_fittings","artisan_labor"],["barrel_or_cask_lot"]),
 ("maintain_vessels","WOOD","OPTIONAL_PROCESS",["barrel_or_cask_lot","maintenance_labor"],["usable_vessels"]),
 ("vinegar_byproduct","CELLAR","OPTIONAL_PROCESS",["suitable_fermented_lot","vessel","controlled_process"],["vinegar_lot"]),
]
ROLES = {"grower","cellarer","cooper","woodsman","carrier","merchant","clerk"}
TRADE = {
 "dorth_lumina": ("dorth","lumina"),
 "lumina_karsath": ("lumina","karsath"),
 "dorth_karsath": ("dorth","karsath"),
 "edranor_rodas": ("casa_edranor","rodas"),
 "edranor_realm": ("casa_edranor","norgard_commercial_network"),
}
UNKNOWNS = {
 "EDD-01_NORTH_BOUNDARY_CLOSURE","EDD-02_GEOREFERENCING_AND_SCALE",
 "EDD-03_LOCAL_WATER_AND_GROUNDWATER","EDD-07_ACCESS_AND_PATHS",
 "LOCAL_PARCELS_AND_OWNERSHIP","LOCAL_SOIL_CLIMATE_PHENOLOGY",
 "WINE_VARIETIES_AND_YIELD","WINE_PRICE_SPECIFIC",
 "CELLAR_LOCATIONS_CAPACITIES","FOREST_HARVEST_RIGHTS_QUOTAS",
 "WOOD_SPECIES_PER_BARREL","LOCAL_MARKETS_AND_GUILD_EXISTENCE",
 "SPECIFIC_FISCAL_TARIFFS","SEASONAL_VINTAGE_DATE",
 "RODAS_ECONOMIC_RELATIONSHIP_DETAILS",
}
FORBIDDEN = {
 "RODAS_EDRANOR_FISCAL_CONTROL","HALLHEIM_EDRANOR","E04_RUNTIME_ENABLED",
 "EACH_UNIT_HAS_VINEYARDS","POLAR_VINEYARDS_DEFAULT","LOCAL_WINE_TAX_AS_CANON",
 "INTERNAL_HOUSE_CUSTOMS","UNVERIFIED_FOREST_OWNERSHIP","ROYAL_FOREST_EDRANOR",
 "DIRECT_RIVER_WINE_ROUTE","FABRICATED_TRADE_ROADS",
 "NUMERIC_HARVEST_OUTPUT_AS_CANON","UNAUTHORIZED_TIMBER_CUTTING",
 "INVENTORY_WITHOUT_WORLD_STATE",
}
SCOPES_FALSE = (
 "northBoundaryClosed","georeferenced","metricGeometryValidated",
 "parcelMapValidated","productionMapValidated","transportGraphValidated",
 "riverTransportValidated","settlementEconomiesInstantiated","localMarketsInstantiated",
)
GUARDS_FALSE = (
 "allSevenUnitsAreVineyards","polarViticultureByDefault",
 "irrigationEstablished","wineRiverTransportEstablished","roadsEstablished",
 "woodHarvestWithoutRightsAllowed","edranorOwnsAllLand",
 "edranorControlsRoyalForest","rodasIsEdranorTaxDistrict",
 "internalHouseTollsAsCustoms","fictionalVineyardVolumesAsFact",
 "simulationOrCoreIntegration",
)
MONEY_TRUE = (
 "singleNorgardMarket","noInternalHouseCustoms","crownIsSupremeFiscalAuthority",
 "edranorMayCollectAuthorizedTaxesOnly","berserkersUnderCrown",
 "goodsRequiresRealInventory","tradeRequiresRealContractAndRights",
)
MONEY_UNKNOWN = (
 "localWineTaxRate","approvedMarketServiceTariffs","remittanceShareToCrown",
 "wineUnitPrice","productionCost","wagesSpecificToEdranor",
)

def index(entries):
    assert isinstance(entries,list)
    assert all(isinstance(x,dict) and isinstance(x.get("id"),str) for x in entries)
    ids=[x["id"] for x in entries]
    assert len(ids)==len(set(ids)), "Identificador duplicado"
    return {x["id"]:x for x in entries}

def check(v):
    assert v["schemaVersion"] == 1
    assert v["documentId"] == "edranor_e04_economy_viticulture"
    assert v["version"] == "0.1" and v["date"] == "2026-11-12"
    assert v["phase"] == "E04" and v["status"] == "DOCUMENTARY_PLANNING_ONLY"
    assert v["runtimeEnabled"] is False and v["inheritance"] == LAYERS
    assert set(v["sourceAuthorities"]) == AUTHORITIES
    assert len(v["sourceAuthorities"]) == len(AUTHORITIES)
    # Regresión de contratos anteriores.
    assert e00["house"]["seatId"] == "dorth"
    assert set(e00["protectedIds"]) == ANCHORS
    assert {x["id"] for x in e01["reliefUnits"]} == UNITS and len(UNITS)==7
    assert e01["cartography"]["northBoundaryClosed"] is False
    assert e02["scope"]["localHydrographyValidated"] is False
    assert e03["scope"]["localSoilsMapped"] is False
    assert e03["landUseRules"]["allSevenUnitsViticultural"] is False

    s=v["scope"]
    assert s["territory"]=="casa_edranor" and s["regionalCanon"]=="norgard"
    for k in SCOPES_FALSE: assert s[k] is False, k
    for k in ("productionPolygons","vineyardPolygons","roadEdges","riverEdges"): assert s[k] == [],k
    for k in ("coordinates","area","localHydrography"): assert s[k]=="UNKNOWN",k

    c=v["canonicalBasis"]
    for k in ("primaryNorgardWineRegion","realmWineTradeExists",
              "luminaBosqueAltoSuppliesWineIndustryWood","forestExploitationControlled",
              "dorthPoliticalSeat","luminaAndKarsathRelevant","grapesCanonicalFood"):
        assert c[k] is True,k
    assert c["wineTypesCanonicalPossibilities"]==[
       "WINE_COMMON","WINE_HIGH_QUALITY","WINE_YOUNG",
       "WINE_AGED","WINE_COOKED_OR_SPICED"]
    assert c["wineCategoriesAreGuaranteedLocalStock"] is False
    assert c["individualWineProducersNamed"] is False and c["evidence"]=="CANON_REPO"

    f=v["forestGuard"]
    assert f["sourceForest"]=="bosque_alto" and f["associatedTown"]=="lumina"
    assert f["confirmedApplications"]==["TONEL","BARRICA","BODEGA_STRUCTURE","OTHER_WINE_STORAGE"]
    assert f["forestParcelsValidated"] is False and f["authorizedHarvestSites"]==[]
    assert f["azuriosRealSouthAssignedToEdranor"] is False
    assert f["forestProcessingSitesConfirmed"] is False
    for k in ("specificTreeToBarrelSpecies","rightsHolder","harvestQuota",
              "replantingPolicy","forestIsOwnedByEdranor"): assert f[k]=="UNKNOWN",k
    assert f["evidence"]=="CANON_REPO"

    anchors=index(v["anchors"])
    assert set(anchors)==ANCHORS
    for id in ANCHORS:
        a=anchors[id]
        owner="crown_aethros" if id in ("rodas","hallheim") else "casa_edranor"
        assert a["owner"]==owner
        assert a["inside"] is (id!="hallheim")
        assert a["taxAuthority"]==("crown_aethros" if owner=="crown_aethros" else "casa_edranor_under_crown")
        assert a["productionSitesConfirmed"] is False
        for k in ("localMarketInfrastructure","wineInventories","priceList","roadAccess"):
            assert a[k]=="UNKNOWN",(id,k)
        assert a["evidence"]==("AUTOR_2026_11_12" if id=="rodas" else "CANON_REPO")

    units=index(v["territorialStudies"])
    assert len(units)==7
    assert set(units)=={"edr_e04_study_"+u.removeprefix("edr_e01_") for u in UNITS}
    assert {x["reliefUnitId"] for x in units.values()}==UNITS
    for id,x in units.items():
        assert id=="edr_e04_study_"+x["reliefUnitId"].removeprefix("edr_e01_")
        assert x["siteParcel"]=="UNKNOWN" and x["eligibility"]=="UNASSESSED"
        assert x["localWineProductionConfirmed"] is False
        assert x["soilAndMicroclimateValidated"] is False
        assert x["jurisdictionVerified"] is False and x["evidence"]=="PROPUESTA"
        for k in ("hectares","yieldPerHectare","irrigation","transportInfrastructure"):
            assert x[k]=="UNKNOWN",(id,k)

    actual=index(v["chainStages"])
    assert len(actual)==len(STAGES)
    assert set(actual)=={"edr_e04_"+s for s,*_ in STAGES}
    for suffix,lane,klass,inputs,outputs in STAGES:
        x=actual["edr_e04_"+suffix]
        assert x["lane"]==lane and x["stageClass"]==klass
        assert x["inputs"]==inputs and x["outputs"]==outputs
        assert x["implementation"]=="DESIGN_ONLY" and x["active"] is False
        for k in ("locality","operator","quantity","processTime","rights"): assert x[k]=="UNKNOWN",k
        assert x["evidence"]=="PROPUESTA"

    roles=index(v["professionsStudy"])
    assert set(roles)=={"edr_e04_role_"+r for r in ROLES}
    role_names={"grower":"VINEYARD_WORK","cellarer":"FERMENT_AND_STORE",
      "cooper":"WOODEN_VESSELS","woodsman":"AUTHORIZED_FOREST_WORK",
      "carrier":"GOODS_TRANSPORT","merchant":"WHOLESALE_OR_MARKET",
      "clerk":"CONTRACT_AND_RECORD"}
    for id,r in roles.items():
        assert r["role"]==role_names[id.removeprefix("edr_e04_role_")]
        assert r["siteConfirmed"] is False and r["workforce"]=="UNKNOWN"
        assert r["evidence"]=="PROPUESTA"

    trade=index(v["tradeStudy"])
    assert set(trade)=={"edr_e04_trade_question_"+x for x in TRADE}
    for short,(a,b) in TRADE.items():
        x=trade["edr_e04_trade_question_"+short]
        assert x["from"]==a and x["to"]==b
        assert x["commercialLinkVerified"] is False
        for k in ("physicalRoute","travelTime","transshipment",
                  "commodityVolume","authorizedAtBoundary"): assert x[k]=="UNKNOWN",k
        assert x["evidence"]=="PROPUESTA"

    g=v["economicRules"]
    for k in MONEY_TRUE: assert g[k] is True,k
    for k in ("localMintAllowed","hallheimInsideEdranor","wineSalesAtRodasUnderEdranorTax"):
        assert g[k] is False,k
    assert g["rodasFiscalOwner"]==g["rodasMilitaryOwner"]=="crown_aethros"
    assert g["currencyAccountingUnit"]=="CLAVO"
    assert g["clavosPerLuna"]==24 and g["clavosPerCorona"]==480
    for k in MONEY_UNKNOWN: assert g[k]=="UNKNOWN",k
    assert g["evidence"]=="CANON_REPO"

    guards=v["guardrails"]
    for k in GUARDS_FALSE: assert guards[k] is False,k
    assert set(v["unknown"])==UNKNOWNS and len(v["unknown"])==len(UNKNOWNS)
    assert set(v["forbiddenClaims"])==FORBIDDEN and len(v["forbiddenClaims"])==len(FORBIDDEN)

# Comprobaciones independientes sobre los textos de origen; no solo sobre el JSON.
sources={
 "houses": N / "Grandes Casas/grandes_casas.md",
 "woods": N / "Geografía/bosques.md",
 "food": N / "Sociedad/gastronomia_alimentacion_norgard_v0.1.md",
 "tax": N / "Gobierno y leyes/sistema_fiscal_y_aduanero_v0.1.md",
 "money": N / "Gobierno y leyes/moneda_y_acunacion.md",
 "property": N / "Gobierno y leyes/propiedad_herencia_alquiler_v0.1.md",
 "rural": N / "Sociedad/aldeas_servicios_y_economia_local.md",
}
marks={
 "houses":["principal zona vinícola","Rodas","Lumina","Karsath"],
 "woods":["Bosque Alto","toneles;","barricas;","controlada","Bosque Real"],
 "food":["El vino circula por Norgard mediante comercio","vino envejecido","uva"],
 "tax":["No existen aduanas","parte estipulada"],
 "money":["1 Luna = 24 Clavos","1 Corona = 480 Clavos"],
 "property":["no equivale automáticamente a título privado"],
 "rural":["hogar local -> vecino"],
}
for source,path in sources.items():
    body=path.read_text(encoding="utf-8")
    for needle in marks[source]:
        assert needle in body,(source,needle)

required=[
 B/"E04_INDICE.md", B/"Economia/E04_CADENA_UVA_VINO_BODEGA.md",
 B/"Economia/E04_COMERCIO_FISCALIDAD.md",
 B/"Economia/E04_OFICIOS_Y_RED_PRODUCTIVA.md",
 B/"Economia/E04_MATRIZ_LOCALIDADES_Y_FLUJOS.md",
 B/"Viticultura/E04_VITICULTURA_Y_VENDIMIA.md",
 B/"Toneleria/E04_BOSQUE_ALTO_Y_TONELERIA.md",
 B/"Auditorias/E04_FUENTES_Y_DECISIONES.md", B/"Auditorias/E04_ACTA.md",
 B/"00_Control_del_proyecto/TRASPASO_E05.md",
 B/"Datos operativos/edranor_e04_economy_viticulture_v0.1.json",
 ROOT/"Tools/EdranorE04/validate.py", ROOT/".github/workflows/edranor-e04.yml",
]
for p in required:
    assert p.is_file() and p.stat().st_size>50,f"Falta {p}"

check(data)

# Pruebas negativas: cada alteración crítica debe ser rechazada sin excepción.
tests=[]
def mutate(path,value):
    tests.append((path,value))
for k,val in [
 ("schemaVersion",2),("documentId","otro"),("version","0.2"),
 ("date","2000-01-01"),("phase","E05"),("status","ACTIVE"),
 ("runtimeEnabled",True),("inheritance",list(reversed(LAYERS))),
 ("sourceAuthorities",["CANON_REPO"]),
 ("unknown",[]),("forbiddenClaims",[]),
]: mutate([k],val)
for k in SCOPES_FALSE: mutate(["scope",k],True)
for k in ("productionPolygons","vineyardPolygons","roadEdges","riverEdges"):
    mutate(["scope",k],[{"falso":True}])
for k in ("territory","regionalCanon","coordinates","area","localHydrography"):
    mutate(["scope",k],"FABRICATED")
for k in ("primaryNorgardWineRegion","realmWineTradeExists",
          "luminaBosqueAltoSuppliesWineIndustryWood","forestExploitationControlled",
          "dorthPoliticalSeat","luminaAndKarsathRelevant","grapesCanonicalFood"):
    mutate(["canonicalBasis",k],False)
for k,val in [("wineCategoriesAreGuaranteedLocalStock",True),
 ("individualWineProducersNamed",True),("evidence","PROPUESTA"),
 ("wineTypesCanonicalPossibilities",["WINE_POLAR"])]:
    mutate(["canonicalBasis",k],val)
for k,val in [("sourceForest","bosque_azurios"),("associatedTown","rodas"),
 ("confirmedApplications",[]),("forestParcelsValidated",True),
 ("authorizedHarvestSites",["illegal_cut"]),("specificTreeToBarrelSpecies","OAK_CONFIRMED"),
 ("rightsHolder","casa_edranor"),("harvestQuota",100),("replantingPolicy","CONFIRMED"),
 ("forestIsOwnedByEdranor",True),("azuriosRealSouthAssignedToEdranor",True),
 ("forestProcessingSitesConfirmed",True),("evidence","PROPUESTA")]:
    mutate(["forestGuard",k],val)
for i,a in enumerate(data["anchors"]):
    for k,val in [("owner","usurper"),("inside",not a["inside"]),
                  ("taxAuthority","usurper"),("productionSitesConfirmed",True),
                  ("localMarketInfrastructure","BUILT"),
                  ("wineInventories",500),("priceList",[10]),
                  ("roadAccess","ROAD"),("evidence","UNKNOWN")]:
        mutate(["anchors",i,k],val)
for i,s in enumerate(data["territorialStudies"]):
    for k,val in [("reliefUnitId","MISSING"),("siteParcel","parcel_confirmed"),
                  ("eligibility","APTO"),("localWineProductionConfirmed",True),
                  ("soilAndMicroclimateValidated",True),
                  ("jurisdictionVerified",True),("hectares",100),
                  ("yieldPerHectare",100),("irrigation","CONFIRMED"),
                  ("transportInfrastructure","ROAD"),("evidence","CANON_REPO")]:
        mutate(["territorialStudies",i,k],val)
for i,s in enumerate(data["chainStages"]):
    for k,val in [("lane","INVALID"),("stageClass","CANON_PROCESS"),
                  ("inputs",[]),("outputs",[]),("implementation","LIVE"),
                  ("active",True),("locality","dorth"),("operator","NPC_1"),
                  ("quantity",100),("processTime",15),("rights","APPROVED"),
                  ("evidence","CANON_REPO")]:
        mutate(["chainStages",i,k],val)
for i,r in enumerate(data["professionsStudy"]):
    for k,val in [("role","INVALID"),("siteConfirmed",True),
                  ("workforce",20),("evidence","CANON_REPO")]:
        mutate(["professionsStudy",i,k],val)
for i,r in enumerate(data["tradeStudy"]):
    for k,val in [("from","hallheim"),("to","incorrect"),
                  ("commercialLinkVerified",True),("physicalRoute","ROAD"),
                  ("travelTime",60),("transshipment","RIVER"),
                  ("commodityVolume",1000),("authorizedAtBoundary","YES"),
                  ("evidence","CANON_REPO")]:
        mutate(["tradeStudy",i,k],val)
for k in MONEY_TRUE: mutate(["economicRules",k],False)
for k in ("localMintAllowed","hallheimInsideEdranor","wineSalesAtRodasUnderEdranorTax"):
    mutate(["economicRules",k],True)
for k in ("rodasFiscalOwner","rodasMilitaryOwner"): mutate(["economicRules",k],"casa_edranor")
for k,val in [("currencyAccountingUnit","DUCADO"),("clavosPerLuna",10),
              ("clavosPerCorona",500),("evidence","PROPUESTA")]:
    mutate(["economicRules",k],val)
for k in MONEY_UNKNOWN: mutate(["economicRules",k],100)
for k in GUARDS_FALSE: mutate(["guardrails",k],True)
for key in ("anchors","chainStages","territorialStudies","professionsStudy","tradeStudy"):
    mutate([key],data[key]+[copy.deepcopy(data[key][0])])
for n,(path,val) in enumerate(tests,1):
    clone=copy.deepcopy(data)
    ref=clone
    for key in path[:-1]: ref=ref[key]
    ref[path[-1]]=val
    try:
        check(clone)
    except (AssertionError,KeyError,TypeError,ValueError):
        pass
    else:
        raise AssertionError(f"Mutación no detectada #{n}: {path}")
print(f"E04 OK | {len(tests)} mutaciones negativas rechazadas | contrato documental; sin gameplay")

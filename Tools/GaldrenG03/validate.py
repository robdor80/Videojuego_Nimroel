"""GALDREN G03: comprobación documental y mutaciones negativas. No runtime."""
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
CLIMATES = ["ORIENTAL_INTERIOR_CONTINENTAL", "ORIENTAL_COASTAL_OCEANIC",
            "NORTH_INTERIOR_CONTINENTAL_COLD", "FAR_NORTH_POLAR_AND_BOREAL_TRANSITION",
            "ZANTHIR_BAY_AND_NORTHERN_WINTER_ICE", "AZURIOS_OROGRAPHIC_MICROCLIMATES",
            "INVERNOS_SNOW_AND_THAW"]
CTX = [
    ("MOUNTAIN_AZURIOS", "G03-C06", "AZURIOS_FOREST_REGIONAL", "MOUNTAIN_SAMPLE"),
    ("INVERNOS_SHARED", "G03-C07", "INVERNOS_REGIONAL", "MOUNTAIN_SAMPLE"),
    ("ZANTHIR_INTERIOR", "G03-C03", "UNKNOWN", "INDUSTRIAL_SOIL_STUDY"),
    ("ZANTHIR_BAY", "G03-C05", "UNKNOWN", "COASTAL_SOIL_STUDY"),
    ("NORGARD_BOREAL", "G03-C04", "BOREAL_NORGARD", "BOREAL_SAMPLE"),
    ("ARLEON_CALERAN", "G03-C01", "AGRICULTURAL_PLAINS", "FERTILE_PLAINS_REGIONAL"),
    ("CALERAN_LOWER", "G03-C02", "CALERAN_LOWER_BASIN", "ALLUVIAL_PARCEL_STUDY"),
    ("BOSQUE_QUEBRADO", "G03-C01", "BOSQUE_QUEBRADO", "PASTURE_AND_WOODLAND_SAMPLE"),
    ("BOSQUE_CAMINO_REAL", "UNKNOWN", "BOSQUE_CAMINO_REAL", "WOODLAND_AND_SLOPE_SAMPLE"),
    ("BOSQUE_RIBERAS", "G03-C01", "BOSQUE_RIBERAS", "ALLUVIAL_PARCEL_STUDY"),
    ("VALRIK_TRESKAL_REFERENCE", "UNKNOWN", "BOSQUE_GEMELOS_VALRIK", "NEIGHBOR_REFERENCE_ONLY"),
    ("VELARIS_VARETH_OUTSIDE", "UNKNOWN", "EXTERNAL_CONTEXT", "OUTSIDE_HOUSE_REFERENCE_ONLY"),
]
ECO = ["bosque_quebrado", "bosque_caminoreal", "bosque_riberas",
       "bosque_azurios", "boreal_norgard", "tundra_norgard", "bosque_gemelos"]
RISK = ["VORNARSK_WINTER_FREEZE", "KELDARSK_WINTER_FREEZE", "ZANTHIR_BAY_NAVIGATION_ICE",
        "INVERNOS_SNOWMELT_RUNOFF", "ARLEON_CALERAN_FLOOD", "CALERAN_BRANCH_EROSION",
        "MOUNTAIN_SLOPE_INSTABILITY", "BOSQUE_QUEBRADO_PASTURE_DROUGHT",
        "ARLEON_AGRICULTURAL_FROST_DAMAGE", "FOREST_FIRE"]
SOURCES = [(N.relative_to(ROOT) / x).as_posix() for x in [
    "Clima/clima_general.md", "Geografía/regiones_naturales.md",
    "Geografía/bosques.md", "Geografía/mares_y_costas.md",
    "Geografía/montanas.md", "Geografía/Montes Invernos/cotas_y_altitudes_borrador.md"
]] + [(H.relative_to(ROOT) / x).as_posix() for x in [
    "Cartografia/G01_ATLAS_FISICO.md",
    "Datos operativos/galdren_g01_geography_v0.1.json",
    "Cartografia/G02_ATLAS_HIDROGRAFICO.md",
    "Hidrologia/G02_ESTACIONALIDAD_Y_RIESGOS.md",
    "Datos operativos/galdren_g02_hydrology_v0.1.json",
    "00_Control_del_proyecto/TRASPASO_G03.md"
]]
U = ["LOCAL_CLIMATE_TIME_SERIES", "LOCAL_TEMPERATURES_AND_PRECIPITATION",
     "NORTHERN_GALDREN_POLAR_MEMBERSHIP", "BIOME_BORDERS_AND_LOCAL_OWNERSHIP",
     "SOIL_HORIZONS_AND_PARCEL_SUITABILITY", "AGRICULTURAL_CALENDAR_AND_CROPS",
     "HORSE_BREEDS_HERD_SIZES_AND_PASTURE_CARRYING_CAPACITY",
     "GEOMORPHOLOGY_AND_RISK_POLYGONS", "CANONICAL_LOCAL_WILDLIFE_SPECIES",
     "CALERAN_WEST_EAST_TOPOLOGY", "ZANTHIR_RIVER_OUTLETS",
     "INVERNOS_GLACIERS_AND_LOCAL_ELEVATIONS", "FOREST_FISCAL_OWNERSHIP",
     "GDD-01", "GDD-02", "GDD-03", "GDD-07"]
def fixed_ids(rows, prefix, n):
    assert isinstance(rows, list)
    assert [r["id"] for r in rows] == [prefix + ("%02d" % i) for i in range(1, n+1)]
    return rows
def unknown(row, keys):
    for key in keys:
        assert row[key] == "UNKNOWN", "Valor local inventado: " + key
def no(row, keys):
    for key in keys:
        assert row[key] is False, "Falso certificado: " + key

def check(v):
    assert v["schemaVersion"] == 1
    assert v["documentId"] == "galdren_g03_climate_soils_ecosystems"
    assert v["phase"] == "G03" and v["version"] == "0.1.0" and v["date"] == "2026-11-13"
    assert v["baselineMainSha"] == "1ad65cb5eb5dd449c6dd981cba3b63d96435d69f"
    assert v["baseDocumentId"] == "galdren_g02" == g2["documentId"]
    assert v["status"] == "DOCUMENTARY_PLANNING_ONLY" and v["runtimeEnabled"] is False
    assert v["authorApproval"] == "G03_WORK_APPROVED; LOCAL_CLIMATE_SOILS_AND_BIOMES_NOT_RATIFIED"
    assert v["inheritance"] == g0["inheritance"] == g1["inheritance"] == g2["inheritance"]
    assert v["sourceAuthorities"] == ["CANON_REPO", "REGIONAL_DRAFT_QUALITATIVE", "STUDY_ONLY", "UNKNOWN"]
    assert len(g0["canonToponyms"]) == 18 and len(g1["reliefUnits"]) == 12
    assert len(g2["rivers"]) == 5 and g2["northern"]["winterIce"] == "CANON"
    assert g2["caleran"]["westToEastLink"] == "TOPOGRAPHIC_ROUTE_UNRESOLVED"
    s = v["scope"]
    assert s["territory"] == "casa_galdren" and s["region"] == "norgard" and s["redOutlineApproximate"] is True
    no(s, ["georeferenced", "metricClimateValidated", "soilMapValidated",
           "biomeMapValidated", "legalBoundariesValidated", "runtimeSimulated"])
    for field in ["climatePolygons", "soilPolygons", "biomePolygons", "riskPolygons"]:
        assert s[field] == []
    unknown(s, ["physicalCoordinates", "localClimateBoundaries", "polarBandMembership"])
    g = v["guardrails"]
    for field in ["caleranOneRiver", "caleranAzuriusWesternBirth", "caleranEasternFertilePlains",
                  "vornarskWinterFrozen", "keldarskWinterFrozen",
                  "zanthirBayWinterIceNavigationDifficulty", "invernosShared"]:
        assert g[field] is True
    no(g, ["caleranTopographicLinkResolved", "permanentGlaciersConfirmed"])
    assert g["newHydronymsAdded"] == g["newForestNamesAdded"] == g["newWildlifeSpeciesAdded"] == 0
    assert g["metalEstelarOnly"] == "montes_azurios"
    assert [g[k] for k in ["treskalOwner", "dorthOwner", "hallheimOwner"]] == [
        "casa_valrik", "casa_edranor", "crown_aethros"]
    assert g["forjaOwner"] == "UNKNOWN" and g["forjaPeacetimeAdministrator"] == "casa_galdren"
    assert g["forjaWartimeCommand"] == "crown_aethros_hallheim"
    c = v["regionalClimate"]
    assert [c[k] for k in ["easternCoast", "easternInterior", "northInterior", "farNorth"]] == [
        "OCEANIC", "CONTINENTAL", "CONTINENTAL_COLD", "POLAR"]
    assert c["transitionGradual"] is True
    no(c, ["farNorthBandIsPoliticalDivision", "localClimateSeriesEstablished", "arleonAndZanthirUniform"])
    unknown(c, ["northGaldrenPolarJurisdiction"])
    cr = fixed_ids(v["climateReferences"], "G03-C", 7)
    for i, row in enumerate(cr):
        assert row["kind"] == CLIMATES[i]
        assert row["evidence"] == (["CANON_REPO"] * 5 + ["STUDY_ONLY", "REGIONAL_DRAFT_QUALITATIVE"])[i]
        assert row["regionalReferenceOnly"] is True
        unknown(row, ["exactBoundary", "measuredRange"])
        no(row, ["metricPolygonVerified", "localClimatologyConfirmed"])
    soilregion = v["regionalSoils"]
    assert soilregion["fertileCaleranEasternPlains"] == soilregion["galdrenNorgardGranary"] == "CANON_REPO"
    no(soilregion, ["everyParcelSuitabilityConfirmed", "geologicalSoilMapConfirmed",
                   "individualCropSpeciesConfirmed", "waterRightsMapped", "forestPropertyMapped"])
    soils = fixed_ids(v["soilStudies"], "G03-S", 12)
    profiles = fixed_ids(v["reliefProfiles"], "G03-P", 12)
    assert [x["reliefUnitId"] for x in soils] == [x["id"] for x in g1["reliefUnits"]]
    for i, (soil, p, origin) in enumerate(zip(soils, profiles, g1["reliefUnits"])):
        ctx, ref, eco, sample = CTX[i]
        assert soil["studyClass"] == sample
        assert soil["evidence"] == ("CANON_REGIONAL_FERTILITY_AND_LOCAL_UNASSESSED" if i == 5 else "STUDY_ONLY")
        assert soil["fertileRegionalPlainContext"] is (i == 5)
        assert soil["reliefUnitId"] == origin["id"]
        assert soil["parcelSuitability"] == "UNASSESSED" and soil["measuredSoilSamples"] == []
        assert soil["depthCm"] is None
        no(soil, ["parcelMapped", "soilProfileValidated", "irrigationInfrastructureConfirmed"])
        unknown(soil, ["parentMaterial", "texture", "ph", "organicMatter",
                       "drainage", "permeability", "soilOwnership"])
        assert p["reliefUnitId"] == origin["id"] and p["reliefAnchor"] == origin["anchor"]
        assert p["studyContext"] == ctx and p["climateReference"] == ref
        assert p["ecologyContext"] == eco and p["soilDossierId"] == soil["id"]
        assert p["climateEvidence"] == "REGIONAL_REFERENCE_ONLY"
        assert p["outsideGaldrenContext"] is (i in [10, 11])
        assert p["localSoilSuitability"] == "UNASSESSED"
        no(p, ["microclimateVerified", "ecosystemPolygonValidated"])
        unknown(p, ["localClimaticZone", "localMonthlyTemperatures", "localRainfall",
                    "windDirection", "winterSnowDuration", "frostDays", "habitatMembership",
                    "jurisdiction", "metricCoordinates", "wildlifeSpeciesInventory"])
    ec = v["regionalEcology"]
    assert [e["id"] for e in ec] == ECO
    assert [e["character"] for e in ec] == [
        "DISCONTINUOUS_MIXED_TEMPERATE", "MIXED_TEMPERATE_WARM", "ALLUVIAL_DECIDUOUS",
        "REGIONAL_MOUNTAIN_FOREST", "REGIONAL_BOREAL", "REGIONAL_TUNDRA",
        "VALRIK_TRESKAL_CONTEXT"]
    assert [e["riverLink"] for e in ec] == [
        "rio_caleran", "brazo_occidental_caleran", "brazo_oriental_caleran",
        "UNKNOWN", "UNKNOWN", "UNKNOWN", "rios_sareno_theleno"]
    assert set(ec[0]["flora"]) == {"robles", "fresnos", "olmos", "arces", "abedules", "alisos", "pinos", "abetos"}
    assert "castanos" in ec[1]["flora"] and {"alamos", "sauces", "alisos"} <= set(ec[2]["flora"])
    assert {"piceas", "alerces", "abedules"} <= set(ec[4]["flora"])
    for i,e in enumerate(ec):
        assert e["evidence"] == "CANON_REPO" and e["localOwnership"] == "UNKNOWN"
        assert e["habitatAreaKm2"] is None and e["speciesNewlyRatified"] == []
        no(e, ["georeferenced", "localJurisdictionVerified"])
        assert e["horseBreedingMainRegionOfNorgard"] is (i == 0)
    eguard = v["ecologyGuard"]
    assert eguard["mainHorseBreedingRegion"] == "bosque_quebrado"
    assert eguard["mainHorseBreedingStatus"] == "CANON_REPO"
    no(eguard, ["boisQuebradoIsTwoIndependentForests", "caminoRealRouteGeoreferenced",
                "riverBankWetlandsInvented", "gemelosBelongsToGaldren",
                "wholeAzuriosForestAssignedToGaldren", "forestOwnershipByBiome",
                "habitatToPoliticalBorder"])
    unknown(eguard, ["northernBorealMembership", "northernTundraMembership"])
    risks = fixed_ids(v["riskScenarios"], "G03-R", 10)
    assert [r["kind"] for r in risks] == RISK
    assert [r["evidence"] for r in risks] == [
        "CANON_QUALITATIVE"] * 3 + ["REGIONAL_DRAFT_QUALITATIVE"] + ["STUDY_ONLY"] * 6
    for i,r in enumerate(risks):
        assert r["confirmedQualitative"] is (i < 3)
        no(r, ["localEventOrImpactConfirmed", "infrastructureLostConfirmed", "runtimeEventEnabled"])
        assert r["physicalHazardPolygon"] == [] and r["probability"] is None
        unknown(r, ["frequency", "intensity", "annualDates"])
    assert [r["season"] for r in v["seasonality"]] == ["PRIMAVERA", "VERANO", "OTONO", "INVIERNO"]
    for s in v["seasonality"]:
        unknown(s, ["calendarDates", "vegetationPhenology", "agriculturalCalendar"])
        assert s["durationDays"] is None and s["regionalReferenceOnly"] is True
        assert s["runtimeValidated"] is False
    assert v["protectedPlaces"] == [
        {"id": "arleon", "owner": "casa_galdren"},
        {"id": "zanthir", "owner": "casa_galdren"},
        {"id": "treskal", "owner": "casa_valrik"},
        {"id": "dorth", "owner": "casa_edranor"},
        {"id": "hallheim", "owner": "crown_aethros"},
        {"id": "forja_estelar", "owner": "UNKNOWN"}]
    assert v["unknown"] == U
    assert v["sourceRegistry"] == SOURCES and len(SOURCES) == 12
    for source in SOURCES:
        assert (ROOT / source).is_file(), "Fuente ausente: " + source

check(g3)
clima = (N / "Clima/clima_general.md").read_text(encoding="utf-8")
bosques = (N / "Geografía/bosques.md").read_text(encoding="utf-8")
regiones = (N / "Geografía/regiones_naturales.md").read_text(encoding="utf-8")
for marker in ["continental", "oceánico", "polar", "Vornarsk", "Keldarsk"]:
    assert marker in clima, "Fuente climática incompleta: " + marker
for marker in ["Bosque Quebrado", "principal región caballar", "Bosque del Camino Real",
               "Bosque de las Riberas", "Bosque de los Gemelos", "robles", "alisos"]:
    assert marker in bosques, "Fuente forestal incompleta: " + marker
assert "llanuras fértiles" in regiones
required = [
    "G03_INDICE.md", "Clima/G03_GRADIENTES_Y_MICROCLIMAS.md",
    "Suelos/G03_ATLAS_EDAFOLOGICO.md", "Ecosistemas/G03_ATLAS_ECOLOGICO.md",
    "Riesgos/G03_ESTACIONALIDAD_Y_PELIGROS.md",
    "Auditorias/G03_FUENTES_Y_DEUDA.md", "Auditorias/G03_ACTA.md",
    "00_Control_del_proyecto/TRASPASO_G04.md",
    "Datos operativos/galdren_g03_climate_soils_ecosystems_v0.1.json"
]
for rel in required:
    assert (H / rel).is_file(), "Archivo ausente: " + rel
assert (ROOT / ".github/workflows/galdren-g03.yml").is_file()

def change(path, value):
    def edit(x):
        p = x
        for k in path[:-1]:
            p = p[k]
        p[path[-1]] = value
    return edit
mutations = [
    (["schemaVersion"], 2), (["documentId"], "otro"), (["phase"], "G04"),
    (["date"], "2027-01-01"), (["baselineMainSha"], "deadbeef"),
    (["baseDocumentId"], "galdren_g01"), (["runtimeEnabled"], True),
    (["status"], "SIMULATION_READY"), (["authorApproval"], "RATIFIED"),
    (["inheritance", 0], "otro"), (["sourceAuthorities", 0], "STUDY_ONLY"),
    (["scope", "territory"], "casa_valrik"), (["scope", "georeferenced"], True),
    (["scope", "soilMapValidated"], True), (["scope", "biomeMapValidated"], True),
    (["scope", "legalBoundariesValidated"], True), (["scope", "runtimeSimulated"], True),
    (["scope", "climatePolygons"], [[1,2]]), (["scope", "soilPolygons"], [[1,2]]),
    (["scope", "biomePolygons"], [[1,2]]), (["scope", "riskPolygons"], [[1,2]]),
    (["scope", "polarBandMembership"], True),
    (["guardrails", "caleranOneRiver"], False),
    (["guardrails", "caleranAzuriusWesternBirth"], False),
    (["guardrails", "caleranTopographicLinkResolved"], True),
    (["guardrails", "vornarskWinterFrozen"], False),
    (["guardrails", "keldarskWinterFrozen"], False),
    (["guardrails", "zanthirBayWinterIceNavigationDifficulty"], False),
    (["guardrails", "invernosShared"], False),
    (["guardrails", "permanentGlaciersConfirmed"], True),
    (["guardrails", "newHydronymsAdded"], 1),
    (["guardrails", "newForestNamesAdded"], 1),
    (["guardrails", "newWildlifeSpeciesAdded"], 1),
    (["guardrails", "treskalOwner"], "casa_galdren"),
    (["guardrails", "dorthOwner"], "casa_galdren"),
    (["guardrails", "hallheimOwner"], "casa_galdren"),
    (["guardrails", "forjaOwner"], "casa_galdren"),
    (["regionalClimate", "easternCoast"], "POLAR"),
    (["regionalClimate", "transitionGradual"], False),
    (["regionalClimate", "arleonAndZanthirUniform"], True),
    (["climateReferences", 0, "kind"], "POLAR"),
    (["climateReferences", 2, "exactBoundary"], "KNOWN"),
    (["climateReferences", 4, "localClimatologyConfirmed"], True),
    (["regionalSoils", "everyParcelSuitabilityConfirmed"], True),
    (["regionalSoils", "forestPropertyMapped"], True),
    (["soilStudies", 5, "parcelSuitability"], "APTO"),
    (["soilStudies", 0, "parentMaterial"], "GRANITE"),
    (["soilStudies", 2, "ph"], 6.4),
    (["soilStudies", 3, "depthCm"], 120),
    (["soilStudies", 6, "irrigationInfrastructureConfirmed"], True),
    (["regionalEcology", 0, "horseBreedingMainRegionOfNorgard"], False),
    (["regionalEcology", 1, "character"], "POLAR"),
    (["regionalEcology", 2, "flora"], ["cipres"]),
    (["regionalEcology", 3, "localOwnership"], "casa_galdren"),
    (["regionalEcology", 4, "habitatAreaKm2"], 250),
    (["regionalEcology", 5, "localJurisdictionVerified"], True),
    (["regionalEcology", 0, "speciesNewlyRatified"], ["dragon"]),
    (["reliefProfiles", 0, "reliefUnitId"], "G01-U12"),
    (["reliefProfiles", 2, "climateReference"], "G03-C01"),
    (["reliefProfiles", 4, "habitatMembership"], "GALDREN_POLAR"),
    (["reliefProfiles", 5, "localMonthlyTemperatures"], [12, 20]),
    (["reliefProfiles", 6, "localSoilSuitability"], "APTO"),
    (["reliefProfiles", 7, "wildlifeSpeciesInventory"], ["dragon"]),
    (["reliefProfiles", 8, "jurisdiction"], "casa_galdren"),
    (["reliefProfiles", 10, "outsideGaldrenContext"], False),
    (["ecologyGuard", "gemelosBelongsToGaldren"], True),
    (["ecologyGuard", "northernBorealMembership"], True),
    (["riskScenarios", 0, "evidence"], "STUDY_ONLY"),
    (["riskScenarios", 3, "evidence"], "CANON_QUALITATIVE"),
    (["riskScenarios", 4, "evidence"], "CANON_QUALITATIVE"),
    (["riskScenarios", 5, "localEventOrImpactConfirmed"], True),
    (["riskScenarios", 7, "probability"], 0.4),
    (["riskScenarios", 8, "frequency"], "YEARLY"),
    (["riskScenarios", 9, "runtimeEventEnabled"], True),
    (["seasonality", 0, "calendarDates"], "MAR-MAY"),
    (["seasonality", 1, "durationDays"], 90),
    (["protectedPlaces", 2, "owner"], "casa_galdren"),
    (["sourceRegistry", 0], "inventada.md"),
    (["unknown", 0], "SETTLED"),
]
attacks = [change(path, value) for path,value in mutations]
attacks += [
    lambda x: x["reliefProfiles"].append(copy.deepcopy(x["reliefProfiles"][0])),
    lambda x: x["soilStudies"].append(copy.deepcopy(x["soilStudies"][0])),
    lambda x: x["regionalEcology"].append(copy.deepcopy(x["regionalEcology"][0])),
    lambda x: x["riskScenarios"].append(copy.deepcopy(x["riskScenarios"][0])),
    lambda x: x["climateReferences"].append(copy.deepcopy(x["climateReferences"][0])),
    lambda x: x["unknown"].pop(),
    lambda x: x["sourceRegistry"].pop(),
]
for idx, attack in enumerate(attacks, 1):
    item = copy.deepcopy(g3)
    attack(item)
    try:
        check(item)
    except (AssertionError, KeyError, IndexError, TypeError):
        continue
    raise AssertionError("Mutación no detectada: " + str(idx))
print("GALDREN G03 STATIC PASS | 7 climas referencia | 12 suelos y perfiles | 7 ecosistemas | 10 riesgos | %d ataques negativos | DOCUMENTAL" % len(attacks))

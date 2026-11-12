"""Contrato E03: coherencia documental y pruebas negativas, sin simulación Godot/CoreRPG."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
B = N / "Territorios/Casa Edranor"
load = lambda path: json.loads(path.read_text(encoding="utf-8"))
data = load(B / "Datos operativos/edranor_e03_climate_soils_ecosystems_v0.1.json")
e00 = load(B / "Datos operativos/edranor_e00_manifest_v0.1.json")
e01 = load(B / "Datos operativos/edranor_e01_relief_v0.1.json")
e02 = load(B / "Datos operativos/edranor_e02_hydrology_v0.1.json")

LAYERS = ["nimroel_core", "norgard_defaults", "casa_edranor", "localidad", "world_state"]
AUTHORITIES = {"CANON_REPO", "AUTOR_2026_11_12", "OBSERVACION_MAPA", "PROPUESTA", "UNKNOWN"}
UNITS = {x["id"] for x in e01["reliefUnits"]}
ANCHORS = {"dorth", "lumina", "karsath", "rodas", "hallheim"}
ECOSYSTEMS = {"bosque_alto", "bosque_azurios", "boreal_norgard", "tundra_norgard"}
RISK_IDS = {
    "edr_e03_risk_frost_vines", "edr_e03_risk_cold_snow",
    "edr_e03_risk_saturated_soils", "edr_e03_risk_slope_erosion",
    "edr_e03_risk_thaw_runoff", "edr_e03_risk_dry_stress",
    "edr_e03_risk_forest_fire", "edr_e03_risk_wind_damage",
}
FORBIDDEN = {
    "POLAR_WINE_BY_DEFAULT", "EVERY_UNIT_VINEYARD",
    "NUMERIC_CLIMATE_NORMALS_AS_FACT", "LOCAL_CLIMATE_BORDER_AS_FACT",
    "SOIL_PH_OR_TEXTURE_AS_FACT", "LOCAL_WETLAND_OR_WATERCOURSE_AS_FACT",
    "BOREAL_OR_TUNDRA_EDRANOR_MEMBERSHIP_AS_FACT", "FOREST_OWNERSHIP_BY_BIOME",
    "RODAS_EDRANOR_FISCAL_OR_MILITARY_CONTROL", "HALLHEIM_INSIDE_EDRANOR",
    "WINE_IRRIGATION_AS_FACT", "E03_SIMULATION_READY",
    "NEW_WILDLIFE_SPECIES_AS_CANON", "LOCAL_RISK_AS_CONFIRMED",
    "ROUTE_OR_BRIDGE_AS_FACT",
}


def indexed(seq, key="id"):
    assert isinstance(seq, list), "Secuencia obligatoria"
    keys = [x[key] for x in seq]
    assert len(keys) == len(set(keys)), f"Identificadores duplicados: {key}"
    return {x[key]: x for x in seq}


def check(v):
    assert v["schemaVersion"] == 1
    assert v["documentId"] == "edranor_e03_climate_soils_ecosystems"
    assert v["phase"] == "E03" and v["version"] == "0.1"
    assert v["status"] == "DOCUMENTARY_PLANNING_ONLY" and v["runtimeEnabled"] is False
    assert v["date"] == "2026-11-12" and v["inheritance"] == LAYERS
    assert set(v["sourceAuthorities"]) == AUTHORITIES and len(v["sourceAuthorities"]) == len(AUTHORITIES)
    assert e00["house"]["seatId"] == "dorth" and set(e00["protectedIds"]) == ANCHORS
    assert e01["cartography"]["northBoundaryClosed"] is False
    assert e02["scope"]["localHydrographyValidated"] is False
    assert e02["regionalCanonicalFeatures"][0]["membershipInEdranor"] == "UNKNOWN"

    s = v["scope"]
    assert s["territory"] == "casa_edranor" and s["regionalCanon"] == "norgard"
    for key in ("northBoundaryClosed", "georeferenced", "metricGeometryValidated",
                "localClimateMapped", "localSoilsMapped", "localBiomesMapped"):
        assert s[key] is False, f"Se ha certificado indebidamente {key}"
    for key in ("climatePolygons", "soilPolygons", "habitatPolygons", "hazardPolygons"):
        assert s[key] == []
    for key in ("scale", "coordinates", "northernPolarMembership", "localHydrologicalNetwork"):
        assert s[key] == "UNKNOWN"

    anchors = indexed(v["anchors"])
    assert set(anchors) == ANCHORS
    for loc in ("dorth", "lumina", "karsath"):
        assert anchors[loc]["owner"] == "casa_edranor" and anchors[loc]["inside"] is True
    r = anchors["rodas"]
    assert r["inside"] is True and r["berserkersUnderCrown"] is True
    for owner_key in ("owner", "militaryOwner", "fiscalOwner"):
        assert r[owner_key] == "crown_aethros"
    assert anchors["hallheim"]["owner"] == "crown_aethros"
    assert anchors["hallheim"]["inside"] is False

    climate = v["regionalClimateCanon"]
    assert climate["centralGradient"] == ["CENTRAL_CONTINENTAL", "CENTRAL_COLD", "FAR_NORTH_POLAR"]
    assert climate["orderedNorthwardTransition"] == ["CONTINENTAL", "COLD", "POLAR"]
    assert climate["farNorthPolarBandIsPoliticalBorder"] is False
    for key in ("polarBandInsideEdranor", "exactClimateBoundaries", "localMeasuredTemperatures"):
        assert climate[key] == "UNKNOWN"
    assert climate["evidence"] == "CANON_REPO"

    eco = indexed(v["regionalEcosystemCanon"])
    assert set(eco) == ECOSYSTEMS
    assert eco["bosque_alto"]["associatedWith"] == "lumina"
    assert eco["bosque_alto"]["description"] == "MIXED_TEMPERATE_HIGHLAND_FOREST"
    assert {"ROBLES", "HAYAS", "CONIFERAS"} <= set(eco["bosque_alto"]["treeReferences"])
    assert eco["bosque_azurios"]["associatedWith"] == "dorth"
    assert eco["bosque_azurios"]["description"] == "MIXED_CONTINENTAL_MONTANE_FOREST"
    assert {"ROBLES", "HAYAS", "FRESNOS", "ARCES", "PINOS", "ABETOS"} <= set(eco["bosque_azurios"]["treeReferences"])
    assert eco["boreal_norgard"]["associatedWith"] == "NORGARD_NORTH"
    assert eco["tundra_norgard"]["associatedWith"] == "NORGARD_FAR_NORTH"
    for entry in eco.values():
        assert entry["evidence"] == "CANON_REPO"
    for key in ("localArea", "localOwnership"):
        for eid in ("bosque_alto", "bosque_azurios"):
            assert eco[eid][key] == "UNKNOWN"
    for eid in ("boreal_norgard", "tundra_norgard"):
        assert eco[eid]["edranorMembership"] == "UNKNOWN"

    profiles = indexed(v["reliefProfiles"])
    assert len(profiles) == 7
    assert {x["reliefUnitId"] for x in profiles.values()} == UNITS
    for p in profiles.values():
        assert p["id"] == "edr_e03_profile_" + p["reliefUnitId"].removeprefix("edr_e01_")
        c = p["climate"]
        assert c["studyClass"] and c["regionalReference"] and c["regionalEvidence"] == "CANON_REPO"
        assert c["localClimateValidated"] is False
        for field in ("localClimateType", "monthlyTemperatures", "precipitationAmounts",
                      "precipitationSeasonality", "snowDuration", "frostDays",
                      "prevailingWind", "localHumidity", "weatherStation"):
            assert c[field] == "UNKNOWN", f"Variable climática inventada: {field}"
        soil = p["soil"]
        assert soil["studyQuestion"] and soil["evidence"] == "PROPUESTA"
        assert soil["soilValidated"] is False and soil["soilProfileLocations"] == []
        assert soil["viticultureSuitability"] == "UNASSESSED"
        assert soil["vineyardOnUnitConfirmed"] is False
        for field in ("parentMaterial", "texture", "effectiveDepth", "drainage",
                      "permeability", "organicMatter", "soilPh", "slopeParcel"):
            assert soil[field] == "UNKNOWN", f"Variable edáfica inventada: {field}"
        e = p["ecosystem"]
        assert e["regionalReference"] and e["regionalEvidence"] in {"CANON_REPO", "UNKNOWN"}
        assert e["localMembership"] == "UNKNOWN" and e["localEcosystemMapped"] is False
        assert e["habitatPolygons"] == [] and e["ecosystemStudyOnly"] is True
        for field in ("speciesInventory", "localFaunaInventory", "habitatOwnership"):
            assert e[field] == "UNKNOWN"
        b = p["boundary"]
        assert b["unitExtent"] == "UNKNOWN" and b["insideNorthernEdranorValidated"] is False

    assert profiles["edr_e03_profile_lumina_bosque_alto"]["ecosystem"]["regionalReference"] == "BOSQUE_ALTO"
    assert profiles["edr_e03_profile_dorth_azurios_west"]["ecosystem"]["regionalReference"] == "BOSQUE_AZURIOS"
    assert profiles["edr_e03_profile_far_north_unclosed"]["climate"]["studyClass"] == "NORTHERN_EXTENT_UNRESOLVED"
    assert profiles["edr_e03_profile_central_wine_context"]["soil"]["studyQuestion"] == "WINE_REGION_PARCEL_STUDY"

    hazards = indexed(v["riskScenarios"])
    assert set(hazards) == RISK_IDS
    for hazard in hazards.values():
        assert hazard["trigger"] and hazard["effect"]
        assert hazard["state"] == "CONDITIONAL_ONLY" and hazard["evidence"] == "PROPUESTA"
        assert hazard["hazardLocalConfirmed"] is False and hazard["exposureValidated"] is False
        assert hazard["frequency"] == "UNKNOWN" and hazard["intensity"] == "UNKNOWN"
        assert hazard["locality"] == "UNKNOWN" and hazard["hazardGeometry"] == []

    seasons = indexed(v["seasonalityStudy"])
    assert set(seasons) == {"edr_e03_season_primavera", "edr_e03_season_verano",
                            "edr_e03_season_otono", "edr_e03_season_invierno"}
    assert {x["season"] for x in seasons.values()} == {"PRIMAVERA", "VERANO", "OTONO", "INVIERNO"}
    for season in seasons.values():
        assert season["calendarDuration"] == "UNKNOWN" and season["localPhenology"] == "UNKNOWN"
        assert season["regionalComparisonOnly"] is True and season["forecastValidated"] is False

    land = v["landUseRules"]
    assert land["edranorMainWineRegion"] is True and land["luminaForestWoodSupportsBarrels"] is True
    for key in ("allSevenUnitsViticultural", "viticulturePolygonValidated",
                "irrigationConfirmed", "polarViticultureByDefault",
                "localSoilSuitabilityValidated", "royalForestWholeAzuriosAssignedToEdranor"):
        assert land[key] is False
    hyd = v["hydrologyGuard"]
    assert hyd["lurienCourseInEdranor"] == hyd["antelaInsideEdranor"] == "UNKNOWN"
    assert hyd["localBasinBoundariesValidated"] is False
    assert hyd["localSpringsConfirmed"] is False and hyd["roadCrossingsConfirmed"] is False
    gov = v["governance"]
    assert gov["rodasFiscalOwner"] == "crown_aethros" and gov["rodasMilitaryOwner"] == "crown_aethros"
    assert gov["hallheimInside"] is False
    assert gov["ecologicalZonesAreAdministrativeBorders"] is False and gov["noInternalCustoms"] is True
    assert set(v["forbiddenClaims"]) == FORBIDDEN
    for item in ("EDD-01_NORTH_BOUNDARY_CLOSURE", "EDD-02_GEOREFERENCING_AND_SCALE",
                 "EDD-03_LOCAL_HYDROGRAPHY_AND_GROUNDWATER", "EDD-07_ACCESS_AND_PATHS",
                 "SOIL_MAP_AND_PROFILE_MEASUREMENTS", "LOCAL_CLIMATE_TIME_SERIES"):
        assert item in v["unknown"]


check(data)

# Regresión de fuente: comprobamos citas EN las fuentes, no solo un contrato autocitado.
climate_source = (N / "Clima/clima_general.md").read_text(encoding="utf-8")
forests_source = (N / "Geografía/bosques.md").read_text(encoding="utf-8")
regional_source = (N / "Geografía/regiones_naturales.md").read_text(encoding="utf-8")
for marker in ("continental frío", "gran franja natural de clima polar", "bosque boreal"):
    assert marker in climate_source, f"No está en el canon climático: {marker}"
for marker in ("Bosque Alto", "Lumina", "robles", "hayas",
               "Bosque de los Azurios", "Dorth", "Bosque Real"):
    assert marker in forests_source, f"No está en el canon de bosques: {marker}"
assert "no coinciden necesariamente" in regional_source

mandatory = [
    B / "E03_INDICE.md",
    B / "Clima/E03_FRANJAS_Y_MICROCLIMAS.md",
    B / "Suelos/E03_EDAFOLOGIA_Y_VITICULTURA.md",
    B / "Ecosistemas/E03_ATLAS_ECOLOGICO.md",
    B / "Riesgos/E03_ESTACIONALIDAD_Y_RIESGOS.md",
    B / "Auditorias/E03_FUENTES_Y_DECISIONES.md",
    B / "Auditorias/E03_ACTA.md",
    B / "00_Control_del_proyecto/TRASPASO_E04.md",
    B / "Datos operativos/edranor_e03_climate_soils_ecosystems_v0.1.json",
    B / "Datos operativos/edranor_e02_hydrology_v0.1.json",
    B / "Datos operativos/edranor_e01_relief_v0.1.json",
    B / "Datos operativos/edranor_e00_manifest_v0.1.json",
    ROOT / ".github/workflows/edranor-e03.yml",
]
for path in mandatory:
    assert path.is_file() and path.stat().st_size > 50, f"Falta fichero E03: {path}"

# La alteración de una sola salvaguarda ha de rechazar el manifest.
mutations = [
    lambda x: x.update(schemaVersion=2),
    lambda x: x.update(documentId="otro"),
    lambda x: x.update(phase="E04"),
    lambda x: x.update(version="0.2"),
    lambda x: x.update(runtimeEnabled=True),
    lambda x: x.update(status="SIMULATION_READY"),
    lambda x: x.update(date="2028-01-01"),
    lambda x: x["inheritance"].reverse(),
    lambda x: x["sourceAuthorities"].remove("UNKNOWN"),
    lambda x: x["scope"].update(territory="casa_aethros"),
    lambda x: x["scope"].update(regionalCanon="darovan"),
    lambda x: x["scope"].update(northBoundaryClosed=True),
    lambda x: x["scope"].update(georeferenced=True),
    lambda x: x["scope"].update(metricGeometryValidated=True),
    lambda x: x["scope"].update(localClimateMapped=True),
    lambda x: x["scope"].update(localSoilsMapped=True),
    lambda x: x["scope"].update(localBiomesMapped=True),
    lambda x: x["scope"].update(climatePolygons=[[1, 2]]),
    lambda x: x["scope"].update(soilPolygons=[[1, 2]]),
    lambda x: x["scope"].update(habitatPolygons=[[1, 2]]),
    lambda x: x["scope"].update(hazardPolygons=[[1, 2]]),
    lambda x: x["scope"].update(scale="1:10000"),
    lambda x: x["scope"].update(coordinates=[42, -8]),
    lambda x: x["scope"].update(northernPolarMembership=True),
    lambda x: x["scope"].update(localHydrologicalNetwork="VALIDATED"),
    lambda x: x["anchors"][0].update(owner="crown_aethros"),
    lambda x: x["anchors"][1].update(inside=False),
    lambda x: x["anchors"][3].update(owner="casa_edranor"),
    lambda x: x["anchors"][3].update(militaryOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(fiscalOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(berserkersUnderCrown=False),
    lambda x: x["anchors"][4].update(inside=True),
    lambda x: x["anchors"].append(copy.deepcopy(x["anchors"][0])),
    lambda x: x["regionalClimateCanon"].update(centralGradient=["POLAR"]),
    lambda x: x["regionalClimateCanon"].update(orderedNorthwardTransition=["POLAR", "CONTINENTAL"]),
    lambda x: x["regionalClimateCanon"].update(farNorthPolarBandIsPoliticalBorder=True),
    lambda x: x["regionalClimateCanon"].update(polarBandInsideEdranor=True),
    lambda x: x["regionalClimateCanon"].update(exactClimateBoundaries="DRAWN"),
    lambda x: x["regionalClimateCanon"].update(localMeasuredTemperatures=[1,2]),
    lambda x: x["regionalClimateCanon"].update(evidence="PROPUESTA"),
    lambda x: x["regionalEcosystemCanon"][0].update(associatedWith="hallheim"),
    lambda x: x["regionalEcosystemCanon"][0].update(description="POLAR_SWAMP"),
    lambda x: x["regionalEcosystemCanon"][0].update(localArea=100),
    lambda x: x["regionalEcosystemCanon"][0].update(localOwnership="casa_edranor"),
    lambda x: x["regionalEcosystemCanon"][1].update(associatedWith="rodas"),
    lambda x: x["regionalEcosystemCanon"][1].update(description="TUNDRA"),
    lambda x: x["regionalEcosystemCanon"][2].update(edranorMembership=True),
    lambda x: x["regionalEcosystemCanon"][3].update(edranorMembership=True),
    lambda x: x["regionalEcosystemCanon"].append(copy.deepcopy(x["regionalEcosystemCanon"][0])),
    lambda x: x["reliefProfiles"][0].update(reliefUnitId="inexistente"),
    lambda x: x["reliefProfiles"][0].update(id="otro"),
    lambda x: x["reliefProfiles"].append(copy.deepcopy(x["reliefProfiles"][0])),
    lambda x: x["reliefProfiles"][0]["climate"].update(localClimateValidated=True),
    lambda x: x["reliefProfiles"][0]["climate"].update(localClimateType="POLAR"),
    lambda x: x["reliefProfiles"][0]["climate"].update(monthlyTemperatures=[5]),
    lambda x: x["reliefProfiles"][0]["climate"].update(precipitationAmounts=[150]),
    lambda x: x["reliefProfiles"][0]["climate"].update(snowDuration=120),
    lambda x: x["reliefProfiles"][0]["climate"].update(frostDays=200),
    lambda x: x["reliefProfiles"][0]["climate"].update(prevailingWind="N"),
    lambda x: x["reliefProfiles"][0]["climate"].update(regionalEvidence="PROPUESTA"),
    lambda x: x["reliefProfiles"][0]["soil"].update(soilValidated=True),
    lambda x: x["reliefProfiles"][0]["soil"].update(parentMaterial="LIMESTONE"),
    lambda x: x["reliefProfiles"][0]["soil"].update(texture="CLAY"),
    lambda x: x["reliefProfiles"][0]["soil"].update(permeability=0.5),
    lambda x: x["reliefProfiles"][0]["soil"].update(soilPh=6.5),
    lambda x: x["reliefProfiles"][0]["soil"].update(soilProfileLocations=[[0,0]]),
    lambda x: x["reliefProfiles"][0]["soil"].update(viticultureSuitability="APTO"),
    lambda x: x["reliefProfiles"][0]["soil"].update(vineyardOnUnitConfirmed=True),
    lambda x: x["reliefProfiles"][0]["soil"].update(evidence="CANON_REPO"),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(localMembership=True),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(localEcosystemMapped=True),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(habitatPolygons=[[0,1]]),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(speciesInventory=["LOBO"]),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(habitatOwnership="casa_edranor"),
    lambda x: x["reliefProfiles"][0]["ecosystem"].update(ecosystemStudyOnly=False),
    lambda x: x["reliefProfiles"][0]["boundary"].update(unitExtent="POLYGON"),
    lambda x: x["reliefProfiles"][0]["boundary"].update(insideNorthernEdranorValidated=True),
    lambda x: x["reliefProfiles"][2]["ecosystem"].update(regionalReference="NORGARD_TUNDRA"),
    lambda x: x["reliefProfiles"][4]["ecosystem"].update(regionalReference="BOSQUE_ALTO"),
    lambda x: x["reliefProfiles"][6]["climate"].update(studyClass="POLAR_EDRANOR_CERTIFIED"),
    lambda x: x["riskScenarios"][0].update(hazardLocalConfirmed=True),
    lambda x: x["riskScenarios"][0].update(exposureValidated=True),
    lambda x: x["riskScenarios"][0].update(state="CONFIRMED"),
    lambda x: x["riskScenarios"][0].update(intensity=5),
    lambda x: x["riskScenarios"][0].update(frequency="ANNUAL"),
    lambda x: x["riskScenarios"][0].update(locality="rodas"),
    lambda x: x["riskScenarios"][0].update(hazardGeometry=[[0,0]]),
    lambda x: x["riskScenarios"].append(copy.deepcopy(x["riskScenarios"][0])),
    lambda x: x["seasonalityStudy"][0].update(calendarDuration=91),
    lambda x: x["seasonalityStudy"][0].update(localPhenology="BUD_BREAK_DAY_10"),
    lambda x: x["seasonalityStudy"][0].update(regionalComparisonOnly=False),
    lambda x: x["seasonalityStudy"][0].update(forecastValidated=True),
    lambda x: x["landUseRules"].update(allSevenUnitsViticultural=True),
    lambda x: x["landUseRules"].update(viticulturePolygonValidated=True),
    lambda x: x["landUseRules"].update(irrigationConfirmed=True),
    lambda x: x["landUseRules"].update(polarViticultureByDefault=True),
    lambda x: x["landUseRules"].update(localSoilSuitabilityValidated=True),
    lambda x: x["landUseRules"].update(royalForestWholeAzuriosAssignedToEdranor=True),
    lambda x: x["hydrologyGuard"].update(lurienCourseInEdranor=True),
    lambda x: x["hydrologyGuard"].update(antelaInsideEdranor=True),
    lambda x: x["hydrologyGuard"].update(localBasinBoundariesValidated=True),
    lambda x: x["hydrologyGuard"].update(localSpringsConfirmed=True),
    lambda x: x["hydrologyGuard"].update(roadCrossingsConfirmed=True),
    lambda x: x["governance"].update(rodasFiscalOwner="casa_edranor"),
    lambda x: x["governance"].update(rodasMilitaryOwner="casa_edranor"),
    lambda x: x["governance"].update(hallheimInside=True),
    lambda x: x["governance"].update(ecologicalZonesAreAdministrativeBorders=True),
    lambda x: x["governance"].update(noInternalCustoms=False),
    lambda x: x["unknown"].remove("EDD-01_NORTH_BOUNDARY_CLOSURE"),
    lambda x: x["forbiddenClaims"].remove("POLAR_WINE_BY_DEFAULT"),
]
for n, mutate in enumerate(mutations, 1):
    sample = copy.deepcopy(data)
    mutate(sample)
    try:
        check(sample)
    except (AssertionError, KeyError, TypeError):
        continue
    raise AssertionError(f"Mutación negativa E03 {n} aceptada incorrectamente")

print(f"EDRANOR E03 STATIC PASS | {len(UNITS)} unidades E01 | {len(ECOSYSTEMS)} referencias ecológicas | {len(RISK_IDS)} riesgos condicionales | {len(mutations)} negativas | {len(mandatory)} archivos | E00/E01/E02 consistentes")

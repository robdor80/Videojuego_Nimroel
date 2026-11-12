"""E02: contrato documental auditable. No es simulación hídrica ni prueba Godot/CoreRPG."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
BASE = N / "Territorios/Casa Edranor"
read = lambda p: json.loads(p.read_text(encoding="utf-8"))
data = read(BASE / "Datos operativos/edranor_e02_hydrology_v0.1.json")
e00 = read(BASE / "Datos operativos/edranor_e00_manifest_v0.1.json")
e01 = read(BASE / "Datos operativos/edranor_e01_relief_v0.1.json")

LAYERS = ["nimroel_core", "norgard_defaults", "casa_edranor", "localidad", "world_state"]
ALLOWED = {"CANON_REPO", "AUTOR_2026_11_12", "OBSERVACION_MAPA", "PROPUESTA", "UNKNOWN"}
UNITS = {v["id"] for v in e01["reliefUnits"]}
CORRIDORS = {v["id"] for v in e01["corridorQuestions"]}
KNOWN_ANCHORS = {"dorth", "lumina", "karsath", "rodas", "hallheim"}
BASIN_IDS = {
    "edr_e02_basin_lurien_membership", "edr_e02_divide_lumina_highland",
    "edr_e02_divide_azurios_west", "edr_e02_northern_discharge_question",
}
RISKS = {"edr_e02_risk_slopes", "edr_e02_risk_plateau", "edr_e02_risk_frost", "edr_e02_risk_channel"}
USES = {"dorth", "lumina", "karsath", "rodas"}
EXPECTED_CLAIMS = {
    "UNMAPPED_LOCAL_RIVER_AS_CANON", "ANTELA_INSIDE_EDRANOR_AS_FACT",
    "LURIEN_FULLY_WITHIN_EDRANOR", "UPSTREAM_LURIEN_NAVIGABILITY",
    "METRIC_BASIN_OR_RIVER_GEOMETRY", "DRAINAGE_DIVIDE_AS_ADMIN_BORDER",
    "RODAS_EDRANOR_FISCAL_OR_MILITARY_CONTROL", "HALLHEIM_INSIDE_EDRANOR",
    "BRIDGE_OR_FORD_AS_FACT", "FLOODPLAIN_OR_FROST_ON_SITE_AS_FACT",
    "CALERAN_OR_BELARA_IMPORTED", "WINERY_WATER_INFRASTRUCTURE_AS_FACT",
}

def unique(entries, key="id"):
    ids = [x[key] for x in entries]
    assert len(ids) == len(set(ids)), f"IDs duplicados: {key}"
    return {x[key]: x for x in entries}

def checked(v):
    assert v["schemaVersion"] == 1 and v["documentId"] == "edranor_e02_hydrology"
    assert v["version"] == "0.1" and v["phase"] == "E02"
    assert v["runtimeEnabled"] is False and v["status"] == "DOCUMENTARY_PLANNING_ONLY"
    assert v["inheritance"] == LAYERS
    assert set(v["sourceAuthorities"]) == ALLOWED and len(v["sourceAuthorities"]) == len(ALLOWED)
    s = v["scope"]
    assert s["territory"] == "casa_edranor" and s["regionalCanon"] == "norgard"
    assert s["administrativeAndHydrologicalLayersIndependent"] is True
    for name in ("northBoundaryClosed","georeferenced","metricGeometryValidated","localHydrographyValidated"):
        assert s[name] is False
    for name in ("coordinates","scale","dem"):
        assert s[name] == "UNKNOWN"
    for name in ("basinPolygons","riverPolylines","floodPolygons"):
        assert s[name] == []

    assert e00["house"]["seatId"] == "dorth" and set(e00["protectedIds"]) == KNOWN_ANCHORS
    assert e01["phase"] == "E01" and e01["cartography"]["northBoundaryClosed"] is False
    assert e01["cartography"]["watercoursesValidated"] is False
    anchors = unique(v["anchors"])
    assert set(anchors) == KNOWN_ANCHORS
    for loc in ("dorth","lumina","karsath"):
        assert anchors[loc]["jurisdictionOwner"] == "casa_edranor"
        assert anchors[loc]["insideTerritorialScope"] is True
    rodas = anchors["rodas"]
    assert rodas["insideTerritorialScope"] is True and rodas["berserkersUnderCrown"] is True
    for key in ("jurisdictionOwner","militaryOwner","fiscalOwner"):
        assert rodas[key] == "crown_aethros"
        assert rodas[key] == next(a for a in e01["anchors"] if a["id"] == "rodas")[key]
    assert anchors["hallheim"]["insideTerritorialScope"] is False
    assert anchors["hallheim"]["jurisdictionOwner"] == "crown_aethros"

    features = unique(v["regionalCanonicalFeatures"])
    assert set(features) == {"norgard_rio_lurien", "norgard_lago_antela"}
    lurien = features["norgard_rio_lurien"]
    antela = features["norgard_lago_antela"]
    assert lurien["name"] == "Río Lurien" and lurien["kind"] == "RIVER"
    assert lurien["source"] == "Geografía/rios_y_lagos.md#1-río-lurien"
    assert lurien["evidence"] == "CANON_REPO" and lurien["regionalLocation"] == "NORGARD_CENTRAL"
    assert lurien["sourceContext"] == "VERTIENTE_ORIENTAL_MONTES_VALKRAM"
    assert lurien["orderedCourse"] == [
        "VERTIENTE_ORIENTAL_MONTES_VALKRAM", "LAGO_ANTELA",
        "HALLHEIM", "GOLFO_DE_NORGARD"
    ]
    assert lurien["navigableFrom"] == "hallheim" and lurien["navigableTo"] == "golfo_de_norgard"
    assert lurien["membershipInEdranor"] == lurien["edranorLocalCourse"] == "UNKNOWN"
    assert lurien["confirmedCrossings"] == [] and lurien["localFlowRates"] == "UNKNOWN"
    assert antela["name"] == "Lago Antela" and antela["kind"] == "LAKE"
    assert antela["evidence"] == "CANON_REPO"
    assert antela["source"] == "Geografía/rios_y_lagos.md#2-lago-antela"
    assert antela["relativeLocation"] == "SUR_DE_KARSATH"
    assert antela["inputRiver"] == antela["outputRiver"] == "norgard_rio_lurien"
    for key in ("membershipInEdranor","shoreline","area","waterLevels"):
        assert antela[key] == "UNKNOWN"

    exclusions = unique(v["excludedTransplants"], "system")
    assert set(exclusions) == {"belara_lhera","caleran","vornarsk_keldarsk"}
    for x in exclusions.values():
        assert x["edranorAssignment"] is False
        assert x["source"] == "Geografía/rios_y_lagos.md"

    drains = unique(v["localDrainageUnits"])
    assert len(drains) == 7 and {x["reliefUnitId"] for x in drains.values()} == UNITS
    for d in drains.values():
        assert d["id"] == "edr_e02_drain_" + d["reliefUnitId"][8:]
        for k in ("watercourse","recipientBasin","outflowDirection","permanentOrSeasonal","springs","groundwater"):
            assert d[k] == "UNKNOWN"
        assert d["subcatchmentsDelimited"] is False
        assert d["watercourseOnTerritoryConfirmed"] is False
        assert d["evidence"] == "UNKNOWN"

    basins = unique(v["basinStudyQuestions"])
    assert set(basins) == BASIN_IDS
    assert basins["edr_e02_basin_lurien_membership"]["relatedFeature"] == "norgard_rio_lurien"
    assert basins["edr_e02_northern_discharge_question"]["evidence"] == "UNKNOWN"
    for b in basins.values():
        assert b["state"] == "UNDELIMITED_HYPOTHESIS" and b["validated"] is False
        assert b["evidence"] in {"PROPUESTA","UNKNOWN"}
        for k in ("physicalExtent","edranorOverlap","outlet"):
            assert b[k] == "UNKNOWN"
        assert b["watershedGeometry"] == []
        assert b["kind"] in {"RIVER_BASIN_INTERSECTION_STUDY", "POTENTIAL_LOCAL_DRAINAGE_DIVIDE_STUDY",
                             "CROSS_SLOPE_OUTFLOW_STUDY","NORTHERN_OUTFLOW_UNCERTAINTY"}
        assert b["relatedFeature"] in {"UNKNOWN","norgard_rio_lurien"}

    uses = unique(v["useQuestions"])
    assert len(uses) == 4 and {u["locationId"] for u in uses.values()} == USES
    for u in uses.values():
        assert u["id"] == "edr_e02_water_" + u["locationId"]
        assert u["purpose"].strip()
        assert u["confirmed"] is False and u["evidence"] == "UNKNOWN"
        for k in ("sourceWaterbody","withdrawalRights","infrastructure","capacity"):
            assert u[k] == "UNKNOWN"

    risks = unique(v["riskScenarios"])
    assert set(risks) == RISKS
    for risk in risks.values():
        assert risk["state"] == "CONDITIONAL_ONLY"
        assert risk["localHazardConfirmed"] is False and risk["mapValidated"] is False
        assert risk["frequency"] == "UNKNOWN" and risk["intensity"] == "UNKNOWN"
        assert risk["trigger"].strip() and risk["responseToStudy"].strip()

    crossings = unique(v["corridorWaterChecks"], "corridorId")
    assert set(crossings) == CORRIDORS
    for c in crossings.values():
        assert c["waterCrossing"] == "UNKNOWN"
        for key in ("bridgeConfirmed","fordConfirmed","routeConfirmed"):
            assert c[key] is False

    g = v["governance"]
    assert g == {"rodasFiscalOwner":"crown_aethros", "rodasMilitaryOwner":"crown_aethros",
                 "rodasWaterRights":"UNKNOWN","edranorWaterRights":"UNKNOWN",
                 "hallheimInEdranor":False, "waterBasinIsAdministrativeBorder":False,
                 "noInternalCustoms":True}
    assert set(v["forbiddenClaims"]) == EXPECTED_CLAIMS
    assert "EDD-01_NORTH_BOUNDARY_CLOSURE" in v["unknown"]
    assert "EDD-03_LOCAL_RIVERS_AFFLUENTS_AND_CATCHMENTS" in v["unknown"]
    assert "EDD-03_LURIEN_ANTELA_EDRANOR_OVERLAP" in v["unknown"]
    assert "EDD-07_BRIDGES_FORDS_AND_PATHS" in v["unknown"]

checked(data)

# Canon guard: the actual regional source must support the two recovered anchors.
rivers = (N / "Geografía/rios_y_lagos.md").read_text(encoding="utf-8")
for statement in ("Río Lurien", "Lago Antela", "sur de **Karsath**",
                  "vertiente oriental de los Montes Valkram",
                  "navegable desde Hallheim hasta el mar"):
    assert statement in rivers, f"No respalda la fuente: {statement}"

mandatory = [
    BASE/"E02_INDICE.md", BASE/"Cartografia/E02_ATLAS_HIDROGRAFICO.md",
    BASE/"Cartografia/E02_CUENCAS_DIVISORIAS.md",
    BASE/"Cartografia/E02_DRENAJE_Y_RIESGOS.md",
    BASE/"Cartografia/E02_CRUCES_Y_MOVILIDAD.md",
    BASE/"Agua_y_usos/E02_AGUA_Y_VITICULTURA.md",
    BASE/"Auditorias/E02_FUENTES_Y_DECISIONES.md",
    BASE/"Auditorias/E02_ACTA.md",
    BASE/"00_Control_del_proyecto/TRASPASO_E03.md",
    BASE/"Datos operativos/edranor_e02_hydrology_v0.1.json",
    BASE/"Cartografia/E01_ATLAS_RELIEVE.md", BASE/"Cartografia/E01_CORREDORES.md",
    BASE/"Datos operativos/edranor_e01_relief_v0.1.json",
    BASE/"Datos operativos/edranor_e00_manifest_v0.1.json",
    N/"Geografía/rios_y_lagos.md", N/"Geografía/montanas.md",
    N/"Geografía/bosques.md", N/"Clima/clima_general.md",
    ROOT/"Worldbuilding/Sistemas/Nimroel Core/README.md",
    ROOT/"Worldbuilding/Sistemas/Norgard Defaults/README.md",
]
for path in mandatory:
    assert path.is_file() and path.stat().st_size > 50, f"Falta documentación: {path}"

mutations = [
    lambda x: x.update(runtimeEnabled=True),
    lambda x: x.update(phase="E11"),
    lambda x: x.update(status="VALIDATED_RUNTIME"),
    lambda x: x["inheritance"].reverse(),
    lambda x: x["sourceAuthorities"].remove("UNKNOWN"),
    lambda x: x["scope"].update(northBoundaryClosed=True),
    lambda x: x["scope"].update(georeferenced=True),
    lambda x: x["scope"].update(metricGeometryValidated=True),
    lambda x: x["scope"].update(localHydrographyValidated=True),
    lambda x: x["scope"].update(scale="1:10000"),
    lambda x: x["scope"].update(dem="real_dem"),
    lambda x: x["scope"].update(riverPolylines=[[1,2],[3,4]]),
    lambda x: x["scope"].update(basinPolygons=[{"id":"fake"}]),
    lambda x: x["scope"].update(floodPolygons=[[5,6]]),
    lambda x: x["scope"].update(administrativeAndHydrologicalLayersIndependent=False),
    lambda x: x["anchors"][0].update(insideTerritorialScope=False),
    lambda x: x["anchors"][0].update(jurisdictionOwner="crown_aethros"),
    lambda x: x["anchors"][3].update(jurisdictionOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(militaryOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(fiscalOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(berserkersUnderCrown=False),
    lambda x: x["anchors"][4].update(insideTerritorialScope=True),
    lambda x: x["anchors"].append(copy.deepcopy(x["anchors"][0])),
    lambda x: x["regionalCanonicalFeatures"][0].update(name="Río Falso"),
    lambda x: x["regionalCanonicalFeatures"][0].update(membershipInEdranor=True),
    lambda x: x["regionalCanonicalFeatures"][0].update(orderedCourse=["Karsath","Dorth"]),
    lambda x: x["regionalCanonicalFeatures"][0].update(sourceContext="MONTAÑAS_EL YRA"),
    lambda x: x["regionalCanonicalFeatures"][0].update(navigableFrom="karsath"),
    lambda x: x["regionalCanonicalFeatures"][0].update(confirmedCrossings=["puente_falso"]),
    lambda x: x["regionalCanonicalFeatures"][0].update(localFlowRates=400),
    lambda x: x["regionalCanonicalFeatures"][1].update(membershipInEdranor=True),
    lambda x: x["regionalCanonicalFeatures"][1].update(relativeLocation="NORTE_DE_KARSATH"),
    lambda x: x["regionalCanonicalFeatures"][1].update(inputRiver="norgard_rio_caleran"),
    lambda x: x["regionalCanonicalFeatures"][1].update(shoreline="POLYGON"),
    lambda x: x["regionalCanonicalFeatures"].append(copy.deepcopy(x["regionalCanonicalFeatures"][0])),
    lambda x: x["excludedTransplants"][0].update(edranorAssignment=True),
    lambda x: x["excludedTransplants"][1].update(source="none"),
    lambda x: x["localDrainageUnits"][0].update(watercourse="Rio Nuevon"),
    lambda x: x["localDrainageUnits"][0].update(recipientBasin="lurien"),
    lambda x: x["localDrainageUnits"][0].update(outflowDirection="N"),
    lambda x: x["localDrainageUnits"][0].update(groundwater="aquifer_known"),
    lambda x: x["localDrainageUnits"][0].update(subcatchmentsDelimited=True),
    lambda x: x["localDrainageUnits"][0].update(watercourseOnTerritoryConfirmed=True),
    lambda x: x["localDrainageUnits"].append(copy.deepcopy(x["localDrainageUnits"][0])),
    lambda x: x["basinStudyQuestions"][0].update(validated=True),
    lambda x: x["basinStudyQuestions"][0].update(watershedGeometry=[{"x":1}]),
    lambda x: x["basinStudyQuestions"][0].update(edranorOverlap=True),
    lambda x: x["basinStudyQuestions"][0].update(outlet="hallheim"),
    lambda x: x["basinStudyQuestions"][1].update(state="CONFIRMED_BASIN"),
    lambda x: x["basinStudyQuestions"][2].update(relatedFeature="norgard_rio_caleran"),
    lambda x: x["basinStudyQuestions"].append(copy.deepcopy(x["basinStudyQuestions"][0])),
    lambda x: x["useQuestions"][0].update(confirmed=True),
    lambda x: x["useQuestions"][1].update(infrastructure="canal"),
    lambda x: x["useQuestions"][2].update(sourceWaterbody="lago_antela"),
    lambda x: x["useQuestions"][3].update(withdrawalRights="casa_edranor"),
    lambda x: x["useQuestions"][3].update(capacity=300),
    lambda x: x["riskScenarios"][0].update(localHazardConfirmed=True),
    lambda x: x["riskScenarios"][1].update(mapValidated=True),
    lambda x: x["riskScenarios"][2].update(frequency="cada invierno"),
    lambda x: x["riskScenarios"][3].update(state="CERTAIN"),
    lambda x: x["corridorWaterChecks"][0].update(bridgeConfirmed=True),
    lambda x: x["corridorWaterChecks"][1].update(fordConfirmed=True),
    lambda x: x["corridorWaterChecks"][2].update(waterCrossing="Lurien"),
    lambda x: x["corridorWaterChecks"][3].update(routeConfirmed=True),
    lambda x: x["governance"].update(rodasFiscalOwner="casa_edranor"),
    lambda x: x["governance"].update(rodasMilitaryOwner="casa_edranor"),
    lambda x: x["governance"].update(hallheimInEdranor=True),
    lambda x: x["governance"].update(waterBasinIsAdministrativeBorder=True),
    lambda x: x["governance"].update(edranorWaterRights="ALL"),
    lambda x: x["governance"].update(noInternalCustoms=False),
    lambda x: x["forbiddenClaims"].remove("ANTELA_INSIDE_EDRANOR_AS_FACT"),
]
for number, mutate in enumerate(mutations, 1):
    trial = copy.deepcopy(data)
    mutate(trial)
    try:
        checked(trial)
    except (AssertionError, KeyError, TypeError):
        pass
    else:
        raise AssertionError(f"Negativa {number} no rechazada")
print(f"EDRANOR E02 STATIC PASS | 2 referencias regionales | 7 fichas E01 | 4 cuencas en estudio | 4 riesgos condicionales | 4 usos | 4 corredores | {len(mutations)} negativas | {len(mandatory)} fuentes/archivos | E00/E01 consistentes")

"""G02: datos de hidrología, contratos no-runtime y mutaciones negativas.
Solo validación documental: NO ejecuta Godot, CoreRPG ni simula caudales.
"""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NORGARD = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
HOUSE = NORGARD / "Territorios/Casa Galdren"
DATA = HOUSE / "Datos operativos"
g0 = json.loads((DATA / "galdren_g00_manifest_v0.1.json").read_text(encoding="utf-8"))
g1 = json.loads((DATA / "galdren_g01_geography_v0.1.json").read_text(encoding="utf-8"))
g2 = json.loads((DATA / "galdren_g02_hydrology_v0.1.json").read_text(encoding="utf-8"))

MAIN = "db49fde947463a7305b9ae453aa1c844740f6dda"
RIVERS = ["rio_caleran", "rio_vornarsk", "rio_keldarsk", "rio_sareno", "rio_theleno"]
ARMS = ["brazo_occidental_caleran", "brazo_oriental_caleran"]
BASINS = ["G02-C%02d" % i for i in range(1, 6)]
INTERFACES = ["G02-I%02d" % i for i in range(1, 7)]
RISKS = ["G02-R%02d" % i for i in range(1, 6)]
EXPECTED_SOURCES = [
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/rios_y_lagos.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/montanas.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/mares_y_costas.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/bosques.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Geografía/Montes Invernos/cotas_y_altitudes_borrador.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Galdren/Cartografia/G01_ATLAS_FISICO.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Galdren/Cartografia/G01_LIMITES_Y_VERTIENTES.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Galdren/Datos operativos/galdren_g01_geography_v0.1.json",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Galdren/00_Control_del_proyecto/TRASPASO_G02.md",
  "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/Cartografia/E02_ATLAS_HIDROGRAFICO.md"
]
UNKNOWN = [
    "CALERAN_SOURCE_TO_EASTERN_PLAINS_TRACE", "CALERAN_EXACT_SPLIT_GEOMETRY",
    "CALERAN_MOUTH_COUNT_AND_BANKS", "VORNARSK_SOURCE_AND_OUTLET",
    "KELDARSK_SOURCE_AND_OUTLET", "ZANTHIR_BASIN_DIVIDES",
    "INVERNOS_GALDREN_VALRIK_DRAINAGE_DIVIDE", "SEASONAL_CALENDAR_AND_DISCHARGE",
    "GAUGED_FLOODPLAINS", "WATER_INFRASTRUCTURE_AND_NAVIGABILITY",
    "LEGAL_BANKS_AND_COASTS",
]

def indexing(records, ids):
    assert type(records) is list and len(records) == len(ids)
    found = [r["id"] for r in records]
    assert found == ids, "Cardinalidad, orden o identidad alterados"
    assert len(set(found)) == len(found)
    return dict(zip(ids, records))

def all_false(mapping, names):
    for key in names:
        assert mapping[key] is False, "Campo falsamente verificado: " + key

def validate(x):
    assert type(x) is dict
    assert x["schemaVersion"] == 1
    assert x["documentId"] == "galdren_g02" and x["phase"] == "G02"
    assert x["version"] == "0.1.0" and x["date"] == "2026-11-13"
    assert x["baselineMainSha"] == MAIN
    assert x["baseDocumentId"] == g1["documentId"] == "galdren_g01"
    assert x["status"] == "DOCUMENTARY_PLANNING_ONLY"
    assert x["runtimeEnabled"] is False
    assert x["authorApproval"] == "G02_WORK_APPROVED; NEW_TOPOLOGY_AND_TOPONYMS_NOT_RATIFIED"
    assert x["inheritance"] == g0["inheritance"] == g1["inheritance"]
    all_false(x["limitations"], [
        "georeferenced", "metricGeometryVerified", "legalBordersVerified",
        "waterflowSimulationValidated", "bridgesVerified", "portsVerified",
        "navigabilityVerified", "quantitativeDischargeVerified", "newRiverNamesApproved"])
    guard = x["guardrails"]
    assert guard == {
        "caleranOneRiver": True, "azuriosWesternBirth": True,
        "easternPlainsCanon": True, "transitionRouteResolved": False,
        "treskalOwner": "casa_valrik", "dorthOwner": "casa_edranor",
        "hallheimOwner": "crown_aethros", "invernosShared": True,
        "permanentGlaciersConfirmed": False, "metalEstelarOnly": "montes_azurios",
        "newWatercoursesAdded": 0,
    }
    assert len(g0["canonToponyms"]) == 18
    assert g1["invariants"]["noNewRivers"] is True
    assert g1["protectedSettlements"][2]["id"] == "treskal"
    assert g1["protectedSettlements"][2]["owner"] == "casa_valrik"
    r = indexing(x["rivers"], RIVERS)
    assert [t["name"] for t in r.values()] == [
        "Río Caleran", "Río Vornarsk", "Río Keldarsk", "Río Sareno", "Río Theleno"]
    for row in r.values():
        assert row["type"] == "RIVER" and row["evidence"] == "CANON_REPO"
        assert row["independent"] is True and row["mouthPositionVerified"] is False
    assert r["rio_caleran"]["source"] == "montes_azurios_vertiente_occidental"
    assert r["rio_caleran"]["flowTo"] == "mar_suthiros" and r["rio_caleran"]["sourceVerified"] is True
    assert r["rio_caleran"]["houseContext"] == "casa_galdren"
    for identifier in ("rio_vornarsk", "rio_keldarsk"):
        q = r[identifier]
        assert q["source"] == q["flowTo"] == "UNKNOWN"
        assert q["sourceVerified"] is False and q["houseContext"] == "entorno_zanthir"
    for identifier in ("rio_sareno", "rio_theleno"):
        q = r[identifier]
        assert q["houseContext"] == "casa_valrik_treskal"
        assert q["flowTo"] == "mar_suthiros"
        assert q["source"] == "montes_invernos_vertiente_meridional" and q["sourceVerified"] is True
    c = x["caleran"]
    assert c["systemId"] == "rio_caleran"
    assert c["birth"] == "montes_azurios_vertiente_occidental"
    assert c["crossesEasternFertilePlains"] is True
    assert c["passes"] == ["arleon"]
    assert c["westToEastLink"] == "TOPOGRAPHIC_ROUTE_UNRESOLVED"
    assert c["cartographicCrossingInvented"] is False
    assert c["upperMainCourseId"] == "rio_caleran"
    assert c["splitOrder"] == ["caleran_main_first_split", "caleran_arms_secondary_splits", "suthiros_outlet"]
    assert c["twoNamedArms"] == ARMS
    arms = indexing(c["arms"], ARMS)
    for arm in arms.values():
        assert arm["parent"] == "rio_caleran" and arm["isNewRiver"] is False
        assert arm["hasSecondaryBifurcation"] is True and arm["secondaryChannelsNamed"] is False
        assert arm["terminalMouthCount"] is None
    assert c["mouthSea"] == "mar_suthiros"
    assert c["confirmedOutletCount"] is None and c["joinedBackBeforeSea"] == "UNKNOWN"
    assert c["navigationStatus"] == "UNKNOWN" and c["floodReturnPeriodYears"] is None
    north = x["northern"]
    assert north == {
        "rivers": ["rio_vornarsk", "rio_keldarsk"],
        "context": "zanthir",
        "originLanguage": "DWARVEN_HYDRONYMS_CANON",
        "etymologiesRatified": False,
        "winterIce": "CANON",
        "sourceMountain": "UNKNOWN",
        "receivingSea": "UNKNOWN",
        "mutualConfluence": "UNKNOWN",
        "winterClosureDates": "UNKNOWN",
        "navigability": "UNKNOWN",
    }
    v = x["treskal"]
    assert v == {
        "rivers": ["rio_sareno", "rio_theleno"],
        "bornOn": "montes_invernos_vertiente_meridional",
        "distinctBeforeLowerCourse": True,
        "convergeAtFinalCourse": True,
        "finalCommonChannelIsNewNamedRiver": False,
        "commonOutlet": "mar_suthiros",
        "near": "treskal",
        "treskalHouse": "casa_valrik",
        "galdrenClaim": False,
        "westernTwinBorderSegment": "REGIONAL_CONCEPT_ONLY",
        "fixedBankSide": "UNKNOWN",
    }
    basin = indexing(x["basinStudies"], BASINS)
    assert [a["watercourse"] for a in basin.values()] == RIVERS
    assert [a["outlet"] for a in basin.values()] == [
        "mar_suthiros", "UNKNOWN", "UNKNOWN", "mar_suthiros", "mar_suthiros"]
    for identifier, q in basin.items():
        assert q["watershedDelineated"] is False and q["metricTraceVerified"] is False
        assert q["houseJurisdiction"] in ("UNKNOWN", "casa_valrik_contexto_sin_poligono")
        if identifier in BASINS[:3]:
            assert q["class"] == "CANONICAL_RIVER_UNDELIMITED_CATCHMENT"
        else:
            assert q["class"] == "NEIGHBOR_REFERENCE_ONLY"
    interface = indexing(x["interfaceStudies"], INTERFACES)
    assert [a["site"] for a in interface.values()] == [
        "azurios_oeste_este", "invernos_sur", "valrik_treskal",
        "zanthir_bahia_norte", "caleran_suthiros", "azurios_edranor"]
    for a in interface.values():
        assert a["question"] and a["status"] == "UNRESOLVED"
        assert a["legalAllocation"] == "UNKNOWN" and a["coordinatesVerified"] is False
    risk = indexing(x["riskStudies"], RISKS)
    assert [a["kind"] for a in risk.values()] == [
        "ZANTHIR_WINTER_ICE", "INVERNOS_SNOWMELT_RUNOFF",
        "ARLEON_CALERAN_FLOODPLAIN", "CALERAN_LOWER_BRANCH_RECONFIGURATION",
        "ZANTHIR_BAY_NAVIGATION_ICE"]
    assert [a["status"] for a in risk.values()] == [
        "CANON_QUALITATIVE", "REGIONAL_DRAFT_QUALITATIVE", "STUDY_ONLY",
        "STUDY_ONLY", "CANON_QUALITATIVE"]
    for a in risk.values():
        assert a["floodHeightMeters"] is None and a["infrastructureConfirmed"] is False
        assert a["frequency"] in ("UNKNOWN", "WINTER_NO_DATES")
    assert x["unknown"] == UNKNOWN
    assert x["sourceRegistry"] == EXPECTED_SOURCES
    assert len(x["sourceRegistry"]) == len(set(x["sourceRegistry"])) == 10
    for path in x["sourceRegistry"]:
        assert (ROOT / path).is_file(), "Fuente ausente: " + path

validate(g2)
docs = [
    "G02_INDICE.md", "Cartografia/G02_ATLAS_HIDROGRAFICO.md",
    "Cartografia/G02_TOPOLOGIA_CALERAN.md",
    "Cartografia/G02_CUENCAS_DIVISORIAS.md",
    "Hidrologia/G02_ESTACIONALIDAD_Y_RIESGOS.md",
    "Auditorias/G02_FUENTES_Y_DEUDA.md", "Auditorias/G02_ACTA.md",
    "00_Control_del_proyecto/TRASPASO_G03.md"]
for p in docs:
    assert (HOUSE / p).is_file(), "Documento ausente: " + p
assert "NO" in (HOUSE / "Cartografia/G02_TOPOLOGIA_CALERAN.md").read_text(encoding="utf-8")
assert "Treskal" in (HOUSE / "Cartografia/G02_CUENCAS_DIVISORIAS.md").read_text(encoding="utf-8")

def change(path, value):
    def fn(x):
        y = x
        for key in path[:-1]:
            y = y[key]
        y[path[-1]] = value
    return fn

attacks = [
    ("runtime", change(["runtimeEnabled"], True)),
    ("phase", change(["phase"], "G03")),
    ("approval", change(["authorApproval"], "NUEVOS_RIOS_CANON")),
    ("baseline", change(["baselineMainSha"], "deadbeef")),
    ("georef", change(["limitations","georeferenced"], True)),
    ("metric", change(["limitations","metricGeometryVerified"], True)),
    ("legal", change(["limitations","legalBordersVerified"], True)),
    ("flow_sim", change(["limitations","waterflowSimulationValidated"], True)),
    ("bridges", change(["limitations","bridgesVerified"], True)),
    ("ports", change(["limitations","portsVerified"], True)),
    ("navigation", change(["limitations","navigabilityVerified"], True)),
    ("discharge", change(["limitations","quantitativeDischargeVerified"], True)),
    ("ratified_naming", change(["limitations","newRiverNamesApproved"], True)),
    ("two_calerans", change(["guardrails","caleranOneRiver"], False)),
    ("birth_east", change(["guardrails","azuriosWesternBirth"], False)),
    ("plains_lost", change(["guardrails","easternPlainsCanon"], False)),
    ("invented_crossing", change(["guardrails","transitionRouteResolved"], True)),
    ("annex_treskal", change(["guardrails","treskalOwner"], "casa_galdren")),
    ("annex_dorth", change(["guardrails","dorthOwner"], "casa_galdren")),
    ("annex_hallheim", change(["guardrails","hallheimOwner"], "casa_galdren")),
    ("invernos_private", change(["guardrails","invernosShared"], False)),
    ("glacier", change(["guardrails","permanentGlaciersConfirmed"], True)),
    ("new_metal", change(["guardrails","metalEstelarOnly"], "zanthir")),
    ("new_river_count", change(["guardrails","newWatercoursesAdded"], 1)),
    ("rename_river", change(["rivers",0,"name"], "Río Nuevo")),
    ("river_extra", lambda x: x["rivers"].append(dict(x["rivers"][0], id="rio_inventado"))),
    ("caleran_source", change(["rivers",0,"source"], "montes_azurios_vertiente_oriental")),
    ("vornarsk_mouth", change(["rivers",1,"flowTo"], "bahia_zanthir")),
    ("keldarsk_source", change(["rivers",2,"source"], "montes_invernos")),
    ("sareno_galdren", change(["rivers",3,"houseContext"], "casa_galdren")),
    ("theleno_confluence", change(["treskal","convergeAtFinalCourse"], False)),
    ("treskal_claim", change(["treskal","galdrenClaim"], True)),
    ("new_common_river", change(["treskal","finalCommonChannelIsNewNamedRiver"], True)),
    ("azurios_tunnel", change(["caleran","cartographicCrossingInvented"], True)),
    ("caleran_link", change(["caleran","westToEastLink"], "KNOWN_TUNNEL")),
    ("first_fork", change(["caleran","splitOrder",0], "mouth")),
    ("third_arm", lambda x: x["caleran"]["twoNamedArms"].append("brazo_central")),
    ("new_arm_river", change(["caleran","arms",0,"isNewRiver"], True)),
    ("renamed_channel", change(["caleran","arms",1,"secondaryChannelsNamed"], True)),
    ("invented_mouths", change(["caleran","confirmedOutletCount"], 4)),
    ("invented_nav", change(["caleran","navigationStatus"], "YES")),
    ("invented_ice_dates", change(["northern","winterClosureDates"], "enero-marzo")),
    ("northern_outlet", change(["northern","receivingSea"], "mar_del_norte")),
    ("northern_fuse", change(["northern","mutualConfluence"], "YES")),
    ("northern_etym", change(["northern","etymologiesRatified"], True)),
    ("basin_poly", change(["basinStudies",0,"watershedDelineated"], True)),
    ("basin_owner", change(["basinStudies",1,"houseJurisdiction"], "casa_galdren")),
    ("vornarsk_to_bay", change(["basinStudies",1,"outlet"], "bahia_zanthir")),
    ("valrik_basin", change(["basinStudies",3,"class"], "GALDREN_BASIN")),
    ("border", change(["interfaceStudies",2,"legalAllocation"], "casa_galdren")),
    ("coordinates", change(["interfaceStudies",0,"coordinatesVerified"], True)),
    ("ice_wrong", change(["riskStudies",0,"status"], "STUDY_ONLY")),
    ("flood_canon", change(["riskStudies",2,"status"], "CANON_QUALITATIVE")),
    ("flood_height", change(["riskStudies",2,"floodHeightMeters"], 15)),
    ("flood_port", change(["riskStudies",3,"infrastructureConfirmed"], True)),
    ("source_path", change(["sourceRegistry",0], "inventada.md")),
    ("unknown_closed", lambda x: x["unknown"].remove("CALERAN_SOURCE_TO_EASTERN_PLAINS_TRACE")),
    ("duplicate_basin", lambda x: x["basinStudies"].append(copy.deepcopy(x["basinStudies"][0]))),
]
for label, fn in attacks:
    z = copy.deepcopy(g2)
    fn(z)
    try:
        validate(z)
    except (AssertionError, KeyError, TypeError, IndexError):
        continue
    raise AssertionError("Mutación indebida aceptada: " + label)
print("GALDREN G02 STATIC PASS | 5 rios canónicos | 2 brazos | 5 cuencas de estudio | 6 interfaces | 5 riesgos | 10 fuentes | %d negativas" % len(attacks))

"""Validación estática/adversarial G01. NO ejecuta CoreRPG, Godot ni contenido jugable."""
import copy
import json
from pathlib import Path

repo = Path(__file__).resolve().parents[2]
n = repo / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
house = n / "Territorios/Casa Galdren"
g0 = json.loads((house / "Datos operativos/galdren_g00_manifest_v0.1.json").read_text(encoding="utf-8"))
g1 = json.loads((house / "Datos operativos/galdren_g01_geography_v0.1.json").read_text(encoding="utf-8"))

unit_ids = {"G01-U%02d" % i for i in range(1, 13)}
border_ids = {"G01-B%02d" % i for i in range(1, 7)}
corridor_ids = {"G01-C%02d" % i for i in range(1, 7)}
dossier_ids = {"TOP-%02d" % i for i in range(1, 6)}
known_ids = [t["id"] for t in g0["canonToponyms"]]
fixed_invariants = {
    "singleCrown": True,
    "houseSovereign": False,
    "metalEstelarOnly": "montes_azurios",
    "caleranSingleRiverSystem": True,
    "invernosSharedGaldrenValrik": True,
    "invernosBoundaryCrossesNorthSouth": True,
    "highestInvernosPeakAssigned": False,
    "forjaOwner": "UNKNOWN",
    "forjaPeacetimeAdministrator": "casa_galdren",
    "forjaWartimeStrategicCommand": "crown_aethros_hallheim",
    "noNewRivers": True,
}
fixed_protected = {
    "arleon": ("casa_galdren", None),
    "zanthir": ("casa_galdren", None),
    "treskal": ("casa_valrik", False),
    "hallheim": ("crown_aethros", False),
    "dorth": ("casa_edranor", False),
    "forja_estelar": ("UNKNOWN", None),
}
fixed_sources = {
    "Geografía/geografia_general.md",
    "Geografía/montanas.md",
    "Geografía/Montes Invernos/cotas_y_altitudes_borrador.md",
    "Geografía/rios_y_lagos.md",
    "Geografía/mares_y_costas.md",
    "Geografía/bosques.md",
    "Geografía/regiones_naturales.md",
    "Toponimia/convencion_toponimica_norgard_v0.1.md",
    "Grandes Casas/grandes_casas.md",
    "Territorios/Casa Galdren/Cartografia/G00_CARTOGRAFIA.md",
    "Territorios/Casa Galdren/Toponimia/G00_REGISTRO_TOPONIMIA.md",
    "Territorios/Casa Galdren/Datos operativos/galdren_g00_manifest_v0.1.json",
}
fixed_source_paths = {
    "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/" + p
    for p in fixed_sources
}
fixed_candidates = {
    "TOP-02": "Laderas Frías",
    "TOP-03": "Vegas de Arleon",
}

def unique_index(rows, allowed):
    assert type(rows) is list and len(rows) == len(allowed)
    ids = [r["id"] for r in rows]
    assert len(set(ids)) == len(ids), "IDs duplicados"
    assert set(ids) == allowed, "IDs fuera de contrato"
    return {r["id"]: r for r in rows}

def validate(x):
    assert type(x) is dict
    assert x["schemaVersion"] == 1
    assert x["documentId"] == "galdren_g01" and x["phase"] == "G01"
    assert x["version"] == "0.1.0" and x["date"] == "2026-11-13"
    assert x["status"] == "DOCUMENTARY_PLANNING_ONLY" and x["runtimeEnabled"] is False
    assert x["authorApproval"] == "G01_WORK_APPROVED; NEW_TOPONYMS_NOT_RATIFIED"
    assert x["baselineMainSha"] == "5b18e8f255a0ee90a0cb2c6ddf08f16760acc15f"
    assert x["baseDocumentId"] == g0["documentId"] == "galdren_g00"
    assert x["inheritance"] == g0["inheritance"]
    geo = x["mapping"]
    assert geo == {
        "redOutlineApproximate": True,
        "authorMarkedMapCommitted": False,
        "georeferenceVerified": False,
        "metricGeometryVerified": False,
        "coordinatesVerified": False,
        "polygonVerified": False,
        "legalBordersVerified": False,
    }
    assert x["invariants"] == fixed_invariants
    assert g0["locations"][3]["id"] == "treskal"
    loc = unique_index(x["protectedSettlements"], set(fixed_protected))
    for id_, (owner, inside) in fixed_protected.items():
        assert loc[id_]["owner"] == owner
        if inside is not None:
            assert loc[id_]["insideGaldren"] is inside
    forge = loc["forja_estelar"]
    assert forge["kind"] == "INSTALACION_ESTRATEGICA"
    assert forge["ownershipTitle"] == "UNKNOWN" and forge["locationVerified"] is False
    assert x["canonicalToponymIds"] == known_ids
    assert len(known_ids) == 18 and len(set(known_ids)) == len(known_ids)
    units = unique_index(x["reliefUnits"], unit_ids)
    for item in units.values():
        assert item["evidenceClass"] in ("CANON_REPO", "REGIONAL_BORRADOR_APROBADO", "HYPOTHESIS_G01")
        assert item["isPoliticalDivision"] is False
        assert item["jurisdictionOwner"] == "UNKNOWN"
        assert item["localHeightAssigned"] is False and item["metricGeometryVerified"] is False
        assert item["anchor"] and item["kind"]
    assert units["G01-U02"]["kind"] == "INVERNOS_SHARED"
    assert units["G01-U11"]["kind"] == "VALRIK_TRESKAL_INTERFACE"
    assert units["G01-U12"]["kind"] == "VELARIS_VARETH_CONTEXT"
    boundaries = unique_index(x["borderInterfaces"], border_ids)
    assert boundaries["G01-B01"]["neighbor"] == "crown_aethros"
    assert boundaries["G01-B02"]["neighbor"] == "casa_edranor"
    assert boundaries["G01-B03"]["neighbor"] == "casa_valrik"
    assert boundaries["G01-B04"]["sector"] == "NORTH_INVERNOS"
    for item in boundaries.values():
        assert item["exactLegalBorder"] == "UNKNOWN"
        assert item["boundaryFixed"] is False and item["metricTraceVerified"] is False
    corridors = unique_index(x["corridorStudies"], corridor_ids)
    for item in corridors.values():
        assert item["status"] == "STUDY_ONLY"
        assert item["physicalContactValidated"] is False
        assert item["routeVerified"] is False
        assert item["bridgeVerified"] is False
        assert item["navigabilityVerified"] is False
        assert item["lengthKm"] is None
    assert corridors["G01-C01"]["origin"] == "Arleon"
    assert corridors["G01-C01"]["destination"] == "Zanthir"
    feats = unique_index(x["featureDossiers"], dossier_ids)
    all_candidates = {}
    for id_, item in feats.items():
        assert item["featureConfirmed"] is False
        assert item["authorRatification"] == "PENDING"
        assert item["jurisdictionOwner"] == "UNKNOWN"
        assert item["coordinatesVerified"] is False
        assert item["waterTopologyVerified"] is False
        assert type(item["nameCandidates"]) is list
        for c in item["nameCandidates"]:
            assert c["status"] == "PROPUESTA_NO_CANON"
            assert c["ratified"] is False
            assert c["assertedIndependentFeature"] is False
            assert c["name"] and id_ not in all_candidates
            all_candidates[id_] = c["name"]
    assert all_candidates == fixed_candidates
    inv = x["invernosRegionalDraft"]
    assert inv == {
        "scope": "ENTIRE_SHARED_MOUNTAIN_CHAIN",
        "approval": "REGIONAL_BORRADOR_APROBADO",
        "localHeightsEstablished": False,
        "crestTypicalMeters": [2200, 2800],
        "exceptionalPeakMaximumApproxMeters": 3600,
        "primaryPassRangeMeters": [1500, 2100],
        "peakHouseAssignment": "UNKNOWN",
        "permanentGlaciersConfirmed": False,
    }
    required = {"GDD-01","GDD-02","GDD-03","GDD-07","TOPOGRAPHY_CALERAN_SOURCE_TO_PLAINS",
                "NORTH_COAST_LEGAL_SCOPE","INVERNOS_PASS_GEOMETRY","RIVER_SECONDARY_NETWORK","G02_NOT_STARTED"}
    assert type(x["unresolved"]) is list and set(x["unresolved"]) == required
    assert type(x["sourceRegistry"]) is list and set(x["sourceRegistry"]) == fixed_source_paths
    assert len(x["sourceRegistry"]) == len(set(x["sourceRegistry"])) == 12

validate(g1)
for path in g1["sourceRegistry"]:
    assert (repo / path).is_file(), "Fuente no encontrada: " + path
documents = (
    "G01_INDICE.md", "Cartografia/G01_ATLAS_FISICO.md",
    "Cartografia/G01_LIMITES_Y_VERTIENTES.md",
    "Cartografia/G01_CORREDORES_HIPOTETICOS.md",
    "Toponimia/G01_FICHAS_TOP_01_05.md",
    "Toponimia/G01_COLISIONES_Y_CONVENCION.md",
    "Auditorias/G01_FUENTES_Y_DECISIONES.md",
    "Auditorias/G01_ACTA.md", "00_Control_del_proyecto/TRASPASO_G02.md",
)
for name in documents:
    assert (house / name).is_file(), "Documento G01 ausente: " + name
assert "PROPUESTA_NO_CANON" in (house / "Toponimia/G01_FICHAS_TOP_01_05.md").read_text(encoding="utf-8")
assert "Treskal" in (house / "Cartografia/G01_LIMITES_Y_VERTIENTES.md").read_text(encoding="utf-8")

def mutate(path, val):
    def apply(x):
        z = x
        for p in path[:-1]:
            z = z[p]
        z[path[-1]] = val
    return apply

attacks = [
    ("runtime", mutate(["runtimeEnabled"], True)),
    ("phase", mutate(["phase"], "G02")),
    ("document", mutate(["documentId"], "galdren_core")),
    ("approval", mutate(["authorApproval"], "CANON_RATIFIED")),
    ("base", mutate(["baselineMainSha"], "deadbeef")),
    ("map_exact", mutate(["mapping","redOutlineApproximate"], False)),
    ("map_committed", mutate(["mapping","authorMarkedMapCommitted"], True)),
    ("georef", mutate(["mapping","georeferenceVerified"], True)),
    ("metric", mutate(["mapping","metricGeometryVerified"], True)),
    ("coordinates", mutate(["mapping","coordinatesVerified"], True)),
    ("polygon", mutate(["mapping","polygonVerified"], True)),
    ("borders", mutate(["mapping","legalBordersVerified"], True)),
    ("sovereignty", mutate(["invariants","houseSovereign"], True)),
    ("metal", mutate(["invariants","metalEstelarOnly"], "zanthir")),
    ("caleran", mutate(["invariants","caleranSingleRiverSystem"], False)),
    ("invernos_shared", mutate(["invariants","invernosSharedGaldrenValrik"], False)),
    ("boundary_mountains", mutate(["invariants","invernosBoundaryCrossesNorthSouth"], False)),
    ("highest_peak", mutate(["invariants","highestInvernosPeakAssigned"], True)),
    ("forge_owned", mutate(["invariants","forjaOwner"], "casa_galdren")),
    ("forge_war", mutate(["invariants","forjaWartimeStrategicCommand"], "casa_galdren")),
    ("new_river", mutate(["invariants","noNewRivers"], False)),
    ("treskal", mutate(["protectedSettlements",2,"owner"], "casa_galdren")),
    ("treskal_inside", mutate(["protectedSettlements",2,"insideGaldren"], True)),
    ("hallheim", mutate(["protectedSettlements",3,"owner"], "casa_galdren")),
    ("dorth", mutate(["protectedSettlements",4,"insideGaldren"], True)),
    ("forja_title", mutate(["protectedSettlements",5,"ownershipTitle"], "casa_galdren")),
    ("forja_georef", mutate(["protectedSettlements",5,"locationVerified"], True)),
    ("topo_name", mutate(["canonicalToponymIds",0], "laderas_frias")),
    ("region_politica", mutate(["reliefUnits",0,"isPoliticalDivision"], True)),
    ("azurios_claim", mutate(["reliefUnits",0,"jurisdictionOwner"], "casa_galdren")),
    ("height_derived", mutate(["reliefUnits",1,"localHeightAssigned"], True)),
    ("invernos_kind", mutate(["reliefUnits",1,"kind"], "GLACIER")),
    ("border_legal", mutate(["borderInterfaces",2,"boundaryFixed"], True)),
    ("border_valrik", mutate(["borderInterfaces",2,"neighbor"], "casa_galdren")),
    ("road", mutate(["corridorStudies",0,"routeVerified"], True)),
    ("bridge", mutate(["corridorStudies",1,"bridgeVerified"], True)),
    ("distance", mutate(["corridorStudies",1,"lengthKm"], 42)),
    ("navigation", mutate(["corridorStudies",2,"navigabilityVerified"], True)),
    ("top_confirmed", mutate(["featureDossiers",0,"featureConfirmed"], True)),
    ("top_ratified", mutate(["featureDossiers",1,"authorRatification"], "APPROVED")),
    ("top_promoted", mutate(["featureDossiers",1,"nameCandidates",0,"status"], "CANON_REPO")),
    ("top_claimed", mutate(["featureDossiers",2,"nameCandidates",0,"assertedIndependentFeature"], True)),
    ("alt_peak", mutate(["invernosRegionalDraft","peakHouseAssignment"], "casa_galdren")),
    ("glacier", mutate(["invernosRegionalDraft","permanentGlaciersConfirmed"], True)),
    ("alt_local", mutate(["invernosRegionalDraft","localHeightsEstablished"], True)),
    ("sources", mutate(["sourceRegistry",0], "missing_source.md")),
    ("g02", mutate(["unresolved",8], "G02_COMPLETED")),
    ("duplicate_unit", lambda x: x["reliefUnits"].append(copy.deepcopy(x["reliefUnits"][0]))),
    ("extra_candidate", lambda x: x["featureDossiers"][0]["nameCandidates"].append({
        "name":"Cima Falsa","status":"PROPUESTA_NO_CANON",
        "ratified":False,"assertedIndependentFeature":False})),
]
for label, attack in attacks:
    bad = copy.deepcopy(g1)
    attack(bad)
    try:
        validate(bad)
    except (AssertionError, KeyError, TypeError, IndexError):
        continue
    raise AssertionError("Mutación indebida aceptada: " + label)
print("GALDREN G01 STATIC PASS | 12 unidades | 6 bordes | 6 corredores | 5 TOP | 18 topónimos heredados | 12 fuentes | %d negativas" % len(attacks))

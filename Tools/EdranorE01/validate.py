"""E01: regresion contractual estatica, no prueba CoreRPG ni Godot."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard"
BASE = N / "Territorios/Casa Edranor"
old = json.loads((BASE / "Datos operativos/edranor_e00_manifest_v0.1.json").read_text(encoding="utf-8"))
data = json.loads((BASE / "Datos operativos/edranor_e01_relief_v0.1.json").read_text(encoding="utf-8"))

ALLOWED = {"CANON_REPO", "AUTOR_2026_11_12", "OBSERVACION_MAPA", "PROPUESTA", "UNKNOWN"}
LAYERS = ["nimroel_core", "norgard_defaults", "casa_edranor", "localidad", "world_state"]
ANCHORS = {"dorth", "lumina", "karsath", "rodas", "hallheim"}
UNITS = {"edr_e01_west_valkram_interface", "edr_e01_karsath_central_west", "edr_e01_lumina_bosque_alto", "edr_e01_central_wine_context", "edr_e01_dorth_azurios_west", "edr_e01_north_cold_transition", "edr_e01_far_north_unclosed"}
EXPECTED_CONTACTS = {"edr_e01_contact_west_center", "edr_e01_contact_karsath_lumina", "edr_e01_contact_lumina_dorth", "edr_e01_contact_south_north", "edr_e01_contact_north_edge"}
EXPECTED_CORRIDORS = {"edr_e01_corridor_karsath_lumina", "edr_e01_corridor_lumina_dorth", "edr_e01_corridor_rodas", "edr_e01_corridor_valkram"}

def checked(v):
    assert v["schemaVersion"] == 1 and v["documentId"] == "edranor_e01_relief"
    assert v["phase"] == "E01" and v["runtimeEnabled"] is False
    assert v["status"] == "DOCUMENTARY_PLANNING_ONLY"
    assert v["inheritance"] == LAYERS and set(v["sourceAuthorities"]) == ALLOWED
    cart = v["cartography"]
    assert cart["reference"] == "E00_MAPA_Y_LIMITES.md"
    assert cart["northBoundaryClosed"] is False and cart["metricGeometryValidated"] is False
    assert cart["georeferenced"] is False and cart["drainageBasinsValidated"] is False
    assert cart["watercoursesValidated"] is False and cart["polygonGeometry"] == []
    for k in ("coordinateSystem", "scale", "elevationModel"):
        assert cart[k] == "UNKNOWN"
    pts = v["anchors"]
    p = {a["id"]: a for a in pts}
    assert len(p) == len(pts) and set(p) == ANCHORS
    for k in ("dorth", "lumina", "karsath"):
        assert p[k]["insideTerritorialScope"] is True
        assert p[k]["jurisdictionOwner"] == "casa_edranor" and p[k]["procedural"] is False
    assert p["dorth"]["territorialRole"] == "SEDE"
    assert p["rodas"]["insideTerritorialScope"] is True and p["rodas"]["procedural"] is False
    assert p["rodas"]["territorialRole"] == "ENCLAVE_REAL_GEOGRAFICO"
    assert p["rodas"]["urbanClass"].startswith("ALDEA_AUTOR_")
    for k in ("jurisdictionOwner", "militaryOwner", "fiscalOwner"):
        assert p["rodas"][k] == "crown_aethros"
    assert p["hallheim"]["insideTerritorialScope"] is False
    assert p["hallheim"]["jurisdictionOwner"] == "crown_aethros"
    assert p["hallheim"]["procedural"] is False
    assert old["house"]["seatId"] == "dorth"
    assert set(old["protectedIds"]) == ANCHORS
    old_rodas = next(x for x in old["locations"] if x["id"] == "rodas")
    assert old_rodas["jurisdictionOwner"] == p["rodas"]["jurisdictionOwner"]
    units = v["reliefUnits"]
    u = {a["id"]: a for a in units}
    assert len(u) == len(units) and set(u) == UNITS
    assert u["edr_e01_lumina_bosque_alto"]["landform"] == "MESETA_ELEVADA_FORESTAL"
    assert u["edr_e01_dorth_azurios_west"]["evidence"] == "CANON_REPO"
    assert u["edr_e01_far_north_unclosed"]["evidence"] == "UNKNOWN"
    for a in units:
        assert a["evidence"] in ALLOWED and a["territorialExtent"] == "UNKNOWN"
        assert a["slopeAssignment"] == "UNKNOWN" and a["elevation"] == "UNKNOWN"
        assert a["description"].strip()
    contacts = v["qualitativeContacts"]
    assert len(contacts) == len(EXPECTED_CONTACTS)
    assert {a["id"] for a in contacts} == EXPECTED_CONTACTS
    for a in contacts:
        assert a["from"] in u and a["to"] in u and a["from"] != a["to"]
        assert a["status"] == "HYPOTHESIS"
        assert a["physicalContactValidated"] is False and a["travelRouteConfirmed"] is False
    corridors = v["corridorQuestions"]
    assert len(corridors) == len(EXPECTED_CORRIDORS)
    assert {a["id"] for a in corridors} == EXPECTED_CORRIDORS
    for a in corridors:
        assert a["routeExists"] is False and a["passNamed"] is False
        assert a["physicalTransitValidated"] is False and a["trace"] == "UNKNOWN"
        assert a["futurePhase"] == "E05"
        assert set(a["endpoints"]) <= ANCHORS - {"hallheim"}
        assert a["type"] in {"TOPOLOGICAL_STUDY_ONLY","JURISDICTION_CROSSING_STUDY_ONLY","UNLOCATED_MOUNTAIN_PASS_STUDY_ONLY"}
    overlay = v["administrativeOverlays"]
    assert overlay == {"rodasControlledBy":"crown_aethros","berserkersControlledBy":"crown_aethros","hallheimOutside":True,"forestOwnerships":"UNKNOWN","noInternalCustoms":True}
    assert "EDD-01_NORTH_BOUNDARY_CLOSURE" in v["unknown"]
    assert "EDD-03_DRAINAGE_AND_HYDRONYMS" in v["unknown"]
    assert "RODAS_EDRANOR_JURISDICTION" in v["forbiddenClaims"]
    assert "POLAR_WINE_VINEYARDS_BY_DEFAULT" in v["forbiddenClaims"]

checked(data)

mandatory = [
    N/"NORGARD.md", N/"Grandes Casas/grandes_casas.md",
    N/"Geografía/bosques.md", N/"Geografía/montanas.md",
    N/"Geografía/regiones_naturales.md", N/"Clima/clima_general.md",
    ROOT/"Worldbuilding/Sistemas/Nimroel Core/README.md",
    ROOT/"Worldbuilding/Sistemas/Norgard Defaults/README.md",
    BASE/"Cartografia/E00_MAPA_Y_LIMITES.md",
    BASE/"E01_INDICE.md", BASE/"Cartografia/E01_ATLAS_RELIEVE.md",
    BASE/"Cartografia/E01_LIMITES_Y_VERTIENTES.md",
    BASE/"Cartografia/E01_CORREDORES.md",
    BASE/"Auditorias/E01_FUENTES_Y_DECISIONES.md",
    BASE/"Auditorias/E01_ACTA.md",
    BASE/"00_Control_del_proyecto/TRASPASO_E02.md"
]
for f in mandatory:
    assert f.is_file(), f"Fichero ausente: {f}"

mutations = [
    lambda x: x.update(runtimeEnabled=True),
    lambda x: x["cartography"].update(northBoundaryClosed=True),
    lambda x: x["cartography"].update(georeferenced=True),
    lambda x: x["cartography"].update(metricGeometryValidated=True),
    lambda x: x["cartography"].update(drainageBasinsValidated=True),
    lambda x: x["cartography"].update(watercoursesValidated=True),
    lambda x: x["cartography"].update(coordinateSystem="EPSG:4326"),
    lambda x: x["cartography"].update(scale="1:100000"),
    lambda x: x["cartography"].update(polygonGeometry=[[1,2],[3,4]]),
    lambda x: x["anchors"][3].update(jurisdictionOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(militaryOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(fiscalOwner="casa_edranor"),
    lambda x: x["anchors"][3].update(procedural=True),
    lambda x: x["anchors"][4].update(insideTerritorialScope=True),
    lambda x: x["anchors"][0].update(jurisdictionOwner="crown_aethros"),
    lambda x: x["anchors"][0].update(procedural=True),
    lambda x: x["reliefUnits"][0].update(elevation=780),
    lambda x: x["reliefUnits"][2].update(territorialExtent="50km2"),
    lambda x: x["reliefUnits"][6].update(evidence="CANON_REPO"),
    lambda x: x["qualitativeContacts"][0].update(travelRouteConfirmed=True),
    lambda x: x["qualitativeContacts"][1].update(physicalContactValidated=True),
    lambda x: x["corridorQuestions"][0].update(routeExists=True),
    lambda x: x["corridorQuestions"][3].update(passNamed=True),
    lambda x: x["corridorQuestions"][2].update(physicalTransitValidated=True),
    lambda x: x["administrativeOverlays"].update(rodasControlledBy="casa_edranor"),
    lambda x: x["administrativeOverlays"].update(berserkersControlledBy="casa_edranor"),
    lambda x: x["administrativeOverlays"].update(forestOwnerships="casa_edranor"),
    lambda x: x["administrativeOverlays"].update(noInternalCustoms=False),
    lambda x: x["qualitativeContacts"][2].update(to="invented_ridge"),
    lambda x: x["reliefUnits"].append(copy.deepcopy(x["reliefUnits"][0])),
]
for i, mutation in enumerate(mutations, 1):
    broken = copy.deepcopy(data)
    mutation(broken)
    try:
        checked(broken)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError(f"Mutacion {i} aceptada indebidamente")

print(f"EDRANOR E01 STATIC PASS | {len(UNITS)} unidades | {len(EXPECTED_CONTACTS)} contactos | {len(EXPECTED_CORRIDORS)} corredores no confirmados | {len(mutations)} negativas | {len(mandatory)} fuentes/ficheros | E00 consistente")

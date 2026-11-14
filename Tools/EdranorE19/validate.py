#!/usr/bin/env python3
"""E19: fail-closed, byte-level provenance and synthetic cartography contract tests.
Does not certify Edranor geography or create runtime content.
"""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
CONTRACT = T / "Datos operativos/edranor_e19_cartography_gate_v0.1.json"
E13 = T / "Datos operativos/edranor_e13_physical_design_v0.1.json"
E16 = T / "Datos operativos/edranor_e16_services_mobility_v0.1.json"
E18 = T / "Datos operativos/edranor_e18_maturity_audit_v0.1.json"
SOURCE_SHA = "223f1e49adfbc73be6a80c6ce36e7aab506450c2"
BLOB_SHA = "c46e017a5c9a0ab66f8f072dd37d7236e05b5e2d"
SHA256 = "582405ee3e38a6606a89342f4b28262d3bf88c087b05c23655a886130ffab91b"
UNITS = ["edr_e01_west_valkram_interface","edr_e01_karsath_central_west","edr_e01_lumina_bosque_alto","edr_e01_central_wine_context","edr_e01_dorth_azurios_west","edr_e01_north_cold_transition","edr_e01_far_north_unclosed"]
ANCHORS = ["dorth", "lumina", "karsath", "rodas", "hallheim"]
DOCS = ["README.md", "01_FUENTES_PROCEDENCIA.md", "02_PERIMETRO_Y_EXCEPCIONES.md",
        "03_CRS_CALIBRACION_Y_GODOT.md", "04_RELIEVE_AGUA_Y_VIAS.md",
        "05_CAPAS_Y_EXPORTACION.md", "06_ACTA_Y_TRASPASO.md", "07_RATIFICACION_AUTORAL_LIMITES_RODAS.md"]

class CartographyError(ValueError):
    pass

def need(test, reason):
    if not test:
        raise CartographyError(reason)

def no_duplicate_keys(pairs):
    obj = {}
    for k, v in pairs:
        need(k not in obj, "duplicate key " + k)
        obj[k] = v
    return obj

def read(path):
    with path.open(encoding="utf-8-sig") as fp:
        return json.load(fp, object_pairs_hook=no_duplicate_keys)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def validate(a, e13, e16, e18, check_bytes=True, check_docs=True):
    need((a.get("schemaVersion"),a.get("documentId"),a.get("version"),a.get("phase")) ==
         (1,"edranor_e19_cartography_gate","0.1","E19"), "identity")
    need(a.get("date") == "2026-11-14" and a.get("sourceMainSha") == SOURCE_SHA, "base evidence")
    need(a.get("phaseStatus") == "PREFLIGHT_COMPLETE_MATERIAL_GATES_OPEN" and
         a.get("authority") == "ASSISTANT_DELEGATED_DESIGN" and
         a.get("maturityLevel") == "B2", "false phase promotion")
    for k, value in {"phaseComplete":False,"metricGeometryValidated":False,
                     "runtimeEnabled":False,"worldStateEntitiesCreated":0,
                     "canonSuperiorModified":False,"syntheticTestsOnly":True}.items():
        need(type(a.get(k)) is type(value) and a[k] == value, "false status: "+k)
    m = a.get("sourceMap", {})
    need(m == {"repositoryPath":"Worldbuilding/Nimroel.jpg","gitBlobSha":BLOB_SHA,
               "sha256":SHA256,"byteLength":4752802,"widthPx":4096,"heightPx":2048,
               "sourceClass":"GENERAL_ILLUSTRATIVE_MAP","titleScaleBar":"400 MILLAS",
               "scaleApplicableToAuthorCrop":False,"byteIdenticalToUserUpload":True},
         "map source altered")
    if check_bytes:
        world = (ROOT / m["repositoryPath"]).read_bytes()
        need(len(world) == m["byteLength"] and hashlib.sha256(world).hexdigest() == SHA256
             and git_blob_sha(world) == BLOB_SHA, "world source bytes mismatch")
    c = a.get("authorCrop",{})
    need(c == {"label":"1000024893.jpg","documentaryReference":"Cartografia/E00_MAPA_Y_LIMITES.md",
               "originalBytesVerified":False,"redTerritoryLineDocumented":True,
               "rodasBlueXDocumented":True,"northernLimitVisible":False,
               "completeBoundarySourceAcquired":False}, "author crop fake promotion")
    s = a.get("spatialReference",{})
    need(s == {"proposedInternalCrsId":"EDRANOR_LOCAL_2D","effectiveCrs":None,
               "axesProposal":"X_EAST_Y_DOWN_GODOT","origin":None,
               "metersPerPixel":None,"controlPoints":[],"minimumNonCollinearControls":3,
               "forwardTransform":None,"inverseTransform":None,"residualRms":None,
               "independentHoldoutValidated":False,"calibrationAccepted":False}, "unproven CRS")
    need(a.get("jurisdiction") == {"perimeter":None,"northernBoundaryClosed":False,
         "polygons":[],"holes":[],"exceptionGeometries":[],"officialFeatureCount":0},
         "unproven jurisdiction")
    ap = a.get("protectedPlaces",[])
    need([x.get("id") for x in ap] == ANCHORS and
         all(x.get("coordinate") is None and x.get("polygon") is None and
             x.get("instantiated") is False for x in ap), "fabricated point")
    need([(x["id"],x["owner"],x["insideEdranorInDocumentaryCanon"],x["kind"]) for x in ap] ==
         [(x["id"],x["owner"],x["insideEdranor"],x["kind"]) for x in e13["protectedPlaces"]],
         "jurisdiction anchor conflict")
    need([u.get("id") for u in a.get("units",[])] == UNITS and
         [u.get("id") for u in a.get("units",[])] == [u.get("unitId") for u in e13["physicalUnits"]],
         "unit identity")
    need(all(u.get("order")==i+1 and u.get("geometry") is None and
             u.get("administrativePolygon") is False and
             u.get("assessment")==("NON_EVALUABLE" if i==6 else "STUDY_ONLY")
             for i,u in enumerate(a["units"])), "unit fictitious polygons")
    layers = a.get("layers",[])
    need([x.get("id") for x in layers] == [f"L{i:02d}" for i in range(12)] and
         all(x.get("spatialGeometryReady") is False and
             x.get("runtimeReady") is False for x in layers), "layer promotion")
    need(layers[0].get("sourceEvidenceStatus")=="WORLD_SOURCE_VERIFIED_CROP_PENDING" and
         all(x.get("sourceEvidenceStatus") == "GEOMETRY_NOT_VERIFIED" for x in layers[1:]), "layer source")
    need(a.get("relief") == {"dem":None,"verticalDatum":None,"tiles":[],
                            "measuredHeights":[],"sourceVerified":False}, "fake DEM")
    need(a.get("hydrology") == {"regionalReferences":["RIO_LURIEN","LAGO_ANTELA"],
          "localRiverSegments":[],"localLakes":[],"catchments":[],"flowGraph":[],
          "waterRightsVerified":False}, "fake hydrography")
    need(a.get("routes") == {"needsGraphSource":"E16","physicalNodes":[],
                             "physicalEdges":[],"rightsVerified":False}, "fake roads")
    need(e16["graph"]["physicalEdges"] == [] and
         e13["map"]["northBoundaryClosed"] is False and
         e13["map"]["metricGeometryValidated"] is False, "source regression")
    need([x.get("id") for x in a.get("materialGates",[])] ==
         ["EDD-01","EDD-02","EDD-03","EDD-07"] and
         all(x.get("status")=="OPEN" and bool(x.get("required"))
             for x in a["materialGates"]), "material gates")
    need([(x.get("id"),x.get("status")) for x in a.get("debtLedger",[])] ==
         [(x["id"],x["status"]) for x in e18["debts"]], "debt ledger promotion")
    need([x["id"] for x in e18["protectedAnchors"]] == ANCHORS, "prior protected anchors")
    need(a.get("safeOutputs") == {"provenanceLedger":True,"nonMetricSchematic":True,
          "metricPolygon":False,"geojsonExport":False,"physicalNavigation":False,
          "godotGameWorld":False}, "misleading exports")
    need(a.get("authorClarifications") == {
        "authority":"AUTHOR_EXPLICIT_2026_11_14",
        "source":"Conversation E19, annotated Nimroel (2).jpg screenshot and two express confirmations",
        "semanticTerritorialLimitsConfirmed":True,
        "north":{"noIntermediatePoliticalBorder":True,
                 "extendsToNorthernExtentOfNorgard":True,
                 "preciseGeometryKnown":False},
        "west":{"mountainRange":"VALKRAM","edranorSlope":"EASTERN",
                "dividingRidgeMapped":False},
        "east":{"mountainRange":"AZURIOS","edranorSlope":"WESTERN",
                "dividingRidgeMapped":False},
        "south":{"adjoiningHouse":"AETHROS",
                 "approximatelyFollowingRiverCorridor":True,
                 "riverIdentityCertified":False,"exactPolylineMapped":False},
        "hallheim":{"outsideEdranor":True,"capitalOf":"NORGARD",
                    "seatOfHouse":"AETHROS"},
        "rodas":{"territorialLocation":"CASA_EDRANOR",
                 "settlementClass":"VILLAGE",
                 "berserkerSummoningAuthority":"CASA_REGENTE_AETHROS",
                 "edranorMaySummonBerserkers":False,
                 "otherCivilFiscalPowersNewlyRatified":False,
                 "legacyRegimeFromE07E09Preserved":True},
        "northSemanticResolvedButEdd01GeometryOpen":True}, "author confirmation / competences")
    need(a.get("decisionIds") == [f"ED19-DEC-{i:02d}" for i in range(1,6)],
         "design decision register")
    need(e18["gates"]["E19"]["metricGeometryReady"] is False, "E18 material gate changed")
    if check_docs:
        need((T / "E19_INDICE.md").is_file(), "index missing")
        for name in DOCS:
            f=T/"E19"/name
            need(f.is_file() and f.stat().st_size > 250, "thin doc: "+name)
        svg=(T/"E19/atlas_lectura_no_metrica.svg").read_text(encoding="utf-8")
        need("<svg " in svg and "NO MÉTRICO" in svg and "SIN FRONTERAS" in svg and
             "RODAS" in svg and "HALLHEIM" in svg, "schematic legend missing")

def synthetic_geometry_tests():
    # These are algorithms/fixtures, NOT geography or scale for Edranor.
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    def controls_valid(points):
        return len(points)>=3 and abs(cross(*points[:3]))>1e-9
    need(controls_valid([(0,0),(2,0),(0,3)]), "valid 3-control fixture")
    need(not controls_valid([(0,0),(2,2),(4,4)]), "collinear accepted")
    need(not controls_valid([(1,1),(1,1),(2,3)]), "duplicated control accepted")
    def invert_affine(a,b,c,d,tx,ty,x,y):
        det = a*d-b*c
        need(abs(det)>1e-9,"singular affine")
        xx, yy = x-tx, y-ty
        return ((d*xx-b*yy)/det,(-c*xx+a*yy)/det)
    x,y=2.5,7.0
    X,Y=3*x+2*y+9, x+4*y-6
    rx,ry=invert_affine(3,2,1,4,9,-6,X,Y)
    need(abs(rx-x)<1e-10 and abs(ry-y)<1e-10, "roundtrip error")
    try:
        invert_affine(1,2,2,4,0,0,10,10)
    except CartographyError:
        pass
    else:
        raise CartographyError("singular transform accepted")
    def flow_is_dag(flow, heights):
        for origin, target in flow.items():
            if origin not in heights or target not in heights or heights[target]>=heights[origin]:
                return False
        for origin in flow:
            seen=set()
            cur=origin
            while cur in flow:
                if cur in seen:
                    return False
                seen.add(cur)
                cur=flow[cur]
        return True
    need(flow_is_dag({"a":"b","b":"c"},{"a":3,"b":2,"c":1}),"valid flow")
    need(not flow_is_dag({"a":"b","b":"a"},{"a":3,"b":2}),"cycle accepted")
    need(not flow_is_dag({"a":"b"},{"a":1,"b":2}),"uphill accepted")

def main():
    a,e13,e16,e18=read(CONTRACT),read(E13),read(E16),read(E18)
    validate(a,e13,e16,e18)
    synthetic_geometry_tests()
    mutations=[
      lambda x: x.__setitem__("phaseComplete",True),
      lambda x: x.__setitem__("runtimeEnabled",True),
      lambda x: x["sourceMap"].__setitem__("gitBlobSha","0"*40),
      lambda x: x["sourceMap"].__setitem__("scaleApplicableToAuthorCrop",True),
      lambda x: x["authorCrop"].__setitem__("completeBoundarySourceAcquired",True),
      lambda x: x["spatialReference"].__setitem__("metersPerPixel",5.0),
      lambda x: x["spatialReference"].__setitem__("controlPoints",[[0,0],[1,1],[2,2]]),
      lambda x: x["jurisdiction"].__setitem__("northernBoundaryClosed",True),
      lambda x: x["protectedPlaces"][3].__setitem__("owner","casa_edranor"),
      lambda x: x["protectedPlaces"][4].__setitem__("insideEdranorInDocumentaryCanon",True),
      lambda x: x["units"][6].__setitem__("assessment","STUDY_ONLY"),
      lambda x: x["layers"][9].__setitem__("spatialGeometryReady",True),
      lambda x: x["relief"].__setitem__("dem",[[3,2],[2,1]]),
      lambda x: x["hydrology"]["localRiverSegments"].append({"name":"fake"}),
      lambda x: x["routes"]["physicalEdges"].append({"from":"dorth","to":"lumina"}),
      lambda x: x["debtLedger"][0].__setitem__("status","RESOLVED"),
      lambda x: x["safeOutputs"].__setitem__("godotGameWorld",True),
      lambda x: x["authorClarifications"]["north"].__setitem__("preciseGeometryKnown",True),
      lambda x: x["authorClarifications"]["west"].__setitem__("edranorSlope","WESTERN"),
      lambda x: x["authorClarifications"]["east"].__setitem__("edranorSlope","EASTERN"),
      lambda x: x["authorClarifications"]["rodas"].__setitem__("territorialLocation","CASA_AETHROS"),
      lambda x: x["authorClarifications"]["rodas"].__setitem__("berserkerSummoningAuthority","CASA_EDRANOR"),
      lambda x: x["authorClarifications"]["hallheim"].__setitem__("outsideEdranor",False),
      lambda x: x["authorClarifications"]["south"].__setitem__("riverIdentityCertified",True)
    ]
    for i,change in enumerate(mutations,1):
        candidate=copy.deepcopy(a)
        change(candidate)
        try:
            validate(candidate,e13,e16,e18,check_bytes=False,check_docs=False)
        except CartographyError:
            pass
        else:
            raise CartographyError(f"adversarial mutation {i} accepted")
    print(f"E19 PREFLIGHT PASS: source bytes SHA-256/Git blob, 5 anchors, "
          f"7 qualitative units, 12 layers, 4 open gates; {len(mutations)} "
          "adversarial mutations rejected; synthetic fixtures PASS; NO GEOMETRY/NO RUNTIME")

if __name__ == "__main__":
    main()

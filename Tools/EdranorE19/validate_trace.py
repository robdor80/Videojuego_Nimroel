#!/usr/bin/env python3
"""Author red-trace raster tests. Pixel geometry only, NOT surveyed geography."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
TRACE = BASE / "E19/author_trace_raster_2048_v0.1.json"
GATE = BASE / "Datos operativos/edranor_e19_cartography_gate_v0.1.json"
SVG = BASE / "E19/author_trace_overlay_2048.svg"
ANNOTATED_SHA = "b5341bb608538aa9bc07c8afae56b9c7264af9f9a8c29fee82e14e63863c303f"
WEST = [1086,6]
EAST = [1571,9]

class TraceError(ValueError):
    pass

def check(v, why):
    if not v:
        raise TraceError(why)

def segment_crosses(a,b,c,d):
    def orient(p,q,r):
        return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    o1,o2,o3,o4=orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
    return (o1*o2<0 and o3*o4<0)

def validate(t,g,read_files=True):
    check((t.get("schemaVersion"),t.get("phase"),t.get("documentId"),t.get("version")) ==
          (1,"E19","edranor_author_drawn_raster_trace","0.1"),"identity")
    check(t.get("authority")=="AUTHOR_2026_11_14_ANNOTATED_IMAGE","authority")
    s=t.get("source",{})
    check(s.get("filename")=="nimroel_Edranor.jpg" and s.get("sha256")==ANNOTATED_SHA
          and [s.get("widthPx"),s.get("heightPx")]==[2048,1024] and
          s.get("availableInConversation") is True and
          s.get("originalBytesStoredInRepository") is False,"source provenance")
    r=t.get("registration",{})
    check(r.get("canonicalMap")=="Worldbuilding/Nimroel.jpg" and
          [r.get("canonicalImageWidth"),r.get("canonicalImageHeight")]==[4096,2048] and
          r.get("sourceToCanonicalMatrix")==[2,0,0,0,2,0] and
          r.get("canonicalToSourceMatrix")==[.5,0,0,0,.5,0] and
          r.get("rasterSameCompositionVerified") is True and
          r.get("godotCoordinatesRasterOnly") is True and
          r.get("worldMetersPerPixel") is None and r.get("geographicCrs") is None and
          r.get("illustrated400MilesBarIsNotMetricCertification") is True,
          "bad raster registration/metric claim")
    b=t.get("authorMarkedBoundary",{})
    pts=b.get("westToEastPoints",[])
    check(isinstance(pts,list) and len(pts)==21 and
          all(isinstance(p,list) and len(p)==2 and all(type(i)==int for i in p)
              and 0<=p[0]<2048 and 0<=p[1]<1024 for p in pts),"point format")
    check(pts[0]==WEST and pts[-1]==EAST and
          min(p[0] for p in pts)==1083 and max(p[0] for p in pts)==1575 and
          max(p[1] for p in pts)==283,"boundary extent")
    check(b.get("meaning")=="VISIBLE_APPROXIMATE_WEST_SOUTH_EAST_BOUNDARY" and
          b.get("referenceCoords")=="annotated_image_px" and
          b.get("pointCount")==len(pts) and b.get("connected") is True and
          b.get("closedNorth") is False and
          b.get("topViewportClipIsNotPoliticalBorder") is True and
          b.get("perimeterLegalPolygonCertified") is False and
          b.get("hatchingStrokesAreNotBoundaries") is True,"false border claim")
    check(all((pts[i][0]-pts[i-1][0])**2+(pts[i][1]-pts[i-1][1])**2<10000
              for i in range(1,len(pts))),"trace continuity")
    check(not any(segment_crosses(pts[i],pts[i+1],pts[j],pts[j+1])
                  for i in range(len(pts)-1) for j in range(i+2,len(pts)-1)),
          "crossing boundary")
    hatch=t.get("authorHatching",{})
    check(hatch.get("meaning")=="AREA_INDICATOR_NON_GEOMETRIC" and
          hatch.get("count")==5 and len(hatch.get("strokes",[]))==5 and
          all(len(h)==2 for h in hatch["strokes"]),"hatching boundary confusion")
    j=t.get("jurisdiction",{})
    check(j.get("dorth")==j.get("lumina")==j.get("karsath")=="EDRANOR" and
          j.get("hallheim")=={"geographicContext":"OUTSIDE_EDRANOR",
                              "capitalOf":"NORGARD","house":"AETHROS"},"anchors")
    check(j.get("rodas")=={"geographicContext":"EDRANOR",
       "exclusiveCivilFiscalJusticeSecurityMilitaryAuthority":"CROWN_AETHROS",
       "mayEdranorSummonBerserkers":False},"Rodas authority")
    rend=t.get("rendering",{})
    check(rend.get("visualMapReady") is True and
          rend.get("metricGameplayReady") is False and
          rend.get("northFillForbidden") is True and
          rend.get("demCreated") is False and
          rend.get("physicalRoutesCreated")==0 and
          rend.get("sitePlacementRequiresLocalProof") is True,"visual!=gameplay")
    ref=g.get("rasterTrace",{})
    check(ref=={"sourceName":"nimroel_Edranor.jpg","sourceSha256":ANNOTATED_SHA,
      "traceAsset":"E19/author_trace_raster_2048_v0.1.json",
      "overlayAsset":"E19/author_trace_overlay_2048.svg",
      "coordinateSystem":"RASTER_2048x1024",
      "godotVisualCoordinatesUsable":True,"nativeMapPixelScaleFactor":2,
      "boundaryVertices":21,"hatchedAreaIndicatorStrokes":5,
      "northPixelBorderIsNotPoliticalBorder":True,
      "administrativePolygonCertified":False,
      "physicalSurfaceMetricsCertified":False},"source contract")
    check(g.get("phaseComplete") is False and
          g.get("metricGeometryValidated") is False and
          g.get("runtimeEnabled") is False,"E19 unproven promotion")
    if read_files:
        svg=SVG.read_text(encoding="utf-8")
        check("viewBox=\"0 0 2048 1024\"" in svg and
              svg.count("<path ")==6 and
              "polygon" not in svg and
              "fill=\"none\"" in svg and
              "M1086,6" in svg and "L1571,9" in svg,
              "SVG misleading geometry")
        check((ROOT / "Worldbuilding/Nimroel.jpg").is_file(),"canonical map missing")
        doc=(BASE/"E19/08_CALCO_VECTORIAL_AUTOR.md").read_text(encoding="utf-8")
        check("21 puntos" in doc and "NO" in doc and "Rodas" in doc, "source doc")

def main():
    t=json.loads(TRACE.read_text(encoding="utf-8"))
    g=json.loads(GATE.read_text(encoding="utf-8"))
    validate(t,g)
    cases=[
      lambda z: z["authorMarkedBoundary"].__setitem__("closedNorth",True),
      lambda z: z["authorMarkedBoundary"].__setitem__("perimeterLegalPolygonCertified",True),
      lambda z: z["authorMarkedBoundary"]["westToEastPoints"].pop(),
      lambda z: z["source"].__setitem__("originalBytesStoredInRepository",True),
      lambda z: z["source"].__setitem__("sha256","0"*64),
      lambda z: z["registration"].__setitem__("worldMetersPerPixel",2500),
      lambda z: z["registration"].__setitem__("sourceToCanonicalMatrix",[1,0,0,0,1,0]),
      lambda z: z["authorHatching"].__setitem__("meaning","OFFICIAL_BORDER"),
      lambda z: z["jurisdiction"]["rodas"].__setitem__("mayEdranorSummonBerserkers",True),
      lambda z: z["jurisdiction"]["rodas"].__setitem__("exclusiveCivilFiscalJusticeSecurityMilitaryAuthority","CASA_EDRANOR"),
      lambda z: z["jurisdiction"]["hallheim"].__setitem__("geographicContext","EDRANOR"),
      lambda z: z["rendering"].__setitem__("northFillForbidden",False),
      lambda z: z["rendering"].__setitem__("metricGameplayReady",True),
    ]
    for i,fn in enumerate(cases,1):
        corrupt=copy.deepcopy(t)
        fn(corrupt)
        try:
            validate(corrupt,g,read_files=False)
        except TraceError:
            pass
        else:
            raise TraceError(f"adversarial case {i} accepted")
    print(f"E19 author raster PASS: 21 boundary control points, 5 hatch strokes, "
          f"{len(cases)} adversarial mutations rejected, pixel-to-canonical x2; NO METRIC POLYGON")

if __name__=="__main__":
    main()

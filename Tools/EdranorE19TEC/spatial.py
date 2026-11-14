#!/usr/bin/env python3
"""E19-TEC: guard y exportador de geometria por sector, sin crear canon."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor/E19-TEC"
KINDS = {"boundary_divide", "river", "waterbody", "route_node",
         "road", "settlement", "forest", "parcel"}
GEOMS = {
    "boundary_divide": "LineString", "river": "LineString",
    "waterbody": None, "route_node": "Point", "road": "LineString",
    "settlement": "Point", "forest": "Polygon", "parcel": "Polygon",
}
CANON = {
    "northJoined": False, "politicalNorthClosed": False,
    "mf08Evaluable": False, "valkramWest": "casa_darovan",
    "valkramEast": "casa_edranor", "azuriosWest": "casa_edranor",
    "azuriosEast": "casa_galdren", "southLurienWholeBoundary": False,
    "rodasKind": "ALDEA", "rodasJurisdiction": "crown_aethros",
    "hallheimInEdranor": False, "bosqueAltoPermitRequired": True,
    "bosqueRealOwner": "crown_aethros", "karsathUrbanPort": False,
    "caleranAtDorth": False,
}

class SpatialError(ValueError):
    """No debe aprobarse ni exportarse material sin evidencia."""

def require(ok: bool, reason: str) -> None:
    if not ok:
        raise SpatialError(reason)

def unique_pairs(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON key duplicada: " + key)
        result[key] = value
    return result

def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_pairs)
    require(type(value) is dict, "JSON raiz debe ser objeto")
    return value

def nonempty(value: Any) -> bool:
    return type(value) is str and bool(value.strip()) and len(value) <= 200

def point(value: Any) -> tuple[float, float]:
    require(type(value) is list and len(value) == 2, "Punto 2D")
    require(all(type(x) in (int, float) and math.isfinite(x) and abs(x) <= 1e9
                for x in value), "Coordenada no numerica/finita/rango invalido")
    return float(value[0]), float(value[1])

def cross(a, b, c) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def on_segment(a, b, p, eps=1e-7) -> bool:
    return abs(cross(a, b, p)) <= eps and (
        min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps and
        min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps)

def intersects(a, b, c, d) -> bool:
    x, y, z, w = cross(a, b, c), cross(a, b, d), cross(c, d, a), cross(c, d, b)
    if (x > 0 > y or y > 0 > x) and (z > 0 > w or w > 0 > z):
        return True
    return ((abs(x) <= 1e-9 and on_segment(a, b, c)) or
            (abs(y) <= 1e-9 and on_segment(a, b, d)) or
            (abs(z) <= 1e-9 and on_segment(c, d, a)) or
            (abs(w) <= 1e-9 and on_segment(c, d, b)))

def line(coords: Any, closed: bool) -> list[tuple[float, float]]:
    require(type(coords) is list and len(coords) >= (4 if closed else 2),
            "Numero insuficiente de vertices")
    pts = [point(p) for p in coords]
    require((pts[0] == pts[-1]) is closed, "Cierre geometrico incorrecto")
    require(all(pts[i] != pts[i + 1] for i in range(len(pts)-1)),
            "Segmento de longitud cero")
    count = len(pts)-1
    for i in range(count):
        for j in range(i+1, count):
            if j == i+1 or (closed and i == 0 and j == count-1):
                continue
            require(not intersects(pts[i], pts[i+1], pts[j], pts[j+1]),
                    "Autointerseccion geometrica")
    if closed:
        area2 = sum(pts[i][0]*pts[i+1][1]-pts[i+1][0]*pts[i][1]
                    for i in range(count))
        require(abs(area2) > 1e-7, "Poligono de area nula")
    return pts

def geometry(feature: dict) -> list[tuple[float, float]]:
    kind = feature["kind"]
    g = feature.get("geometry")
    require(type(g) is dict, "Geometria ausente")
    typ = g.get("type")
    required_type = GEOMS[kind]
    require(typ == required_type if required_type else typ in ("Point", "Polygon"),
            "Geometria incompatible con tipo de entidad")
    if typ == "Point":
        return [point(g.get("coordinates"))]
    if typ == "LineString":
        return line(g.get("coordinates"), False)
    return line(g.get("coordinates"), True)

def valid_manifest(manifest: dict) -> None:
    require(manifest.get("schemaVersion") == 1 and
            manifest.get("documentId") == "edranor_e19_tec_technical_manifest",
            "Identidad de manifiesto")
    require(manifest.get("status") ==
            "TECHNICAL_PIPELINE_IN_PROGRESS_NO_B3_EVIDENCE", "Falsa promocion")
    require(manifest.get("invariants") == CANON, "Invariantes de canon")
    require(manifest.get("spatialReference") is None and
            manifest.get("approvedGeometryAssets") == [], "Geometria inventada")
    for field in ("actualPhysicalRoadEdges", "verifiedSettlements",
                  "verifiedProviders", "actualWorldStateEntities"):
        require(type(manifest.get(field)) is int and manifest[field] == 0,
                "Falso inventario: " + field)
    require(manifest.get("rejectedSourcePR84Used") is False, "PR84 descartada")
    require(manifest.get("materialization") == {
        "scope": "NONE_YET", "exportable": False, "layerCount": 0, "sectorIds": []},
        "Sector falsamente materializado")
    require(manifest.get("layerTypes") == sorted(KINDS) or
            set(manifest.get("layerTypes", [])) == KINDS, "Capas incompletas")
    gates = manifest.get("gates")
    require(type(gates) is list and len(gates) == 8, "Puertas TEC")
    require([g.get("id") for g in gates] ==
            ["TEC-%02d" % i for i in range(1, 9)], "Ids de puertas")
    require([g.get("passed") for g in gates] == [True] + [False]*7,
            "Puertas B3/B4 no acreditadas")
    require(manifest.get("source", {}).get("headSha") ==
            "fd31360a8b3a6d94da3b020bce38bb23481e7e79", "Padre R6")

def feature_evidence(f: dict, mode: str, registry: dict) -> None:
    source = f.get("sourceId")
    if mode == "synthetic":
        require(source == "TEST_ONLY" and f.get("status") == "SYNTHETIC_TEST",
                "Ejemplo no puede afirmar fuente real")
        return
    require(nonempty(source) and source != "TEST_ONLY", "Falta fuente real")
    require(f.get("status") == "APPROVED_B3" and nonempty(f.get("approvalId")),
            "Elemento sin aprobacion B3")
    matches = [e for e in registry["evidence"] if e.get("id") == source and
               e.get("status") == "APPROVED_B3" and nonempty(e.get("reviewer"))]
    require(len(matches) == 1, "Fuente no registrada/autorizada: " + source)

def validate_packet(packet: dict, registry: dict | None = None) -> dict:
    require(packet.get("schemaVersion") == 1, "Version de paquete")
    require(nonempty(packet.get("sectorId")), "Sector sin ID estable")
    mode = packet.get("mode")
    require(mode in ("synthetic", "production"), "Modo obligatorio")
    production = mode == "production"
    auth = packet.get("authorization")
    require(type(auth) is dict, "Autorizacion ausente")
    ref = packet.get("spatialReference")
    require(type(ref) is dict and ref.get("kind") == "LOCAL_METRIC" and
            ref.get("units") == "metres" and nonempty(ref.get("sourceId")),
            "Sistema espacial no acreditado")
    error = ref.get("uncertaintyMetres")
    require(type(error) in (int, float) and math.isfinite(error) and error >= 0,
            "Error espacial inexistente")
    # Transformacion afín local reversible: sin escala/origen no se puede
    # contrastar un plano de fuente con coordenadas metricas.
    transform = ref.get("sourceToLocal")
    require(type(transform) is dict and set(transform) == {
            "scaleMetresPerSourceUnit", "rotationRadians",
            "sourceOrigin", "localOrigin"}, "Transformacion local ausente")
    scale, rotation = (transform["scaleMetresPerSourceUnit"],
                       transform["rotationRadians"])
    require(type(scale) in (int, float) and math.isfinite(scale) and
            1e-12 < scale <= 1e9, "Transformacion no invertible")
    require(type(rotation) in (int, float) and math.isfinite(rotation),
            "Rotacion invalida")
    point(transform["sourceOrigin"])
    point(transform["localOrigin"])
    registry = registry or {"schemaVersion": 1, "approvedSectors": [], "evidence": []}
    require(registry.get("schemaVersion") == 1 and
            type(registry.get("approvedSectors")) is list and
            type(registry.get("evidence")) is list, "Registro de evidencias invalido")
    if production:
        require(auth.get("kind") == "AUTHOR_APPROVED_SECTOR" and
                auth.get("approved") is True and nonempty(auth.get("approvalId")),
                "Falta autorizacion sectorial")
        require(nonempty(auth.get("sourceId")) and
                auth["sourceId"] != "TEST_ONLY", "Autoridad sintetica")
        require(any(s.get("id") == packet["sectorId"] and
                    s.get("approvalId") == auth["approvalId"]
                    for s in registry["approvedSectors"]), "Sector no inscrito")
        for src in (ref["sourceId"], auth["sourceId"]):
            require(any(e.get("id") == src and e.get("status") == "APPROVED_B3" and
                        nonempty(e.get("reviewer")) for e in registry["evidence"]),
                    "Autoridad/escala sin registro")
    else:
        require(auth == {"kind": "SYNTHETIC_TEST", "approved": False,
                         "sourceId": "TEST_ONLY", "approvalId": None},
                "Un test no concede autoridad")
        require(ref["sourceId"] == "TEST_ONLY", "Referencia sintetica exigida")
    feats = packet.get("features")
    require(type(feats) is list and (len(feats) > 0 or not production),
            "Sector productivo vacio o caracteristicas invalidas")
    ids, points = set(), {}
    for f in feats:
        require(type(f) is dict and nonempty(f.get("id")) and
                f["id"] not in ids and f.get("kind") in KINDS, "ID/tipo duplicado o invalido")
        ids.add(f["id"])
        feature_evidence(f, mode, registry)
        points[f["id"]] = geometry(f)
        if f["kind"] == "boundary_divide":
            require(f.get("mountainRange") in ("Valkram", "Azurios") and
                    f.get("politicalNorthClosure") is False, "Frontera irregular")
            west, east = (("casa_darovan", "casa_edranor")
                          if f["mountainRange"] == "Valkram"
                          else ("casa_edranor", "casa_galdren"))
            require(f.get("westOwner") == west and f.get("eastOwner") == east,
                    "Laderas inversas")
        if f["kind"] == "settlement":
            name = str(f.get("name", "")).lower()
            require(name != "hallheim", "Hallheim externo")
            if name == "rodas":
                require(f.get("kindOfSettlement") == "ALDEA" and
                        f.get("jurisdiction") == "crown_aethros", "Rodas regia")
            if name == "karsath":
                require(f.get("urbanPort") is False, "Puerto de Karsath sin fuente")
            if name == "dorth":
                require(f.get("caleranAtTown") is False, "Caleran en Dorth")
        if f["kind"] == "forest":
            if f.get("name") == "Bosque Real":
                require(f.get("owner") == "crown_aethros", "Bosque Real regio")
            if f.get("name") == "Bosque Alto":
                require(f.get("harvestPermitRequired") is True,
                        "Bosque Alto requiere permiso")
        if f["kind"] == "road":
            access = f.get("access")
            require(type(access) is dict and all(access.get(k) is True for k in
                    ("surveyed", "legal", "maintained", "waterCrossingsSurveyed")),
                    "Camino Gp sin inspeccion/permisos")
            require(type(access.get("capacity")) in (int, float) and
                    math.isfinite(access["capacity"]) and access["capacity"] > 0,
                    "Capacidad de paso no probada")
        if f["kind"] == "river":
            require(nonempty(f.get("receiverId")) and
                    f["receiverId"] != f["id"], "Rio sin receptor valido")
    index = {f["id"]: f for f in feats}
    for f in feats:
        if f["kind"] == "road":
            a, b = f.get("fromNodeId"), f.get("toNodeId")
            require(a in index and b in index and a != b and
                    index[a]["kind"] == index[b]["kind"] == "route_node",
                    "Gp no enlazado a nodos reales")
            require(points[f["id"]][0] == points[a][0] and
                    points[f["id"]][-1] == points[b][0], "Camino y nodos sin continuidad")
        if f["kind"] == "river":
            receiver = f["receiverId"]
            require(receiver in index and index[receiver]["kind"] in
                    ("river", "waterbody"), "Receptor de agua inexistente")
            end = points[f["id"]][-1]
            receiving_pts = points[receiver]
            if len(receiving_pts) == 1:
                require(end == receiving_pts[0], "Desembocadura no conectada")
            else:
                require(any(on_segment(receiving_pts[i], receiving_pts[i+1], end)
                            for i in range(len(receiving_pts)-1)),
                        "Receptor sin conexion topologica")
    for f in feats:
        if f["kind"] == "river":
            seen, current = set(), f
            while current["kind"] == "river":
                require(current["id"] not in seen, "Ciclo hidrologico")
                seen.add(current["id"])
                current = index[current["receiverId"]]
    return {"sectorId": packet["sectorId"], "mode": mode,
            "features": len(feats), "productionEligible": production}

def export_sector(packet: dict, registry: dict) -> dict:
    result = validate_packet(packet, registry)
    require(result["productionEligible"], "Prohibido exportar un test como territorio")
    ordered = sorted(packet["features"], key=lambda f: f["id"])
    payload = {
        "schemaVersion": 1, "profile": "NIMROEL_GODOT_2D_SPATIAL",
        "maturity": "SECTOR_B3_GEOMETRY_ONLY_NOT_RUNTIME_B4",
        "sectorId": packet["sectorId"],
        "spatialReference": packet["spatialReference"],
        "authorization": packet["authorization"],
        "features": ordered,
    }
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    payload["sha256"] = hashlib.sha256(data).hexdigest()
    return payload

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--registry", type=Path,
                        default=BASE / "approval_registry_v0.1.json")
    args = parser.parse_args()
    valid_manifest(read_json(BASE / "technical_manifest_v0.1.json"))
    require(args.input is not None and args.output is not None,
            "Manifiesto OK. Para exportar son obligatorios --input y --output")
    packet, registry = read_json(args.input), read_json(args.registry)
    result = export_sector(packet, registry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False,
                                     sort_keys=True, indent=2) + "\n",
                           encoding="utf-8")
    print("E19-TEC: export sector autorizado", result["sectorId"], result["sha256"])

if __name__ == "__main__":
    try:
        main()
    except (SpatialError, OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit("E19-TEC BLOQUEADO: " + str(exc))

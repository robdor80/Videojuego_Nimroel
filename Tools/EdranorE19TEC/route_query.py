#!/usr/bin/env python3
"""E19-TEC: consulta de caminos Gp verificados, nunca de preguntas Gq/CT.

Solo lee geografia fija y un estado/permiso recibido del Core. NO muta mundo,
no concede permisos, no despacha agentes ni calcula tiempos imaginarios.
"""
from __future__ import annotations

import heapq
import math
from typing import Any

from spatial import SpatialError, require, validate_packet

MODES = {"walk", "cart"}
JURISDICTIONS = {"casa_edranor", "crown_aethros"}


def route_length(geometry: dict) -> float:
    pts = geometry["coordinates"]
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))


def query_route(packet: dict, registry: dict, *, start_id: str, goal_id: str,
                mode: str, grants: set[str], blocked_roads: set[str]) -> dict:
    """Una ruta solo existe en un paquete espacial inscrito y aprobado estructuralmente."""
    result = validate_packet(packet, registry)
    require(result["productionEligible"], "Grafo ficticio no apto para consultas Gp")
    require(type(mode) is str and mode in MODES, "Modo de desplazamiento desconocido")
    require(type(grants) is set and all(type(x) is str for x in grants),
            "Permisos deben venir de fuente confiable")
    require(type(blocked_roads) is set and all(type(x) is str for x in blocked_roads),
            "Cierres no son datos de geometria")
    index = {f["id"]: f for f in packet["features"]}
    require(start_id in index and goal_id in index and
            index[start_id]["kind"] == "route_node" and
            index[goal_id]["kind"] == "route_node", "Origen/destino sin nodos Gp")
    # Registros de TEST_ONLY sirven para probar algoritmos. No son autoridad.
    lab = any(e.get("reviewer") == "TEST_ONLY" for e in registry["evidence"])
    status = "LAB_PATH_ONLY_NOT_GAMEPLAY" if lab else "VERIFIED_STRUCTURE_NOT_RUNTIME"
    if start_id == goal_id:
        return {"status": status, "pathIds": [], "lengthMetres": 0.0,
                "travelTime": None, "committed": False}
    graph: dict[str, list[tuple[float, str, str]]] = {
        f["id"]: [] for f in packet["features"] if f["kind"] == "route_node"}
    for road in packet["features"]:
        if road["kind"] != "road" or road["id"] in blocked_roads:
            continue
        access: dict = road["access"]
        permitted = access.get("modes")
        require(type(permitted) is list and permitted and
                all(v in MODES for v in permitted) and
                len(permitted) == len(set(permitted)), "Modos de camino no inspeccionados")
        jurisdiction = road.get("jurisdiction")
        require(jurisdiction in JURISDICTIONS, "Jurisdiccion de camino UNKNOWN")
        forest = road.get("forestContext")
        require(forest in ("NONE", "BOSQUE_ALTO", "BOSQUE_REAL"),
                "Proteccion forestal UNKNOWN")
        require(type(road.get("bidirectional")) is bool, "Sentido Gp sin confirmar")
        if mode not in permitted:
            continue
        if jurisdiction == "crown_aethros" and "CROWN_ACCESS" not in grants:
            continue
        if forest == "BOSQUE_ALTO" and "BOSQUE_ALTO_ACCESS" not in grants:
            continue
        if forest == "BOSQUE_REAL" and "ROYAL_FOREST_ACCESS" not in grants:
            continue
        a, b = road["fromNodeId"], road["toNodeId"]
        length = route_length(road["geometry"])
        require(math.isfinite(length) and length > 0, "Longitud no autorizada")
        graph[a].append((length, road["id"], b))
        if road["bidirectional"]:
            graph[b].append((length, road["id"], a))
    # Dijkstra con desempate estable por IDs de segmentos.
    frontier = [(0.0, (), start_id)]
    settled = set()
    while frontier:
        cost, path, node = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node)
        if node == goal_id:
            return {"status": status, "pathIds": list(path),
                    "lengthMetres": round(cost, 6),
                    "travelTime": None, "committed": False}
        for length, edge, neighbor in graph[node]:
            if neighbor not in settled:
                heapq.heappush(frontier, (cost + length, path + (edge,), neighbor))
    return {"status": "NO_VERIFIED_ROUTE", "pathIds": [],
            "lengthMetres": None, "travelTime": None, "committed": False}

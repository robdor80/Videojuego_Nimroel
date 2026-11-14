#!/usr/bin/env python3
"""E19-TEC: nucleo hidrologico determinista de laboratorio, NO rios reales.

La geometria real, el receptor, la ley y los derechos siguen requiriendo B3.
Esta implementacion SOLO acepta terrenos sintéticos de prueba; ningún cauce
resultante tiene permiso para integrarse en el ContentPack o el World State.
"""
from __future__ import annotations

import hashlib
import json
import math
from typing import Any

from spatial import SpatialError, require

OFFSETS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)
           if dr != 0 or dc != 0]


def cell_id(sector: str, row: int, column: int) -> str:
    return f"TEST:{sector}:{row:02d}:{column:02d}"


def _coordinate(value: Any, rows: int, cols: int) -> tuple[int, int]:
    require(type(value) is list and len(value) == 2 and
            all(type(v) is int for v in value), "Coordenada de celda inválida")
    r, c = value
    require(0 <= r < rows and 0 <= c < cols, "Celda fuera de malla")
    return r, c


def _integer(value: Any, label: str) -> int:
    require(type(value) is int and 0 <= value <= 10**6,
            "Cantidad entera no negativa requerida: " + label)
    return value


def _tiebreak(seed: str, sector: str, row: int, col: int, end: tuple) -> bytes:
    source = f"{seed}|{sector}|{row}|{col}|{end[0]}|{end[1]}".encode("utf-8")
    return hashlib.sha256(source).digest()


def solve_lab(model: dict) -> dict:
    require(type(model) is dict and model.get("schemaVersion") == 1,
            "Esquema de laboratorio inválido")
    require(model.get("mode") == "SYNTHETIC_TEST" and
            model.get("sourceId") == "TEST_ONLY", "No exportar mundo real por laboratorio")
    sector, seed, version = (model.get("sectorId"), model.get("seed"),
                              model.get("algorithmVersion"))
    for item, desc in ((sector, "sectorId"), (seed, "seed")):
        require(type(item) is str and 1 <= len(item) <= 64 and
                item.isascii() and all(x.isalnum() or x in "_-" for x in item),
                "Identidad inválida: " + desc)
    require(version == "D8-CAUSAL-LAB-1", "Versión de algoritmo no fijada")
    require(model.get("contextId") in {f"MF-{i:02d}" for i in range(1,8)},
            "MF-08/U7 no evaluable")
    grid = model.get("cells")
    require(type(grid) is list and 2 <= len(grid) <= 64 and
            all(type(row) is list and row for row in grid), "Malla no rectangular")
    nr, nc = len(grid), len(grid[0])
    require(2 <= nc <= 64 and nr * nc <= 4096 and
            all(len(row) == nc for row in grid), "Dimensiones de malla inválidas")
    fields = ("elevation", "rain", "snowmelt", "infiltration", "evapotranspiration")
    height, local_runoff, absorbed = {}, {}, {}
    total_input, total_absorbed = 0, 0
    for r in range(nr):
        for c in range(nc):
            entry = grid[r][c]
            require(type(entry) is dict and set(entry) == set(fields),
                    "Celda sin capas físicas completas")
            h = entry["elevation"]
            require(type(h) in (float, int) and math.isfinite(h) and
                    -100000 <= h <= 100000, "Altura sintética inválida")
            height[r, c] = h
            for f in fields[1:]:
                _integer(entry[f], f)
            supply = entry["rain"] + entry["snowmelt"]
            losses = entry["infiltration"] + entry["evapotranspiration"]
            require(losses <= supply, "Balance negativo en la celda")
            local_runoff[r, c] = supply - losses
            absorbed[r, c] = losses
            total_input += supply
            total_absorbed += losses
    outlets, sinks = set(), {}
    raw_outlets, raw_sinks = model.get("boundaryOutlets"), model.get("closedSinks")
    require(type(raw_outlets) is list and type(raw_sinks) is list,
            "Falta declarar receptor o sumidero")
    for item in raw_outlets:
        position = _coordinate(item, nr, nc)
        require(position[0] in (0, nr - 1) or position[1] in (0, nc - 1),
                "Salida abierta solo en borde de sector")
        require(position not in outlets, "Repetición de salida")
        outlets.add(position)
    for entry in raw_sinks:
        require(type(entry) is dict and set(entry) == {"cell", "capacityUnits",
                "balanceEvidence"}, "Sumidero sin balance trazable")
        position = _coordinate(entry["cell"], nr, nc)
        require(position not in sinks and position not in outlets,
                "Sumidero repetido o solapado")
        require(entry["balanceEvidence"] == "TEST_ONLY", "Sumidero sin prueba")
        sinks[position] = _integer(entry["capacityUnits"], "capacityUnits")
    require(bool(outlets or sinks), "El sector carece de receptores")
    require(type(model.get("candidateThresholdUnits")) is int and
            1 <= model["candidateThresholdUnits"] <= 10**6,
            "Umbral de prueba debe ser explícito")
    downstream: dict[tuple[int,int], tuple[int,int] | None] = {}
    for r in range(nr):
        for c in range(nc):
            current = (r, c)
            # El receptor declarado es terminal, nunca fuente de camino sobreescrita.
            if current in outlets or current in sinks:
                downstream[current] = None
                continue
            eligible = []
            for dr, dc in OFFSETS:
                rr, cc = r + dr, c + dc
                if not (0 <= rr < nr and 0 <= cc < nc):
                    continue
                drop = height[current] - height[rr, cc]
                if drop <= 0:
                    continue
                # Gradiente (caída / distancia). D8 diagonal sqrt(2).
                # Se elige gradiente máximo; hash estable solo desempata.
                gradient = drop / math.sqrt(dr*dr + dc*dc)
                eligible.append((gradient, (rr, cc)))
            require(bool(eligible), "Depresión/llano sin receptor aprobado: "
                    + str(current))
            best_gradient = max(x[0] for x in eligible)
            tied = [e for g, e in eligible if
                    math.isclose(g, best_gradient, rel_tol=1e-12, abs_tol=1e-12)]
            chosen = min(tied, key=lambda pos: _tiebreak(seed, sector, r, c, pos))
            downstream[current] = chosen
    # Orden descendente. Al fluir solo a cota menor, no hay ciclos.
    order = sorted(height, key=lambda x: (-height[x], x[0], x[1]))
    acc = dict(local_runoff)
    for current in order:
        dest = downstream[current]
        if dest is not None:
            require(height[dest] < height[current], "Flujo contra pendiente")
            acc[dest] += acc[current]
    terminals = sorted(x for x in height if downstream[x] is None)
    terminal_total = sum(acc[x] for x in terminals)
    require(total_input == total_absorbed + terminal_total,
            "La masa de agua no se conserva")
    for k, cap in sinks.items():
        require(acc[k] <= cap, "Sumidero sin capacidad temporal comprobada")
    result_cells = []
    for r in range(nr):
        for c in range(nc):
            key = (r, c)
            dest = downstream[key]
            result_cells.append({
                "id": cell_id(sector, r, c),
                "receiverId": cell_id(sector, *dest) if dest is not None else None,
                "heightSynthetic": height[key],
                "runoffUnits": local_runoff[key],
                "accumulatedUnits": acc[key],
                "candidateChannel": acc[key] >= model["candidateThresholdUnits"],
                "status": "POTENTIAL_ONLY_NO_RIVER",
                "coordinates": None,
                "worldStateId": None,
            })
    payload = {
        "schemaVersion": 1, "profile": "EDRANOR_TEST_DRAINAGE_ONLY",
        "algorithmVersion": version, "status": "SYNTHETIC_NOT_CANON",
        "sectorId": sector, "contextId": model["contextId"],
        "seed": seed, "sourceId": "TEST_ONLY", "sourceMode": "SYNTHETIC_TEST",
        "terminalCount": len(terminals),
        "totalRainAndMelt": total_input,
        "totalInfiltrationAndEvapotranspiration": total_absorbed,
        "totalDeliveredOrStored": terminal_total,
        "physicalRiversCreated": 0, "approvedWaterRightsCreated": 0,
        "gameplayRoutesCreated": 0, "worldStateCreated": False,
        "cells": result_cells,
    }
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"), allow_nan=False).encode("utf-8")
    payload["sha256"] = hashlib.sha256(raw).hexdigest()
    return payload

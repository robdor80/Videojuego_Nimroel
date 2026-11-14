#!/usr/bin/env python3
"""Regresiones del calculo hidrologico causal de laboratorio E19-TEC."""
from __future__ import annotations

import copy
import json
import unittest

from drainage_lab import solve_lab
from spatial import SpatialError


def cell(height: int, rain=1, snowmelt=0, infiltration=0, evap=0):
    return {"elevation": height, "rain": rain, "snowmelt": snowmelt,
            "infiltration": infiltration, "evapotranspiration": evap}


def slope():
    return {
        "schemaVersion": 1,
        "mode": "SYNTHETIC_TEST", "sourceId": "TEST_ONLY",
        "sectorId": "slope_lab", "seed": "reproducible",
        "algorithmVersion": "D8-CAUSAL-LAB-1", "contextId": "MF-02",
        "candidateThresholdUnits": 3,
        "boundaryOutlets": [[2, 2]], "closedSinks": [],
        "cells": [[cell(5-r-c) for c in range(3)] for r in range(3)],
    }


class DrainageTests(unittest.TestCase):
    def reject(self, mutate, original=None):
        payload = copy.deepcopy(original if original is not None else slope())
        mutate(payload)
        with self.assertRaises(SpatialError):
            solve_lab(payload)

    def test_all_reaches_approved_terminal(self):
        got = solve_lab(slope())
        self.assertEqual(got["terminalCount"], 1)
        self.assertEqual(got["totalRainAndMelt"], 9)
        self.assertEqual(got["totalDeliveredOrStored"], 9)
        self.assertEqual(got["totalInfiltrationAndEvapotranspiration"], 0)
        self.assertEqual(got["physicalRiversCreated"], 0)
        self.assertFalse(got["worldStateCreated"])
        self.assertEqual(len(got["cells"]), 9)
        self.assertIsNone(got["cells"][-1]["receiverId"])
        self.assertEqual(got["cells"][-1]["accumulatedUnits"], 9)
        self.assertTrue(got["cells"][-1]["candidateChannel"])
        self.assertEqual({c["status"] for c in got["cells"]},
                         {"POTENTIAL_ONLY_NO_RIVER"})
        self.assertTrue(all(c["coordinates"] is None for c in got["cells"]))

    def test_supply_losses_conserved(self):
        sample = slope()
        sample["cells"][0][0] = cell(5, rain=5, snowmelt=3, infiltration=4, evap=2)
        got = solve_lab(sample)
        self.assertEqual(got["totalRainAndMelt"], 16)
        self.assertEqual(got["totalInfiltrationAndEvapotranspiration"], 6)
        self.assertEqual(got["totalDeliveredOrStored"], 10)

    def test_deterministic_digest(self):
        one = solve_lab(slope())
        two = solve_lab(slope())
        self.assertEqual(one, two)
        self.assertEqual(len(one["sha256"]), 64)
        self.assertEqual(one["cells"][0]["id"], "TEST:slope_lab:00:00")

    def test_no_canon_or_world_state(self):
        self.reject(lambda x: x.update(mode="PRODUCTION"))
        self.reject(lambda x: x.update(sourceId="CANON"))
        self.reject(lambda x: x.update(contextId="MF-08"))
        self.reject(lambda x: x.update(contextId="U7"))

    def test_no_invalid_seed_or_version(self):
        self.reject(lambda x: x.update(seed=""))
        self.reject(lambda x: x.update(sectorId="../../escape"))
        self.reject(lambda x: x.update(algorithmVersion="D8-2"))

    def test_outlet_must_be_edge(self):
        self.reject(lambda x: x.update(boundaryOutlets=[[1, 1]]))
        self.reject(lambda x: x.update(boundaryOutlets=[[2, 2], [2, 2]]))

    def test_no_unjustified_flat_terrain(self):
        self.reject(lambda x: x.update(cells=[
            [cell(1), cell(1)], [cell(1), cell(1)]],
            boundaryOutlets=[[1, 1]]))

    def test_no_invented_sink(self):
        self.reject(lambda x: x.update(boundaryOutlets=[]))
        self.reject(lambda x: x.update(closedSinks=[
            {"cell": [1, 1], "capacityUnits": 100, "balanceEvidence": "FAKE"}]))

    def test_no_uphill_pond_from_label(self):
        self.reject(lambda x: x.update(closedSinks=[{
            "cell": [0, 0], "capacityUnits": 100, "balanceEvidence": "TEST_ONLY"
        }]))

    def test_balance_rejects_negative_capacity(self):
        self.reject(lambda x: x["cells"][1][1].update(infiltration=2))
        self.reject(lambda x: x["cells"][1][1].update(rain=-1))
        self.reject(lambda x: x["cells"][1][1].update(snowmelt=True))

    def test_real_closed_basin_requires_storage(self):
        s = slope()
        s["cells"] = [[cell(4), cell(3), cell(4)],
                      [cell(3), cell(1), cell(3)],
                      [cell(4), cell(3), cell(4)]]
        s["boundaryOutlets"] = []
        s["closedSinks"] = [{"cell": [1, 1], "capacityUnits": 9,
                            "balanceEvidence": "TEST_ONLY"}]
        got = solve_lab(s)
        self.assertEqual(got["totalDeliveredOrStored"], 9)
        self.assertEqual(got["terminalCount"], 1)
        self.reject(lambda x: x["closedSinks"][0].update(capacityUnits=8), s)

    def test_multiple_allowed_outlets(self):
        s = slope()
        s["cells"] = [[cell(9), cell(8), cell(1)],
                      [cell(8), cell(7), cell(8)],
                      [cell(1), cell(8), cell(9)]]
        s["boundaryOutlets"] = [[0, 2], [2, 0]]
        got = solve_lab(s)
        self.assertEqual(got["terminalCount"], 2)
        self.assertEqual(got["totalDeliveredOrStored"], 9)

    def test_tie_break_only_between_downhill_choices(self):
        s = slope()
        s["cells"] = [[cell(3), cell(2)],
                      [cell(2), cell(3)]]
        s["boundaryOutlets"] = [[0, 1], [1, 0]]
        next_hops = set()
        for i in range(32):
            s["seed"] = "tie-" + str(i)
            got = solve_lab(s)
            next_hops.add(got["cells"][0]["receiverId"])
            self.assertEqual(got["totalDeliveredOrStored"], 4)
        self.assertEqual(next_hops, {"TEST:slope_lab:00:01",
                                     "TEST:slope_lab:01:00"})

    def test_rectangular_grid_only(self):
        self.reject(lambda x: x.update(cells=[x["cells"][0], x["cells"][1][0:2]]))
        self.reject(lambda x: x.update(cells=[]))

    def test_no_nan_or_boolean_height(self):
        self.reject(lambda x: x["cells"][0][0].update(elevation=float("nan")))
        self.reject(lambda x: x["cells"][0][0].update(elevation=True))

    def test_negative_direction_forbidden_by_algorithm(self):
        got = solve_lab(slope())
        index = {x["id"]: x for x in got["cells"]}
        for entry in got["cells"]:
            nxt = entry["receiverId"]
            if nxt is not None:
                self.assertLess(index[nxt]["heightSynthetic"],
                                entry["heightSynthetic"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

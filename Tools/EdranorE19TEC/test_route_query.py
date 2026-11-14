#!/usr/bin/env python3
"""E19-TEC: consultas de grafo Gp, únicamente sobre paquetes sintéticos inscritos."""
from __future__ import annotations
import copy
import unittest

from route_query import query_route
from spatial import SpatialError
from test_spatial import packet, production


def setup():
    p, registry = production(packet())
    road = next(f for f in p["features"] if f["id"] == "road1")
    road["access"]["modes"] = ["walk", "cart"]
    road["jurisdiction"] = "casa_edranor"
    road["forestContext"] = "NONE"
    road["bidirectional"] = True
    return p, registry


def ask(p, registry, **kwargs):
    values = {"start_id": "n1", "goal_id": "n2", "mode": "walk",
              "grants": set(), "blocked_roads": set()}
    values.update(kwargs)
    return query_route(p, registry, **values)


class RouteTests(unittest.TestCase):
    def test_no_real_route_is_claimed_by_fixture(self):
        p, reg = setup()
        result = ask(p, reg)
        self.assertEqual(result["status"], "LAB_PATH_ONLY_NOT_GAMEPLAY")
        self.assertEqual(result["pathIds"], ["road1"])
        self.assertEqual(result["lengthMetres"], 2.0)
        self.assertIsNone(result["travelTime"])
        self.assertFalse(result["committed"])

    def test_no_unapproved_graph(self):
        p, reg = setup()
        reg["approvedSectors"] = []
        with self.assertRaises(SpatialError):
            ask(p, reg)

    def test_no_synthetic_export(self):
        with self.assertRaises(SpatialError):
            ask(packet(), {"schemaVersion": 1, "evidence": [], "approvedSectors": []})

    def test_blocked_route_stays_blocked(self):
        p, reg = setup()
        self.assertEqual(ask(p, reg, blocked_roads={"road1"})["status"],
                         "NO_VERIFIED_ROUTE")
        self.assertFalse(ask(p, reg, blocked_roads={"road1"})["committed"])

    def test_crown_requires_explicit_grant(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["jurisdiction"] = "crown_aethros"
        self.assertEqual(ask(p, reg)["status"], "NO_VERIFIED_ROUTE")
        self.assertEqual(ask(p, reg, grants={"CROWN_ACCESS"})["pathIds"], ["road1"])

    def test_bosque_alto_requires_grant(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["forestContext"] = "BOSQUE_ALTO"
        self.assertEqual(ask(p, reg)["status"], "NO_VERIFIED_ROUTE")
        self.assertEqual(ask(p, reg, grants={"BOSQUE_ALTO_ACCESS"})["pathIds"],
                         ["road1"])

    def test_bosque_real_requires_separate_royal_grant(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["forestContext"] = "BOSQUE_REAL"
        self.assertEqual(ask(p, reg, grants={"BOSQUE_ALTO_ACCESS"})["status"],
                         "NO_VERIFIED_ROUTE")
        self.assertEqual(ask(p, reg, grants={"ROYAL_FOREST_ACCESS"})["pathIds"],
                         ["road1"])

    def test_mode_restriction(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["access"]["modes"] = ["walk"]
        self.assertEqual(ask(p, reg, mode="cart")["status"], "NO_VERIFIED_ROUTE")
        self.assertEqual(ask(p, reg)["pathIds"], ["road1"])

    def test_directionality(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["bidirectional"] = False
        self.assertEqual(ask(p, reg, start_id="n2", goal_id="n1")["status"],
                         "NO_VERIFIED_ROUTE")

    def test_repeated_query_is_pure(self):
        p, reg = setup()
        before = copy.deepcopy(p)
        x = ask(p, reg)
        y = ask(p, reg)
        self.assertEqual(x, y)
        self.assertEqual(before, p)

    def test_unknown_place_or_mode(self):
        p, reg = setup()
        with self.assertRaises(SpatialError):
            ask(p, reg, goal_id="CT-01")
        with self.assertRaises(SpatialError):
            ask(p, reg, mode="spaceship")

    def test_unknown_rights_deny(self):
        p, reg = setup()
        road = next(f for f in p["features"] if f["id"] == "road1")
        road["jurisdiction"] = "UNKNOWN"
        with self.assertRaises(SpatialError):
            ask(p, reg)
        road["jurisdiction"] = "casa_edranor"
        road["forestContext"] = "UNKNOWN"
        with self.assertRaises(SpatialError):
            ask(p, reg)

    def test_self_query_does_not_move(self):
        p, reg = setup()
        result = ask(p, reg, goal_id="n1")
        self.assertEqual(result["pathIds"], [])
        self.assertEqual(result["lengthMetres"], 0.0)
        self.assertFalse(result["committed"])

if __name__ == "__main__":
    unittest.main(verbosity=2)

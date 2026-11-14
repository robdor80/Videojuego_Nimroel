#!/usr/bin/env python3
"""Validacion causal de R1-R5: B2 no puede ascender a B3/B4 por accidente."""
from __future__ import annotations
import copy
import hashlib
import json
import unittest

from spatial import SpatialError
from causal_atlas import MFS, build_catalog, read_inputs, verify_parents

class CausalAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = read_inputs()
        cls.catalog = build_catalog(cls.source)

    def assert_rejected(self, fn):
        sample = copy.deepcopy(self.source)
        fn(sample)
        with self.assertRaises(SpatialError):
            build_catalog(sample)

    def test_real_parents_compatible(self):
        verify_parents(self.source)
        self.assertEqual(len(self.catalog["contexts"]), 7)
        self.assertEqual([x["contextId"] for x in self.catalog["contexts"]], MFS)

    def test_worldstate_still_nonexistent(self):
        c = self.catalog
        self.assertIsNone(c["worldState"])
        self.assertIsNone(c["coordinates"])
        self.assertIsNone(c["seed"])
        self.assertEqual(c["physicalRouteCount"], 0)
        self.assertEqual(c["actualSettlementCount"], 0)
        self.assertEqual(c["unknownRegionIds"], ["MF-08"])
        for entry in c["contexts"]:
            self.assertIsNone(entry["geometry"])
            self.assertFalse(entry["eligibleForWorldState"])
            self.assertFalse(entry["approvedLandUse"])
            self.assertEqual(entry["actualPlaces"], [])
            self.assertEqual(entry["physicalGraphEdges"], [])

    def test_cross_phase_ids_not_instantiated(self):
        by_context = {c["contextId"]: c for c in self.catalog["contexts"]}
        for entry in self.source["R2"]["basinFamilies"]:
            if entry["contextId"] in by_context:
                self.assertEqual(by_context[entry["contextId"]]["basinStudyId"], entry["id"])
        self.assertEqual(len(self.catalog["sourceNameIdsOnlyNotMapped"]), 6)
        self.assertIn("rodas", [a["id"] for a in self.catalog["anchors"]])
        self.assertEqual(next(a["jurisdiction"] for a in self.catalog["anchors"]
                              if a["id"] == "rodas"), "crown_aethros")

    def test_catalog_byte_reproducible(self):
        first = json.dumps(self.catalog, sort_keys=True, ensure_ascii=False)
        second = json.dumps(build_catalog(read_inputs()), sort_keys=True, ensure_ascii=False)
        self.assertEqual(first, second)
        digest = self.catalog.copy()
        digest.pop("sha256")
        raw = json.dumps(digest, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":"), allow_nan=False).encode("utf-8")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.catalog["sha256"])

    def test_reject_r1_false_materialization(self):
        self.assert_rejected(lambda x: x["R1"].update(worldStateEntities=1))
        self.assert_rejected(lambda x: x["R1"].update(geometry={"fake": "polygon"}))

    def test_reject_invalid_mf08(self):
        self.assert_rejected(lambda x: x["R1"]["physicalRegions"][7].update(evaluable=True))
        self.assert_rejected(lambda x: x["R3"]["contexts"][7].update(status="ACTIVE"))
        self.assert_rejected(lambda x: x["R5"]["contexts"][7].update(nonEvaluable=False))

    def test_reject_wrong_hydrologic_parent(self):
        self.assert_rejected(lambda x: x["R3"]["contexts"][0].update(basinId="HC-04"))
        self.assert_rejected(lambda x: x["R5"]["contexts"][0].update(hydrology="HC-04"))
        self.assert_rejected(lambda x: x["R2"]["basinFamilies"][0].update(contextId="MF-02"))
        self.assert_rejected(lambda x: x["R2"]["basinFamilies"][0].update(receiver="LURIEN"))

    def test_reject_made_up_stream(self):
        self.assert_rejected(lambda x: x["R2"]["graphContract"]["minorGraphEdges"].append(
            {"from": "fake", "to": "fake"}))
        self.assert_rejected(lambda x: x["R2"]["materialization"].update(worldStateEntities=1))

    def test_reject_fake_roads(self):
        self.assert_rejected(lambda x: x["R4"]["networks"].update(pathfindingEnabled=True))
        self.assert_rejected(lambda x: x["R4"]["maturity"].update(actualRoads=1))
        self.assert_rejected(lambda x: x["R4"]["corridorQuestions"][0].update(actualRoute=True))

    def test_reject_fake_habitation(self):
        self.assert_rejected(lambda x: x["R5"]["maturity"].update(actualResidents=1))
        self.assert_rejected(lambda x: x["R5"]["maturity"].update(actualSettlements=1))
        self.assert_rejected(lambda x: x["R5"]["coverage"]["providerNodeIds"].append("tavern"))
        self.assert_rejected(lambda x: x["R5"]["worldState"].update(enabled=True))
        self.assert_rejected(lambda x: x["R5"]["studies"][0].update(actualSettlement=True))

    def test_reject_manual_anchors_generated(self):
        self.assert_rejected(lambda x: x["R5"]["anchors"][0].update(proceduralSpawn=True))
        self.assert_rejected(lambda x: next(a for a in x["R5"]["anchors"]
                                            if a["id"] == "rodas").update(
            jurisdiction="casa_edranor"))

    def test_reject_wrong_rights(self):
        self.assert_rejected(lambda x: x["R1"]["jurisdiction"].update(rodas="casa_edranor"))
        self.assert_rejected(lambda x: x["R1"]["jurisdiction"].update(
            bosqueAltoHarvest="OPEN_ACCESS"))
        self.assert_rejected(lambda x: x["R1"]["jurisdiction"].update(
            bosqueReal="casa_edranor"))

if __name__ == "__main__":
    unittest.main(verbosity=2)

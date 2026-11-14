#!/usr/bin/env python3
"""Regresion E19-TEC: pruebas puramente sinteticas sin materializar canon."""
from __future__ import annotations
import copy
import json
import unittest
from pathlib import Path

from spatial import (BASE, SpatialError, export_sector, read_json,
                     valid_manifest, validate_packet)

def feat(id, kind, typ, coords, **kwargs):
    result = {"id": id, "kind": kind,
              "geometry": {"type": typ, "coordinates": coords},
              "sourceId": "TEST_ONLY", "status": "SYNTHETIC_TEST"}
    result.update(kwargs)
    return result

def packet():
    return {
        "schemaVersion": 1, "sectorId": "TEST_SECTOR_ONLY",
        "contextIds": ["MF-01"], "mode": "synthetic",
        "authorization": {"kind": "SYNTHETIC_TEST", "approved": False,
                          "sourceId": "TEST_ONLY", "approvalId": None},
        "spatialReference": {"kind": "LOCAL_METRIC", "units": "metres",
                             "sourceId": "TEST_ONLY", "uncertaintyMetres": 0.25,
                             "sourceToLocal": {
                                 "scaleMetresPerSourceUnit": 1,
                                 "rotationRadians": 0,
                                 "sourceOrigin": [0, 0], "localOrigin": [0, 0]}},
        "features": [
            feat("n1", "route_node", "Point", [0, 0]),
            feat("n2", "route_node", "Point", [2, 0]),
            feat("road1", "road", "LineString", [[0, 0], [1, 0], [2, 0]],
                 fromNodeId="n1", toNodeId="n2", terrainEvidence={
                     "slopeSurveyed": True, "soilSurveyed": True,
                     "servitudeVerified": True, "inspectionId": "TEST_ONLY"},
                 access={
                     "surveyed": True, "legal": True, "maintained": True,
                     "waterCrossingsSurveyed": True, "capacity": 2}),
            feat("lake", "waterbody", "Point", [5, 5]),
            feat("stream", "river", "LineString", [[3, 3], [5, 5]],
                 receiverId="lake", hydrologyEvidence={
                     "basinId": "HC-01", "sourceCause": "TEST_SLOPE_RUNOFF",
                     "gradientSurveyed": True, "receiverSurveyed": True,
                     "seasonalityReviewed": True, "surveyId": "TEST_ONLY"}),
            feat("divide", "boundary_divide", "LineString",
                 [[10, 0], [10, 5]], mountainRange="Valkram",
                 westOwner="casa_darovan", eastOwner="casa_edranor",
                 politicalNorthClosure=False),
            feat("rodas", "settlement", "Point", [8, 8], name="Rodas",
                 kindOfSettlement="ALDEA", jurisdiction="crown_aethros",
                 sitingEvidence={
                     "waterAvailabilityVerified": True,
                     "sanitationVerified": True,
                     "certifiedGpAccess": True,
                     "landTenureVerified": True,
                     "hazardsReviewed": True}),
            feat("alto", "forest", "Polygon",
                 [[0, 10], [2, 10], [2, 12], [0, 12], [0, 10]],
                 name="Bosque Alto", harvestPermitRequired=True),
        ]
    }

def production(p):
    p = copy.deepcopy(p)
    p["mode"] = "production"
    p["authorization"] = {"kind": "AUTHOR_APPROVED_SECTOR", "approved": True,
                          "sourceId": "SOURCE:sector",
                          "approvalId": "APPROVAL:sector"}
    p["spatialReference"]["sourceId"] = "SURVEY:reference"
    for f in p["features"]:
        f["sourceId"] = "SURVEY:features"
        f["status"] = "APPROVED_B3"
        f["approvalId"] = "APPROVAL:sector"
    registry = {"schemaVersion": 1, "approvedSectors": [
        {"id": p["sectorId"], "approvalId": "APPROVAL:sector"}],
        "evidence": [
            {"id": id, "status": "APPROVED_B3", "reviewer": "TEST_ONLY"}
            for id in ("SOURCE:sector", "SURVEY:reference", "SURVEY:features")
        ]}
    return p, registry

class TestSpatial(unittest.TestCase):
    def setUp(self):
        self.p = packet()

    def reject(self, change):
        p = copy.deepcopy(self.p)
        change(p)
        with self.assertRaises(SpatialError):
            validate_packet(p)

    def test_manifest_explicitly_unmaterialized(self):
        valid_manifest(read_json(BASE / "technical_manifest_v0.1.json"))
        registry = read_json(BASE / "approval_registry_v0.1.json")
        self.assertEqual(registry, {"schemaVersion": 1,
                                    "approvedSectors": [], "evidence": []})

    def test_positive_synthetic_only(self):
        self.assertEqual(validate_packet(self.p)["features"], 8)
        self.assertFalse(validate_packet(self.p)["productionEligible"])

    def test_synthetic_cannot_export(self):
        with self.assertRaises(SpatialError):
            export_sector(self.p, {"schemaVersion": 1,
                                    "approvedSectors": [], "evidence": []})

    def test_production_requires_enrolled_evidence(self):
        p, registry = production(self.p)
        with self.assertRaises(SpatialError):
            export_sector(p, {"schemaVersion": 1,
                              "approvedSectors": [], "evidence": []})
        result = export_sector(p, registry)
        self.assertEqual(result["profile"], "NIMROEL_GODOT_2D_SPATIAL")
        self.assertEqual(result["contextIds"], ["MF-01"])
        self.assertEqual(result["maturity"], "LAB_GEOMETRY_NON_CANON_NOT_RUNTIME")
        self.assertEqual(len(result["sha256"]), 64)
        self.assertNotIn("worldState", result)

    def test_export_deterministic(self):
        p, registry = production(self.p)
        one = export_sector(p, registry)
        p["features"].reverse()
        two = export_sector(p, registry)
        self.assertEqual(one, two)
        self.assertEqual(one["features"], sorted(one["features"], key=lambda f: f["id"]))

    def test_no_false_northern_closure(self):
        self.reject(lambda p: p["features"][5].update(politicalNorthClosure=True))

    def test_no_wrong_mountain_side(self):
        self.reject(lambda p: p["features"][5].update(westOwner="casa_edranor"))

    def test_rodas_crown_and_aldea(self):
        self.reject(lambda p: p["features"][6].update(jurisdiction="casa_edranor"))
        self.reject(lambda p: p["features"][6].update(kindOfSettlement="VILLA"))

    def test_hallheim_outside(self):
        self.reject(lambda p: p["features"][6].update(name="Hallheim"))

    def test_no_unlicensed_alto(self):
        self.reject(lambda p: p["features"][7].update(harvestPermitRequired=False))

    def test_no_false_karsath_port(self):
        self.reject(lambda p: p["features"][6].update(name="Karsath", urbanPort=True))

    def test_no_false_dorth_caleran(self):
        self.reject(lambda p: p["features"][6].update(name="Dorth", caleranAtTown=True))

    def test_nonfictional_materialization_evidence(self):
        self.reject(lambda p: p["features"][2]["terrainEvidence"].update(
            soilSurveyed=False))
        self.reject(lambda p: p["features"][2]["terrainEvidence"].update(
            servitudeVerified=False))
        self.reject(lambda p: p["features"][4]["hydrologyEvidence"].update(
            receiverSurveyed=False))
        self.reject(lambda p: p["features"][4]["hydrologyEvidence"].update(
            basinId=""))
        self.reject(lambda p: p["features"][6]["sitingEvidence"].update(
            certifiedGpAccess=False))
        self.reject(lambda p: p["features"][6]["sitingEvidence"].update(
            landTenureVerified=False))

    def test_graph_road_without_real_nodes(self):
        self.reject(lambda p: p["features"][2].update(toNodeId="missing"))
        self.reject(lambda p: p["features"][2]["geometry"].update(
            coordinates=[[0, 0], [1, 0], [3, 0]]))

    def test_road_needs_access_and_capacity(self):
        self.reject(lambda p: p["features"][2]["access"].update(legal=False))
        self.reject(lambda p: p["features"][2]["access"].update(capacity=0))
        self.reject(lambda p: p["features"][2]["access"].update(surveyed=False))

    def test_river_requires_real_receiver_and_continuity(self):
        self.reject(lambda p: p["features"][4].update(receiverId="none"))
        self.reject(lambda p: p["features"][4]["geometry"].update(
            coordinates=[[3, 3], [4, 4]]))

    def test_water_cycle(self):
        def mutate(p):
            p["features"][3] = feat("lake", "river", "LineString",
                                   [[5, 5], [3, 3]], receiverId="stream",
                                   hydrologyEvidence={
                                       "basinId": "HC-01",
                                       "sourceCause": "TEST_SLOPE_RUNOFF",
                                       "gradientSurveyed": True,
                                       "receiverSurveyed": True,
                                       "seasonalityReviewed": True,
                                       "surveyId": "TEST_ONLY"})
        self.reject(mutate)

    def test_boolean_coordinate_forbidden(self):
        self.reject(lambda p: p["features"][0]["geometry"].update(
            coordinates=[True, 0]))

    def test_nan_coordinate_forbidden(self):
        self.reject(lambda p: p["features"][0]["geometry"].update(
            coordinates=[float("nan"), 0]))

    def test_line_self_intersection(self):
        self.reject(lambda p: p["features"][5]["geometry"].update(
            coordinates=[[0, 0], [2, 2], [0, 2], [2, 0]]))

    def test_polygon_self_intersection(self):
        self.reject(lambda p: p["features"][7]["geometry"].update(
            coordinates=[[0, 10], [2, 12], [0, 12], [2, 10], [0, 10]]))

    def test_duplicate_id(self):
        self.reject(lambda p: p["features"][1].update(id="n1"))

    def test_north_context_not_materializable(self):
        self.reject(lambda p: p.update(contextIds=["MF-08"]))
        self.reject(lambda p: p.update(contextIds=["U7"]))
        self.reject(lambda p: p.update(contextIds=[]))

    def test_no_false_authority(self):
        self.reject(lambda p: p["authorization"].update(approved=True))
        self.reject(lambda p: p["features"][0].update(status="APPROVED_B3"))

    def test_empty_production_sector_denied(self):
        p, registry = production(self.p)
        p["features"] = []
        with self.assertRaises(SpatialError):
            export_sector(p, registry)

    def test_reference_has_units_and_error(self):
        self.reject(lambda p: p["spatialReference"].update(units="pixels"))
        self.reject(lambda p: p["spatialReference"].update(uncertaintyMetres=-1))
        self.reject(lambda p: p["spatialReference"].pop("sourceToLocal"))
        self.reject(lambda p: p["spatialReference"]["sourceToLocal"].update(
            scaleMetresPerSourceUnit=0))
        self.reject(lambda p: p["spatialReference"]["sourceToLocal"].update(
            rotationRadians=float("inf")))

    def test_manifest_mutations_denied(self):
        m = read_json(BASE / "technical_manifest_v0.1.json")
        for fn in (
            lambda x: x["invariants"].update(northJoined=True),
            lambda x: x.update(actualPhysicalRoadEdges=1),
            lambda x: x["gates"][2].update(passed=True),
            lambda x: x.update(rejectedSourcePR84Used=True),
            lambda x: x.update(spatialReference={"units": "metres"}),
        ):
            altered = copy.deepcopy(m)
            fn(altered)
            with self.assertRaises(SpatialError):
                valid_manifest(altered)

if __name__ == "__main__":
    unittest.main(verbosity=2)

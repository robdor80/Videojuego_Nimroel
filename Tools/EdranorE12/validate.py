#!/usr/bin/env python3
"""Edranor E12: verificación CRUZADA de autoría y contratos, nunca gameplay."""
import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Edranor"
DATA = TERR / "Datos operativos"
PACK = ROOT / "ContentPacks/edranor-territory"
NAMES = ["dorth", "lumina", "karsath", "rodas"]
PROTECTED = NAMES + ["hallheim"]
OWNERS = ["casa_edranor"] * 3 + ["crown_aethros"]
BASE = "nimroel.edranor.territory"
SUFFIX = [
    "manifest", "relief", "hydrology", "climate_soils_ecosystems",
    "economy_viticulture", "roads_communications", "settlement_rules",
    "canonical_nuclei", "population_services", "governance", "lore",
]
FILES = {
    f"E{i:02d}": DATA / f"edranor_e{i:02d}_{suffix}_v0.1.json"
    for i, suffix in enumerate(SUFFIX)
}

class AuditError(ValueError):
    pass

def require(ok, why):
    if not ok:
        raise AuditError(why)

def unique_pairs(pairs):
    output = {}
    for key, value in pairs:
        require(key not in output, "Duplicate JSON key: " + key)
        output[key] = value
    return output

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_pairs)

def ids(items):
    return [item["id"] for item in items]

def pointer(obj, fragment):
    require(fragment.startswith("/"), "JSON pointer must be absolute")
    for part in fragment.split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj

def check(docs, projection, manifest, resources, fixtures):
    a = [docs[f"E{i:02d}"] for i in range(11)]
    d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10 = a
    require(all(d.get("phase")==f"E{i:02d}" and d.get("runtimeEnabled") is False
                for i,d in enumerate(a)), "E00–E10 are design-only")
    require(d0["house"]["id"] == "casa_edranor" and d0["house"]["seatId"] == "dorth",
            "E00 house or capital")
    require(d0["inheritance"] == ["nimroel_core", "norgard_defaults",
                                "casa_edranor", "localidad", "world_state"],
            "Norgard authority hierarchy")
    require(d0["protectedIds"] == PROTECTED and ids(d0["locations"]) == PROTECTED,
            "E00 canonical anchors")
    for phase, rows in [
        ("E00", d0["locations"][:4]), ("E01", d1["anchors"][:4]),
        ("E02", d2["anchors"][:4]), ("E03", d3["anchors"][:4]),
        ("E04", d4["anchors"][:4]), ("E05", d5["anchors"][:4]),
        ("E06", d6["protectedAnchors"][:4]), ("E07", d7["settlements"]),
        ("E08", d8["localityModels"]), ("E09", d9["localityModels"]),
        ("E10", d10["territorialPlaces"]), ("E11", projection["places"]),
    ]:
        require(ids(rows) == NAMES, "Canonical place drift: " + phase)
    for phase, rows, field in [
        ("E00",d0["locations"][:4],"jurisdictionOwner"),
        ("E01",d1["anchors"][:4],"jurisdictionOwner"),
        ("E02",d2["anchors"][:4],"jurisdictionOwner"),
        ("E03",d3["anchors"][:4],"owner"),
        ("E04",d4["anchors"][:4],"owner"),
        ("E05",d5["anchors"][:4],"owner"),
        ("E07",d7["settlements"],"jurisdictionOwner"),
        ("E08",d8["localityModels"],"jurisdictionOwner"),
        ("E09",d9["localityModels"],"jurisdictionOwner"),
        ("E10",d10["territorialPlaces"],"authorityOwner"),
        ("E11",projection["places"],"jurisdictionOwner"),
    ]:
        require([x[field] for x in rows] == OWNERS, "Jurisdiction drift: " + phase)
    require(d0["locations"][4]["insideEdranorPerimeter"] is False
            and d1["cartography"]["northBoundaryClosed"] is False
            and d1["cartography"]["metricGeometryValidated"] is False
            and d1["cartography"]["georeferenced"] is False
            and d1["cartography"]["polygonGeometry"] == [],
            "E00/E01 false map certainty")
    units = ids(d1["reliefUnits"])
    require(len(units) == len(set(units)) == 7, "E01 seven unique qualitative units")
    for phase, got in [
        ("E02", [x["reliefUnitId"] for x in d2["localDrainageUnits"]]),
        ("E03", [x["reliefUnitId"] for x in d3["reliefProfiles"]]),
        ("E04", [x["reliefUnitId"] for x in d4["territorialStudies"]]),
        ("E06", ids(d6["zones"])),
    ]:
        require(got == units, "Seven physical units drift in " + phase)
    require(d2["scope"]["basinPolygons"] == [] and d2["scope"]["riverPolylines"] == []
            and d2["scope"]["localHydrographyValidated"] is False
            and [x["membershipInEdranor"] for x in d2["regionalCanonicalFeatures"]]
                == ["UNKNOWN","UNKNOWN"], "E02 lake/river promoted to local geometry")
    require(d3["landUseRules"]["allSevenUnitsViticultural"] is False
            and d3["landUseRules"]["polarViticultureByDefault"] is False
            and d3["hydrologyGuard"]["antelaInsideEdranor"] == "UNKNOWN"
            and d3["scope"]["soilPolygons"] == [], "E03 fabricated climate/soils")
    require(d4["canonicalBasis"]["primaryNorgardWineRegion"] is True
            and d4["forestGuard"]["sourceForest"] == "bosque_alto"
            and d4["forestGuard"]["rightsHolder"] == "UNKNOWN"
            and d4["guardrails"]["roadsEstablished"] is False
            and d4["economicRules"]["noInternalHouseCustoms"] is True,
            "E04 production/ownership invented")
    require(len(d5["candidateRoadQuestions"]) == 4
            and all(x["status"] == "QUESTION_ONLY" and
                    x["roadConfirmed"] is False and
                    x["traversable"] is False
                    for x in d5["candidateRoadQuestions"])
            and d5["scope"]["physicalEdges"] == []
            and d5["scope"]["pathfindingEnabled"] is False
            and d5["rightsAndFiscality"]["edranorControlsRodas"] is False,
            "E05 road or Rodas sovereignty invented")
    require(len(d6["models"]) == 8 and len(set(ids(d6["models"]))) == 8
            and d6["scope"]["realSitePlacementAllowed"] is False
            and d6["scope"]["proceduralSettlementsInstantiated"] == 0
            and d6["scope"]["realSettlementInstances"] == []
            and ids(d6["protectedAnchors"]) == PROTECTED
            and all(x["procedural"] is False for x in d6["protectedAnchors"]),
            "E06 laboratory incorrectly treated as settlements")
    require(d7["protectedIds"] == PROTECTED and
            all(x["protected"] is True and x["procedural"] is False and
                x["instantiated"] is False and x["population"] is None and
                x["coordinates"] is None and x["physicalRoads"] == []
                for x in d7["settlements"]),
            "E07 canonical settlements instantiated")
    require(d7["settlements"][3]["type"] == "village"
            and d7["settlements"][3]["berserkerCommandOwner"] == "crown_aethros",
            "EDD-06 or royal berserker authority regression")
    require(len(d8["serviceCatalog"]) == 15 and len(d8["occupationCatalog"]) == 16
            and all(x["operational"] is False and x["providerInstances"] == []
                    for x in d8["serviceCatalog"])
            and all(x["filledPositions"] == 0 and x["workerPersonIds"] == []
                    for x in d8["occupationCatalog"])
            and all(value == [] for value in d8["instanceRegistry"].values())
            and all(x["population"] is None and x["householdCount"] is None
                    for x in d8["localityModels"]),
            "E08 services or census invented")
    require(len(d9["institutionRoleCatalog"]) == 10
            and len(d9["authorizationCatalog"]) == 11
            and d9["fiscalPolicy"]["noInternalCustoms"] is True
            and d9["fiscalPolicy"]["noEdranorMint"] is True
            and d9["defencePolicy"]["noEdranorCommandOverRodasBerserkers"] is True
            and d9["defencePolicy"]["minimumArmedAge"] == 18
            and all(value == [] for value in d9["instanceRegistry"].values())
            and all(x["issuedIds"] == [] and x["operational"] is False
                    for x in d9["authorizationCatalog"]),
            "E09 governance, personnel, permits or tariffs invented")
    require(d10["dynasty"]["status"] == "PROPUESTA_E10_NOT_LEGAL_KIN"
            and d10["dynasty"]["legalSuccessionEstablished"] is False
            and len(d10["characters"]) == 11
            and len(d10["conflicts"]) == 8 and len(d10["scenes"]) == 8
            and all(x["provenance"] == "PROPUESTA_E10"
                    and x["npcId"] is None and x["legalKinRecordId"] is None
                    for x in d10["characters"])
            and all(x["runtimeEnabled"] is False for x in d10["conflicts"] + d10["scenes"])
            and d10["instantiatedNpcIds"] == [] and d10["historicalTreatyIds"] == []
            and d10["instantiatedQuestIds"] == [] and d10["physicalRoadIds"] == [],
            "E10 lore wrongly ratified or executed")
    require(projection["classification"] == "STRUCTURAL_CATALOG_NOT_GAMEPLAY"
            and projection["runtimeEnabled"] is False
            and projection["worldStateEntitiesCreated"] == 0
            and projection["protectedIds"] == PROTECTED
            and projection["territorialContextPlaceIds"] == NAMES
            and projection["excludedPlaceIds"] == ["hallheim"]
            and projection["governance"]["rodasMilitaryCommand"] == "crown_aethros"
            and projection["governance"]["rodasDruidicHouseIsTemple"] is False
            and projection["governance"]["internalCustoms"] is False
            and projection["governance"]["hallheimInsideEdranor"] is False
            and all(v is False for v in projection["executionCapabilities"].values()),
            "E11 projection claims gameplay/sovereignty")
    for i, place in enumerate(projection["places"]):
        require(all(place[field] == OWNERS[i]
                    for field in ("jurisdictionOwner", "fiscalOwner",
                                  "justiceOwner", "securityOwner")),
                "E11 legal authority drift: " + NAMES[i])
        require(place["berserkerCommander"] ==
                ("crown_aethros" if i == 3 else None)
                and place["proceduralSpawnAllowed"] is False
                and place["physicalRouteConfirmed"] is False
                and place["population"] is None
                and place["instantiatedNpcIds"] == [],
                "E11 materialization or berserker command: " + NAMES[i])
    require(len(projection["sourceLocks"]) == 11
            and [x["phase"] for x in projection["sourceLocks"]]
                == [f"E{i:02d}" for i in range(11)], "E11 source locks")
    for lock in projection["sourceLocks"]:
        require(lock["path"] == FILES[lock["phase"]].relative_to(ROOT).as_posix(),
                "E11 wrong source lock path")
    require([x["id"] for x in projection["definitions"]]
            == [BASE + ":territory/edranor"] + [BASE + ":places/" + n for n in NAMES],
            "E11 stable DefinitionIds")
    for definition in projection["definitions"]:
        require(definition["sourcePhase"] in docs
                and pointer(docs[definition["sourcePhase"]],
                            definition["sourcePointer"]) is not None,
                "E11 broken source pointer")
    require(projection["unpromotedDesign"] == {
            "sourcePhase":"E10", "provenance":"PROPUESTA_E10",
            "characters":11, "conflicts":8, "scenes":8,
            "legalKinRecords":0, "npcInstances":0, "questInstances":0,
            "worldStateEvents":0}, "E11 promoted E10 proposals")
    require(manifest["pack_id"] == BASE and manifest["dependencies"] == []
            and len(manifest["resources"]) == 5
            and len(resources) == 5, "E11 manifest/resource quantity")
    require({x["id"] for x in resources.values()}
            == {x["id"] for x in projection["definitions"]}, "Pack IDs differ")
    for resource in resources.values():
        require(set(resource) == {"$schema","id","kind","references"},
                "Unapproved CoreRPG resource fields")
        for link in resource["references"]:
            require(any(x["id"] == link["target"] and
                        x["kind"] == link["expected_kind"]
                        for x in resources.values()), "Broken typed resource link")
    require(fixtures["status"] == "TEST_ONLY"
            and len(fixtures["scenarios"]) == 12
            and all(x["classification"] == "TEST_ONLY"
                    and x["executedInCoreRPG"] is False
                    and x["implementedAsGameplay"] is False
                    for x in fixtures["scenarios"]), "Fixtures promoted to gameplay")

def load():
    docs = {phase:read(path) for phase,path in FILES.items()}
    projection = read(PACK / "authoring/projection-v0.1.json")
    manifest = read(PACK / "pack/manifest.json")
    resources = {path:read(PACK / "pack" / path) for path in manifest["resources"]}
    fixtures = read(PACK / "fixtures/e11-scenarios-v0.1.json")
    return docs, projection, manifest, resources, fixtures

def check_source_locks(projection):
    for lock in projection["sourceLocks"]:
        path = lock["path"]
        got = subprocess.run(["git", "hash-object", "--path=" + path, path],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
        require(got == lock["gitBlobSha"], "Source SHA mismatch: "+lock["phase"])

def inventory():
    md = js = refs = 0
    required = [
        "PLAN_DESARROLLO_EDRANOR_v0.1.md", "README.md", "E12_INDICE.md",
        "00_Control_del_proyecto/TRASPASO_E12.md",
        "00_Control_del_proyecto/ESTADO_VIGENTE_E12.md",
        "Auditorias/E12_AUDITORIA_INTEGRAL.md",
        "Auditorias/E12_INVENTARIO_CANON_Y_AUTORIDAD.md",
        "Auditorias/E12_MATRIZ_TRANSVERSAL.md",
        "Auditorias/E12_REGISTRO_INCIDENCIAS.md",
        "Auditorias/E12_ACTA_CIERRE.md",
    ] + [f"E{i:02d}_INDICE.md" for i in range(1,12)]
    require(all((TERR / name).is_file() for name in required), "Missing phase/closure document")
    for path in TERR.rglob("*"):
        if path.suffix.lower() == ".md":
            path.read_text(encoding="utf-8-sig")
            md += 1
        elif path.suffix.lower() == ".json":
            document = read(path)
            js += 1
            def walk(value):
                nonlocal refs
                if isinstance(value, dict):
                    for item in value.values(): walk(item)
                elif isinstance(value, list):
                    for item in value: walk(item)
                elif isinstance(value, str) and value.startswith("Worldbuilding/") and value.endswith((".md",".json")):
                    refs += 1
                    require((ROOT / value).is_file(), "Missing source reference: "+value)
            walk(document)
    require(md >= 80 and js >= 15, "Incomplete Edranor material inventory")
    return md,js,refs

def negatives(original):
    docs, proj, manifest, resources, fixtures = original
    trials = [
        ("E00", lambda x:x["locations"][3].update(jurisdictionOwner="casa_edranor")),
        ("E01", lambda x:x["cartography"].update(northBoundaryClosed=True)),
        ("E01", lambda x:x["reliefUnits"].append({"id":"invented"})),
        ("E02", lambda x:x["regionalCanonicalFeatures"][1].update(membershipInEdranor="YES")),
        ("E02", lambda x:x["scope"].update(localHydrographyValidated=True)),
        ("E03", lambda x:x["landUseRules"].update(polarViticultureByDefault=True)),
        ("E04", lambda x:x["forestGuard"].update(rightsHolder="casa_edranor")),
        ("E04", lambda x:x["guardrails"].update(roadsEstablished=True)),
        ("E05", lambda x:x["candidateRoadQuestions"][0].update(roadConfirmed=True)),
        ("E05", lambda x:x["rightsAndFiscality"].update(edranorControlsRodas=True)),
        ("E06", lambda x:x["scope"].update(proceduralSettlementsInstantiated=1)),
        ("E06", lambda x:x["protectedAnchors"][3].update(procedural=True)),
        ("E07", lambda x:x["settlements"][3].update(type="city")),
        ("E08", lambda x:x["localityModels"][0].update(population=1234)),
        ("E08", lambda x:x["instanceRegistry"]["people"].append("invented")),
        ("E09", lambda x:x["fiscalPolicy"].update(noInternalCustoms=False)),
        ("E09", lambda x:x["defencePolicy"].update(noEdranorCommandOverRodasBerserkers=False)),
        ("E10", lambda x:x["dynasty"].update(legalSuccessionEstablished=True)),
        ("E10", lambda x:x["characters"][0].update(npcId="invented")),
    ]
    for phase,fn in trials:
        changed = copy.deepcopy(docs)
        fn(changed[phase])
        try: check(changed,proj,manifest,resources,fixtures)
        except (AuditError,KeyError,TypeError,IndexError): continue
        raise AuditError("Negative mutation accepted: "+phase)
    for label,modify in [
        ("E11 gameplay flag",lambda p:p["executionCapabilities"].update(gameplay=True)),
        ("E11 royal fiscal right",lambda p:p["places"][3].update(fiscalOwner="casa_edranor")),
        ("E11 Hallheim inclusion",lambda p:p["excludedPlaceIds"].clear()),
        ("E11 fake name canon",lambda p:p["unpromotedDesign"].update(npcInstances=1)),
    ]:
        p=copy.deepcopy(proj); modify(p)
        try: check(docs,p,manifest,resources,fixtures)
        except (AuditError,KeyError,TypeError,IndexError): continue
        raise AuditError("Negative mutation accepted: "+label)
    bad=copy.deepcopy(resources); bad["resources/places/rodas.json"]["id"]="fake"
    try: check(docs,proj,manifest,bad,fixtures)
    except AuditError: pass
    else: raise AuditError("E11 ID mutation accepted")
    return len(trials)+5

def main():
    n=inventory()
    original=load()
    check(*original)
    check_source_locks(original[1])
    rejected=negatives(original)
    print(f"EDRANOR E12 STATIC PASS: {n[0]} MD, {n[1]} JSON, {n[2]} source path refs; "
          f"11 source locks, 5 stable definitions, 4 sites, {rejected} negative mutations rejected.")
    print("Documentary / native Core catalog only; no Godot scene or territorial gameplay.")

if __name__ == "__main__":
    try: main()
    except (AuditError, KeyError, TypeError, IndexError, OSError, ValueError,
            subprocess.CalledProcessError) as exc:
        print("EDRANOR E12 FAIL:", exc, file=sys.stderr)
        sys.exit(1)

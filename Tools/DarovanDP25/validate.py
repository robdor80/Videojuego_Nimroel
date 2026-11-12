#!/usr/bin/env python3
"""D.P25 editorial static contract, source-provenance and adversarial test suite.
This does not instantiate NPCs, relationships, routes, quests or WorldState.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR_REL = Path("Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan")
DATA_REL = TERR_REL / "Datos operativos/darovan_dp25_personajes_relaciones_conflictos_v0.1.json"
DOC = ROOT / TERR_REL / "Profundizacion_2026/D.P25"
SOURCE_FILES = {
    "D.P20": "darovan_dp20_veldora_proposals_v0.1.json",
    "D.P21": "darovan_dp21_taramin_proposals_v0.1.json",
    "D.P22": "darovan_dp22_syvaris_proposals_v0.1.json",
    "D.P23": "darovan_dp23_treihord_editorial_v0.1.json",
    "D.P24": "darovan_dp24_rural_editorial_v0.1.json",
}
SOURCE_ARRAY = {"D.P20": "proposedPeople", "D.P21": "proposedPeople",
                "D.P22": "proposedPeople", "D.P23": "biographyBases",
                "D.P24": "biographyBases"}
EXPECTED_NAMES = [
    ("TRH-N01", "Aldren Meris", "treihord"),
    ("TRH-N04", "Ilva Nered", "treihord"),
    ("TRH-N07", "Orven Deil", "treihord"),
    ("TRH-N08", "Naira Halven", "treihord"),
    ("TRH-N10", "Varo Mendir", "treihord"),
    ("VEL-N01", "Liria Menor", "veldora"),
    ("VEL-N02", "Sered Alvar", "veldora"),
    ("VEL-N04", "Oren Talen", "veldora"),
    ("VEL-N05", "Vesa Orrin", "veldora"),
    ("VEL-N08", "Edris Fen", "veldora"),
    ("VEL-N10", "Fenra Doril", "veldora"),
    ("TAR-N01", "Mareva Senn", "taramin"),
    ("TAR-N04", "Corven Dail", "taramin"),
    ("TAR-N05", "Orea Niv", "taramin"),
    ("TAR-N08", "Sarel Tern", "taramin"),
    ("TAR-N10", "Breon Cal", "taramin"),
    ("SYV-N03", "Maela Ruvin", "syvaris"),
    ("SYV-N04", "Teren Velas", "syvaris"),
    ("SYV-N06", "Sera Nald", "syvaris"),
    ("SYV-N07", "Orel Sena", "syvaris"),
    ("SYV-N08", "Cira Denor", "syvaris"),
    ("RUR-N01", "Mara Lenvar", "rural_conditional"),
    ("RUR-N04", "Toren Valis", "rural_conditional"),
    ("RUR-N05", "Saira Dren", "rural_conditional"),
    ("RUR-N06", "Olven Seran", "rural_conditional"),
    ("RUR-N07", "Mira Kelen", "arven_conditional"),
    ("RUR-N08", "Neris Salvar", "arven_conditional"),
]
BY_PREFIX = {"TRH": "D.P23", "VEL": "D.P20", "TAR": "D.P21",
             "SYV": "D.P22", "RUR": "D.P24"}
UNKNOWN_KEYS = set("""currentDarovanLord royalCommanders namedJudges exactNpcAges
npcEntityIds verifiedNpcHomes actualKinshipGraph actualRelationships
relationshipScores npcCoordinates householdCensus validatedRuralSites
sourceWaterIds parcelRights materialInventory pricesAndWages timeToTravel
interIslandRoutes bridgesAndFords verifiedForestPlots actualHistoricalEvents
publicQuestEvents""".split())
CANON = {
    "kingdom": "Norgard", "house": "Darovan",
    "cities": ["treihord", "veldora", "taramin", "syvaris"],
    "excludedCity": "karsath", "treihordRiver": "Belara",
    "treihordNeighborhoodCount": 8, "treihordApproxPopulation": 32000,
    "treihordMint": False, "treihordLaVenaPublicAccess": False,
    "belaraShallowIndustrialNavigationOnly": True,
    "veldoraExternalCustomsAuthority": "CORONA_NORGARD",
    "noInternalCustoms": True, "taraminRiver": "Thalen",
    "taraminRiverBranchCount": 2, "taraminSingleSouthernForest": True,
    "syvarisNavy": "ARMADA_REAL_NORGARD", "arvenOwner": "DAROVAN",
    "arvenMantoVerdePercentApprox": 90, "arvenSyvarisFerryExists": False,
    "verifiedNewTransportRoutes": [], "pilaresSingleForest": True,
    "agujaInteriorPermanentSettlements": False,
}
RUNTIME = {
    "coreRpgIntegrated": False, "godotIntegrated": False,
    "newNpcs": 0, "newHouseholds": 0, "activeConflicts": 0,
    "realQuests": 0, "worldStateChanged": False,
    "activatedRelationships": 0, "physicalSettlements": 0,
    "newRoutes": 0, "newMilitaryOrders": 0, "newCustoms": 0,
}

def req(test: bool, message: str) -> None:
    if not test:
        raise AssertionError(message)

def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def ids(group: list, prefix: str, n: int) -> None:
    req(isinstance(group, list) and len(group) == n, f"{prefix}: count")
    req([row["id"] for row in group] ==
        [f"{prefix}{i:02d}" for i in range(1, n + 1)],
        f"{prefix}: missing, reordered or duplicated IDs")

def validate(d: dict, *, docs: bool = False) -> None:
    req((d["schemaVersion"], d["documentId"], d["phase"], d["version"]) ==
        (1, "darovan_dp25_personajes_relaciones_conflictos_v0.1", "D.P25", "0.1.0"), "metadata")
    req(d["status"] == "EDITORIAL_SELECTED_BY_EXPLICIT_DELEGATION_NOT_WORLDSTATE", "unauthorized promotion")
    req(d["approval"] == {
        "creativeApproved": True,
        "source": "USER_D.P25_2026_11_12_AUTONOMOUS_DECISIONS",
        "scope": "EDITORIAL_ONLY",
        "mergeAuthorized": False,
    }, "approval or merge authority")
    req(d["branchBase"] == {"name": "main", "sha": "512434957f248f2513761615a9685ddd6c49c65f"}, "base")
    req(d["dependencies"] == [
        {"phase": "D.P23", "pr": 46, "expectedHeadAtStart": "6ee4f4a672a138e29feefb558e41bbf10fbce64e",
         "wasDraft": True, "mergedIntoBranch": False},
        {"phase": "D.P24", "pr": 47, "expectedHeadAtStart": "b0b14db66f1cf1ca0e9eb27f28cde403e3e16a89",
         "wasDraft": True, "mergedIntoBranch": False},
    ], "unresolved upstream PR dependency")
    req(d["inheritedCanon"] == CANON, "changed Norgard/Darovan canon")
    req(d["runtime"] == RUNTIME, "invented executable state")
    req(set(d["lockedUnknowns"]) == UNKNOWN_KEYS
        and all(v is None for v in d["lockedUnknowns"].values()), "UNKNOWN promoted")
    req(d["sourceCatalog"] == {
        "biographiesTotal": 52,
        "byPhase": {"D.P20": 10, "D.P21": 10, "D.P22": 10, "D.P23": 10, "D.P24": 12},
        "selectedCount": 27, "unselectedCount": 25,
        "sourceFilesStatus": "D.P23_D.P24_UNMERGED_WHEN_AUTHORED",
    }, "source scope")
    req(d["verification"] == {
        "mustReconcilePrs": [46, 47], "requireFinalHeadCi": True,
        "ciNotProofOfRuntime": True, "dP26AuditRequired": True,
        "mergeNeedsSeparateAuthorization": True,
    }, "incorrect closure flags")

    ids(d["people"], "DP25-P", 27)
    ids(d["relationships"], "DP25-R", 30)
    ids(d["householdCareModels"], "DP25-F", 4)
    ids(d["conflicts"], "DP25-C", 10)
    ids(d["testOnlyScenes"], "DP25-E", 10)
    ids(d["delegatedDecisions"], "DP25-D", 8)
    refs = set()
    for p, (ref, name, scope) in zip(d["people"], EXPECTED_NAMES):
        req((p["sourceBiographyId"], p["editorialName"], p["territorialScope"]) ==
            (ref, name, scope), f"biography retconned: {ref}")
        req(p["sourcePhase"] == BY_PREFIX[ref[:3]], f"bad biography provenance {ref}")
        req(ref not in refs, "duplicate source person")
        refs.add(ref)
        req(p["editorialStatus"] == "AUTHORED_EDITORIAL_SELECTED"
            and p["selectedForTerritorialNarrative"] is True
            and p["npcInstantiated"] is False and p["worldStateChanged"] is False,
            f"person became NPC: {ref}")
        for key in ("personEntityId", "householdEntityId", "actualLocationId", "legalRoleId",
                    "knowledgeStateId"):
            req(p[key] is None, f"invented person fact {ref}: {key}")
        req(p["currentRelationshipIds"] == [], f"active relationship list on {ref}")

    seen_edges = set()
    for rel in d["relationships"]:
        pair = rel["personRefs"]
        req(len(pair) == 2 and pair[0] != pair[1] and set(pair) <= refs,
            f"invalid relationship endpoints {rel['id']}")
        req(tuple(sorted(pair)) not in seen_edges, "duplicate relationship pair")
        seen_edges.add(tuple(sorted(pair)))
        req(bool(rel["domain"]) and rel["status"] == "FUTURE_CONDITIONAL_RELATION"
            and rel["actorContactsVerified"] is False and rel["active"] is False
            and rel["sourceEventId"] is None and rel["actualRelationshipId"] is None
            and rel["aToBDimensions"] is None and rel["bToADimensions"] is None
            and rel["approvedRouteId"] is None and rel["worldStateChanged"] is False,
            f"relationship activated without evidence: {rel['id']}")

    for f in d["householdCareModels"]:
        req(len(f["personRefs"]) == 2 and set(f["personRefs"]) <= refs
            and f["status"] == "FUTURE_HOUSEHOLD_CARE_MODEL"
            and f["actualKinshipIds"] == [] and f["actualHouseholdIds"] == []
            and f["kinshipEstablished"] is False and f["worldStateChanged"] is False,
            f"genealogy invented: {f['id']}")

    edgeids = {r["id"] for r in d["relationships"]}
    for c in d["conflicts"]:
        req(bool(c["name"]) and len(c["personRefs"]) >= 2
            and len(set(c["personRefs"])) == len(c["personRefs"])
            and set(c["personRefs"]) <= refs
            and len(c["triggersRequired"]) >= 3
            and all(isinstance(x, str) and x for x in c["triggersRequired"])
            and len(c["relationshipIdeaRefs"]) >= 2
            and set(c["relationshipIdeaRefs"]) <= edgeids,
            f"conflict graph or required evidence: {c['id']}")
        req(c["status"] == "FUTURE_CONDITIONAL_CONFLICT" and
            c["activated"] is False and c["triggerSatisfied"] is False
            and c["actualConflictEntityId"] is None and c["actualQuestId"] is None
            and c["publicHistoryEventId"] is None and c["determinedOutcome"] is None
            and c["worldStateChanged"] is False, f"fabricated conflict history: {c['id']}")

    conflict_map = {c["id"]: c for c in d["conflicts"]}
    for scene in d["testOnlyScenes"]:
        c = conflict_map[scene["linkedConflictRef"]]
        req(scene["id"][-2:] == c["id"][-2:]
            and scene["personRefs"] and set(scene["personRefs"]) <= set(c["personRefs"])
            and scene["status"] == "TEST_ONLY" and scene["everOccurred"] is False
            and scene["actualSceneEntityId"] is None and scene["worldStateEventId"] is None
            and scene["worldStateChanged"] is False and scene["knowledgeLeaked"] is False
            and scene["realTravelPerformed"] is False and scene["inventoryMutation"] is False,
            f"TEST_ONLY leaked into WorldState: {scene['id']}")
    for dec in d["delegatedDecisions"]:
        req(dec["option"] == "A" and dec["status"] == "EDITORIAL_APPROVED_BY_USER_DELEGATION"
            and dec["createsWorldState"] is False and dec["grantsMergeAuthority"] is False,
            f"overextended decision: {dec['id']}")

    if docs:
        mapping = {
            "people": "01_reparto_y_relevancia_territorial.md",
            "relationships": "02_red_de_relaciones_y_hogares.md",
            "householdCareModels": "02_red_de_relaciones_y_hogares.md",
            "conflicts": "03_conflictos_y_cadenas_causales.md",
            "testOnlyScenes": "05_escenas_multirrol_y_memoria.md",
            "delegatedDecisions": "07_decisiones_editoriales.md",
        }
        req((DOC / "README.md").is_file(), "missing D.P25 README")
        for group, filename in mapping.items():
            content = (DOC / filename).read_text(encoding="utf-8")
            for row in d[group]:
                req(row["id"] in content, f"untraceable {row['id']} in {filename}")
        for filename in ("04_poderes_y_justicia.md", "06_contratos_y_materializacion.md",
                         "08_auditoria_y_deuda.md"):
            req((DOC / filename).is_file(), f"missing {filename}")
        for token in ("CoreRPG", "PR #46", "PR #47", "no"):
            req(token.lower() in (DOC / "README.md").read_text(encoding="utf-8").lower(),
                f"missing central scope rule {token}")

def verify_sources(d: dict, src23: Path | None, src24: Path | None,
                   *, require_external: bool) -> None:
    if require_external:
        req(src23 is not None and src24 is not None, "missing pinned D.P23/D.P24 worktrees")
    sources = {"D.P20": ROOT, "D.P21": ROOT, "D.P22": ROOT,
               "D.P23": src23, "D.P24": src24}
    catalog = {}
    for phase, worktree in sources.items():
        if worktree is None:
            print(f"WARNING {phase}: external Draft PR not present; only pinned provenance checked")
            continue
        manifest = read(worktree / TERR_REL / "Datos operativos" / SOURCE_FILES[phase])
        rows = manifest[SOURCE_ARRAY[phase]]
        expected_count = d["sourceCatalog"]["byPhase"][phase]
        req(len(rows) == expected_count, f"{phase}: source biography count changed")
        for row in rows:
            req(row["id"] not in catalog, f"duplicate source ID: {row['id']}")
            catalog[row["id"]] = (phase, row["name"])
    for p in d["people"]:
        if p["sourcePhase"] in sources and sources[p["sourcePhase"]] is None:
            continue
        req(catalog.get(p["sourceBiographyId"]) == (p["sourcePhase"], p["editorialName"]),
            f"source mismatch or deleted biography: {p['sourceBiographyId']}")
    if require_external:
        req(len(catalog) == 52, "cross-source total does not match 52")
    print(f"Source biography verification: {len(catalog)} present, external required={require_external}")

def mutations(d: dict) -> int:
    cases = []
    def add(label, edit):
        cases.append((label, edit))
    add("phase", lambda x: x.update(phase="D.P26"))
    add("merge", lambda x: x["approval"].update(mergeAuthorized=True))
    add("missing dependency", lambda x: x["dependencies"].pop())
    add("false merged source", lambda x: x["dependencies"][0].update(mergedIntoBranch=True))
    add("wrong upstream HEAD", lambda x: x["dependencies"][1].update(expectedHeadAtStart="bad"))
    add("extra city", lambda x: x["inheritedCanon"]["cities"].append("karsath"))
    add("royal navy misused", lambda x: x["inheritedCanon"].update(syvarisNavy="DAROVAN"))
    add("ferry", lambda x: x["inheritedCanon"].update(arvenSyvarisFerryExists=True))
    add("road", lambda x: x["inheritedCanon"]["verifiedNewTransportRoutes"].append("imaginary"))
    add("customs", lambda x: x["inheritedCanon"].update(noInternalCustoms=False))
    add("La Vena", lambda x: x["inheritedCanon"].update(treihordLaVenaPublicAccess=True))
    add("mint", lambda x: x["inheritedCanon"].update(treihordMint=True))
    add("changed river", lambda x: x["inheritedCanon"].update(treihordRiver="Eshneva"))
    add("Arven deforestation", lambda x: x["inheritedCanon"].update(arvenMantoVerdePercentApprox=20))
    add("runtime npc", lambda x: x["runtime"].update(newNpcs=1))
    add("merge verified prematurely", lambda x: x["verification"].update(mergeNeedsSeparateAuthorization=False))
    add("duplicate person", lambda x: x["people"][1].update(sourceBiographyId="TRH-N01"))
    add("short scene list", lambda x: x["testOnlyScenes"].pop())
    add("unknown invented", lambda x: x["lockedUnknowns"].update(npcCoordinates=[0,0]))
    add("wrong source scope", lambda x: x["sourceCatalog"].update(biographiesTotal=27))
    add("invalid source person", lambda x: x["people"][0].update(editorialName="Otro"))
    add("duplicate edge", lambda x: x["relationships"][1].update(personRefs=x["relationships"][0]["personRefs"][:]))
    add("unselected actor", lambda x: x["relationships"][0].update(personRefs=["TRH-N02","TRH-N01"]))
    add("unrecognized conflict link", lambda x: x["conflicts"][0].update(relationshipIdeaRefs=["DP25-R99","DP25-R01"]))
    add("invalid trigger", lambda x: x["conflicts"][0].update(triggersRequired=["unverified"]))
    add("scene wrong conflict", lambda x: x["testOnlyScenes"][0].update(linkedConflictRef="DP25-C02"))
    for i in range(27):
        add(f"materialized NPC {i}", lambda x, i=i: x["people"][i].update(personEntityId="npc"))
    for i in range(30):
        add(f"active relation {i}", lambda x, i=i: x["relationships"][i].update(active=True))
    for i in range(10):
        add(f"active conflict {i}", lambda x, i=i: x["conflicts"][i].update(activated=True))
    for i in range(10):
        add(f"executed test scene {i}", lambda x, i=i: x["testOnlyScenes"][i].update(worldStateChanged=True))
    for i in range(4):
        add(f"fabricated kinship {i}", lambda x, i=i: x["householdCareModels"][i].update(kinshipEstablished=True))
    for i in range(8):
        add(f"unauthorized delegated merge {i}", lambda x, i=i: x["delegatedDecisions"][i].update(grantsMergeAuthority=True))
    for name, edit in cases:
        mutated = copy.deepcopy(d)
        edit(mutated)
        try:
            validate(mutated)
        except (AssertionError, KeyError, TypeError, IndexError):
            continue
        raise AssertionError(f"UNDETECTED ADVERSARIAL MUTATION: {name}")
    return len(cases)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dp23", type=Path)
    parser.add_argument("--source-dp24", type=Path)
    parser.add_argument("--require-external", action="store_true")
    args = parser.parse_args()
    data = read(ROOT / DATA_REL)
    validate(data, docs=True)
    verify_sources(data, args.source_dp23, args.source_dp24,
                   require_external=args.require_external)
    total = mutations(data)
    print(f"PASS D.P25: 27 protagonists, 30 links, 4 care models, "
          f"10 conditional conflicts, 10 TEST_ONLY scenes, 8 decisions, "
          f"{len(UNKNOWN_KEYS)} UNKNOWN fields, {total} adversarial mutations rejected.")
    print("Editorial only: zero active NPC, families, conflicts, quests or world mutations.")

if __name__ == "__main__":
    main()

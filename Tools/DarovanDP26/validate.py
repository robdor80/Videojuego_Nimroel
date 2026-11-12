#!/usr/bin/env python3
"""D.P26: auditoría cruzada editorial de Casa Darovan (NO RUNTIME).

Cruza las fuentes reales de D.P20–D.P25 y rechaza cambios de canon,
activaciones artificiales, referencias huérfanas y cierres administrativos falsos.
Funciona offline, siempre que los checkouts de las PR externas estén presentes.
"""
from __future__ import annotations

import argparse
import copy
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TERR = Path("Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Territorios/Casa Darovan")
DATA = TERR / "Datos operativos"
DOC = ROOT / TERR / "Profundizacion_2026" / "D.P26"
MANIFEST = ROOT / DATA / "darovan_dp26_cierre_editorial_v0.1.json"
T = {
    "D.P20": ("darovan_dp20_veldora_proposals_v0.1.json", "proposedPeople", 10, "VEL-N"),
    "D.P21": ("darovan_dp21_taramin_proposals_v0.1.json", "proposedPeople", 10, "TAR-N"),
    "D.P22": ("darovan_dp22_syvaris_proposals_v0.1.json", "proposedPeople", 10, "SYV-N"),
    "D.P23": ("darovan_dp23_treihord_editorial_v0.1.json", "biographyBases", 10, "TRH-N"),
    "D.P24": ("darovan_dp24_rural_editorial_v0.1.json", "biographyBases", 12, "RUR-N"),
}
PINS = {
    "D.P23": (46, "6ee4f4a672a138e29feefb558e41bbf10fbce64e"),
    "D.P24": (47, "b0b14db66f1cf1ca0e9eb27f28cde403e3e16a89"),
    "D.P25": (48, "2288d79ab03ed7d5a7509943ec140d3387b8f76f"),
}


def require(ok: bool, why: str) -> None:
    if not ok:
        raise AssertionError(why)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def unchanged_unknowns(value: dict) -> None:
    require(isinstance(value, dict) and len(value) >= 10, "unknown inventory")
    require(all(x is None for x in value.values()), "an UNKNOWN was invented")


def official_blob(path: Path) -> str:
    # Git tree SHA, not working-tree bytes (CRLF differs on Windows).
    relative = path.relative_to(ROOT).as_posix()
    cmd = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD:" + relative],
        text=True, capture_output=True, check=True)
    return cmd.stdout.strip()


def verify_refs(m: dict, roots: dict[str, Path]) -> dict[str, dict]:
    require(m["schemaVersion"] == 1 and m["phase"] == "D.P26", "metadata")
    require(m["scope"] == "INTEGRAL_EDITORIAL_AUDIT_NOT_RUNTIME", "scope")
    require(m["baseline"]["sha"] == "512434957f248f2513761615a9685ddd6c49c65f", "baseline")
    require(m["canonicalCities"] == ["treihord", "veldora", "taramin", "syvaris"], "four cities")
    require(m["requiredIntegrationPrOrder"] == [46, 47, 48, "D.P26"], "integration order")
    require(len(m["sourcePrPins"]) == 3, "source count")
    for pin, (phase, (pr, sha)) in zip(m["sourcePrPins"], PINS.items()):
        require(pin == {"phase": phase, "pr": pr, "sha": sha,
                        "wasDraftAtAudit": True, "mergedIntoBaseline": False},
                f"source pin changed for {phase}")
    for phase in PINS:
        require(phase in roots and roots[phase].is_dir(), f"{phase}: checkout missing")
    require(m["delivery"] == {
        "editorialSufficient": True,
        "administrativeIntegrationComplete": False,
        "runtimePlayable": False,
        "newWorldStateEntities": 0,
        "activatedNewRelationships": 0,
        "activatedNewConflicts": 0,
        "newQuests": 0,
        "authorAuthorizedMerges": False,
    }, "fake administrative or runtime closure")
    require(m["classification"] == {
        "editorial": "APTO_CON_DEPENDENCIAS",
        "administrative": "PENDING_AUTHOR_AND_SEQUENTIAL_MERGES",
        "runtime": "NOT_IMPLEMENTED_BY_DP26",
    }, "overstated closure")
    require(m["ciRequirements"] == {
        "windows2022": True, "ubuntu2404": True,
        "checkSourceCommits": True, "recheckAfterMerges": True,
        "doesNotProveGodotAndroidRuntime": True,
    }, "CI contract")
    unchanged_unknowns(m["unresolved"])
    merged = m["integrationReconciliation"]
    require(merged["status"] == "UPSTREAM_PRS_MERGED_AND_VERIFIED_IN_MAIN"
            and merged["verifiedDate"] == "2026-11-12"
            and merged["mainAfterDP25"] == "50e2412dc2160b3bb5bf5abef0d04382160807d2"
            and merged["allManifestBlobsIdenticalToPinnedSources"] is True
            and merged["dp26MergeStatusAtAttestation"] == "AWAITING_PR49_MERGE"
            and merged["finalPostMergeCiRequired"] is True
            and merged["runtimeStillNotIntegrated"] is True,
            "merged upstream attestation or PR49 state")
    merged_sources = [
        (46, "D.P23", "dcb2bb8939ee6f62ca89ca926ea1f4afbf75dab0",
         "darovan_dp23_treihord_editorial_v0.1.json",
         "0f6f2ecad7cbbd9adeb4290e15df6ed25b2b5d6b"),
        (47, "D.P24", "21712c17d1369f4979a518247ec040f44c529ab9",
         "darovan_dp24_rural_editorial_v0.1.json",
         "5a2c41e07c654ef15f751dd07d3670c0468a3bfc"),
        (48, "D.P25", "50e2412dc2160b3bb5bf5abef0d04382160807d2",
         "darovan_dp25_personajes_relaciones_conflictos_v0.1.json",
         "8fb6ef595138581781a202dcd95d95f56a0dd504"),
    ]
    require(len(merged["upstreamPrMerges"]) == 3, "merged PR count")
    for index, (number, phase, merge_sha, filename, expected_blob) in enumerate(merged_sources):
        require(merged["upstreamPrMerges"][index] == {
            "pr": number, "phase": phase, "mergeCommit": merge_sha,
            "manifestBlobSha": expected_blob,
        }, f"merged PR attestation changed: {number}")
        relative = (DATA / filename).as_posix()
        cmd = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD:" + relative],
            text=True, capture_output=True, check=True)
        require(cmd.stdout.strip() == expected_blob,
                f"main vs pinned source drift: {phase}")
    protected = m["protected"]
    require(protected["arvenUnderDarovan"] and
            protected["belaraContiguousNotCrossingTreihord"] and
            protected["taraminThalenTwoBranchesOneRiver"] and
            protected["syvarisNorgardRoyalNavy"] and
            protected["noDarovanMint"] and protected["laVenaRestricted"] and
            protected["noInternalCustoms"] and protected["noUnverifiedNewRoutes"],
            "protected canon changed")
    require(protected["agujasPermanentInteriorSettlements"] is False,
            "Bosque de las Agujas inhabited by fiat")
    require(m["originalTreihordBlob"] == "cfc1d664ac87e1f1521a79b6299cdf1a71b45de5",
            "Treihord original blob changed in manifest")
    original = ROOT / "Worldbuilding/Reinos/Reinos de los Hombres/Norgard/Ciudades/Casa Darovan/Treihord.md"
    require(official_blob(original) == m["originalTreihordBlob"],
            "the authoritative Treihord manuscript has changed")

    source_people: dict[str, tuple[str, str]] = {}
    source_names: set[str] = set()
    contents: dict[str, dict] = {}
    for phase, (filename, field, count, prefix) in T.items():
        worktree = roots.get(phase, ROOT)
        d = read_json(worktree / DATA / filename)
        require(d["phase"] == phase, f"source phase mismatch: {phase}")
        rows = d[field]
        require(len(rows) == count, f"biography count changed: {phase}")
        require(m["biographies"]["sourcesByPhase"][phase] == count,
                f"manifest biography count changed: {phase}")
        for i, p in enumerate(rows, 1):
            ident = f"{prefix}{i:02d}"
            require(p["id"] == ident and bool(p["name"]), f"source ID: {ident}")
            require(ident not in source_people, f"duplicate source identity {ident}")
            require(p["name"].casefold() not in source_names,
                    f"duplicate biography name {p['name']}")
            source_people[ident] = (phase, p["name"])
            source_names.add(p["name"].casefold())
        contents[phase] = d
    require(len(source_people) == 52 and len(source_names) == 52, "52 unique identities")
    require(m["biographies"]["totalUnique"] == 52 and
            m["biographies"]["selectedByDP25"] == 27 and
            m["biographies"]["notSelected"] == 25, "selection accounting")

    dp23, dp24 = contents["D.P23"], contents["D.P24"]
    canon23 = dp23["canon"]
    require(canon23["originalBlobSha"] == m["originalTreihordBlob"]
            and canon23["originalLines"] == 2374
            and canon23["neighborhoodCount"] == 8
            and canon23["populationApprox"] == 32000
            and canon23["river"] == "Belara"
            and canon23["riverCrossesCity"] is False
            and canon23["hasMint"] is False
            and canon23["laVenaPublicAccess"] is False
            and canon23["riverIndustrialShallowBarges"] is True
            and canon23["royalJusticeAppliesInLaCostra"] is True,
            "Treihord canonical constraints")
    require(len(dp23["neighborhoods"]) == 8
            and len(dp23["futureEstablishments"]) == 12
            and all(not e["created"] for e in dp23["futureEstablishments"])
            and dp23["mergeAuthorized"] is False
            and dp23["createsWorldStateEntities"] is False
            and dp23["coreRpgIntegrated"] is False, "Treihord falsely materialized")
    require(len(dp24["futureCommunities"]) == 9
            and len(dp24["materialChains"]) == 10
            and dp24["merger"]["authorized"] is False
            and dp24["runtime"]["worldStateChanged"] is False
            and dp24["runtime"]["generatedSettlements"] == 0
            and dp24["inheritedCanon"]["arvenMantoVerdeCoverApproxPercent"] == 90
            and dp24["inheritedCanon"]["agujaInteriorPermanentSettlements"] is False
            and dp24["inheritedCanon"]["internalCustomsCreated"] is False,
            "rural canon or materialization")
    for c in dp24["futureCommunities"]:
        require(c["futureObjectiveOnly"] is True and c["instantiated"] is False
                and c["gatesPassed"] is False and c["worldStateEntityId"] is None
                and c["siteId"] is None and c["actualResidentCount"] is None,
                f"unapproved rural instance: {c['id']}")
    d25 = read_json(roots["D.P25"] / DATA /
                    "darovan_dp25_personajes_relaciones_conflictos_v0.1.json")
    require(d25["phase"] == "D.P25" and d25["approval"]["mergeAuthorized"] is False,
            "D.P25 approval changed")
    require(d25["runtime"]["worldStateChanged"] is False
            and d25["runtime"]["newNpcs"] == 0
            and d25["runtime"]["activatedRelationships"] == 0
            and d25["runtime"]["activeConflicts"] == 0
            and d25["runtime"]["realQuests"] == 0, "world state activated")
    require(d25["inheritedCanon"]["noInternalCustoms"] is True
            and d25["inheritedCanon"]["syvarisNavy"] == "ARMADA_REAL_NORGARD"
            and d25["inheritedCanon"]["taraminRiverBranchCount"] == 2
            and d25["inheritedCanon"]["arvenSyvarisFerryExists"] is False
            and d25["inheritedCanon"]["verifiedNewTransportRoutes"] == [],
            "D.P25 invented legal rights or routes")
    unchanged_unknowns(d25["lockedUnknowns"])
    require(len(d25["people"]) == 27 and
            len(d25["relationships"]) == 30 and
            len(d25["conflicts"]) == 10 and
            len(d25["testOnlyScenes"]) == 10,
            "D.P25 counts")
    require(m["proposals"]["namedRuralCommunities"] == 9
            and m["proposals"]["treihordExistingNeighborhoods"] == 8
            and m["proposals"]["proposedRelationships"] == 30
            and m["proposals"]["proposedTerritorialConflicts"] == 10,
            "manifest proposal counts")
    for phase in ("veldora", "taramin", "syvaris"):
        n = m["proposals"][phase + "FutureEstablishments"]
        require(n == 12, "city establishment count")
    require(m["proposals"]["treihordFutureEstablishments"] == 12
            and m["proposals"]["testOnlyDP25Scenes"] == 10, "proposal count")

    selected = set()
    for p in d25["people"]:
        ref = p["sourceBiographyId"]
        require(ref in source_people and ref not in selected, f"source missing or duplicate {ref}")
        require(source_people[ref] == (p["sourcePhase"], p["editorialName"]),
                f"renamed or reassigned character {ref}")
        require(p["personEntityId"] is None and p["householdEntityId"] is None
                and p["npcInstantiated"] is False
                and p["worldStateChanged"] is False
                and p["currentRelationshipIds"] == [], f"NPC instantiated {ref}")
        selected.add(ref)
    require(len(selected) == 27 and len(source_people) - len(selected) == 25,
            "unselected cast removed")

    edges = set()
    edge_ids = set()
    for rel in d25["relationships"]:
        a, b = rel["personRefs"]
        require(a != b and {a, b} <= selected, f"bad relationship endpoint {rel['id']}")
        pair = tuple(sorted((a, b)))
        require(pair not in edges and rel["id"] not in edge_ids,
                f"duplicate relationship {rel['id']}")
        edges.add(pair)
        edge_ids.add(rel["id"])
        require(rel["status"] == "FUTURE_CONDITIONAL_RELATION"
                and rel["active"] is False
                and rel["actorContactsVerified"] is False
                and rel["actualRelationshipId"] is None
                and rel["approvedRouteId"] is None
                and rel["worldStateChanged"] is False,
                f"activated relationship {rel['id']}")
    conflict_ids = set()
    for c in d25["conflicts"]:
        require(c["id"] not in conflict_ids and
                len(c["personRefs"]) >= 2 and set(c["personRefs"]) <= selected and
                len(c["triggersRequired"]) >= 3 and
                set(c["relationshipIdeaRefs"]) <= edge_ids,
                f"invalid conflict {c['id']}")
        conflict_ids.add(c["id"])
        require(c["status"] == "FUTURE_CONDITIONAL_CONFLICT"
                and c["activated"] is False
                and c["triggerSatisfied"] is False
                and c["actualQuestId"] is None
                and c["publicHistoryEventId"] is None
                and c["determinedOutcome"] is None
                and c["worldStateChanged"] is False,
                f"premature conflict {c['id']}")
    for scene in d25["testOnlyScenes"]:
        require(scene["linkedConflictRef"] in conflict_ids
                and scene["status"] == "TEST_ONLY"
                and scene["everOccurred"] is False
                and scene["knowledgeLeaked"] is False
                and scene["realTravelPerformed"] is False
                and scene["inventoryMutation"] is False
                and scene["worldStateChanged"] is False,
                f"scene leaked into real world {scene['id']}")

    for name in ("README.md", "01_auditoria_transversal.md",
                 "02_matriz_dependencias_y_pruebas.md",
                 "03_deuda_real_y_traspaso.md", "04_acta_cierre_editorial.md",
                 "05_reconciliacion_de_fusiones.md"):
        require((DOC / name).is_file(), f"missing D.P26 acta: {name}")
    return {"sourceProfiles": len(source_people), "selected": len(selected),
            "unselected": len(source_people) - len(selected),
            "edges": len(edges), "conflicts": len(conflict_ids)}


def assert_external_shas(roots: dict[str, Path]) -> None:
    for phase, (_, expected) in PINS.items():
        p = roots[phase]
        cmd = subprocess.run(["git", "-C", str(p), "rev-parse", "HEAD"],
                             text=True, capture_output=True, check=True)
        require(cmd.stdout.strip().lower() == expected,
                f"wrong checkout SHA: {phase}")


def negative_tests(m: dict, roots: dict[str, Path]) -> int:
    # Mutaciones de manifiesto que SIEMPRE deben rechazarse.
    cases = [
        ("false_final_closure", ("delivery", "administrativeIntegrationComplete"), True),
        ("playability", ("delivery", "runtimePlayable"), True),
        ("invented_NPC", ("delivery", "newWorldStateEntities"), 1),
        ("active_relations", ("delivery", "activatedNewRelationships"), 1),
        ("active_conflicts", ("delivery", "activatedNewConflicts"), 1),
        ("invented_quest", ("delivery", "newQuests"), 1),
        ("unapproved_merge", ("delivery", "authorAuthorizedMerges"), True),
        ("wrong_pr_order", ("requiredIntegrationPrOrder",), [48, 47, 46, "D.P26"]),
        ("fake_authority", ("protected", "noInternalCustoms"), False),
        ("mint", ("protected", "noDarovanMint"), False),
        ("Agujas", ("protected", "agujasPermanentInteriorSettlements"), True),
        ("wrong_cities", ("canonicalCities",), ["treihord", "veldora"]),
        ("fake_unknown", ("unresolved", "currentDarovanRuler"), "Nuevo señor"),
        ("treihord_changed", ("originalTreihordBlob",), "badsha"),
        ("missing_biography", ("biographies", "totalUnique"), 51),
        ("wrong_selection", ("biographies", "selectedByDP25"), 52),
        ("invented_conflict", ("proposals", "proposedTerritorialConflicts"), 11),
        ("wrong_source", ("sourcePrPins", 0, "sha"), "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
        ("no_windows", ("ciRequirements", "windows2022"), False),
        ("merge_claim", ("classification", "administrative"), "CLOSED"),
        ("wrong_merged_sha", ("integrationReconciliation", "upstreamPrMerges", 1, "manifestBlobSha"), "forged"),
        ("fake_upstream", ("integrationReconciliation", "status"), "UNKNOWN"),
    ]
    passed = 0
    for name, path, replacement in cases:
        candidate = copy.deepcopy(m)
        cur = candidate
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = replacement
        try:
            verify_refs(candidate, roots)
        except AssertionError:
            passed += 1
        else:
            raise AssertionError(f"negative mutation unexpectedly accepted: {name}")
    return passed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dp23", type=Path)
    parser.add_argument("--source-dp24", type=Path)
    parser.add_argument("--source-dp25", type=Path)
    parser.add_argument("--require-external", action="store_true")
    args = parser.parse_args()
    roots = {"D.P20": ROOT, "D.P21": ROOT, "D.P22": ROOT}
    for phase, value in (("D.P23", args.source_dp23),
                         ("D.P24", args.source_dp24),
                         ("D.P25", args.source_dp25)):
        require(value is not None and value.is_dir(),
                f"source checkout for {phase} is required")
        roots[phase] = value.resolve()
    if args.require_external:
        assert_external_shas(roots)
    m = read_json(MANIFEST)
    summary = verify_refs(m, roots)
    negatives = negative_tests(m, roots)
    print("DAROVAN D.P26 STATIC OK: " +
          ", ".join(f"{k}={v}" for k, v in summary.items()) +
          f", negative_mutations_rejected={negatives}; NO RUNTIME / NO MERGE")


if __name__ == "__main__":
    main()

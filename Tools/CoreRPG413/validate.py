"""Validate an installed release offline; optionally re-extract approved authoring sources."""
from __future__ import annotations

import argparse
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from pack import CONTENT, REPO, canonical, check_artifacts, extract, inside, read, sha, MAX_BYTES

PREFIX = "nimroel.treskal.villages:"
KINDS = {PREFIX + "models/v1": "settlement_model",
         PREFIX + "capabilities/basic-blacksmithing": "service_capability",
         PREFIX + "capabilities/local-tavern": "service_capability",
         PREFIX + "objects/ordinary-agricultural-tool": "object_category"}
REQUIRED = {"housing_for_generated_households", "permanent_potable_water_access", "local_production",
            "functional_external_connection", "domestic_productive_auxiliary_space",
            "community_meeting_point", "basic_blacksmithing", "local_tavern"}
OPTIONAL = {"mill", "inn", "carpentry", "cartwright", "trained_healer", "advanced_blacksmith"}
FORBIDDEN = {"perimeter_city_wall", "permanent_local_garrison", "formal_sawmill", "compulsory_inn", "compulsory_mill"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def schema(name, value):
    spec = read(CONTENT / "schemas" / (name + ".schema.json"))
    Draft202012Validator.check_schema(spec)
    Draft202012Validator(spec).validate(value)


def validate_installed(root, core_root):
    """No network or canonical repository needed once pack and schemas are installed.

    Hashes identify a release, not its publisher. The Host must select a trusted
    release; never derive an expected save identity from an unverified replacement.
    """
    root = Path(root)
    lock = read(inside(root, "content-lock.json"))
    schema("content-lock-1", lock)
    files = lock["files"]
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    require(actual == set(files) | {"content-lock.json"}, "unexpected/missing installed file")
    for name, digest in sorted(files.items()):
        path = inside(root, name)
        with path.open("rb") as stream:
            data = stream.read(MAX_BYTES + 1)
        require(len(data) <= MAX_BYTES and sha(data) == digest, f"content hash mismatch: {name}")
    require(sha(canonical(files)) == lock["release_sha256"], "release fingerprint mismatch")
    # Closed local registry. An unknown URI fails resolution; there is no HTTP fallback.
    specs = [read(p) for p in sorted((Path(core_root) / "schemas/content/0.1.0").glob("*.json"))]
    require(len(specs) == 3, "Core 0.1.0 schemas unavailable")
    registry = Registry().with_resources((s["$id"], Resource.from_contents(s)) for s in specs)
    by_id = {s["$id"]: s for s in specs}

    def core_schema(role, value):
        key = "https://robdor80.github.io/CoreRPG/schemas/content/0.1.0/" + role + ".schema.json"
        Draft202012Validator(by_id[key], registry=registry).validate(value)

    manifest = read(inside(root, "manifest.json"))
    core_schema("content-pack-manifest", manifest)
    require(manifest["pack_id"] == lock["pack_id"] and manifest["pack_version"] == lock["pack_version"], "manifest identity mismatch")
    require(manifest["content_contract_version"] == "0.1.0" and manifest["minimum_core_version"] == "0.1.0", "incompatible Core contract")
    require(manifest["dependencies"] == [], "nonexistent physical dependencies")
    require(set(manifest["resources"]) == {p for p in files if p.startswith("resources/")}, "unindexed resource")
    definitions = {}
    for name in manifest["resources"]:
        entry = read(inside(root, name))
        core_schema("resource-definition", entry)
        require(entry["id"] not in definitions, "duplicate definition")
        definitions[entry["id"]] = entry
    require({key: d["kind"] for key, d in definitions.items()} == KINDS, "wrong definition set or kinds")
    for entry in definitions.values():
        for ref in entry["references"]:
            require(ref["target"] in definitions, "missing reference")
            require(definitions[ref["target"]]["kind"] == ref["expected_kind"], "reference type mismatch")
    expected_refs = {
        PREFIX + "models/v1": {PREFIX + "capabilities/basic-blacksmithing", PREFIX + "capabilities/local-tavern"},
        PREFIX + "objects/ordinary-agricultural-tool": {PREFIX + "capabilities/basic-blacksmithing"}}
    for key, d in definitions.items():
        require({r["target"] for r in d["references"]} == expected_refs.get(key, set()), "wrong structural references")
    identity = [{"id": key, "kind": d["kind"]} for key, d in sorted(definitions.items())]
    require(sha(canonical(identity)) == lock["definition_set_sha256"], "definition identity fingerprint mismatch")
    profile = read(inside(root, "nimroel/model-v1.json"))
    schema("village-model-1", profile)
    require(profile["population"]["generalCanonicalRange"] == [35, 100], "Pueblo or invalid village population")
    require(profile["population"]["v001TargetRange"] == [40, 60], "invalid V001 range")
    require(set(profile["required_capabilities"]) == REQUIRED, "mandatory village capability missing")
    require(set(profile["optional_services"]) == OPTIONAL, "optional service promoted/lost")
    require(set(profile["forbidden_defaults"]) == FORBIDDEN, "forbidden default lost")
    require(set(profile["activities"]) == {"local_agriculture", "some_livestock", "visible_timber_haulage_road_influence"}, "V1 activities changed")
    provenance = read(inside(root, "provenance.json"))
    schema("provenance-1", provenance)
    source_paths = [s["path"] for s in provenance["sources"]["sources"]]
    require(len(source_paths) == len(set(source_paths)), "duplicate source path")
    for name in source_paths:
        inside(CONTENT, name)  # syntax/confinement only, not an installed source lookup
    for field in provenance["profile_fields"].values():
        require(field["source"] in source_paths and field["pointer"].startswith("/"), "unlocked profile source")
    mappings = provenance["definitions"]
    require({m["definition_id"] for m in mappings} == set(definitions), "missing provenance")
    for m in mappings:
        require(m["source"] in source_paths, "unlocked source")
        require(read(inside(root, m["resource"]))["id"] == m["definition_id"], "ambiguous provenance")
    fixture = read(inside(root, "integration-fixture.json"))
    schema("integration-fixture-1", fixture)
    require(fixture["materialized"] == 2 and fixture["max_batch"] == 2,
            "this structural fixture supports exactly two anonymous observers")
    require(int(fixture["world_seed"]) <= 2**64 - 1 and int(fixture["rng_probe_stream"]) <= 2**64 - 1, "uint64 overflow")
    region = fixture["region"]
    require(fixture["stable_settlement_id"] in region["nodes"], "unknown settlement in regional fixture")
    edge = region["edges"][0]
    require(edge["source"] == fixture["stable_settlement_id"] and edge["target"] in region["nodes"] and edge["source"] != edge["target"], "no functional external connection")
    return lock


def save_identity(lock):
    """Host metadata outside CRPGSAVE. Exact matching only; no implicit migration."""
    return {key: lock[key] for key in ("pack_id", "pack_version", "definition_set_sha256", "release_sha256")}


def require_compatible(saved, installed_lock):
    require(saved == save_identity(installed_lock), "content incompatible; explicit migration required")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", type=Path, default=CONTENT / "pack")
    parser.add_argument("--core-root", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, default=REPO)
    parser.add_argument("--installed-only", action="store_true")
    args = parser.parse_args()
    lock = validate_installed(args.pack, args.core_root)
    if not args.installed_only:
        check_artifacts(args.pack, extract(args.source_root))
    print("OK: schema, canon, provenance, hashes; " + lock["release_sha256"])


if __name__ == "__main__":
    main()

"""Offline authoring projection. Canon stays in the locked Worldbuilding sources."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CONTENT = REPO / "ContentPacks/treskal-villages"
CORE_SCHEMA = "https://robdor80.github.io/CoreRPG/schemas/content/0.1.0/"
MAX_BYTES = 1024 * 1024  # Tooling budget, not a lore rule.


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def read(path):
    with Path(path).open("rb") as stream:
        data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES or data.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"oversized document or BOM: {path}")
    return json.loads(data.decode("utf-8"), object_pairs_hook=unique_object,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def inside(root, relative):
    path = PurePosixPath(relative)
    if (not relative or path.is_absolute() or "\\" in relative or ":" in relative
            or any(p in ("", ".", "..") for p in relative.split("/"))):
        raise ValueError(f"invalid relative locator: {relative}")
    result = (Path(root) / relative).resolve()
    if not result.is_relative_to(Path(root).resolve()):
        raise ValueError(f"path escape: {relative}")
    return result


def pointer(document, path):
    if not path.startswith("/"):
        raise ValueError(f"invalid JSON pointer: {path}")
    for token in path[1:].split("/"):
        key = token.replace("~1", "/").replace("~0", "~")
        document = document[int(key)] if isinstance(document, list) else document[key]
    return document


def verify_sources(root, lock):
    seen = set()
    for entry in lock["sources"]:
        name = entry["path"]
        if name in seen:
            raise ValueError(f"duplicate source: {name}")
        seen.add(name)
        path = inside(root, name)
        # These bounded authoring sources include Markdown as well as JSON.
        with path.open("rb") as stream:
            data = stream.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES or sha(data) != entry["sha256"]:
            raise ValueError(f"source differs from approved revision: {name}")


def extract(root=REPO, selection=None, source_lock=None, fixture=None):
    selection = read(CONTENT / "authoring/selection.json") if selection is None else selection
    source_lock = read(CONTENT / "authoring/source-lock.json") if source_lock is None else source_lock
    fixture = read(CONTENT / "fixtures/v001.json") if fixture is None else fixture
    verify_sources(root, source_lock)
    sources = {s["path"] for s in source_lock["sources"]}
    if selection["handoff"] not in sources:
        raise ValueError("handoff not locked")
    handoff = read(inside(root, selection["handoff"]))
    if handoff["isCoreRpgContentPack"] or handoff["documentRole"] != "authoring_handoff_and_test_contract":
        raise ValueError("wrong handoff role")
    artifacts = {}
    definitions = sorted(selection["definitions"], key=lambda d: d["id"])
    mapping = []
    for entry in definitions:
        if entry["source"] not in sources:
            raise ValueError("definition source not locked")
        source = inside(root, entry["source"])
        if entry["pointer"].startswith("/"):
            pointer(read(source), entry["pointer"])
        elif entry["pointer"] not in source.read_text(encoding="utf-8"):
            raise ValueError("Markdown anchor missing")
        local = entry["id"].split(":", 1)[1]
        locator = "resources/" + local + ".json"
        inside(CONTENT, locator)  # reject escaping authoring paths before output
        artifacts[locator] = canonical({"$schema": CORE_SCHEMA + "resource-definition.schema.json",
                                       "id": entry["id"], "kind": entry["kind"],
                                       "references": sorted(entry["references"],
                                                            key=lambda r: (r["target"], r["expected_kind"]))})
        mapping.append({"definition_id": entry["id"], "resource": locator,
                        "source": entry["source"], "pointer": entry["pointer"]})
    if len(artifacts) != len(definitions):
        raise ValueError("duplicate definition or locator")
    artifacts["manifest.json"] = canonical({"$schema": CORE_SCHEMA + "content-pack-manifest.schema.json",
        "pack_id": selection["pack_id"], "pack_version": selection["pack_version"],
        "content_contract_version": "0.1.0", "minimum_core_version": "0.1.0",
        "dependencies": [], "resources": sorted(artifacts),
        "display_name": "Aldeas de Treskal — modelo V1",
        "description": "Modelo rural mixto maderero-agrícola. No instancia Treskal ciudad."})
    fields = {"population": "/generation/population", "required_capabilities": "/generation/mandatoryCapabilities",
              "activities": "/generation/v1ActivityTags", "optional_services": "/generation/optionalServicesNotForced",
              "forbidden_defaults": "/generation/forbiddenDefaults", "quest_object_category": "/quest/objectType",
              "deferred": "/deferredToImplementation"}
    profile = {"schema_version": 1, "model_definition": selection["pack_id"] + ":models/v1",
               "scope": handoff["testLocation"], "rules_status": "approved_v001_scope_model_still_in_development"}
    profile.update({key: pointer(handoff, path) for key, path in fields.items()})
    artifacts["nimroel/model-v1.json"] = canonical(profile)
    artifacts["provenance.json"] = canonical({"schema_version": 1, "sources": source_lock,
        "selection_sha256": sha(canonical(selection)), "definitions": mapping,
        "profile_fields": {key: {"source": selection["handoff"], "pointer": path}
                           for key, path in fields.items()},
        "inheritance_is_documentary_not_pack_dependencies": True})
    artifacts["integration-fixture.json"] = canonical(fixture)
    files = {name: sha(data) for name, data in sorted(artifacts.items())}
    identity = [{"id": d["id"], "kind": d["kind"]} for d in definitions]
    # Explicit byte algorithm: SHA-256 of UTF-8, sorted keys, indent=2, LF + final LF.
    lock = {"schema_version": 1, "pack_id": selection["pack_id"], "pack_version": selection["pack_version"],
            "definition_set_sha256": sha(canonical(identity)), "release_sha256": sha(canonical(files)),
            "files": files}
    artifacts["content-lock.json"] = canonical(lock)
    return artifacts


def check_artifacts(output, artifacts):
    expected = set(artifacts)
    actual = {p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()}
    if actual != expected:
        raise ValueError(f"artifact inventory differs: {sorted(actual ^ expected)}")
    for name, data in artifacts.items():
        if inside(output, name).read_bytes() != data:
            raise ValueError(f"non-reproducible artifact: {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=REPO)
    parser.add_argument("--output", type=Path, default=CONTENT / "pack")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    artifacts = extract(args.source_root)
    if args.check:
        check_artifacts(args.output, artifacts)
    else:
        # Build/validate all data first. Write only to a new directory, never patch a release.
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in artifacts.items():
            path = inside(args.output, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f"OK: {len(artifacts)} reproducible files")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""NIM-08 static contract checks. Never claims an executable world or V001 PASS."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "Docs" / "NIM-08-19"
PHASE = BASE / "NIM-08" / "contracts"
CANON = (ROOT / "Worldbuilding" / "Reinos" / "Reinos de los Hombres" /
         "Norgard" / "Territorios" / "Casa Valrik" / "Aldeas" /
         "03_Prueba_v0.0.1" / "MATRIZ_ACEPTACION_V001_v0.1.md")
EXPECTED = {f"V001-{group}{n:02d}" for group, count in
            (("G", 6), ("P", 4), ("Q", 8), ("S", 6), ("H", 4))
            for n in range(1, count + 1)}
PATTERN = re.compile(r"\bV001-[GPQSH]\d{2}\b")


class ContractFailure(ValueError):
    """Invalid document or unsupported in-repo design contract."""


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_ids() -> dict[str, int]:
    observed: dict[str, set[str]] = {}
    for name, path in (
        ("canonical", CANON),
        ("planning", BASE / "02_MATRIZ_TRAZABILIDAD_V001.md"),
    ):
        found = set(PATTERN.findall(path.read_text(encoding="utf-8")))
        if found != EXPECTED:
            raise ContractFailure(f"{name}: IDs missing={sorted(EXPECTED - found)}, unexpected={sorted(found - EXPECTED)}")
        observed[name] = found
    planning = (BASE / "02_MATRIZ_TRAZABILIDAD_V001.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*(V001-[GPQSH]\d{2})\s*\|.*\|\s*([A-Z_]+)\s*\|\s*$",
                      planning, flags=re.MULTILINE)
    if len(rows) != 28 or {r[0] for r in rows} != EXPECTED:
        raise ContractFailure("Planning table lacks exactly 28 rows")
    if any(status != "PENDIENTE" for _, status in rows):
        raise ContractFailure("NIM-08 may not change V001 acceptance statuses")
    return {group: len([x for x in EXPECTED if x.startswith("V001-" + group)])
            for group in "GPQSH"}


def _resolve(ref: str, root_schema: dict) -> dict:
    if not ref.startswith("#/$defs/"):
        raise ContractFailure(f"External or unsupported schema reference: {ref}")
    try:
        return root_schema["$defs"][ref.removeprefix("#/$defs/")]
    except KeyError as exc:
        raise ContractFailure(f"Broken local schema ref: {ref}") from exc


def check_schema_structure(schema: dict) -> None:
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ContractFailure("Unsupported schema dialect")
    if not str(schema.get("$id", "")).endswith(".schema.json"):
        raise ContractFailure("Schema must have a stable versioned $id")

    def walk(node: Any) -> None:
        if isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            if "$ref" in node:
                _resolve(node["$ref"], schema)
            if "pattern" in node:
                re.compile(node["pattern"])
            if node.get("type") == "object":
                props = node.get("properties", {})
                if node.get("additionalProperties") is False and not props:
                    raise ContractFailure("Closed object without properties")
                if set(node.get("required", [])) - set(props):
                    raise ContractFailure("Required properties missing from schema")
            for item in node.values():
                walk(item)
    walk(schema)


def _is_type(value: Any, type_name: str) -> bool:
    return {
        "object": lambda: isinstance(value, dict),
        "array": lambda: isinstance(value, list),
        "string": lambda: isinstance(value, str),
        "integer": lambda: isinstance(value, int) and not isinstance(value, bool),
        "boolean": lambda: isinstance(value, bool),
        "null": lambda: value is None,
    }[type_name]()


def validate(value: Any, schema: dict, root_schema: dict | None = None, path: str = "$") -> None:
    """Strict deterministic validator for ONLY the JSON Schema keywords used in NIM-08.
    This is not a general JSON Schema interpreter; NIM-09 must choose/full-test one."""
    if root_schema is None:
        root_schema = schema
    if "$ref" in schema:
        return validate(value, _resolve(schema["$ref"], root_schema), root_schema, path)
    for keyword, mode in (("oneOf", 1), ("anyOf", None)):
        if keyword in schema:
            successes = 0
            for branch in schema[keyword]:
                try:
                    validate(value, branch, root_schema, path)
                except ContractFailure:
                    continue
                successes += 1
            if (mode == 1 and successes != 1) or (mode is None and successes < 1):
                raise ContractFailure(f"{path}: {keyword} validation failed")
            return
    if "const" in schema and value != schema["const"]:
        raise ContractFailure(f"{path}: const differs")
    if "enum" in schema and value not in schema["enum"]:
        raise ContractFailure(f"{path}: enum differs")
    if "type" in schema:
        types = schema["type"]
        if isinstance(types, str):
            types = [types]
        if not any(_is_type(value, t) for t in types):
            raise ContractFailure(f"{path}: wrong type")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0) or len(value) > schema.get("maxLength", 2**31):
            raise ContractFailure(f"{path}: string length")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            raise ContractFailure(f"{path}: string pattern")
    if isinstance(value, int) and not isinstance(value, bool):
        if value < schema.get("minimum", -2**63) or value > schema.get("maximum", 2**63):
            raise ContractFailure(f"{path}: numeric range")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", 2**31):
            raise ContractFailure(f"{path}: list size")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            raise ContractFailure(f"{path}: list duplicates")
        if "items" in schema:
            for i, item in enumerate(value):
                validate(item, schema["items"], root_schema, f"{path}[{i}]")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        if set(schema.get("required", [])) - set(value):
            raise ContractFailure(f"{path}: required keys missing")
        for key, item in value.items():
            if key in props:
                validate(item, props[key], root_schema, path + "." + key)
            elif schema.get("additionalProperties") is False:
                raise ContractFailure(f"{path}: unexpected key {key}")
            elif isinstance(schema.get("additionalProperties"), dict):
                validate(item, schema["additionalProperties"], root_schema, path + "." + key)


def assert_provenance(example: dict) -> None:
    lock_path = ROOT / example["source_lock"]["path"]
    lock_bytes = lock_path.read_bytes()
    git_digest = hashlib.sha1(b"blob " + str(len(lock_bytes)).encode("ascii") + b"\x00" + lock_bytes).hexdigest()
    if git_digest != example["source_lock"]["git_blob_sha"]:
        raise ContractFailure("source-lock changed; baseline Git blob SHA does not match")
    lock = json.loads(lock_bytes)
    if lock["revision"] != example["source_lock"]["revision"]:
        raise ContractFailure("source-lock revision mismatch")
    pack = load_json(ROOT / "ContentPacks/treskal-villages/pack/manifest.json")
    expected = example["content_pack"]
    if any([pack["pack_id"] != expected["id"],
            pack["pack_version"] != expected["version"],
            pack["content_contract_version"] != expected["contract_version"]]):
        raise ContractFailure("Pack ID/version/contract mismatch")
    content_lock = load_json(ROOT / "ContentPacks/treskal-villages/pack/content-lock.json")
    if content_lock["release_sha256"] != expected["release_sha256"]:
        raise ContractFailure("Pack release hash mismatch")
    pins = (ROOT / "Game/BridgeCoreRPG/cmake/dependencies.cmake").read_text(encoding="utf-8")
    if "GIT_TAG " + example["runtime"]["corerpg_pin"] not in pins:
        raise ContractFailure("Nimroel pinned CoreRPG has moved")
    if example["stage"] != "DESIGN_ONLY":
        raise ContractFailure("A technical fixture must not assert operability")


def run_checks() -> dict:
    counts = assert_ids()
    schemas = [
        "generation-manifest-0.1.0.schema.json",
        "world-instance-0.1.0.schema.json",
        "action-envelope-0.1.0.schema.json",
    ]
    for filename in schemas:
        check_schema_structure(load_json(PHASE / filename))
    manifest = load_json(PHASE / "technical-manifest-example.json")
    validate(manifest, load_json(PHASE / schemas[0]))
    assert_provenance(manifest)
    return {"result": "PASS_STATIC_ONLY", "canonical_ids": sum(counts.values()),
            "groups": counts, "schemas": schemas, "provenance": "git_blob_sha+pack_release+pin verified",
            "v001_behavioural_pass": 0, "physical_pass": 0}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = run_checks()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    else:
        print("NIM08 static PASS (NOT V001 behavioural PASS):", report)


if __name__ == "__main__":
    main()

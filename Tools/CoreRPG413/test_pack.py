import copy
import os
from pathlib import Path
import shutil
import tempfile
import unittest

from jsonschema import ValidationError

import pack
import validate

CORE = Path(os.environ.get("CORERPG_SOURCE_DIR", pack.REPO.parent / "CoreRPG"))


class PackTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "pack"
        shutil.copytree(pack.CONTENT / "pack", self.root)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, value):
        (self.root / name).write_bytes(pack.canonical(value))

    def alter(self, name, change):
        value = pack.read(self.root / name)
        change(value)
        self.write(name, value)
        self.rehash()

    def rehash(self):
        # Recompute transport checksums to ensure semantic tests reach validation.
        lock = pack.read(self.root / "content-lock.json")
        lock["files"] = {k: pack.sha((self.root / k).read_bytes()) for k in lock["files"]}
        lock["release_sha256"] = pack.sha(pack.canonical(lock["files"]))
        self.write("content-lock.json", lock)

    def reject(self):
        with self.assertRaises((ValueError, ValidationError, FileNotFoundError)):
            validate.validate_installed(self.root, CORE)

    def test_real_release_and_repeated_extraction_are_exact(self):
        validate.validate_installed(self.root, CORE)
        first = pack.extract()
        self.assertEqual(first, pack.extract())
        pack.check_artifacts(self.root, first)

    def test_installed_release_needs_no_worldbuilding_sources(self):
        # The release validator does not open source-root or access the network.
        lock = validate.validate_installed(self.root, CORE)
        validate.require_compatible(validate.save_identity(lock), lock)

    def test_corrupt_bytes(self):
        with (self.root / "manifest.json").open("ab") as stream:
            stream.write(b"x")
        self.reject()

    def test_missing_resource(self):
        (self.root / "resources/models/v1.json").unlink()
        self.reject()

    def test_unindexed_resource(self):
        self.write("resources/extra.json", {})
        self.reject()

    def test_duplicate_json_keys(self):
        (self.root / "resources/models/v1.json").write_text('{"id":"a","id":"b"}')
        self.rehash()
        self.reject()

    def test_unknown_payload_rejected_by_original_contract(self):
        self.alter("resources/models/v1.json", lambda d: d.update(data={"population": 50}))
        self.reject()

    def test_duplicate_definition(self):
        self.alter("resources/objects/ordinary-agricultural-tool.json",
                   lambda d: d.update(id=validate.PREFIX + "models/v1"))
        self.reject()

    def test_reference_missing_wrong_kind_and_duplicate(self):
        path = "resources/models/v1.json"
        original = (self.root / path).read_bytes()
        for mode in ("missing", "kind", "duplicate"):
            with self.subTest(mode=mode):
                (self.root / path).write_bytes(original)
                def change(d):
                    if mode == "missing":
                        d["references"][0]["target"] = validate.PREFIX + "missing"
                    elif mode == "kind":
                        d["references"][0]["expected_kind"] = "object_category"
                    else:
                        d["references"].append(copy.deepcopy(d["references"][0]))
                self.alter(path, change)
                self.reject()

    def test_incompatible_versions_dependencies_and_wrong_schema(self):
        path = "manifest.json"
        original = (self.root / path).read_bytes()
        mutations = [lambda d: d.update(content_contract_version="0.2.0"),
                     lambda d: d.update(minimum_core_version="99.0.0"),
                     lambda d: d.update(pack_version="0.1.1"),
                     lambda d: d.update(dependencies=[{"pack_id": "nimroel.core", "version_requirement": {"minimum_inclusive": "0.1.0"}}]),
                     lambda d: d.update({"$schema": "https://unregistered.invalid/schema"})]
        for mutation in mutations:
            (self.root / path).write_bytes(original)
            self.alter(path, mutation)
            self.reject()

    def test_pueblo_population_not_inherited(self):
        self.alter("nimroel/model-v1.json", lambda d: d["population"].update(generalCanonicalRange=[350, 900]))
        self.reject()

    def test_required_optional_forbidden_and_activity_invariants(self):
        path = "nimroel/model-v1.json"
        original = (self.root / path).read_bytes()
        for field in ("required_capabilities", "optional_services", "forbidden_defaults", "activities"):
            (self.root / path).write_bytes(original)
            self.alter(path, lambda d: d[field].pop())
            self.reject()

    def test_fixture_out_of_range_budget_overflow_and_no_exit(self):
        path = "integration-fixture.json"
        original = (self.root / path).read_bytes()
        changes = [lambda d: d.update(population=61), lambda d: d.update(materialized=51),
                   lambda d: d.update(world_seed=str(2**64)),
                   lambda d: d["region"]["edges"][0].update(target=d["stable_settlement_id"]),
                   lambda d: d.update(generator_version="future-generator-2")]
        for change in changes:
            (self.root / path).write_bytes(original)
            self.alter(path, change)
            self.reject()

    def test_save_identity_rejects_every_changed_axis(self):
        lock = validate.validate_installed(self.root, CORE)
        saved = validate.save_identity(lock)
        for key in saved:
            changed = dict(saved)
            changed[key] += "different"
            with self.assertRaises(ValueError):
                validate.require_compatible(changed, lock)
        with self.assertRaises(ValueError):
            validate.require_compatible({}, lock)

    def test_source_missing_changed_or_unlocked(self):
        lock = pack.read(pack.CONTENT / "authoring/source-lock.json")
        sources = Path(self.temp.name) / "sources"
        for entry in lock["sources"]:
            path = sources / entry["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pack.REPO / entry["path"], path)
        target = sources / lock["sources"][0]["path"]
        target.unlink()
        with self.assertRaises(FileNotFoundError):
            pack.extract(sources)
        target.write_text("corrupt")
        with self.assertRaises(ValueError):
            pack.extract(sources)
        selection = pack.read(pack.CONTENT / "authoring/selection.json")
        selection["definitions"][0]["source"] = "not-approved.json"
        with self.assertRaises(ValueError):
            pack.extract(selection=selection)

    def test_no_paths_escape_or_absolute_or_backslash(self):
        for path in ("../escape", "/absolute", "a\\b", "a/./b", "a//b", "C:/b"):
            with self.assertRaises(ValueError):
                pack.inside(self.root, path)
        outside = Path(self.temp.name) / "outside.json"
        outside.write_text("{}")
        link = self.root / "escape.json"
        try:
            link.symlink_to(outside)
        except OSError:
            self.skipTest("symlinks unavailable on this Host")
        with self.assertRaises(ValueError):
            pack.inside(self.root, "escape.json")

    def test_document_bom_size_and_nonstandard_constants(self):
        for data in (b"\xef\xbb\xbf{}", b" " * (pack.MAX_BYTES + 1), b'{"x":NaN}'):
            path = Path(self.temp.name) / "bad.json"
            path.write_bytes(data)
            with self.assertRaises(ValueError):
                pack.read(path)

    def test_authoring_check_rejects_semantically_equal_noncanonical_bytes(self):
        with (self.root / "manifest.json").open("ab") as stream:
            stream.write(b"\n")
        with self.assertRaises(ValueError):
            pack.check_artifacts(self.root, pack.extract())


if __name__ == "__main__":
    unittest.main()

"""Stage the one trusted V001 release. Generated transport, never authoring data."""
import argparse
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'Tools/CoreRPG413'))
from pack import CONTENT, check_artifacts, extract
from validate import validate_installed

# Project trust decision; a self-consistent replacement lock is insufficient.
LOCK_SHA256 = '669891e25821b36a431d0af940aed02c4d40be6b6972cd9466179b686a2cc370'
DESTINATION = ROOT / 'Game/Host2D/generated_content/treskal-v001'


def validate(root, core_root=None):
    if hashlib.sha256((root / 'content-lock.json').read_bytes()).hexdigest() != LOCK_SHA256:
        raise ValueError('untrusted V001 publication')
    return validate_installed(root, core_root)


def stage(core_root=None):
    source = CONTENT / 'pack'
    lock = validate(source, core_root)
    check_artifacts(source, extract())
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=DESTINATION.parent) as temporary:
        candidate = Path(temporary) / 'pack'
        candidate.mkdir()
        for name in sorted(set(lock['files']) | {'content-lock.json'}):
            target = candidate / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, target)
        validate(candidate, core_root)
        if DESTINATION.exists():
            shutil.rmtree(DESTINATION)
        shutil.copytree(candidate, DESTINATION)
    validate(DESTINATION, core_root)
    print('V001 staged: 9 identical files; ' + lock['release_sha256'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core-root', type=Path)
    args = parser.parse_args()
    stage(args.core_root)

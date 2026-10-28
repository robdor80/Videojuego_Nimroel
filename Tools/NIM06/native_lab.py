"""Reproducible native lab driver. Run from any directory; no workstation paths."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import struct
import subprocess
import urllib.request
import zipfile
import tempfile

ROOT = Path(__file__).resolve().parents[2]
LAB = ROOT / 'Game/BridgeCoreRPG/lab'
PROJECT = LAB / 'project'
CACHE = ROOT / 'Tools/NIM06/.cache'
EVIDENCE = ROOT / 'Tools/NIM06/evidence'
VERSION = '4.7.2-stable'
NDK = '29.0.14206865'
FUNCTIONAL = False
SOURCE = LAB
NAME = 'nimroel_core_lab'
ENTRY = 'nimroel_core_lab_init'
ASSETS = {
    'windows': ('Godot_v4.7.2-stable_win64.exe.zip', '731980f9608d61333e5baf54a2ef17210acc7a538446c0cb9969f002aca1e953'),
    'linux': ('Godot_v4.7.2-stable_linux.x86_64.zip', 'cadd3204e728a35d3f13adb7fd0d7902636b79f6b95c40c265eb73b6c35329e4'),
    'templates': ('Godot_v4.7.2-stable_export_templates.tpz', 'f298490b8d44d934be425a5a65a51bf15f422428b229a06a6e11d9ffea248011'),
}


def run(args, name=None, cwd=ROOT, extra_env=None, timeout=1200):
    print('+', ' '.join(str(x) for x in args), flush=True)
    try:
        proc = subprocess.run([str(x) for x in args], cwd=cwd, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, text=True, errors='replace',
                              env=os.environ | (extra_env or {}), timeout=timeout)
    except subprocess.TimeoutExpired as error:
        output = error.stdout or ''
        if isinstance(output, bytes):
            output = output.decode('utf-8', errors='replace')
        print(output, flush=True)
        if name:
            (EVIDENCE / name).write_text(output, encoding='utf-8')
        raise
    print(proc.stdout, flush=True)
    if name:
        (EVIDENCE / name).write_text(proc.stdout, encoding='utf-8')
    if proc.returncode:
        raise RuntimeError(f'Exit {proc.returncode}: {args[0]}')
    return proc.stdout


def asset(kind):
    filename, expected = ASSETS[kind]
    path = CACHE / filename
    if not path.exists():
        urllib.request.urlretrieve(f'https://github.com/godotengine/godot-builds/releases/download/{VERSION}/{filename}', path)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f'Official asset checksum mismatch: {filename}: {actual}')
    with zipfile.ZipFile(path) as archive:
        archive.extractall(CACHE / kind)
    return CACHE / kind


def godot():
    kind = 'windows' if platform.system() == 'Windows' else 'linux'
    folder = asset(kind)
    path = folder / ('Godot_v4.7.2-stable_win64_console.exe' if kind == 'windows'
                     else 'Godot_v4.7.2-stable_linux.x86_64')
    path.chmod(0o755)
    version = run([path, '--headless', '--version'], 'godot-version.txt')
    if not version.strip().startswith('4.7.2.stable'):
        raise RuntimeError(f'Unexpected Godot version: {version}')
    return path


def ndk_root():
    return Path(os.environ['ANDROID_HOME']) / 'ndk' / NDK


def stage_v001():
    if FUNCTIONAL:
        run(["python", ROOT / "Tools/NIM07/stage_pack.py"], "v001-stage.txt")


def build(target):
    stage_v001()
    out = SOURCE / f'build-{target}'
    args = ['cmake', '-S', SOURCE, '-B', out, '-DCMAKE_BUILD_TYPE=Release', '-DCMAKE_EXPORT_COMPILE_COMMANDS=ON']
    if target == 'windows':
        args += ['-G', 'Visual Studio 17 2022', '-A', 'x64', '-T', 'v143,version=14.44.35207']
    else:
        args += ['-G', 'Ninja']
    if target == 'linux':
        args += ['-DCMAKE_CXX_FLAGS=-g']
    if target == 'android':
        args += [f'-DCMAKE_TOOLCHAIN_FILE={ndk_root()}/build/cmake/android.toolchain.cmake',
                 '-DANDROID_ABI=arm64-v8a', '-DANDROID_PLATFORM=android-24', '-DANDROID_STL=c++_static']
    run(['cmake', '--version'], f'{target}-cmake-version.txt')
    run(args, f'{target}-configure.txt')
    run(['cmake', '--build', out, '--config', 'Release', '--parallel', '4'], f'{target}-build.txt')
    shutil.copyfile(out / 'CMakeCache.txt', EVIDENCE / f'{target}-CMakeCache.txt')
    shutil.copyfile(out / 'nimroel.map', EVIDENCE / f'{target}-link.map')
    linkmap = (out / 'nimroel.map').read_text(errors='replace')
    for symbol in (['ActionEngine', 'Simulation', 'Persistence', 'ContextBuilder', 'Visibility', 'ContentCatalog', 'decode_content_pack_manifest', 'decode_resource_definition'] if FUNCTIONAL else ['SemanticVersion']):
        if symbol not in linkmap:
            raise RuntimeError(f'CoreRPG {symbol} absent from link map')
    if FUNCTIONAL:
        shutil.copyfile(SOURCE / 'host.gdextension.in', PROJECT / 'native/core_rpg.gdextension')
    for dep in (['corerpg', 'godotcpp', 'jsoncons'] if FUNCTIONAL else ['corerpg', 'godotcpp']):
        run(['git', '-C', out / f'_deps/{dep}-src', 'rev-parse', 'HEAD'], f'{target}-{dep}-commit.txt')
    verify(target)


def verify(target):
    names = {'windows': f'{NAME}.windows.x86_64.dll',
             'android': f'lib{NAME}.android.arm64.so',
             'linux': f'lib{NAME}.linux.x86_64.so'}
    path = PROJECT / ('native/bin' if FUNCTIONAL else 'bin') / names[target]
    data = path.read_bytes()
    details = {'file': path.name, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}
    if target == 'windows':
        assert data[:2] == b'MZ'
        pe = struct.unpack_from('<I', data, 0x3c)[0]
        assert data[pe:pe+4] == b'PE\0\0'
        assert struct.unpack_from('<H', data, pe+4)[0] == 0x8664, 'Not AMD64'
        vswhere = Path(os.environ['ProgramFiles(x86)']) / 'Microsoft Visual Studio/Installer/vswhere.exe'
        install = run([vswhere, '-latest', '-products', '*', '-property', 'installationPath']).strip()
        dumpbin = sorted((Path(install) / 'VC/Tools/MSVC').glob('*/bin/Hostx64/x64/dumpbin.exe'))[-1]
        text = run([dumpbin, '/headers', '/dependents', '/exports', path], 'windows-pe.txt')
        assert ENTRY in text
        assert not re.search(r'(?:VCRUNTIME|MSVCP|ucrtbased|libgcc|libstdc\+\+).*\.dll', text, re.I)
        details['machine'] = 'PE AMD64 (0x8664)'
    else:
        assert data[:6] == b'\x7fELF\x02\x01', 'Expected ELF64 little endian'
        assert struct.unpack_from('<H', data, 18)[0] == (183 if target == 'android' else 62)
        reader = ndk_root() / 'toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-readelf' if target == 'android' else 'readelf'
        text = run([reader, '-h', '-d', '-l', '--dyn-syms', '--wide', path], f'{target}-elf.txt')
        assert ENTRY in text
        if FUNCTIONAL:
            # Only the GDExtension ABI is public, not Core C++ implementation symbols.
            assert 'WorldState' not in text and 'Inspector' not in text and 'ActionEngine' not in text
        needed = re.findall(r'\(NEEDED\).*?\[(.*?)\]', text)
        if target == 'android':
            assert set(needed) <= {'libc.so', 'libm.so', 'libdl.so', 'liblog.so', 'libandroid.so'}, needed
            aligns = [int(line.split()[-1], 16) for line in text.splitlines() if line.strip().startswith('LOAD ')]
            assert aligns and all(value >= 16384 for value in aligns), aligns
        details.update(machine='ELF AArch64 (183)' if target == 'android' else 'ELF x86-64 (62)', needed=needed)
    (EVIDENCE / f'{target}-binary.json').write_text(json.dumps(details, indent=2) + '\n')
    print(json.dumps(details, indent=2))


def smoke():
    stage_v001()
    exe = godot()
    import_error = None
    try:
        imported = run([exe, '--headless', '--editor', '--path', PROJECT,
                        '--quit-after', '3600', '--max-fps', '30'], 'godot-import.txt',
                       extra_env={'NIM06_IMPORT_ONLY': '1'}, timeout=180)
        if 'NIM06_EDITOR_IMPORT_OK' not in imported or 'ERROR:' in imported:
            raise RuntimeError('Godot import emitted errors')
    except RuntimeError as error:
        import_error = error
        baseline = CACHE / 'baseline'
        baseline.mkdir(exist_ok=True)
        (baseline / 'project.godot').write_text('config_version=5\n[application]\nconfig/name="Empty control"\n[rendering]\nrenderer/rendering_method="gl_compatibility"\n')
        try:
            run([exe, '--headless', '--editor', '--path', baseline, '--import', '--quit'], 'godot-empty-control.txt')
        except RuntimeError as baseline_error:
            print('Empty control also failed:', baseline_error)
        if platform.system() == 'Linux' and shutil.which('gdb'):
            run(['gdb', '--batch', '-ex', 'run', '-ex', 'thread apply all bt', '--args', exe,
                 '--headless', '--editor', '--path', PROJECT, '--import', '--quit'], 'godot-gdb.txt')
    output = run([exe, '--headless', '--path', PROJECT, '--script', 'res://tests/nim06_smoke.gd' if FUNCTIONAL else 'res://smoke.gd'], 'godot-smoke.txt', timeout=180)
    if import_error:
        raise import_error
    if not ('NIM06_FUNCTIONAL_REPORT' in output and '"ok":true' in output.replace(' ', '') if FUNCTIONAL else 'NIM06_CORE_OPERATION_OK cases=8' in output) or 'ERROR:' in output:
        raise RuntimeError('No successful native operation evidence')


def export_android():
    stage_v001()
    exe = godot()
    templates = asset('templates') / 'templates'
    destination = Path.home() / '.local/share/godot/export_templates/4.7.2.stable'
    shutil.copytree(templates, destination, dirs_exist_ok=True)
    output = PROJECT / 'export'
    output.mkdir(exist_ok=True)
    exported = run([exe, '--headless', '--path', PROJECT, '--export-debug', 'Android Native ARM64' if FUNCTIONAL else 'Android Lab ARM64',
                    'export/Nimroel_NIM06_Functional.apk' if FUNCTIONAL else 'export/Nimroel_NIM06_Lab.apk'], 'android-export.txt')
    if 'ERROR:' in exported:
        raise RuntimeError('Godot export emitted errors')
    if '/build-tools/36.0.0/apksigner' not in exported.replace('\\', '/'):
        raise RuntimeError('Godot did not use the pinned Android signing tool')
    apk = output / ('Nimroel_NIM06_Functional.apk' if FUNCTIONAL else 'Nimroel_NIM06_Lab.apk')
    run([Path(os.environ['ANDROID_HOME']) / 'build-tools/36.0.0/apksigner',
         'verify', '--verbose', apk], 'android-signature.txt')
    manifest = run([Path(os.environ['ANDROID_HOME']) / 'build-tools/36.0.0/aapt2',
                    'dump', 'badging', apk], 'android-manifest.txt')
    if "minSdkVersion:'24'" not in manifest or "targetSdkVersion:'36'" not in manifest:
        raise RuntimeError('Unexpected minimum/target Android SDK in actual APK')
    with zipfile.ZipFile(apk) as archive:
        libs = [n for n in archive.namelist() if n.startswith('lib/') and n.endswith('.so')]
        assert libs and all(n.startswith('lib/arm64-v8a/') for n in libs), libs
        entry = f'lib/arm64-v8a/lib{NAME}.android.arm64.so'
        assert entry in libs, libs
        assert archive.read(entry) == (PROJECT / ('native/bin' if FUNCTIONAL else 'bin') / f'lib{NAME}.android.arm64.so').read_bytes()
        assert all(struct.unpack_from('<H', archive.read(n), 18)[0] == 183 for n in libs)
    if FUNCTIONAL:
        verify_v001_package(exe, apk, android=True)
    details = {'sha256': hashlib.sha256(apk.read_bytes()).hexdigest(), 'libraries': libs,
               'extension_bytes_match': True, 'device_execution': 'NOT TESTED', 'file': apk.name}
    (EVIDENCE / 'android-apk.json').write_text(json.dumps(details, indent=2) + '\n')
    print(json.dumps(details, indent=2))


def export_windows():
    stage_v001()
    exe = godot()
    templates = asset('templates') / 'templates'
    destination = Path(os.environ['APPDATA']) / 'Godot/export_templates/4.7.2.stable'
    shutil.copytree(templates, destination, dirs_exist_ok=True)
    output = PROJECT / 'export'
    output.mkdir(exist_ok=True)
    exported = run([exe, '--headless', '--path', PROJECT, '--export-debug', 'Windows Native x64',
                    'export/Nimroel_NIM06_Functional.exe'], 'windows-export.txt')
    if 'ERROR:' in exported:
        raise RuntimeError('Windows export emitted errors')
    compiled = PROJECT / 'native/bin/nimroel_core.windows.x86_64.dll'
    packaged = list(output.rglob(compiled.name))
    assert len(packaged) == 1 and packaged[0].read_bytes() == compiled.read_bytes(), packaged
    console = output / 'Nimroel_NIM06_Functional.console.exe'
    assert console.exists()
    tested = run([console, '--headless', '--', '--nim06-self-test'], 'windows-package-execution.txt', cwd=output, timeout=180)
    assert 'NIM06_FUNCTIONAL_REPORT' in tested and '"ok":true' in tested.replace(' ', '') and 'ERROR:' not in tested
    packaged_i2 = run([console, '--headless', '--', '--nim07-i2-self-test'], 'windows-package-i2.txt', cwd=output, timeout=180)
    assert 'NIM-07 I2 SMOKE PASS' in packaged_i2 and 'ERROR:' not in packaged_i2
    packaged_i3 = run([console, '--headless', '--', '--nim07-i3-self-test'], 'windows-package-i3.txt', cwd=output, timeout=180)
    assert 'NIM-07 I3 SMOKE PASS' in packaged_i3 and 'ERROR:' not in packaged_i3
    i4_processes(console, packaged=True, cwd=output)
    verify_v001_package(exe, output / 'Nimroel_NIM06_Functional.pck')
    details = {str(p.relative_to(output)): {'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in output.rglob('*') if p.is_file()}
    (EVIDENCE / 'windows-package.json').write_text(json.dumps(details, indent=2) + '\n')
    print(json.dumps(details, indent=2))


def verify_v001_package(exe, package, android=False):
    """Read exported bytes, not the editor copy. APK ZIP is a Linux FileAccess control."""
    source = ROOT / 'ContentPacks/treskal-villages/pack'
    expected = {p.relative_to(source).as_posix(): p.read_bytes() for p in source.rglob('*') if p.is_file()}
    prefix = 'generated_content/treskal-v001/'
    mounted = package
    if android:
        # Godot Android exports individual assets rather than a desktop PCK.
        # Re-root ONLY the original nine JSON asset bytes into a mountable ZIP.
        mounted = EVIDENCE / 'android-v001-assets.zip'
        with zipfile.ZipFile(package) as apk, zipfile.ZipFile(mounted, 'w') as content:
            entries = {n.removeprefix('assets/generated_content/treskal-v001/'): n
                       for n in apk.namelist() if n.startswith('assets/generated_content/treskal-v001/') and not n.endswith('/')}
            assert set(entries) == set(expected), entries
            for name, entry in entries.items():
                data = apk.read(entry)
                assert data == expected[name], name
                content.writestr('generated_content/treskal-v001/' + name, data)
    else:
        # Parse the unencrypted Godot 4 PCK directory; compare its actual payloads.
        data = package.read_bytes()
        assert data[:4] == b'GDPC'
        pack_version = struct.unpack_from('<I', data, 4)[0]
        assert pack_version in (2, 3, 4), pack_version
        flags = struct.unpack_from('<I', data, 20)[0]
        base = struct.unpack_from('<Q', data, 24)[0]
        assert flags & ~2 == 0, flags
        offset = struct.unpack_from('<Q', data, 32)[0] if pack_version >= 3 else 96
        count = struct.unpack_from('<I', data, offset)[0]
        offset += 4
        entries = {}
        for _ in range(count):
            length = struct.unpack_from('<I', data, offset)[0]
            offset += 4
            path = data[offset:offset+length].rstrip(b'\0').decode('utf-8').removeprefix('res://')
            offset += length
            position, size = struct.unpack_from('<QQ', data, offset)
            offset += 36  # position, size, MD5, flags
            if path.startswith(prefix):
                entries[path.removeprefix(prefix)] = data[base+position:base+position+size]
        assert entries == expected, list(entries)
    tested = run([exe, '--headless', '--path', PROJECT, '--script', 'res://tests/nim07_pack_probe.gd', '--', mounted.resolve()],
                 'android-pack-read.txt' if android else 'windows-pack-read.txt', timeout=180)
    assert 'NIM07_PACK_REPORT' in tested and '"ok":true' in tested.replace(' ', '') and 'ERROR:' not in tested
    detail = {'files': {n: hashlib.sha256(b).hexdigest() for n, b in expected.items()},
              'bytes_match': True, 'godot_fileaccess_and_native_catalog': True,
              'scope': 'APK asset ZIP mounted in Linux control; no Android runtime' if android else 'actual Windows PCK mounted in Godot'}
    (EVIDENCE / ('android-v001-package.json' if android else 'windows-v001-package.json')).write_text(json.dumps(detail, indent=2) + '\n')


def i4_processes(exe, packaged=False, cwd=ROOT):
    """Two OS processes, fresh per-pair user storage, shared ONLY through files."""
    with tempfile.TemporaryDirectory(prefix='nim07-i4-') as directory:
        env = {'APPDATA': directory} if platform.system() == 'Windows' else {'XDG_DATA_HOME': directory}
        reports = []
        for phase in ('write', 'read'):
            args = [exe, '--headless']
            if not packaged:
                args += ['--path', PROJECT, '--script', 'res://tests/nim07_i4_smoke.gd']
            args += ['--', '--nim07-i4-' + phase]
            output = run(args, ('windows-package' if packaged else 'regression') + '-i4-' + phase + '.txt',
                         cwd=cwd, extra_env=env, timeout=180)
            assert 'NIM-07 I4 SMOKE PASS ' + phase in output and 'ERROR:' not in output
            reports.append(json.loads(re.search(r'NIM07_I4_REPORT (.*)', output).group(1)))
        assert reports[0]['pid'] != reports[1]['pid']
        (EVIDENCE / ('windows-package-i4.json' if packaged else 'i4-processes.json')).write_text(
            json.dumps({'independent_processes': True, 'reports': reports}, indent=2) + '\n')


def regressions():
    stage_v001()
    exe = godot()
    scripts = ['smoke', 'nim02_smoke', 'nim03_smoke', 'nim04_smoke', 'nim05_smoke', 'keyboard_layout_smoke', 'native_layout_smoke']
    if FUNCTIONAL:
        scripts += ['nim07_smoke', 'nim07_i2_smoke', 'nim07_i3_smoke']
    for script in scripts:
        output = run([exe, '--headless', '--path', PROJECT, '--script', f'res://tests/{script}.gd'], f'regression-{script}.txt', timeout=120)
        assert 'ERROR:' not in output and 'PASS' in output, script
    if FUNCTIONAL:
        i4_processes(exe)
    for folder in ['NIM03', 'NIM04', 'NIM05']:
        run(['python', '-m', 'unittest', 'discover', '-s', ROOT / 'Tools' / folder, '-p', 'test_*.py', '-v'], f'regression-{folder}.txt')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['build', 'smoke', 'export-android', 'export-windows', 'regressions'])
    parser.add_argument('--functional', action='store_true')
    parser.add_argument('--target', choices=['windows', 'android', 'linux'])
    args = parser.parse_args()
    global FUNCTIONAL, SOURCE, PROJECT, EVIDENCE, NAME, ENTRY
    if args.functional:
        FUNCTIONAL = True
        SOURCE = ROOT / 'Game/BridgeCoreRPG/native'
        PROJECT = ROOT / 'Game/Host2D'
        EVIDENCE = EVIDENCE / 'functional'
        NAME = 'nimroel_core'
        ENTRY = 'nimroel_core_init'
    CACHE.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    if args.command == 'build':
        if not args.target:
            parser.error('build requires --target')
        build(args.target)
    elif args.command == 'smoke':
        smoke()
    elif args.command == 'export-android':
        export_android()
    elif args.command == 'export-windows':
        export_windows()
    else:
        regressions()


if __name__ == '__main__':
    main()

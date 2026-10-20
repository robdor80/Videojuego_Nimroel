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
    proc = subprocess.run([str(x) for x in args], cwd=cwd, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, text=True, errors='replace',
                          env=os.environ | (extra_env or {}), timeout=timeout)
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


def build(target):
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
    for symbol in (['ActionEngine', 'Simulation', 'Persistence', 'ContextBuilder', 'Visibility'] if FUNCTIONAL else ['SemanticVersion']):
        if symbol not in linkmap:
            raise RuntimeError(f'CoreRPG {symbol} absent from link map')
    if FUNCTIONAL:
        shutil.copyfile(SOURCE / 'host.gdextension.in', PROJECT / 'native/core_rpg.gdextension')
    for dep in ['corerpg', 'godotcpp']:
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
    details = {'sha256': hashlib.sha256(apk.read_bytes()).hexdigest(), 'libraries': libs,
               'extension_bytes_match': True, 'device_execution': 'NOT TESTED', 'file': apk.name}
    (EVIDENCE / 'android-apk.json').write_text(json.dumps(details, indent=2) + '\n')
    print(json.dumps(details, indent=2))


def export_windows():
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
    details = {str(p.relative_to(output)): {'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in output.rglob('*') if p.is_file()}
    (EVIDENCE / 'windows-package.json').write_text(json.dumps(details, indent=2) + '\n')
    print(json.dumps(details, indent=2))


def regressions():
    exe = godot()
    for script in ['smoke', 'nim02_smoke', 'nim03_smoke', 'nim04_smoke', 'keyboard_layout_smoke']:
        output = run([exe, '--headless', '--path', PROJECT, '--script', f'res://tests/{script}.gd'], f'regression-{script}.txt', timeout=120)
        assert 'ERROR:' not in output and 'PASS' in output, script
    for folder in ['NIM03', 'NIM04']:
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

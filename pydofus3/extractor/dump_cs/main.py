import re
import subprocess
from pathlib import Path

assembly_pattern = re.compile(r'^\[assembly:.*$\n', flags=re.MULTILINE)
image_return_line = re.compile(r'\n^// Image', flags=re.MULTILINE)
using_pattern = re.compile(r'^using [\w._]*;\n', flags=re.MULTILINE)


def redux(game_path: Path, output: Path, unity_version: str, ida_script: bool = False) -> None:
    """
    dump with il2cpp inspector redux
    """
    output.mkdir(exist_ok=True, parents=True)
    dumper_path = Path(__file__).parent / 'redux/Il2CppInspector.dll'
    if not (metadata_path := next(game_path.rglob('**/global-metadata.dat'))):
        raise FileNotFoundError('global-metadata.dat not found')
    if not (il2cpp_path := next(game_path.glob('GameAssembly.*'))):
        raise FileNotFoundError('GameAssembly not found')
    cmd = ['dotnet', dumper_path, '-i', il2cpp_path.resolve(), '-m', metadata_path.resolve(), '--unity-version',
           unity_version, '-n', '--select-outputs', '--cs-out', 'dump.cs', '--dll-out', 'DummyDll']
    if ida_script:
        cmd.extend(['--py-out', 'il2cpp.py'])
    subprocess.run(cmd, cwd=output)
    if ida_script:
        old = '-target x86_64-pc-linux -x c++ -D_IDACLANG_=1'
        py_script = output / 'il2cpp.py'
        py_script.write_text(py_script.read_text().replace(old, f'{old} -fdeclspec'))

    dump_cs = output / 'dump.cs'
    dump_cs_text = dump_cs.read_text()
    dump_cs_text = assembly_pattern.sub('', dump_cs_text)
    dump_cs_text = image_return_line.sub('// Image', dump_cs_text)
    dump_cs_text = using_pattern.sub('', dump_cs_text)
    dump_cs.write_text(assembly_pattern.sub('', dump_cs_text))

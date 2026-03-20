import ast
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

assembly_pattern = re.compile(r'^\[assembly:.*$\n', flags=re.MULTILINE)
image_return_line = re.compile(r'\n^// Image', flags=re.MULTILINE)
using_pattern = re.compile(r'^using [\w._]*;\n', flags=re.MULTILINE)


def redux(game_path: Path, output: Path, unity_version: str,generated_code_in_output:bool=False , code_gen:bool=False,dll:bool=False, dumpcs:bool=False,ida_script: bool = False) -> None:
    """
    dump with il2cpp inspector redux
    """

    if not code_gen and not dumpcs and not ida_script and not dll:
        code_gen = True
        dumpcs = True
        dll = True

    output.mkdir(exist_ok=True, parents=True)
    dumper_path = Path(__file__).parent / 'redux/CodeGen.dll'
    generated_code_path = (output if generated_code_in_output else Path(__file__).parent.parent.parent) / 'generated'
    if not (metadata_path := next(game_path.rglob('**/global-metadata.dat'))):
        raise FileNotFoundError('global-metadata.dat not found')
    if not (il2cpp_path := next(game_path.glob('GameAssembly.*'))):
        raise FileNotFoundError('GameAssembly not found')
    cmd = ['dotnet', dumper_path, '-i', il2cpp_path.resolve(), '-m', metadata_path.resolve(), '--unity-version',
           unity_version, '-n', '--select-outputs']
    if dll:
        cmd.extend(['--dll-out', output/'DummyDll'])
    if dumpcs:
        cmd.extend(['--cs-out', output/'dump.cs'])
    if ida_script:
        cmd.extend(['--py-out', output/'il2cpp.py', '--json-out',output/'metadata.json','--cpp-out', output/'cpp'])
    if code_gen:
        cmd.extend(['--py-generated-out', generated_code_path/'pydantic', '--py-enum-out', generated_code_path/'GeneratedEnum',
           '--config', Path(__file__).parent/'config.json'])

    subprocess.run(cmd)
    if ida_script:
        old = '-target x86_64-pc-linux -x c++ -D_IDACLANG_=1'
        py_script = output / 'il2cpp.py'
        py_script.write_text(py_script.read_text().replace(old, f'{old} -fdeclspec'))
    if code_gen:
        codegen_postprocess(generated_code_path)

def codegen_postprocess(generated_path):
    d2o_classes = find_direct_subclasses(generated_path / 'pydantic', 'D2oData')

    d2o_folder = generated_path / 'pydantic_d2o'
    d2o_folder.mkdir(exist_ok=True, parents=True)
    for k, v in d2o_classes.items():
        imports = '\n'.join(f'from pydofus3.generated.pydantic.{c.path} import {c.name}' for c in v)
        all_ = f"__all__ =[{', '.join(f'"{c.name}"' for c in v)}]"
        (d2o_folder / f'{k}.py').write_text(f'{imports}\n\n{all_}')

    env = Environment(loader=FileSystemLoader(Path(__file__).parent / 'templates'))
    total = sum(map(len, d2o_classes.values()))

    datacenter_code = env.get_template('datacenter.py.jinja').render(class_name=d2o_classes, total=total)
    (generated_path / 'datacenter.py').write_text(datacenter_code)

    api_code = env.get_template('api.py.jinja').render(class_name=d2o_classes, total=total)
    (generated_path / 'api.py').write_text(api_code)

@dataclass(order=True)
class ClassDefinition:
    name:str
    path: str

def find_direct_subclasses(directory: Path, base_class: str) -> dict[str, list[ClassDefinition]]:
    results = defaultdict(list)

    for file in directory.rglob("*.py"):
            try:
                tree = ast.parse(file.read_text())
            except SyntaxError:
                continue

            file_name = ".".join(file.relative_to(directory).with_suffix("").parts)
            folder_name = file.parent.name

            for node in ast.walk(tree):
                if not isinstance(node, ast.ClassDef):
                    continue

                base_names = {b.id for b in node.bases if isinstance(b, ast.Name)}
                if base_class in base_names:
                    results[folder_name].append(ClassDefinition(node.name, file_name))

    return {k: sorted(v) for k, v in sorted(results.items())}

import logging
from pathlib import Path
from typing import Annotated

import typer
from pydofus3.cli.data_extract import DEFAULT_DOFUS, DEFAULT_OUTPUT, data_app
from pydofus3.enum_data import Language, TypeDataOther

DEFAULT_GENERATED = Path(__file__).parent.parent / 'generated'

logging.basicConfig(
    filename='python.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

app = typer.Typer(pretty_exceptions_enable=False, no_args_is_help=True)
app.add_typer(data_app, name='data', help='extract dofus data')

@app.command()
def pydantic(
        dofus_path: Annotated[Path, typer.Argument(help='dofus game path', resolve_path=True, exists=True)] = DEFAULT_DOFUS,
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_GENERATED,
        ):
    """
    generate pydantic model and enum
    """
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.tools import get_unity_version

    version = get_unity_version(dofus_path)
    redux(dofus_path, output / 'dummyDLL', version, code_gen=True)


@app.command()
def stub(
        dofus_path: Annotated[Path, typer.Argument(help='dofus game path', exists=True)] = DEFAULT_DOFUS,
        output_generated: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_GENERATED,
        ):
    """
    generate python stub and typed dict for typetree present in bundles
    """
    from pydofus3.extractor.data.typetree.stub_typetree import StubTypeTree

    StubTypeTree(dofus_path, output_generated)


@app.command()
def ornament(
        dofus_path: Annotated[Path, typer.Argument(help='dofus game path', exists=True)] = DEFAULT_DOFUS,
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT / TypeDataOther.Ornament,
        ):
    """
    generate ornament
    """
    from pydofus3.extractor.ornament import Ornament
    from pydofus3.tools import set_unity_version

    set_unity_version(dofus_path)
    Ornament(dofus_path).save_all(output)


@app.command(deprecated=True)
def proto(output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT):
    """
    generate proto (deprecated)
    """
    from pydofus3.extractor.proto.protodec import protodec

    protodec(output / 'dummyDLL', output / 'proto')


@app.command()
def dumpcs(
        dofus_path: Annotated[
            Path, typer.Argument(help='dofus game path', resolve_path=True, exists=True)] = DEFAULT_DOFUS,
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT,
        ida_script: Annotated[bool, typer.Option(help='add ida script')] = False,
        dump_cs: Annotated[bool, typer.Option(help='dump.cs')] = False,
        dll: Annotated[bool, typer.Option(help='dll')] = False,
        codegen: Annotated[bool, typer.Option(help='generate code')] = False,
        ):
    """
    modify il2cpp inspector redux that can also generate python code
    """
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.tools import get_unity_version

    version = get_unity_version(dofus_path)
    redux(dofus_path, output / 'dummyDLL', version, ida_script=ida_script, dumpcs=dump_cs, dll=dll, code_gen=codegen)


@app.command()
def i18n(
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT,
        i18n_folder: Annotated[Path, typer.Argument(help='i18n folder', resolve_path=True, exists=True)] = DEFAULT_DOFUS
                                                                                                           / TypeDataOther.I18n,
        compress: Annotated[bool, typer.Option(help='compress monobehaviour with zstd')] = False,
        ):
    """
    extract all i18n
    """

    from pydofus3.extractor.i18n import extract_i18n

    extract_i18n(i18n_folder, output, compress)


@app.command()
def audio(
        dofus_path: Annotated[
            Path, typer.Argument(help='dofus game path', resolve_path=True, exists=True)] = DEFAULT_DOFUS,
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT,
        file_change: Annotated[
            Path | None,
            typer.Option(
                help="Path to a JSON file describing file changes. The JSON can be either: a list of files or a dict with keys 'new', 'change', 'remove' and lists of files as values. The list of files must be relative to the dofus_path."
                ),
        ] = None,
        ):
    """
    extract audio bank event
    """
    from pydofus3.extractor.audio.audio import extract_audio

    from .data_extract import read_file_change

    if file_change and file_change.exists():
        banks = [file for i in read_file_change(file_change) if (file := (dofus_path / i)).suffix == '.bank']
    else:
        banks = list((dofus_path / TypeDataOther.Audio).glob('*.bank'))
    extract_audio(banks, output / TypeDataOther.Audio)


@app.command()
def open_api(output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT):
    """
    generate open api schema
    """
    from pydofus3.extractor.open_api_schema import generate_openapi
    generate_openapi(output)


@app.command()
def process(
        output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT,
        output_generated: Annotated[Path, typer.Argument(help='code generated output folder')] = DEFAULT_GENERATED,
        ):
    """
    process all data after update
    """
    import orjson

    from pydofus3.enum_data import TypeData
    from pydofus3.extractor.audio.audio import extract_audio
    from pydofus3.extractor.config import UnityExtractorOptionConfig
    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.extractor.data.typetree.stub_typetree import StubTypeTree
    from pydofus3.extractor.i18n import extract_i18n
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.not_generated.i18n import i18n_dict
    from pydofus3.tools import group_file_by_catalog, get_unity_version
    from pydofus3.db_dump.process import Processor
    from pydofus3.extractor.proto.protodec import protodec
    import UnityPy

    dofus_path = output / 'dofus_unity'

    files_change = orjson.loads((dofus_path / 'change.json').read_bytes())
    files = set(dofus_path / f for f in files_change['new'] + files_change['change'])
    grouped_files = group_file_by_catalog(files, dofus_path)
    version = get_unity_version(dofus_path)
    UnityPy.config.FALLBACK_UNITY_VERSION = version

    redux(dofus_path, output / 'dummyDLL', version, code_gen=True)
    if any('I18n' in str(f) for f in files) or TypeData.Data in grouped_files:
        i18n_dict.update(extract_i18n(dofus_path / TypeDataOther.I18n, output / TypeDataOther.I18n))

    for key, value in grouped_files.items(): # skin and bone in priority to update skin data
        conf = UnityExtractorOptionConfig(output=output, files=value)
        if key == TypeData.Picto_Items:
            conf.force_texture2d = True
        elif key not in [TypeData.Skins, TypeData.Bones]:
            continue
        UnityExtractor(dofus_path, key, conf).extract()

    for key, value in grouped_files.items():
        conf = UnityExtractorOptionConfig(output=output, files=value)
        if key in [TypeData.Map_Textures_Effects, TypeData.Picto_UI, TypeData.Picto_Spells,
                   TypeData.Picto_Monsters, TypeData.Picto_Worldmaps]:  # fmt: skip
            conf.force_texture2d = True
        elif key in [TypeData.Map_Textures1, TypeData.Map_Textures2]:
            conf.force_texture2d, conf.force_gc_collect = True, True
        elif key == TypeData.Map_Data:
            conf.compress, conf.reference = True, True
        elif key == TypeData.Data:
            conf.process_datacenter, conf.load_all_files = True, True
        elif key == TypeData.aa:
            conf.sprite_rect_size = True
        else:
            continue
        UnityExtractor(dofus_path, key, conf).extract()
    if audio_files := [i for i in files if i.suffix == '.bank']:
        extract_audio(audio_files, output / TypeDataOther.Audio)
    StubTypeTree(dofus_path, output_generated, grouped_files)
    Processor().db_dump()
    redux(dofus_path, output / 'dummyDLL', version, dll=True, dumpcs=True)
    protodec(output / 'dummyDLL', output / 'proto')


@app.command()
def process_data(output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT):
    """
    validate data with pydantic
    """
    from pydofus3.enum_data import TypeData
    from pydofus3.extractor.config import UnityExtractorOptionConfig
    from pydofus3.extractor.data.main import UnityExtractor

    dofus_path = output / 'dofus_unity'

    conf = UnityExtractorOptionConfig(output=output, process_datacenter=True, load_all_files=True)
    UnityExtractor(dofus_path, TypeData.Data, conf).extract()


if __name__ == '__main__':
    app()

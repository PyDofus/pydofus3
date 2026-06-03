import logging
from pathlib import Path
from typing import Annotated

import typer

from pydofus3.cli.data_extract import DEFAULT_DOFUS, DEFAULT_OUTPUT, data_app
from pydofus3.enum_data import TypeDataOther

DEFAULT_GENERATED = Path(__file__).parent.parent / 'generated'

logging.basicConfig(
    filename='python.log',
    filemode='a',
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

app = typer.Typer(pretty_exceptions_enable=False, no_args_is_help=True)
app.add_typer(data_app, name='data', help='Extract Dofus Unity asset bundles.')


@app.command()
def pydantic(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    output: Annotated[
        Path | None, typer.Option(help='Output folder.')
    ] = None,
):
    """
    Generate Pydantic models and enums from the IL2CPP metadata.

    Runs the redux IL2CPP inspector with code generation enabled to produce typed Pydantic classes mirroring the datacenter schema and enums.
    """
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.tools import get_unity_version

    version = get_unity_version(dofus_path)
    output = output if output is not None else DEFAULT_OUTPUT
    redux(dofus_path, output, version, generated_code_in_output=output is not None, code_gen=True)


@app.command()
def stub(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', exists=True)
    ] = DEFAULT_DOFUS,
    output_generated: Annotated[
        Path, typer.Argument(help='Folder where Python stubs and TypedDicts are written.')
    ] = DEFAULT_GENERATED,
):
    """
    Generate Python stubs and TypedDicts from Unity typetrees found in bundles.

    Note: not adapted to the macOS layout. If you only need the stubs, prefer the ones already generated under ``generated/stub`` and ``generated/typed_dict``.
    """
    from pydofus3.extractor.data.stub_typetree import StubTypeTree

    StubTypeTree(dofus_path, output_generated)


@app.command()
def ornament(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', exists=True)
    ] = DEFAULT_DOFUS,
    output: Annotated[
        Path, typer.Argument(help='Output folder')
    ] = DEFAULT_OUTPUT,
):
    """
    Render the in-game ornaments (PNG and WebM animation) from their Unity assets.
    """
    from pydofus3.extractor.ornament import Ornament
    from pydofus3.tools import set_unity_version

    set_unity_version(dofus_path)
    Ornament(dofus_path).save_all(output/ TypeDataOther.Ornament)


@app.command()
def proto(
    output: Annotated[
        Path, typer.Argument(help='Output folder. Reads "dummyDLL/" and writes "proto/" inside it.')
    ] = DEFAULT_OUTPUT,
):
    """
    Generate the obfuscated protobuf.
    """
    from pydofus3.extractor.proto.protodec import protodec

    protodec(output / 'dummyDLL', output / 'proto')


@app.command()
def dumpcs(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    output: Annotated[
        Path, typer.Argument(help='Output folder.')
    ] = DEFAULT_OUTPUT,
    code_gen_in_output: Annotated[
        bool, typer.Option(help='Write generated Python code under OUTPUT instead of the in-package generated folder.')
    ] = False,
    ida_script: Annotated[bool, typer.Option(help='Also export an IDA Python script.')] = False,
    dump_cs: Annotated[bool, typer.Option(help='Export ``dump.cs``.')] = False,
    dll: Annotated[bool, typer.Option(help='Export the reconstructed dummy DLLs.')] = False,
    codegen: Annotated[bool, typer.Option(help='Generate Pydantic/enum Python code.')] = False,
):
    """
    Run the modified IL2CPP Inspector "redux" against the Dofus binary.

    Combine the flags to pick which artifacts to produce.
    """
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.tools import get_unity_version

    version = get_unity_version(dofus_path)
    redux(
        dofus_path,
        output / 'dummyDLL',
        version,
        generated_code_in_output=code_gen_in_output,
        ida_script=ida_script,
        dumpcs=dump_cs,
        dll=dll,
        code_gen=codegen,
    )


@app.command()
def i18n(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    output: Annotated[Path, typer.Argument(help='output folder.')] = DEFAULT_OUTPUT,
    compress: Annotated[bool, typer.Option(help='Compress the produced JSON with zstd.')] = False,
):
    """
    Extract every i18n bin.
    """
    from pydofus3.extractor.i18n import extract_i18n
    from pydofus3.enum_data import get_data_other_path
    i18n_folder = get_data_other_path(dofus_path, TypeDataOther.I18n)
    if i18n_folder:
        extract_i18n(i18n_folder, output/TypeDataOther.I18n, compress)


@app.command()
def audio(
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    output: Annotated[Path, typer.Argument(help='output folder.')] = DEFAULT_OUTPUT,
    file_change: Annotated[
        Path | None,
        typer.Option(
            help=(
                "Optional JSON manifest restricting extraction to specific .bank files. "
                "Either a list of relative paths, or a dict with keys 'new', 'change', 'remove'. "
                "Paths are relative to DOFUS_PATH."
            )
        ),
    ] = None,
    audio_manager: Annotated[bool, typer.Option(help="extract and process audio manager")] = False
):
    """
    Extract event names and metadata from FMOD .bank audio files.
    """
    from pydofus3.enum_data import get_data_other_path
    from pydofus3.extractor.audio.audio import extract_audio, process_audio_manager

    from .data_extract import read_file_change

    if file_change and file_change.exists():
        banks = [file for i in read_file_change(file_change) if (file := (dofus_path / i)).suffix == '.bank']
    else:
        path_audio = get_data_other_path(dofus_path, TypeDataOther.Audio)
        if path_audio is None:
            typer.echo(f"Could not find '{TypeDataOther.Audio.value}' in either layout under {dofus_path}")
            raise typer.Exit(code=1)
        banks = list(path_audio.glob('*.bank'))
    extract_audio(banks, output / TypeDataOther.Audio)
    if audio_manager:
        process_audio_manager(output, dofus_path)


@app.command()
def open_api(
    output: Annotated[Path, typer.Argument(help='output folder')] = DEFAULT_OUTPUT,
):
    """
    Generate an OpenAPI schema from the previously extracted datacenter.
    """
    from pydofus3.extractor.open_api_schema import generate_openapi

    generate_openapi(output)


@app.command()
def process(
    output: Annotated[Path, typer.Argument(help='Root output folder.')] = DEFAULT_OUTPUT,
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    output_generated: Annotated[
        Path, typer.Argument(help='Folder where Python stubs and TypedDicts are written.')
    ] = DEFAULT_GENERATED,
):
    """
    End-to-end incremental update pipeline.

    Reads DOFUS_PATH/change.json, groups changed files by catalog, and runs the right extractor with the right options for each (textures, datacenter,maps, audio, ...).
    It also refreshes typetree stubs, regenerates protos, runs redux against the binary, and dumps the datacenter to PostgreSQL.

    WARNING: this command is wired for my setup (Linux, PostgreSQL configured via .env). It is unlikely to work as-is on other machines.
    """
    import orjson
    import UnityPy

    from pydofus3.db_dump.process import Processor
    from pydofus3.enum_data import TypeData
    from pydofus3.extractor.audio.audio import extract_audio, process_audio_manager
    from pydofus3.extractor.data.cache import update_character_cache
    from pydofus3.extractor.data.config import UnityExtractorOptionConfig
    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.extractor.data.stub_typetree import StubTypeTree
    from pydofus3.extractor.dump_cs.main import redux
    from pydofus3.extractor.i18n import extract_i18n
    from pydofus3.extractor.proto.protodec import protodec
    from pydofus3.not_generated.i18n import i18n_dict
    from pydofus3.tools import get_unity_version, group_file_by_catalog

    files_change = orjson.loads((dofus_path / 'change.json').read_bytes())
    files = set(dofus_path / f for f in files_change['new'] + files_change['change'])
    grouped_files = group_file_by_catalog(files, dofus_path)
    version = get_unity_version(dofus_path)
    UnityPy.config.FALLBACK_UNITY_VERSION = version

    redux(dofus_path, output / 'dummyDLL', version, code_gen=True)
    if any('I18n' in str(f) for f in files) or TypeData.Data in grouped_files:
        i18n_dict.update(extract_i18n(dofus_path / TypeDataOther.I18n, output / TypeDataOther.I18n))  # ty:ignore[no-matching-overload]

    for key, value in grouped_files.items():  # skin and bone in priority to update skin data directly
        conf = UnityExtractorOptionConfig(output=output, files=value)
        if key == TypeData.Picto_Items:
            conf.force_texture2d = True
        elif key in [TypeData.Skins, TypeData.Bones]:
            conf.no_big_int = True
            conf.skin_png = True
            conf.skin_webp = True
        else:
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
    update_character_cache(grouped_files, output)
    if audio_files := [i for i in files if i.suffix == '.bank']:
        extract_audio(audio_files, output / TypeDataOther.Audio)
        process_audio_manager(output, dofus_path)
    redux(dofus_path, output / 'dummyDLL', version, dll=True, dumpcs=True)
    protodec(output / 'dummyDLL', output / 'proto')
    StubTypeTree(dofus_path, output_generated, grouped_files)
    Processor().db_dump()


if __name__ == '__main__':
    app()

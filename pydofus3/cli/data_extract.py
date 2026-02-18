"""
cli data app
"""

from pathlib import Path
from typing import Annotated

import typer

from pydofus3.enum_data import TypeData

data_app = typer.Typer(no_args_is_help=True)


DEFAULT_OUTPUT = Path('output')
DEFAULT_DOFUS = DEFAULT_OUTPUT / 'dofus_unity'


@data_app.callback()
def main(
    ctx: typer.Context,
    output: Annotated[Path, typer.Option(help='output folder')] = DEFAULT_OUTPUT,
    compress: Annotated[
        bool,
        typer.Option(
            help='Compress monobehaviour data with zstd (not compatible with datacenter monobehaviour if process_datacenter is enabled)'
        ),
    ] = False,
    force_texture2d: Annotated[bool, typer.Option(help='force to render sprite as texture2d')] = False,
    force_object: Annotated[
        bool, typer.Option(help='extract all object (extract only object in container if false)')
    ] = False,
    add_typetree: Annotated[bool, typer.Option(help='extract bundle typetree')] = False,
    add_script: Annotated[bool, typer.Option(help='add script in monobehaviour')] = False,
    process_reference: Annotated[bool, typer.Option(help='process reference for monobehaviour')] = False,
    sprite_rect: Annotated[
        bool, typer.Option(help='Use m_Rect to resize sprite (useful for sprite atlas where force texture2d not work)')
    ] = False,
    process_datacenter: Annotated[
        bool, typer.Option(help='process datacenter monobehaviour: add i18n value, bool and m_flags')
    ] = False,
    load_all_files: Annotated[bool, typer.Option(help='Load all files at once (faster, but uses more memory)')] = False,
    force_gc_collect: Annotated[
        bool, typer.Option(help='Force garbage collection after each file (recommended for map textures)')
    ] = False,
):
    """
    Common command parameters
    """
    from pydofus3.extractor.config import UnityExtractorOptionConfig

    ctx.obj = {
        'extract_conf': UnityExtractorOptionConfig(
            output=output,
            compress=compress,
            force_texture2d=force_texture2d,
            type_tree=add_typetree,
            add_script=add_script,
            reference=process_reference,
            force_object=force_object,
            sprite_rect_size=sprite_rect,
            process_datacenter=process_datacenter,
            load_all_files=load_all_files,
            force_gc_collect=force_gc_collect,
        )
    }


@data_app.command()
def file(
    ctx: typer.Context,
    file_path: Annotated[Path, typer.Argument(help='file to extract', resolve_path=True, exists=True)],
):
    """
    Extract a given file
    """

    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.tools import find_directory_containing_file

    dofus_path = find_directory_containing_file(file_path, 'gameassembly')
    catalog_path = find_directory_containing_file(file_path, 'catalog')
    ctx.obj['extract_conf'].files = [file_path]
    if catalog_path and (data_type := '/'.join(catalog_path.relative_to(dofus_path).parts)):
        UnityExtractor(dofus_path, data_type, ctx.obj['extract_conf']).extract()


@data_app.command()
def catalog(
    ctx: typer.Context,
    catalog_name: Annotated[TypeData, typer.Argument(help='catalog name')],
    dofus_path: Annotated[Path, typer.Argument(help='dofus game path', resolve_path=True, exists=True)] = DEFAULT_DOFUS,
    file_change: Annotated[
        Path | None,
        typer.Option(
            help="Path to a JSON file describing file changes. The JSON can be either: a list of files or a dict with keys 'new', 'change', 'remove' and lists of files as values. The list of files must be relative to the dofus_path."
        ),
    ] = None,
):
    """
    Extract all dofus data link to a catalog
    """

    from pydofus3.extractor.data.main import UnityExtractor

    if file_change and file_change.exists():
        data = read_file_change(file_change)
        ctx.obj['extract_conf'].files = [dofus_path / i for i in data if i.startswith(catalog_name)]

    UnityExtractor(dofus_path, catalog_name, ctx.obj['extract_conf']).extract()


@data_app.command()
def json(
    ctx: typer.Context,
    files: Annotated[
        Path,
        typer.Argument(
            help="Path to a JSON file describing file changes. The JSON can be either: a list of files or a dict with keys 'new', 'change', 'remove' and lists of files as values. The list of files must be relative to the dofus_path.",
            resolve_path=True,
            exists=True,
        ),
    ],
    dofus_path: Annotated[Path, typer.Argument(help='dofus game path', resolve_path=True, exists=True)] = DEFAULT_DOFUS,
):
    """
    Extract all Path contained in a json file
    """

    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.tools import group_file_by_catalog

    files_path = [dofus_path / Path(i) for i in read_file_change(files)]
    if files_path:
        file_by_type = group_file_by_catalog(files_path, dofus_path)
        for key, value in file_by_type.items():
            ctx.obj['extract_conf'].files = value
            UnityExtractor(dofus_path, key, ctx.obj['extract_conf']).extract()


def read_file_change(file_change: Path) -> list[str]:
    import orjson

    try:
        data = orjson.loads(file_change.read_bytes())
    except orjson.JSONDecodeError:
        typer.echo('Error: file_change must be a valid JSON file')
        raise typer.Exit(code=1)
    if 'new' in data and 'change' in data:
        data = data['new'] + data['change']
    return data

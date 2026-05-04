from pathlib import Path
from typing import Annotated

import typer

from pydofus3.enum_data import TypeData

data_app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False)


DEFAULT_OUTPUT = Path('output')
DEFAULT_DOFUS = DEFAULT_OUTPUT / 'dofus_unity'


def _complete_type_data(incomplete: str) -> list[str]:
    return [name for name in TypeData.__members__ if name.startswith(incomplete)]


def _parse_type_data(value: str) -> TypeData:
    try:
        return TypeData[value]
    except KeyError:
        raise typer.BadParameter(
            f"Invalid catalog '{value}'. Choose from: {', '.join(TypeData.__members__)}"
        )


@data_app.callback()
def main(
    ctx: typer.Context,
    output: Annotated[Path, typer.Option(help='output folder.')] = DEFAULT_OUTPUT,
    compress: Annotated[
        bool,
        typer.Option(help='Compress MonoBehaviour JSON with zstd'),
    ] = False,
    force_texture2d: Annotated[
        bool, typer.Option(help='Render sprites as Texture2D (use for Picto and Map textures).')
    ] = False,
    force_object: Annotated[
        bool,
        typer.Option(
            help='Extract every object in the bundle (default: only objects referenced by the catalog container).'
        ),
    ] = False,
    add_script: Annotated[
        bool, typer.Option(help='Embed the MonoScript class info inside each MonoBehaviour JSON.')
    ] = False,
    process_reference: Annotated[bool, typer.Option(help='Process references for monobehaviour')] = False,
    sprite_rect: Annotated[
        bool,
        typer.Option(
            help='Use Sprite m_Rect to crop sprites; useful for sprite atlases when --force-texture2d does not work.'
        ),
    ] = False,
    process_datacenter: Annotated[
        bool, typer.Option(help='Enrich datacenter MonoBehaviours with i18n strings, booleans and m_flags expansion.')
    ] = False,
    load_all_files: Annotated[
        bool, typer.Option(help='Load every bundle in memory before processing (faster, uses more RAM).')
    ] = False,
    force_gc_collect: Annotated[
        bool, typer.Option(help='Force a gc.collect() after each file (recommended for map textures).')
    ] = False,
    no_big_int: Annotated[bool, typer.Option(help='Remove bing int (for js/ts usage).')] = False,
    indent: Annotated[bool, typer.Option(help='Pretty-print JSON outputs with indentation.')] = False,
    skin_png: Annotated[bool, typer.Option(help='Export skin textures as PNG (faster than WEBP)')] = False,
    skin_webp: Annotated[bool, typer.Option(help='Export skin textures as WEBP.')] = False,
):
    """
    Extract Dofus Unity asset bundles. Options here are shared by every subcommand.
    """
    ctx.obj = {
        'output': output,
        'compress': compress,
        'force_texture2d': force_texture2d,
        'add_script': add_script,
        'reference': process_reference,
        'force_object': force_object,
        'sprite_rect_size': sprite_rect,
        'process_datacenter': process_datacenter,
        'load_all_files': load_all_files,
        'force_gc_collect': force_gc_collect,
        'no_big_int': no_big_int,
        'indent': indent,
        'skin_png': skin_png,
        'skin_webp': skin_webp
    }


def _build_conf(ctx: typer.Context, **overrides):
    from pydofus3.extractor.data.config import UnityExtractorOptionConfig

    return UnityExtractorOptionConfig(**ctx.obj, **overrides)


@data_app.command()
def file(
    ctx: typer.Context,
    file_path: Annotated[Path, typer.Argument(help='Asset file to extract.', resolve_path=True, exists=True)],
):
    """
    Extract a single asset file. The catalog (and so the destination subfolder) is inferred by walking up from the file until a catalog and zaap.yml are found.
    """
    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.tools import find_directory_containing_file

    dofus_path = find_directory_containing_file(file_path, 'zaap.yml')
    catalog_path = find_directory_containing_file(file_path, 'catalog')
    if not (catalog_path and dofus_path):
        typer.echo(f"Could not locate a Dofus install (zaap.yml + catalog) above {file_path}")
        raise typer.Exit(code=1)
    data_type = '/'.join(catalog_path.relative_to(dofus_path).parts)
    UnityExtractor(dofus_path, data_type, _build_conf(ctx, files=[file_path])).extract()


@data_app.command()
def catalog(
    ctx: typer.Context,
    catalog_name: Annotated[
        TypeData,
        typer.Argument(
            help='Catalog to extract. One of TypeData names (e.g. Skins, Bones, Data, Map_Data, Picto_Items).',
            metavar='CATALOG',
            autocompletion=_complete_type_data,
            parser=_parse_type_data,
            show_default=False,
        ),
    ],
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
    file_change: Annotated[
        Path | None,
        typer.Option(
            help=(
                "Optional JSON manifest of files to restrict the extraction to. "
                "Either a list of relative paths, or a dict with keys 'new', 'change', 'remove'. "
                "Paths are relative to DOFUS_PATH."
            )
        ),
    ] = None,
):
    """
    Extract every file of a catalog..
    """
    from pydofus3.enum_data import get_data_path
    from pydofus3.extractor.data.main import UnityExtractor

    catalog_path = str(get_data_path(dofus_path, catalog_name).relative_to(dofus_path))
    overrides: dict = {}
    if file_change and file_change.exists():
        data = read_file_change(file_change)
        overrides['files'] = [dofus_path / i for i in data if i.startswith(catalog_name)]

    UnityExtractor(dofus_path, catalog_path, _build_conf(ctx, **overrides)).extract()


@data_app.command()
def json(
    ctx: typer.Context,
    files: Annotated[
        Path,
        typer.Argument(
            help=(
                "JSON manifest of files to extract. Either a list of relative paths, "
                "or a dict with keys 'new', 'change', 'remove'. Paths are relative to DOFUS_PATH."
            ),
            resolve_path=True,
            exists=True,
        ),
    ],
    dofus_path: Annotated[
        Path, typer.Argument(help='Path to the Dofus game folder.', resolve_path=True, exists=True)
    ] = DEFAULT_DOFUS,
):
    """
    Extract every file listed in a JSON manifest.
    """
    from pydofus3.extractor.data.main import UnityExtractor
    from pydofus3.tools import group_file_by_catalog

    files_path = [dofus_path / Path(i) for i in read_file_change(files)]
    if not files_path:
        return
    file_by_type = group_file_by_catalog(files_path, dofus_path)
    for key, value in file_by_type.items():
        UnityExtractor(dofus_path, key, _build_conf(ctx, files=value)).extract()


def read_file_change(file_change: Path) -> list[str]:
    """Read a manifest file. Accepts either a list of paths or a dict with new/change/remove."""
    import orjson

    try:
        data = orjson.loads(file_change.read_bytes())
    except orjson.JSONDecodeError:
        typer.echo('Error: file_change must be a valid JSON file')
        raise typer.Exit(code=1)
    if 'new' in data and 'change' in data:
        data = data['new'] + data['change']
    return data

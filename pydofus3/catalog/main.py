from itertools import chain
from pathlib import Path

from pydofus3.catalog.binary.ContentCatalogDataBinary import ContentCatalogDataBinary
from pydofus3.catalog.catalog import ContentCatalogData
from pydofus3.catalog.json import ContentCatalogDataJson


def load_catalog(path: Path | str) -> ContentCatalogData:
    """Loads a catalog from a file"""
    if isinstance(path, str):
        path: Path = Path(path)
    if path.suffix == '.json':
        return ContentCatalogDataJson.read(path)
    else:
        return ContentCatalogDataBinary.read(path)


def search_load_catalog(path: Path | str) -> ContentCatalogData:
    """Searches for a catalog in a directory and loads it"""
    if isinstance(path, str):
        path: Path = Path(path)
    catalog_path = next(chain(path.glob('catalog*.bin'), path.glob('catalog*.json')), None)
    if catalog_path is None:
        raise FileNotFoundError(f'Catalog not found in {path}')
    return load_catalog(catalog_path)

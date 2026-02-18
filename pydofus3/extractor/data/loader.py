import UnityPy
from pydantic import TypeAdapter
from tqdm import tqdm

from pydofus3.config import check_extract_dir, settings
from pydofus3.enum_data import TypeData
from pydofus3.extractor.data.tools import process_references
from pydofus3.not_generated.base import D2oData, MetadataRoot
from pydofus3.not_generated.i18n import check_i18n
from pydofus3.tools import SingletonMeta


def load_data(bundle_name: str) -> dict:
    """Load a D2O file and return a dict of raw data."""
    file_path = settings.game_path / TypeData.Data / f'data_assets_{bundle_name}.asset.bundle'
    if not file_path.exists():
        tqdm.write(f'Bundle {bundle_name} not found.')
        return dict()
    env = UnityPy.load(str(file_path))
    data = next(iter(env.container.values())).read_typetree()
    process_references(data)
    return data


@check_i18n
def load_d2o[T: D2oData](class_d2o: type[T]) -> dict[int, T]:
    """Load a D2O file and return a dict of pydantic objects."""
    data = load_data(class_d2o.bundle_name)
    return TypeAdapter(dict[int, class_d2o]).validate_python(data.get('objectsById', {}))


@check_extract_dir
def load_json_data[T: D2oData](class_d2o: type[T]) -> dict[int, T]:
    """Load a json file and return a dict of pydantic objects."""
    data_path = settings.extract_dir / TypeData.Data / f'{class_d2o.bundle_name}.json'
    return MetadataRoot[class_d2o].model_validate_json(data_path.read_bytes()).objectsById


class D2oLoaderPydantic[T: D2oData](metaclass=SingletonMeta):
    """D2o singleton with pydantic"""

    def __init__(self, class_d2o: type[T]):
        self.data = load_d2o(class_d2o)
        self.data_list = list(self.data.values())


class JsonLoaderPydantic[T: D2oData](metaclass=SingletonMeta):
    """load json file with pydantic"""

    def __init__(self, class_d2o: type[T]):
        self.data = load_json_data(class_d2o)
        self.data_list = list(self.data.values())

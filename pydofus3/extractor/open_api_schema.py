import importlib
import inspect
import pkgutil
from pathlib import Path

import orjson

from pydofus3.generated import pydantic_d2o
from pydofus3.not_generated.base import D2oData


def collect_pydantic_models():
    models = {}

    for module_info in pkgutil.walk_packages(pydantic_d2o.__path__, pydantic_d2o.__name__ + '.'):
        module = importlib.import_module(module_info.name)
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, D2oData):
                models[name] = obj
    return models


def generate_openapi(output_path: Path):
    models = collect_pydantic_models()
    schemas = {}
    for name, model in models.items():
        schema = model.model_json_schema(ref_template='#/components/schemas/{model}')
        schemas[name] = schema
        if '$defs' in schema:
            for def_name, def_schema in schema.pop('$defs').items():
                schemas[def_name] = def_schema

    schemas = dict(sorted(schemas.items()))
    openapi_spec = {
        'openapi': '3.1.0',
        'info': {'title': 'Dofus datacenter schema', 'version': '1.0.0'},
        'components': {'schemas': schemas},
        'paths': {},
    }
    (output_path / 'openapi.json').write_bytes(orjson.dumps(openapi_spec))

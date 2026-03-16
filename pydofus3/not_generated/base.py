import math
from enum import IntEnum
from typing import Annotated, Any, ClassVar, get_args

from pydantic import BaseModel, BeforeValidator, ConfigDict, GetCoreSchemaHandler, GetJsonSchemaHandler, model_validator
from pydantic_core import CoreSchema, core_schema


class MyBaseModel(BaseModel):
    model_config = ConfigDict(extra='allow')


class D2oData(MyBaseModel):
    bundle_name: ClassVar[str]


class MetadataRoot[T](MyBaseModel):
    objectsById: dict[int, T]


class FlagBaseModel(BaseModel):
    @model_validator(mode='before')
    def set_enum(cls, data):
        if isinstance(data, dict):
            return data
        elif isinstance(data, int):
            return {key: bool(data & mask.__metadata__[0]) for key, mask in cls.__annotations__.items()}
        return data


def none_to_na(value):
    return math.nan if value is None else value


type float_nan = Annotated[float, BeforeValidator(none_to_na)]


def wrap_remove_values(value):
    return value['values'] if (isinstance(value, dict) and 'values' in value) else value


type WrappedList[T] = Annotated[list[T], BeforeValidator(wrap_remove_values)]


class OpenAPIIntEnum(IntEnum):
    """
    add description to enum for openapi schema
    """

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler):
        json_schema = handler(core_schema)
        json_schema['description'] = ', '.join(f'{v.value}: {v.name}' for v in cls)
        json_schema['x-enum-varnames'] = [v.name for v in cls]
        return json_schema


class SerializableDictionary[K, V](dict[K, V]):
    """
    adapt unity key-value dictionary to pydantic dictionary
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler: GetCoreSchemaHandler):
        key, value = cls._get_kv_types(source_type)
        schema = core_schema.dict_schema(handler(key), handler(value))
        return core_schema.no_info_before_validator_function(cls._validate, schema)

    @staticmethod
    def _validate(value: Any) -> Any:
        if isinstance(value, dict) and 'm_keys' in value and 'm_values' in value:
            value = dict(zip(value['m_keys'], value['m_values']))
        return value

    @classmethod
    def _get_kv_types(cls, source_type):
        args = get_args(source_type)
        if not args and hasattr(source_type, '__orig_bases__'):
            for base in source_type.__orig_bases__:
                if args := get_args(base):
                    break
        if len(args) != 2:
            raise TypeError(f'Cannot determine K and V types for {source_type}')
        return args

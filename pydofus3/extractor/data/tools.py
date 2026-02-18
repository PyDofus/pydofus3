from collections import defaultdict
from typing import Any, Iterable

from UnityPy import Environment
from UnityPy.classes import MonoBehaviour, MonoScript, Object, PPtr
from UnityPy.enums import ClassIDType
from UnityPy.files import ObjectReader


def process_references(data: dict) -> None:
    """
    replace managed reference element directly in the monobehaviour and build python dict for nested m_keys,m_values
    :param data: monobehaviour
    """

    def recursive_references(items: Iterable[tuple[str | int, Any]], data: list | dict) -> None:
        to_del = []
        for key, value in items:
            if isinstance(value, dict):
                if len(value) == 1 and 'rid' in value:
                    if elem := ref.get(value['rid']):
                        data[key] = elem
                    else:
                        to_del.append(key)
                elif len(value) == 2 and 'm_keys' in value and 'm_values' in value:
                    data[key] = dict(zip(value['m_keys'], value['m_values']))
                    recursive_references(data[key].items(), data[key])
                else:
                    recursive_references(value.items(), value)
            elif isinstance(value, list):
                recursive_references(enumerate(value), value)
        for key in to_del:
            del data[key]

    ref = {
        i['rid']: elem
        for i in data.get('references', {}).get('RefIds', [])
        if (elem := i.get('data')) and not elem.update(type_class=i.get('type'))
    }
    recursive_references(data.items(), data)
    data.pop('references', None)


def get_monoscript(obj: ObjectReader[MonoBehaviour]) -> ObjectReader[MonoScript] | None:
    script_type = obj.assets_file.script_types[obj.serialized_type.script_type_index]
    if script_type.local_serialized_file_index == 0:
        return obj.assets_file.objects[script_type.local_identifier_in_file]
    else:
        cab_name = obj.assets_file.externals[script_type.local_serialized_file_index - 1].name.lower()
        cab = obj.assets_file.environment.cabs.get(cab_name)
        if cab and (script := cab.objects.get(script_type.local_identifier_in_file)):
            return script
    return None


class BetterContainer:
    def __init__(self, env: Environment) -> None:
        self._data: dict[str, dict[ClassIDType, list[PPtr[Object]]]] = defaultdict(lambda: defaultdict(list))
        for k, asset in env.container.items():
            self._data[k][asset.type].append(asset)

    def get_asset_type(self, key: str, asset_type: ClassIDType) -> list[PPtr[Object]]:
        return self._data.get(key, {}).get(asset_type, [])

    def __getitem__(self, key: str) -> dict[ClassIDType, list[PPtr[Object]]]:
        return self._data[key]

    def __contains__(self, key: str) -> bool:
        return key in self._data

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

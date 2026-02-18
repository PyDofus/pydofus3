from pydofus3.generated.pydantic.Editor.AleCore.Data.AleRect import AleRect
from pydofus3.not_generated.base import MyBaseModel


class AtlasDictionary(MyBaseModel):
	m_keys: list[int]
	m_values: list[AleRect]


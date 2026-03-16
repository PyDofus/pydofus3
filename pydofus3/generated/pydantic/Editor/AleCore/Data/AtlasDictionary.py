from pydofus3.generated.pydantic.Editor.AleCore.Data.AleRect import AleRect

class AtlasDictionary(dict[int, AleRect]):
	m_keys: list[int]
	m_values: list[AleRect]


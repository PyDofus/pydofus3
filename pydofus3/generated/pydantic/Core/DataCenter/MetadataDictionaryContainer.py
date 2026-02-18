from pydofus3.not_generated.base import MyBaseModel


class MetadataDictionaryContainer[T](MyBaseModel):
	m_keys: list[int]
	m_values: list[T]


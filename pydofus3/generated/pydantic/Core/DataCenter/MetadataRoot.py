from pydofus3.generated.pydantic.Core.DataCenter.MetadataDictionaryContainer import MetadataDictionaryContainer
from pydofus3.not_generated.base import MyBaseModel

class MetadataRoot[T](MyBaseModel):
	objectsById: MetadataDictionaryContainer[T]


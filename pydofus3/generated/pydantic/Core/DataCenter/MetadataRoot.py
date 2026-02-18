from pydofus3.generated.pydantic.Core.DataCenter.IDataContainer import IDataContainer
from pydofus3.generated.pydantic.Core.DataCenter.MetadataDictionaryContainer import MetadataDictionaryContainer

class MetadataRoot[T](IDataContainer):
	objectsById: MetadataDictionaryContainer[T]


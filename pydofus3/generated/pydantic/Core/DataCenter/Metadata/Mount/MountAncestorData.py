from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Mount.MountData import MountData
from pydofus3.not_generated.base import MyBaseModel

from typing import Any

class MountAncestorData(MyBaseModel):
	mount: MountData
	mother: 'MountAncestorData'
	father: 'MountAncestorData'
	entityLook: Any


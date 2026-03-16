from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class OptionalFeatureData(D2oData):
	bundle_name: ClassVar[str] = "optionalfeaturesdataroot"

	id: int
	keyword: str
	isClient: bool
	isServer: bool
	isActivationOnLaunch: bool
	isActivationOnServerConnection: bool
	activationCriterions: str


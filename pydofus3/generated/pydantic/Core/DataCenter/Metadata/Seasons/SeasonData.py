from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n

class SeasonData(MyBaseModel):
	uid: int
	nameId: i18n
	beginning: float_nan
	closure: float_nan
	resetDate: float_nan
	flagObjectId: int


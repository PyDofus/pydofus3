from pydofus3.not_generated.base import MyBaseModel

class StagingEvolutiveVar[T](MyBaseModel):
	active: bool
	startValue: T
	maxValue: T


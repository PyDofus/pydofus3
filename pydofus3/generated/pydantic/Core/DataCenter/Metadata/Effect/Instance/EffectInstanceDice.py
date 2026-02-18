from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceInteger import EffectInstanceInteger

class EffectInstanceDice(EffectInstanceInteger):
	diceNum: int
	diceSide: int
	displayZero: bool


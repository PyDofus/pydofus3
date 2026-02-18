from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Item.ItemData import ItemData

class WeaponData(ItemData):
	criticalHitBonus: int
	minRange: int
	criticalHitProbability: int
	range: int
	castInLine: bool
	apCost: int
	castInDiagonal: bool
	castTestLos: bool
	maxCastPerTurn: int


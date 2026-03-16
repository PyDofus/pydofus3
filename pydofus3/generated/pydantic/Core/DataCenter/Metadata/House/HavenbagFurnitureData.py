from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.unity import Vector2Int
from typing import ClassVar

class HavenbagFurnitureData(D2oData):
	bundle_name: ClassVar[str] = "havenbagfurnituresdataroot"

	typeId: int
	themeId: int
	elementId: int
	color: int
	skillId: int
	layerId: int
	blocksMovement: bool
	isStackable: bool
	cellsWidth: int
	cellsHeight: int
	order: int
	gfxId: int
	height: int
	horizontalSymmetry: bool
	origin: Vector2Int
	size: Vector2Int


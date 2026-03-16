from enum import IntEnum

class AnimationMaskType(IntEnum):
	None_ = 0
	Bounds = 1
	Symbol = 2

class BufferState(IntEnum):
	Ready = 0
	Running = 1
	Pending = 2

class FlashFilters:
	class FilterType(IntEnum):
		Blur = 0
		Glow = 1
		DropShadow = 2
		ColorMatrix = 3

class FlashMaskState(IntEnum):
	None_ = 0
	SetMask = 1
	ObeyMask = 2
	ClearMask = 3

class PrepassTextureType(IntEnum):
	Collection = 0
	Individual = 1

class ShaderConstants:
	class OutlineTestDiff(IntEnum):
		CROSS_2_SIDES = 0
		CROSS_FROM_CENTER = 1
		CROSS_AROUND = 2
		OUTLINE_MASK = 3

	class RenderingLayerIDs(IntEnum):
		DEFAULT = 1
		REFRACTION = 2
		INLINE = 4
		OUTLINE = 8
		WAVE = 16


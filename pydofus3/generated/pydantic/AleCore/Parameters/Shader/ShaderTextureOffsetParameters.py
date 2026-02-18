from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.UVModes import UVModes
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.generated.pydantic.AleCore.Utils.TextureOffsetType import TextureOffsetType
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderTextureOffsetParameters(IShaderParameters):
	textureOffsetType: Annotated[Union[TextureOffsetType, int], Field(union_mode='left_to_right')]
	texUVMode: Annotated[Union[UVModes, int], Field(union_mode='left_to_right')]
	texTiling: AleVector2
	tile: float_nan
	texOffset: AleVector2
	direction: AleVector2
	directionSpeed: float_nan
	flowmapID: int
	flowmapSpeed: float_nan
	flowmapPower: float_nan


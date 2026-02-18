from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Parameters.PostProcess.IPostProcessParameters import IPostProcessParameters
from pydofus3.generated.pydantic.AleCore.Utils.FilmGrainType import FilmGrainType
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class PPFilmGrainParameters(IPostProcessParameters):
	type: Annotated[Union[FilmGrainType, int], Field(union_mode='left_to_right')]
	intensity: float_nan
	response: float_nan


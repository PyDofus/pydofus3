from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Utils.FilmGrainType import FilmGrainType
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class PPFilmGrainParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Film Grain"
	type: Annotated[Union[FilmGrainType, int], Field(union_mode='left_to_right')]
	intensity: float_nan
	response: float_nan


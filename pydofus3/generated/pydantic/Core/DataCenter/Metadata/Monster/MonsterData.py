from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.AnimFunMonsterData import AnimFunMonsterData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterDropData import MonsterDropData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterFlags import MonsterFlags
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterGlobalDropData import MonsterGlobalDropData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterGradeData import MonsterGradeData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterSoulData import MonsterSoulData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class MonsterData(D2oData):
	bundle_name: ClassVar[str] = "monstersdataroot"

	m_flags: MonsterFlags
	id: int
	nameId: i18n
	gfxId: int
	race: int
	grades: list[MonsterGradeData]
	look: str
	animFunList: list[AnimFunMonsterData]
	drops: list[MonsterDropData]
	temporisDrops: list[MonsterDropData]
	globalDrops: list[MonsterGlobalDropData]
	subareas: list[int]
	spells: list[int]
	spellGrades: list[str]
	favoriteSubareaId: int
	correspondingMiniBossId: int
	speedAdjust: int
	creatureBoneId: int
	summonCost: int
	incompatibleIdols: list[int]
	incompatibleChallenges: list[int]
	aggressiveZoneSize: int
	aggressiveLevelDiff: int
	aggressiveImmunityCriterion: str
	aggressiveAttackDelay: int
	scaleGradeRef: int
	characRatios: list[WrappedList[float_nan]]
	isBounty: bool
	souls: list[MonsterSoulData]


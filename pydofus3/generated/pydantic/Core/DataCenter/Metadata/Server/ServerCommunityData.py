from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class ServerCommunityData(D2oData):
	bundle_name: ClassVar[str] = "servercommunitiesdataroot"

	id: int
	nameId: i18n
	defaultCountries: list[str]
	shortId: str
	supportedLangIds: list[int]
	namingRulePlayerNameId: int
	namingRuleGuildNameId: int
	namingRuleAllianceNameId: int
	namingRuleAllianceTagId: int
	namingRulePartyNameId: int
	namingRuleMountNameId: int
	namingRuleNameGeneratorId: int
	namingRuleAdminId: int
	namingRuleModoId: int
	namingRulePresetNameId: int


from fastapi import FastAPI
from pydofus3.generated.datacenter import Datacenter
from pydofus3.generated.pydantic_d2o import Alignment, Alliance, Almanax, Alterations, Appearance, Arena, Bonus, Breach, Breed, Calendar, Card, Challenge, Characteristic, Collection, Communication, Constant, Document, Effect, ExternalNotification, Feature, Guild, GuildMission, House, InfiniteDreams, Interactive, Item, Job, LivingObjects, Lobby, Misc, Monster, Mount, Notification, Npc, OptionalFeatures, Popup, Progression, Quest, Raid, Ride, Scenarios, Seasons, Server, Social, Sound, Spell, TradeCenter, TreasureHunt, World

data = Datacenter()
app = FastAPI()

# @formatter:off
@app.get("/AlignmentGiftData", tags=["Alignment"])
async def AlignmentGiftData() -> list[Alignment.AlignmentGiftData]:
    return data.AlignmentGiftData
@app.get("/AlignmentOrderData", tags=["Alignment"])
async def AlignmentOrderData() -> list[Alignment.AlignmentOrderData]:
    return data.AlignmentOrderData
@app.get("/AlignmentRankData", tags=["Alignment"])
async def AlignmentRankData() -> list[Alignment.AlignmentRankData]:
    return data.AlignmentRankData
@app.get("/AlignmentRankGiftsData", tags=["Alignment"])
async def AlignmentRankGiftsData() -> list[Alignment.AlignmentRankGiftsData]:
    return data.AlignmentRankGiftsData
@app.get("/AlignmentSideData", tags=["Alignment"])
async def AlignmentSideData() -> list[Alignment.AlignmentSideData]:
    return data.AlignmentSideData
@app.get("/AlignmentTitleData", tags=["Alignment"])
async def AlignmentTitleData() -> list[Alignment.AlignmentTitleData]:
    return data.AlignmentTitleData
@app.get("/AllianceRankData", tags=["Alliance"])
async def AllianceRankData() -> list[Alliance.AllianceRankData]:
    return data.AllianceRankData
@app.get("/AllianceRankNameSuggestionData", tags=["Alliance"])
async def AllianceRankNameSuggestionData() -> list[Alliance.AllianceRankNameSuggestionData]:
    return data.AllianceRankNameSuggestionData
@app.get("/AllianceRightData", tags=["Alliance"])
async def AllianceRightData() -> list[Alliance.AllianceRightData]:
    return data.AllianceRightData
@app.get("/AllianceRightGroupData", tags=["Alliance"])
async def AllianceRightGroupData() -> list[Alliance.AllianceRightGroupData]:
    return data.AllianceRightGroupData
@app.get("/AllianceTagData", tags=["Alliance"])
async def AllianceTagData() -> list[Alliance.AllianceTagData]:
    return data.AllianceTagData
@app.get("/AllianceTagTypeData", tags=["Alliance"])
async def AllianceTagTypeData() -> list[Alliance.AllianceTagTypeData]:
    return data.AllianceTagTypeData
@app.get("/KothRoleData", tags=["Alliance"])
async def KothRoleData() -> list[Alliance.KothRoleData]:
    return data.KothRoleData
@app.get("/AlmanaxCalendarData", tags=["Almanax"])
async def AlmanaxCalendarData() -> list[Almanax.AlmanaxCalendarData]:
    return data.AlmanaxCalendarData
@app.get("/AlmanaxCategoryData", tags=["Almanax"])
async def AlmanaxCategoryData() -> list[Almanax.AlmanaxCategoryData]:
    return data.AlmanaxCategoryData
@app.get("/AlmanaxZodiacData", tags=["Almanax"])
async def AlmanaxZodiacData() -> list[Almanax.AlmanaxZodiacData]:
    return data.AlmanaxZodiacData
@app.get("/AlterationCategoryData", tags=["Alterations"])
async def AlterationCategoryData() -> list[Alterations.AlterationCategoryData]:
    return data.AlterationCategoryData
@app.get("/AlterationData", tags=["Alterations"])
async def AlterationData() -> list[Alterations.AlterationData]:
    return data.AlterationData
@app.get("/AppearanceData", tags=["Appearance"])
async def AppearanceData() -> list[Appearance.AppearanceData]:
    return data.AppearanceData
@app.get("/CreatureBoneOverrideData", tags=["Appearance"])
async def CreatureBoneOverrideData() -> list[Appearance.CreatureBoneOverrideData]:
    return data.CreatureBoneOverrideData
@app.get("/CreatureBoneTypeData", tags=["Appearance"])
async def CreatureBoneTypeData() -> list[Appearance.CreatureBoneTypeData]:
    return data.CreatureBoneTypeData
@app.get("/IdleData", tags=["Appearance"])
async def IdleData() -> list[Appearance.IdleData]:
    return data.IdleData
@app.get("/OrnamentData", tags=["Appearance"])
async def OrnamentData() -> list[Appearance.OrnamentData]:
    return data.OrnamentData
@app.get("/RiderBoneData", tags=["Appearance"])
async def RiderBoneData() -> list[Appearance.RiderBoneData]:
    return data.RiderBoneData
@app.get("/SkinMappingData", tags=["Appearance"])
async def SkinMappingData() -> list[Appearance.SkinMappingData]:
    return data.SkinMappingData
@app.get("/SkinPositionData", tags=["Appearance"])
async def SkinPositionData() -> list[Appearance.SkinPositionData]:
    return data.SkinPositionData
@app.get("/SkinSlotRuleData", tags=["Appearance"])
async def SkinSlotRuleData() -> list[Appearance.SkinSlotRuleData]:
    return data.SkinSlotRuleData
@app.get("/TitleCategoryData", tags=["Appearance"])
async def TitleCategoryData() -> list[Appearance.TitleCategoryData]:
    return data.TitleCategoryData
@app.get("/TitleData", tags=["Appearance"])
async def TitleData() -> list[Appearance.TitleData]:
    return data.TitleData
@app.get("/ArenaLeagueData", tags=["Arena"])
async def ArenaLeagueData() -> list[Arena.ArenaLeagueData]:
    return data.ArenaLeagueData
@app.get("/BonusCriterionData", tags=["Bonus"])
async def BonusCriterionData() -> list[Bonus.BonusCriterionData]:
    return data.BonusCriterionData
@app.get("/BonusData", tags=["Bonus"])
async def BonusData() -> list[Bonus.BonusData]:
    return data.BonusData
@app.get("/BreachBossData", tags=["Breach"])
async def BreachBossData() -> list[Breach.BreachBossData]:
    return data.BreachBossData
@app.get("/BreachDungeonModificatorData", tags=["Breach"])
async def BreachDungeonModificatorData() -> list[Breach.BreachDungeonModificatorData]:
    return data.BreachDungeonModificatorData
@app.get("/BreachPrizeData", tags=["Breach"])
async def BreachPrizeData() -> list[Breach.BreachPrizeData]:
    return data.BreachPrizeData
@app.get("/BreachWorldMapCoordinateData", tags=["Breach"])
async def BreachWorldMapCoordinateData() -> list[Breach.BreachWorldMapCoordinateData]:
    return data.BreachWorldMapCoordinateData
@app.get("/BreachWorldMapSectorData", tags=["Breach"])
async def BreachWorldMapSectorData() -> list[Breach.BreachWorldMapSectorData]:
    return data.BreachWorldMapSectorData
@app.get("/BodyData", tags=["Breed"])
async def BodyData() -> list[Breed.BodyData]:
    return data.BodyData
@app.get("/BreedData", tags=["Breed"])
async def BreedData() -> list[Breed.BreedData]:
    return data.BreedData
@app.get("/BreedRoleData", tags=["Breed"])
async def BreedRoleData() -> list[Breed.BreedRoleData]:
    return data.BreedRoleData
@app.get("/HeadData", tags=["Breed"])
async def HeadData() -> list[Breed.HeadData]:
    return data.HeadData
@app.get("/CalendarEventData", tags=["Calendar"])
async def CalendarEventData() -> list[Calendar.CalendarEventData]:
    return data.CalendarEventData
@app.get("/CardBackgroundData", tags=["Card"])
async def CardBackgroundData() -> list[Card.CardBackgroundData]:
    return data.CardBackgroundData
@app.get("/ChallengeData", tags=["Challenge"])
async def ChallengeData() -> list[Challenge.ChallengeData]:
    return data.ChallengeData
@app.get("/CharacteristicCategoryData", tags=["Characteristic"])
async def CharacteristicCategoryData() -> list[Characteristic.CharacteristicCategoryData]:
    return data.CharacteristicCategoryData
@app.get("/CharacteristicData", tags=["Characteristic"])
async def CharacteristicData() -> list[Characteristic.CharacteristicData]:
    return data.CharacteristicData
@app.get("/CollectableData", tags=["Collection"])
async def CollectableData() -> list[Collection.CollectableData]:
    return data.CollectableData
@app.get("/CollectionData", tags=["Collection"])
async def CollectionData() -> list[Collection.CollectionData]:
    return data.CollectionData
@app.get("/ChatChannelData", tags=["Communication"])
async def ChatChannelData() -> list[Communication.ChatChannelData]:
    return data.ChatChannelData
@app.get("/EmoticonData", tags=["Communication"])
async def EmoticonData() -> list[Communication.EmoticonData]:
    return data.EmoticonData
@app.get("/InfoMessageData", tags=["Communication"])
async def InfoMessageData() -> list[Communication.InfoMessageData]:
    return data.InfoMessageData
@app.get("/NamingRuleData", tags=["Communication"])
async def NamingRuleData() -> list[Communication.NamingRuleData]:
    return data.NamingRuleData
@app.get("/SmileyData", tags=["Communication"])
async def SmileyData() -> list[Communication.SmileyData]:
    return data.SmileyData
@app.get("/SmileyPackData", tags=["Communication"])
async def SmileyPackData() -> list[Communication.SmileyPackData]:
    return data.SmileyPackData
@app.get("/ConstantData", tags=["Constant"])
async def ConstantData() -> list[Constant.ConstantData]:
    return data.ConstantData
@app.get("/DocumentData", tags=["Document"])
async def DocumentData() -> list[Document.DocumentData]:
    return data.DocumentData
@app.get("/ActionFilterData", tags=["Effect"])
async def ActionFilterData() -> list[Effect.ActionFilterData]:
    return data.ActionFilterData
@app.get("/EffectData", tags=["Effect"])
async def EffectData() -> list[Effect.EffectData]:
    return data.EffectData
@app.get("/EvolutiveEffectData", tags=["Effect"])
async def EvolutiveEffectData() -> list[Effect.EvolutiveEffectData]:
    return data.EvolutiveEffectData
@app.get("/ExternalNotificationData", tags=["ExternalNotification"])
async def ExternalNotificationData() -> list[ExternalNotification.ExternalNotificationData]:
    return data.ExternalNotificationData
@app.get("/OptionalFeatureData", tags=["Feature"])
async def OptionalFeatureData() -> list[Feature.OptionalFeatureData]:
    return data.OptionalFeatureData
@app.get("/EmblemBackgroundData", tags=["Guild"])
async def EmblemBackgroundData() -> list[Guild.EmblemBackgroundData]:
    return data.EmblemBackgroundData
@app.get("/EmblemSymbolCategoryData", tags=["Guild"])
async def EmblemSymbolCategoryData() -> list[Guild.EmblemSymbolCategoryData]:
    return data.EmblemSymbolCategoryData
@app.get("/EmblemSymbolData", tags=["Guild"])
async def EmblemSymbolData() -> list[Guild.EmblemSymbolData]:
    return data.EmblemSymbolData
@app.get("/GuildChestTabData", tags=["Guild"])
async def GuildChestTabData() -> list[Guild.GuildChestTabData]:
    return data.GuildChestTabData
@app.get("/GuildHallData", tags=["Guild"])
async def GuildHallData() -> list[Guild.GuildHallData]:
    return data.GuildHallData
@app.get("/GuildHallThemeData", tags=["Guild"])
async def GuildHallThemeData() -> list[Guild.GuildHallThemeData]:
    return data.GuildHallThemeData
@app.get("/GuildLevelRewardData", tags=["Guild"])
async def GuildLevelRewardData() -> list[Guild.GuildLevelRewardData]:
    return data.GuildLevelRewardData
@app.get("/GuildRankData", tags=["Guild"])
async def GuildRankData() -> list[Guild.GuildRankData]:
    return data.GuildRankData
@app.get("/GuildRankNameSuggestionData", tags=["Guild"])
async def GuildRankNameSuggestionData() -> list[Guild.GuildRankNameSuggestionData]:
    return data.GuildRankNameSuggestionData
@app.get("/GuildRightData", tags=["Guild"])
async def GuildRightData() -> list[Guild.GuildRightData]:
    return data.GuildRightData
@app.get("/GuildRightGroupData", tags=["Guild"])
async def GuildRightGroupData() -> list[Guild.GuildRightGroupData]:
    return data.GuildRightGroupData
@app.get("/GuildShopBoostData", tags=["Guild"])
async def GuildShopBoostData() -> list[Guild.GuildShopBoostData]:
    return data.GuildShopBoostData
@app.get("/GuildTagData", tags=["Guild"])
async def GuildTagData() -> list[Guild.GuildTagData]:
    return data.GuildTagData
@app.get("/GuildTagTypeData", tags=["Guild"])
async def GuildTagTypeData() -> list[Guild.GuildTagTypeData]:
    return data.GuildTagTypeData
@app.get("/GuildMissionActivityData", tags=["GuildMission"])
async def GuildMissionActivityData() -> list[GuildMission.GuildMissionActivityData]:
    return data.GuildMissionActivityData
@app.get("/GuildMissionData", tags=["GuildMission"])
async def GuildMissionData() -> list[GuildMission.GuildMissionData]:
    return data.GuildMissionData
@app.get("/GuildMissionGradeData", tags=["GuildMission"])
async def GuildMissionGradeData() -> list[GuildMission.GuildMissionGradeData]:
    return data.GuildMissionGradeData
@app.get("/GuildMissionMilestoneData", tags=["GuildMission"])
async def GuildMissionMilestoneData() -> list[GuildMission.GuildMissionMilestoneData]:
    return data.GuildMissionMilestoneData
@app.get("/GuildMissionMilestoneRewardData", tags=["GuildMission"])
async def GuildMissionMilestoneRewardData() -> list[GuildMission.GuildMissionMilestoneRewardData]:
    return data.GuildMissionMilestoneRewardData
@app.get("/GuildMissionObjectiveData", tags=["GuildMission"])
async def GuildMissionObjectiveData() -> list[GuildMission.GuildMissionObjectiveData]:
    return data.GuildMissionObjectiveData
@app.get("/GuildMissionRankData", tags=["GuildMission"])
async def GuildMissionRankData() -> list[GuildMission.GuildMissionRankData]:
    return data.GuildMissionRankData
@app.get("/GuildMissionSuperCategoryData", tags=["GuildMission"])
async def GuildMissionSuperCategoryData() -> list[GuildMission.GuildMissionSuperCategoryData]:
    return data.GuildMissionSuperCategoryData
@app.get("/HavenbagFurnitureData", tags=["House"])
async def HavenbagFurnitureData() -> list[House.HavenbagFurnitureData]:
    return data.HavenbagFurnitureData
@app.get("/HavenbagThemeData", tags=["House"])
async def HavenbagThemeData() -> list[House.HavenbagThemeData]:
    return data.HavenbagThemeData
@app.get("/HouseData", tags=["House"])
async def HouseData() -> list[House.HouseData]:
    return data.HouseData
@app.get("/InfiniteDreamIntensityData", tags=["InfiniteDreams"])
async def InfiniteDreamIntensityData() -> list[InfiniteDreams.InfiniteDreamIntensityData]:
    return data.InfiniteDreamIntensityData
@app.get("/InfiniteDreamRewardActionData", tags=["InfiniteDreams"])
async def InfiniteDreamRewardActionData() -> list[InfiniteDreams.InfiniteDreamRewardActionData]:
    return data.InfiniteDreamRewardActionData
@app.get("/InfiniteDreamRewardData", tags=["InfiniteDreams"])
async def InfiniteDreamRewardData() -> list[InfiniteDreams.InfiniteDreamRewardData]:
    return data.InfiniteDreamRewardData
@app.get("/InfiniteDreamTrialData", tags=["InfiniteDreams"])
async def InfiniteDreamTrialData() -> list[InfiniteDreams.InfiniteDreamTrialData]:
    return data.InfiniteDreamTrialData
@app.get("/InteractiveData", tags=["Interactive"])
async def InteractiveData() -> list[Interactive.InteractiveData]:
    return data.InteractiveData
@app.get("/SignsData", tags=["Interactive"])
async def SignsData() -> list[Interactive.SignsData]:
    return data.SignsData
@app.get("/SkillNameData", tags=["Interactive"])
async def SkillNameData() -> list[Interactive.SkillNameData]:
    return data.SkillNameData
@app.get("/StealthBoneData", tags=["Interactive"])
async def StealthBoneData() -> list[Interactive.StealthBoneData]:
    return data.StealthBoneData
@app.get("/EvolutiveItemTypeData", tags=["Item"])
async def EvolutiveItemTypeData() -> list[Item.EvolutiveItemTypeData]:
    return data.EvolutiveItemTypeData
@app.get("/ItemData", tags=["Item"])
async def ItemData() -> list[Item.ItemData]:
    return data.ItemData
@app.get("/ItemSetData", tags=["Item"])
async def ItemSetData() -> list[Item.ItemSetData]:
    return data.ItemSetData
@app.get("/ItemSuperTypeData", tags=["Item"])
async def ItemSuperTypeData() -> list[Item.ItemSuperTypeData]:
    return data.ItemSuperTypeData
@app.get("/ItemTypeData", tags=["Item"])
async def ItemTypeData() -> list[Item.ItemTypeData]:
    return data.ItemTypeData
@app.get("/LegendaryPowerCategoryData", tags=["Item"])
async def LegendaryPowerCategoryData() -> list[Item.LegendaryPowerCategoryData]:
    return data.LegendaryPowerCategoryData
@app.get("/PresetIconData", tags=["Item"])
async def PresetIconData() -> list[Item.PresetIconData]:
    return data.PresetIconData
@app.get("/RandomDropGroupData", tags=["Item"])
async def RandomDropGroupData() -> list[Item.RandomDropGroupData]:
    return data.RandomDropGroupData
@app.get("/VeteranRewardData", tags=["Item"])
async def VeteranRewardData() -> list[Item.VeteranRewardData]:
    return data.VeteranRewardData
@app.get("/JobData", tags=["Job"])
async def JobData() -> list[Job.JobData]:
    return data.JobData
@app.get("/RecipeData", tags=["Job"])
async def RecipeData() -> list[Job.RecipeData]:
    return data.RecipeData
@app.get("/SkillData", tags=["Job"])
async def SkillData() -> list[Job.SkillData]:
    return data.SkillData
@app.get("/LivingObjectSkinMoodsData", tags=["LivingObjects"])
async def LivingObjectSkinMoodsData() -> list[LivingObjects.LivingObjectSkinMoodsData]:
    return data.LivingObjectSkinMoodsData
@app.get("/SpeakingItemTextData", tags=["LivingObjects"])
async def SpeakingItemTextData() -> list[LivingObjects.SpeakingItemTextData]:
    return data.SpeakingItemTextData
@app.get("/SpeakingItemTriggerData", tags=["LivingObjects"])
async def SpeakingItemTriggerData() -> list[LivingObjects.SpeakingItemTriggerData]:
    return data.SpeakingItemTriggerData
@app.get("/LobbyTagData", tags=["Lobby"])
async def LobbyTagData() -> list[Lobby.LobbyTagData]:
    return data.LobbyTagData
@app.get("/LobbyTypeData", tags=["Lobby"])
async def LobbyTypeData() -> list[Lobby.LobbyTypeData]:
    return data.LobbyTypeData
@app.get("/CharacterXpMappingData", tags=["Misc"])
async def CharacterXpMappingData() -> list[Misc.CharacterXpMappingData]:
    return data.CharacterXpMappingData
@app.get("/ChoiceData", tags=["Misc"])
async def ChoiceData() -> list[Misc.ChoiceData]:
    return data.ChoiceData
@app.get("/LuaFormulaData", tags=["Misc"])
async def LuaFormulaData() -> list[Misc.LuaFormulaData]:
    return data.LuaFormulaData
@app.get("/MonthData", tags=["Misc"])
async def MonthData() -> list[Misc.MonthData]:
    return data.MonthData
@app.get("/TextIconReferenceData", tags=["Misc"])
async def TextIconReferenceData() -> list[Misc.TextIconReferenceData]:
    return data.TextIconReferenceData
@app.get("/CompanionCharacteristicData", tags=["Monster"])
async def CompanionCharacteristicData() -> list[Monster.CompanionCharacteristicData]:
    return data.CompanionCharacteristicData
@app.get("/CompanionData", tags=["Monster"])
async def CompanionData() -> list[Monster.CompanionData]:
    return data.CompanionData
@app.get("/CompanionSpellData", tags=["Monster"])
async def CompanionSpellData() -> list[Monster.CompanionSpellData]:
    return data.CompanionSpellData
@app.get("/MonsterData", tags=["Monster"])
async def MonsterData() -> list[Monster.MonsterData]:
    return data.MonsterData
@app.get("/MonsterMiniBossData", tags=["Monster"])
async def MonsterMiniBossData() -> list[Monster.MonsterMiniBossData]:
    return data.MonsterMiniBossData
@app.get("/MonsterRaceData", tags=["Monster"])
async def MonsterRaceData() -> list[Monster.MonsterRaceData]:
    return data.MonsterRaceData
@app.get("/MonsterSoulData", tags=["Monster"])
async def MonsterSoulData() -> list[Monster.MonsterSoulData]:
    return data.MonsterSoulData
@app.get("/MonsterSuperRaceData", tags=["Monster"])
async def MonsterSuperRaceData() -> list[Monster.MonsterSuperRaceData]:
    return data.MonsterSuperRaceData
@app.get("/MountBehaviorData", tags=["Mount"])
async def MountBehaviorData() -> list[Mount.MountBehaviorData]:
    return data.MountBehaviorData
@app.get("/MountBoneData", tags=["Mount"])
async def MountBoneData() -> list[Mount.MountBoneData]:
    return data.MountBoneData
@app.get("/MountData", tags=["Mount"])
async def MountData() -> list[Mount.MountData]:
    return data.MountData
@app.get("/MountFamilyData", tags=["Mount"])
async def MountFamilyData() -> list[Mount.MountFamilyData]:
    return data.MountFamilyData
@app.get("/RideFoodData", tags=["Mount"])
async def RideFoodData() -> list[Mount.RideFoodData]:
    return data.RideFoodData
@app.get("/NotificationData", tags=["Notification"])
async def NotificationData() -> list[Notification.NotificationData]:
    return data.NotificationData
@app.get("/NpcActionData", tags=["Npc"])
async def NpcActionData() -> list[Npc.NpcActionData]:
    return data.NpcActionData
@app.get("/NpcData", tags=["Npc"])
async def NpcData() -> list[Npc.NpcData]:
    return data.NpcData
@app.get("/NpcDialogSkinData", tags=["Npc"])
async def NpcDialogSkinData() -> list[Npc.NpcDialogSkinData]:
    return data.NpcDialogSkinData
@app.get("/NpcMessageData", tags=["Npc"])
async def NpcMessageData() -> list[Npc.NpcMessageData]:
    return data.NpcMessageData
@app.get("/TaxCollectorFirstnameData", tags=["Npc"])
async def TaxCollectorFirstnameData() -> list[Npc.TaxCollectorFirstnameData]:
    return data.TaxCollectorFirstnameData
@app.get("/TaxCollectorNameData", tags=["Npc"])
async def TaxCollectorNameData() -> list[Npc.TaxCollectorNameData]:
    return data.TaxCollectorNameData
@app.get("/CustomModeBreedSpellData", tags=["OptionalFeatures"])
async def CustomModeBreedSpellData() -> list[OptionalFeatures.CustomModeBreedSpellData]:
    return data.CustomModeBreedSpellData
@app.get("/ForgettableSpellData", tags=["OptionalFeatures"])
async def ForgettableSpellData() -> list[OptionalFeatures.ForgettableSpellData]:
    return data.ForgettableSpellData
@app.get("/ModsterData", tags=["OptionalFeatures"])
async def ModsterData() -> list[OptionalFeatures.ModsterData]:
    return data.ModsterData
@app.get("/ProgressingAchievementSeasonData", tags=["OptionalFeatures"])
async def ProgressingAchievementSeasonData() -> list[OptionalFeatures.ProgressingAchievementSeasonData]:
    return data.ProgressingAchievementSeasonData
@app.get("/ProgressingAchievementStepData", tags=["OptionalFeatures"])
async def ProgressingAchievementStepData() -> list[OptionalFeatures.ProgressingAchievementStepData]:
    return data.ProgressingAchievementStepData
@app.get("/PopupInformationData", tags=["Popup"])
async def PopupInformationData() -> list[Popup.PopupInformationData]:
    return data.PopupInformationData
@app.get("/ActivitySuggestionCategoryData", tags=["Progression"])
async def ActivitySuggestionCategoryData() -> list[Progression.ActivitySuggestionCategoryData]:
    return data.ActivitySuggestionCategoryData
@app.get("/ActivitySuggestionData", tags=["Progression"])
async def ActivitySuggestionData() -> list[Progression.ActivitySuggestionData]:
    return data.ActivitySuggestionData
@app.get("/DofusProgressionData", tags=["Progression"])
async def DofusProgressionData() -> list[Progression.DofusProgressionData]:
    return data.DofusProgressionData
@app.get("/FeatureDescriptionData", tags=["Progression"])
async def FeatureDescriptionData() -> list[Progression.FeatureDescriptionData]:
    return data.FeatureDescriptionData
@app.get("/AchievementCategoryData", tags=["Quest"])
async def AchievementCategoryData() -> list[Quest.AchievementCategoryData]:
    return data.AchievementCategoryData
@app.get("/AchievementData", tags=["Quest"])
async def AchievementData() -> list[Quest.AchievementData]:
    return data.AchievementData
@app.get("/AchievementObjectiveData", tags=["Quest"])
async def AchievementObjectiveData() -> list[Quest.AchievementObjectiveData]:
    return data.AchievementObjectiveData
@app.get("/AchievementRewardData", tags=["Quest"])
async def AchievementRewardData() -> list[Quest.AchievementRewardData]:
    return data.AchievementRewardData
@app.get("/QuestCategoryData", tags=["Quest"])
async def QuestCategoryData() -> list[Quest.QuestCategoryData]:
    return data.QuestCategoryData
@app.get("/QuestData", tags=["Quest"])
async def QuestData() -> list[Quest.QuestData]:
    return data.QuestData
@app.get("/QuestObjectiveData", tags=["Quest"])
async def QuestObjectiveData() -> list[Quest.QuestObjectiveData]:
    return data.QuestObjectiveData
@app.get("/QuestObjectiveTypeData", tags=["Quest"])
async def QuestObjectiveTypeData() -> list[Quest.QuestObjectiveTypeData]:
    return data.QuestObjectiveTypeData
@app.get("/QuestStepData", tags=["Quest"])
async def QuestStepData() -> list[Quest.QuestStepData]:
    return data.QuestStepData
@app.get("/QuestStepRewardData", tags=["Quest"])
async def QuestStepRewardData() -> list[Quest.QuestStepRewardData]:
    return data.QuestStepRewardData
@app.get("/GuildRaidData", tags=["Raid"])
async def GuildRaidData() -> list[Raid.GuildRaidData]:
    return data.GuildRaidData
@app.get("/GuildRaidsGoalData", tags=["Raid"])
async def GuildRaidsGoalData() -> list[Raid.GuildRaidsGoalData]:
    return data.GuildRaidsGoalData
@app.get("/GuildRaidsGroupData", tags=["Raid"])
async def GuildRaidsGroupData() -> list[Raid.GuildRaidsGroupData]:
    return data.GuildRaidsGroupData
@app.get("/GuildRaidsReward", tags=["Raid"])
async def GuildRaidsReward() -> list[Raid.GuildRaidsReward]:
    return data.GuildRaidsReward
@app.get("/PaddockGaugesData", tags=["Ride"])
async def PaddockGaugesData() -> list[Ride.PaddockGaugesData]:
    return data.PaddockGaugesData
@app.get("/PaddocksData", tags=["Ride"])
async def PaddocksData() -> list[Ride.PaddocksData]:
    return data.PaddocksData
@app.get("/RideGaugesData", tags=["Ride"])
async def RideGaugesData() -> list[Ride.RideGaugesData]:
    return data.RideGaugesData
@app.get("/RideSpeciesData", tags=["Ride"])
async def RideSpeciesData() -> list[Ride.RideSpeciesData]:
    return data.RideSpeciesData
@app.get("/RidesData", tags=["Ride"])
async def RidesData() -> list[Ride.RidesData]:
    return data.RidesData
@app.get("/FightScenarioData", tags=["Scenarios"])
async def FightScenarioData() -> list[Scenarios.FightScenarioData]:
    return data.FightScenarioData
@app.get("/ArenaLeagueSeasonData", tags=["Seasons"])
async def ArenaLeagueSeasonData() -> list[Seasons.ArenaLeagueSeasonData]:
    return data.ArenaLeagueSeasonData
@app.get("/ExpeditionSeasonData", tags=["Seasons"])
async def ExpeditionSeasonData() -> list[Seasons.ExpeditionSeasonData]:
    return data.ExpeditionSeasonData
@app.get("/ServerSeasonData", tags=["Seasons"])
async def ServerSeasonData() -> list[Seasons.ServerSeasonData]:
    return data.ServerSeasonData
@app.get("/ServerCommunityData", tags=["Server"])
async def ServerCommunityData() -> list[Server.ServerCommunityData]:
    return data.ServerCommunityData
@app.get("/ServerData", tags=["Server"])
async def ServerData() -> list[Server.ServerData]:
    return data.ServerData
@app.get("/ServerGameTypeData", tags=["Server"])
async def ServerGameTypeData() -> list[Server.ServerGameTypeData]:
    return data.ServerGameTypeData
@app.get("/ServerLangData", tags=["Server"])
async def ServerLangData() -> list[Server.ServerLangData]:
    return data.ServerLangData
@app.get("/ServerPopulationData", tags=["Server"])
async def ServerPopulationData() -> list[Server.ServerPopulationData]:
    return data.ServerPopulationData
@app.get("/SocialTagData", tags=["Social"])
async def SocialTagData() -> list[Social.SocialTagData]:
    return data.SocialTagData
@app.get("/SocialTagTypeData", tags=["Social"])
async def SocialTagTypeData() -> list[Social.SocialTagTypeData]:
    return data.SocialTagTypeData
@app.get("/SoundBoneData", tags=["Sound"])
async def SoundBoneData() -> list[Sound.SoundBoneData]:
    return data.SoundBoneData
@app.get("/SpellBombData", tags=["Spell"])
async def SpellBombData() -> list[Spell.SpellBombData]:
    return data.SpellBombData
@app.get("/SpellBombWallData", tags=["Spell"])
async def SpellBombWallData() -> list[Spell.SpellBombWallData]:
    return data.SpellBombWallData
@app.get("/SpellData", tags=["Spell"])
async def SpellData() -> list[Spell.SpellData]:
    return data.SpellData
@app.get("/SpellLevelData", tags=["Spell"])
async def SpellLevelData() -> list[Spell.SpellLevelData]:
    return data.SpellLevelData
@app.get("/SpellPairData", tags=["Spell"])
async def SpellPairData() -> list[Spell.SpellPairData]:
    return data.SpellPairData
@app.get("/SpellScriptData", tags=["Spell"])
async def SpellScriptData() -> list[Spell.SpellScriptData]:
    return data.SpellScriptData
@app.get("/SpellStateData", tags=["Spell"])
async def SpellStateData() -> list[Spell.SpellStateData]:
    return data.SpellStateData
@app.get("/SpellTypeData", tags=["Spell"])
async def SpellTypeData() -> list[Spell.SpellTypeData]:
    return data.SpellTypeData
@app.get("/SpellVariantData", tags=["Spell"])
async def SpellVariantData() -> list[Spell.SpellVariantData]:
    return data.SpellVariantData
@app.get("/AuctionHouseData", tags=["TradeCenter"])
async def AuctionHouseData() -> list[TradeCenter.AuctionHouseData]:
    return data.AuctionHouseData
@app.get("/LegendaryTreasureHuntData", tags=["TreasureHunt"])
async def LegendaryTreasureHuntData() -> list[TreasureHunt.LegendaryTreasureHuntData]:
    return data.LegendaryTreasureHuntData
@app.get("/PointOfInterestData", tags=["TreasureHunt"])
async def PointOfInterestData() -> list[TreasureHunt.PointOfInterestData]:
    return data.PointOfInterestData
@app.get("/AreaData", tags=["World"])
async def AreaData() -> list[World.AreaData]:
    return data.AreaData
@app.get("/DungeonData", tags=["World"])
async def DungeonData() -> list[World.DungeonData]:
    return data.DungeonData
@app.get("/HintCategoryData", tags=["World"])
async def HintCategoryData() -> list[World.HintCategoryData]:
    return data.HintCategoryData
@app.get("/HintData", tags=["World"])
async def HintData() -> list[World.HintData]:
    return data.HintData
@app.get("/MapInformationData", tags=["World"])
async def MapInformationData() -> list[World.MapInformationData]:
    return data.MapInformationData
@app.get("/MapReferenceData", tags=["World"])
async def MapReferenceData() -> list[World.MapReferenceData]:
    return data.MapReferenceData
@app.get("/MapScrollActionData", tags=["World"])
async def MapScrollActionData() -> list[World.MapScrollActionData]:
    return data.MapScrollActionData
@app.get("/MapsCoordinateData", tags=["World"])
async def MapsCoordinateData() -> list[World.MapsCoordinateData]:
    return data.MapsCoordinateData
@app.get("/SubAreaData", tags=["World"])
async def SubAreaData() -> list[World.SubAreaData]:
    return data.SubAreaData
@app.get("/SuperAreaData", tags=["World"])
async def SuperAreaData() -> list[World.SuperAreaData]:
    return data.SuperAreaData
@app.get("/WaypointData", tags=["World"])
async def WaypointData() -> list[World.WaypointData]:
    return data.WaypointData
@app.get("/WorldEventData", tags=["World"])
async def WorldEventData() -> list[World.WorldEventData]:
    return data.WorldEventData
@app.get("/WorldEventDungeonData", tags=["World"])
async def WorldEventDungeonData() -> list[World.WorldEventDungeonData]:
    return data.WorldEventDungeonData
@app.get("/WorldEventFarmingSimulatorData", tags=["World"])
async def WorldEventFarmingSimulatorData() -> list[World.WorldEventFarmingSimulatorData]:
    return data.WorldEventFarmingSimulatorData
@app.get("/WorldEventMonstersHunterData", tags=["World"])
async def WorldEventMonstersHunterData() -> list[World.WorldEventMonstersHunterData]:
    return data.WorldEventMonstersHunterData
@app.get("/WorldEventRewardData", tags=["World"])
async def WorldEventRewardData() -> list[World.WorldEventRewardData]:
    return data.WorldEventRewardData
@app.get("/WorldEventWorldBossesData", tags=["World"])
async def WorldEventWorldBossesData() -> list[World.WorldEventWorldBossesData]:
    return data.WorldEventWorldBossesData
@app.get("/WorldMapData", tags=["World"])
async def WorldMapData() -> list[World.WorldMapData]:
    return data.WorldMapData
# @formatter:on
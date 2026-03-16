from pydantic import BaseModel
from tqdm import tqdm

from pydofus3.tools import SingletonMeta
from pydofus3.extractor.data.loader import load_d2o
from pydofus3.generated.pydantic_d2o import Alignment, Alliance, Almanax, Alterations, Appearance, Arena, Bonus, Breach, Breed, Calendar, Challenge, Characteristic, Collection, Communication, Document, Effect, ExternalNotification, Feature, Guild, GuildMission, House, InfiniteDreams, Interactive, Item, Job, LivingObjects, Misc, Monster, Mount, Notification, Npc, OptionalFeatures, Popup, Progression, Quest, Ride, Scenarios, Seasons, Server, Social, Sound, Spell, TradeCenter, TreasureHunt, World

class Datacenter(metaclass=SingletonMeta):
    def __init__(self, empty: bool = False):
        self.empty = empty
        if not empty:
            self.progress = tqdm(total=198)
        
        self.AlignmentGiftData = self.load_d2o(Alignment.AlignmentGiftData)
        self.AlignmentOrderData = self.load_d2o(Alignment.AlignmentOrderData)
        self.AlignmentRankData = self.load_d2o(Alignment.AlignmentRankData)
        self.AlignmentRankGiftsData = self.load_d2o(Alignment.AlignmentRankGiftsData)
        self.AlignmentSideData = self.load_d2o(Alignment.AlignmentSideData)
        self.AlignmentTitleData = self.load_d2o(Alignment.AlignmentTitleData)
        
        self.AllianceRankData = self.load_d2o(Alliance.AllianceRankData)
        self.AllianceRankNameSuggestionData = self.load_d2o(Alliance.AllianceRankNameSuggestionData)
        self.AllianceRightData = self.load_d2o(Alliance.AllianceRightData)
        self.AllianceRightGroupData = self.load_d2o(Alliance.AllianceRightGroupData)
        self.AllianceTagData = self.load_d2o(Alliance.AllianceTagData)
        self.AllianceTagTypeData = self.load_d2o(Alliance.AllianceTagTypeData)
        self.KothRoleData = self.load_d2o(Alliance.KothRoleData)
        
        self.AlmanaxCalendarData = self.load_d2o(Almanax.AlmanaxCalendarData)
        self.AlmanaxCategoryData = self.load_d2o(Almanax.AlmanaxCategoryData)
        self.AlmanaxZodiacData = self.load_d2o(Almanax.AlmanaxZodiacData)
        
        self.AlterationCategoryData = self.load_d2o(Alterations.AlterationCategoryData)
        self.AlterationData = self.load_d2o(Alterations.AlterationData)
        
        self.AppearanceData = self.load_d2o(Appearance.AppearanceData)
        self.CreatureBoneOverrideData = self.load_d2o(Appearance.CreatureBoneOverrideData)
        self.CreatureBoneTypeData = self.load_d2o(Appearance.CreatureBoneTypeData)
        self.IdleData = self.load_d2o(Appearance.IdleData)
        self.OrnamentData = self.load_d2o(Appearance.OrnamentData)
        self.RiderBoneData = self.load_d2o(Appearance.RiderBoneData)
        self.SkinMappingData = self.load_d2o(Appearance.SkinMappingData)
        self.SkinPositionData = self.load_d2o(Appearance.SkinPositionData)
        self.SkinSlotRuleData = self.load_d2o(Appearance.SkinSlotRuleData)
        self.TitleCategoryData = self.load_d2o(Appearance.TitleCategoryData)
        self.TitleData = self.load_d2o(Appearance.TitleData)
        
        self.ArenaLeagueData = self.load_d2o(Arena.ArenaLeagueData)
        
        self.BonusCriterionData = self.load_d2o(Bonus.BonusCriterionData)
        self.BonusData = self.load_d2o(Bonus.BonusData)
        
        self.BreachBossData = self.load_d2o(Breach.BreachBossData)
        self.BreachDungeonModificatorData = self.load_d2o(Breach.BreachDungeonModificatorData)
        self.BreachPrizeData = self.load_d2o(Breach.BreachPrizeData)
        self.BreachWorldMapCoordinateData = self.load_d2o(Breach.BreachWorldMapCoordinateData)
        self.BreachWorldMapSectorData = self.load_d2o(Breach.BreachWorldMapSectorData)
        
        self.BodyData = self.load_d2o(Breed.BodyData)
        self.BreedData = self.load_d2o(Breed.BreedData)
        self.BreedRoleData = self.load_d2o(Breed.BreedRoleData)
        self.HeadData = self.load_d2o(Breed.HeadData)
        
        self.CalendarEventData = self.load_d2o(Calendar.CalendarEventData)
        
        self.ChallengeData = self.load_d2o(Challenge.ChallengeData)
        
        self.CharacteristicCategoryData = self.load_d2o(Characteristic.CharacteristicCategoryData)
        self.CharacteristicData = self.load_d2o(Characteristic.CharacteristicData)
        
        self.CollectableData = self.load_d2o(Collection.CollectableData)
        self.CollectionData = self.load_d2o(Collection.CollectionData)
        
        self.ChatChannelData = self.load_d2o(Communication.ChatChannelData)
        self.EmoticonData = self.load_d2o(Communication.EmoticonData)
        self.InfoMessageData = self.load_d2o(Communication.InfoMessageData)
        self.NamingRuleData = self.load_d2o(Communication.NamingRuleData)
        self.SmileyData = self.load_d2o(Communication.SmileyData)
        self.SmileyPackData = self.load_d2o(Communication.SmileyPackData)
        
        self.DocumentData = self.load_d2o(Document.DocumentData)
        
        self.ActionFilterData = self.load_d2o(Effect.ActionFilterData)
        self.EffectData = self.load_d2o(Effect.EffectData)
        self.EvolutiveEffectData = self.load_d2o(Effect.EvolutiveEffectData)
        
        self.ExternalNotificationData = self.load_d2o(ExternalNotification.ExternalNotificationData)
        
        self.OptionalFeatureData = self.load_d2o(Feature.OptionalFeatureData)
        
        self.EmblemBackgroundData = self.load_d2o(Guild.EmblemBackgroundData)
        self.EmblemSymbolCategoryData = self.load_d2o(Guild.EmblemSymbolCategoryData)
        self.EmblemSymbolData = self.load_d2o(Guild.EmblemSymbolData)
        self.GuildChestTabData = self.load_d2o(Guild.GuildChestTabData)
        self.GuildHallData = self.load_d2o(Guild.GuildHallData)
        self.GuildHallThemeData = self.load_d2o(Guild.GuildHallThemeData)
        self.GuildLevelRewardData = self.load_d2o(Guild.GuildLevelRewardData)
        self.GuildRankData = self.load_d2o(Guild.GuildRankData)
        self.GuildRankNameSuggestionData = self.load_d2o(Guild.GuildRankNameSuggestionData)
        self.GuildRightData = self.load_d2o(Guild.GuildRightData)
        self.GuildRightGroupData = self.load_d2o(Guild.GuildRightGroupData)
        self.GuildShopBoostData = self.load_d2o(Guild.GuildShopBoostData)
        self.GuildTagData = self.load_d2o(Guild.GuildTagData)
        self.GuildTagTypeData = self.load_d2o(Guild.GuildTagTypeData)
        
        self.GuildMissionActivityData = self.load_d2o(GuildMission.GuildMissionActivityData)
        self.GuildMissionData = self.load_d2o(GuildMission.GuildMissionData)
        self.GuildMissionGradeData = self.load_d2o(GuildMission.GuildMissionGradeData)
        self.GuildMissionMilestoneData = self.load_d2o(GuildMission.GuildMissionMilestoneData)
        self.GuildMissionMilestoneRewardData = self.load_d2o(GuildMission.GuildMissionMilestoneRewardData)
        self.GuildMissionObjectiveData = self.load_d2o(GuildMission.GuildMissionObjectiveData)
        self.GuildMissionRankData = self.load_d2o(GuildMission.GuildMissionRankData)
        self.GuildMissionSuperCategoryData = self.load_d2o(GuildMission.GuildMissionSuperCategoryData)
        
        self.HavenbagFurnitureData = self.load_d2o(House.HavenbagFurnitureData)
        self.HavenbagThemeData = self.load_d2o(House.HavenbagThemeData)
        self.HouseData = self.load_d2o(House.HouseData)
        
        self.InfiniteDreamIntensityData = self.load_d2o(InfiniteDreams.InfiniteDreamIntensityData)
        self.InfiniteDreamRewardActionData = self.load_d2o(InfiniteDreams.InfiniteDreamRewardActionData)
        self.InfiniteDreamRewardData = self.load_d2o(InfiniteDreams.InfiniteDreamRewardData)
        self.InfiniteDreamTrialData = self.load_d2o(InfiniteDreams.InfiniteDreamTrialData)
        
        self.InteractiveData = self.load_d2o(Interactive.InteractiveData)
        self.SignsData = self.load_d2o(Interactive.SignsData)
        self.SkillNameData = self.load_d2o(Interactive.SkillNameData)
        self.StealthBoneData = self.load_d2o(Interactive.StealthBoneData)
        
        self.EvolutiveItemTypeData = self.load_d2o(Item.EvolutiveItemTypeData)
        self.ItemData = self.load_d2o(Item.ItemData)
        self.ItemSetData = self.load_d2o(Item.ItemSetData)
        self.ItemSuperTypeData = self.load_d2o(Item.ItemSuperTypeData)
        self.ItemTypeData = self.load_d2o(Item.ItemTypeData)
        self.LegendaryPowerCategoryData = self.load_d2o(Item.LegendaryPowerCategoryData)
        self.PresetIconData = self.load_d2o(Item.PresetIconData)
        self.RandomDropGroupData = self.load_d2o(Item.RandomDropGroupData)
        self.VeteranRewardData = self.load_d2o(Item.VeteranRewardData)
        
        self.JobData = self.load_d2o(Job.JobData)
        self.RecipeData = self.load_d2o(Job.RecipeData)
        self.SkillData = self.load_d2o(Job.SkillData)
        
        self.LivingObjectSkinMoodsData = self.load_d2o(LivingObjects.LivingObjectSkinMoodsData)
        self.SpeakingItemTextData = self.load_d2o(LivingObjects.SpeakingItemTextData)
        self.SpeakingItemTriggerData = self.load_d2o(LivingObjects.SpeakingItemTriggerData)
        
        self.CharacterXpMappingData = self.load_d2o(Misc.CharacterXpMappingData)
        self.ChoiceData = self.load_d2o(Misc.ChoiceData)
        self.LuaFormulaData = self.load_d2o(Misc.LuaFormulaData)
        self.MonthData = self.load_d2o(Misc.MonthData)
        self.TextIconReferenceData = self.load_d2o(Misc.TextIconReferenceData)
        
        self.CompanionCharacteristicData = self.load_d2o(Monster.CompanionCharacteristicData)
        self.CompanionData = self.load_d2o(Monster.CompanionData)
        self.CompanionSpellData = self.load_d2o(Monster.CompanionSpellData)
        self.MonsterData = self.load_d2o(Monster.MonsterData)
        self.MonsterMiniBossData = self.load_d2o(Monster.MonsterMiniBossData)
        self.MonsterRaceData = self.load_d2o(Monster.MonsterRaceData)
        self.MonsterSoulData = self.load_d2o(Monster.MonsterSoulData)
        self.MonsterSuperRaceData = self.load_d2o(Monster.MonsterSuperRaceData)
        
        self.MountBehaviorData = self.load_d2o(Mount.MountBehaviorData)
        self.MountBoneData = self.load_d2o(Mount.MountBoneData)
        self.MountData = self.load_d2o(Mount.MountData)
        self.MountFamilyData = self.load_d2o(Mount.MountFamilyData)
        self.RideFoodData = self.load_d2o(Mount.RideFoodData)
        
        self.NotificationData = self.load_d2o(Notification.NotificationData)
        
        self.NpcActionData = self.load_d2o(Npc.NpcActionData)
        self.NpcData = self.load_d2o(Npc.NpcData)
        self.NpcDialogSkinData = self.load_d2o(Npc.NpcDialogSkinData)
        self.NpcMessageData = self.load_d2o(Npc.NpcMessageData)
        self.TaxCollectorFirstnameData = self.load_d2o(Npc.TaxCollectorFirstnameData)
        self.TaxCollectorNameData = self.load_d2o(Npc.TaxCollectorNameData)
        
        self.CustomModeBreedSpellData = self.load_d2o(OptionalFeatures.CustomModeBreedSpellData)
        self.ForgettableSpellData = self.load_d2o(OptionalFeatures.ForgettableSpellData)
        self.ModsterData = self.load_d2o(OptionalFeatures.ModsterData)
        self.ProgressingAchievementSeasonData = self.load_d2o(OptionalFeatures.ProgressingAchievementSeasonData)
        self.ProgressingAchievementStepData = self.load_d2o(OptionalFeatures.ProgressingAchievementStepData)
        
        self.PopupInformationData = self.load_d2o(Popup.PopupInformationData)
        
        self.ActivitySuggestionCategoryData = self.load_d2o(Progression.ActivitySuggestionCategoryData)
        self.ActivitySuggestionData = self.load_d2o(Progression.ActivitySuggestionData)
        self.FeatureDescriptionData = self.load_d2o(Progression.FeatureDescriptionData)
        
        self.AchievementCategoryData = self.load_d2o(Quest.AchievementCategoryData)
        self.AchievementData = self.load_d2o(Quest.AchievementData)
        self.AchievementObjectiveData = self.load_d2o(Quest.AchievementObjectiveData)
        self.AchievementRewardData = self.load_d2o(Quest.AchievementRewardData)
        self.QuestCategoryData = self.load_d2o(Quest.QuestCategoryData)
        self.QuestData = self.load_d2o(Quest.QuestData)
        self.QuestObjectiveData = self.load_d2o(Quest.QuestObjectiveData)
        self.QuestObjectiveTypeData = self.load_d2o(Quest.QuestObjectiveTypeData)
        self.QuestStepData = self.load_d2o(Quest.QuestStepData)
        self.QuestStepRewardData = self.load_d2o(Quest.QuestStepRewardData)
        
        self.PaddockGaugesData = self.load_d2o(Ride.PaddockGaugesData)
        self.PaddocksData = self.load_d2o(Ride.PaddocksData)
        self.RideGaugesData = self.load_d2o(Ride.RideGaugesData)
        self.RideSpeciesData = self.load_d2o(Ride.RideSpeciesData)
        self.RidesData = self.load_d2o(Ride.RidesData)
        
        self.FightScenarioData = self.load_d2o(Scenarios.FightScenarioData)
        
        self.ArenaLeagueSeasonData = self.load_d2o(Seasons.ArenaLeagueSeasonData)
        self.ExpeditionSeasonData = self.load_d2o(Seasons.ExpeditionSeasonData)
        self.ServerSeasonData = self.load_d2o(Seasons.ServerSeasonData)
        
        self.ServerCommunityData = self.load_d2o(Server.ServerCommunityData)
        self.ServerData = self.load_d2o(Server.ServerData)
        self.ServerGameTypeData = self.load_d2o(Server.ServerGameTypeData)
        self.ServerLangData = self.load_d2o(Server.ServerLangData)
        self.ServerPopulationData = self.load_d2o(Server.ServerPopulationData)
        
        self.SocialTagData = self.load_d2o(Social.SocialTagData)
        self.SocialTagTypeData = self.load_d2o(Social.SocialTagTypeData)
        
        self.SoundBoneData = self.load_d2o(Sound.SoundBoneData)
        
        self.SpellBombData = self.load_d2o(Spell.SpellBombData)
        self.SpellBombWallData = self.load_d2o(Spell.SpellBombWallData)
        self.SpellData = self.load_d2o(Spell.SpellData)
        self.SpellLevelData = self.load_d2o(Spell.SpellLevelData)
        self.SpellPairData = self.load_d2o(Spell.SpellPairData)
        self.SpellScriptData = self.load_d2o(Spell.SpellScriptData)
        self.SpellStateData = self.load_d2o(Spell.SpellStateData)
        self.SpellTypeData = self.load_d2o(Spell.SpellTypeData)
        self.SpellVariantData = self.load_d2o(Spell.SpellVariantData)
        
        self.AuctionHouseData = self.load_d2o(TradeCenter.AuctionHouseData)
        
        self.LegendaryTreasureHuntData = self.load_d2o(TreasureHunt.LegendaryTreasureHuntData)
        self.PointOfInterestData = self.load_d2o(TreasureHunt.PointOfInterestData)
        
        self.AreaData = self.load_d2o(World.AreaData)
        self.DungeonData = self.load_d2o(World.DungeonData)
        self.HintCategoryData = self.load_d2o(World.HintCategoryData)
        self.HintData = self.load_d2o(World.HintData)
        self.MapInformationData = self.load_d2o(World.MapInformationData)
        self.MapReferenceData = self.load_d2o(World.MapReferenceData)
        self.MapScrollActionData = self.load_d2o(World.MapScrollActionData)
        self.MapsCoordinateData = self.load_d2o(World.MapsCoordinateData)
        self.SubAreaData = self.load_d2o(World.SubAreaData)
        self.SuperAreaData = self.load_d2o(World.SuperAreaData)
        self.WaypointData = self.load_d2o(World.WaypointData)
        self.WorldEventData = self.load_d2o(World.WorldEventData)
        self.WorldEventDungeonData = self.load_d2o(World.WorldEventDungeonData)
        self.WorldEventFarmingSimulatorData = self.load_d2o(World.WorldEventFarmingSimulatorData)
        self.WorldEventMonstersHunterData = self.load_d2o(World.WorldEventMonstersHunterData)
        self.WorldEventRewardData = self.load_d2o(World.WorldEventRewardData)
        self.WorldEventWorldBossesData = self.load_d2o(World.WorldEventWorldBossesData)
        self.WorldMapData = self.load_d2o(World.WorldMapData)
        
        if not empty:
            self.progress.close()

    def load_d2o[T: BaseModel](self, d2o_class: type[T]) -> list[T]:
        if self.empty:
            return []
        self.progress.set_postfix(d2o=d2o_class.__name__)
        self.progress.update()
        try:
            return list(load_d2o(d2o_class).values())
        except Exception:
            tqdm.write(f"Error loading {d2o_class.__name__}")
            return []
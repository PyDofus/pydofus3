from __future__ import annotations
from typing import TypedDict, Any, Union

class PPtr(TypedDict):
    m_FileID: int
    m_PathID: int

class MonoBehaviour(TypedDict):
    m_Enabled: int
    m_GameObject: PPtr
    m_Name: str
    m_Script: PPtr

class AchievementCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, AchievementCategoryData]

class AchievementCategoryData(TypedDict):
    id: int
    nameId: int
    parentId: int
    icon: str
    order: int
    color: str
    achievementIds: list[int]
    visibilityCriterion: str

class AchievementData(TypedDict):
    id: int
    nameId: int
    categoryId: int
    descriptionId: int
    iconId: int
    points: int
    level: int
    order: int
    accountLinked: int
    objectiveIds: list[int]
    rewardIds: list[int]

class AchievementObjectiveData(TypedDict):
    id: int
    achievementId: int
    order: int
    nameId: int
    criterion: str

class AchievementObjectivesDataRoot(MonoBehaviour):
    objectsById: dict[str, AchievementObjectiveData]

class AchievementRewardData(TypedDict):
    id: int
    achievementId: int
    criterions: str
    kamasRatio: float
    experienceRatio: float
    kamasScaleWithPlayerLevel: int
    itemsReward: list[int]
    itemsQuantityReward: list[int]
    emotesReward: list[int]
    spellsReward: list[int]
    titlesReward: list[int]
    ornamentsReward: list[int]
    alterationsReward: list[int]
    guildPoints: int

class AchievementRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, AchievementRewardData]

class AchievementsDataRoot(MonoBehaviour):
    objectsById: dict[str, AchievementData]

class ActionFilterData(TypedDict):
    id: int
    nameId: int
    order: int

class ActionFiltersDataRoot(MonoBehaviour):
    objectsById: dict[str, ActionFilterData]

class ActivitySuggestionCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, ActivitySuggestionCategoryData]

class ActivitySuggestionCategoryData(TypedDict):
    id: int
    nameId: int
    parentId: int

class ActivitySuggestionData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    categoryId: int
    level: int
    mapId: int
    isLarge: int
    startDate: float
    endDate: float
    icon: str
    iconCategoryId: int

class ActivitySuggestionsDataRoot(MonoBehaviour):
    objectsById: dict[str, ActivitySuggestionData]

class AlignmentGiftData(TypedDict):
    id: int
    nameId: int

class AlignmentGiftsDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentGiftData]

class AlignmentOrderData(TypedDict):
    id: int
    nameId: int
    sideId: int

class AlignmentOrdersDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentOrderData]

class AlignmentRankData(TypedDict):
    id: int
    orderId: int
    nameId: int
    descriptionId: int
    minimumAlignment: int

class AlignmentRankGiftsData(TypedDict):
    id: int
    gifts: list[int]

class AlignmentRanksDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentRankData]

class AlignmentRanksGiftsDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentRankGiftsData]

class AlignmentSideData(TypedDict):
    id: int
    nameId: int

class AlignmentSidesDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentSideData]

class AlignmentTitleData(TypedDict):
    sideId: int
    namesId: list[str]
    shortsId: list[str]

class AlignmentTitlesDataRoot(MonoBehaviour):
    objectsById: dict[str, AlignmentTitleData]

class AllianceRankData(TypedDict):
    id: int
    nameId: int
    order: int
    isModifiable: int
    gfxId: int

class AllianceRankNameSuggestionData(TypedDict):
    uiKey: str

class AllianceRankNameSuggestionsDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceRankNameSuggestionData]

class AllianceRanksDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceRankData]

class AllianceRightData(TypedDict):
    id: int
    nameId: int
    order: int
    groupId: int

class AllianceRightGroupData(TypedDict):
    id: int
    nameId: int
    order: int
    rights: list[SocialRightData]

class AllianceRightGroupsDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceRightGroupData]

class AllianceRightsDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceRightData]

class AllianceTagData(TypedDict):
    id: int
    typeId: int
    nameId: int
    order: int

class AllianceTagTypeData(TypedDict):
    id: int
    nameId: int

class AllianceTagTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceTagTypeData]

class AllianceTagsDataRoot(MonoBehaviour):
    objectsById: dict[str, AllianceTagData]

class AlmanaxCalendarData(TypedDict):
    id: int
    nameId: int
    descId: int
    npcId: int
    categoryId: int
    bonusesIds: list[int]
    dates: list[str]
    objectiveId: int
    meridiaDescriptionId: int
    meridiaEffectId: int
    rubrikabraxId: int
    meridiaIllustrationId: int
    celebrationNameId: int
    celebrationDescriptionId: int

class AlmanaxCalendarsDataRoot(MonoBehaviour):
    objectsById: dict[str, AlmanaxCalendarData]

class AlmanaxCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, AlmanaxCategoryData]

class AlmanaxCategoryData(TypedDict):
    id: int
    nameId: int
    protectorNameId: int
    protectorDescriptionId: int
    protectorIllustrationId: int

class AlmanaxZodiacData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    dateStart: str
    dateEnd: str
    picture: str

class AlmanaxZodiacsDataRoot(MonoBehaviour):
    objectsById: dict[str, AlmanaxZodiacData]

class AlterationCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, AlterationCategoryData]

class AlterationCategoryData(TypedDict):
    id: int
    nameId: int
    parentId: int

class AlterationData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    categoryId: int
    iconId: int
    isVisible: int
    criterions: str
    isWebDisplay: int
    possibleEffects: list[EffectInstanceData]

class AlterationsDataRoot(MonoBehaviour):
    objectsById: dict[str, AlterationData]

class AnimFunMonsterData(TypedDict):
    animId: int
    entityId: int
    animName: str
    animWeight: int

class AnimFunNpcData(TypedDict):
    animId: int
    entityId: int
    animName: str
    animWeight: int
    subAnimFunData: list[NestedAnimFunNpcData]

class AppearanceData(TypedDict):
    id: int
    type: int
    data: str
    usePlayerLook: int

class AppearancesDataRoot(MonoBehaviour):
    objectsById: dict[str, AppearanceData]

class AreaData(TypedDict):
    id: int
    nameId: int
    superAreaId: int
    containHouses: int
    containPaddocks: int
    bounds: Rectangle
    worldmapId: int
    subareaIds: list[int]
    hasWorldMap: int
    hasSuggestion: int

class AreasDataRoot(MonoBehaviour):
    objectsById: dict[str, AreaData]

class ArenaLeagueData(TypedDict):
    id: int
    nameId: int
    ornamentId: int
    icon: str
    illus: str
    isLastLeague: int
    lowRatingBound: int
    highRatingBound: int

class ArenaLeagueSeasonData(TypedDict):
    uid: int
    nameId: str
    beginning: float
    closure: float
    resetDate: float
    flagObjectId: int

class ArenaLeagueSeasonsDataRoot(MonoBehaviour):
    objectsById: dict[str, ArenaLeagueSeasonData]

class ArenaLeaguesDataRoot(MonoBehaviour):
    objectsById: dict[str, ArenaLeagueData]

class AuctionHouseData(TypedDict):
    id: int
    typeId: int

class AuctionHousesDataRoot(MonoBehaviour):
    objectsById: dict[str, AuctionHouseData]

class BodiesDataRoot(MonoBehaviour):
    objectsById: dict[str, BodyData]

class BodyData(TypedDict):
    id: int
    skins: str
    assetId: str
    breed: int
    gender: int
    label: str
    order: int
    payable: int
    availableAtCreation: int
    nameId: int

class BonusCriterionData(TypedDict):
    id: int
    type: int
    value: int

class BonusData(TypedDict):
    id: int
    type: int
    amount: int
    criterionsIds: list[int]

class BonusesCriterionsDataRoot(MonoBehaviour):
    objectsById: dict[str, BonusCriterionData]

class BonusesDataRoot(MonoBehaviour):
    objectsById: dict[str, BonusData]

class BoundScriptUsageData(TypedDict):
    id: int
    order: int
    scriptId: int
    spellLevels: list[int]
    criterion: str
    casterMask: str
    targetMask: str
    targetZone: str
    activationMask: str
    activationZone: str
    random: int
    randomGroup: int
    sequenceGroup: int
    isTargetTreatedAsCaster: int
    areTargetsAffectedConcurrently: int

class BreachBossData(TypedDict):
    id: int
    monsterId: int
    category: int
    apparitionCriterion: str
    accessCriterion: str
    incompatibleBosses: list[int]
    rewardId: int

class BreachBossesDataRoot(MonoBehaviour):
    objectsById: dict[str, BreachBossData]

class BreachDungeonModificatorData(TypedDict):
    id: int
    modificatorId: int
    criterion: str
    additionalRewardPercent: float
    score: float
    isPositiveForPlayers: int
    tooltipBaseline: str

class BreachDungeonModificatorsDataRoot(MonoBehaviour):
    objectsById: dict[str, BreachDungeonModificatorData]

class BreachPrizeData(TypedDict):
    id: int
    nameId: int
    categoryId: int
    tooltipKey: str
    descriptionKey: str

class BreachPrizesDataRoot(MonoBehaviour):
    objectsById: dict[str, BreachPrizeData]

class BreachWorldMapCoordinateData(TypedDict):
    mapStage: int
    mapCoordinateX: int
    mapCoordinateY: int
    unexploredMapIcon: int
    exploredMapIcon: int

class BreachWorldMapCoordinatesDataRoot(MonoBehaviour):
    objectsById: dict[str, BreachWorldMapCoordinateData]

class BreachWorldMapSectorData(TypedDict):
    id: int
    sectorNameId: str
    legendId: str
    sectorIcon: str
    minStage: int
    maxStage: int

class BreachWorldMapSectorsDataRoot(MonoBehaviour):
    objectsById: dict[str, BreachWorldMapSectorData]

class BreedData(TypedDict):
    id: int
    shortNameId: str
    descriptionId: int
    gameplayDescriptionId: str
    maleLook: str
    femaleLook: str
    creatureBonesId: int
    statsPointsForStrength: list[WrappedUintList]
    statsPointsForIntelligence: list[WrappedUintList]
    statsPointsForChance: list[WrappedUintList]
    statsPointsForAgility: list[WrappedUintList]
    statsPointsForVitality: list[WrappedUintList]
    statsPointsForWisdom: list[WrappedUintList]
    breedSpellsId: list[int]
    breedRoles: list[BreedRoleByBreedData]
    maleColors: list[int]
    femaleColors: list[int]
    complexity: int
    sortIndex: int

class BreedRoleByBreedData(TypedDict):
    roleId: int
    descriptionId: int
    value: int
    order: int

class BreedRoleData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    assetId: int
    color: int

class BreedRolesDataRoot(MonoBehaviour):
    objectsById: dict[str, BreedRoleData]

class BreedingRelationData(TypedDict):
    parent: int
    child: int

class BreedsDataRoot(MonoBehaviour):
    objectsById: dict[str, BreedData]

class CalendarEventData(TypedDict):
    id: int
    categoryId: int
    nameId: int
    descriptionId: int
    criterion: str
    recommendedLevel: int
    rewards: str
    map: int
    picture: str

class CalendarEventsDataRoot(MonoBehaviour):
    objectsById: dict[str, CalendarEventData]

class ChallengeData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    incompatibleChallenges: list[int]
    categoryId: int
    iconId: int
    completionCriterion: str
    activationCriterion: str
    targetMonsterId: int

class ChallengesDataRoot(MonoBehaviour):
    objectsById: dict[str, ChallengeData]

class CharacterXPMappingsDataRoot(MonoBehaviour):
    objectsById: dict[str, CharacterXpMappingData]

class CharacterXpMappingData(TypedDict):
    experiencePoints: float

class CharacteristicCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, CharacteristicCategoryData]

class CharacteristicCategoryData(TypedDict):
    id: int
    nameId: int
    order: int
    characteristicIds: list[int]

class CharacteristicData(TypedDict):
    id: int
    keyword: str
    nameId: int
    asset: str
    categoryId: int
    visible: int
    order: int
    scaleFormulaId: int
    upgradable: int

class CharacteristicsDataRoot(MonoBehaviour):
    objectsById: dict[str, CharacteristicData]

class ChatChannelData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    shortcut: str
    isPrivate: int

class ChatChannelsDataRoot(MonoBehaviour):
    objectsById: dict[str, ChatChannelData]

class ChoiceData(TypedDict):
    id: int
    choiceNameId: int
    duration: int
    options: list[ChoiceOptionData]

class ChoiceOptionData(TypedDict):
    id: int
    descriptionId: int
    rewardType: int
    rewardValue: str
    gfxId: int

class ChoicesDataRoot(MonoBehaviour):
    objectsById: dict[str, ChoiceData]

class CollectableData(TypedDict):
    entityId: int
    name: str
    typeId: int
    gfxId: int
    order: int
    rarity: int

class CollectablesDataRoot(MonoBehaviour):
    objectsById: dict[str, CollectableData]

class CollectionData(TypedDict):
    typeId: int
    name: str
    criterion: str
    collectables: list[CollectableData]

class CollectionsDataRoot(MonoBehaviour):
    objectsById: dict[str, CollectionData]

class CompanionCharacteristicData(TypedDict):
    id: int
    caracId: int
    companionId: int
    order: int
    statPerLevelRange: list[WrappedFloatList]

class CompanionCharacteristicsDataRoot(MonoBehaviour):
    objectsById: dict[str, CompanionCharacteristicData]

class CompanionData(TypedDict):
    id: int
    nameId: int
    look: str
    webDisplay: int
    descriptionId: int
    startingSpellLevelId: int
    assetId: int
    characteristics: list[int]
    spells: list[int]
    creatureBoneId: int
    visibility: str

class CompanionSpellData(TypedDict):
    id: int
    spellId: int
    companionId: int
    gradeByLevel: str

class CompanionSpellsDataRoot(MonoBehaviour):
    objectsById: dict[str, CompanionSpellData]

class CompanionsDataRoot(MonoBehaviour):
    objectsById: dict[str, CompanionData]

class CreatureBoneOverrideData(TypedDict):
    boneId: int
    creatureBoneId: int

class CreatureBoneTypeData(TypedDict):
    id: int
    creatureBoneId: int

class CreatureBonesOverridesDataRoot(MonoBehaviour):
    objectsById: dict[str, CreatureBoneOverrideData]

class CreatureBonesTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, CreatureBoneTypeData]

class CustomModeBreedSpellData(TypedDict):
    id: int
    pairId: int
    breedId: int
    isInitialSpell: int
    isHidden: int

class CustomModeBreedSpellsDataRoot(MonoBehaviour):
    objectsById: dict[str, CustomModeBreedSpellData]

class DocumentData(TypedDict):
    id: int
    typeId: int
    showTitle: int
    showBackgroundImage: int
    titleId: str
    authorId: str
    subTitleId: str
    contentId: str
    contentCSS: str
    clientProperties: str

class DocumentsDataRoot(MonoBehaviour):
    objectsById: dict[str, DocumentData]

class DungeonData(TypedDict):
    id: int
    nameId: int
    optimalPlayerLevel: int
    mapIds: list[int]
    entranceMapId: int
    exitMapId: int

class DungeonsDataRoot(MonoBehaviour):
    objectsById: dict[str, DungeonData]

class EffectData(TypedDict):
    id: int
    descriptionId: int
    iconId: int
    characteristic: int
    category: int
    characteristicOperator: str
    showInTooltip: int
    useDice: int
    forceMinMax: int
    boost: int
    active: int
    oppositeId: int
    theoreticalDescriptionId: str
    theoreticalPattern: int
    showInSet: int
    bonusType: int
    useInFight: int
    effectPriority: int
    effectPowerRate: float
    elementId: int
    isInPercent: int
    hideValueInTooltip: int
    textIconReferenceId: int
    effectTriggerDuration: int
    actionFiltersId: list[int]

class EffectInstanceData(TypedDict):
    m_flags: int
    effectUid: int
    baseEffectId: int
    effectId: int
    order: int
    targetId: int
    targetMask: str
    duration: int
    random: float
    group: int
    modificator: int
    dispellable: int
    delay: int
    triggers: str
    effectElement: int
    spellId: int
    effectTriggerDuration: int
    zoneDescr: SpellZoneDescr

class EffectInstanceDice(TypedDict):
    m_flags: int
    effectUid: int
    baseEffectId: int
    effectId: int
    order: int
    targetId: int
    targetMask: str
    duration: int
    random: float
    group: int
    modificator: int
    dispellable: int
    delay: int
    triggers: str
    effectElement: int
    spellId: int
    effectTriggerDuration: int
    zoneDescr: SpellZoneDescr
    value: int
    diceNum: int
    diceSide: int
    displayZero: int

class EffectsDataRoot(MonoBehaviour):
    objectsById: dict[str, EffectData]

class EmblemBackgroundData(TypedDict):
    id: int
    order: int

class EmblemBackgroundsDataRoot(MonoBehaviour):
    objectsById: dict[str, EmblemBackgroundData]

class EmblemSymbolCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, EmblemSymbolCategoryData]

class EmblemSymbolCategoryData(TypedDict):
    id: int
    nameId: int

class EmblemSymbolData(TypedDict):
    id: int
    skinId: int
    iconId: int
    order: int
    categoryId: int
    colorizable: int

class EmblemSymbolsDataRoot(MonoBehaviour):
    objectsById: dict[str, EmblemSymbolData]

class EmoticonData(TypedDict):
    id: int
    nameId: int
    shortcutId: str
    order: int
    animName: str
    persistancy: int
    persistantAnimName: str
    eightDirections: int
    aura: int
    cooldown: int
    duration: int
    weight: int
    spellLevelId: int
    scale: int
    allowOnMount: int
    criterion: str

class EmoticonsDataRoot(MonoBehaviour):
    objectsById: dict[str, EmoticonData]

class EvolutiveEffectData(TypedDict):
    id: int
    actionId: int
    targetId: int
    progressionPerLevelRange: list[WrappedFloatList]

class EvolutiveEffectsDataRoot(MonoBehaviour):
    objectsById: dict[str, EvolutiveEffectData]

class EvolutiveItemTypeData(TypedDict):
    id: int
    maxLevel: int
    experienceBoost: float
    experienceByLevel: list[int]

class EvolutiveItemTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, EvolutiveItemTypeData]

class ExpeditionSeasonData(TypedDict):
    uid: int
    nameId: str
    beginning: float
    closure: float
    resetDate: float
    flagObjectId: int

class ExpeditionSeasonsDataRoot(MonoBehaviour):
    objectsById: dict[str, ExpeditionSeasonData]

class ExternalNotificationData(TypedDict):
    id: int
    categoryId: int
    iconId: int
    colorId: int
    descriptionId: int
    defaultEnable: int
    defaultSound: int
    defaultMultiAccount: int
    defaultNotify: int
    name: str
    messageId: str

class ExternalNotificationsDataRoot(MonoBehaviour):
    objectsById: dict[str, ExternalNotificationData]

class FeatureDescriptionData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    priority: int
    parentId: int
    children: list[int]
    criterion: str
    images: list[FeatureImage]

class FeatureDescriptionsDataRoot(MonoBehaviour):
    objectsById: dict[str, FeatureDescriptionData]

class FeatureImage(TypedDict):
    id: int
    order: int
    category: int
    imageId: str
    verticalAlign: int
    horizontalAlign: int

class FightScenarioData(TypedDict):
    id: int
    nameId: str

class FightScenariosDataRoot(MonoBehaviour):
    objectsById: dict[str, FightScenarioData]

class ForgettableSpellData(TypedDict):
    id: int
    pairId: int
    itemId: int

class ForgettableSpellsDataRoot(MonoBehaviour):
    objectsById: dict[str, ForgettableSpellData]

class GuildChestTabData(TypedDict):
    tabId: int
    nameId: int
    index: int
    gfxId: int
    serverType: int
    cost: int
    seniority: int
    openRight: int
    dropRight: int
    takeRight: int

class GuildChestTabsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildChestTabData]

class GuildHallData(TypedDict):
    id: int
    nameId: int
    subareaId: int
    mapId: int

class GuildHallThemeData(TypedDict):
    id: int
    nameId: int
    order: int

class GuildHallThemesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildHallThemeData]

class GuildHallsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildHallData]

class GuildLevelRewardData(TypedDict):
    level: int
    nameId: int
    descriptionId: int
    picto: str

class GuildLevelRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildLevelRewardData]

class GuildMissionActivitiesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionActivityData]

class GuildMissionActivityData(TypedDict):
    id: int
    nameId: int
    level: int
    recommendedPlayers: int
    rerollCost: int
    milestonesIds: list[int]

class GuildMissionData(TypedDict):
    id: int
    categoryId: int
    superCategoryId: int
    nameId: int
    recommendedLevel: int
    gradeId: int
    activityPoint: int
    token: int
    objectives: list[int]

class GuildMissionGradeData(TypedDict):
    id: int
    name: str
    rankId: int
    activityPoint: int
    token: int

class GuildMissionGradesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionGradeData]

class GuildMissionMilestoneData(TypedDict):
    id: int
    activityId: int
    nameId: int
    milestoneLevel: int
    activityPoint: int
    xp: int
    acknowledgmentPoint: int

class GuildMissionMilestoneRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, Any]

class GuildMissionMilestonesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionMilestoneData]

class GuildMissionObjectiveData(TypedDict):
    id: int
    superCategoryId: int
    missionId: int
    order: int
    activationCriterion: str
    alterationId: int
    areaId: int
    subareaId: int
    mapId: int
    descriptionId: int
    monsterId: int
    inDungeon: int
    quantity: int
    familyId: int
    familyMonsters: list[int]
    minLevel: int
    intensity: int
    stage: int
    objectId: int

class GuildMissionObjectivesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionObjectiveData]

class GuildMissionRankData(TypedDict):
    id: int
    nameId: int
    grades: list[int]

class GuildMissionRanksDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionRankData]

class GuildMissionSuperCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionSuperCategoryData]

class GuildMissionSuperCategoryData(TypedDict):
    id: int
    nameId: int

class GuildMissionsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildMissionData]

class GuildRankData(TypedDict):
    id: int
    nameId: int
    order: int
    gfxId: int

class GuildRankNameSuggestionData(TypedDict):
    uiKey: str

class GuildRankNameSuggestionsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildRankNameSuggestionData]

class GuildRanksDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildRankData]

class GuildRightData(TypedDict):
    id: int
    nameId: int
    order: int
    groupId: int

class GuildRightGroupData(TypedDict):
    id: int
    nameId: int
    order: int
    rights: list[SocialRightData]

class GuildRightGroupsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildRightGroupData]

class GuildRightsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildRightData]

class GuildShopBoostData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    alterationId: int

class GuildShopBoostsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildShopBoostData]

class GuildTagData(TypedDict):
    id: int
    typeId: int
    nameId: int
    order: int

class GuildTagTypeData(TypedDict):
    id: int
    nameId: int

class GuildTagTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildTagTypeData]

class GuildTagsDataRoot(MonoBehaviour):
    objectsById: dict[str, GuildTagData]

class HavenbagFurnitureData(TypedDict):
    typeId: int
    themeId: int
    elementId: int
    color: int
    skillId: int
    layerId: int
    blocksMovement: int
    isStackable: int
    cellsWidth: int
    cellsHeight: int
    order: int
    gfxId: int
    height: int
    horizontalSymmetry: int
    origin: int2_storage
    size: int2_storage

class HavenbagFurnituresDataRoot(MonoBehaviour):
    objectsById: dict[str, HavenbagFurnitureData]

class HavenbagThemeData(TypedDict):
    id: int
    nameId: int
    mapId: int

class HavenbagThemesDataRoot(MonoBehaviour):
    objectsById: dict[str, HavenbagThemeData]

class HeadData(TypedDict):
    id: int
    skins: str
    assetId: str
    breed: int
    gender: int
    label: str
    order: int
    payable: int
    availableAtCreation: int
    nameId: int

class HeadsDataRoot(MonoBehaviour):
    objectsById: dict[str, HeadData]

class HintCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, HintCategoryData]

class HintCategoryData(TypedDict):
    id: int
    nameId: int

class HintData(TypedDict):
    id: int
    categoryId: int
    gfx: int
    nameId: int
    mapId: int
    realMapId: int
    x: int
    y: int
    outdoor: int
    subareaId: int
    worldMapId: int
    level: int

class HintsDataRoot(MonoBehaviour):
    objectsById: dict[str, HintData]

class HouseData(TypedDict):
    typeId: int
    defaultPrice: int
    nameId: int
    descriptionId: int
    gfxId: int
    roomCount: int

class HousesDataRoot(MonoBehaviour):
    objectsById: dict[str, HouseData]

class IdleData(TypedDict):
    nameId: int
    animationKey: str
    known: int
    iconIdMale: str
    iconIdFemale: str
    order: int
    criterion: str
    breed: int

class IdlesDataRoot(MonoBehaviour):
    objectsById: dict[str, IdleData]

class InfiniteDreamIntensitiesDataRoot(MonoBehaviour):
    objectsById: dict[str, InfiniteDreamIntensityData]

class InfiniteDreamIntensityData(TypedDict):
    id: int
    intensity: int
    droplegend: int
    dropBonus: float
    xpBonus: float
    money: int
    additionalLife: int
    nameId: int
    dreamFragments: int

class InfiniteDreamRewardActionData(TypedDict):
    id: int
    effect: EffectInstanceData
    duration: int
    isAlly: int

class InfiniteDreamRewardActionsDataRoot(MonoBehaviour):
    objectsById: dict[str, InfiniteDreamRewardActionData]

class InfiniteDreamRewardData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    actions: list[int]

class InfiniteDreamRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, InfiniteDreamRewardData]

class InfiniteDreamTrialData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    seed: str
    achievementId: int
    achievementIntensity: int
    picture: str

class InfiniteDreamTrialsDataRoot(MonoBehaviour):
    objectsById: dict[str, InfiniteDreamTrialData]

class InfoMessageData(TypedDict):
    typeId: int
    messageId: int
    textId: int

class InfoMessagesDataRoot(MonoBehaviour):
    objectsById: dict[str, InfoMessageData]

class InteractiveData(TypedDict):
    id: int
    nameId: int

class InteractivesDataRoot(MonoBehaviour):
    objectsById: dict[str, InteractiveData]

class ItemData(TypedDict):
    m_flags: int
    id: int
    nameId: int
    typeId: int
    descriptionId: int
    iconId: int
    level: int
    realWeight: int
    price: float
    itemSetId: int
    criterions: str
    criterionsTarget: str
    appearanceId: int
    isColorable: int
    recipeSlots: int
    recipeIds: list[int]
    dropMonsterIds: list[int]
    dropTemporisMonsterIds: list[int]
    possibleEffects: list[EffectInstanceData]
    evolutiveEffectIds: list[int]
    favoriteSubAreas: list[int]
    favoriteSubAreasBonus: int
    craftXpRatio: int
    craftVisibleCriterion: str
    craftConditionalCriterion: str
    craftFeasibleCriterion: str
    visibilityCriterion: str
    recyclingNuggets: float
    favoriteRecyclingSubareas: list[int]
    resourcesBySubarea: list[WrappedIntList]
    importantNoticeId: str

class ItemSetData(TypedDict):
    id: int
    items: list[int]
    nameId: int
    bonusIsSecret: int
    isCosmetic: int
    effects: list[WrappedEffectInstanceList]

class ItemSetsDataRoot(MonoBehaviour):
    objectsById: dict[str, ItemSetData]

class ItemSuperTypeData(TypedDict):
    id: int
    possiblePositions: list[int]

class ItemSuperTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, ItemSuperTypeData]

class ItemTypeData(TypedDict):
    id: int
    nameId: int
    superTypeId: int
    categoryId: int
    isInEncyclopedia: int
    rawZone: str
    craftXpRatio: int
    evolutiveTypeId: int

class ItemTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, ItemTypeData]

class ItemsDataRoot(MonoBehaviour):
    objectsById: dict[str, ItemData]

class JobData(TypedDict):
    id: int
    nameId: int
    iconId: int
    hasLegendaryCraft: int

class JobsDataRoot(MonoBehaviour):
    objectsById: dict[str, JobData]

class KothRoleData(TypedDict):
    id: int
    nameId: int
    isDefault: int

class KothRolesDataRoot(MonoBehaviour):
    objectsById: dict[str, KothRoleData]

class LegendaryPowerCategoryData(TypedDict):
    id: int
    categoryName: str
    categoryOverridable: int
    categorySpells: list[int]

class LegendaryPowersCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, LegendaryPowerCategoryData]

class LegendaryTreasureHuntData(TypedDict):
    id: int
    nameId: int
    level: int
    chestId: int
    monsterId: int
    mapItemId: int
    xpRatio: float

class LegendaryTreasureHuntsDataRoot(MonoBehaviour):
    objectsById: dict[str, LegendaryTreasureHuntData]

class LivingObjectSkinMoodsData(TypedDict):
    skinId: int
    moods: list[WrappedIntList]

class LivingObjectSkinsMoodsDataRoot(MonoBehaviour):
    objectsById: dict[str, LivingObjectSkinMoodsData]

class LuaFormulaData(TypedDict):
    formula: str

class LuaFormulasDataRoot(MonoBehaviour):
    objectsById: dict[str, LuaFormulaData]

class ManagedReferencesRegistry(TypedDict):
    version: int
    RefIds: list[ReferencedObject]

class MapInformationData(TypedDict):
    m_flags: int
    id: int
    posX: int
    posY: int
    nameId: int
    subAreaId: int
    worldMap: int
    tacticalModeTemplateId: int

class MapReferenceData(TypedDict):
    id: int
    mapId: int
    cellId: int

class MapReferencesDataRoot(MonoBehaviour):
    objectsById: dict[str, MapReferenceData]

class MapScrollActionData(TypedDict):
    id: int
    rightExists: int
    bottomExists: int
    leftExists: int
    topExists: int
    rightMapId: int
    bottomMapId: int
    leftMapId: int
    topMapId: int

class MapScrollActionsDataRoot(MonoBehaviour):
    objectsById: dict[str, MapScrollActionData]

class MapsCoordinateData(TypedDict):
    compressedCoords: int
    mapIds: list[int]

class MapsCoordinatesDataRoot(MonoBehaviour):
    objectsById: dict[str, MapsCoordinateData]

class MapsInformationDataRoot(MonoBehaviour):
    objectsById: dict[str, MapInformationData]

type MetadataDictionaryContainer = dict[int, managedRefArrayItem]

class ModsterData(TypedDict):
    id: int
    itemId: int
    modsterId: int
    order: int
    parentsModsterId: list[int]
    modsterActiveSpells: list[int]
    modsterPassiveSpells: list[int]
    modsterHiddenAchievements: list[int]
    modsterAchievements: list[int]

class ModstersDataRoot(MonoBehaviour):
    objectsById: dict[str, ModsterData]

class MonsterBonusCharacteristicsData(TypedDict):
    lifePoints: int
    strength: int
    wisdom: int
    chance: int
    agility: int
    intelligence: int
    earthResistance: int
    fireResistance: int
    waterResistance: int
    airResistance: int
    neutralResistance: int
    tackleEvade: int
    tackleBlock: int
    bonusEarthDamage: int
    bonusFireDamage: int
    bonusWaterDamage: int
    bonusAirDamage: int
    aPRemoval: int

class MonsterData(TypedDict):
    m_flags: int
    id: int
    nameId: int
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
    characRatios: list[WrappedFloatList]
    isBounty: int
    souls: list[MonsterSoulData]

class MonsterDropCoefficientData(TypedDict):
    monsterId: int
    monsterGrade: int
    dropCoefficient: float
    criterions: str

class MonsterDropData(TypedDict):
    dropId: int
    monsterId: int
    objectId: int
    percentDropForGrade1: float
    percentDropForGrade2: float
    percentDropForGrade3: float
    percentDropForGrade4: float
    percentDropForGrade5: float
    count: int
    criterions: str
    hasCriterions: int
    hiddenIfInvalidCriterions: int
    specificDropCoefficient: list[MonsterDropCoefficientData]
    disableDropModificator: int

class MonsterGlobalDropData(TypedDict):
    objectId: int
    alterationId: int
    receiverCriterion: str
    disableDropModificator: int
    minPercentDrop: float
    maxPercentDrop: float

class MonsterGradeData(TypedDict):
    bonusCharacteristics: MonsterBonusCharacteristicsData
    grade: int
    monsterId: int
    level: int
    lifePoints: int
    actionPoints: int
    movementPoints: int
    vitality: int
    paDodge: int
    pmDodge: int
    wisdom: int
    earthResistance: int
    airResistance: int
    fireResistance: int
    waterResistance: int
    neutralResistance: int
    gradeXp: int
    damageReflect: int
    strength: int
    intelligence: int
    chance: int
    agility: int
    startingSpellId: int
    bonusRange: int

class MonsterMiniBossData(TypedDict):
    id: int
    monsterReplacingId: int

class MonsterMiniBossesDataRoot(MonoBehaviour):
    objectsById: dict[str, MonsterMiniBossData]

class MonsterRaceData(TypedDict):
    id: int
    superRaceId: int
    nameId: int
    aggressiveZoneSize: int
    aggressiveLevelDiff: int
    aggressiveImmunityCriterion: str
    aggressiveAttackDelay: int
    monsters: list[int]

class MonsterRacesDataRoot(MonoBehaviour):
    objectsById: dict[str, MonsterRaceData]

class MonsterSoulData(TypedDict):
    objectId: int
    criterion: str
    hasCriterion: int

class MonsterSuperRaceData(TypedDict):
    id: int
    nameId: int

class MonsterSuperRacesDataRoot(MonoBehaviour):
    objectsById: dict[str, MonsterSuperRaceData]

class MonstersDataRoot(MonoBehaviour):
    objectsById: dict[str, MonsterData]

class MonthData(TypedDict):
    nameId: int

class MonthsDataRoot(MonoBehaviour):
    objectsById: dict[str, MonthData]

class MountBehaviorData(TypedDict):
    id: int
    nameId: int
    descriptionId: int

class MountBehaviorsDataRoot(MonoBehaviour):
    objectsById: dict[str, MountBehaviorData]

class MountBoneData(TypedDict):
    id: int

class MountBonesDataRoot(MonoBehaviour):
    objectsById: dict[str, MountBoneData]

class MountData(TypedDict):
    id: int
    familyId: int
    nameId: int
    look: str
    certificateId: int
    effects: list[EffectInstanceData]

class MountFamiliesDataRoot(MonoBehaviour):
    objectsById: dict[str, MountFamilyData]

class MountFamilyData(TypedDict):
    id: int
    nameId: int
    headUri: str

class MountsDataRoot(MonoBehaviour):
    objectsById: dict[str, MountData]

class NamingRuleData(TypedDict):
    id: int
    minLength: int
    maxLength: int
    regexp: str

class NamingRulesDataRoot(MonoBehaviour):
    objectsById: dict[str, NamingRuleData]

class NestedAnimFunNpcData(TypedDict):
    animId: int
    entityId: int
    animName: str
    animWeight: int

class NotificationData(TypedDict):
    id: int
    titleId: str
    messageId: str
    iconId: int
    typeId: int
    trigger: str
    cantBeClosed: int

class NotificationsDataRoot(MonoBehaviour):
    objectsById: dict[str, NotificationData]

class NpcActionData(TypedDict):
    id: int
    realId: int
    nameId: int

class NpcActionsDataRoot(MonoBehaviour):
    objectsById: dict[str, NpcActionData]

class NpcData(TypedDict):
    id: int
    nameId: int
    dialogMessages: list[WrappedIntList]
    dialogReplies: list[WrappedIntList]
    actions: list[int]
    gender: int
    look: str
    animFunList: list[AnimFunNpcData]
    fastAnimsFun: int
    tooltipVisible: int
    dialogData: list[NpcDialogData]
    defaultSkinId: int

class NpcDialogData(TypedDict):
    id: int
    messageId: int
    moodId: int
    bubblePosition: int

class NpcDialogSkinData(TypedDict):
    id: int
    gfxId: int
    buttonsColorTypes: int
    backgroundColor: str
    isBold: int
    fontColor: str
    borderColor: str
    hasHalo: int
    headerGfxId: int
    headerColor: str
    headerFontColor: str
    headerDecorationGfxId: int
    headerDecorationColor: str
    headerOrnamentGfxId: int
    headerOrnamentColor: str

class NpcDialogSkinsDataRoot(MonoBehaviour):
    objectsById: dict[str, NpcDialogSkinData]

class NpcMessageData(TypedDict):
    id: int
    messageId: str
    messageParams: list[str]
    messageSkinId: int
    messageBubblePosition: int
    messageNpcMoodId: int

class NpcMessagesDataRoot(MonoBehaviour):
    objectsById: dict[str, NpcMessageData]

class NpcsDataRoot(MonoBehaviour):
    objectsById: dict[str, NpcData]

class OptionalFeatureData(TypedDict):
    id: int
    keyword: str
    isClient: int
    isServer: int
    isActivationOnLaunch: int
    isActivationOnServerConnection: int
    activationCriterions: str

class OptionalFeaturesDataRoot(MonoBehaviour):
    objectsById: dict[str, OptionalFeatureData]

class OrnamentData(TypedDict):
    id: int
    nameId: int
    visible: int
    assetId: int
    iconId: int
    order: int

class OrnamentsRootData(MonoBehaviour):
    objectsById: dict[str, OrnamentData]

class PaddockGaugesData(TypedDict):
    id: int
    name: str
    tierMaxValues: list[PaddockTierData]

class PaddockGaugesDataRoot(MonoBehaviour):
    objectsById: dict[str, PaddockGaugesData]

class PaddockTierData(TypedDict):
    tier: int
    consumptionTick: int

class PaddocksData(TypedDict):
    id: int
    nameId: int

class PaddocksDataRoot(MonoBehaviour):
    objectsById: dict[str, PaddocksData]

class ParentsRelationData(TypedDict):
    parent1: int
    parent2: int

class PointOfInterestData(TypedDict):
    id: int
    nameId: int

class PointsOfInterestDataRoot(MonoBehaviour):
    objectsById: dict[str, PointOfInterestData]

class PopupButtonData(TypedDict):
    id: int
    popupId: int
    type: int
    textId: str
    actionType: int
    actionValue: str

class PopupInformationData(TypedDict):
    id: int
    parentId: int
    titleId: str
    headerId: str
    descriptionId: int
    illuName: str
    buttons: list[PopupButtonData]
    criterion: str
    cacheType: int
    autoTrigger: int

class PopupsInformationDataRoot(MonoBehaviour):
    objectsById: dict[str, PopupInformationData]

class PresetIconData(TypedDict):
    id: int

class PresetIconsDataRoot(MonoBehaviour):
    objectsById: dict[str, PresetIconData]

class PreviewSpellZoneDescr(TypedDict):
    id: int
    displayZoneDescr: SpellZoneDescr
    isPreviewZoneHidden: int
    casterMask: str
    activationZoneDescr: SpellZoneDescr
    activationMask: str

class ProgressingAchievementSeasonData(TypedDict):
    id: int
    name: str
    seasonId: int

class ProgressingAchievementSeasonsDataRoot(MonoBehaviour):
    objectsById: dict[str, ProgressingAchievementSeasonData]

class ProgressingAchievementStepData(TypedDict):
    id: int
    progressId: int
    score: int
    isCosmetic: int
    achievementId: int
    isBuyable: int

class ProgressingAchievementStepsDataRoot(MonoBehaviour):
    objectsById: dict[str, ProgressingAchievementStepData]

class QuestCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, QuestCategoryData]

class QuestCategoryData(TypedDict):
    id: int
    nameId: int
    order: int
    questIds: list[int]

class QuestData(TypedDict):
    id: int
    nameId: int
    categoryId: int
    repeatType: int
    repeatLimit: int
    isDungeonQuest: int
    levelMin: int
    levelMax: int
    stepIds: list[int]
    isPartyQuest: int
    startCriterion: str
    followable: int
    isEvent: int

class QuestObjectiveBringItemToNpcData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveBringSoulToNpcData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveCraftItemData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveDiscoverMapData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveDiscoverSubAreaData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFightMonsterData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFightMonstersOnMapData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFreeFormData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveGoToNpcData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveMultiFightMonsterData(TypedDict):
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveParametersData(TypedDict):
    numParams: int
    parameter0: int
    parameter1: int
    parameter2: int
    parameter3: int
    parameter4: int
    dungeonOnly: int

class QuestObjectiveTypeData(TypedDict):
    id: int
    nameId: int

class QuestObjectiveTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, QuestObjectiveTypeData]

class QuestObjectivesDataRoot(MonoBehaviour):
    objectsById: dict[str, Any]

class QuestStepData(TypedDict):
    id: int
    questId: int
    nameId: int
    descriptionId: int
    dialogId: int
    optimalLevel: int
    duration: float
    objectiveIds: list[int]
    rewardsIds: list[int]

class QuestStepRewardData(TypedDict):
    id: int
    stepId: int
    levelMin: int
    levelMax: int
    kamasRatio: float
    experienceRatio: float
    kamasScaleWithPlayerLevel: int
    itemsReward: list[WrappedUintList]
    emotesReward: list[int]
    jobsReward: list[int]
    spellsReward: list[int]
    titlesReward: list[int]

class QuestStepRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, QuestStepRewardData]

class QuestStepsDataRoot(MonoBehaviour):
    objectsById: dict[str, QuestStepData]

class QuestsDataRoot(MonoBehaviour):
    objectsById: dict[str, QuestData]

class RandomDropGroupData(TypedDict):
    id: int
    randomDropItems: list[RandomDropItemData]
    displayChances: int

class RandomDropGroupsDataRoot(MonoBehaviour):
    objectsById: dict[str, RandomDropGroupData]

class RandomDropItemData(TypedDict):
    id: int
    itemId: int
    probability: float
    minQuantity: int
    maxQuantity: int

class RecipeData(TypedDict):
    resultId: int
    resultNameId: str
    resultTypeId: int
    resultLevel: int
    ingredientIds: list[int]
    quantities: list[int]
    jobId: int
    skillId: int

class RecipesDataRoot(MonoBehaviour):
    objectsById: dict[str, RecipeData]

class Rectangle(TypedDict):
    x: float
    y: float
    width: float
    height: float

class ReferencedManagedType(TypedDict):
    class_: str
    ns: str
    asm: str

class ReferencedObject(TypedDict):
    rid: int
    type: ReferencedManagedType
    data: ReferencedObjectData

class ReferencedObjectData(TypedDict):
    pass

class RideFoodData(TypedDict):
    gid: int
    typeId: int
    familyId: int

class RideFoodsDataRoot(MonoBehaviour):
    objectsById: dict[str, RideFoodData]

class RideGaugesData(TypedDict):
    id: int
    maxValue: int
    minMood: int
    maxMood: int

class RideGaugesDataRoot(MonoBehaviour):
    objectsById: dict[str, RideGaugesData]

class RideSpeciesData(TypedDict):
    id: int
    nameId: int
    extractionRewardGid: int

class RideSpeciesDataRoot(MonoBehaviour):
    objectsById: dict[str, RideSpeciesData]

class RiderBoneData(TypedDict):
    id: int

class RiderBonesDataRoot(MonoBehaviour):
    objectsById: dict[str, RiderBoneData]

class RidesData(TypedDict):
    id: int
    nameId: int
    colorId: int
    speciesId: int
    generation: int
    geneticWeight: int
    linkedItemGid: int
    extractionRewardQuantity: int
    senileExtractionRewardQuantity: int
    breedingTokenRewardQuantity: int
    breedingExperienceRewardQuantity: int
    parents: list[ParentsRelationData]
    children: list[BreedingRelationData]

class RidesDataRoot(MonoBehaviour):
    objectsById: dict[str, RidesData]

class SerializableNullVector2(TypedDict):
    x: int
    y: int

class ServerCommunitiesDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerCommunityData]

class ServerCommunityData(TypedDict):
    id: int
    nameId: int
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

class ServerData(TypedDict):
    id: int
    nameId: int
    commentId: str
    language: str
    populationId: int
    gameTypeId: int
    communityId: int
    monoAccount: int
    illus: str

class ServerGameTypeData(TypedDict):
    id: int
    selectableByPlayer: int
    nameId: int
    rulesId: int
    descriptionId: int

class ServerGameTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerGameTypeData]

class ServerLangData(TypedDict):
    id: int
    nameId: int
    langCode: str

class ServerLangsDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerLangData]

class ServerPopulationData(TypedDict):
    id: int
    nameId: int
    weight: int

class ServerPopulationsDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerPopulationData]

class ServerSeasonData(TypedDict):
    uid: int
    nameId: str
    beginning: float
    closure: float
    resetDate: float
    flagObjectId: int

class ServerSeasonsDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerSeasonData]

class ServersDataRoot(MonoBehaviour):
    objectsById: dict[str, ServerData]

class SignData(TypedDict):
    id: int
    skillParams: str
    skillId: int
    textKey: int
    skillVisibleCriterion: str

class SignsData(TypedDict):
    signs: list[SignData]

class SignsDataRoot(MonoBehaviour):
    objectsById: dict[str, SignsData]

class SkillData(TypedDict):
    id: int
    nameId: int
    parentJobId: int
    isForgemagus: int
    modifiableItemTypeIds: list[int]
    gatheredRessourceItem: int
    craftableItemIds: list[int]
    range: int
    useRangeInClient: int
    useAnimation: str
    cursor: int
    elementActionId: int
    availableInHouse: int
    clientDisplay: int
    levelMin: int
    allowMarking: int

class SkillNameData(TypedDict):
    id: int
    nameId: int

class SkillNamesDataRoot(MonoBehaviour):
    objectsById: dict[str, SkillNameData]

class SkillsDataRoot(MonoBehaviour):
    objectsById: dict[str, SkillData]

class SkinMappingData(TypedDict):
    id: int
    lowDefId: int

class SkinMappingsDataRoot(MonoBehaviour):
    objectsById: dict[str, SkinMappingData]

class SkinSlotRuleData(TypedDict):
    skinId: int
    slotRulesList: list[SkinSlotsRulesInfoData]

class SkinSlotsRulesDataRoot(MonoBehaviour):
    objectsById: dict[str, SkinSlotRuleData]

class SkinSlotsRulesInfoData(TypedDict):
    slotRuleType: int
    slotRuleInfo: int
    slotsRules: list[SlotRuleData]

class SlotRuleData(TypedDict):
    id: int
    mask: int

class SmileyData(TypedDict):
    id: int
    order: int
    gfxId: str
    forPlayers: int
    referenceId: int
    categoryId: int

class SmileyPackData(TypedDict):
    id: int
    nameId: int
    order: int
    smileys: list[int]

class SmileyPacksDataRoot(MonoBehaviour):
    objectsById: dict[str, SmileyPackData]

class SmileysDataRoot(MonoBehaviour):
    objectsById: dict[str, SmileyData]

class SocialRightData(TypedDict):
    id: int
    nameId: int
    order: int
    groupId: int

class SoundAnimationData(TypedDict):
    eventNames: list[str]
    startFrames: list[str]
    guids: list[str]
    loopingEventNames: list[str]

class SoundBoneData(TypedDict):
    animSounds: SoundBonesDictionary

class SoundBonesDataRoot(MonoBehaviour):
    objectsById: dict[str, SoundBoneData]

type SoundBonesDictionary = dict[str, SoundAnimationData]

class SpeakingItemTextData(TypedDict):
    textId: int
    textProba: float
    textStringId: str
    textLevel: int
    textSound: int
    textRestriction: str

class SpeakingItemTriggerData(TypedDict):
    textIds: list[int]

class SpeakingItemsTextsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpeakingItemTextData]

class SpeakingItemsTriggersDataRoot(MonoBehaviour):
    objectsById: dict[str, SpeakingItemTriggerData]

class SpellBombData(TypedDict):
    id: int
    chainReactionSpellId: int
    explodSpellId: int
    wallId: int
    instantSpellId: int
    comboCoeff: int

class SpellBombWallData(TypedDict):
    id: int
    spellId: int
    color: int
    linear: int
    minHop: int
    maxHop: int

class SpellBombWallsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellBombWallData]

class SpellBombsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellBombData]

class SpellData(TypedDict):
    m_flags: int
    id: int
    nameId: int
    descriptionId: int
    typeId: int
    order: int
    scriptParams: str
    scriptParamsCritical: str
    scriptId: int
    scriptIdCritical: int
    iconId: int
    spellLevels: list[int]
    boundScriptUsageData: list[BoundScriptUsageData]
    criticalHitBoundScriptUsageData: list[BoundScriptUsageData]
    basePreviewZoneDescr: SpellZoneDescr
    adminName: str

class SpellLevelData(TypedDict):
    m_flags: int
    id: int
    spellId: int
    grade: int
    spellBreed: int
    apCost: int
    minRange: int
    range: int
    criticalHitProbability: int
    maxStack: int
    maxCastPerTurn: int
    maxCastPerTarget: int
    minCastInterval: int
    initialCooldown: int
    globalCooldown: int
    minPlayerLevel: int
    statesCriterion: str
    effects: list[EffectInstanceDice]
    criticalEffect: list[EffectInstanceDice]
    previewZones: list[PreviewSpellZoneDescr]

class SpellLevelsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellLevelData]

class SpellPairData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    iconId: int

class SpellPairsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellPairData]

class SpellScriptData(TypedDict):
    rawParams: str
    type: int

class SpellScriptsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellScriptData]

class SpellStateData(TypedDict):
    id: int
    nameId: int
    preventsSpellCast: int
    preventsFight: int
    isSilent: int
    cantBeMoved: int
    cantBePushed: int
    cantDealDamage: int
    invulnerable: int
    cantSwitchPosition: int
    incurable: int
    effectsIds: list[int]
    icon: str
    iconVisibilityMask: int
    invulnerableMelee: int
    invulnerableRange: int
    cantTackle: int
    cantBeTackled: int
    displayTurnRemaining: int
    isMainState: int

class SpellStatesDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellStateData]

class SpellTypeData(TypedDict):
    id: int
    longNameId: str
    shortNameId: str

class SpellTypesDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellTypeData]

class SpellVariantData(TypedDict):
    id: int
    breedId: int
    spellIds: list[int]

class SpellVariantsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellVariantData]

class SpellZoneDescr(TypedDict):
    cellIds: list[int]
    shape: int
    param1: int
    param2: int
    damageDecreaseStepPercent: int
    maxDamageDecreaseApplyCount: int
    isStopAtTarget: int
    forcedDirection: int
    includeCarried: int
    onlyAffectIfInSightLine: int

class SpellsDataRoot(MonoBehaviour):
    objectsById: dict[str, SpellData]

class StealthBoneData(TypedDict):
    id: int

class StealthBonesDataRoot(MonoBehaviour):
    objectsById: dict[str, StealthBoneData]

class SubAreaData(TypedDict):
    id: int
    nameId: int
    areaId: int
    mapIds: list[int]
    bounds: Rectangle
    shape: list[int]
    customWorldMapId: int
    packId: int
    level: int
    isConquestVillage: int
    basicAccountAllowed: int
    displayOnWorldMap: int
    mountAutoTripAllowed: int
    psiAllowed: int
    monsters: list[int]
    entranceMapIds: list[int]
    exitMapIds: list[int]
    capturable: int
    achievements: list[int]
    exploreAchievementId: int
    harvestables: list[int]
    associatedZaapMapId: int
    neighbors: list[int]
    dungeonId: int

class SubAreasDataRoot(MonoBehaviour):
    objectsById: dict[str, SubAreaData]

class SuperAreaData(TypedDict):
    id: int
    nameId: int
    worldmapId: int
    hasWorldMap: int

class SuperAreasDataRoot(MonoBehaviour):
    objectsById: dict[str, SuperAreaData]

class TaxCollectorFirstnameData(TypedDict):
    id: int
    firstnameId: str

class TaxCollectorFirstnamesDataRoot(MonoBehaviour):
    objectsById: dict[str, TaxCollectorFirstnameData]

class TaxCollectorNameData(TypedDict):
    id: int
    nameId: int

class TaxCollectorNamesDataRoot(MonoBehaviour):
    objectsById: dict[str, TaxCollectorNameData]

class TextIconReferenceData(TypedDict):
    referenceKey: str

class TextIconReferencesDataRoot(MonoBehaviour):
    objectsById: dict[str, TextIconReferenceData]

class TitleCategoriesDataRoot(MonoBehaviour):
    objectsById: dict[str, TitleCategoryData]

class TitleCategoryData(TypedDict):
    id: int
    nameId: int

class TitleData(TypedDict):
    id: int
    nameMaleId: str
    nameFemaleId: str
    visible: int
    categoryId: int

class TitlesDataRoot(MonoBehaviour):
    objectsById: dict[str, TitleData]

class VeteranRewardData(TypedDict):
    id: int
    requiredSubDays: int
    itemGID: int
    itemQuantity: int

class VeteranRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, VeteranRewardData]

class WaypointData(TypedDict):
    id: int
    mapId: int
    subAreaId: int
    activated: int

class WaypointsDataRoot(MonoBehaviour):
    objectsById: dict[str, WaypointData]

class WeaponData(TypedDict):
    m_flags: int
    id: int
    nameId: int
    typeId: int
    descriptionId: int
    iconId: int
    level: int
    realWeight: int
    price: float
    itemSetId: int
    criterions: str
    criterionsTarget: str
    appearanceId: int
    isColorable: int
    recipeSlots: int
    recipeIds: list[int]
    dropMonsterIds: list[int]
    dropTemporisMonsterIds: list[int]
    possibleEffects: list[EffectInstanceData]
    evolutiveEffectIds: list[int]
    favoriteSubAreas: list[int]
    favoriteSubAreasBonus: int
    craftXpRatio: int
    craftVisibleCriterion: str
    craftConditionalCriterion: str
    craftFeasibleCriterion: str
    visibilityCriterion: str
    recyclingNuggets: float
    favoriteRecyclingSubareas: list[int]
    resourcesBySubarea: list[WrappedIntList]
    importantNoticeId: str
    criticalHitBonus: int
    minRange: int
    criticalHitProbability: int
    range: int
    castInLine: int
    apCost: int
    castInDiagonal: int
    castTestLos: int
    maxCastPerTurn: int

class WorldEventData(TypedDict):
    id: int
    nameId: int
    descriptionId: int
    categoryId: int
    level: int
    areas: list[int]
    subareas: list[int]
    globalDrops: list[int]
    fightScenarios: list[int]
    deletedObjects: list[int]
    monsterHunterGroupsPerMap: int
    dungeonHunterGroupsPerMap: int
    preMsgId: int
    startMsgId: int
    endMsgId: int
    preMsgDelay: int
    worldEventRewardId: int
    duration: int
    worldEventDataType: int
    worldEventEventId: int

class WorldEventDungeonData(TypedDict):
    dungeonId: int
    dungeonMapIdTeleport: int
    scoreGroupShared: int
    scorePerDamage: int
    scorePerDungeon: int

class WorldEventFarmingSimulatorData(TypedDict):
    scorePerHarvest: int

class WorldEventMonstersHunterData(TypedDict):
    monsterList: list[int]
    criterion: str
    mapList: list[int]
    subareaList: list[int]
    areaList: list[int]
    scoreGroupShared: int
    scorePerDamage: int
    scorePerMonster: int

class WorldEventRewardData(TypedDict):
    worldEventRewardId: int
    objects: str
    emotes: str
    spells: str
    titles: str
    ornaments: str
    rankingConditions: str
    criterions: str
    experience: float
    kamas: float
    gameaction: int
    guildPoints: int
    isForTeam: int
    order: int

class WorldEventWorldBossesData(TypedDict):
    monsterList: list[int]
    criterion: str
    mapList: list[int]
    subareaList: list[int]
    areaList: list[int]
    scoreGroupShared: int
    scorePerDamage: int
    scoreTotal: int
    scoreRatio: int
    scoreDayCount: int

class WorldEventsDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventData]

class WorldEventsDungeonsDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventDungeonData]

class WorldEventsFarmingSimulatorDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventFarmingSimulatorData]

class WorldEventsMonstersHunterDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventMonstersHunterData]

class WorldEventsRewardsDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventRewardData]

class WorldEventsWorldBossesDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldEventWorldBossesData]

class WorldMapData(TypedDict):
    id: int
    nameId: int
    origineX: int
    origineY: int
    mapWidth: float
    mapHeight: float
    minScale: float
    maxScale: float
    startScale: float
    totalWidth: int
    totalHeight: int
    zoom: list[float]
    visibleOnMap: int

class WorldMapsDataRoot(MonoBehaviour):
    objectsById: dict[str, WorldMapData]

class WrappedEffectInstanceList(TypedDict):
    values: list[EffectInstanceData]

class WrappedFloatList(TypedDict):
    values: list[float]

class WrappedIntList(TypedDict):
    values: list[int]

class WrappedUintList(TypedDict):
    values: list[int]

class int2_storage(TypedDict):
    x: int
    y: int

class managedRefArrayItem(TypedDict):
    rid: int

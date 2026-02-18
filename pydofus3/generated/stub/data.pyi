from UnityPy.classes.PPtr import PPtr
from UnityPy.classes.generated import MonoBehaviour
from typing import Union

class AchievementCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AchievementCategoryData]
    references: ManagedReferencesRegistry

class AchievementCategoryData:
    id: int
    nameId: int
    parentId: int
    icon: str
    order: int
    color: str
    achievementIds: list[int]
    visibilityCriterion: str

class AchievementData:
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

class AchievementObjectiveData:
    id: int
    achievementId: int
    order: int
    nameId: int
    criterion: str

class AchievementObjectivesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AchievementObjectiveData]
    references: ManagedReferencesRegistry

class AchievementRewardData:
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
    objectsById: MetadataDictionaryContainer[AchievementRewardData]
    references: ManagedReferencesRegistry

class AchievementsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AchievementData]
    references: ManagedReferencesRegistry

class ActionFilterData:
    id: int
    nameId: int
    order: int

class ActionFiltersDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ActionFilterData]
    references: ManagedReferencesRegistry

class ActivitySuggestionCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ActivitySuggestionCategoryData]
    references: ManagedReferencesRegistry

class ActivitySuggestionCategoryData:
    id: int
    nameId: int
    parentId: int

class ActivitySuggestionData:
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
    objectsById: MetadataDictionaryContainer[ActivitySuggestionData]
    references: ManagedReferencesRegistry

class AlignmentGiftData:
    id: int
    nameId: int

class AlignmentGiftsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentGiftData]
    references: ManagedReferencesRegistry

class AlignmentOrderData:
    id: int
    nameId: int
    sideId: int

class AlignmentOrdersDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentOrderData]
    references: ManagedReferencesRegistry

class AlignmentRankData:
    id: int
    orderId: int
    nameId: int
    descriptionId: int
    minimumAlignment: int

class AlignmentRankGiftsData:
    id: int
    gifts: list[int]

class AlignmentRanksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentRankData]
    references: ManagedReferencesRegistry

class AlignmentRanksGiftsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentRankGiftsData]
    references: ManagedReferencesRegistry

class AlignmentSideData:
    id: int
    nameId: int

class AlignmentSidesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentSideData]
    references: ManagedReferencesRegistry

class AlignmentTitleData:
    sideId: int
    namesId: list[str]
    shortsId: list[str]

class AlignmentTitlesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlignmentTitleData]
    references: ManagedReferencesRegistry

class AllianceRankData:
    id: int
    nameId: int
    order: int
    isModifiable: int
    gfxId: int

class AllianceRankNameSuggestionData:
    uiKey: str

class AllianceRankNameSuggestionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceRankNameSuggestionData]
    references: ManagedReferencesRegistry

class AllianceRanksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceRankData]
    references: ManagedReferencesRegistry

class AllianceRightData:
    id: int
    nameId: int
    order: int
    groupId: int

class AllianceRightGroupData:
    id: int
    nameId: int
    order: int
    rights: list[managedRefArrayItem[SocialRightData]]
    references: ManagedReferencesRegistry

class AllianceRightGroupsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceRightGroupData]
    references: ManagedReferencesRegistry

class AllianceRightsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceRightData]
    references: ManagedReferencesRegistry

class AllianceTagData:
    id: int
    typeId: int
    nameId: int
    order: int

class AllianceTagTypeData:
    id: int
    nameId: int

class AllianceTagTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceTagTypeData]
    references: ManagedReferencesRegistry

class AllianceTagsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AllianceTagData]
    references: ManagedReferencesRegistry

class AlmanaxCalendarData:
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
    objectsById: MetadataDictionaryContainer[AlmanaxCalendarData]
    references: ManagedReferencesRegistry

class AlmanaxCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlmanaxCategoryData]
    references: ManagedReferencesRegistry

class AlmanaxCategoryData:
    id: int
    nameId: int
    protectorNameId: int
    protectorDescriptionId: int
    protectorIllustrationId: int

class AlmanaxZodiacData:
    id: int
    nameId: int
    descriptionId: int
    dateStart: str
    dateEnd: str
    picture: str

class AlmanaxZodiacsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlmanaxZodiacData]
    references: ManagedReferencesRegistry

class AlterationCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlterationCategoryData]
    references: ManagedReferencesRegistry

class AlterationCategoryData:
    id: int
    nameId: int
    parentId: int

class AlterationData:
    id: int
    nameId: int
    descriptionId: int
    categoryId: int
    iconId: int
    isVisible: int
    criterions: str
    isWebDisplay: int
    possibleEffects: list[managedRefArrayItem[EffectInstanceData]]
    references: ManagedReferencesRegistry

class AlterationsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AlterationData]
    references: ManagedReferencesRegistry

class AnimFunMonsterData:
    animId: int
    entityId: int
    animName: str
    animWeight: int

class AnimFunNpcData:
    animId: int
    entityId: int
    animName: str
    animWeight: int
    subAnimFunData: list[NestedAnimFunNpcData]

class AppearanceData:
    id: int
    type: int
    data: str
    usePlayerLook: int

class AppearancesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AppearanceData]
    references: ManagedReferencesRegistry

class AreaData:
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
    objectsById: MetadataDictionaryContainer[AreaData]
    references: ManagedReferencesRegistry

class ArenaLeagueData:
    id: int
    nameId: int
    ornamentId: int
    icon: str
    illus: str
    isLastLeague: int
    lowRatingBound: int
    highRatingBound: int

class ArenaLeagueSeasonData:
    uid: int
    nameId: str
    beginning: float
    closure: float
    resetDate: float
    flagObjectId: int

class ArenaLeagueSeasonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ArenaLeagueSeasonData]
    references: ManagedReferencesRegistry

class ArenaLeaguesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ArenaLeagueData]
    references: ManagedReferencesRegistry

class AuctionHouseData:
    id: int
    typeId: int

class AuctionHousesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[AuctionHouseData]
    references: ManagedReferencesRegistry

class BodiesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BodyData]
    references: ManagedReferencesRegistry

class BodyData:
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

class BonusCriterionData:
    id: int
    type: int
    value: int

class BonusData:
    id: int
    type: int
    amount: int
    criterionsIds: list[int]

class BonusesCriterionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BonusCriterionData]
    references: ManagedReferencesRegistry

class BonusesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BonusData]
    references: ManagedReferencesRegistry

class BoundScriptUsageData:
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

class BreachBossData:
    id: int
    monsterId: int
    category: int
    apparitionCriterion: str
    accessCriterion: str
    incompatibleBosses: list[int]
    rewardId: int

class BreachBossesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreachBossData]
    references: ManagedReferencesRegistry

class BreachDungeonModificatorData:
    id: int
    modificatorId: int
    criterion: str
    additionalRewardPercent: float
    score: float
    isPositiveForPlayers: int
    tooltipBaseline: str

class BreachDungeonModificatorsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreachDungeonModificatorData]
    references: ManagedReferencesRegistry

class BreachPrizeData:
    id: int
    nameId: int
    categoryId: int
    tooltipKey: str
    descriptionKey: str

class BreachPrizesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreachPrizeData]
    references: ManagedReferencesRegistry

class BreachWorldMapCoordinateData:
    mapStage: int
    mapCoordinateX: int
    mapCoordinateY: int
    unexploredMapIcon: int
    exploredMapIcon: int

class BreachWorldMapCoordinatesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreachWorldMapCoordinateData]
    references: ManagedReferencesRegistry

class BreachWorldMapSectorData:
    id: int
    sectorNameId: str
    legendId: str
    sectorIcon: str
    minStage: int
    maxStage: int

class BreachWorldMapSectorsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreachWorldMapSectorData]
    references: ManagedReferencesRegistry

class BreedData:
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

class BreedRoleByBreedData:
    roleId: int
    descriptionId: int
    value: int
    order: int

class BreedRoleData:
    id: int
    nameId: int
    descriptionId: int
    assetId: int
    color: int

class BreedRolesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreedRoleData]
    references: ManagedReferencesRegistry

class BreedingRelationData:
    parent: int
    child: int

class BreedsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[BreedData]
    references: ManagedReferencesRegistry

class CalendarEventData:
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
    objectsById: MetadataDictionaryContainer[CalendarEventData]
    references: ManagedReferencesRegistry

class ChallengeData:
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
    objectsById: MetadataDictionaryContainer[ChallengeData]
    references: ManagedReferencesRegistry

class CharacterXPMappingsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CharacterXpMappingData]
    references: ManagedReferencesRegistry

class CharacterXpMappingData:
    experiencePoints: float

class CharacteristicCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CharacteristicCategoryData]
    references: ManagedReferencesRegistry

class CharacteristicCategoryData:
    id: int
    nameId: int
    order: int
    characteristicIds: list[int]

class CharacteristicData:
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
    objectsById: MetadataDictionaryContainer[CharacteristicData]
    references: ManagedReferencesRegistry

class ChatChannelData:
    id: int
    nameId: int
    descriptionId: int
    shortcut: str
    isPrivate: int

class ChatChannelsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ChatChannelData]
    references: ManagedReferencesRegistry

class ChoiceData:
    id: int
    choiceNameId: int
    duration: int
    options: list[ChoiceOptionData]

class ChoiceOptionData:
    id: int
    descriptionId: int
    rewardType: int
    rewardValue: str
    gfxId: int

class ChoicesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ChoiceData]
    references: ManagedReferencesRegistry

class CollectableData:
    entityId: int
    name: str
    typeId: int
    gfxId: int
    order: int
    rarity: int

class CollectablesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CollectableData]
    references: ManagedReferencesRegistry

class CollectionData:
    typeId: int
    name: str
    criterion: str
    collectables: list[CollectableData]

class CollectionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CollectionData]
    references: ManagedReferencesRegistry

class CompanionCharacteristicData:
    id: int
    caracId: int
    companionId: int
    order: int
    statPerLevelRange: list[WrappedFloatList]

class CompanionCharacteristicsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CompanionCharacteristicData]
    references: ManagedReferencesRegistry

class CompanionData:
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

class CompanionSpellData:
    id: int
    spellId: int
    companionId: int
    gradeByLevel: str

class CompanionSpellsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CompanionSpellData]
    references: ManagedReferencesRegistry

class CompanionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CompanionData]
    references: ManagedReferencesRegistry

class CreatureBoneOverrideData:
    boneId: int
    creatureBoneId: int

class CreatureBoneTypeData:
    id: int
    creatureBoneId: int

class CreatureBonesOverridesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CreatureBoneOverrideData]
    references: ManagedReferencesRegistry

class CreatureBonesTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CreatureBoneTypeData]
    references: ManagedReferencesRegistry

class CustomModeBreedSpellData:
    id: int
    pairId: int
    breedId: int
    isInitialSpell: int
    isHidden: int

class CustomModeBreedSpellsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[CustomModeBreedSpellData]
    references: ManagedReferencesRegistry

class DocumentData:
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
    objectsById: MetadataDictionaryContainer[DocumentData]
    references: ManagedReferencesRegistry

class DungeonData:
    id: int
    nameId: int
    optimalPlayerLevel: int
    mapIds: list[int]
    entranceMapId: int
    exitMapId: int

class DungeonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[DungeonData]
    references: ManagedReferencesRegistry

class EffectData:
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

class EffectInstanceData:
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

class EffectInstanceDice:
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
    objectsById: MetadataDictionaryContainer[EffectData]
    references: ManagedReferencesRegistry

class EmblemBackgroundData:
    id: int
    order: int

class EmblemBackgroundsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[EmblemBackgroundData]
    references: ManagedReferencesRegistry

class EmblemSymbolCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[EmblemSymbolCategoryData]
    references: ManagedReferencesRegistry

class EmblemSymbolCategoryData:
    id: int
    nameId: int

class EmblemSymbolData:
    id: int
    skinId: int
    iconId: int
    order: int
    categoryId: int
    colorizable: int

class EmblemSymbolsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[EmblemSymbolData]
    references: ManagedReferencesRegistry

class EmoticonData:
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
    objectsById: MetadataDictionaryContainer[EmoticonData]
    references: ManagedReferencesRegistry

class EvolutiveEffectData:
    id: int
    actionId: int
    targetId: int
    progressionPerLevelRange: list[WrappedFloatList]

class EvolutiveEffectsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[EvolutiveEffectData]
    references: ManagedReferencesRegistry

class EvolutiveItemTypeData:
    id: int
    maxLevel: int
    experienceBoost: float
    experienceByLevel: list[int]

class EvolutiveItemTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[EvolutiveItemTypeData]
    references: ManagedReferencesRegistry

class ExpeditionSeasonData:
    uid: int
    nameId: str
    beginning: float
    closure: float
    resetDate: float
    flagObjectId: int

class ExpeditionSeasonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ExpeditionSeasonData]
    references: ManagedReferencesRegistry

class ExternalNotificationData:
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
    objectsById: MetadataDictionaryContainer[ExternalNotificationData]
    references: ManagedReferencesRegistry

class FeatureDescriptionData:
    id: int
    nameId: int
    descriptionId: int
    priority: int
    parentId: int
    children: list[int]
    criterion: str
    images: list[FeatureImage]

class FeatureDescriptionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[FeatureDescriptionData]
    references: ManagedReferencesRegistry

class FeatureImage:
    id: int
    order: int
    category: int
    imageId: str
    verticalAlign: int
    horizontalAlign: int

class FightScenarioData:
    id: int
    nameId: str

class FightScenariosDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[FightScenarioData]
    references: ManagedReferencesRegistry

class ForgettableSpellData:
    id: int
    pairId: int
    itemId: int

class ForgettableSpellsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ForgettableSpellData]
    references: ManagedReferencesRegistry

class GuildChestTabData:
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
    objectsById: MetadataDictionaryContainer[GuildChestTabData]
    references: ManagedReferencesRegistry

class GuildHallData:
    id: int
    nameId: int
    subareaId: int
    mapId: int

class GuildHallThemeData:
    id: int
    nameId: int
    order: int

class GuildHallThemesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildHallThemeData]
    references: ManagedReferencesRegistry

class GuildHallsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildHallData]
    references: ManagedReferencesRegistry

class GuildLevelRewardData:
    level: int
    nameId: int
    descriptionId: int
    picto: str

class GuildLevelRewardsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildLevelRewardData]
    references: ManagedReferencesRegistry

class GuildMissionActivitiesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionActivityData]
    references: ManagedReferencesRegistry

class GuildMissionActivityData:
    id: int
    nameId: int
    level: int
    recommendedPlayers: int
    rerollCost: int
    milestonesIds: list[int]

class GuildMissionData:
    id: int
    categoryId: int
    superCategoryId: int
    nameId: int
    recommendedLevel: int
    gradeId: int
    activityPoint: int
    token: int
    objectives: list[int]

class GuildMissionGradeData:
    id: int
    name: str
    rankId: int
    activityPoint: int
    token: int

class GuildMissionGradesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionGradeData]
    references: ManagedReferencesRegistry

class GuildMissionMilestoneData:
    id: int
    activityId: int
    nameId: int
    milestoneLevel: int
    activityPoint: int
    xp: int
    acknowledgmentPoint: int

class GuildMissionMilestoneRewardsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer
    references: ManagedReferencesRegistry

class GuildMissionMilestonesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionMilestoneData]
    references: ManagedReferencesRegistry

class GuildMissionObjectiveData:
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
    objectsById: MetadataDictionaryContainer[GuildMissionObjectiveData]
    references: ManagedReferencesRegistry

class GuildMissionRankData:
    id: int
    nameId: int
    grades: list[int]

class GuildMissionRanksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionRankData]
    references: ManagedReferencesRegistry

class GuildMissionSuperCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionSuperCategoryData]
    references: ManagedReferencesRegistry

class GuildMissionSuperCategoryData:
    id: int
    nameId: int

class GuildMissionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildMissionData]
    references: ManagedReferencesRegistry

class GuildRankData:
    id: int
    nameId: int
    order: int
    gfxId: int

class GuildRankNameSuggestionData:
    uiKey: str

class GuildRankNameSuggestionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildRankNameSuggestionData]
    references: ManagedReferencesRegistry

class GuildRanksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildRankData]
    references: ManagedReferencesRegistry

class GuildRightData:
    id: int
    nameId: int
    order: int
    groupId: int

class GuildRightGroupData:
    id: int
    nameId: int
    order: int
    rights: list[managedRefArrayItem[SocialRightData]]
    references: ManagedReferencesRegistry

class GuildRightGroupsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildRightGroupData]
    references: ManagedReferencesRegistry

class GuildRightsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildRightData]
    references: ManagedReferencesRegistry

class GuildShopBoostData:
    id: int
    nameId: int
    descriptionId: int
    alterationId: int

class GuildShopBoostsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildShopBoostData]
    references: ManagedReferencesRegistry

class GuildTagData:
    id: int
    typeId: int
    nameId: int
    order: int

class GuildTagTypeData:
    id: int
    nameId: int

class GuildTagTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildTagTypeData]
    references: ManagedReferencesRegistry

class GuildTagsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[GuildTagData]
    references: ManagedReferencesRegistry

class HavenbagFurnitureData:
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
    objectsById: MetadataDictionaryContainer[HavenbagFurnitureData]
    references: ManagedReferencesRegistry

class HavenbagThemeData:
    id: int
    nameId: int
    mapId: int

class HavenbagThemesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[HavenbagThemeData]
    references: ManagedReferencesRegistry

class HeadData:
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
    objectsById: MetadataDictionaryContainer[HeadData]
    references: ManagedReferencesRegistry

class HintCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[HintCategoryData]
    references: ManagedReferencesRegistry

class HintCategoryData:
    id: int
    nameId: int

class HintData:
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
    objectsById: MetadataDictionaryContainer[HintData]
    references: ManagedReferencesRegistry

class HouseData:
    typeId: int
    defaultPrice: int
    nameId: int
    descriptionId: int
    gfxId: int
    roomCount: int

class HousesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[HouseData]
    references: ManagedReferencesRegistry

class IdleData:
    nameId: int
    animationKey: str
    known: int
    iconIdMale: str
    iconIdFemale: str
    order: int
    criterion: str
    breed: int

class IdlesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[IdleData]
    references: ManagedReferencesRegistry

class InfiniteDreamIntensitiesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InfiniteDreamIntensityData]
    references: ManagedReferencesRegistry

class InfiniteDreamIntensityData:
    id: int
    intensity: int
    droplegend: int
    dropBonus: float
    xpBonus: float
    money: int
    additionalLife: int
    nameId: int
    dreamFragments: int

class InfiniteDreamRewardActionData:
    id: int
    effect: EffectInstanceData
    duration: int
    isAlly: int

class InfiniteDreamRewardActionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InfiniteDreamRewardActionData]
    references: ManagedReferencesRegistry

class InfiniteDreamRewardData:
    id: int
    nameId: int
    descriptionId: int
    actions: list[int]

class InfiniteDreamRewardsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InfiniteDreamRewardData]
    references: ManagedReferencesRegistry

class InfiniteDreamTrialData:
    id: int
    nameId: int
    descriptionId: int
    seed: str
    achievementId: int
    achievementIntensity: int
    picture: str

class InfiniteDreamTrialsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InfiniteDreamTrialData]
    references: ManagedReferencesRegistry

class InfoMessageData:
    typeId: int
    messageId: int
    textId: int

class InfoMessagesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InfoMessageData]
    references: ManagedReferencesRegistry

class InteractiveData:
    id: int
    nameId: int

class InteractivesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[InteractiveData]
    references: ManagedReferencesRegistry

class ItemData:
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
    possibleEffects: list[managedRefArrayItem[EffectInstanceData]]
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
    references: ManagedReferencesRegistry

class ItemSetData:
    id: int
    items: list[int]
    nameId: int
    bonusIsSecret: int
    isCosmetic: int
    effects: list[WrappedEffectInstanceList]
    references: ManagedReferencesRegistry

class ItemSetsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ItemSetData]
    references: ManagedReferencesRegistry

class ItemSuperTypeData:
    id: int
    possiblePositions: list[int]

class ItemSuperTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ItemSuperTypeData]
    references: ManagedReferencesRegistry

class ItemTypeData:
    id: int
    nameId: int
    superTypeId: int
    categoryId: int
    isInEncyclopedia: int
    rawZone: str
    craftXpRatio: int
    evolutiveTypeId: int

class ItemTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ItemTypeData]
    references: ManagedReferencesRegistry

class ItemsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ItemData]
    references: ManagedReferencesRegistry

class JobData:
    id: int
    nameId: int
    iconId: int
    hasLegendaryCraft: int

class JobsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[JobData]
    references: ManagedReferencesRegistry

class KothRoleData:
    id: int
    nameId: int
    isDefault: int

class KothRolesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[KothRoleData]
    references: ManagedReferencesRegistry

class LegendaryPowerCategoryData:
    id: int
    categoryName: str
    categoryOverridable: int
    categorySpells: list[int]

class LegendaryPowersCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[LegendaryPowerCategoryData]
    references: ManagedReferencesRegistry

class LegendaryTreasureHuntData:
    id: int
    nameId: int
    level: int
    chestId: int
    monsterId: int
    mapItemId: int
    xpRatio: float

class LegendaryTreasureHuntsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[LegendaryTreasureHuntData]
    references: ManagedReferencesRegistry

class LivingObjectSkinMoodsData:
    skinId: int
    moods: list[WrappedIntList]

class LivingObjectSkinsMoodsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[LivingObjectSkinMoodsData]
    references: ManagedReferencesRegistry

class LuaFormulaData:
    formula: str

class LuaFormulasDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[LuaFormulaData]
    references: ManagedReferencesRegistry

class ManagedReferencesRegistry:
    version: int
    RefIds: list[ReferencedObject]

class MapInformationData:
    m_flags: int
    id: int
    posX: int
    posY: int
    nameId: int
    subAreaId: int
    worldMap: int
    tacticalModeTemplateId: int

class MapReferenceData:
    id: int
    mapId: int
    cellId: int

class MapReferencesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MapReferenceData]
    references: ManagedReferencesRegistry

class MapScrollActionData:
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
    objectsById: MetadataDictionaryContainer[MapScrollActionData]
    references: ManagedReferencesRegistry

class MapsCoordinateData:
    compressedCoords: int
    mapIds: list[int]

class MapsCoordinatesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MapsCoordinateData]
    references: ManagedReferencesRegistry

class MapsInformationDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MapInformationData]
    references: ManagedReferencesRegistry

class MetadataDictionaryContainer[T]:
    m_keys: list[int]
    m_values: list[managedRefArrayItem]

class ModsterData:
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
    objectsById: MetadataDictionaryContainer[ModsterData]
    references: ManagedReferencesRegistry

class MonsterBonusCharacteristicsData:
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

class MonsterData:
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

class MonsterDropCoefficientData:
    monsterId: int
    monsterGrade: int
    dropCoefficient: float
    criterions: str

class MonsterDropData:
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

class MonsterGlobalDropData:
    objectId: int
    alterationId: int
    receiverCriterion: str
    disableDropModificator: int
    minPercentDrop: float
    maxPercentDrop: float

class MonsterGradeData:
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

class MonsterMiniBossData:
    id: int
    monsterReplacingId: int

class MonsterMiniBossesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MonsterMiniBossData]
    references: ManagedReferencesRegistry

class MonsterRaceData:
    id: int
    superRaceId: int
    nameId: int
    aggressiveZoneSize: int
    aggressiveLevelDiff: int
    aggressiveImmunityCriterion: str
    aggressiveAttackDelay: int
    monsters: list[int]

class MonsterRacesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MonsterRaceData]
    references: ManagedReferencesRegistry

class MonsterSoulData:
    objectId: int
    criterion: str
    hasCriterion: int

class MonsterSuperRaceData:
    id: int
    nameId: int

class MonsterSuperRacesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MonsterSuperRaceData]
    references: ManagedReferencesRegistry

class MonstersDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MonsterData]
    references: ManagedReferencesRegistry

class MonthData:
    nameId: int

class MonthsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MonthData]
    references: ManagedReferencesRegistry

class MountBehaviorData:
    id: int
    nameId: int
    descriptionId: int

class MountBehaviorsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MountBehaviorData]
    references: ManagedReferencesRegistry

class MountBoneData:
    id: int

class MountBonesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MountBoneData]
    references: ManagedReferencesRegistry

class MountData:
    id: int
    familyId: int
    nameId: int
    look: str
    certificateId: int
    effects: list[managedRefArrayItem[EffectInstanceData]]
    references: ManagedReferencesRegistry

class MountFamiliesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MountFamilyData]
    references: ManagedReferencesRegistry

class MountFamilyData:
    id: int
    nameId: int
    headUri: str

class MountsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[MountData]
    references: ManagedReferencesRegistry

class NamingRuleData:
    id: int
    minLength: int
    maxLength: int
    regexp: str

class NamingRulesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[NamingRuleData]
    references: ManagedReferencesRegistry

class NestedAnimFunNpcData:
    animId: int
    entityId: int
    animName: str
    animWeight: int

class NotificationData:
    id: int
    titleId: str
    messageId: str
    iconId: int
    typeId: int
    trigger: str
    cantBeClosed: int

class NotificationsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[NotificationData]
    references: ManagedReferencesRegistry

class NpcActionData:
    id: int
    realId: int
    nameId: int

class NpcActionsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[NpcActionData]
    references: ManagedReferencesRegistry

class NpcData:
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

class NpcDialogData:
    id: int
    messageId: int
    moodId: int
    bubblePosition: int

class NpcDialogSkinData:
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
    objectsById: MetadataDictionaryContainer[NpcDialogSkinData]
    references: ManagedReferencesRegistry

class NpcMessageData:
    id: int
    messageId: str
    messageParams: list[str]
    messageSkinId: int
    messageBubblePosition: int
    messageNpcMoodId: int

class NpcMessagesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[NpcMessageData]
    references: ManagedReferencesRegistry

class NpcsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[NpcData]
    references: ManagedReferencesRegistry

class OptionalFeatureData:
    id: int
    keyword: str
    isClient: int
    isServer: int
    isActivationOnLaunch: int
    isActivationOnServerConnection: int
    activationCriterions: str

class OptionalFeaturesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[OptionalFeatureData]
    references: ManagedReferencesRegistry

class OrnamentData:
    id: int
    nameId: int
    visible: int
    assetId: int
    iconId: int
    order: int

class OrnamentsRootData(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[OrnamentData]
    references: ManagedReferencesRegistry

class PaddockGaugesData:
    id: int
    name: str
    tierMaxValues: list[PaddockTierData]

class PaddockGaugesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[PaddockGaugesData]
    references: ManagedReferencesRegistry

class PaddockTierData:
    tier: int
    consumptionTick: int

class PaddocksData:
    id: int
    nameId: int

class PaddocksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[PaddocksData]
    references: ManagedReferencesRegistry

class ParentsRelationData:
    parent1: int
    parent2: int

class PointOfInterestData:
    id: int
    nameId: int

class PointsOfInterestDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[PointOfInterestData]
    references: ManagedReferencesRegistry

class PopupButtonData:
    id: int
    popupId: int
    type: int
    textId: str
    actionType: int
    actionValue: str

class PopupInformationData:
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
    objectsById: MetadataDictionaryContainer[PopupInformationData]
    references: ManagedReferencesRegistry

class PresetIconData:
    id: int

class PresetIconsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[PresetIconData]
    references: ManagedReferencesRegistry

class PreviewSpellZoneDescr:
    id: int
    displayZoneDescr: SpellZoneDescr
    isPreviewZoneHidden: int
    casterMask: str
    activationZoneDescr: SpellZoneDescr
    activationMask: str

class ProgressingAchievementSeasonData:
    id: int
    name: str
    seasonId: int

class ProgressingAchievementSeasonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ProgressingAchievementSeasonData]
    references: ManagedReferencesRegistry

class ProgressingAchievementStepData:
    id: int
    progressId: int
    score: int
    isCosmetic: int
    achievementId: int
    isBuyable: int

class ProgressingAchievementStepsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ProgressingAchievementStepData]
    references: ManagedReferencesRegistry

class QuestCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[QuestCategoryData]
    references: ManagedReferencesRegistry

class QuestCategoryData:
    id: int
    nameId: int
    order: int
    questIds: list[int]

class QuestData:
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

class QuestObjectiveBringItemToNpcData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveBringSoulToNpcData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveCraftItemData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveDiscoverMapData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveDiscoverSubAreaData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFightMonsterData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFightMonstersOnMapData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveFreeFormData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveGoToNpcData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveMultiFightMonsterData:
    id: int
    stepId: int
    typeId: int
    dialogId: int
    parameters: QuestObjectiveParametersData
    coords: SerializableNullVector2
    mapId: int

class QuestObjectiveParametersData:
    numParams: int
    parameter0: int
    parameter1: int
    parameter2: int
    parameter3: int
    parameter4: int
    dungeonOnly: int

class QuestObjectiveTypeData:
    id: int
    nameId: int

class QuestObjectiveTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[QuestObjectiveTypeData]
    references: ManagedReferencesRegistry

class QuestObjectivesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer
    references: ManagedReferencesRegistry

class QuestStepData:
    id: int
    questId: int
    nameId: int
    descriptionId: int
    dialogId: int
    optimalLevel: int
    duration: float
    objectiveIds: list[int]
    rewardsIds: list[int]

class QuestStepRewardData:
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
    objectsById: MetadataDictionaryContainer[QuestStepRewardData]
    references: ManagedReferencesRegistry

class QuestStepsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[QuestStepData]
    references: ManagedReferencesRegistry

class QuestsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[QuestData]
    references: ManagedReferencesRegistry

class RandomDropGroupData:
    id: int
    randomDropItems: list[RandomDropItemData]
    displayChances: int

class RandomDropGroupsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RandomDropGroupData]
    references: ManagedReferencesRegistry

class RandomDropItemData:
    id: int
    itemId: int
    probability: float
    minQuantity: int
    maxQuantity: int

class RecipeData:
    resultId: int
    resultNameId: str
    resultTypeId: int
    resultLevel: int
    ingredientIds: list[int]
    quantities: list[int]
    jobId: int
    skillId: int

class RecipesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RecipeData]
    references: ManagedReferencesRegistry

class Rectangle:
    x: float
    y: float
    width: float
    height: float

class ReferencedManagedType:
    class: str
    ns: str
    asm: str

class ReferencedObject:
    rid: int
    type: ReferencedManagedType
    data: ReferencedObjectData

class ReferencedObjectData:
    pass

class RideFoodData:
    gid: int
    typeId: int
    familyId: int

class RideFoodsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RideFoodData]
    references: ManagedReferencesRegistry

class RideGaugesData:
    id: int
    maxValue: int
    minMood: int
    maxMood: int

class RideGaugesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RideGaugesData]
    references: ManagedReferencesRegistry

class RideSpeciesData:
    id: int
    nameId: int
    extractionRewardGid: int

class RideSpeciesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RideSpeciesData]
    references: ManagedReferencesRegistry

class RiderBoneData:
    id: int

class RiderBonesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[RiderBoneData]
    references: ManagedReferencesRegistry

class RidesData:
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
    objectsById: MetadataDictionaryContainer[RidesData]
    references: ManagedReferencesRegistry

class SerializableNullVector2:
    x: int
    y: int

class ServerCommunitiesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ServerCommunityData]
    references: ManagedReferencesRegistry

class ServerCommunityData:
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

class ServerData:
    id: int
    nameId: int
    commentId: str
    language: str
    populationId: int
    gameTypeId: int
    communityId: int
    monoAccount: int
    illus: str

class ServerGameTypeData:
    id: int
    selectableByPlayer: int
    nameId: int
    rulesId: int
    descriptionId: int

class ServerGameTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ServerGameTypeData]
    references: ManagedReferencesRegistry

class ServerLangData:
    id: int
    nameId: int
    langCode: str

class ServerLangsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ServerLangData]
    references: ManagedReferencesRegistry

class ServerPopulationData:
    id: int
    nameId: int
    weight: int

class ServerPopulationsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ServerPopulationData]
    references: ManagedReferencesRegistry

class ServerSeasonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer
    references: ManagedReferencesRegistry

class ServersDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[ServerData]
    references: ManagedReferencesRegistry

class SignData:
    id: int
    skillParams: str
    skillId: int
    textKey: int
    skillVisibleCriterion: str

class SignsData:
    signs: list[SignData]

class SignsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SignsData]
    references: ManagedReferencesRegistry

class SkillData:
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

class SkillNameData:
    id: int
    nameId: int

class SkillNamesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SkillNameData]
    references: ManagedReferencesRegistry

class SkillsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SkillData]
    references: ManagedReferencesRegistry

class SkinMappingData:
    id: int
    lowDefId: int

class SkinMappingsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SkinMappingData]
    references: ManagedReferencesRegistry

class SkinSlotRuleData:
    skinId: int
    slotRulesList: list[SkinSlotsRulesInfoData]

class SkinSlotsRulesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SkinSlotRuleData]
    references: ManagedReferencesRegistry

class SkinSlotsRulesInfoData:
    slotRuleType: int
    slotRuleInfo: int
    slotsRules: list[SlotRuleData]

class SlotRuleData:
    id: int
    mask: int

class SmileyData:
    id: int
    order: int
    gfxId: str
    forPlayers: int
    referenceId: int
    categoryId: int

class SmileyPackData:
    id: int
    nameId: int
    order: int
    smileys: list[int]

class SmileyPacksDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SmileyPackData]
    references: ManagedReferencesRegistry

class SmileysDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SmileyData]
    references: ManagedReferencesRegistry

class SocialRightData:
    id: int
    nameId: int
    order: int
    groupId: int

class SoundAnimationData:
    eventNames: list[str]
    startFrames: list[str]
    guids: list[str]
    loopingEventNames: list[str]

class SoundBoneData:
    animSounds: SoundBonesDictionary

class SoundBonesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SoundBoneData]
    references: ManagedReferencesRegistry

class SoundBonesDictionary:
    m_keys: list[str]
    m_values: list[SoundAnimationData]

class SpeakingItemTextData:
    textId: int
    textProba: float
    textStringId: str
    textLevel: int
    textSound: int
    textRestriction: str

class SpeakingItemTriggerData:
    textIds: list[int]

class SpeakingItemsTextsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpeakingItemTextData]
    references: ManagedReferencesRegistry

class SpeakingItemsTriggersDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpeakingItemTriggerData]
    references: ManagedReferencesRegistry

class SpellBombData:
    id: int
    chainReactionSpellId: int
    explodSpellId: int
    wallId: int
    instantSpellId: int
    comboCoeff: int

class SpellBombsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpellBombData]
    references: ManagedReferencesRegistry

class SpellData:
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

class SpellLevelData:
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
    objectsById: MetadataDictionaryContainer[SpellLevelData]
    references: ManagedReferencesRegistry

class SpellPairData:
    id: int
    nameId: int
    descriptionId: int
    iconId: int

class SpellPairsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpellPairData]
    references: ManagedReferencesRegistry

class SpellScriptData:
    rawParams: str
    type: int

class SpellScriptsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpellScriptData]
    references: ManagedReferencesRegistry

class SpellStateData:
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
    objectsById: MetadataDictionaryContainer[SpellStateData]
    references: ManagedReferencesRegistry

class SpellTypeData:
    id: int
    longNameId: str
    shortNameId: str

class SpellTypesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpellTypeData]
    references: ManagedReferencesRegistry

class SpellVariantData:
    id: int
    breedId: int
    spellIds: list[int]

class SpellVariantsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SpellVariantData]
    references: ManagedReferencesRegistry

class SpellZoneDescr:
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
    objectsById: MetadataDictionaryContainer[SpellData]
    references: ManagedReferencesRegistry

class StealthBoneData:
    id: int

class StealthBonesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[StealthBoneData]
    references: ManagedReferencesRegistry

class SubAreaData:
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
    objectsById: MetadataDictionaryContainer[SubAreaData]
    references: ManagedReferencesRegistry

class SuperAreaData:
    id: int
    nameId: int
    worldmapId: int
    hasWorldMap: int

class SuperAreasDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[SuperAreaData]
    references: ManagedReferencesRegistry

class TaxCollectorFirstnameData:
    id: int
    firstnameId: str

class TaxCollectorFirstnamesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[TaxCollectorFirstnameData]
    references: ManagedReferencesRegistry

class TaxCollectorNameData:
    id: int
    nameId: int

class TaxCollectorNamesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[TaxCollectorNameData]
    references: ManagedReferencesRegistry

class TextIconReferenceData:
    referenceKey: str

class TextIconReferencesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[TextIconReferenceData]
    references: ManagedReferencesRegistry

class TitleCategoriesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[TitleCategoryData]
    references: ManagedReferencesRegistry

class TitleCategoryData:
    id: int
    nameId: int

class TitleData:
    id: int
    nameMaleId: str
    nameFemaleId: str
    visible: int
    categoryId: int

class TitlesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[TitleData]
    references: ManagedReferencesRegistry

class VeteranRewardData:
    id: int
    requiredSubDays: int
    itemGID: int
    itemQuantity: int

class VeteranRewardsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[VeteranRewardData]
    references: ManagedReferencesRegistry

class WaypointData:
    id: int
    mapId: int
    subAreaId: int
    activated: int

class WaypointsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WaypointData]
    references: ManagedReferencesRegistry

class WeaponData:
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
    possibleEffects: list[managedRefArrayItem[EffectInstanceData]]
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
    references: ManagedReferencesRegistry

class WorldEventData:
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

class WorldEventDungeonData:
    dungeonId: int
    dungeonMapIdTeleport: int
    scoreGroupShared: int
    scorePerDamage: int
    scorePerDungeon: int

class WorldEventFarmingSimulatorData:
    scorePerHarvest: int

class WorldEventMonstersHunterData:
    monsterList: list[int]
    criterion: str
    mapList: list[int]
    subareaList: list[int]
    areaList: list[int]
    scoreGroupShared: int
    scorePerDamage: int
    scorePerMonster: int

class WorldEventRewardData:
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

class WorldEventWorldBossesData:
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
    objectsById: MetadataDictionaryContainer[WorldEventData]
    references: ManagedReferencesRegistry

class WorldEventsDungeonsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WorldEventDungeonData]
    references: ManagedReferencesRegistry

class WorldEventsFarmingSimulatorDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WorldEventFarmingSimulatorData]
    references: ManagedReferencesRegistry

class WorldEventsMonstersHunterDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WorldEventMonstersHunterData]
    references: ManagedReferencesRegistry

class WorldEventsRewardsDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WorldEventRewardData]
    references: ManagedReferencesRegistry

class WorldEventsWorldBossesDataRoot(MonoBehaviour):
    objectsById: MetadataDictionaryContainer[WorldEventWorldBossesData]
    references: ManagedReferencesRegistry

class WorldMapData:
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
    objectsById: MetadataDictionaryContainer[WorldMapData]
    references: ManagedReferencesRegistry

class WrappedEffectInstanceList:
    values: list[managedRefArrayItem[EffectInstanceData]]

class WrappedFloatList:
    values: list[float]

class WrappedIntList:
    values: list[int]

class WrappedUintList:
    values: list[int]

class int2_storage:
    x: int
    y: int

class managedRefArrayItem[T]:
    rid: int

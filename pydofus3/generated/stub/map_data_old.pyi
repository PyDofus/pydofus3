from UnityPy.classes.PPtr import PPtr
from UnityPy.classes.generated import MonoBehaviour
from typing import Union
from UnityPy.classes.generated import Material, ParticleSystem, Texture2D

class Ale2ConstantsOrCurves:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class Ale2ConstantsOrCurvesHideMode:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleAlphaKey:
    alpha: float
    time: float

class AleAnimationCurve:
    keys: list[AleKeyframe]

class AleBurst:
    time: float
    count: AleMinMaxCurve
    cycleCount: int
    repeatInterval: float
    probability: float

class AleColor:
    value: int

class AleColorKey:
    color: AleColor
    time: float

class AleConstantOr2Constants:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleConstantOrCurve:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleCurve:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleCurveHideMode:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleGradient:
    colorKeys: list[AleColorKey]
    alphaKeys: list[AleAlphaKey]

class AleGradients:
    colorMin: AleColor
    colorMax: AleColor
    gradientMin: AleGradient
    gradientMax: AleGradient
    mode: int

class AleKeyframe:
    inTangent: float
    inWeight: float
    outTangent: float
    outWeight: float
    time: float
    value: float
    weightedMode: int

class AleMatrix4x4:
    column0: AleVector4
    column1: AleVector4
    column2: AleVector4
    column3: AleVector4

class AleMinMaxCurve:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleMinMaxCurveHideMode:
    constantMin: float
    constantMax: float
    curveMin: AleAnimationCurve
    curveMax: AleAnimationCurve
    mode: int

class AleMinMaxGradient:
    colorMin: AleColor
    colorMax: AleColor
    gradientMin: AleGradient
    gradientMax: AleGradient
    mode: int

class AleParticleSystemNoiseQuality:
    noiseQuality: int

class AleParticleSystemRenderMode:
    renderMode: int

class AleParticleSystemRenderSpace:
    renderSpace: int

class AleParticleSystemShapeMultiModeValue:
    multiModeValue: int

class AleParticleSystemShapeType:
    shapeType: int

class AleParticleSystemSortMode:
    sortMode: int

class AleParticleSystemTrailTextureMode:
    textureMode: int

class AleRect:
    x: float
    y: float
    width: float
    height: float

class AleVector2:
    x: float
    y: float

class AleVector2Int:
    x: int
    y: int

class AleVector3:
    x: float
    y: float
    z: float

class AleVector4:
    x: float
    y: float
    z: float
    w: float

class AnimatedElement:
    m_id: int
    m_type: int
    m_entityLook: str
    m_horizontalSymmetry: int
    m_playAnimation: int
    m_playAnimStatic: int
    m_minDelay: int
    m_maxDelay: int

class AtlasDictionary:
    m_keys: list[int]
    m_values: list[AleRect]

class ClientAnimatedElementTransform:
    gfxId: int
    cellId: int
    playAnimation: int
    playAnimStatic: int
    playerGuildCustomisable: int
    isStagingTarget: int
    stagingId: str
    minDelay: int
    maxDelay: int
    requiresServerUpdate: int
    transform: Transform2D
    type: int
    color: AleColor
    innerCellRenderOrder: int
    displayBehaviour: int

class ClientCellData:
    cellNumber: int
    speed: int
    mapChangeData: int
    moveZone: int
    linkedZone: int
    mov: int
    los: int
    nonWalkableDuringFight: int
    nonWalkableDuringRP: int
    farmCell: int
    visible: int
    havenbagCell: int
    roleplayMonstersMovementBlocked: int
    floor: int
    red: int
    blue: int
    arrow: int

class ClientElementTransform:
    gfxId: int
    color: AleColor
    transform: Transform2D
    materialIndex: int
    displayBehaviour: int

class ClientInteractiveAnimatedElementTransform:
    gfxId: int
    cellId: int
    playAnimation: int
    playAnimStatic: int
    playerGuildCustomisable: int
    isStagingTarget: int
    stagingId: str
    minDelay: int
    maxDelay: int
    requiresServerUpdate: int
    transform: Transform2D
    type: int
    color: AleColor
    innerCellRenderOrder: int
    displayBehaviour: int
    m_interactionId: int
    shaderOutlineParameters: managedReference[ShaderOutlineParameters]
    references: ManagedReferencesRegistry

class ClientInteractiveElementTransform:
    gfxId: int
    color: AleColor
    transform: Transform2D
    materialIndex: int
    displayBehaviour: int
    cellId: int
    innerCellRenderOrder: int
    m_interactionId: int
    shaderOutlineParameters: managedReference[ShaderOutlineParameters]

class ClientMapData:
    topNeighbourId: int
    bottomNeighbourId: int
    leftNeighbourId: int
    rightNeighbourId: int
    backgroundColor: AleColor
    playlistSet: PlaylistSet
    backgroundElements: list[ClientElementTransform]
    sortableElements: list[ClientSortableElementTransform]
    foregroundElements: list[ClientElementTransform]
    animatedElements: list[ClientAnimatedElementTransform]
    refractionElements: list[ClientElementTransform]
    interactiveElements: list[managedRefArrayItem[Union[ClientInteractiveAnimatedElementTransform| ClientInteractiveElementTransform]]]
    boundingBoxes: list[ClientInteractiveElementTransform]
    particlesParameters: list[ClientParticlesParameters]
    foregroundMaterialData: MaterialData
    backgroundMaterialData: MaterialData
    sortableMaterialData: MaterialData
    cellsData: list[ClientCellData]
    topArrowCellList: list[int]
    leftArrowCellList: list[int]
    bottomArrowCellList: list[int]
    rightArrowCellList: list[int]
    mapWindConfiguration: managedReference[MapWindConfiguration]
    mapPostProcessConfiguration: managedReference[MapPostProcessConfiguration]
    mapWaveConfiguration: managedReference[MapWaveConfiguration]
    mapNoiseModifierConfiguration: managedReference[MapNoiseModifierConfiguration]
    stagingSequences: list[managedRefArrayItem[StagingSequence]]
    localizedSounds: list[LocalizedSound]

class ClientParticlesParameters:
    id: str
    materialIndex: int
    trailMaterialIndex: int
    transform: TransformParameters
    layer: int
    cellId: int
    renderOrder: int
    isStagingTarget: int
    stagingId: str
    particlesMainParameters: ParticlesMainParameters
    particlesModulesParameters: ParticlesModulesParameters
    particlesEmissionParameters: ParticlesEmissionParameters
    particlesShapeParameters: ParticlesShapeParameters
    particlesVelocityOverLifetimeParameters: ParticlesVelocityOverLifetimeParameters
    particlesColorOverLifetimeParameters: ParticlesColorOverLifetimeParameters
    particlesSizeOverLifetimeParameters: ParticlesSizeOverLifetimeParameters
    particlesRotationOverLifetimeParameters: ParticlesRotationOverLifetimeParameters
    particlesNoiseParameters: ParticlesNoiseParameters
    particleSpritesheetParameters: ParticleSpritesheetParameters
    particlesTrailsParameters: ParticlesTrailsParameters
    particlesRendererParameters: ParticlesRendererParameters
    particlesSubEmittersParameters: ParticlesSubEmittersParameters
    soundParameters: ParticlesSoundParameters

class ClientSortableElementTransform:
    gfxId: int
    color: AleColor
    transform: Transform2D
    materialIndex: int
    displayBehaviour: int
    cellId: int
    innerCellRenderOrder: int

class ColorAnimationStagingEffect:
    material: PPtr[Material]
    finalColor: StagingEvolutiveVar
    alpha: StagingEvolutiveVar
    frequency: StagingEvolutiveVar
    resetTime: int
    noiseOffset: StagingEvolutiveVar
    noiseStrength: StagingEvolutiveVar
    noiseSpeed: StagingEvolutiveVar
    shouldSmooth: int

class DissolveStagingEffect:
    material: PPtr[Material]
    dissolveTexTiling: StagingEvolutiveVar
    dissolveTexOffset: StagingEvolutiveVar
    dissolveTexSpeedVector: StagingEvolutiveVar
    alphaClip: StagingEvolutiveVar
    alphaClipFadeWidth: StagingEvolutiveVar
    burnWidth: StagingEvolutiveVar
    burnColor: StagingEvolutiveVar
    burnColorPower: StagingEvolutiveVar

class DistortionStagingEffect:
    material: PPtr[Material]
    noiseTexTiling: StagingEvolutiveVar
    noiseTexOffset: StagingEvolutiveVar
    uvMode: int
    distortionVector: StagingEvolutiveVar

class ElementAtlas:
    width: int
    height: int
    idsToRects: AtlasDictionary

class EmissiveStagingEffect:
    material: PPtr[Material]
    factor: StagingEvolutiveVar

class FmodParameterValue:
    name: str
    value: float

class GfxElement:
    m_id: int
    m_type: int
    m_gfxId: int
    m_height: int
    m_horizontalSymmetry: int
    m_origin: AleVector2Int
    m_size: AleVector2Int

class LocalizedSound:
    audioEvent: str
    position: AleVector2

class ManagedReferencesRegistry:
    version: int
    RefIds: list[ReferencedObject]

class MapElementsDictionary:
    m_keys: list[int]
    m_values: list[managedRefArrayItem[Union[AnimatedElement| GfxElement]]]

class MapElementsMetadata(MonoBehaviour):
    m_elementsMap: MapElementsDictionary
    references: ManagedReferencesRegistry

class MapMetadata(MonoBehaviour):
    mapData: ClientMapData
    mapTextures: list[PPtr[Texture2D]]
    allowMapEffects: int
    references: ManagedReferencesRegistry

class MapNoiseModifierConfiguration:
    noiseModifierParameters: NoiseModifierParameters

class MapPostProcessConfiguration:
    postProcessParameters: list[managedRefArrayItem[Union[PPBloomParameters| PPChromaticAberrationParameters| PPFilmGrainParameters]]]
    references: ManagedReferencesRegistry

class MapWaveConfiguration:
    waveParameters: WaveParameters

class MapWindConfiguration:
    windParameters: WindParameters

class MaterialData:
    atlas1x: ElementAtlas
    atlas2x: ElementAtlas
    atlas4x: ElementAtlas
    shaderData: list[managedRefArrayItem[ShaderData]]

class NoAnimAlphaStagingEffect:
    material: PPtr[Material]
    effectDisplay: int
    alpha: StagingEvolutiveVar
    color: StagingEvolutiveVar

class NoiseModifierParameters:
    mapNoiseModifierTexId: int
    mapNoiseModifierTiling: AleVector2
    mapNoiseModifierOffset: AleVector2
    mapNoiseModifierSpeed: AleVector2

class PPBloomParameters:
    threshold: float
    intensity: float
    scatter: float
    color: AleColor

class PPChromaticAberrationParameters:
    intensity: float

class PPFilmGrainParameters:
    type: int
    intensity: float
    response: float

class PaintShaderData:
    shaderParameters: list[managedRefArrayItem[Union[ShaderBlendingParameters| ShaderColorAnimationParameters| ShaderCustomFramerateParameters| ShaderDepthAlphaClipParameters| ShaderDissolveParameters| ShaderDistortionParameters| ShaderEmissiveParameters| ShaderRefractionParameters| ShaderRotationParameters| ShaderScaleParameters| ShaderTextureOffsetParameters| ShaderTranslationParameters| ShaderWaveParameters| ShaderWindParameters]]]
    gfxId: int
    unique: int
    isStagingTarget: int
    stagingId: str
    paintSpanOrder: int
    background: int
    references: ManagedReferencesRegistry

class ParticleEmissionBurstStagingParameters:
    burstIndex: int
    time: StagingEvolutiveVar
    count: StagingEvolutiveVar
    cycles: StagingEvolutiveVar
    interval: StagingEvolutiveVar
    probability: StagingEvolutiveVar

class ParticleEmissionStagingEffect:
    particlesSystem: PPtr[ParticleSystem]
    rateOverTime: StagingEvolutiveVar
    bursts: list[ParticleEmissionBurstStagingParameters]

class ParticleMainStagingEffect:
    particlesSystem: PPtr[ParticleSystem]
    startColor: StagingEvolutiveVar

class ParticleSpritesheetParameters:
    tiles: AleVector2Int
    frameOverTime: AleMinMaxCurve
    startFrame: AleConstantOr2Constants
    cycles: int

class ParticlesColorOverLifetimeParameters:
    colorOverLifetimeColor: AleGradients

class ParticlesEmissionParameters:
    rateOverTime: AleMinMaxCurve
    bursts: list[AleBurst]

class ParticlesMainParameters:
    duration: float
    looping: int
    prewarm: int
    startDelay: AleConstantOr2Constants
    startLifetime: AleMinMaxCurve
    startSpeed: AleMinMaxCurve
    is3DStartSize: int
    startSize3DMode: int
    startSize: AleMinMaxCurve
    startSizeX: AleMinMaxCurveHideMode
    startSizeY: AleMinMaxCurveHideMode
    startSizeZ: AleMinMaxCurveHideMode
    is3DStartRotation: int
    startRotation3DMode: int
    startRotation: AleMinMaxCurve
    startRotationX: AleMinMaxCurveHideMode
    startRotationY: AleMinMaxCurveHideMode
    startRotationZ: AleMinMaxCurveHideMode
    flipRotation: float
    startColor: AleMinMaxGradient
    gravityModifier: AleMinMaxCurve
    simulationSpace: int
    simulationSpeed: float
    useAutoRandomSeed: int
    randomSeed: int
    stopped: int

class ParticlesModulesParameters:
    isEmissionModuleActivated: int
    isShapeModuleActivated: int
    isVelocityOverLifetimeModuleActivated: int
    isColorOverLifetimeModuleActivated: int
    isSizeOverLifetimeModuleActivated: int
    isRotationOverLifetimeModuleActivated: int
    isNoiseModuleActivated: int
    isSpritesheetModuleActivated: int
    isTrailsModuleActivated: int
    isRendererModuleActivated: int
    isSubemitterModuleActivated: int
    isSoundModuleActivated: int

class ParticlesNoiseParameters:
    isNoiseStrengthSeparateAxes: int
    noiseStrength3DMode: int
    noiseStrength: AleMinMaxCurve
    noiseStrengthX: AleMinMaxCurveHideMode
    noiseStrengthY: AleMinMaxCurveHideMode
    noiseStrengthZ: AleMinMaxCurveHideMode
    noiseFrequency: float
    noiseScrollSpeed: AleConstantOrCurve
    noiseDamping: int
    noiseQuality: AleParticleSystemNoiseQuality
    noiseRemapEnabled: int
    noiseRemap3DMode: int
    noiseRemapCurve: AleCurve
    noiseRemapCurveX: AleCurveHideMode
    noiseRemapCurveY: AleCurveHideMode
    noiseRemapCurveZ: AleCurveHideMode
    noisePositionAmount: AleMinMaxCurve
    noiseRotationAmount: AleMinMaxCurve
    noiseSizeAmount: AleMinMaxCurve

class ParticlesPlayStagingEffect:
    particlesSystem: PPtr[ParticleSystem]

class ParticlesRendererParameters:
    renderMode: AleParticleSystemRenderMode
    cameraVelocityScale: float
    velocityScale: float
    lengthScale: float
    freeformStretching: int
    rotateWithStretchDirection: int
    sortMode: AleParticleSystemSortMode
    sortingFudge: float
    minParticleSize: float
    maxParticleSize: float
    renderAlignment: AleParticleSystemRenderSpace
    flip: AleVector3
    allowRoll: int
    pivot: AleVector3

class ParticlesRotationOverLifetimeParameters:
    isRotationOverLifetimeSeparateAxes: int
    rotationOverLifetime3DMode: int
    angularVelocity: AleMinMaxCurve
    angularVelocityX: AleMinMaxCurveHideMode
    angularVelocityY: AleMinMaxCurveHideMode
    angularVelocityZ: AleMinMaxCurveHideMode

class ParticlesShaderData:
    shaderParameters: list[managedRefArrayItem[Union[ShaderBlendingParameters| ShaderColorAnimationParameters| ShaderCustomFramerateParameters| ShaderDepthAlphaClipParameters| ShaderDissolveParameters| ShaderDistortionParameters| ShaderEmissiveParameters| ShaderRefractionParameters| ShaderRotationParameters| ShaderScaleParameters| ShaderTextureOffsetParameters| ShaderTranslationParameters| ShaderWaveParameters| ShaderWindParameters]]]
    gfxId: int
    unique: int
    isStagingTarget: int
    stagingId: str
    references: ManagedReferencesRegistry

class ParticlesShapeParameters:
    particleSystemShape: AleParticleSystemShapeType
    angle: float
    radius: float
    donutRadius: float
    radiusThickness: float
    arc: float
    arcMode: AleParticleSystemShapeMultiModeValue
    arcSpread: float
    arcSpeed: AleConstantOrCurve
    length: float
    emitFromCone: int
    emitFromBox: int
    boxThickness: AleVector3
    shapePosition: AleVector3
    shapeRotation: AleVector3
    shapeScale: AleVector3
    alignToDirection: int
    randomDirectionAmount: float
    sphericalDirectionAmount: float
    randomPositionAmount: float

class ParticlesSizeOverLifetimeParameters:
    isSizeOverLifetimeSeparateAxes: int
    sizeOverLifetime3DMode: int
    sizeOverLifetimeSize: Ale2ConstantsOrCurves
    sizeOverLifetimeSizeX: Ale2ConstantsOrCurvesHideMode
    sizeOverLifetimeSizeY: Ale2ConstantsOrCurvesHideMode
    sizeOverLifetimeSizeZ: Ale2ConstantsOrCurvesHideMode

class ParticlesSoundParameters:
    maxParticles: int
    spawnFmodEvent: str
    deathFmodEvent: str

class ParticlesStopStagingEffect:
    particlesSystem: PPtr[ParticleSystem]
    clear: int

class ParticlesSubEmittersParameters:
    parentId: str
    type: int
    properties: int
    emitProbability: float

class ParticlesTrailsParameters:
    trailsRatio: float
    trailsLifetime: AleMinMaxCurve
    trailsMinVertexDistance: float
    trailsWorldSpace: int
    trailsDieWithParticles: int
    trailsTextureMode: AleParticleSystemTrailTextureMode
    trailsSizeAffectsWidth: int
    trailsSizeAffectsLifetime: int
    trailsInheritParticleColor: int
    trailsColorOverLifetime: AleMinMaxGradient
    trailsWidthOverTrail: AleMinMaxCurve
    trailsColorOverTrail: AleMinMaxGradient

class ParticlesVelocityOverLifetimeParameters:
    linearVelocityMode: int
    linearX: AleMinMaxCurveHideMode
    linearY: AleMinMaxCurveHideMode
    linearZ: AleMinMaxCurveHideMode
    systemSimulationSimulationSpaceRestricted: int
    orbitalVelocityMode: int
    orbitalX: AleMinMaxCurveHideMode
    orbitalY: AleMinMaxCurveHideMode
    orbitalZ: AleMinMaxCurveHideMode
    offsetVelocityMode: int
    orbitalOffsetX: AleMinMaxCurveHideMode
    orbitalOffsetY: AleMinMaxCurveHideMode
    orbitalOffsetZ: AleMinMaxCurveHideMode
    radial: AleMinMaxCurve
    speedModifier: AleMinMaxCurve

class PlayFmodEventStagingEffect:
    fmodEvent: str
    xPosition: AleConstantOrCurve
    yPosition: AleConstantOrCurve

class Playlist:
    fmodEventGuid: str

class PlaylistSet:
    musicPlaylist: Playlist
    ambiantPlaylist: Playlist
    bossFightPlaylist: Playlist
    snapshot: str
    fmodParameterValues: list[FmodParameterValue]

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

class RotationStagingEffect:
    material: PPtr[Material]
    rotationCenterVector: StagingEvolutiveVar
    frequency: StagingEvolutiveVar
    resetTime: int
    amplitude: StagingEvolutiveVar
    offset: StagingEvolutiveVar
    noiseStrength: StagingEvolutiveVar
    noiseSpeed: StagingEvolutiveVar
    noiseOffset: StagingEvolutiveVar

class ScaleStagingEffect:
    material: PPtr[Material]
    axesVector: StagingEvolutiveVar
    pivotVector: StagingEvolutiveVar
    frequency: StagingEvolutiveVar
    resetTime: int
    amplitude: StagingEvolutiveVar
    offset: StagingEvolutiveVar
    noiseStrengthVector: StagingEvolutiveVar
    noiseOffsetVector: StagingEvolutiveVar

class SequenceEventStagingEffect:
    stagingEventType: int

class SetFmodParamStagingEffect:
    paramName: str
    startValue: float
    endValue: StagingEvolutiveVar

class ShaderBlendingParameters:
    sourceFactor: int
    blendOperation: int
    destinationFactor: int

class ShaderColorAnimationParameters:
    animationCurveType: int
    finalColor: AleColor
    isFinalColorLinkedToMapNoiseModifier: int
    finalColorModifier: AleColor
    frequency: float
    linkFrequencyToWind: int
    timeOffset: float
    isTimeOffsetRandom: int
    shouldSmooth: int
    shouldApplyNoise: int
    noiseTexID: int
    noiseOffset: AleVector2
    isNoiseOffsetRandom: int
    noiseStrength: float
    linkNoiseStrengthToWind: int
    noiseSpeed: float
    linkNoiseSpeedToWind: int

class ShaderCustomFramerateParameters:
    framerate: float

class ShaderData:
    shaderParameters: list[managedRefArrayItem[Union[ShaderBlendingParameters| ShaderColorAnimationParameters| ShaderCustomFramerateParameters| ShaderDepthAlphaClipParameters| ShaderDissolveParameters| ShaderDistortionParameters| ShaderEmissiveParameters| ShaderRefractionParameters| ShaderRotationParameters| ShaderScaleParameters| ShaderTextureOffsetParameters| ShaderTranslationParameters| ShaderWaveParameters| ShaderWindParameters]]]
    gfxId: int
    unique: int
    isStagingTarget: int
    stagingId: str
    references: ManagedReferencesRegistry

class ShaderDepthAlphaClipParameters:
    alphaClip: float

class ShaderDissolveParameters:
    dissolveTexID: int
    dissolveTexTiling: AleVector2
    dissolveTexOffset: AleVector2
    isDissolveTexOffsetRandom: int
    dissolveTexSpeed: AleVector2
    texSpeedMultiplier: float
    isTexSpeedMultiplierRandom: int
    texSpeedMultiplierRandomRatio: float
    dissolveMaskID: int
    alphaClip: float
    alphaClipFadeWidth: float
    burnWidth: float
    isBurnWidthLinkedToMapNoiseModifier: int
    burnColor: AleColor
    isBurnColorLinkedToMapNoiseModifier: int
    burnColorModifier: AleColor
    burnColorPower: float
    isBurnColorPowerLinkedToMapNoiseModifier: int
    isBurnFaded: int
    displayUseDissolvePerParticle: int
    useDissolvePerParticle: int
    alphaClipPerParticle: AleMinMaxCurve
    isAnimated: int
    animationCurveType: int
    frequency: float
    curveMin: float
    curveMax: float
    shouldSmooth: int
    shouldApplyNoise: int
    noiseTexID: int
    noiseStrength: float
    noiseSpeed: float

class ShaderDistortionParameters:
    noiseTexID: int
    noiseTexUVMode: int
    noiseTexTiling: AleVector2
    tile: float
    noiseTexOffset: AleVector2
    isDistortionNoiseTexOffsetRandom: int
    direction: AleVector2
    directionSpeedMultiplier: float
    isDirectionSpeedMultiplierRandom: int
    directionSpeedMultiplierRandomRatio: float
    strength: float
    distortionDirection: AleVector2
    linkToWind: int
    maskTexID: int

class ShaderEmissiveParameters:
    emissiveTexID: int
    color: AleColor
    factor: float
    isFactorLinkedToMapNoiseModifier: int
    isAnimated: int
    displayUseEmissiveAnimationPerParticle: int
    useEmissiveAnimationPerParticle: int
    animationOffsetPerParticle: AleMinMaxCurve
    frequency: float
    timeOffset: float
    isTimeOffsetRandom: int
    curveMin: float
    curveMax: float
    curveClampMin: float
    curveClampMax: float
    isFrequencyNoised: int
    frequencyNoiseTexID: int
    noiseStrength: float
    noiseSpeed: float
    areAreasDelayed: int

class ShaderOutlineParameters:
    type: int
    testDiff: int
    alphaClip: float
    color: AleColor

class ShaderRefractionParameters:
    noiseTexID: int
    noiseTexUVMode: int
    noiseTexTiling: AleVector2
    tile: float
    noiseTexOffset: AleVector2
    direction: AleVector2
    directionSpeedMultiplier: float
    isDirectionSpeedMultiplierRandom: int
    directionSpeedMultiplierRandomRatio: float
    strength: float
    maskTexID: int
    color: AleColor

class ShaderRotationParameters:
    animationCurveType: int
    rotationCenter: AleVector2
    frequency: float
    linkFrequencyToWind: int
    amplitude: float
    linkAmplitudeToWind: int
    offset: float
    isOffsetLinkedToMapNoiseModifier: int
    timeOffset: float
    isTimeOffsetRandom: int
    shouldSmooth: int
    shouldApplyNoise: int
    noiseTexID: int
    noiseStrength: float
    linkNoiseStrengthToWind: int
    noiseSpeed: float
    linkNoiseSpeedToWind: int
    noiseOffset: AleVector2
    isNoiseOffsetRandom: int

class ShaderScaleParameters:
    animationCurveType: int
    axes: AleVector2
    pivot: AleVector2
    frequency: float
    linkFrequencyToWind: int
    amplitude: float
    linkAmplitudeToWind: int
    offset: float
    timeOffset: float
    isTimeOffsetRandom: int
    shouldSmooth: int
    shouldApplyNoise: int
    noiseTexID: int
    noiseStrength: AleVector2
    noiseStrengthMultiplier: float
    linkNoiseStrengthToWind: int
    noiseOffset: AleVector2
    noiseSpeed: float
    linkNoiseSpeedToWind: int

class ShaderTextureOffsetParameters:
    textureOffsetType: int
    texUVMode: int
    texTiling: AleVector2
    tile: float
    texOffset: AleVector2
    direction: AleVector2
    directionSpeed: float
    flowmapID: int
    flowmapSpeed: float
    flowmapPower: float

class ShaderTranslationParameters:
    animationCurveType: int
    direction: AleVector2
    frequency: float
    linkFrequencyToWind: int
    amplitude: float
    linkAmplitudeToWind: int
    offset: float
    timeOffset: float
    isTimeOffsetRandom: int
    shouldSmooth: int
    shouldApplyNoise: int
    noiseTexID: int
    noiseStrength: AleVector2
    noiseStrengthMultiplier: float
    linkNoiseStrengthToWind: int
    noiseSpeed: float
    linkNoiseSpeedToWind: int
    noiseOffset: AleVector2
    isNoiseOffsetRandom: int

class ShaderWaveParameters:
    waveTexID: int

class ShaderWindParameters:
    isWindSensitive: int
    bendCenter: AleVector2
    worldSpaceBendCenter: AleVector4
    bendStart: AleVector2
    worldSpaceBendStart: AleVector4
    bendAxe: AleVector2
    bendAxeMultiplier: float
    flexibility: float
    shouldSwing: int
    windSwingNoiseSpeedCoef: float
    windSwingNoiseAmplitude: float
    parentParameters: list[ShaderWindParentParameters]

class ShaderWindParentParameters:
    bendCenter: AleVector2
    bendStart: AleVector2
    bendAxe: AleVector2
    bendAxeMultiplier: float
    flexibility: float
    shouldSwing: int
    windSwingNoiseSpeedCoef: float
    windSwingNoiseAmplitude: float

class ShowMapAnimatedElementStagingEffect:
    show: int

class StagingEffectsPack:
    targets: list[str]
    stagingEffects: list[managedRefArrayItem[Union[PlayFmodEventStagingEffect| SequenceEventStagingEffect| SetFmodParamStagingEffect| StopLocalizedFmodEventsStagingEffect| ColorAnimationStagingEffect| DissolveStagingEffect| DistortionStagingEffect| EmissiveStagingEffect| NoAnimAlphaStagingEffect| RotationStagingEffect| ScaleStagingEffect| TranslationStagingEffect| ParticleEmissionStagingEffect| ParticleMainStagingEffect| ParticlesPlayStagingEffect| ParticlesStopStagingEffect]]]

class StagingEvolutiveVar:
    active: int
    startValue: float
    maxValue: float

class StagingSequence:
    id: str
    uniqueId: int
    exclusiveGroupId: str
    exclusivityResolveMethod: int
    stagingShots: list[StagingShot]
    references: ManagedReferencesRegistry

class StagingShot:
    id: str
    previousShot: str
    delay: float
    duration: float
    intensityMultiplierSensitivity: float
    skipIfInstant: int
    intensityCurve: AleAnimationCurve
    stagingEffectsPacks: list[StagingEffectsPack]

class StopLocalizedFmodEventsStagingEffect:
    fmodEvent: str

class Transform2D:
    m11: float
    m12: float
    m21: float
    m22: float
    m31: float
    m32: float

class TransformParameters:
    pos: AleVector3
    rot: AleVector3
    scale: AleVector3

class TranslationStagingEffect:
    material: PPtr[Material]
    directionVector: StagingEvolutiveVar
    frequency: StagingEvolutiveVar
    resetTime: int
    amplitude: StagingEvolutiveVar
    offset: StagingEvolutiveVar
    noiseStrenghVector: StagingEvolutiveVar
    noiseSpeedVector: StagingEvolutiveVar
    noiseOffset: StagingEvolutiveVar

class WaveParameters:
    waveFrequency: float
    waveDirection: AleVector2
    waveDynamicsTexID: int
    waveDissolveDynamicsTexID: int
    waveDistoTexID: int
    waveDistoTexTiling: AleVector2
    waveDistoTexOffset: AleVector2
    waveDistoTexSpeed: AleVector2
    waveDistoPower: float
    waveDistoSpeedStopMin1: float
    waveDistoSpeedStopMax1: float
    waveDistoSpeedStopMin2: float
    waveDistoSpeedStopMax2: float
    waveDistoSpeedStopMin3: float
    waveDistoSpeedStopMax3: float
    waveDistoSpeedStopMin4: float
    waveDistoSpeedStopMax4: float
    waveDissolveTexID1: int
    waveDissolveTexTiling1: AleVector2
    waveDissolveTexOffset1: AleVector2
    waveDissolveTexSpeed1: AleVector2
    waveDissolvePower1: float
    waveDissolveFadeDistance: float
    waveDissolveTexID2: int
    waveDissolveTexTiling2: AleVector2
    waveDissolveTexOffset2: AleVector2
    waveDissolveTexSpeed2: AleVector2
    waveDissolvePower2: float
    waveDissolveShouldFade2: int
    waveDissolveFadeStartRatio2: float
    waveDissolveFadeDistanceRatio2: float
    waveDissolveTexID3: int
    waveDissolveTexTiling3: AleVector2
    waveDissolveTexOffset3: AleVector2
    waveDissolveTexSpeed3: AleVector2
    waveDissolvePower3: float
    waveDissolveShouldFade3: int
    waveDissolveFadeStartRatio3: float
    waveDissolveFadeDistanceRatio3: float
    waveDissolveTexID4: int
    waveDissolveTexTiling4: AleVector2
    waveDissolveTexOffset4: AleVector2
    waveDissolveTexSpeed4: AleVector2
    waveDissolvePower4: float
    waveDissolveShouldFade4: int
    waveDissolveFadeStartRatio4: float
    waveDissolveFadeDistanceRatio4: float
    globalWaveMasksTexCamMatrix: AleMatrix4x4
    waterColor1: AleColor
    waterColor1Dissolved: AleColor
    waterColor2: AleColor
    waterColor2Dissolved: AleColor
    waterColor3: AleColor
    waterColor3Dissolved: AleColor
    waterColor4: AleColor
    waterColor4Dissolved: AleColor

class WindParameters:
    windPower: float
    windModelTexID: int
    mainWindNoiseTexID: int
    mainWindNoiseTiling: AleVector2
    mainWindNoiseTilingMultiplier: float
    mainWindNoiseDirection: AleVector2
    mainWindNoiseDirectionMultiplier: float
    mainWindAmplitudeMultiplierCursor: float
    mainWindAmplitudeCurvePower: float
    mainWindFrequencyCurvePower: float
    swingNoiseTexID: int
    swingNoiseTiling: AleVector2
    swingNoiseTilingMultiplier: float
    swingNoiseDirection: AleVector2
    swingNoiseDirectionMultiplier: float
    swingAmplitudeMultiplierCursor: float
    swingAmplitudeCurvePower: float
    swingFrequencyCurvePower: float
    mainWindAmplitudeMultiplier: float
    mainWindFrequencyMultiplier: float
    swingFrequencyMultiplier: float
    swingAmplitudeMultiplier: float
    minimumSwingAmplitude: float
    windSwingNoiseSpeed: AleVector2

class managedRefArrayItem[T]:
    rid: int

class managedReference[T]:
    rid: int

from enum import IntFlag

# Core.UILogic.Components.Figma.AssetToggleLine
class AssetToggleLine(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.AssetToggleLine
class AssetToggleLine(IntFlag):
    Left = 0
    Right = 1
    Both = 2
    NONE = 3

# Core.UILogic.Components.Figma.BasicTooltipHeader
class BasicTooltipHeader(IntFlag):
    titleTag = 0
    titleSubtitle = 1
    title = 2
    titleTagLine = 3

# Core.UILogic.Components.Figma.ChallengeIcon
class ChallengeIcon(IntFlag):
    regular = 0
    success = 1

# Core.UILogic.Components.Figma.ChallengeIcon
class ChallengeIcon(IntFlag):
    none = 0
    completed = 1
    failed = 2

# Core.UILogic.Components.Figma.CheckboxCustom
class CheckboxCustom(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.CircularGauge
class CircularGauge(IntFlag):
    none = 0
    primary = 1
    green = 2
    red = 3
    orange = 4
    grey = 5
    purple = 6
    white = 7

# Core.UILogic.Components.Figma.CurrencyType
class CurrencyType(IntFlag):
    Nugget = 0
    Kamas = 1
    Ogrine = 2
    DreamPoint = 3
    Item = 4
    GuildKamas = 5

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    none = 0
    primary = 1
    secondary = 2
    tertiary = 3
    link = 4
    floating = 5

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    none = 0
    normal = 1
    negative = 2
    strong = 3
    light = 4
    dark = 5

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    text = 1
    icon = 2
    asset = 4
    textIcon = 3
    textAsset = 5

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    Left = 0
    Right = 1
    Both = 2

# Core.UILogic.Components.Figma.DofusButtonCustom
class DofusButtonCustom(IntFlag):
    Icon = 0
    Image = 1

# Core.UILogic.Components.Figma.DofusTab
class DofusTab(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.DofusTab
class DofusTab(IntFlag):
    normal = 0
    fullCaps = 1

# Core.UILogic.Components.Figma.DofusTab
class DofusTab(IntFlag):
    text = 0
    asset = 1

# Core.UILogic.Components.Figma.DofusToggleButtonCustom
class DofusToggleButtonCustom(IntFlag):
    none = 0
    primary = 1
    secondary = 2

# Core.UILogic.Components.Figma.DofusToggleButtonCustom
class DofusToggleButtonCustom(IntFlag):
    text = 1
    icon = 2
    asset = 4
    textIcon = 3
    textAsset = 5

# Core.UILogic.Components.Figma.DofusToggleButtonCustom
class DofusToggleButtonCustom(IntFlag):
    Icon = 0
    Image = 1

# Core.UILogic.Components.Figma.DofusToggleButtonCustom
class DofusToggleButtonCustom(IntFlag):
    normal = 0
    blue = 1
    green = 2

# Core.UILogic.Components.Figma.DofusToggleButtonCustom
class DofusToggleButtonCustom(IntFlag):
    small = 0
    medium = 1
    large = 2
    xLarge = 3
    xxLarge = 4

# Core.UILogic.Components.Figma.Dropdown
class Dropdown(IntFlag):
    small = 0
    medium = 1

# Core.UILogic.Components.Figma.Dropdown
class Dropdown(IntFlag):
    text = 0
    icon = 1

# Core.UILogic.Components.Figma.FigmaIcons
class FigmaIcons(IntFlag):
    none = 0
    addCharacter = 1
    alliance = 2
    allianceBanner = 3
    almanax = 4
    alteration = 5
    amulet = 6
    ankama = 7
    anomaly = 8
    archimonster = 9
    areaBoomerang = 10
    areaCircle = 11
    areaCone = 12
    areaCross = 13
    areaCrossWithoutCenter = 14
    areaDiagonalCross = 15
    areaDiagonalCrossWithoutCenter = 16
    areaDiagonalLine = 17
    areaFork = 18
    areaHalfCircle = 19
    areaLine = 20
    areaLineFromCaster = 21
    areaPerpendicularDiagonalLine = 22
    areaPerpendicularLine = 23
    areaRectangle = 24
    areaRing = 25
    areaSquare = 26
    areaSquareWithoutDiagonal = 27
    areaStar = 28
    armor = 29
    arrowAngle = 30
    arrowBigBottom = 31
    arrowBigBottomLeft = 32
    arrowBigBottomRight = 33
    arrowBigLeft = 34
    arrowBigRight = 35
    arrowBigTopLeft = 36
    arrowBigTopRight = 37
    arrowBigUp = 38
    arrowBottom = 39
    arrowBottomDoubleLine = 40
    arrowBottomLine = 41
    arrowDoubleTop = 42
    arrowLeft = 43
    arrowRight = 44
    arrowTop = 45
    arrowTopDoubleLine = 46
    arrowTopLine = 47
    arrowTripleTop = 48
    attitudes = 49
    aura = 50
    authenticator = 51
    axe = 52
    battery = 53
    bellOff = 54
    bellOn = 55
    belt = 56
    bigKnife = 57
    block = 58
    boots = 59
    boss = 60
    bow = 61
    breach = 62
    brokenCup = 63
    brokenSwords = 64
    bug = 65
    calendar = 66
    calendarOne = 67
    calendarSeven = 68
    cape = 69
    celebration = 70
    chains = 71
    challenges = 72
    chart = 73
    chat = 74
    checkboxActive = 75
    checkboxpartial = 76
    chest = 77
    chevronBottom = 78
    chevronLeft = 79
    chevronRight = 80
    chevronTop = 81
    circle = 82
    circleCross = 83
    circleLock = 84
    circleOne = 85
    circleThree = 86
    circleTick = 87
    circleTickInverted = 88
    circleTwo = 89
    circleWarning = 90
    cog = 91
    collapse = 92
    companion = 93
    compare = 94
    copy = 95
    costume = 96
    creature = 97
    cross = 98
    crossedSwords = 99
    crown = 100
    dagger = 101
    deadCreature = 102
    diamondDouble = 103
    diamondFill = 104
    diamondOutline = 105
    dice = 106
    divide = 107
    dna = 108
    dofus = 109
    dragoturkey = 110
    dungeonRusher = 111
    earth = 112
    edit = 113
    enter = 114
    envelope = 115
    equal = 116
    equipItem = 117
    exchange = 118
    exclamationMark = 119
    exclamationMarkDailyRepeat = 120
    exclamationMarkWeeklyRepeat = 121
    expand = 122
    experience = 123
    external = 124
    eye = 125
    eyeSlashed = 126
    familiar = 127
    familyTree = 128
    fatality = 129
    feather = 130
    femaleGender = 131
    filter = 132
    fire = 133
    flag = 134
    flashingLight = 135
    flask = 136
    floppy = 137
    fm = 138
    fold = 139
    folder = 140
    food = 141
    fragment = 142
    gift = 143
    gobbal = 144
    grid = 145
    guild = 146
    guildExperience = 147
    hammer = 148
    havreSac = 149
    heal = 150
    heart = 151
    helmet = 152
    hexagon = 153
    highlight = 154
    hook = 155
    horseshoe = 156
    hourglass = 157
    house = 158
    import = 159
    infinite = 160
    info = 161
    initiative = 162
    item = 163
    kamas = 164
    krosmoz = 165
    lance = 166
    last = 167
    leave = 168
    lines = 169
    link = 170
    lock = 171
    lockFriends = 172
    lockSolo = 173
    losange = 174
    loudspeakerOff = 175
    loudspeakerOn = 176
    magnifier = 177
    maleGender = 178
    menu = 179
    menuVertical = 180
    minus = 181
    money = 182
    moreActions = 183
    mouse = 184
    mouseLeft = 185
    mouseRight = 186
    move = 187
    multiElement = 188
    multiSelect = 189
    net = 190
    neutral = 191
    ogrin = 192
    omega = 193
    ornament = 194
    palette = 195
    panoplie = 196
    parchment = 197
    party = 198
    pause = 199
    petsmount = 200
    pickaxe = 201
    pin = 202
    pinClock = 203
    play = 204
    player = 205
    playerStanding = 206
    plus = 207
    poo = 208
    prism = 209
    prysmaradite = 210
    pushPin = 211
    questionMark = 212
    quests = 213
    radioOff = 214
    radioOn = 215
    rain = 216
    random = 217
    recipe = 218
    recycle = 219
    reduce = 220
    resources = 221
    released = 222
    reset = 223
    rhineetle = 224
    ring = 225
    ringInclined = 226
    rotate = 227
    rotationArrow = 228
    rotationArrowUp = 229
    rune = 230
    saddle = 231
    saddleCrossed = 232
    scissors = 233
    scythe = 234
    seemyool = 235
    send = 236
    sendLeft = 237
    share = 238
    shield = 239
    shinySword = 240
    shop = 241
    shoulderPad = 242
    shovel = 243
    shutDown = 244
    simeyOther = 245
    simeySad = 246
    sixDots = 247
    skull = 248
    smileyHappy = 249
    sort = 250
    spaceKey = 251
    spanner = 252
    spectate = 253
    spell = 254
    spiderGraph = 255
    squareOne = 256
    squarePlus = 257
    squareThree = 258
    squareTwo = 259
    starBoot = 260
    starBow = 261
    starEmpty = 262
    starFilled = 263
    starHat = 264
    starRing = 265
    starShield = 266
    starSword = 267
    stick = 268
    subscription = 269
    success = 270
    sun = 271
    target = 272
    teleport = 273
    text = 274
    thunder = 275
    tick = 276
    ticket = 277
    tileBug = 278
    tileDetails = 279
    tileSmall = 280
    timeline = 281
    tiredness = 282
    titan = 283
    trap = 284
    trash = 285
    treasureMap = 286
    triangle = 287
    triangleWarning = 288
    trophy = 289
    turn = 290
    twinkleScreenOff = 291
    twinkleScreenOn = 292
    underpants = 293
    unfold = 294
    unlock = 295
    water = 296
    wand = 297
    waveMonsters = 298
    weapon = 299
    weight = 300
    widget = 301
    wind = 302
    wings = 303
    world = 304
    zaap = 305

# Core.UILogic.Components.Figma.HeaderWidget
class HeaderWidget(IntFlag):
    horizontal = 0
    vertical = 1

# Core.UILogic.Components.Figma.HeaderWidget
class HeaderWidget(IntFlag):
    small = 0
    large = 1

# Core.UILogic.Components.Figma.HeaderWindow
class HeaderWindow(IntFlag):
    primary = 0
    secondary = 1
    tertiary = 2

# Core.UILogic.Components.Figma.ListElementBase
class ListElementBase(IntFlag):
    small = 0
    medium = 1

# Core.UILogic.Components.Figma.ListElementBasic
class ListElementBasic(IntFlag):
    choice = 0
    action = 1
    actionCritical = 2
    setting = 3

# Core.UILogic.Components.Figma.PortraitRanking
class PortraitRanking(IntFlag):
    Gold = 1
    Silver = 2
    Copper = 3

# Core.UILogic.Components.Figma.RadioButton
class RadioButton(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.RadioButton
class RadioButton(IntFlag):
    text = 0
    icon = 1

# Core.UILogic.Components.Figma.SectionHeader
class SectionHeader(IntFlag):
    section = 0
    nav = 1

# Core.UILogic.Components.Figma.SectionHeader
class SectionHeader(IntFlag):
    one = 0
    two = 1
    three = 2
    four = 3

# Core.UILogic.Components.Figma.ShortcutFigs
class ShortcutFigs(IntFlag):
    none = 0
    key = 1
    text = 2
    icon = 3

# Core.UILogic.Components.Figma.ShortcutFigs
class ShortcutFigs(IntFlag):
    filled = 0
    outlined = 1

# Core.UILogic.Components.Figma.ShortcutFigs
class ShortcutFigs(IntFlag):
    purple = 0
    white = 1
    yellow = 2

# Core.UILogic.Components.Figma.ShortcutFigs
class ShortcutFigs(IntFlag):
    single = 0
    multi = 1

# Core.UILogic.Components.Figma.ShortcutInput
class ShortcutInput(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.SpellTileMaster
class SpellTileMaster(IntFlag):
    Secret = 0
    known = 1
    unknown = 2

# Core.UILogic.Components.Figma.SpellTileSizeEnum
class SpellTileSizeEnum(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.Switch
class Switch(IntFlag):
    none = 0
    choice = 1
    boolean = 2

# Core.UILogic.Components.Figma.Switch
class Switch(IntFlag):
    left = 0
    right = 1

# Core.UILogic.Components.Figma.Switch
class Switch(IntFlag):
    medium = 0
    large = 1

# Core.UILogic.Components.Figma.Switch
class Switch(IntFlag):
    text = 0
    icon = 1

# Core.UILogic.Components.Figma.TableColumnHeader
class TableColumnHeader(IntFlag):
    text = 0
    icon = 1

# Core.UILogic.Components.Figma.TableColumnHeader
class TableColumnHeader(IntFlag):
    Inactive = 0
    Ascending = 1
    Descending = 2

# Core.UILogic.Components.Figma.Tag
class Tag(IntFlag):
    none = 0
    normal = 1
    negative = 2
    positive = 3
    solid = 4
    gold = 5

# Core.UILogic.Components.Figma.Tag
class Tag(IntFlag):
    small = 0
    medium = 1

# Core.UILogic.Components.Figma.Tag
class Tag(IntFlag):
    outline = 0
    filled = 1
    outlineFilled = 2

# Core.UILogic.Components.Figma.TextInput
class TextInput(IntFlag):
    text = 0
    number = 1

# Core.UILogic.Components.Figma.TextInput
class TextInput(IntFlag):
    small = 0
    medium = 1
    large = 2

# Core.UILogic.Components.Figma.TextInputToValidate
class TextInputToValidate(IntFlag):
    small = 0
    medium = 1


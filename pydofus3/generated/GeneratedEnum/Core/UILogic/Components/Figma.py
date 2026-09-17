from enum import IntEnum
from enum import IntFlag

class AssetToggleLine:
	class TextSide(IntEnum):
		Left = 0
		Right = 1
		Both = 2
		None_ = 3

	class Size(IntEnum):
		small = 0
		medium = 1
		large = 2

class BasicTooltipHeader:
	class BasicTooltipHeaderStyle(IntEnum):
		titleTag = 0
		titleSubtitle = 1
		title = 2
		titleTagLine = 3

class ChallengeIcon:
	class ChallengeType(IntEnum):
		regular = 0
		success = 1

	class ChallengeResult(IntEnum):
		none = 0
		completed = 1
		failed = 2

class CheckboxCustom:
	class Size(IntEnum):
		small = 0
		medium = 1
		large = 2

class CircularGauge:
	class GaugeColorEnum(IntEnum):
		none = 0
		primary = 1
		green = 2
		red = 3
		orange = 4
		grey = 5
		purple = 6
		white = 7

class CurrencyField:
	class CurrencyType(IntEnum):
		Nugget = 0
		Kamas = 1
		Ogrine = 2
		DreamPoint = 3
		Item = 4
		GuildKamas = 5

class Divider:
	class ComponentStyle(IntEnum):
		simple = 0
		shadow = 1
		gradient = 2
		gradient_shadow = 3

	class Orientation(IntEnum):
		horizontal = 0
		vertical = 1

class DofusButtonCustom:
	class ButtonContentEnum(IntFlag):
		text = 1
		icon = 2
		textIcon = 3
		asset = 4
		textAsset = 5

	class IconPositionEnum(IntEnum):
		Left = 0
		Right = 1
		Both = 2

	class IconTypeEnum(IntEnum):
		Icon = 0
		Image = 1

	class ComponentStyleEnum(IntEnum):
		primary = 0
		secondary = 1
		tertiary = 2
		link = 3
		floating = 4
		document = 5

	class ButtonStatusEnum(IntEnum):
		normal = 0
		negative = 1
		strong = 2
		light = 3
		dark = 4

	class SizeEnum(IntEnum):
		small = 0
		medium = 1
		large = 2

class DofusTab:
	class TabSize(IntEnum):
		small = 0
		medium = 1
		large = 2

	class TextCaseEnum(IntEnum):
		normal = 0
		fullCaps = 1

	class TabContentEnum(IntEnum):
		text = 0
		asset = 1

class DofusToggleButtonCustom:
	class ButtonContentEnum(IntFlag):
		text = 1
		icon = 2
		textIcon = 3
		asset = 4
		textAsset = 5

	class ComponentStyleEnum(IntEnum):
		none = 0
		primary = 1
		secondary = 2
		navigation = 3
		favorite = 4

	class IconTypeEnum(IntEnum):
		Icon = 0
		Image = 1

	class ToggleColorEnum(IntEnum):
		normal = 0
		blue = 1
		green = 2

	class ToggleSizeEnum(IntEnum):
		small = 0
		medium = 1
		large = 2
		xLarge = 3
		xxLarge = 4
		huge = 5

class Dropdown:
	class DropdownSizeEnum(IntEnum):
		small = 0
		medium = 1

	class DropdownTypeEnum(IntEnum):
		text = 0
		icon = 1

class FigmaIcons(IntEnum):
	none = 0
	activity = 1
	addCharacter = 2
	alliance = 3
	allianceBanner = 4
	almanax = 5
	alteration = 6
	amulet = 7
	ankama = 8
	anomaly = 9
	archimonster = 10
	areaBoomerang = 11
	areaCircle = 12
	areaCone = 13
	areaCross = 14
	areaCrossWithoutCenter = 15
	areaDiagonalCross = 16
	areaDiagonalCrossWithoutCenter = 17
	areaDiagonalLine = 18
	areaFork = 19
	areaHalfCircle = 20
	areaLine = 21
	areaLineFromCaster = 22
	areaPerpendicularDiagonalLine = 23
	areaPerpendicularLine = 24
	areaRectangle = 25
	areaRing = 26
	areaSquare = 27
	areaSquareWithoutDiagonal = 28
	areaStar = 29
	armor = 30
	arrowAngle = 31
	arrowBigBottom = 32
	arrowBigBottomLeft = 33
	arrowBigBottomRight = 34
	arrowBigLeft = 35
	arrowBigRight = 36
	arrowBigTopLeft = 37
	arrowBigTopRight = 38
	arrowBigUp = 39
	arrowBottom = 40
	arrowBottomDoubleLine = 41
	arrowBottomLine = 42
	arrowDoubleTop = 43
	arrowLeft = 44
	arrowRight = 45
	arrowTop = 46
	arrowTopDoubleLine = 47
	arrowTopLine = 48
	arrowTripleTop = 49
	attitudes = 50
	aura = 51
	authenticator = 52
	axe = 53
	battery = 54
	bellOff = 55
	bellOn = 56
	belt = 57
	bigKnife = 58
	block = 59
	boots = 60
	boss = 61
	bow = 62
	breach = 63
	brokenCup = 64
	brokenSwords = 65
	brush = 66
	brushSlashed = 67
	bug = 68
	calendar = 69
	calendarOne = 70
	calendarSeven = 71
	cape = 72
	celebration = 73
	chains = 74
	challenges = 75
	character = 76
	chart = 77
	chat = 78
	checkboxActive = 79
	checkboxpartial = 80
	chest = 81
	chevronBottom = 82
	chevronLeft = 83
	chevronRight = 84
	chevronTop = 85
	circle = 86
	circleCross = 87
	circleLock = 88
	circleOne = 89
	circleThree = 90
	circleTick = 91
	circleTickInverted = 92
	circleTwo = 93
	circleWarning = 94
	cog = 95
	collapse = 96
	companion = 97
	compare = 98
	copy = 99
	costume = 100
	creature = 101
	cross = 102
	crossedSwords = 103
	crown = 104
	dagger = 105
	deadCreature = 106
	diamondDouble = 107
	diamondFill = 108
	diamondObjectiveQuest = 109
	diamondObjectiveQuestPrincipal = 110
	diamondObjectiveQuestRepeat = 111
	diamondOutline = 112
	diamondQuest = 113
	diamondQuestPrimordial = 114
	diamondQuestRepeat = 115
	dice = 116
	divide = 117
	dna = 118
	dofus = 119
	dofusLink = 120
	dragoturkey = 121
	dungeonRusher = 122
	earth = 123
	edit = 124
	enter = 125
	envelope = 126
	equal = 127
	equipItem = 128
	exchange = 129
	exclamationMark = 130
	exclamationMarkDailyRepeat = 131
	exclamationMarkWeeklyRepeat = 132
	expand = 133
	experience = 134
	external = 135
	eye = 136
	eyeSlashed = 137
	familiar = 138
	familyTree = 139
	fatality = 140
	feather = 141
	femaleGender = 142
	filter = 143
	fire = 144
	flag = 145
	flashingLight = 146
	flask = 147
	floppy = 148
	fm = 149
	fold = 150
	folder = 151
	food = 152
	foreground = 153
	fragment = 154
	genealogy = 155
	gift = 156
	gobbal = 157
	glyph = 158
	grid = 159
	guild = 160
	guildExperience = 161
	hammer = 162
	havreSac = 163
	heal = 164
	heart = 165
	helmet = 166
	hexagon = 167
	highlight = 168
	hook = 169
	horseshoe = 170
	hourglass = 171
	house = 172
	import = 173
	infinite = 174
	info = 175
	initiative = 176
	item = 177
	job = 178
	kamas = 179
	krosmoz = 180
	lance = 181
	last = 182
	leave = 183
	lines = 184
	link = 185
	livingObject = 186
	lock = 187
	lockFriends = 188
	lockSolo = 189
	losange = 190
	loudspeakerOff = 191
	loudspeakerOn = 192
	magnifier = 193
	maleGender = 194
	medal = 195
	menu = 196
	menuVertical = 197
	mimibiote = 198
	minus = 199
	money = 200
	moreActions = 201
	mouse = 202
	mouseLeft = 203
	mouseRight = 204
	move = 205
	multiElement = 206
	multiSelect = 207
	net = 208
	neutral = 209
	objectiveQuestInitiation = 210
	objectiveQuestPrimordial = 211
	objectiveQuestPrincipal = 212
	ogrin = 213
	omega = 214
	ornament = 215
	page = 216
	palette = 217
	panoplie = 218
	parchment = 219
	party = 220
	pause = 221
	petsmount = 222
	pickaxe = 223
	pin = 224
	pinClock = 225
	play = 226
	player = 227
	playerStanding = 228
	plus = 229
	poo = 230
	prism = 231
	prysmaradite = 232
	pushPin = 233
	questInitiation = 234
	questionMark = 235
	questPrimordial = 236
	questPrincipal = 237
	quests = 238
	radioOff = 239
	radioOn = 240
	rain = 241
	random = 242
	recipe = 243
	recycle = 244
	reduce = 245
	resources = 246
	released = 247
	reset = 248
	rhineetle = 249
	ring = 250
	ringInclined = 251
	rotate = 252
	rotationArrow = 253
	rotationArrowUp = 254
	rune = 255
	saddle = 256
	saddleCrossed = 257
	scissors = 258
	scythe = 259
	seemyool = 260
	send = 261
	sendLeft = 262
	share = 263
	shield = 264
	shinySword = 265
	shop = 266
	shoulderPad = 267
	shovel = 268
	shutDown = 269
	simeyOther = 270
	simeySad = 271
	sixDots = 272
	skull = 273
	smileyHappy = 274
	smileyNeutral = 275
	smileySad = 276
	smileyVeryHappy = 277
	smileyVerySad = 278
	sort = 279
	spaceKey = 280
	spanner = 281
	spectate = 282
	spell = 283
	spiderGraph = 284
	squareOne = 285
	squarePlus = 286
	squareThree = 287
	squareTwo = 288
	starBoot = 289
	starBow = 290
	starEmpty = 291
	starFilled = 292
	starHat = 293
	starRing = 294
	starShield = 295
	starSword = 296
	stick = 297
	subscription = 298
	success = 299
	successEmpty = 300
	sun = 301
	target = 302
	teleport = 303
	text = 304
	thunder = 305
	tick = 306
	ticket = 307
	tileBug = 308
	tileDetails = 309
	tileSmall = 310
	timeline = 311
	tiredness = 312
	titan = 313
	trap = 314
	trash = 315
	treasureMap = 316
	triangle = 317
	triangleWarning = 318
	trophy = 319
	turn = 320
	twinkleScreenOff = 321
	twinkleScreenOn = 322
	underpants = 323
	unfold = 324
	unlock = 325
	water = 326
	wand = 327
	waveMonsters = 328
	weapon = 329
	weight = 330
	widget = 331
	wind = 332
	wings = 333
	world = 334
	zaap = 335

class HeaderWidget:
	class ComponentStyleEnum(IntEnum):
		horizontal = 0
		vertical = 1

	class ComponentSizeEnum(IntEnum):
		small = 0
		large = 1

class HeaderWindow:
	class ComponentStyleEnum(IntEnum):
		primary = 0
		secondary = 1
		tertiary = 2

class ListElementBase:
	class ListElementSizeEnum(IntEnum):
		small = 0
		medium = 1

class ListElementBasic:
	class ListElementStyleEnum(IntEnum):
		choice = 0
		action = 1
		actionCritical = 2
		setting = 3

class PortraitRanking:
	class RankingStyle(IntEnum):
		Gold = 1
		Silver = 2
		Copper = 3

class RadioButton:
	class Size(IntEnum):
		small = 0
		medium = 1
		large = 2

	class Type(IntEnum):
		text = 0
		icon = 1

class SectionHeader:
	class SectionHeaderDepth(IntEnum):
		one = 0
		two = 1
		three = 2
		four = 3

	class SectionHeaderStyleEnum(IntEnum):
		section = 0
		nav = 1

class ShortcutFigs:
	class ShortcutStyle(IntEnum):
		filled = 0
		outlined = 1

	class ShortcutColor(IntEnum):
		purple = 0
		white = 1
		yellow = 2

	class ShortcutOrientation(IntEnum):
		horizontal = 0
		vertical = 1

	class ShortcutType(IntEnum):
		none = 0
		key = 1
		text = 2
		icon = 3
		keyIcon = 4

	class ShortcutElement:
		class ShortcutSize(IntEnum):
			single = 0
			multi = 1

class ShortcutInput:
	class TextInputStyleEnum(IntEnum):
		small = 0
		medium = 1
		large = 2

class SpellTileMaster:
	class SpellTileSizeEnum(IntEnum):
		small = 0
		medium = 1
		large = 2

	class SpellTileMasterStatusEnum(IntEnum):
		Secret = 0
		known = 1
		unknown = 2

class Switch:
	class SwitchPosition(IntEnum):
		left = 0
		right = 1

	class ComponentStyleEnum(IntEnum):
		choice = 0
		boolean = 1

	class Size(IntEnum):
		medium = 0
		large = 1

	class ContentType(IntEnum):
		text = 0
		icon = 1

class TableColumnHeader:
	class TableColumnHeaderTypeEnum(IntEnum):
		text = 0
		icon = 1

	class TableColumnHeaderState(IntEnum):
		Inactive = 0
		Ascending = 1
		Descending = 2

class Tag:
	class StatusEnum(IntEnum):
		none = 0
		normal = 1
		negative = 2
		positive = 3
		warning = 4
		gold = 5

	class SizeEnum(IntEnum):
		small = 0
		medium = 1

	class StyleEnum(IntEnum):
		outline = 0
		filled = 1
		outlineFilled = 2
		solid = 3

class TextInput:
	class TextInputStyleEnum(IntEnum):
		small = 0
		medium = 1
		large = 2

	class ContentType(IntEnum):
		text = 0
		number = 1

	class ErrorCondition(IntEnum):
		Length = 0
		Value = 1

class TextInputToValidate:
	class TextInputToValidateStyleEnum(IntEnum):
		small = 0
		medium = 1


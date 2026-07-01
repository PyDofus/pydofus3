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
		icons = 2

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
	fragment = 153
	genealogy = 154
	gift = 155
	gobbal = 156
	grid = 157
	guild = 158
	guildExperience = 159
	hammer = 160
	havreSac = 161
	heal = 162
	heart = 163
	helmet = 164
	hexagon = 165
	highlight = 166
	hook = 167
	horseshoe = 168
	hourglass = 169
	house = 170
	import = 171
	infinite = 172
	info = 173
	initiative = 174
	item = 175
	job = 176
	kamas = 177
	krosmoz = 178
	lance = 179
	last = 180
	leave = 181
	lines = 182
	link = 183
	livingObject = 184
	lock = 185
	lockFriends = 186
	lockSolo = 187
	losange = 188
	loudspeakerOff = 189
	loudspeakerOn = 190
	magnifier = 191
	maleGender = 192
	medal = 193
	menu = 194
	menuVertical = 195
	mimibiote = 196
	minus = 197
	money = 198
	moreActions = 199
	mouse = 200
	mouseLeft = 201
	mouseRight = 202
	move = 203
	multiElement = 204
	multiSelect = 205
	net = 206
	neutral = 207
	objectiveQuestInitiation = 208
	objectiveQuestPrimordial = 209
	objectiveQuestPrincipal = 210
	ogrin = 211
	omega = 212
	ornament = 213
	page = 214
	palette = 215
	panoplie = 216
	parchment = 217
	party = 218
	pause = 219
	petsmount = 220
	pickaxe = 221
	pin = 222
	pinClock = 223
	play = 224
	player = 225
	playerStanding = 226
	plus = 227
	poo = 228
	prism = 229
	prysmaradite = 230
	pushPin = 231
	questInitiation = 232
	questionMark = 233
	questPrimordial = 234
	questPrincipal = 235
	quests = 236
	radioOff = 237
	radioOn = 238
	rain = 239
	random = 240
	recipe = 241
	recycle = 242
	reduce = 243
	resources = 244
	released = 245
	reset = 246
	rhineetle = 247
	ring = 248
	ringInclined = 249
	rotate = 250
	rotationArrow = 251
	rotationArrowUp = 252
	rune = 253
	saddle = 254
	saddleCrossed = 255
	scissors = 256
	scythe = 257
	seemyool = 258
	send = 259
	sendLeft = 260
	share = 261
	shield = 262
	shinySword = 263
	shop = 264
	shoulderPad = 265
	shovel = 266
	shutDown = 267
	simeyOther = 268
	simeySad = 269
	sixDots = 270
	skull = 271
	smileyHappy = 272
	smileyNeutral = 273
	smileySad = 274
	smileyVeryHappy = 275
	smileyVerySad = 276
	sort = 277
	spaceKey = 278
	spanner = 279
	spectate = 280
	spell = 281
	spiderGraph = 282
	squareOne = 283
	squarePlus = 284
	squareThree = 285
	squareTwo = 286
	starBoot = 287
	starBow = 288
	starEmpty = 289
	starFilled = 290
	starHat = 291
	starRing = 292
	starShield = 293
	starSword = 294
	stick = 295
	subscription = 296
	success = 297
	sun = 298
	target = 299
	teleport = 300
	text = 301
	thunder = 302
	tick = 303
	ticket = 304
	tileBug = 305
	tileDetails = 306
	tileSmall = 307
	timeline = 308
	tiredness = 309
	titan = 310
	trap = 311
	trash = 312
	treasureMap = 313
	triangle = 314
	triangleWarning = 315
	trophy = 316
	turn = 317
	twinkleScreenOff = 318
	twinkleScreenOn = 319
	underpants = 320
	unfold = 321
	unlock = 322
	water = 323
	wand = 324
	waveMonsters = 325
	weapon = 326
	weight = 327
	widget = 328
	wind = 329
	wings = 330
	world = 331
	zaap = 332

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

	class ShortcutType(IntEnum):
		none = 0
		key = 1
		text = 2
		icon = 3

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


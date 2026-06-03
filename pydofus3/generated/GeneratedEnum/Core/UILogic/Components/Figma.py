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
	diamondOutline = 109
	diamondQuest = 110
	diamondQuestPrimordial = 111
	diamondQuestRepeat = 112
	dice = 113
	divide = 114
	dna = 115
	dofus = 116
	dofusLink = 117
	dragoturkey = 118
	dungeonRusher = 119
	earth = 120
	edit = 121
	effect = 122
	enter = 123
	envelope = 124
	equal = 125
	equipItem = 126
	exchange = 127
	exclamationMark = 128
	exclamationMarkDailyRepeat = 129
	exclamationMarkWeeklyRepeat = 130
	expand = 131
	experience = 132
	external = 133
	eye = 134
	eyeSlashed = 135
	familiar = 136
	familyTree = 137
	fatality = 138
	feather = 139
	femaleGender = 140
	filter = 141
	fire = 142
	flag = 143
	flashingLight = 144
	flask = 145
	floppy = 146
	fm = 147
	fold = 148
	folder = 149
	food = 150
	fragment = 151
	genealogy = 152
	gift = 153
	gobbal = 154
	grid = 155
	guild = 156
	guildExperience = 157
	hammer = 158
	havreSac = 159
	heal = 160
	heart = 161
	helmet = 162
	hexagon = 163
	highlight = 164
	hook = 165
	horseshoe = 166
	hourglass = 167
	house = 168
	import = 169
	infinite = 170
	info = 171
	initiative = 172
	item = 173
	job = 174
	kamas = 175
	krosmoz = 176
	lance = 177
	last = 178
	leave = 179
	lines = 180
	link = 181
	livingObject = 182
	lock = 183
	lockFriends = 184
	lockSolo = 185
	losange = 186
	loudspeakerOff = 187
	loudspeakerOn = 188
	magnifier = 189
	maleGender = 190
	medal = 191
	menu = 192
	menuVertical = 193
	mimibiote = 194
	minus = 195
	money = 196
	moreActions = 197
	mouse = 198
	mouseLeft = 199
	mouseRight = 200
	move = 201
	multiElement = 202
	multiSelect = 203
	net = 204
	neutral = 205
	objectiveQuestPrimordial = 206
	objectiveQuestPrincipal = 207
	ogrin = 208
	omega = 209
	ornament = 210
	page = 211
	palette = 212
	panoplie = 213
	parchment = 214
	party = 215
	pause = 216
	petsmount = 217
	pickaxe = 218
	pin = 219
	pinClock = 220
	play = 221
	player = 222
	playerStanding = 223
	plus = 224
	poo = 225
	prism = 226
	prysmaradite = 227
	pushPin = 228
	questInitiation = 229
	questionMark = 230
	quests = 231
	radioOff = 232
	radioOn = 233
	rain = 234
	random = 235
	recipe = 236
	recycle = 237
	reduce = 238
	resources = 239
	released = 240
	reset = 241
	rhineetle = 242
	ring = 243
	ringInclined = 244
	rotate = 245
	rotationArrow = 246
	rotationArrowUp = 247
	rune = 248
	saddle = 249
	saddleCrossed = 250
	scissors = 251
	scythe = 252
	seemyool = 253
	send = 254
	sendLeft = 255
	share = 256
	shield = 257
	shinySword = 258
	shop = 259
	shoulderPad = 260
	shovel = 261
	shutDown = 262
	simeyOther = 263
	simeySad = 264
	sixDots = 265
	skull = 266
	smileyHappy = 267
	smileyNeutral = 268
	smileySad = 269
	smileyVeryHappy = 270
	smileyVerySad = 271
	sort = 272
	spaceKey = 273
	spanner = 274
	spectate = 275
	spell = 276
	spiderGraph = 277
	squareOne = 278
	squarePlus = 279
	squareThree = 280
	squareTwo = 281
	starBoot = 282
	starBow = 283
	starEmpty = 284
	starFilled = 285
	starHat = 286
	starRing = 287
	starShield = 288
	starSword = 289
	stick = 290
	subscription = 291
	success = 292
	sun = 293
	target = 294
	teleport = 295
	text = 296
	thunder = 297
	tick = 298
	ticket = 299
	tileBug = 300
	tileDetails = 301
	tileSmall = 302
	timeline = 303
	tiredness = 304
	titan = 305
	trap = 306
	trash = 307
	treasureMap = 308
	triangle = 309
	triangleWarning = 310
	trophy = 311
	turn = 312
	twinkleScreenOff = 313
	twinkleScreenOn = 314
	underpants = 315
	unfold = 316
	unlock = 317
	water = 318
	wand = 319
	waveMonsters = 320
	weapon = 321
	weight = 322
	widget = 323
	wind = 324
	wings = 325
	world = 326
	zaap = 327

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

class TextInputToValidate:
	class TextInputToValidateStyleEnum(IntEnum):
		small = 0
		medium = 1


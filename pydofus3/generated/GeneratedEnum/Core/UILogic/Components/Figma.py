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
	chart = 76
	chat = 77
	checkboxActive = 78
	checkboxpartial = 79
	chest = 80
	chevronBottom = 81
	chevronLeft = 82
	chevronRight = 83
	chevronTop = 84
	circle = 85
	circleCross = 86
	circleLock = 87
	circleOne = 88
	circleThree = 89
	circleTick = 90
	circleTickInverted = 91
	circleTwo = 92
	circleWarning = 93
	cog = 94
	collapse = 95
	companion = 96
	compare = 97
	copy = 98
	costume = 99
	creature = 100
	cross = 101
	crossedSwords = 102
	crown = 103
	dagger = 104
	deadCreature = 105
	diamondDouble = 106
	diamondFill = 107
	diamondOutline = 108
	dice = 109
	divide = 110
	dna = 111
	dofus = 112
	dragoturkey = 113
	dungeonRusher = 114
	earth = 115
	edit = 116
	enter = 117
	envelope = 118
	equal = 119
	equipItem = 120
	exchange = 121
	exclamationMark = 122
	exclamationMarkDailyRepeat = 123
	exclamationMarkWeeklyRepeat = 124
	expand = 125
	experience = 126
	external = 127
	eye = 128
	eyeSlashed = 129
	familiar = 130
	familyTree = 131
	fatality = 132
	feather = 133
	femaleGender = 134
	filter = 135
	fire = 136
	flag = 137
	flashingLight = 138
	flask = 139
	floppy = 140
	fm = 141
	fold = 142
	folder = 143
	food = 144
	fragment = 145
	genealogy = 146
	gift = 147
	gobbal = 148
	grid = 149
	guild = 150
	guildExperience = 151
	hammer = 152
	havreSac = 153
	heal = 154
	heart = 155
	helmet = 156
	hexagon = 157
	highlight = 158
	hook = 159
	horseshoe = 160
	hourglass = 161
	house = 162
	import = 163
	infinite = 164
	info = 165
	initiative = 166
	item = 167
	kamas = 168
	krosmoz = 169
	lance = 170
	last = 171
	leave = 172
	lines = 173
	link = 174
	livingObject = 175
	lock = 176
	lockFriends = 177
	lockSolo = 178
	losange = 179
	loudspeakerOff = 180
	loudspeakerOn = 181
	magnifier = 182
	maleGender = 183
	menu = 184
	menuVertical = 185
	mimibiote = 186
	minus = 187
	money = 188
	moreActions = 189
	mouse = 190
	mouseLeft = 191
	mouseRight = 192
	move = 193
	multiElement = 194
	multiSelect = 195
	net = 196
	neutral = 197
	ogrin = 198
	omega = 199
	ornament = 200
	page = 201
	palette = 202
	panoplie = 203
	parchment = 204
	party = 205
	pause = 206
	petsmount = 207
	pickaxe = 208
	pin = 209
	pinClock = 210
	play = 211
	player = 212
	playerStanding = 213
	plus = 214
	poo = 215
	prism = 216
	prysmaradite = 217
	pushPin = 218
	questionMark = 219
	quests = 220
	radioOff = 221
	radioOn = 222
	rain = 223
	random = 224
	recipe = 225
	recycle = 226
	reduce = 227
	resources = 228
	released = 229
	reset = 230
	rhineetle = 231
	ring = 232
	ringInclined = 233
	rotate = 234
	rotationArrow = 235
	rotationArrowUp = 236
	rune = 237
	saddle = 238
	saddleCrossed = 239
	scissors = 240
	scythe = 241
	seemyool = 242
	send = 243
	sendLeft = 244
	share = 245
	shield = 246
	shinySword = 247
	shop = 248
	shoulderPad = 249
	shovel = 250
	shutDown = 251
	simeyOther = 252
	simeySad = 253
	sixDots = 254
	skull = 255
	smileyHappy = 256
	smileyNeutral = 257
	smileySad = 258
	smileyVeryHappy = 259
	smileyVerySad = 260
	sort = 261
	spaceKey = 262
	spanner = 263
	spectate = 264
	spell = 265
	spiderGraph = 266
	squareOne = 267
	squarePlus = 268
	squareThree = 269
	squareTwo = 270
	starBoot = 271
	starBow = 272
	starEmpty = 273
	starFilled = 274
	starHat = 275
	starRing = 276
	starShield = 277
	starSword = 278
	stick = 279
	subscription = 280
	success = 281
	sun = 282
	target = 283
	teleport = 284
	text = 285
	thunder = 286
	tick = 287
	ticket = 288
	tileBug = 289
	tileDetails = 290
	tileSmall = 291
	timeline = 292
	tiredness = 293
	titan = 294
	trap = 295
	trash = 296
	treasureMap = 297
	triangle = 298
	triangleWarning = 299
	trophy = 300
	turn = 301
	twinkleScreenOff = 302
	twinkleScreenOn = 303
	underpants = 304
	unfold = 305
	unlock = 306
	water = 307
	wand = 308
	waveMonsters = 309
	weapon = 310
	weight = 311
	widget = 312
	wind = 313
	wings = 314
	world = 315
	zaap = 316

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
		gold = 4

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


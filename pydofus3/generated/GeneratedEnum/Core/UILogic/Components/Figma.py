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
	enter = 122
	envelope = 123
	equal = 124
	equipItem = 125
	exchange = 126
	exclamationMark = 127
	exclamationMarkDailyRepeat = 128
	exclamationMarkWeeklyRepeat = 129
	expand = 130
	experience = 131
	external = 132
	eye = 133
	eyeSlashed = 134
	familiar = 135
	familyTree = 136
	fatality = 137
	feather = 138
	femaleGender = 139
	filter = 140
	fire = 141
	flag = 142
	flashingLight = 143
	flask = 144
	floppy = 145
	fm = 146
	fold = 147
	folder = 148
	food = 149
	fragment = 150
	genealogy = 151
	gift = 152
	gobbal = 153
	grid = 154
	guild = 155
	guildExperience = 156
	hammer = 157
	havreSac = 158
	heal = 159
	heart = 160
	helmet = 161
	hexagon = 162
	highlight = 163
	hook = 164
	horseshoe = 165
	hourglass = 166
	house = 167
	import = 168
	infinite = 169
	info = 170
	initiative = 171
	item = 172
	job = 173
	kamas = 174
	krosmoz = 175
	lance = 176
	last = 177
	leave = 178
	lines = 179
	link = 180
	livingObject = 181
	lock = 182
	lockFriends = 183
	lockSolo = 184
	losange = 185
	loudspeakerOff = 186
	loudspeakerOn = 187
	magnifier = 188
	maleGender = 189
	medal = 190
	menu = 191
	menuVertical = 192
	mimibiote = 193
	minus = 194
	money = 195
	moreActions = 196
	mouse = 197
	mouseLeft = 198
	mouseRight = 199
	move = 200
	multiElement = 201
	multiSelect = 202
	net = 203
	neutral = 204
	objectiveQuestPrimordial = 205
	objectiveQuestPrincipal = 206
	ogrin = 207
	omega = 208
	ornament = 209
	page = 210
	palette = 211
	panoplie = 212
	parchment = 213
	party = 214
	pause = 215
	petsmount = 216
	pickaxe = 217
	pin = 218
	pinClock = 219
	play = 220
	player = 221
	playerStanding = 222
	plus = 223
	poo = 224
	prism = 225
	prysmaradite = 226
	pushPin = 227
	questInitiation = 228
	questionMark = 229
	quests = 230
	radioOff = 231
	radioOn = 232
	rain = 233
	random = 234
	recipe = 235
	recycle = 236
	reduce = 237
	resources = 238
	released = 239
	reset = 240
	rhineetle = 241
	ring = 242
	ringInclined = 243
	rotate = 244
	rotationArrow = 245
	rotationArrowUp = 246
	rune = 247
	saddle = 248
	saddleCrossed = 249
	scissors = 250
	scythe = 251
	seemyool = 252
	send = 253
	sendLeft = 254
	share = 255
	shield = 256
	shinySword = 257
	shop = 258
	shoulderPad = 259
	shovel = 260
	shutDown = 261
	simeyOther = 262
	simeySad = 263
	sixDots = 264
	skull = 265
	smileyHappy = 266
	smileyNeutral = 267
	smileySad = 268
	smileyVeryHappy = 269
	smileyVerySad = 270
	sort = 271
	spaceKey = 272
	spanner = 273
	spectate = 274
	spell = 275
	spiderGraph = 276
	squareOne = 277
	squarePlus = 278
	squareThree = 279
	squareTwo = 280
	starBoot = 281
	starBow = 282
	starEmpty = 283
	starFilled = 284
	starHat = 285
	starRing = 286
	starShield = 287
	starSword = 288
	stick = 289
	subscription = 290
	success = 291
	sun = 292
	target = 293
	teleport = 294
	text = 295
	thunder = 296
	tick = 297
	ticket = 298
	tileBug = 299
	tileDetails = 300
	tileSmall = 301
	timeline = 302
	tiredness = 303
	titan = 304
	trap = 305
	trash = 306
	treasureMap = 307
	triangle = 308
	triangleWarning = 309
	trophy = 310
	turn = 311
	twinkleScreenOff = 312
	twinkleScreenOn = 313
	underpants = 314
	unfold = 315
	unlock = 316
	water = 317
	wand = 318
	waveMonsters = 319
	weapon = 320
	weight = 321
	widget = 322
	wind = 323
	wings = 324
	world = 325
	zaap = 326

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


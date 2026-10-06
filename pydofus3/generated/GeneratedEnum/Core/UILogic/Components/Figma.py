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
	glyphHighlight = 159
	grid = 160
	guild = 161
	guildExperience = 162
	hammer = 163
	havreSac = 164
	heal = 165
	heart = 166
	helmet = 167
	hexagon = 168
	highlight = 169
	hook = 170
	horseshoe = 171
	hourglass = 172
	house = 173
	import = 174
	infinite = 175
	info = 176
	initiative = 177
	item = 178
	job = 179
	kamas = 180
	krosmoz = 181
	lance = 182
	last = 183
	leave = 184
	lines = 185
	link = 186
	livingObject = 187
	lock = 188
	lockFriends = 189
	lockSolo = 190
	losange = 191
	loudspeakerOff = 192
	loudspeakerOn = 193
	magnifier = 194
	maleGender = 195
	medal = 196
	menu = 197
	menuVertical = 198
	mimibiote = 199
	minus = 200
	money = 201
	moreActions = 202
	mouse = 203
	mouseLeft = 204
	mouseRight = 205
	move = 206
	multiElement = 207
	multiSelect = 208
	net = 209
	neutral = 210
	objectiveQuestInitiation = 211
	objectiveQuestPrimordial = 212
	objectiveQuestPrincipal = 213
	ogrin = 214
	omega = 215
	ornament = 216
	page = 217
	palette = 218
	panoplie = 219
	parchment = 220
	party = 221
	pause = 222
	petsmount = 223
	pickaxe = 224
	pin = 225
	pinClock = 226
	play = 227
	player = 228
	playerStanding = 229
	plus = 230
	poo = 231
	prism = 232
	prysmaradite = 233
	pushPin = 234
	questInitiation = 235
	questionMark = 236
	questPrimordial = 237
	questPrincipal = 238
	quests = 239
	radioOff = 240
	radioOn = 241
	rain = 242
	random = 243
	recipe = 244
	recycle = 245
	reduce = 246
	resources = 247
	released = 248
	reset = 249
	rhineetle = 250
	ring = 251
	ringInclined = 252
	rotate = 253
	rotationArrow = 254
	rotationArrowUp = 255
	rune = 256
	saddle = 257
	saddleCrossed = 258
	scissors = 259
	scythe = 260
	seemyool = 261
	send = 262
	sendLeft = 263
	share = 264
	shield = 265
	shinySword = 266
	shop = 267
	shoulderPad = 268
	shovel = 269
	shutDown = 270
	simeyOther = 271
	simeySad = 272
	sixDots = 273
	skull = 274
	smileyHappy = 275
	smileyNeutral = 276
	smileySad = 277
	smileyVeryHappy = 278
	smileyVerySad = 279
	sort = 280
	spaceKey = 281
	spanner = 282
	spectate = 283
	spell = 284
	spiderGraph = 285
	squareOne = 286
	squarePlus = 287
	squareThree = 288
	squareTwo = 289
	starBoot = 290
	starBow = 291
	starEmpty = 292
	starFilled = 293
	starHat = 294
	starRing = 295
	starShield = 296
	starSword = 297
	stick = 298
	subscription = 299
	success = 300
	successEmpty = 301
	sun = 302
	target = 303
	teleport = 304
	text = 305
	thunder = 306
	tick = 307
	ticket = 308
	tileBug = 309
	tileDetails = 310
	tileSmall = 311
	timeline = 312
	tiredness = 313
	titan = 314
	trap = 315
	trash = 316
	treasureMap = 317
	triangle = 318
	triangleWarning = 319
	trophy = 320
	turn = 321
	twinkleScreenOff = 322
	twinkleScreenOn = 323
	underpants = 324
	unfold = 325
	unlock = 326
	water = 327
	wand = 328
	waveMonsters = 329
	weapon = 330
	weight = 331
	widget = 332
	wind = 333
	wings = 334
	world = 335
	zaap = 336

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


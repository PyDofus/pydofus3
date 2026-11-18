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

class ColorPickerField:
	class ColorPickerFieldSize(IntEnum):
		large = 0
		medium = 1

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
		negative = 3

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
	groupSearch = 161
	guild = 162
	guildExperience = 163
	hammer = 164
	havreSac = 165
	heal = 166
	heart = 167
	helmet = 168
	hexagon = 169
	highlight = 170
	hook = 171
	horseshoe = 172
	hourglass = 173
	house = 174
	import = 175
	infinite = 176
	info = 177
	initiative = 178
	item = 179
	job = 180
	kamas = 181
	krosmoz = 182
	lance = 183
	last = 184
	leave = 185
	lineage = 186
	lines = 187
	link = 188
	livingObject = 189
	lock = 190
	lockFriends = 191
	lockSolo = 192
	losange = 193
	loudspeakerOff = 194
	loudspeakerOn = 195
	magnifier = 196
	maleGender = 197
	medal = 198
	menu = 199
	menuVertical = 200
	mimibiote = 201
	minus = 202
	money = 203
	moreActions = 204
	mouse = 205
	mouseLeft = 206
	mouseRight = 207
	move = 208
	multiElement = 209
	multiSelect = 210
	net = 211
	neutral = 212
	objectiveQuestInitiation = 213
	objectiveQuestPrimordial = 214
	objectiveQuestPrincipal = 215
	ogrin = 216
	omega = 217
	ornament = 218
	page = 219
	palette = 220
	panoplie = 221
	parchment = 222
	party = 223
	pause = 224
	petsmount = 225
	pickaxe = 226
	pin = 227
	pinClock = 228
	play = 229
	player = 230
	playerStanding = 231
	plus = 232
	poo = 233
	prism = 234
	prysmaradite = 235
	pushPin = 236
	questInitiation = 237
	questionMark = 238
	questPrimordial = 239
	questPrincipal = 240
	quests = 241
	radioOff = 242
	radioOn = 243
	rain = 244
	random = 245
	recipe = 246
	recycle = 247
	reduce = 248
	resources = 249
	released = 250
	reset = 251
	rhineetle = 252
	ring = 253
	ringInclined = 254
	rotate = 255
	rotationArrow = 256
	rotationArrowBig = 257
	rotationArrowUp = 258
	rotationArrowUpBig = 259
	rune = 260
	saddle = 261
	saddleCrossed = 262
	scissors = 263
	scythe = 264
	seemyool = 265
	send = 266
	sendLeft = 267
	share = 268
	shield = 269
	shinySword = 270
	shop = 271
	shoulderPad = 272
	shovel = 273
	shutDown = 274
	simeyOther = 275
	simeySad = 276
	sixDots = 277
	skull = 278
	smileyHappy = 279
	smileyNeutral = 280
	smileySad = 281
	smileyVeryHappy = 282
	smileyVerySad = 283
	sort = 284
	spaceKey = 285
	spanner = 286
	spectate = 287
	spell = 288
	spiderGraph = 289
	squareOne = 290
	squarePlus = 291
	squareThree = 292
	squareTwo = 293
	starBoot = 294
	starBow = 295
	starEmpty = 296
	starFilled = 297
	starHat = 298
	starRing = 299
	starShield = 300
	starSword = 301
	stick = 302
	subscription = 303
	success = 304
	successEmpty = 305
	sun = 306
	target = 307
	teleport = 308
	text = 309
	thunder = 310
	tick = 311
	ticket = 312
	tileBug = 313
	tileDetails = 314
	tileSmall = 315
	timeline = 316
	tiredness = 317
	titan = 318
	trap = 319
	trash = 320
	treasureMap = 321
	triangle = 322
	triangleWarning = 323
	trophy = 324
	turn = 325
	twinkleScreenOff = 326
	twinkleScreenOn = 327
	underpants = 328
	unfold = 329
	unlock = 330
	water = 331
	wand = 332
	waveMonsters = 333
	weapon = 334
	weight = 335
	widget = 336
	wind = 337
	wings = 338
	world = 339
	zaap = 340

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


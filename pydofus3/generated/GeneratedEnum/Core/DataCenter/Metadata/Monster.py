from enum import IntFlag

class MonsterFlags(IntFlag):
	UseSummonSlot = 1
	UseBombSlot = 2
	IsBoss = 4
	IsMiniBoss = 8
	IsQuestMonster = 16
	FastAnimsFun = 32
	CanPlay = 64
	CanTackle = 128
	CanBePushed = 256
	CanSwitchPos = 512
	CanSwitchPosOnTarget = 1024
	CanBeCarried = 2048
	CanUsePortal = 4096
	AllIdolsDisabled = 8192
	UseRaceValues = 16384
	SoulCaptureForbidden = 32768
	HideInBestiary = 65536


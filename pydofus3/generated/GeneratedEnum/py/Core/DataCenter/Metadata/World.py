from enum import IntFlag

# Core.DataCenter.Metadata.World.MapInformationFlags
class MapInformationFlags(IntFlag):
    CapabilityAllowChallenge = 1
    CapabilityAllowAggression = 2
    CapabilityAllowTeleportTo = 4
    CapabilityAllowTeleportFrom = 8
    CapabilityAllowExchangesBetweenPlayers = 16
    CapabilityAllowHumanVendor = 32
    CapabilityAllowCollector = 64
    CapabilityAllowSoulCapture = 128
    CapabilityAllowSoulSummon = 256
    CapabilityAllowTavernRegen = 512
    CapabilityAllowTombMode = 1024
    CapabilityAllowTeleportEverywhere = 2048
    CapabilityAllowFightChallenges = 4096
    CapabilityAllowMonsterRespawn = 8192
    CapabilityAllowMonsterFight = 16384
    CapabilityAllowMount = 32768
    CapabilityAllowObjectDisposal = 65536
    CapabilityAllowUnderwater = 131072
    CapabilityAllowPvp1V1 = 262144
    CapabilityAllowPvp3V3 = 524288
    CapabilityAllowMonsterAggression = 1048576
    AllCapabilitiesMask = 2097151
    Outdoor = 2097152
    ShowNameOnFingerpost = 4194304
    HasPriorityOnWorldmap = 8388608
    AllowPrism = 16777216
    IsTransition = 33554432
    MapHasTemplate = 67108864
    HasPublicPaddock = 134217728


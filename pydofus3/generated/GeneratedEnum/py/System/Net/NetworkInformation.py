from enum import IntFlag

# System.Net.NetworkInformation.DuplicateAddressDetectionState
class DuplicateAddressDetectionState(IntFlag):
    Invalid = 0
    Tentative = 1
    Duplicate = 2
    Deprecated = 3
    Preferred = 4

# System.Net.NetworkInformation.NetBiosNodeType
class NetBiosNodeType(IntFlag):
    Unknown = 0
    Broadcast = 1
    Peer2Peer = 2
    Mixed = 4
    Hybrid = 8

# System.Net.NetworkInformation.NetworkInterfaceComponent
class NetworkInterfaceComponent(IntFlag):
    IPv4 = 0
    IPv6 = 1

# System.Net.NetworkInformation.NetworkInterfaceType
class NetworkInterfaceType(IntFlag):
    Unknown = 1
    Ethernet = 6
    TokenRing = 9
    Fddi = 15
    BasicIsdn = 20
    PrimaryIsdn = 21
    Ppp = 23
    Loopback = 24
    Ethernet3Megabit = 26
    Slip = 28
    Atm = 37
    GenericModem = 48
    FastEthernetT = 62
    Isdn = 63
    FastEthernetFx = 69
    Wireless80211 = 71
    AsymmetricDsl = 94
    RateAdaptDsl = 95
    SymmetricDsl = 96
    VeryHighSpeedDsl = 97
    IPOverAtm = 114
    GigabitEthernet = 117
    Tunnel = 131
    MultiRateSymmetricDsl = 143
    HighPerformanceSerialBus = 144
    Wman = 237
    Wwanpp = 243
    Wwanpp2 = 244

# System.Net.NetworkInformation.OperationalStatus
class OperationalStatus(IntFlag):
    Up = 1
    Down = 2
    Testing = 3
    Unknown = 4
    Dormant = 5
    NotPresent = 6
    LowerLayerDown = 7

# System.Net.NetworkInformation.PrefixOrigin
class PrefixOrigin(IntFlag):
    Other = 0
    Manual = 1
    WellKnown = 2
    Dhcp = 3
    RouterAdvertisement = 4

# System.Net.NetworkInformation.SuffixOrigin
class SuffixOrigin(IntFlag):
    Other = 0
    Manual = 1
    WellKnown = 2
    OriginDhcp = 3
    LinkLayerAddress = 4
    Random = 5


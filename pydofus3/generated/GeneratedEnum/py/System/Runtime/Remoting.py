from enum import IntFlag

# System.Runtime.Remoting.CustomErrorsModes
class CustomErrorsModes(IntFlag):
    On = 0
    Off = 1
    RemoteOnly = 2

# System.Runtime.Remoting.WellKnownObjectMode
class WellKnownObjectMode(IntFlag):
    Singleton = 1
    SingleCall = 2


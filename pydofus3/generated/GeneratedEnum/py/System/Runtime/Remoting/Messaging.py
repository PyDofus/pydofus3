from enum import IntFlag

# System.Runtime.Remoting.Messaging.ArgInfoType
class ArgInfoType(IntFlag):
    In = 0
    Out = 1

# System.Runtime.Remoting.Messaging.CallType
class CallType(IntFlag):
    Sync = 0
    BeginInvoke = 1
    EndInvoke = 2
    OneWay = 3


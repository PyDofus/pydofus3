from enum import IntFlag

# System.Runtime.Remoting.Lifetime.LeaseState
class LeaseState(IntFlag):
    Null = 0
    Initial = 1
    Active = 2
    Renewing = 3
    Expired = 4


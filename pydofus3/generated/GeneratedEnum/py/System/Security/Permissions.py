from enum import IntFlag

# System.Security.Permissions.PermissionState
class PermissionState(IntFlag):
    NONE = 0
    Unrestricted = 1

# System.Security.Permissions.SecurityAction
class SecurityAction(IntFlag):
    Demand = 2
    Assert = 3
    Deny = 4
    PermitOnly = 5
    LinkDemand = 6
    InheritanceDemand = 7
    RequestMinimum = 8
    RequestOptional = 9
    RequestRefuse = 10


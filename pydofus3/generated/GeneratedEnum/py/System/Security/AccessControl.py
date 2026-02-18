from enum import IntFlag

# System.Security.AccessControl.AccessControlModification
class AccessControlModification(IntFlag):
    Add = 0
    Set = 1
    Reset = 2
    Remove = 3
    RemoveAll = 4
    RemoveSpecific = 5

# System.Security.AccessControl.AccessControlSections
class AccessControlSections(IntFlag):
    NONE = 0
    Audit = 1
    Access = 2
    Owner = 4
    Group = 8
    All = 15

# System.Security.AccessControl.AccessControlType
class AccessControlType(IntFlag):
    Allow = 0
    Deny = 1

# System.Security.AccessControl.AceFlags
class AceFlags(IntFlag):
    NONE = 0
    ObjectInherit = 1
    ContainerInherit = 2
    NoPropagateInherit = 4
    InheritOnly = 8
    InheritanceFlags = 15
    Inherited = 16
    SuccessfulAccess = 64
    FailedAccess = 128
    AuditFlags = 192

# System.Security.AccessControl.AceQualifier
class AceQualifier(IntFlag):
    AccessAllowed = 0
    AccessDenied = 1
    SystemAudit = 2
    SystemAlarm = 3

# System.Security.AccessControl.AceType
class AceType(IntFlag):
    AccessAllowed = 0
    AccessDenied = 1
    SystemAudit = 2
    SystemAlarm = 3
    AccessAllowedCompound = 4
    AccessAllowedObject = 5
    AccessDeniedObject = 6
    SystemAuditObject = 7
    SystemAlarmObject = 8
    AccessAllowedCallback = 9
    AccessDeniedCallback = 10
    AccessAllowedCallbackObject = 11
    AccessDeniedCallbackObject = 12
    SystemAuditCallback = 13
    SystemAlarmCallback = 14
    SystemAuditCallbackObject = 15
    SystemAlarmCallbackObject = 16
    MaxDefinedAceType = 16

# System.Security.AccessControl.AuditFlags
class AuditFlags(IntFlag):
    NONE = 0
    Success = 1
    Failure = 2

# System.Security.AccessControl.ControlFlags
class ControlFlags(IntFlag):
    NONE = 0
    OwnerDefaulted = 1
    GroupDefaulted = 2
    DiscretionaryAclPresent = 4
    DiscretionaryAclDefaulted = 8
    SystemAclPresent = 16
    SystemAclDefaulted = 32
    DiscretionaryAclUntrusted = 64
    ServerSecurity = 128
    DiscretionaryAclAutoInheritRequired = 256
    SystemAclAutoInheritRequired = 512
    DiscretionaryAclAutoInherited = 1024
    SystemAclAutoInherited = 2048
    DiscretionaryAclProtected = 4096
    SystemAclProtected = 8192
    RMControlValid = 16384
    SelfRelative = 32768

# System.Security.AccessControl.InheritanceFlags
class InheritanceFlags(IntFlag):
    NONE = 0
    ContainerInherit = 1
    ObjectInherit = 2

# System.Security.AccessControl.ObjectAceFlags
class ObjectAceFlags(IntFlag):
    NONE = 0
    ObjectAceTypePresent = 1
    InheritedObjectAceTypePresent = 2

# System.Security.AccessControl.PropagationFlags
class PropagationFlags(IntFlag):
    NONE = 0
    NoPropagateInherit = 1
    InheritOnly = 2

# System.Security.AccessControl.ResourceType
class ResourceType(IntFlag):
    Unknown = 0
    FileObject = 1
    Service = 2
    Printer = 3
    RegistryKey = 4
    LMShare = 5
    KernelObject = 6
    WindowObject = 7
    DSObject = 8
    DSObjectAll = 9
    ProviderDefined = 10
    WmiGuidObject = 11
    RegistryWow6432Key = 12

# System.Security.AccessControl.SecurityInfos
class SecurityInfos(IntFlag):
    Owner = 1
    Group = 2
    DiscretionaryAcl = 4
    SystemAcl = 8


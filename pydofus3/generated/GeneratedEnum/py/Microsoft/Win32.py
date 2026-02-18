from enum import IntFlag

# Microsoft.Win32.RegistryHive
class RegistryHive(IntFlag):
    ClassesRoot = -2147483648
    CurrentUser = -2147483647
    LocalMachine = -2147483646
    Users = -2147483645
    PerformanceData = -2147483644
    CurrentConfig = -2147483643
    DynData = -2147483642

# Microsoft.Win32.RegistryKey
class RegistryKey(IntFlag):
    Dirty = 1
    SystemKey = 2
    WriteAccess = 4
    PerfData = 8

# Microsoft.Win32.RegistryKeyPermissionCheck
class RegistryKeyPermissionCheck(IntFlag):
    Default = 0
    ReadSubTree = 1
    ReadWriteSubTree = 2

# Microsoft.Win32.RegistryValueOptions
class RegistryValueOptions(IntFlag):
    NONE = 0
    DoNotExpandEnvironmentNames = 1

# Microsoft.Win32.RegistryView
class RegistryView(IntFlag):
    Default = 0
    Registry64 = 256
    Registry32 = 512


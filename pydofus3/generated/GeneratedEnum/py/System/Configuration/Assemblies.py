from enum import IntFlag

# System.Configuration.Assemblies.AssemblyHashAlgorithm
class AssemblyHashAlgorithm(IntFlag):
    NONE = 0
    MD5 = 32771
    SHA1 = 32772
    SHA256 = 32780
    SHA384 = 32781
    SHA512 = 32782

# System.Configuration.Assemblies.AssemblyVersionCompatibility
class AssemblyVersionCompatibility(IntFlag):
    SameMachine = 1
    SameProcess = 2
    SameDomain = 3


from enum import IntFlag

# UnityEngine.ResourceManagement.AsyncOperations.AsyncOperationStatus
class AsyncOperationStatus(IntFlag):
    NONE = 0
    Succeeded = 1
    Failed = 2

# UnityEngine.ResourceManagement.AsyncOperations.GroupOperation
class GroupOperation(IntFlag):
    NONE = 0
    ReleaseDependenciesOnFailure = 1
    AllowFailedDependencies = 2


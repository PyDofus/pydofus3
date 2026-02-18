from enum import IntFlag

# UnityEngine.ResourceManagement.ResourceManager
class ResourceManager(IntFlag):
    AsyncOperationFail = 0
    AsyncOperationCreate = 1
    AsyncOperationPercentComplete = 2
    AsyncOperationComplete = 3
    AsyncOperationReferenceCount = 4
    AsyncOperationDestroy = 5


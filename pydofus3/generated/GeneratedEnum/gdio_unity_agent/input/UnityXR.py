from enum import IntEnum
from enum import IntFlag

class GDIOBlittableArrayWrapper:
	class UpdateFlags(IntEnum):
		NoUpdateNeeded = 0
		SizeChanged = 1
		DataIsNativePointer = 2
		DataIsNativeOwnedMemory = 3
		DataIsEmpty = 4
		DataIsNull = 5

class UnityXRSupport:
	class UpdateSuccessFlags(IntFlag):
		None_ = 0
		LeftHandRootPose = 1
		LeftHandJoints = 2
		RightHandRootPose = 4
		RightHandJoints = 8
		All = 15

	class XRDetectedHandMeshLayout(IntEnum):
		Unknown = 0
		OpenXRMetaQuest = 1
		OpenXRAndroidXR = 2


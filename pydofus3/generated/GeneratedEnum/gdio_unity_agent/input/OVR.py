from enum import IntEnum
from enum import IntFlag

class OVRSupport:
	class ESupSystemHeadset(IntEnum):
		None_ = 0
		Oculus_Quest = 8
		Oculus_Quest_2 = 9
		Meta_Quest_Pro = 10
		Meta_Quest_3 = 11
		Placeholder_12 = 12
		Placeholder_13 = 13
		Placeholder_14 = 14
		Rift_DK1 = 4096
		Rift_DK2 = 4097
		Rift_CV1 = 4098
		Rift_CB = 4099
		Rift_S = 4100
		Oculus_Link_Quest = 4101
		Oculus_Link_Quest_2 = 4102
		Meta_Link_Quest_Pro = 4103
		Meta_Link_Quest_3 = 4104
		PC_Placeholder_4105 = 4105
		PC_Placeholder_4106 = 4106
		PC_Placeholder_4107 = 4107

	class ESupResult(IntEnum):
		Failure_SpaceTooBright = -9006
		Failure_SpaceTooDark = -9005
		Failure_SpaceRateLimited = -9004
		Failure_SpacePermissionInsufficient = -9003
		Failure_SpaceInsufficientView = -9002
		Failure_SpaceStorageAtCapacity = -9001
		Failure_SpaceInsufficientResources = -9000
		Failure_SpaceComponentStatusAlreadySet = -2008
		Failure_SpaceComponentStatusPending = -2007
		Failure_SpaceComponentNotEnabled = -2006
		Failure_SpaceComponentNotSupported = -2005
		Failure_SpaceNetworkRequestFailed = -2004
		Failure_SpaceNetworkTimeout = -2003
		Failure_SpaceLocalizationFailed = -2002
		Failure_SpaceMappingInsufficient = -2001
		Failure_SpaceCloudStorageDisabled = -2000
		Failure_HandleInvalid = -1013
		Failure_RuntimeUnavailable = -1012
		Failure_ErrorInitializationFailed = -1011
		Failure_ErrorLimitReached = -1010
		Failure_DeprecatedOperation = -1009
		Failure_DataIsInvalid = -1008
		Failure_InsufficientSize = -1007
		Failure_OperationFailed = -1006
		Failure_NotYetImplemented = -1005
		Failure_Unsupported = -1004
		Failure_InvalidOperation = -1003
		Failure_NotInitialized = -1002
		Failure_InvalidParameter = -1001
		Failure = -1000
		Success = 0
		Success_EventUnavailable = 1
		Success_Pending = 2
		Warning_BoundaryVisibilitySuppressionNotAllowed = 9030

	class ESupVirtualKeyboardLocationType(IntEnum):
		Custom = 0
		Far = 1
		Direct = 2

	class ESupTrackingOrigin(IntEnum):
		EyeLevel = 0
		FloorLevel = 1
		Stage = 2
		View = 4
		Count = 5

	class ESupController(IntEnum):
		All = -1
		None_ = 0
		LTouch = 1
		RTouch = 2
		Touch = 3
		Remote = 4
		Gamepad = 16
		LHand = 32
		RHand = 64
		Hands = 96
		Active = 2147483647

	class ESupButton(IntFlag):
		Any = -1
		None_ = 0
		A = 1
		B = 2
		RThumbstick = 4
		RShoulder = 8
		LThumbstickUp = 16
		LThumbstickDown = 32
		LThumbstickLeft = 64
		LThumbstickRight = 128
		X = 256
		Y = 512
		LThumbstick = 1024
		LShoulder = 2048
		RThumbstickUp = 4096
		RThumbstickDown = 8192
		RThumbstickLeft = 16384
		RThumbstickRight = 32768
		DpadUp = 65536
		DpadDown = 131072
		DpadLeft = 262144
		DpadRight = 524288
		Start = 1048576
		Back = 2097152
		RIndexTrigger = 67108864
		RHandTrigger = 134217728
		LIndexTrigger = 268435456
		LHandTrigger = 536870912
		LTouchpad = 1073741824
		RTouchpad = 2147483647

	class ESupRawNearTouch(IntFlag):
		Any = -1
		None_ = 0
		LIndexTrigger = 1
		LThumbButtons = 2
		RIndexTrigger = 4
		RThumbButtons = 8

	class ESupRawTouch(IntFlag):
		Any = -1
		None_ = 0
		A = 1
		B = 2
		RThumbstick = 4
		RThumbRest = 8
		RIndexTrigger = 16
		X = 256
		Y = 512
		LThumbstick = 1024
		LThumbRest = 2048
		LIndexTrigger = 4096
		LTouchpad = 1073741824
		RTouchpad = 2147483647

	class ESupStep(IntEnum):
		Render = -1
		Physics = 0

	class ESupNode(IntEnum):
		None_ = -1
		EyeLeft = 0
		EyeRight = 1
		EyeCenter = 2
		HandLeft = 3
		HandRight = 4
		TrackerZero = 5
		TrackerOne = 6
		TrackerTwo = 7
		TrackerThree = 8
		Head = 9
		DeviceObjectZero = 10
		TrackedKeyboard = 11
		ControllerLeft = 12
		ControllerRight = 13
		Count = 14

	class ESupHandStatus(IntFlag):
		HandTracked = 1
		InputStateValid = 2
		SystemGestureInProgress = 64
		DominantHand = 128
		MenuPressed = 256

	class ESupTrackingConfidence(IntEnum):
		Low = 0
		High = 1065353216

	class ESupHandFingerPinch(IntEnum):
		Thumb = 1
		Index = 2
		Middle = 4
		Ring = 8
		Pinky = 16

	class ESupMeshType(IntEnum):
		None_ = -1
		HandLeft = 0
		HandRight = 1

	class ESupBoundaryVisibility(IntEnum):
		NotSuppressed = 1
		Suppressed = 2

	class ESupTrackedKeyboardFlags(IntEnum):
		Exists = 1
		Local = 2
		Remote = 4
		Connected = 8

	class ESupTrackedKeyboardPresentationStyles(IntEnum):
		Unknown = 0
		Opaque = 1
		MR = 2

	class ESupTrackedKeyboardQueryFlags(IntEnum):
		Local = 2
		Remote = 4

	class ESupRenderModelFlags(IntFlag):
		SupportsGltf20Subset1 = 1
		SupportsGltf20Subset2 = 2

	class ESupOverlayShape(IntEnum):
		Quad = 0
		Cylinder = 1
		Cubemap = 2
		OffcenterCubemap = 4
		Equirect = 5
		ReconstructionPassthrough = 7
		SurfaceProjectedPassthrough = 8
		Fisheye = 9
		KeyboardHandsPassthrough = 10
		KeyboardMaskedHandsPassthrough = 11

	class ESupLayerLayout(IntEnum):
		Stereo = 0
		Mono = 1
		DoubleWide = 2
		Array = 3
		EnumSize = 15

	class ESupEyeTextureFormat(IntEnum):
		Default = 0
		R8G8B8A8_sRGB = 0
		R8G8B8A8 = 1
		R16G16B16A16_FP = 2
		R11G11B10_FP = 3
		B8G8R8A8_sRGB = 4
		B8G8R8A8 = 5
		R5G6B5 = 11
		EnumSize = 2147483647


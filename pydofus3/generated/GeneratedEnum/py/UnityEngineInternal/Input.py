from enum import IntFlag

# UnityEngineInternal.Input.NativeInputEventType
class NativeInputEventType(IntFlag):
    DeviceRemoved = 1146242381
    DeviceConfigChanged = 1145259591
    Text = 1413830740
    State = 1398030676
    Delta = 1145852993

# UnityEngineInternal.Input.NativeInputUpdateType
class NativeInputUpdateType(IntFlag):
    Dynamic = 1
    Fixed = 2
    BeforeRender = 4
    Editor = 8
    IgnoreFocus = -2147483648


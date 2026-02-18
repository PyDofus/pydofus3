from enum import IntFlag

# UnityEngine.Windows.WebCam.CapturePixelFormat
class CapturePixelFormat(IntFlag):
    BGRA32 = 0
    NV12 = 1
    JPEG = 2
    PNG = 3

# UnityEngine.Windows.WebCam.PhotoCapture
class PhotoCapture(IntFlag):
    Success = 0
    UnknownError = 1

# UnityEngine.Windows.WebCam.VideoCapture
class VideoCapture(IntFlag):
    Success = 0
    UnknownError = 1


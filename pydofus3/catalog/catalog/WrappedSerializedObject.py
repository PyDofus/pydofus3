from dataclasses import dataclass

from ..classes import AssetBundleRequestOptions
from .SerializedType import SerializedType


@dataclass
class WrappedSerializedObject:
    Type: SerializedType
    Object: AssetBundleRequestOptions

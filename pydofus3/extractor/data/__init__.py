import warnings

import UnityPy
from UnityPy.config import UnityVersionFallbackWarning

from pydofus3.config import settings
from pydofus3.tools import set_unity_version

warnings.simplefilter('ignore', UnityVersionFallbackWarning)

if UnityPy.config.FALLBACK_UNITY_VERSION is None:
    set_unity_version(settings.game_path)

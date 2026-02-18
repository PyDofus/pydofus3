from functools import wraps

from pydantic import BaseModel, model_validator
from pydofus3.config import check_game_path, settings
from pydofus3.enum_data import TypeDataOther
from pydofus3.extractor.i18n import read

i18n_dict: dict[int, 'i18n'] = {}


class i18n(BaseModel):
    fr: str
    en: str
    de: str
    es: str
    pt: str
    id: int

    @model_validator(mode='before')
    def set_i18n(cls, data):
        if isinstance(data, dict):
            return data
        else:
            key = data if isinstance(data, int) else (int(data) if data else -1)
            if (i18n_data := i18n_dict.get(key)) is None:
                val = f'UNKNOWN_TEXT_ID_{data}'
                i18n_data = {'fr': val, 'en': val, 'de': val, 'es': val, 'pt': val, 'id': key}
            return i18n_data


@check_game_path
def _load_i18n():
    global i18n_dict
    if not i18n_dict:
        i18n_dict = read(settings.game_path / TypeDataOther.I18n)


def check_i18n(f):
    """
    decorator to check if i18n dict is set
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        _load_i18n()
        return f(*args, **kwargs)

    return decorated


def release_i18n():
    global i18n_dict
    i18n_dict.clear()

from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    JsonConfigSettingsSource,
    )

CONFIG_PATH = Path(__file__).parent / "conf.json"


class ManyData(BaseModel):
    key_id_table1: str = "id"
    key_id_table2: str = "id"
    table2: str
    key_sup: list[str] = []
    split: list[str] = []


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(json_file=CONFIG_PATH, json_file_encoding="utf-8")

    relation: dict[str, dict[str, str]]
    relation_many_many: dict[str, dict[str, ManyData]]

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
            ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (JsonConfigSettingsSource(settings_cls),)


db_settings = DBSettings()

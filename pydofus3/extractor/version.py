from pathlib import Path
from pydantic import BaseModel, field_validator
from datetime import datetime
from pydofus3.enum_data import get_data_path, TypeData

class GameVersion(BaseModel):
    Version: str
    beta: bool = False
    BuildDate: int

    @field_validator("BuildDate", mode="before")
    @classmethod
    def parse_build_date(cls, v):
        return datetime.fromisoformat(v).timestamp() if isinstance(v, str) else v

    @staticmethod
    def load_game_version(game_path: Path) ->  GameVersion:
        version_path = get_data_path(game_path, TypeData.aa).parent / 'version'
        data = {}
        for line in version_path.read_text().splitlines():
            key, sep, value = line.partition('=')
            if sep:
                data[key] = value.strip()
            data['beta'] = data.get('ConfigUrl', '').endswith('beta.json')
        return GameVersion.model_validate(data, extra="ignore")

    @classmethod
    def export(cls,game_path:Path, output:Path)-> None:
        version = cls.load_game_version(game_path)
        output.write_text(version.model_dump_json())

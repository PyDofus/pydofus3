from functools import wraps, cached_property
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

from pydofus3.extractor.version import GameVersion


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='allow', env_file_encoding='utf-8')

    game_path: None | Path = None
    extract_dir: None | Path = None
    unity_fallback_version: str = '6000.1.2f1'
    db_user: None | str = 'test'
    db_password: None | str = 'test123'
    db_name: None | str = "dofus"
    db_host: str = 'localhost'
    db_port: int = 5432
    db_connector: str = "psycopg"
    db_type: str = "postgresql"

    @property
    def db_uri(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme=f"{self.db_type}+{self.db_connector}",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_name,
            )

    @cached_property
    def version(self) -> GameVersion|None:
        if self.game_path:
            return GameVersion.load_game_version(self.game_path)
        return None

settings = Settings()


def check_game_path(f):
    """
    Decorator to check if game path data is set and exists
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        if not (isinstance(settings.game_path, Path) and settings.game_path.exists()):
            raise RuntimeError(
                'GAME_PATH_DATA is None or does not exist. You must set it in pydofus3.config or via the environment variable EXTRACT_DIR'
                )
        return f(*args, **kwargs)

    return decorated


def check_extract_dir(f):
    """
    Decorator to check if extract_dir is set and exists
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        if not (isinstance(settings.extract_dir, Path) and settings.extract_dir.exists()):
            raise RuntimeError(
                'EXTRACT_DIR is None or does not exist. You must set it in pydofus3.config or via the environment variable EXTRACT_DIR'
                )
        return f(*args, **kwargs)

    return decorated

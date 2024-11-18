from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Config(BaseSettings):
    database_url: PostgresDsn | str
    access_token_expire: int
    refresh_token_expire: int
    algorithm: str
    jwt_secret_key: str
    jwt_refresh_secret_key: str

    class Config:
        env_file = ".env"


def get_config():
    return Config()


config = get_config()

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    DATABASE_URL: str = 'mongodb://localhost:27017/'
    DATABASE_NAME: str = 'local'

    model_config = SettingsConfigDict(env_file='.env')
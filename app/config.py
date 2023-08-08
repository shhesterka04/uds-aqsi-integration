from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    UDS_ID: str
    UDS_KEY: str
    ASQI_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
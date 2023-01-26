from pydantic import BaseSettings
import configuration.defaults as defaults


class Settings(BaseSettings):
    POSTGRES_HOST: str = defaults.POSTGRES_HOST
    POSTGRES_PORT: int = defaults.POSTGRES_PORT
    POSTGRES_USER: str = defaults.POSTGRES_USER
    POSTGRES_PASSWORD: str = defaults.POSTGRES_PASSWORD
    POSTGRES_DB: str = defaults.POSTGRES_DB
    SQLALCHEMY_DB_URL: str = defaults.SQLALCHEMY_DB_URL
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


settings = Settings()

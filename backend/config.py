from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_ROOT_USER: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_HOSTNAME: str
    DATABASE_PORT: str
    MYSQL_DATABASE: str
    class Config:
        env_file = "./.env"
        env_file_encoding = 'utf-8'

settings = Settings()
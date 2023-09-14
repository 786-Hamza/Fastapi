from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT = 6500
    POSTGRES_PASSWORD = password123
    POSTGRES_USER = postgres
    POSTGRES_DB = fastapi
    POSTGRES_HOST = postgres
    POSTGRES_HOSTNAME = "127.0.0.1"


    env_file = './.env'


settings = Settings()


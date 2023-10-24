from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str = 'redis'
    REDIS_PORT: int = 7777

    class Config:
        env_file = find_dotenv('.env')
        env_file_encoding = "utf-8"


settings = Settings()
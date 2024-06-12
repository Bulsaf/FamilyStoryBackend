from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn
from dotenv import load_dotenv
import os
load_dotenv()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: str = os.getenv('DATABASE_URL')
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings:
    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()
    api: ApiPrefix = ApiPrefix()

settings = Settings()
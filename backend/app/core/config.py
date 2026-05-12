from pydantic_settings import BaseSettings
import os 
from pathlib import Path






class Settings(BaseSettings):
    APP_NAME : str
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    class Config:
        env_file = ".env"
        env_file_config = "utf-8"



settings = Settings()

from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://user:pass@localhost/db'
    REDIS_URL: str = 'redis://localhost:6379'
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        

settings = Settings()

import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
      env_file = ".env"
      
    app_name: str = "FastAPI Demo"
    admin_email: str = "sirayhancs@gmail.com"
    secret_key: str = os.getenv("SECRET_KEY")
    hash_algo: str = os.getenv("HASH_ALGO", "HS256")
    access_token_expiration: int = os.getenv("ACCESS_TOKEN_EXPIRATION", 86400)


settings = Settings()

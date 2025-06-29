import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV_PATH = os.path.join(os.path.dirname(BASE_DIR), ".env")
load_dotenv(ENV_PATH)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = os.environ.get("ENV", "DEV")
    SITE_DOMAIN: str = "codeground"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 14
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "")
    SECRET_KEY_AUTH: str = os.environ.get("SECRET_KEY_AUTH", "")
    DB_HOST: str = os.environ.get("DB_HOST", "")
    DB_USER: str = os.environ.get("DB_USER", "")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "")
    DB_NAME: str = os.environ.get("DB_NAME", "")
    DB_URL: str = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    ONLINE_JUDGE_HOST_ENDPOINT: str = os.environ.get("ONLINE_JUDGE_HOST_ENDPOINT", "")


settings = Settings()

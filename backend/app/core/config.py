import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Career OS"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///career_os.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "career_os_secret")
    ALGORITHM = "HS256"

settings = Settings()
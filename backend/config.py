import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Secret Key obligatoria
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY is not set in environment variables.")

    # JWT secret obligatoria
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    if not JWT_SECRET_KEY:
        raise RuntimeError("JWT_SECRET_KEY is not set in environment variables.")

    # Expiración y token location opcional (con defaults razonables)
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    JWT_TOKEN_LOCATION = os.getenv("JWT_TOKEN_LOCATION", "headers").split(',')

    # URI obligatoria
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("DATABASE_URL is not set in environment variables.")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
